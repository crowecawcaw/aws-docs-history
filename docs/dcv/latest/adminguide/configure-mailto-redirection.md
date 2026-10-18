

# Configure mailto: redirection
<a name="configure-mailto-redirection"></a>

To redirect email links, add `mailto:` patterns to the allow list. A `mailto:` pattern has the form `mailto:name@domain` and supports the same wildcards as URL patterns. For example, `mailto:*@example.com` matches every email address in the example.com domain. URL patterns don't match `mailto:` links.

A `mailto:` link opens in the email application on the local device only when:
+ Every recipient in the link, including the **To**, **Cc**, and **Bcc** recipients, matches a `mailto:` pattern in the allow list.
+ No recipient matches a `mailto:` pattern in the exception list.

Otherwise, including when the link has no recipients, the link opens in the email application in the session.

Amazon DCV matches only recipients against the patterns. Other fields in the link, such as the subject and body, are passed to the email application on the local device. Amazon DCV removes attachments from redirected links. Patterns are case-insensitive.