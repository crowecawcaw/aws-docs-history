

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business data source connector field mappings
<a name="oracle-database-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q PostgreSQL connector supports the following field mappings:

**Topics**
+ [Document](#oracle-database-field-mappings-document)

## Document
<a name="oracle-database-field-mappings-document"></a>


| JDBC field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| jd\_document\_id | jd\_document\_id | Custom | String | 
| jd\_document\_title | jd\_document\_title | Custom | String | 
| jd\_source\_uri | \_source\_uri | Default | String | 