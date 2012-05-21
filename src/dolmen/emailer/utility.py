# -*- coding: utf-8 -*-

import grokcore.component as grok
import email.MIMEText, email.Header

from zope.component import queryUtility, getUtility
from zope.sendmail.interfaces import IMailDelivery

from .interfaces import IMailSender


class MailSender(grok.GlobalUtility):
    grok.baseclass()
    grok.implements(IMailSender)

    mailer_name = u"dolmen.mailer"
    admin_email = u"service@mysite.com"

    def send(self, recipients, subject, body, sender=None, **kwargs):

        if kwargs:
            raise ValueError('unsupported arguments %r' % kwargs)

        if sender is None:
            sender = self.admin_email

        mailer = getUtility(IMailDelivery, self.mailer_name)
        msg = email.MIMEText.MIMEText(body.encode('UTF-8'), 'plain', 'UTF-8')
        msg["Subject"] = email.Header.Header(subject, 'UTF-8')
        msg["From"] = sender

        for recipient in recipients:
            msg["To"] = recipient
            mailer.send(sender, [recipient], msg.as_string())


def get_sender(name=u''):
    return queryUtility(IMailSender, name=name)
