

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Microsoft Yammer data source connector field mappings
<a name="yammer-field-mappings"></a>

To help you structure data for retrieval and chat filtering, Amazon Q Business crawls data source document attributes or metadata and maps them to fields in your Amazon Q index.

Amazon Q has reserved fields that it uses when querying your application. When possible, Amazon Q automatically maps these built-in fields to attributes in your data source. If a built-in field doesn't have a default mapping, or if you want to map additional index fields, use the custom field mappings to specify how a data source attribute maps to your Amazon Q application. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Yammer connector supports the following entities and the associated reserved and custom attributes.

**Note**  
You can map any Yammer field to the document title or document body Amazon Q reserved/default index fields.

**Topics**
+ [Message](#yammer-field-mappings-message)
+ [Attachment](#yammer-field-mappings-attachment)
+ [User](#yammer-field-mappings-user)
+ [Community](#yammer-field-mappings-community)

## Message
<a name="yammer-field-mappings-message"></a>

Amazon Q supports crawling [Microsoft Yammer Messages](https://learn.microsoft.com/en-us/rest/api/yammer/messagesjson) and offers the following message field mappings.


| Microsoft Yammer field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  id  |  ymr\_id  |  Custom  |  String  | 
|  message\_type  |  ymr\_message\_type  |  Custom  |  String  | 
|  api\_url  |  ymr\_api\_url  |  Custom  |  String  | 
|  group\_id  |  ymr\_group\_id  |  Custom  |  String  | 
|  group\_name  |  ymr\_group\_name  |  Custom  |  String  | 
|  in\_private\_conversation  |  ymr\_in\_private\_conversation  |  Custom  |  String  | 
|  in\_private\_group  |  ymr\_in\_private\_group  |  Custom  |  String  | 
|  sender\_email  |  ymr\_sender\_email  |  Custom  |  String  | 
|  sender\_id  |  ymr\_sender\_id  |  Custom  |  String  | 
|  sender\_name  |  ymr\_sender\_name  |  Custom  |  String  | 
|  created\_at  |  \_created\_at  |  Default  |  Date  | 
|  web\_url  |  \_source\_uri  |  Default  |  String  | 

## Attachment
<a name="yammer-field-mappings-attachment"></a>


| Microsoft Yammer field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  id  |  ymr\_attachment\_id  |  Custom  |  String  | 
|  name  |  ymr\_attachment\_name  |  Custom  |  String  | 
|  size  |  ymr\_attachment\_size  |  Custom  |  String  | 
|  url  |  ymr\_attachment\_url  |  Custom  |  String  | 
|  file\_type  |  ymr\_attachment\_type  |  Custom  |  String  | 
|  created\_at  |  \_created\_at  |  Default  |  Date  | 
|  privacy  |  ymr\_attachment\_privacy  |  Custom  |  String  | 
|  group\_name  |  ymr\_attachment\_group\_name  |  Custom  |  String  | 
|  sender\_email  |  ymr\_attachment\_sender\_email  |  Custom  |  String  | 
|  web\_url  |  \_source\_uri  |  Default  |  String  | 

## User
<a name="yammer-field-mappings-user"></a>


| Microsoft Yammer field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  id  |  ymr\_user\_id  |  Custom  |  String  | 
|  user\_type  |  ymr\_user\_type  |  Custom  |  String  | 
|  state  |  ymr\_user\_state  |  Custom  |  String  | 
|  full\_name  |  ymr\_user\_full\_name  |  Custom  |  String  | 
|  activated\_at  |  \_created\_at  |  Default  |  Date  | 
|  first\_name  |  ymr\_user\_first\_name  |  Custom  |  String  | 
|  last\_name  |  ymr\_user\_last\_name  |  Custom  |  String  | 
|  network\_name  |  ymr\_user\_network\_name  |  Custom  |  String  | 
|  network\_domains  |  ymr\_user\_network\_domains  |  Custom  |  String  | 
|  url  |  ymr\_user\_url  |  Custom  |  String  | 
|  name  |  ymr\_user\_name  |  Custom  |  String  | 
|  birth\_date  |  ymr\_user\_birth\_date  |  Custom  |  Date  | 
|  admin  |  ymr\_user\_admin  |  Custom  |  String  | 
|  verified\_admin  |  ymr\_user\_verified\_admin  |  Custom  |  String  | 
|  contact  |  ymr\_user\_contact  |  Custom  |  String  | 
|  email  |  ymr\_user\_email  |  Custom  |  String  | 
|  web\_url  |  \_source\_uri  |  Default  |  String  | 

## Community
<a name="yammer-field-mappings-community"></a>


| Microsoft Yammer field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  id  |  ymr\_community\_id  |  Custom  |  String  | 
|  name  |  ymr\_community\_name  |  Custom  |  String  | 
|  email  |  ymr\_community\_email  |  Custom  |  String  | 
|  full\_name  |  ymr\_community\_full\_name  |  Custom  |  String  | 
|  description  |  ymr\_community\_description  |  Custom  |  String  | 
|  privacy  |  ymr\_community\_privacy  |  Custom  |  String  | 
|  url  |  ymr\_community\_url  |  Custom  |  String  | 
|  created\_at  |  \_created\_at  |  Default  |  Date  | 
|  state  |  ymr\_community\_state  |  Custom  |  String  | 
|  web\_url  |  \_source\_uri  |  Default  |  String  | 