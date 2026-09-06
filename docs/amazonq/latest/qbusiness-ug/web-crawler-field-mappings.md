

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Web Crawler data source connector field mappings
<a name="web-crawler-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Web Crawler connector supports the following entities and the associated reserved and custom attributes.

**Topics**
+ [Web Pages](#web-crawler-field-mappings-web-pages)
+ [Attachments](#web-crawler-field-mappings-assets)

## Web Pages
<a name="web-crawler-field-mappings-web-pages"></a>


| Web Crawler field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| category | \_category | Default | String | 
| sourceUrl | \_source\_uri | Default | String | 
| title | \_document\_title | Default | String | 
| htmlSize | wc\_html\_size | Custom | Long (numeric) | 

## Attachments
<a name="web-crawler-field-mappings-assets"></a>


| Web Crawler field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| category | \_category | Default | String | 
| sourceUrl | \_source\_uri | Default | String | 
| fileName | wc\_file\_name | Custom | String | 
| fileType | wc\_file\_type | Custom | String | 
| fileSize | wc\_file\_size | Custom | Long (numeric) | 