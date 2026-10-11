

# Credentials by reference, never by value
<a name="dp-credentials"></a>

The catalog stores an AWS Secrets Manager ARN. The secret itself never enters the catalog record and never reaches the browser.

The detail view masks part of the ARN for display. To be precise about what that is: **the masking is a signal, not a control.** An ARN is catalog metadata, not a secret. It is masked so that an operator reading the page absorbs "credentials are referenced here, not stored here" without having to be told.