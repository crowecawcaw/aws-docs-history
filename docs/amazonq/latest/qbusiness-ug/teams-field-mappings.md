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

| Microsoft Teams field name | Index field name    | Description | Data type   |
| -------------------------- | ------------------- | ----------- | ----------- |
| subject                    | tms_subject         | Custom      | String      |
| summary                    | tms_summary         | Custom      | String      |
| importance                 | tms_importance      | Custom      | String      |
| messageType                | tms_message_type    | Custom      | String      |
| sender                     | tms_sender          | Custom      | String      |
| sourceUrl                  | \_source_uri        | Default     | String      |
| attachments                | tms_attachments     | Custom      | String list |
| reactions                  | tms_reactions       | Custom      | String list |
| mentions                   | tms_mentions        | Custom      | String list |
| deletedAt                  | tms_last_deleted_at | Custom      | Date        |
| createdAt                  | \_created_at        | Default     | Date        |
| lastModifiedAt             | \_last_updated_at   | Default     | Date        |

## Chat attachments

| Microsoft Teams field name | Index field name     | Description | Data type      |
| -------------------------- | -------------------- | ----------- | -------------- |
| fileName                   | tms_name             | Custom      | String         |
| size                       | tms_file_size        | Custom      | Long (numeric) |
| title                      | tms_title            | Custom      | String         |
| sourceUrl                  | \_source_uri         | Default     | String         |
| lastModifiedBy             | tms_last_modified_by | Custom      | String         |
| createdBy                  | tms_created_by       | Custom      | String         |
| createdAt                  | \_created_at         | Default     | Date           |
| lastModifiedAt             | \_last_updated_at    | Default     | Date           |

## Channel posts

| Microsoft Teams field name | Index field name    | Description | Data type   |
| -------------------------- | ------------------- | ----------- | ----------- |
| subject                    | tms_subject         | Custom      | String      |
| summary                    | tms_summary         | Custom      | String      |
| importance                 | tms_importance      | Custom      | String      |
| messageType                | tms_message_type    | Custom      | String      |
| createdBy                  | tms_created_by      | Custom      | String      |
| deletedAt                  | tms_last_deleted_at | Custom      | Date        |
| sourceUrl                  | \_source_uri        | Default     | String      |
| mentions                   | tms_mentions        | Custom      | String list |
| reactions                  | tms_reactions       | Custom      | String list |
| attachments                | tms_attachments     | Custom      | String list |
| createdAt                  | \_created_at        | Default     | Date        |
| lastModifiedAt             | \_last_updated_at   | Default     | Date        |

## Channel file attachments

| Microsoft Teams field name | Index field name     | Description | Data type      |
| -------------------------- | -------------------- | ----------- | -------------- |
| fileName                   | tms_name             | Custom      | String         |
| size                       | tms_file_size        | Custom      | Long (numeric) |
| channelName                | tms_channel_name     | Custom      | String         |
| Title                      | tms_title            | Custom      | String         |
| sourceUrl                  | \_source_uri         | Default     | String         |
| createdBy                  | tms_created_by       | Custom      | String         |
| lastModifiedBy             | tms_last_modified_by | Custom      | String         |
| createdAt                  | \_created_at         | Default     | Date           |
| lastModifiedAt             | \_last_updated_at    | Default     | Date           |
| oneNoteDocument            | tms_onenote_document | Custom      | String         |
| oneNoteSection             | tms_onenote_section  | Custom      | String         |
| oneNotePage                | tms_onenote_page     | Custom      | String         |

## Wiki

| Microsoft Teams field name | Index field name     | Description | Data type      |
| -------------------------- | -------------------- | ----------- | -------------- |
| channelName                | tms_channel_name     | Custom      | String         |
| fileName                   | tms_name             | Custom      | String         |
| size                       | tms_file_size        | Custom      | Long (numeric) |
| createdBy                  | tms_created_by       | Custom      | String         |
| lastModifiedBy             | tms_last_modified_by | Custom      | String         |
| title                      | tms_title            | Custom      | String         |
| sourceUrl                  | \_source_uri         | Default     | String         |
| createdAt                  | \_created_at         | Default     | Date           |
| lastModifiedAt             | \_last_updated_at    | Default     | Date           |

## Meeting chats

| Microsoft Teams field name | Index field name    | Description | Data type   |
| -------------------------- | ------------------- | ----------- | ----------- |
| subject                    | tms_subject         | Custom      | String      |
| summary                    | tms_summary         | Custom      | String      |
| importance                 | tms_importance      | Custom      | String      |
| messageType                | tms_message_type    | Custom      | String      |
| Sender                     | tms_sender          | Custom      | String      |
| attachments                | tms_attachments     | Custom      | String list |
| mentions                   | tms_mentions        | Custom      | String list |
| reactions                  | tms_reactions       | Custom      | String list |
| sourceUrl                  | \_source_uri        | Default     | String      |
| deletedAt                  | tms_last_deleted_at | Custom      | Date        |
| createdAt                  | \_created_at        | Default     | Date        |
| lastModifiedAt             | \_last_updated_at   | Default     | Date        |

## Meeting details

| Microsoft Teams field name | Index field name     | Description | Data type |
| -------------------------- | -------------------- | ----------- | --------- |
| subject                    | tms_subject          | Custom      | String    |
| summary                    | tms_summary          | Custom      | String    |
| importance                 | tms_importance       | Custom      | String    |
| username                   | tms_from_user        | Custom      | String    |
| eventStartTime             | tms_event_start_time | Custom      | Date      |
| eventEndTime               | tms_event_end_time   | Custom      | Date      |
| sourceURL                  | \_source_uri         | Default     | String    |

## Meeting notes

| Microsoft Teams field name | Index field name     | Description | Data type |
| -------------------------- | -------------------- | ----------- | --------- |
| fileName                   | tms_name             | Custom      | String    |
| title                      | tms_title            | Custom      | String    |
| createdBy                  | tms_created_by       | Custom      | String    |
| lastModifiedBy             | tms_last_modified_by | Custom      | String    |
| sourceUrl                  | \_source_uri         | Default     | String    |
| createdAt                  | \_created_at         | Default     | Date      |
| lastModifiedAt             | \_last_updated_at    | Default     | Date      |

## Meeting files

| Microsoft Teams field name | Index field name     | Description | Data type      |
| -------------------------- | -------------------- | ----------- | -------------- |
| fileName                   | tms_name             | Custom      | String         |
| title                      | tms_title            | Custom      | String         |
| size                       | tms_file_size        | Custom      | Long (numeric) |
| sourceUrl                  | \_source_uri         | Default     | String         |
| createdBy                  | tms_created_by       | Custom      | String         |
| lastModifiedBy             | tms_last_modified_by | Custom      | String         |
| createdAt                  | \_created_at         | Default     | Date           |
| lastModifiedAt             | \_last_updated_at    | Default     | Date           |
