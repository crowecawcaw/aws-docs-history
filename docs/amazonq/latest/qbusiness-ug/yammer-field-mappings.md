# Microsoft Yammer data source connector

field mappings

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
Yammer connector supports the following entities and the associated reserved
and custom attributes.

###### Note

You can map any Yammer field to the document title or document body
Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Message](#yammer-field-mappings-message "#yammer-field-mappings-message")
- [Attachment](#yammer-field-mappings-attachment "#yammer-field-mappings-attachment")
- [User](#yammer-field-mappings-user "#yammer-field-mappings-user")
- [Community](#yammer-field-mappings-community "#yammer-field-mappings-community")

## Message

Amazon Q supports crawling [Microsoft Yammer Messages](https://learn.microsoft.com/en-us/rest/api/yammer/messagesjson "https://learn.microsoft.com/en-us/rest/api/yammer/messagesjson") and offers the following message field
mappings.

| Microsoft Yammer field name | Index field name            | Description | Data type |
| --------------------------- | --------------------------- | ----------- | --------- | ------------- |
| id                          | ymr_id                      | Custom      | String    |
| message_type                | ymr_message_type            | Custom      | String    |
| api_url                     | ymr_api_url                 | Custom      | String    |
| group_id                    | ymr_group_id                | Custom      | String    |
| group_name                  | ymr_group_name              | Custom      | String    |
| in_private_conversation     | ymr_in_private_conversation | Custom      | String    |
| in_private_group            | ymr_in_private_group        | Custom      | String    |
| sender_email                | ymr_sender_email            | Custom      | String    |
| sender_id                   | ymr_sender_id               | Custom      | String    |
| sender_name                 | ymr_sender_name             | Custom      | String    |
| created_at                  | \_created_at                | Default     | Date      |
| web_url                     | \_source_uri                | Default     | String    | ## Attachment |
| Microsoft Yammer field name | Index field name            | Description | Data type |
| ---                         | ---                         | ---         | ---       |
| id                          | ymr_attachment_id           | Custom      | String    |
| name                        | ymr_attachment_name         | Custom      | String    |
| size                        | ymr_attachment_size         | Custom      | String    |
| url                         | ymr_attachment_url          | Custom      | String    |
| file_type                   | ymr_attachment_type         | Custom      | String    |
| created_at                  | \_created_at                | Default     | Date      |
| privacy                     | ymr_attachment_privacy      | Custom      | String    |
| group_name                  | ymr_attachment_group_name   | Custom      | String    |
| sender_email                | ymr_attachment_sender_email | Custom      | String    |
| web_url                     | \_source_uri                | Default     | String    | ## User       |
| Microsoft Yammer field name | Index field name            | Description | Data type |
| ---                         | ---                         | ---         | ---       |
| id                          | ymr_user_id                 | Custom      | String    |
| user_type                   | ymr_user_type               | Custom      | String    |
| state                       | ymr_user_state              | Custom      | String    |
| full_name                   | ymr_user_full_name          | Custom      | String    |
| activated_at                | \_created_at                | Default     | Date      |
| first_name                  | ymr_user_first_name         | Custom      | String    |
| last_name                   | ymr_user_last_name          | Custom      | String    |
| network_name                | ymr_user_network_name       | Custom      | String    |
| network_domains             | ymr_user_network_domains    | Custom      | String    |
| url                         | ymr_user_url                | Custom      | String    |
| name                        | ymr_user_name               | Custom      | String    |
| birth_date                  | ymr_user_birth_date         | Custom      | Date      |
| admin                       | ymr_user_admin              | Custom      | String    |
| verified_admin              | ymr_user_verified_admin     | Custom      | String    |
| contact                     | ymr_user_contact            | Custom      | String    |
| email                       | ymr_user_email              | Custom      | String    |
| web_url                     | \_source_uri                | Default     | String    | ## Community  |
| Microsoft Yammer field name | Index field name            | Description | Data type |
| ---                         | ---                         | ---         | ---       |
| id                          | ymr_community_id            | Custom      | String    |
| name                        | ymr_community_name          | Custom      | String    |
| email                       | ymr_community_email         | Custom      | String    |
| full_name                   | ymr_community_full_name     | Custom      | String    |
| description                 | ymr_community_description   | Custom      | String    |
| privacy                     | ymr_community_privacy       | Custom      | String    |
| url                         | ymr_community_url           | Custom      | String    |
| created_at                  | \_created_at                | Default     | Date      |
| state                       | ymr_community_state         | Custom      | String    |
| web_url                     | \_source_uri                | Default     | String    |
