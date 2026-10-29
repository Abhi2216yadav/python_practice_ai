import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv(Path(__file__).with_name(".env"))

st.set_page_config(page_title="Recipe Studio", page_icon="🍲", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap');

    .stApp {
        background: radial-gradient(ellipse at 8% 0%, #eaf4e9 0, transparent 34%),
                    linear-gradient(145deg, #fbfcf8 0%, #f4f7f1 100%);
        color: #23342a;
        font-family: 'DM Sans', sans-serif;
    }
    h1, h2, h3 { font-family: 'Fraunces', Georgia, serif !important; color: #183d2b; }
    h1 { font-size: 3rem !important; margin-bottom: .15rem !important; }
    [data-testid="stForm"] {
        border: 1px solid #d9e4d8;
        border-radius: 8px;
        background: rgba(255, 255, 255, .78);
        padding: 1.4rem 1.5rem 1rem;
    }
    [data-testid="stBaseButton-primary"] {
        background: #bd4c35;
        border-color: #bd4c35;
        color: white;
        font-weight: 700;
    }
    [data-testid="stBaseButton-primary"]:hover {
        background: #a83f2c;
        border-color: #a83f2c;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Recipe Studio")
st.write("Start with what's in your kitchen. Gemini will help turn it into dinner.")


def build_prompt(
    ingredients: str,
    cuisine: str,
    dietary_needs: list[str],
    servings: int,
    minutes: int,
    experience: str,
    extra_requests: str,
) -> str:
    dietary_text = ", ".join(dietary_needs) if dietary_needs else "none"
    extra_text = extra_requests.strip() or "none"
    return f"""Make one quick, practical recipe from: {ingredients.strip()}.
Cuisine: {cuisine}. Dietary needs: {dietary_text}. Servings: {servings}.
Time limit: {minutes} minutes. Skill: {experience}. Extra: {extra_text}.
Keep the answer concise: title, time, ingredients with amounts, and 4-6 short steps.
Use common pantry items only. Include a safe cooking temperature if using meat."""


with st.form("recipe_form"):
    ingredients_column, preferences_column = st.columns([1.15, 0.85], gap="large")

    with ingredients_column:
        st.subheader("What do you have?")
        ingredients = st.text_area(
            "Ingredients",
            placeholder="e.g. chickpeas, spinach, coconut milk, onion, lemon",
            height=145,
            label_visibility="collapsed",
        )
        cuisine = st.selectbox(
            "Cuisine or flavor direction",
            ["Surprise me", "Italian", "Mexican", "Indian", "Japanese", "Mediterranean", "Comfort food", "Other"],
        )
        extra_requests = st.text_input(
            "Anything else?",
            placeholder="Use one pan, make it spicy, avoid food waste...",
        )

    with preferences_column:
        st.subheader("Make it yours")
        dietary_needs = st.multiselect(
            "Dietary needs",
            ["Vegetarian", "Vegan", "Gluten-free", "Dairy-free", "Nut-free", "High-protein"],
        )
        servings = st.number_input("Servings", min_value=1, max_value=12, value=2)
        minutes = st.slider("Time available", min_value=15, max_value=120, value=35, step=5, format="%d min")
        experience = st.select_slider(
            "Cooking comfort",
            options=["New to cooking", "Comfortable", "Experienced"],
            value="Comfortable",
        )

    submitted = st.form_submit_button("Generate my recipe", type="primary", use_container_width=True)

if submitted:
    if not ingredients.strip():
        st.warning("Add at least one ingredient to get started.")
    else:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("Gemini API key not found. Add GEMINI_API_KEY to Call_LLM/.env and try again.")
        else:
            prompt = build_prompt(
                ingredients,
                cuisine,
                dietary_needs,
                int(servings),
                minutes,
                experience,
                extra_requests,
            )
            model = "gemini-3.8-flash"
            try:
                client = genai.Client(
                    api_key=api_key,
                    http_options=genai.types.HttpOptions(timeout=30_000),
                )
                st.divider()
                st.subheader("Your recipe")
                with st.spinner("Getting the first steps ready..."):
                    recipe = st.write_stream(
                        event.delta.text
                        for event in client.interactions.create(
                            model=model,
                            input=prompt,
                            stream=True,
                            generation_config={"max_output_tokens": 450},
                            timeout=30.0,
                        )
                        if event.event_type == "step.delta" and event.delta.type == "text"
                    )
                st.session_state["recipe_markdown"] = recipe
            except Exception as error:
                st.error(f"Gemini couldn't generate the recipe right now. Please try again. Details: {error}")

if st.session_state.get("recipe_markdown") and not submitted:
    st.divider()
    st.subheader("Your recipe")
    st.markdown(st.session_state["recipe_markdown"])