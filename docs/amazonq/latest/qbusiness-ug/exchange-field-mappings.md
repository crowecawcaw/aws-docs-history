# Microsoft Exchange data source connector

field mappings

You can improve search results and customize your users' chat experience by mapping document attributes from your Microsoft Exchange data to fields in your Amazon Q index.

Amazon Q offers two types of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use reserved
  attributes to map commonly occurring document attributes in your data source to
  Amazon Q index fields.
- **Custom** – You can create custom attributes to map
  document attributes that are unique to your data to Amazon Q index
  fields.
  When you connect Amazon Q to a data source, Amazon Q automatically
  maps specific data source document attributes to fields within an Amazon Q index.
  If a document attribute in your data source doesn't have an attribute mapping already
  available, or if you want to map additional document attributes to index fields, use
  custom field mappings to specify how a data source attribute maps to an Amazon Q
  index field. You create field mappings by editing your data source after your application
  and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through the API.

###### Note

You can map any Exchange field to the document title or document body
Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Mails](#exchange-field-mappings-mails "#exchange-field-mappings-mails")
- [Calendar](#exchange-field-mappings-calendar "#exchange-field-mappings-calendar")
- [Attachments](#exchange-field-mappings-attachments "#exchange-field-mappings-attachments")
- [OneNotes](#exchange-field-mappings-onenotes "#exchange-field-mappings-onenotes")
- [Contacts](#exchange-field-mappings-contacts "#exchange-field-mappings-contacts")

## Mails

| Microsoft Exchange field name | Index field name       | Description | Data type   |
| ----------------------------- | ---------------------- | ----------- | ----------- |
| createdDateTime               | \_created_at           | Default     | Date        |
| lastModifiedDateTime          | \_last_updated_at      | Default     | Date        |
| uri                           | \_source_uri           | Default     | String      |
| category                      | \_category             | Default     | String      |
| bccRecipients                 | xchng_bccRecipient     | Custom      | String list |
| ccRecipients                  | xchng_ccRecipient      | Custom      | String list |
| hasAttachment                 | xchng_hasAttachment    | Custom      | String      |
| sendDateTime                  | xchng_sendDateTime     | Custom      | Date        |
| importance                    | xchng_importance       | Custom      | String      |
| from                          | xchng_from             | Custom      | String      |
| to                            | xchng_to               | Custom      | String list |
| receivedDateTime              | xchng_receivedDateTime | Custom      | Date        |
| isRead                        | xchng_isRead           | Custom      | String      |
| replyTo                       | xchng_replyTo          | Custom      | String      |
| folder                        | xchng_folder           | Custom      | String      |
| title                         | xchng_title            | Custom      | String      |
| flagStatus                    | xchng_flagStatus       | Custom      | String      |

## Calendar

| Microsoft Exchange field name | Index field name      | Description | Data type |
| ----------------------------- | --------------------- | ----------- | --------- |
| location                      | xchng_location        | Custom      | String    |
| organizer                     | xchng_organizer       | Custom      | String    |
| subject                       | xchng_subject         | Custom      | String    |
| weblink                       | \_source_uri          | Default     | String    |
| createdDateTime               | \_created_at          | Default     | Date      |
| lastModifiedDateTime          | \_last_updated_at     | Default     | Date      |
| eventStartTime                | xchng_eventStartTime  | Default     | Date      |
| eventEndTime                  | xchng_eventEndTime    | Default     | Date      |
| attendees                     | xchng_attendees       | Custom      | String    |
| recurrence                    | xchng_Recurrence      | Custom      | String    |
| category                      | \_category            | Default     | String    |
| isReminderOn                  | xchng_isReminderOn    | Custom      | String    |
| sensitivity                   | xchng_sensitivity     | Custom      | String    |
| isOnlineMeeting               | xchng_isOnlineMeeting | Custom      | String    |
| seriesMasterId                | xchng_seriesMasterId  | Custom      | String    |
| isCancelled                   | xchng_isCancelled     | Custom      | String    |

## Attachments

| Microsoft Exchange field name | Index field name  | Description | Data type |
| ----------------------------- | ----------------- | ----------- | --------- |
| title                         | xchng_title       | Custom      | String    |
| lastModifiedDateTime          | \_last_updated_at | Default     | Date      |
| category                      | \_category        | Default     | String    |
| contentType                   | \_file_type       | Default     | String    |
| size                          | xchng_size        | Custom      | String    |
| url                           | \_source_uri      | Default     | String    |

## OneNotes

| Microsoft Exchange field name | Index field name    | Description | Data type |
| ----------------------------- | ------------------- | ----------- | --------- |
| isShared                      | xchng_isShared      | Custom      | String    |
| link                          | xchng_links         | Custom      | String    |
| title                         | xchng_title         | Custom      | String    |
| lastUpdatedBy                 | xchng_lastUpdatedBy | Custom      | String    |
| lastModifiedDateTime          | \_last_updated_at   | Default     | Date      |
| createdDateTime               | \_created_at        | Default     | Date      |
| category                      | \_category          | Default     | String    |
| createdBy                     | xchng_createdBy     | Custom      | String    |
| userRole                      | xchng_useRole       | Custom      | String    |

## Contacts

| Microsoft Exchange field name | Index field name      | Description | Data type |
| ----------------------------- | --------------------- | ----------- | --------- |
| contactName                   | xchng_contactName     | Custom      | String    |
| emailAddress                  | xchng_email           | Custom      | String    |
| companyName                   | xchng_companyName     | Custom      | String    |
| manager                       | xchng_manager         | Custom      | String    |
| jobTitle                      | xchng_jobtitle        | Custom      | String    |
| location                      | xchng_officeLocation  | Custom      | String    |
| mobilePhone                   | xchng_mobile          | Custom      | String    |
| birthday                      | xchng_birthday        | Custom      | Date      |
| homeAddress                   | xchng_homeAddress     | Custom      | String    |
| businessAddress               | xchng_businessAddress | Custom      | String    |
| department                    | xchng_department      | Custom      | String    |
| profession                    | xchng_profession      | Custom      | String    |
| createdAt                     | \_created_at          | Default     | Date      |
| category                      | \_category            | Default     | String    |
| url                           | \_source_uri          | Custom      | String    |
