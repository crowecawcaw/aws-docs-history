

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business Alfresco (Server) data source connector field mappings
<a name="alfresco-server-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application environment and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes-types.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Alfresco connector supports the following entities and the associated reserved and custom attributes.

**Important**  
If you map any Alfresco (Server) field to Amazon Q document title and document body fields, Amazon Q will generate responses from data in the document title and body.

**Topics**
+ [Documents](#alfresco-field-mappings-documents)
+ [Comments](#alfresco-field-mappings-comments)

## Documents
<a name="alfresco-field-mappings-documents"></a>


| Alfresco field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| creationTime | \_created\_at | Default | Date | 
| lastModified | \_last\_updated\_at | Default | Date | 
| author | \_authors | Default | String list | 
| sourceUri | \_source\_uri | Default | String | 
| category | \_category | Default | String | 
| fileType | \_file\_type | Default | String | 
| version | \_version | Default | String | 
| siteName | al\_site\_name | Custom | String | 
| size | al\_document\_size | Custom | Long (numeric) | 
| versionType | al\_version\_type | Custom | String | 
| title | al\_document\_title | Custom | String | 
| repositoryId | al\_repository\_id | Custom | String | 

## Comments
<a name="alfresco-field-mappings-comments"></a>


| Alfresco field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| creationTime | \_created\_at | Default | Date | 
| lastModified | \_last\_updated\_at | Default | Date | 
| author | \_authors | Default | String list | 
| sourceUri | \_source\_uri | Default | String | 
| version | \_version | Default | String | 
| category | \_category | Default | String | 
| fileType | \_file\_type | Default | String | 
| siteName | al\_site\_name | Custom | String | 
| size | al\_document\_size | Custom | Long (numeric) | 
| versionType | \_al\_version\_type | Custom | String | 
| title | al\_document\_title | Custom | String | 
| repositoryId | al\_repository\_id | Custom | String | 