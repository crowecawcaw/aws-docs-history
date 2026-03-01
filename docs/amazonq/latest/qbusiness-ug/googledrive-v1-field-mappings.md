# Google Drive data source connector field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

The Amazon Q
Google Drive connector supports the following entities and the
associated reserved and custom attributes.

## Files

| Google Drive field name | Index field name  | Description | Data type      |
| ----------------------- | ----------------- | ----------- | -------------- |
| authors                 | \_authors         | Default     | String list    |
| mimeType                | gd_file_mime_type | Custom      | String         |
| size                    | gd_size           | Custom      | Long (numeric) |
| webViewLink             | \_source_uri      | Default     | String         |
| createdAt               | \_created_at      | Default     | Date           |
| modifiedAt              | \_last_updated_at | Default     | Date           |

## Comments

| Google Drive field name | Index field name  | Description | Data type   |
| ----------------------- | ----------------- | ----------- | ----------- |
| authors                 | \_authors         | Default     | String list |
| commentType             | gd_type           | Custom      | String      |
| createdAt               | \_created_at      | Default     | Date        |
| modifiedAt              | \_last_updated_at | Default     | Date        |
