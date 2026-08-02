Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Microsoft Exchange data source connector field mappings

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

| Microsoft Exchange field name | Index field name        | Description | Data type   |
| ----------------------------- | ----------------------- | ----------- | ----------- |
| createdDateTime               | \_created\_at           | Default     | Date        |
| lastModifiedDateTime          | \_last\_updated\_at     | Default     | Date        |
| uri                           | \_source\_uri           | Default     | String      |
| category                      | \_category              | Default     | String      |
| bccRecipients                 | xchng\_bccRecipient     | Custom      | String list |
| ccRecipients                  | xchng\_ccRecipient      | Custom      | String list |
| hasAttachment                 | xchng\_hasAttachment    | Custom      | String      |
| sendDateTime                  | xchng\_sendDateTime     | Custom      | Date        |
| importance                    | xchng\_importance       | Custom      | String      |
| from                          | xchng\_from             | Custom      | String      |
| to                            | xchng\_to               | Custom      | String list |
| receivedDateTime              | xchng\_receivedDateTime | Custom      | Date        |
| isRead                        | xchng\_isRead           | Custom      | String      |
| replyTo                       | xchng\_replyTo          | Custom      | String      |
| folder                        | xchng\_folder           | Custom      | String      |
| title                         | xchng\_title            | Custom      | String      |
| flagStatus                    | xchng\_flagStatus       | Custom      | String      |

## Calendar

| Microsoft Exchange field name | Index field name       | Description | Data type |
| ----------------------------- | ---------------------- | ----------- | --------- |
| location                      | xchng\_location        | Custom      | String    |
| organizer                     | xchng\_organizer       | Custom      | String    |
| subject                       | xchng\_subject         | Custom      | String    |
| weblink                       | \_source\_uri          | Default     | String    |
| createdDateTime               | \_created\_at          | Default     | Date      |
| lastModifiedDateTime          | \_last\_updated\_at    | Default     | Date      |
| eventStartTime                | xchng\_eventStartTime  | Default     | Date      |
| eventEndTime                  | xchng\_eventEndTime    | Default     | Date      |
| attendees                     | xchng\_attendees       | Custom      | String    |
| recurrence                    | xchng\_Recurrence      | Custom      | String    |
| category                      | \_category             | Default     | String    |
| isReminderOn                  | xchng\_isReminderOn    | Custom      | String    |
| sensitivity                   | xchng\_sensitivity     | Custom      | String    |
| isOnlineMeeting               | xchng\_isOnlineMeeting | Custom      | String    |
| seriesMasterId                | xchng\_seriesMasterId  | Custom      | String    |
| isCancelled                   | xchng\_isCancelled     | Custom      | String    |

## Attachments

| Microsoft Exchange field name | Index field name    | Description | Data type |
| ----------------------------- | ------------------- | ----------- | --------- |
| title                         | xchng\_title        | Custom      | String    |
| lastModifiedDateTime          | \_last\_updated\_at | Default     | Date      |
| category                      | \_category          | Default     | String    |
| contentType                   | \_file\_type        | Default     | String    |
| size                          | xchng\_size         | Custom      | String    |
| url                           | \_source\_uri       | Default     | String    |

## OneNotes

| Microsoft Exchange field name | Index field name     | Description | Data type |
| ----------------------------- | -------------------- | ----------- | --------- |
| isShared                      | xchng\_isShared      | Custom      | String    |
| link                          | xchng\_links         | Custom      | String    |
| title                         | xchng\_title         | Custom      | String    |
| lastUpdatedBy                 | xchng\_lastUpdatedBy | Custom      | String    |
| lastModifiedDateTime          | \_last\_updated\_at  | Default     | Date      |
| createdDateTime               | \_created\_at        | Default     | Date      |
| category                      | \_category           | Default     | String    |
| createdBy                     | xchng\_createdBy     | Custom      | String    |
| userRole                      | xchng\_useRole       | Custom      | String    |

## Contacts

| Microsoft Exchange field name | Index field name       | Description | Data type |
| ----------------------------- | ---------------------- | ----------- | --------- |
| contactName                   | xchng\_contactName     | Custom      | String    |
| emailAddress                  | xchng\_email           | Custom      | String    |
| companyName                   | xchng\_companyName     | Custom      | String    |
| manager                       | xchng\_manager         | Custom      | String    |
| jobTitle                      | xchng\_jobtitle        | Custom      | String    |
| location                      | xchng\_officeLocation  | Custom      | String    |
| mobilePhone                   | xchng\_mobile          | Custom      | String    |
| birthday                      | xchng\_birthday        | Custom      | Date      |
| homeAddress                   | xchng\_homeAddress     | Custom      | String    |
| businessAddress               | xchng\_businessAddress | Custom      | String    |
| department                    | xchng\_department      | Custom      | String    |
| profession                    | xchng\_profession      | Custom      | String    |
| createdAt                     | \_created\_at          | Default     | Date      |
| category                      | \_category             | Default     | String    |
| url                           | \_source\_uri          | Custom      | String    |
