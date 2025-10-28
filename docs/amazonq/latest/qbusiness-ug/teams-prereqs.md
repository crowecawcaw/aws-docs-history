# Prerequisites for connecting Amazon Q Business to Microsoft Teams

Before you begin, make sure that you have completed the following
prerequisites.

**In Microsoft Teams, make sure you
have:**

- Created a Microsoft Teams account in Office 365.
- Copied your Microsoft 365 Tenant ID. You can find your Tenant
  ID in the Properties of your Azure Active Directory Portal. You need this URL to
  allow Amazon Q to connect with your Microsoft Teams
  data source. For more information, see [Register a Microsoft Entra app and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#sign-in-to-the-application "https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#sign-in-to-the-application") on
  the Microsoft website.
- Configured an OAuth 2.0 credential token containing a client ID
  and client secret. For more information, see [Azure documentation on managing access tokens for Teams](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/manage-teams-identity?pivots=programming-language-csharp "https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/manage-teams-identity?pivots=programming-language-csharp") on the
  Microsoft website.
- Added the necessary permissions. You can choose to add all permissions, or you
  can limit the scope by selecting fewer permissions based on which entities you
  want to crawl. _(Application level permissions required for new connector)_ All permissions must be at _application_ level, not delegated. The following table shows permissions by corresponding
  entity.

| Entity           | Required permissions for data sync                                                                                         | Required permissions for identity sync |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Channel Post     | + ChannelMessage.Read.All + Group.Read.All + User.Read + User.Read.All                                                     | TeamMember.Read.All                    |
| Chat Message     | + Chat.Read.All + ChatMessage.Read.All + ChatMember.Read.All + User.Read + User.Read.All + Group.Read.All                  | TeamMember.Read.All                    |
| Calendar Meeting | + Chat.Read.All + ChatMessage.Read.All + ChatMember.Read.All + User.Read + User.Read.All + Group.Read.All + Files.Read.All | TeamMember.Read.All                    |
| Meeting Notes    | + User.Read + User.Read.All + Group.Read.All + Files.Read.All                                                              | TeamMember.Read.All                    | <br>• Generated Microsoft Teams OAuth 2.0 credentials containing a client ID, client secret, username, and password. You need these credentials to authenticate Amazon Q to access Microsoft Teams. **In your AWS account, make sure you have:** <br>• Created a Amazon Q Business application. <br>• Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md"). <br>• Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role. <br>• Stored your Microsoft Teams authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret. ###### Note If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console. For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md"). |
