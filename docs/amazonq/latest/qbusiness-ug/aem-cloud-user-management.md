

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# How Amazon Q Business connector crawls AEM (Cloud) ACLs
<a name="aem-cloud-user-management"></a>

Connectors support crawling ACL and identity information where applicable based on the data source. If you index documents without ACLs, all documents are considered public. Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an AEM (Cloud) data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group information) from your AEM (Cloud) instance. If you choose to activate ACL crawling, the information can be used to filter chat responses to your end user's document access level.

The group and user IDs are mapped as follows:
+ `_group_ids` – Group IDs exist in Adobe Experience Manager content where there are set access permissions. They're mapped from the names of the groups in AEM.
+ `_user_id` – User IDs exist in Adobe Experience Manager content where there are set access permissions. They're mapped from the user emails as the IDs in AEM.

 For more information, see:
+ [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization)
+ [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler)
+ [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html)