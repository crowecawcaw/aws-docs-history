#

Connecting to Salesforce

Salesforce provides customer relationship management (CRM) software that help you with sales, customer service, e-commerce, and more. If you're a Salesforce user, you can connect AWS Glue to your Salesforce account. Then, you can use Salesforce as a data source or destination in your ETL Jobs. Run these jobs to transfer data between Salesforce and AWS services or other supported applications.

###### Topics

- [AWS Glue support for Salesforce](salesforce-support.md "salesforce-support.md")
- [Policies containing the API operations for creating and using connections](salesforce-configuring-iam-permissions.md "salesforce-configuring-iam-permissions.md")
- [Configuring Salesforce](salesforce-configuring.md "salesforce-configuring.md")
- [Apply System Admin profile](#salesforce-configuring-apply-system-admin-profile "#salesforce-configuring-apply-system-admin-profile")
- [Configuring Salesforce connections](salesforce-configuring-connections.md "salesforce-configuring-connections.md")
- [Reading from Salesforce](salesforce-reading-from-entities.md "salesforce-reading-from-entities.md")
- [Writing to Salesforce](salesforce-writing-to.md "salesforce-writing-to.md")
- [Salesforce connection options](salesforce-connection-options.md "salesforce-connection-options.md")
- [Limitations for the Salesforce connector](salesforce-connector-limitations.md "salesforce-connector-limitations.md")
- [Set up the Authorization Code flow for Salesforce](salesforce-setup-authorization-code-flow.md "salesforce-setup-authorization-code-flow.md")
- [Set up the JWT bearer OAuth flow for Salesforce](salesforce-setup-jwt-bearer-oauth.md "salesforce-setup-jwt-bearer-oauth.md")

## Apply System Admin profile

In Salesforce, follow the steps to apply the System Admin profile:

1. In Salesforce, navigate to **Settings > Connected Apps > Connected Apps OAuth Usage**.
2. In the list of connected apps, find AWS Glue and choose **Install**. If needed, choose **Unblock**.
3. Navigate to **Settings > Manage Connected Apps then choose AWS Glue**. Under OAuth Policies, choose **Admin
   approved users are pre-authorized** and select the **System Admin** profile. This action restricts
   access to AWS Glue only to users with the System Admin profile.
