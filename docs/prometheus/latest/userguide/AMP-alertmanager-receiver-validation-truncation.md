# Understanding

Amazon SNS message validation rules

Amazon Simple Notification Service (Amazon SNS) requires messages to meet certain standards. Messages that
don't meed these standards will be modified when they are received. The alert
messages will be validated, truncated, or modified, if necessary, by the Amazon SNS
receiver based on the following rules:

- Message contains non-utf characters.
  - Message will be replaced by **Error - not a valid
    UTF-8 encoded string**.
  - One message attribute will be added with the key of
    **truncated** and the value of
    **true**.
  - One message attribute will be added with the key of
    **modified** and the value of
    **Message: Error - not a valid UTF-8 encoded
    string**.

- Message is empty.
  - Message will be replaced by **Error - Message should
    not be empty**.
  - One message attribute will be added with the key of
    **modified** and the value of
    **Message: Error - Message should not be
    empty**.

- Message has been truncated.
  - Message will have the truncated content.
  - One message attribute will be added with the key of
    **truncated** and the value of
    **true**.
  - One message attribute will be added with the key of "modified"
    and the value of **Message: Error - Message has been
    truncated from `X` KB, because it
    exceeds the 256 KB size limit**.

- Subject contains control or non-ASCII characters.
  - If the subject contains control characters or non-ASCII
    characters, SNS replaces the subject with **Error -
    contains control- or non-ASCII characters**.
  - For SNS email subjects, remove control characters, such as
    newlines: `\n`.

- Subject is not ASCII.
  - Subject will be replaced by **Error - contains non
    printable ASCII characters**.
  - One message attribute will be added with the key of
    **modified** and the value of
    **Subject: Error - contains non-printable ASCII
    characters**.

- Subject has been truncated.
  - Subject will have the truncated content.
  - One message attribute will be added with the key of
    **modified** and the value of
    **Subject: Error - Subject has been truncated from
    `X` characters, because it
    exceeds the 100 character size limit**.

- Message attribute has invalid key/value.
  - Invalid message attribute will be removed.
  - One message attribute will be added with the key of
    **modified** and the value of
    **MessageAttribute: Error -
    `X` of the message attributes
    have been removed because of invalid MessageAttributeKey or
    MessageAttributeValue**.

- Message attribute has been truncated.
  - Extra message attributes will be removed.
  - One message attribute will be added with the key of
    **modified** and the value of
    **MessageAttribute: Error -
    `X` of the message attributes
    have been removed, because it exceeds the 256KB size
    limit**.
