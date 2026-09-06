

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

#  Zendesk data source connector field mappings
<a name="zendesk-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Zendesk connector supports the following entities and the associated reserved and custom attributes.

**Topics**
+ [Tickets](#zendesk-field-mappings-tickets)
+ [Ticket comments](#zendesk-field-mappings-ticket-comments)
+ [Ticket comment attachment](#zendesk-field-mappings-ticket-comment-attachment)
+ [Article](#zendesk-field-mappings-article)
+ [Article comment](#zendesk-field-mappings-article-comment)
+ [Article comment attachment](#zendesk-field-mappings-article-comment-attachment)
+ [Community topic](#zendesk-field-mappings-community-topic)
+ [Community post](#zendesk-field-mappings-community-post)
+ [Community post comment](#zendesk-field-mappings-community-post-comment)

## Tickets
<a name="zendesk-field-mappings-tickets"></a>

Amazon Q supports crawling [Zendesk Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/) and offers the following ticket field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| ticketChannel | zd-channel | Custom | String | 
| category | \_category | Default | String | 
| authors | \_authors | Default | String list | 
| assignee | zd\_assignee | Custom | String | 
| tags | zd\_tags | Custom | String list | 
| status | zd\_status | Custom | String | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 
| organizationName | zd\_organization\_name | Custom | String | 

## Ticket comments
<a name="zendesk-field-mappings-ticket-comments"></a>

Amazon Q supports crawling [Zendesk Ticket Comments](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/) and offers the following ticket comment field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| category | \_category | Default | String | 
| authors | \_authors | Default | String list | 
| status | zd\_status | Custom | String | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 
| organizationName | zd\_organization\_name | Custom | String | 

## Ticket comment attachment
<a name="zendesk-field-mappings-ticket-comment-attachment"></a>

Amazon Q supports crawling [Zendesk Ticket Comment Attachments](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/) and offers the following ticket comment attachment field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| category | \_category | Default | String | 
| authors | \_authors | Default | String list | 
| status | zd\_status | Custom | String | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 
| organizationName | zd\_organization\_name | Custom | String | 

## Article
<a name="zendesk-field-mappings-article"></a>

Amazon Q supports crawling [Zendesk Articles](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) and offers the following article field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| authors | \_authors | Default | String list | 
| labels | zd\_article\_labels | Custom | String list | 
| section | zd\_article\_section | Custom | String list | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 

## Article comment
<a name="zendesk-field-mappings-article-comment"></a>

Amazon Q supports crawling [Zendesk Article Comments](https://developer.zendesk.com/api-reference/help_center/help-center-api/article_comments/) and offers the following article comment field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| authors | \_authors | Default | String list | 
| labels | zd\_article\_labels | Custom | String list | 
| section | zd\_article\_section | Custom | String list | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 

## Article comment attachment
<a name="zendesk-field-mappings-article-comment-attachment"></a>

Amazon Q supports crawling [Zendesk Article Comment Attachments](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/) and offers the following article comment attachment field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| authors | \_authors | Default | String list | 
| labels | zd\_article\_labels | Custom | String list | 
| fileName | zd\_file\_name | Custom | String | 
| fileType | \_file\_type | Default | String | 
| fileSize | zd\_file\_size | Custom | Long (numeric) | 
| section | zd\_article\_section | Custom | String list | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 

## Community topic
<a name="zendesk-field-mappings-community-topic"></a>

Amazon Q supports crawling [Zendesk Community Topics](https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_topic_page/) and offers the following community topic field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| topicName | zd\_topic\_name | Custom | String | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 
| category | \_category | Default | String | 

## Community post
<a name="zendesk-field-mappings-community-post"></a>

Amazon Q supports crawling [Zendesk Community Posts](https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_post_page/) and offers the following community post field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| postName | zd\_post\_name | Custom | String | 
| topicName | zd\_topic\_name | Custom | String | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 
| category | \_category | Default | String | 

## Community post comment
<a name="zendesk-field-mappings-community-post-comment"></a>

Amazon Q supports crawling [Zendesk Community Post Comments](https://developer.zendesk.com/api-reference/help_center/help-center-api/post_comments/) and offers the following community post comment field mappings.


| Zendesk field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| postName | zd\_post\_name | Custom | String | 
| topicName | zd\_topic\_name | Custom | String | 
| sourceUrl | \_source\_uri | Default | String | 
| createdAt | \_created\_at | Default | Date | 
| updatedAt | \_last\_updated\_at | Default | Date | 
| category | \_category | Default | String | 