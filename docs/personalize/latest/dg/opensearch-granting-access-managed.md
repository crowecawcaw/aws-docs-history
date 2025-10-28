# Setting up Amazon OpenSearch Service permissions

If you use Amazon OpenSearch Service, you must be able to access your Amazon Personalize resources from your OpenSearch Service domain.

###### To set up permissions

1. Depending on if your resources are in the same or different accounts, create one or more IAM service roles with
   permission to access your resources.
   - If your OpenSearch Service and Amazon Personalize resources are in the same account, you create an IAM service role for OpenSearch Service and
     grant it permission to get a personalized ranking from your Amazon Personalize campaign. For more information, see [Configuring permissions when resources are in the same
     account](service-role-managed.md "service-role-managed.md").
   - If your OpenSearch Service and Amazon Personalize resources are in separate accounts, you create two IAM service roles. You create
     one in the account with your OpenSearch Service resources and grant it access to your OpenSearch Service resources. And you create one in
     the account with your Amazon Personalize resources and grant it permission to get a personalized ranking from your Amazon Personalize
     campaign. For more information, see [Configuring permissions when resources are in different
     accounts](configuring-multiple-accounts.md "configuring-multiple-accounts.md").

2. Grant the user or role that's accessing your OpenSearch Service domain `PassRole` permissions for the IAM service
   role that you created for OpenSearch Service. For more information, see [Configuring Amazon OpenSearch Service domain security](domain-user-managed.md "domain-user-managed.md").
   After you set up permissions, you are ready to install the plugin on your domain. For more information, see [Installing the plugin](open-search-install-managed.md "open-search-install-managed.md").

###### Topics

- [Configuring permissions when resources are in the same
  account](service-role-managed.md "service-role-managed.md")
- [Configuring permissions when resources are in different
  accounts](configuring-multiple-accounts.md "configuring-multiple-accounts.md")
- [Configuring Amazon OpenSearch Service domain security](domain-user-managed.md "domain-user-managed.md")
