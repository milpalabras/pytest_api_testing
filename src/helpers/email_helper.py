import imaplib
import re
from email import policy
from email.parser import BytesParser
from datetime import datetime
from src.helpers.logging_helper import logHelper
from config import GMAI_IMAP_SERVER, GMAIL_USER, GMAIL_PASSWORD


class EmailHelper:
    def __init__(self):
        self.logger = logHelper().get_logger(__name__)
        self.email_adress = GMAIL_USER
        self.password = GMAIL_PASSWORD
        self.imap_server = GMAI_IMAP_SERVER

    def connect(self):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_adress, self.password)
        mail.select("inbox")
        return mail

    def get_email(self, subject, date):
        """
        Obtiene el email con el asunto y fecha especificada
        @param subject: Asunto del email
        @param date: Fecha del email en formato "YYYY-MM-DD HH:MM:SS+00:00"
        @example get_email("Nueva contraseña", "2024-03-13 14:32:52-03:00")
        """
        mail = self.connect()
        try:
            self.logger.info(f"Buscando email con asunto {subject} y fecha {date}")
            mail.literal = subject.encode("utf-8")
            result, data = mail.uid("SEARCH", "CHARSET", "UTF-8", "SUBJECT")
        except Exception as e:
            self.logger.error(f"Error al buscar el email: {e}")
            mail.close()
            mail.logout()
            return None

        if result == "OK":
            self.logger.info(f"Email encontrado con asunto {subject} y fecha {date}")
            self.logger.info(f"Data: {data}")
            for num in data[0].split():
                result, data = mail.fetch(num, "(RFC822)")
                raw_email = data[0][1]
                msg = BytesParser(policy=policy.default).parsebytes(raw_email)
                email_date = datetime.strptime(msg["Date"], "%a, %d %b %Y %H:%M:%S %z")
                date_converted = datetime.strptime(date, "%Y-%m-%d %H:%M:%S%z")
                self.logger.info(f"Fecha del email {email_date} y fecha buscada {date_converted}")
                if email_date.date() == date_converted.date():
                    mail.close()
                    mail.logout()
                    self.logger.info(f"Email encontrado {msg}")
                    return msg
        mail.close()
        mail.logout()
        return None

    def get_email_by_subject_and_sender(self, subject, sender):
        """
        Obtiene el email con el asunto especificado
        @param subject: Asunto del email
        @param sender: Email del remitente
        @example get_email_by_subject_and_sender("Nueva contraseña", "ayuda_cotodigital@cotodigital.com.ar")
        """
        mail = self.connect()

        try:
            self.logger.info(f"Buscando email con asunto {subject} y enviado por {sender}")
            mail.literal = subject.encode("utf-8")
            result, data = mail.search("UTF-8", '(FROM "%s")' % sender, "SUBJECT")
        except Exception as e:
            self.logger.error(f"Error al buscar el email: {e}")
            mail.close()
            mail.logout()
            return None

        if result == "OK":
            self.logger.info(f"Email encontrado con asunto {subject} y enviado por {sender}")
            for num in data[0].split():
                type, data = mail.fetch(num, "(RFC822)")
                raw_email = data[0][1]
                msg = BytesParser(policy=policy.default).parsebytes(raw_email)
                mail.close()
                mail.logout()
                return msg


    def check_email(self, sender):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.email_adress, self.password)
        mail.select("inbox")
        result, data = mail.search(None, '(FROM "%s")' % sender)
        for num in data[0].split():
            type, data = mail.fetch(num, '(RFC822)')
            print ('Message %s\n%s\n' % (num, data[0][1]))
        mail.close()
        mail.logout()

    def delete_email_from_sender(self, sender):
        mail= self.connect()
        result, data = mail.search(None, '(FROM "%s")' % sender)
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Deleted')
        mail.expunge()
        mail.close()
        mail.logout()



    
