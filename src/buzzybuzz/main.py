from imap_tools import MailBox
from buzzybuzz.settings import settings

def main() -> None:
    with MailBox(settings.IMAP_HOST).login(
        username=settings.IMAP_USERNAME.get_secret_value(),
        password=settings.IMAP_PASSWORD.get_secret_value(),
        initial_folder="INBOX"
    ) as mailbox:
        for message in mailbox.fetch():
            print(message.subject)

if __name__ == "__main__":
    main()
