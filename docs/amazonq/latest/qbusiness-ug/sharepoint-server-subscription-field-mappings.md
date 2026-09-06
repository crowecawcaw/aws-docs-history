

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business SharePoint Server (Subscription Edition) data source connector field mappings
<a name="sharepoint-server-subscription-field-mappings"></a>

To help you structure data for retrieval and chat filtering, Amazon Q Business crawls data source document attributes or metadata and maps them to fields in your Amazon Q index.

Amazon Q has reserved fields that it uses when querying your application. When possible, Amazon Q automatically maps these built-in fields to attributes in your data source. If a built-in field doesn't have a default mapping, or if you want to map additional index fields, use the custom field mappings to specify how a data source attribute maps to your Amazon Q application. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes-types.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q SharePoint connector supports the following entities and the associated reserved and custom attributes.

**Important**  
If you map any SharePoint Server (Subscription Edition) field to Amazon Q document title and document body fields, Amazon Q will generate responses from data in the document title and body.

**Note**  
You can map any SharePoint field to the document title or document body Amazon Q reserved/default index fields.

**Topics**
+ [Files](#sharepoint-field-mappings-files)
+ [Events](#sharepoint-field-mappings-events)
+ [Pages](#sharepoint-field-mappings-pages)
+ [Links](#sharepoint-field-mappings-links)
+ [Attachments](#sharepoint-field-mappings-attachments)
+ [Comments](#sharepoint-field-mappings-comments)

## Files
<a name="sharepoint-field-mappings-files"></a>


| SharePoint field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  title  |  sp\_title  |  Custom  |  String  | 
|  sourceUri  |  \_source\_uri  |  Default  |  String  | 
|  checkInComment  |  sp\_checkInComment  |  Custom  |  String  | 
|  size  |  sp\_sizeLong  |  Custom  |  Long (numeric)  | 
|  lastModifiedDateTime  |  \_last\_updated\_at  |  Default  |  Date  | 
|  createdAt  |  \_created\_at  |  Default  |  Date  | 
|  author  |  \_authors  |  Default  |  String list  | 
|  majorVersion  |  sp\_majorVersion  |  Custom  |  String  | 
|  uiVersionLabel  |  sp\_uiVersionLabel  |  Custom  |  String  | 
|  uniqueId  |  sp\_uniqueId  |  Custom  |  String  | 
|  irmEnabled  |  sp\_irmEnabled  |  Custom  |  String  | 
|  checkOutType  |  sp\_checkOutType  |  Custom  |  String  | 
|  category  |  \_category  |  Default  |  String  | 
|  modifiedBy  |  sp\_modifiedBy  |  Custom  |  String  | 
|  level  |  sp\_level  |  Custom  |  String  | 
|  uiVersion  |  sp\_uiVersion  |  Custom  |  String  | 
|  contentTag  |  sp\_contentTag  |  Custom  |  String  | 
|  eTag  |  sp\_eTag  |  Custom  |  String  | 
|  oneNoteDocument  |  sp\_oneNoteDocument  |  Custom  |  String  | 
|  oneNoteSection  |  sp\_oneNoteSection  |  Custom  |  String  | 
|  oneNotePage  |  sp\_oneNotePage  |  Custom  |  String  | 

## Events
<a name="sharepoint-field-mappings-events"></a>


| SharePoint field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  title  |  sp\_title  |  Custom  |  String  | 
|  lastModifiedDateTime  |  \_last\_updated\_at  |  Default  |  Date  | 
|  sourceUri  |  \_source\_uri  |  Default  |  String  | 
|  attachments  |  sp\_hasAttachments  |  Custom  |  String  | 
|  createdDate  |  \_created\_at  |  Default  |  Date  | 
|  authorId  |  sp\_authorId  |  Custom  |  String  | 
|  editorId  |  sp\_editorId  |  Custom  |  String  | 
|  location  |  sp\_location  |  Custom  |  String  | 
|  eventDate  |  sp\_eventDate  |  Custom  |  Date  | 
|  eventEndDate  |  sp\_eventEndDate  |  Custom  |  Date  | 
|  ifRecurrence  |  sp\_ifRecurrence  |  Custom  |  String  | 
|  ifAllDayEvent  |  sp\_ifAllDayEvent  |  Custom  |  String  | 
|  category  |  \_category  |  Default  |  String  | 
|  eventCategory  |  sp\_eventcategory  |  Custom  |  String  | 

## Pages
<a name="sharepoint-field-mappings-pages"></a>


| SharePoint field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  createdDateTime  |  \_created\_at  |  Default  |  Date  | 
|  lastModifiedDateTime  |  \_last\_updated\_at  |  Default  |  Date  | 
|  title  |  sp\_title  |  Custom  |  String  | 
|  sourceUri  |  \_source\_uri  |  Default  |  String  | 
|  firstPublishedDate  |  sp\_firstPublishedDate  |  Custom  |  Date  | 
|  authorId  |  sp\_authorId  |  Custom  |  String  | 
|  editorId  |  sp\_editorId  |  Custom  |  String  | 
|  category  |  \_category  |  Default  |  String  | 

## Links
<a name="sharepoint-field-mappings-links"></a>


| SharePoint field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  createdAt  |  \_created\_at  |  Default  |  Date  | 
|  lastModifiedDateTime  |  \_last\_updated\_at  |  Default  |  Date  | 
|  title  |  sp\_title  |  Custom  |  String  | 
|  sourceUri  |  \_source\_uri  |  Default  |  String  | 
|  fileType  |  sp\_fileType  |  Custom  |  String  | 
|  fileDirPath  |  sp\_fileDirPath  |  Custom  |  String  | 
|  firstPublishedDate  |  sp\_firstPublishedDate  |  Custom  |  Date  | 
|  authorId  |  sp\_authorId  |  Custom  |  String  | 
|  editorId  |  sp\_editorId  |  Custom  |  String  | 
|  category  |  \_category  |  Default  |  String  | 
|  size  |  sp\_sizeLong  |  Custom  |  Long (numeric)  | 

## Attachments
<a name="sharepoint-field-mappings-attachments"></a>


| SharePoint field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  title  |  sp\_\_title  |  Custom  |  String  | 
|  parentCreatedDate  |  \_created\_at  |  Default  |  Date  | 
|  sourceUri  |  \_source\_uri  |  Default  |  String  | 
|  parentModifiedDate  |  \_last\_updated\_at  |  Custom  |  Date  | 
|  parentListId  |  sp\_parentListId  |  Custom  |  String  | 
|  parentTitle  |  sp\_parentTitle  |  Custom  |  String  | 
|  category  |  \_category  |  Default  |  String  | 

## Comments
<a name="sharepoint-field-mappings-comments"></a>


| SharePoint field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
|  createdDateTime  |  \_created\_at  |  Default  |  Date  | 
|  likedBy  |  sp\_likedBy  |  Custom  |  String  | 
|  sourceUri  |  \_source\_uri  |  Custom  |  String  | 
|  isReply  |  sp\_isReply  |  Custom  |  String  | 
|  author  |  \_authors  |  Default  |  String list  | 
|  listId  |  sp\_listId  |  Custom  |  String  | 
|  category  |  \_category  |  Default  |  String  | 
|  replyCount  |  sp\_replyCount  |  Custom  |  String  | 
|  parentTitle  |  sp\_parentTitle  |  Custom  |  String  | 