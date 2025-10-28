#  Zendesk data source connector

field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields
in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use reserved
  attributes to map commonly occurring document attributes in your data source to
  Amazon Q index fields.
- **Custom** – You can create custom attributes to map
  document attributes that are unique to your data to Amazon Q index
  fields.
  When you connect Amazon Q to a data source, Amazon Q automatically
  maps specific data source document attributes to fields within an Amazon Q index.
  If a document attribute in your data source doesn't have a attribute mapping already
  available, or if you want to map additional document attributes to index fields, use the
  custom field mappings to specify how a data source attribute maps to an Amazon Q
  index field. You create field mappings by editing your data source after your application
  and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through the API.

The Amazon Q
Zendesk connector supports the following entities and the associated reserved
and custom attributes.

###### Supported entities and field mappings

- [Tickets](#zendesk-field-mappings-tickets "#zendesk-field-mappings-tickets")
- [Ticket
  comments](#zendesk-field-mappings-ticket-comments "#zendesk-field-mappings-ticket-comments")
- [Ticket
  comment attachment](#zendesk-field-mappings-ticket-comment-attachment "#zendesk-field-mappings-ticket-comment-attachment")
- [Article](#zendesk-field-mappings-article "#zendesk-field-mappings-article")
- [Article
  comment](#zendesk-field-mappings-article-comment "#zendesk-field-mappings-article-comment")
- [Article
  comment attachment](#zendesk-field-mappings-article-comment-attachment "#zendesk-field-mappings-article-comment-attachment")
- [Community
  topic](#zendesk-field-mappings-community-topic "#zendesk-field-mappings-community-topic")
- [Community post](#zendesk-field-mappings-community-post "#zendesk-field-mappings-community-post")
- [Community post
  comment](#zendesk-field-mappings-community-post-comment "#zendesk-field-mappings-community-post-comment")

## Tickets

Amazon Q supports crawling [Zendesk Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/ "https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/") and offers the following ticket field
mappings.

| Zendesk field name | Index field name     | Description | Data type      |
| ------------------ | -------------------- | ----------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ticketChannel      | zd-channel           | Custom      | String         |
| category           | \_category           | Default     | String         |
| authors            | \_authors            | Default     | String list    |
| assignee           | zd_assignee          | Custom      | String         |
| tags               | zd_tags              | Custom      | String list    |
| status             | zd_status            | Custom      | String         |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           |
| organizationName   | zd_organization_name | Custom      | String         | ## Ticket comments Amazon Q supports crawling [Zendesk Ticket Comments](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/ "https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/") and offers the following ticket comment field mappings.                                             |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| category           | \_category           | Default     | String         |
| authors            | \_authors            | Default     | String list    |
| status             | zd_status            | Custom      | String         |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           |
| organizationName   | zd_organization_name | Custom      | String         | ## Ticket comment attachment Amazon Q supports crawling [Zendesk Ticket Comment Attachments](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/ "https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/") and offers the following ticket comment attachment field mappings.       |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| category           | \_category           | Default     | String         |
| authors            | \_authors            | Default     | String list    |
| status             | zd_status            | Custom      | String         |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           |
| organizationName   | zd_organization_name | Custom      | String         | ## Article Amazon Q supports crawling [Zendesk Articles](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/ "https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/") and offers the following article field mappings.                                                             |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| authors            | \_authors            | Default     | String list    |
| labels             | zd_article_labels    | Custom      | String list    |
| section            | zd_article_section   | Custom      | String list    |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           | ## Article comment Amazon Q supports crawling [Zendesk Article Comments](https://developer.zendesk.com/api-reference/help_center/help-center-api/article_comments/ "https://developer.zendesk.com/api-reference/help_center/help-center-api/article_comments/") and offers the following article comment field mappings.                     |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| authors            | \_authors            | Default     | String list    |
| labels             | zd_article_labels    | Custom      | String list    |
| section            | zd_article_section   | Custom      | String list    |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           | ## Article comment attachment Amazon Q supports crawling [Zendesk Article Comment Attachments](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/ "https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/") and offers the following article comment attachment field mappings.    |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| authors            | \_authors            | Default     | String list    |
| labels             | zd_article_labels    | Custom      | String list    |
| fileName           | zd_file_name         | Custom      | String         |
| fileType           | \_file_type          | Default     | String         |
| fileSize           | zd_file_size         | Custom      | Long (numeric) |
| section            | zd_article_section   | Custom      | String list    |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           | ## Community topic Amazon Q supports crawling [Zendesk Community Topics](https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_topic_page/ "https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_topic_page/") and offers the following community topic field mappings. |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| topicName          | zd_topic_name        | Custom      | String         |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           |
| category           | \_category           | Default     | String         | ## Community post Amazon Q supports crawling [Zendesk Community Posts](https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_post_page/ "https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_post_page/") and offers the following community post field mappings.      |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| postName           | zd_post_name         | Custom      | String         |
| topicName          | zd_topic_name        | Custom      | String         |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           |
| category           | \_category           | Default     | String         | ## Community post comment Amazon Q supports crawling [Zendesk Community Post Comments](https://developer.zendesk.com/api-reference/help_center/help-center-api/post_comments/ "https://developer.zendesk.com/api-reference/help_center/help-center-api/post_comments/") and offers the following community post comment field mappings.      |
| Zendesk field name | Index field name     | Description | Data type      |
| ---                | ---                  | ---         | ---            |
| postName           | zd_post_name         | Custom      | String         |
| topicName          | zd_topic_name        | Custom      | String         |
| sourceUrl          | \_source_uri         | Default     | String         |
| createdAt          | \_created_at         | Default     | Date           |
| updatedAt          | \_last_updated_at    | Default     | Date           |
| category           | \_category           | Default     | String         |
