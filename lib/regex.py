import re

name = r"^[A-Z](?:[a-z]+|[A-Z][a-z]*)(?:[ '-][A-Z][a-z]+)*$"
name_regex = re.compile(name)

phone_number = r"^(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$"
phone_regex = re.compile(phone_number)

email_address = r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)