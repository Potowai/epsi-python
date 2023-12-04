with open('../index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Extract passwords from the JavaScript code
passwords = []
for line in html_content.split('\n'):
    if 'pwd' in line and '==' in line:
        password = line.split('==')[1].strip().replace(';', '').replace('"', '').replace(")", '')
        passwords.append(password)

# Display the extracted passwords
if passwords:
    print("Extracted Passwords:")
    for password in passwords:
        print(password)
else:
    print("No passwords found in the JavaScript code.")
