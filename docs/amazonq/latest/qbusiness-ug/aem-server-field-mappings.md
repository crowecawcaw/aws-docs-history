

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# AEM (Server) data source connector field mappings
<a name="aem-server-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application environment and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes-types.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Adobe Experience Manager (AEM) connector supports the following entities and the associated reserved and custom attributes.

**Important**  
If you map any AEM (Server) field to Amazon Q document title and document body fields, Amazon Q will generate responses from data in the document title and body.

**Topics**
+ [Pages](#aem-field-mappings-pages)
+ [Assets](#aem-field-mappings-assets)

## Pages
<a name="aem-field-mappings-pages"></a>

Amazon Q supports crawling [AEM Pages](https://experienceleague.adobe.com/docs/experience-manager-65/content/sites/authoring/essentials/page-authoring.html?lang=en) and offers the following page field mappings.


| Adobe Experience Manager (AEM) field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| aem\_page\_source\_uri | \_source\_uri | Default | String | 
| aem\_page\_createdBy | \_authors | Default | String list | 
| aem\_page\_template | aem\_page\_template | Custom | String | 
| aem\_entity\_type | \_category | Default | String | 
| aem\_page\_createdAt | \_created\_at | Default | Date | 
| aem\_page\_lastModified | \_last\_updated\_at | Default | Date | 
| aem\_page\_lastReplicatedBy | aem\_page\_publisher | Custom | String | 
| aem\_page\_lastReplicatedAt | aem\_page\_publishedAt | Custom | Date | 

## Assets
<a name="aem-field-mappings-assets"></a>

Amazon Q supports crawling [AEM Assets](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/assets.html?lang=en) and offers the following asset field mappings.


| Adobe Experience Manager (AEM) field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| aem\_page\_source\_uri | \_source\_uri | Default | String | 
| aem\_page\_createdBy | \_authors | Default | String list | 
| aem\_entity\_type | \_category | Default | String | 
| aem\_page\_createdAt | \_created\_at | Default | Date | 
| aem\_page\_lastModified | \_last\_updated\_at | Default | Date | 
| aem\_page\_lastReplicatedBy | aem\_page\_publisher | Custom | String | 
| aem\_page\_lastReplicatedAt | aem\_page\_publishedAt | Custom | Date | 