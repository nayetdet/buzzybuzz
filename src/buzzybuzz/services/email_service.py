from typing import Iterator
from imap_tools import MailBox, MailMessage, AND
from buzzybuzz.settings import settings

class EmailService:
    @staticmethod
    def iterate() -> Iterator[MailMessage]:
        with MailBox(settings.IMAP_HOST).login(
            username=settings.IMAP_USERNAME.get_secret_value(),
            password=settings.IMAP_PASSWORD.get_secret_value(),
            initial_folder="INBOX"
        ) as mailbox:
            for message in mailbox.fetch(AND(seen=False)):
                yield message
