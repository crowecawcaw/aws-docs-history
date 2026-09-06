

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# How Amazon Q Business connector crawls Quip ACLs
<a name="quip-user-management"></a>

Connectors support crawling ACL and identity information where applicable based on the data source. If you index documents without ACLs, all documents are considered public. Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Quip data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group information) from your Quip instance. If you choose to activate ACL crawling, the information can be used to filter chat responses to your end user's document access level.

The Quip user IDs are mapped as follows:
+ `_user_id`—User IDs exist in Quip on files where there are set access permissions. They are mapped from the user emails as the IDs in Quip.

 For more information, see:
+ [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization)
+ [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler)
+ [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html)