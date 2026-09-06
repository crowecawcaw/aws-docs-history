

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Slack data source connector field mappings
<a name="slack-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Slack connector supports the following field mappings:


|  Slack field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| size | sl\_gen\_size | Custom | Long (numeric) | 
| emojis | sl\_gen\_emojis | Custom | String list | 
| title | sl\_gen\_title | Custom | String | 
| authors | \_authors | Default | String list | 
| url | \_source\_uri | Default | String | 
| category | sl\_gen\_category | Custom | String | 
| created\_at | \_created\_at | Default | Date | 
| last\_updated\_at | \_last\_updated\_at | Default | Date | 
| msg\_channel\_id | sl\_message\_channel\_id | Custom | String | 
| msg\_channel\_name | sl\_msg\_channel\_name | Custom | String | 