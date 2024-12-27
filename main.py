from imapclient import IMAPClient
import email
from email.header import decode_header
import re


def fetch_email_content(email_account, email_password, server, port):
    try:
        with IMAPClient(host=server, port=port, ssl=True) as client:
            client.login(email_account, email_password)
            client.select_folder('INBOX')

            # Search for unseen emails with specific sender and subject
            messages = client.search([
                'UNSEEN',  # Use 'SEEN' instead to fetch emails that have already been read
                'FROM', 'sender@example.com',  # Replace with desired sender
                'SUBJECT', 'Specific Email Subject'  # Replace with desired subject
            ])
            print(f"Total emails found: {len(messages)}")
            if not messages:
                return None

            # Fetch the latest email
            msg_id = messages[-1]
            msg_data = client.fetch(msg_id, ['ENVELOPE', 'RFC822'])
            envelope = msg_data[msg_id][b'ENVELOPE']
            print("From:", envelope.from_)
            print("Subject:", envelope.subject.decode('utf-8'))

            # Fetch email content
            msg_bytes = msg_data[msg_id][b'RFC822']
            msg = email.message_from_bytes(msg_bytes)
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        email_body = part.get_payload(decode=True).decode()
                        print("Email Body:", email_body)

                        # Extract desired information using regex
                        match = re.search(r'access your account:(.*?)If this wasn\'t you', email_body, re.DOTALL)
                        if match:
                            return match.group(1).strip()

        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    email_account = "your_email@example.com"  # Replace with your email
    email_password = "your_password"  # Replace with your password
    server = "imap.gmail.com"  # Replace with IMAP server
    port = 993  # Replace with IMAP port

    content = fetch_email_content(email_account, email_password, server, port)
    if content:
        print("Extracted Content:", content)
    else:
        print("No content found or an error occurred.")
