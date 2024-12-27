# IMAP Email Fetcher and Parser

A Python script that connects to an IMAP email server, retrieves unseen emails based on specified criteria, and extracts specific information from the email body using regular expressions.

## Features
- Connects securely to an IMAP email server.
- Retrieves unseen emails matching specific sender and subject criteria.
- Parses email content to extract targeted information.
- Customizable for various email automation tasks.

## Requirements
- Python 3.6+
- `imapclient` library
- `email` module (standard library)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ShaadyEmad/IMAP-Email-Fetcher.git
   ```
   ```bash
   cd IMAP-Email-Fetcher
   ```

2. Install the required library:
   ```bash
   pip install imapclient
   ```

## Usage

1. Update the following variables in the script with your email credentials and server information:
   ```python
   email_account = "your_email@example.com"
   email_password = "your_password"
   server = "imap.your-email-provider.com"
   port = "port"
   ```

   Here are common IMAP server and port details for popular email providers:
   - Gmail:
     - Server: `imap.gmail.com`
     - Port: `993`
   - Yandex:
     - Server: `imap.yandex.com`
     - Port: `993`
   - Outlook:
     - Server: `outlook.office365.com`
     - Port: `993`

2. Customize the search criteria if needed. For example, change the sender email or subject:
   ```python
   messages = client.search([
       'UNSEEN',
       'FROM', 'sender@example.com',
       'SUBJECT', 'Specific Email Subject'
   ])
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## Example Output
If an email matching the criteria is found, the script will output:
- Total emails found
- Email sender
- Email subject
- Extracted content

Example:
```
Total emails found: 1
From: sender@example.com
Subject: Your Account Notification
Extracted Content: [Extracted Data Here]
```

## Customization
- Modify the `re.search` pattern to extract specific information from the email body based on your needs.
- Adjust the IMAP folder and search criteria to target different types of emails.

## Security Note
- Store your credentials securely and avoid hardcoding them in the script. Consider using environment variables or a secrets manager.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.

## Acknowledgments
Thanks to the Python community for providing excellent libraries like `imapclient` to simplify email automation tasks.
