# Authenticate with Amazon Location Service

To use Amazon Location Service, a user must be granted access to the resources and APIs that make up
Amazon Location. There are three strategies you can use to grant access to your resources:

- **API keys** – Grant read-only access to
  unauthenticated users for Maps, Places, and Routes APIs. API keys are the simplest
  option when you don't need to authenticate every user, such as a public web
  application. For more information, see [Use API keys to authenticate](using-apikeys.md "using-apikeys.md").
- **Amazon Cognito** – Grant anonymous or authenticated
  access to all Amazon Location Service APIs. With Amazon Cognito, you can define richer authorization
  policies, combine multiple authentication methods, and use your own sign-in
  flow. For more information, see [Use Amazon Cognito to authenticate](authenticating-using-cognito.md "authenticating-using-cognito.md").
- **AWS Identity and Access Management (IAM)** – Grant access to
  users authenticated with AWS IAM Identity Center or IAM. Use IAM for server-side
  applications, internal tools, and any scenario requiring full control over
  permissions. For more information, see [Use AWS Identity and Access Management to authenticate](security-iam.md "security-iam.md").
