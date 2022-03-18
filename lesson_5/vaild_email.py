import re

email = "email@mail.com"
result = re.match(r"^([a-zA-Z09]{5,30})@(gmail|mail|yandex|icloud|namba).(com|ru|kg)", email)
print(result)
