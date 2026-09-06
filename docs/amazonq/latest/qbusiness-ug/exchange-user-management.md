

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# How Amazon Q Business connector crawls Exchange ACLs
<a name="exchange-user-management"></a>

Connectors support crawling ACL and identity information where applicable based on the data source. If you index documents without ACLs, all documents are considered public. Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Exchange data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group information) from your Exchange instance. If you choose to activate ACL crawling, this information can be used to filter chat responses to your end user's document access level.

The Exchange group and user IDs are mapped as follows:
+ `_tenant_id` – Your Microsoft tenant ID is a globally unique identifier required to configure each connector instance. You can find your tenant ID in the properties section of your Microsoft account dashboard. 

 For more information, see:
+ [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization)
+ [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler)
+ [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html)