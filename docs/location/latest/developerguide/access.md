# Authenticate with Amazon Location Service

To use Amazon Location Service, a user must be granted access to the resources and APIs that make up
Amazon Location. There are three strategies you can use to grant access to your resources.

- **Use API keys** – To grant access to
  unauthenticated users, you can create API keys that give read-only access to your
  Amazon Location Service resources and actions. This is useful in a case where you don't want to
  authenticate every user. For example, a web application.

For more information about API keys, see [Use API keys to authenticate](using-apikeys.md "using-apikeys.md").

- **Use Amazon Cognito** – An alternative to API keys is
  to use Amazon Cognito to grant anonymous access. Amazon Cognito allows you to create a richer
  authorization with policy to define what can be done by the unauthenticated users.

For more information about using Amazon Cognito, see [Use Amazon Cognito to authenticate](authenticating-using-cognito.md "authenticating-using-cognito.md").

- **Use AWS Identity and Access Management (IAM)** – To grant access to
  users authenticated with AWS IAM Identity Center or AWS Identity and Access Management (IAM), create an IAM policy that
  allows access to the resources that you want.

For more information about IAM and Amazon Location, see [Use AWS Identity and Access Management to authenticate](security-iam.md "security-iam.md").
