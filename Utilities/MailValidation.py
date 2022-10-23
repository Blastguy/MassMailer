import re


def isGmailValid(mail):
    """
    It returns True if the string mail ends with @gmail.com, and False otherwise

    :param mail: The email address to be validated
    :return: A boolean value.
    """
    return re.search("^.*@gmail.com$", mail)


def isMailValid(mail):
    """
    It returns true if the mail is valid, false otherwise

    :param mail: The mail to be checked
    :return: A boolean value.
    """
    return re.search("([a-zA-Z]|[0-9])*@.([a-zA-Z]|[0-9])*\.([a-zA-Z]|[0-9])*", mail)


def getValidMails(mails):
    """
    It takes a list of emails and returns a list of valid emails

    :param mails: A list of emails
    :return: A list of valid emails
    """
    mailList = []
    for mail in mails:
        if isMailValid(mail):
            mailList.append(mail)
    return mailList
