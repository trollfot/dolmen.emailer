from zope.interface import Interface


class IMailSender(Interface):
    """A mail sender definition.
    """

    def send(recipients, subject, body, sender=None, **kwargs):
        """Send a mail to the given recipients.
        """
