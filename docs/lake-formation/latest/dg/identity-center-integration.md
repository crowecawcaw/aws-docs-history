# Integrating IAM Identity Center

With AWS IAM Identity Center, you can connect to identity providers (IdPs) and centrally manage access
for users and groups across AWS analytics services. You can integrate identity providers
such as Okta, Ping, and Microsoft Entra ID (formerly Azure Active Directory) with IAM Identity Center for users in your organization to
access data using a single-sign on experience. IAM Identity Center also supports connecting additional
third-party identity providers.

For more information see, [Supported identity
providers](../../../singlesignon/latest/userguide/supported-idps.md "../../../singlesignon/latest/userguide/supported-idps.md") in the AWS IAM Identity Center User Guide.

You can configure AWS Lake Formation as an enabled application in IAM Identity Center, and data lake
administrators can grant fine-grained permissions to authorized users and groups on AWS Glue Data Catalog resources.

Users from your organization can sign in to any Identity Center enabled application using
your organization’s identity provider, and query datasets applying Lake Formation permissions. With this integration,
you can manage access to AWS services, without creating multiple IAM roles.

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

For limitations, see [IAM Identity Center integration limitations](identity-center-lf-notes.md "identity-center-lf-notes.md").

###### Topics

- [Prerequisites for IAM Identity Center integration with Lake Formation](prerequisites-identity-center.md "prerequisites-identity-center.md")
- [Connecting Lake Formation with IAM Identity Center](connect-lf-identity-center.md "connect-lf-identity-center.md")
- [Updating IAM Identity Center
  integration](update-lf-identity-center-connection.md "update-lf-identity-center-connection.md")
- [Deleting a Lake Formation connection with IAM Identity Center](delete-lf-identity-center-connection.md "delete-lf-identity-center-connection.md")
- [Granting permissions to users and groups](grant-permissions-sso.md "grant-permissions-sso.md")
- [Including IAM Identity Center user context in CloudTrail logs](identity-center-ct-logs.md "identity-center-ct-logs.md")
