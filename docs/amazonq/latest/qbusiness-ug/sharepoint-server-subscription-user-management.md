

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# How Amazon Q Business connector crawls SharePoint Server (Subscription Edition) ACLs
<a name="sharepoint-server-subscription-user-management"></a>

When you connect an SharePoint Server (Subscription Edition) data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group information) from your SharePoint Server (Subscription Edition) instance. If you choose to activate ACL crawling, the information can be used to filter chat responses to your end user's document access level.

To filter using a username, use the **User principal name** from your Azure portal. For example, johnstiles@kendra.onmicrosoft.com.

When you use a SharePoint group for user context filtering, calculate the group ID as follows:

**For local groups**

1. Get the site name. For example, `https://host.onmicrosoft.com/sites/siteName.`

1. Take the SHA256 hash of the site name. For example, `430a6b90503eef95c89295c8999c7981`.

1. Create the group ID by concatenating the SHA256 hash with a vertical bar ( \| ) and the group name. For example, if the group name is "local group name", the group ID is the following:

   `"430a6b90503eef95c89295c8999c7981 | localGroupName"` (with a space before and after the vertical bar).

 For more information, see:
+ [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization)
+ [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler)
+ [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html)