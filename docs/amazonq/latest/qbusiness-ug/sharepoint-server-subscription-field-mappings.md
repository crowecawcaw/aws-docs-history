# Amazon Q Business

SharePoint Server (Subscription Edition) data source connector field mappings

To help you structure data for retrieval and chat filtering, Amazon Q Business
crawls data source document attributes or metadata and maps them to fields in your
Amazon Q index.

Amazon Q has reserved fields that it uses when querying your application. When
possible, Amazon Q automatically maps these built-in fields to attributes in your data
source. If a built-in field doesn't have a default mapping, or if you want to map
additional index fields, use the custom field mappings to specify how a data source
attribute maps to your Amazon Q application. You create field mappings by editing your
data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](doc-attributes-types.md "doc-attributes-types.md").

###### Important

Filtering using document attributes in chat is only supported through the
API.

The Amazon Q SharePoint connector supports the following entities and
the associated reserved and custom attributes.

###### Important

If you map any SharePoint Server (Subscription Edition) field to Amazon Q document title and document body fields,
Amazon Q will generate responses from data in the document title and body.

###### Note

You can map any SharePoint field to the document title or document
body Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Files](#sharepoint-field-mappings-files "#sharepoint-field-mappings-files")
- [Events](#sharepoint-field-mappings-events "#sharepoint-field-mappings-events")
- [Pages](#sharepoint-field-mappings-pages "#sharepoint-field-mappings-pages")
- [Links](#sharepoint-field-mappings-links "#sharepoint-field-mappings-links")
- [Attachments](#sharepoint-field-mappings-attachments "#sharepoint-field-mappings-attachments")
- [Comments](#sharepoint-field-mappings-comments "#sharepoint-field-mappings-comments")

## Files

| SharePoint field name | Index field name      | Description | Data type      |
| --------------------- | --------------------- | ----------- | -------------- | -------------- |
| title                 | sp_title              | Custom      | String         |
| sourceUri             | \_source_uri          | Default     | String         |
| checkInComment        | sp_checkInComment     | Custom      | String         |
| size                  | sp_sizeLong           | Custom      | Long (numeric) |
| lastModifiedDateTime  | \_last_updated_at     | Default     | Date           |
| createdAt             | \_created_at          | Default     | Date           |
| author                | \_authors             | Default     | String list    |
| majorVersion          | sp_majorVersion       | Custom      | String         |
| uiVersionLabel        | sp_uiVersionLabel     | Custom      | String         |
| uniqueId              | sp_uniqueId           | Custom      | String         |
| irmEnabled            | sp_irmEnabled         | Custom      | String         |
| checkOutType          | sp_checkOutType       | Custom      | String         |
| category              | \_category            | Default     | String         |
| modifiedBy            | sp_modifiedBy         | Custom      | String         |
| level                 | sp_level              | Custom      | String         |
| uiVersion             | sp_uiVersion          | Custom      | String         |
| contentTag            | sp_contentTag         | Custom      | String         |
| eTag                  | sp_eTag               | Custom      | String         |
| oneNoteDocument       | sp_oneNoteDocument    | Custom      | String         |
| oneNoteSection        | sp_oneNoteSection     | Custom      | String         |
| oneNotePage           | sp_oneNotePage        | Custom      | String         | ## Events      |
| SharePoint field name | Index field name      | Description | Data type      |
| ---                   | ---                   | ---         | ---            |
| title                 | sp_title              | Custom      | String         |
| lastModifiedDateTime  | \_last_updated_at     | Default     | Date           |
| sourceUri             | \_source_uri          | Default     | String         |
| attachments           | sp_hasAttachments     | Custom      | String         |
| createdDate           | \_created_at          | Default     | Date           |
| authorId              | sp_authorId           | Custom      | String         |
| editorId              | sp_editorId           | Custom      | String         |
| location              | sp_location           | Custom      | String         |
| eventDate             | sp_eventDate          | Custom      | Date           |
| eventEndDate          | sp_eventEndDate       | Custom      | Date           |
| ifRecurrence          | sp_ifRecurrence       | Custom      | String         |
| ifAllDayEvent         | sp_ifAllDayEvent      | Custom      | String         |
| category              | \_category            | Default     | String         |
| eventCategory         | sp_eventcategory      | Custom      | String         | ## Pages       |
| SharePoint field name | Index field name      | Description | Data type      |
| ---                   | ---                   | ---         | ---            |
| createdDateTime       | \_created_at          | Default     | Date           |
| lastModifiedDateTime  | \_last_updated_at     | Default     | Date           |
| title                 | sp_title              | Custom      | String         |
| sourceUri             | \_source_uri          | Default     | String         |
| firstPublishedDate    | sp_firstPublishedDate | Custom      | Date           |
| authorId              | sp_authorId           | Custom      | String         |
| editorId              | sp_editorId           | Custom      | String         |
| category              | \_category            | Default     | String         | ## Links       |
| SharePoint field name | Index field name      | Description | Data type      |
| ---                   | ---                   | ---         | ---            |
| createdAt             | \_created_at          | Default     | Date           |
| lastModifiedDateTime  | \_last_updated_at     | Default     | Date           |
| title                 | sp_title              | Custom      | String         |
| sourceUri             | \_source_uri          | Default     | String         |
| fileType              | sp_fileType           | Custom      | String         |
| fileDirPath           | sp_fileDirPath        | Custom      | String         |
| firstPublishedDate    | sp_firstPublishedDate | Custom      | Date           |
| authorId              | sp_authorId           | Custom      | String         |
| editorId              | sp_editorId           | Custom      | String         |
| category              | \_category            | Default     | String         |
| size                  | sp_sizeLong           | Custom      | Long (numeric) | ## Attachments |
| SharePoint field name | Index field name      | Description | Data type      |
| ---                   | ---                   | ---         | ---            |
| title                 | sp\_\_title           | Custom      | String         |
| parentCreatedDate     | \_created_at          | Default     | Date           |
| sourceUri             | \_source_uri          | Default     | String         |
| parentModifiedDate    | \_last_updated_at     | Custom      | Date           |
| parentListId          | sp_parentListId       | Custom      | String         |
| parentTitle           | sp_parentTitle        | Custom      | String         |
| category              | \_category            | Default     | String         | ## Comments    |
| SharePoint field name | Index field name      | Description | Data type      |
| ---                   | ---                   | ---         | ---            |
| createdDateTime       | \_created_at          | Default     | Date           |
| likedBy               | sp_likedBy            | Custom      | String         |
| sourceUri             | \_source_uri          | Custom      | String         |
| isReply               | sp_isReply            | Custom      | String         |
| author                | \_authors             | Default     | String list    |
| listId                | sp_listId             | Custom      | String         |
| category              | \_category            | Default     | String         |
| replyCount            | sp_replyCount         | Custom      | String         |
| parentTitle           | sp_parentTitle        | Custom      | String         |
