# User access logging in Amazon WorkSpaces Secure Browser

Administrators are able to record WorkSpaces Secure Browser session events, including start, stop, and URL
visits. These logs are encrypted and securely delivered to customers through an Amazon Kinesis
Data Stream. Browsing information from user access logging is not stored by AWS, or
available from sessions without logging configured. URL visits in incognito mode, or deleted
URLs from browser history, are not recorded in user access logging.
