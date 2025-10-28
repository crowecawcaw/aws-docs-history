# Configuring personal access tokens

You can enable personal access token for Amazon WorkMail users to access their mailboxes using
desktop and mobile email clients. After IAM Identity Center is enabled, by default, the personal
access token status is set to active and is valid for 365 days. After enabling IAM Identity Center,
your users’ existing credentials will no longer be valid to log into their email
clients. Your users can generate the personal access token from the Amazon WorkMail web application
and use it to log into any email clients. You can edit the personal access token
expiration and when the token expires, your user can generate a new one.

###### Note

- Your user can only view and copy your personal access token once when you
  create them in Amazon WorkMail. If you lose your personal access token, you will need
  to generate a new one for security reasons.
- Amazon WorkMail only allows personal access tokens for mailbox access when the Amazon WorkMail
  user is associated with an IAM Identity Center user who is authorized to access the Amazon WorkMail
  application.
  The personal access token configurations are listed below:

- Active – When the personal access token status set to
  _Active_, your user can generate personal access token
  from Amazon WorkMail and use it to log in to any email client within the token's
  lifetime.
- Inactive – When the personal access token status is set to
  _Inactive_, your user will not be able to generate or use
  personal access tokens to access mailboxes.
- Token lifetime – By default, the personal access token is valid for
  365 days. You have the option to change the personal access token lifetime. When
  you leave the lifetime setting blank, the token will have an indefinite lifetime
  and never expire.

###### To configure personal access tokens, follow these steps.

1. Under the **Identity Center Settings** page, choose the
   **Personal access token configuration** tab.
2. Choose **Edit**.

The **Edit personal token configuration** page
appears. 3. Under **Token status**, slide the **Active**
button to enable personal access token. 4. In the **Token lifetime (in days)** text box, enter the
number of days the personal access token can be activated. 5. Choose **Save**.
