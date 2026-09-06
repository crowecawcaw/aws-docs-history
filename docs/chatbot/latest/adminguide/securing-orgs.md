

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Securing your AWS organization in Amazon Q Developer in chat applications
<a name="securing-orgs"></a>

You can secure your AWS organization or organizational units (OUs) using organization policies. AWS Organizations is a service for grouping and centrally managing multiple AWS accounts that your business owns. If you enable all features in an organization, you can apply organization policies such as a chat applications policy and service control policies (SCPs) to any or all of your accounts. A chat applications policy defines which permissions models, chat platforms, and chat workspaces can be used to access your accounts. SCPs limit permissions for entities in member accounts, including each AWS account root user. Effective chat application permissions are the intersection between organization level controls (organization policies) and account level controls ([User role requirement](understanding-permissions.md#role-reqs), Amazon Q Developer in chat applications configuration resources). For more information about organization policies, see [ Managing policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) in the *AWS Organizations User Guide*.

**Topics**
+ [Amazon Q Developer in chat applications organization policies](chatbot-orgs-policy.md)
+ [Service control policies (SCPs) for Amazon Q Developer in chat applications](scp.md)