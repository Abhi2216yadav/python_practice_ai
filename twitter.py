import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

# if matches:
#     print(f"Username:", matches.group(1))

