Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Microsoft Teams data source connector field mappings

To help you structure data for retrieval and chat filtering, Amazon Q Business
crawls data source document attributes or metadata and maps them to fields in your Amazon Q index.

Amazon Q has reserved fields that it uses when querying your application. When
possible, Amazon Q automatically maps these built-in fields to attributes in your
data source. If a built-in field doesn't have a default mapping, or if you want to map
additional index fields, use the custom field mappings to specify how a data source
attribute maps to your Amazon Q application. You create field mappings by editing
your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through the API.

The Amazon Q
Teams connector supports the following entities and the associated reserved
and custom attributes.

###### Note

You can map any Teams field to the document title or document body
Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Chat messages](#teams-field-mappings-chat-messages "#teams-field-mappings-chat-messages")
- [Chat attachments](#teams-field-mappings-chat-attachments "#teams-field-mappings-chat-attachments")
- [Channel posts](#teams-field-mappings-channel-posts "#teams-field-mappings-channel-posts")
- [Channel file attachments](#teams-field-mappings-channel-file-attachments "#teams-field-mappings-channel-file-attachments")
- [Wiki](#teams-field-mappings-wiki "#teams-field-mappings-wiki")
- [Meeting chats](#teams-field-mappings-meeting-chats "#teams-field-mappings-meeting-chats")
- [Meeting details](#teams-field-mappings-meeting-details "#teams-field-mappings-meeting-details")
- [Meeting notes](#teams-field-mappings-meeting-notes "#teams-field-mappings-meeting-notes")
- [Meeting files](#teams-field-mappings-meeting-files "#teams-field-mappings-meeting-files")

## Chat messages

| Microsoft Teams field name | Index field name       | Description | Data type   |
| -------------------------- | ---------------------- | ----------- | ----------- |
| subject                    | tms\_subject           | Custom      | String      |
| summary                    | tms\_summary           | Custom      | String      |
| importance                 | tms\_importance        | Custom      | String      |
| messageType                | tms\_message\_type     | Custom      | String      |
| sender                     | tms\_sender            | Custom      | String      |
| sourceUrl                  | \_source\_uri          | Default     | String      |
| attachments                | tms\_attachments       | Custom      | String list |
| reactions                  | tms\_reactions         | Custom      | String list |
| mentions                   | tms\_mentions          | Custom      | String list |
| deletedAt                  | tms\_last\_deleted\_at | Custom      | Date        |
| createdAt                  | \_created\_at          | Default     | Date        |
| lastModifiedAt             | \_last\_updated\_at    | Default     | Date        |

## Chat attachments

| Microsoft Teams field name | Index field name        | Description | Data type      |
| -------------------------- | ----------------------- | ----------- | -------------- |
| fileName                   | tms\_name               | Custom      | String         |
| size                       | tms\_file\_size         | Custom      | Long (numeric) |
| title                      | tms\_title              | Custom      | String         |
| sourceUrl                  | \_source\_uri           | Default     | String         |
| lastModifiedBy             | tms\_last\_modified\_by | Custom      | String         |
| createdBy                  | tms\_created\_by        | Custom      | String         |
| createdAt                  | \_created\_at           | Default     | Date           |
| lastModifiedAt             | \_last\_updated\_at     | Default     | Date           |

## Channel posts

| Microsoft Teams field name | Index field name       | Description | Data type   |
| -------------------------- | ---------------------- | ----------- | ----------- |
| subject                    | tms\_subject           | Custom      | String      |
| summary                    | tms\_summary           | Custom      | String      |
| importance                 | tms\_importance        | Custom      | String      |
| messageType                | tms\_message\_type     | Custom      | String      |
| createdBy                  | tms\_created\_by       | Custom      | String      |
| deletedAt                  | tms\_last\_deleted\_at | Custom      | Date        |
| sourceUrl                  | \_source\_uri          | Default     | String      |
| mentions                   | tms\_mentions          | Custom      | String list |
| reactions                  | tms\_reactions         | Custom      | String list |
| attachments                | tms\_attachments       | Custom      | String list |
| createdAt                  | \_created\_at          | Default     | Date        |
| lastModifiedAt             | \_last\_updated\_at    | Default     | Date        |

## Channel file attachments

| Microsoft Teams field name | Index field name        | Description | Data type      |
| -------------------------- | ----------------------- | ----------- | -------------- |
| fileName                   | tms\_name               | Custom      | String         |
| size                       | tms\_file\_size         | Custom      | Long (numeric) |
| channelName                | tms\_channel\_name      | Custom      | String         |
| Title                      | tms\_title              | Custom      | String         |
| sourceUrl                  | \_source\_uri           | Default     | String         |
| createdBy                  | tms\_created\_by        | Custom      | String         |
| lastModifiedBy             | tms\_last\_modified\_by | Custom      | String         |
| createdAt                  | \_created\_at           | Default     | Date           |
| lastModifiedAt             | \_last\_updated\_at     | Default     | Date           |
| oneNoteDocument            | tms\_onenote\_document  | Custom      | String         |
| oneNoteSection             | tms\_onenote\_section   | Custom      | String         |
| oneNotePage                | tms\_onenote\_page      | Custom      | String         |

## Wiki

| Microsoft Teams field name | Index field name        | Description | Data type      |
| -------------------------- | ----------------------- | ----------- | -------------- |
| channelName                | tms\_channel\_name      | Custom      | String         |
| fileName                   | tms\_name               | Custom      | String         |
| size                       | tms\_file\_size         | Custom      | Long (numeric) |
| createdBy                  | tms\_created\_by        | Custom      | String         |
| lastModifiedBy             | tms\_last\_modified\_by | Custom      | String         |
| title                      | tms\_title              | Custom      | String         |
| sourceUrl                  | \_source\_uri           | Default     | String         |
| createdAt                  | \_created\_at           | Default     | Date           |
| lastModifiedAt             | \_last\_updated\_at     | Default     | Date           |

## Meeting chats

| Microsoft Teams field name | Index field name       | Description | Data type   |
| -------------------------- | ---------------------- | ----------- | ----------- |
| subject                    | tms\_subject           | Custom      | String      |
| summary                    | tms\_summary           | Custom      | String      |
| importance                 | tms\_importance        | Custom      | String      |
| messageType                | tms\_message\_type     | Custom      | String      |
| Sender                     | tms\_sender            | Custom      | String      |
| attachments                | tms\_attachments       | Custom      | String list |
| mentions                   | tms\_mentions          | Custom      | String list |
| reactions                  | tms\_reactions         | Custom      | String list |
| sourceUrl                  | \_source\_uri          | Default     | String      |
| deletedAt                  | tms\_last\_deleted\_at | Custom      | Date        |
| createdAt                  | \_created\_at          | Default     | Date        |
| lastModifiedAt             | \_last\_updated\_at    | Default     | Date        |

## Meeting details

| Microsoft Teams field name | Index field name        | Description | Data type |
| -------------------------- | ----------------------- | ----------- | --------- |
| subject                    | tms\_subject            | Custom      | String    |
| summary                    | tms\_summary            | Custom      | String    |
| importance                 | tms\_importance         | Custom      | String    |
| username                   | tms\_from\_user         | Custom      | String    |
| eventStartTime             | tms\_event\_start\_time | Custom      | Date      |
| eventEndTime               | tms\_event\_end\_time   | Custom      | Date      |
| sourceURL                  | \_source\_uri           | Default     | String    |

## Meeting notes

| Microsoft Teams field name | Index field name        | Description | Data type |
| -------------------------- | ----------------------- | ----------- | --------- |
| fileName                   | tms\_name               | Custom      | String    |
| title                      | tms\_title              | Custom      | String    |
| createdBy                  | tms\_created\_by        | Custom      | String    |
| lastModifiedBy             | tms\_last\_modified\_by | Custom      | String    |
| sourceUrl                  | \_source\_uri           | Default     | String    |
| createdAt                  | \_created\_at           | Default     | Date      |
| lastModifiedAt             | \_last\_updated\_at     | Default     | Date      |

## Meeting files

| Microsoft Teams field name | Index field name        | Description | Data type      |
| -------------------------- | ----------------------- | ----------- | -------------- |
| fileName                   | tms\_name               | Custom      | String         |
| title                      | tms\_title              | Custom      | String         |
| size                       | tms\_file\_size         | Custom      | Long (numeric) |
| sourceUrl                  | \_source\_uri           | Default     | String         |
| createdBy                  | tms\_created\_by        | Custom      | String         |
| lastModifiedBy             | tms\_last\_modified\_by | Custom      | String         |
| createdAt                  | \_created\_at           | Default     | Date           |
| lastModifiedAt             | \_last\_updated\_at     | Default     | Date           |
