Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Google Calendar data source connector field mappings

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
Google Calendar connector supports the following entities and field
mappings.

###### Supported entities and field mappings

- [Files](#gcal-field-mappings-files "#gcal-field-mappings-files")

## Files

Calendar

| Google Calendar field name | Index field name | Description | Data type |
| -------------------------- | ---------------- | ----------- | --------- |
| sourceUrl                  | \_sourceUrl      | Default     | String    |

Events

| Google Calendar field name | Index field name         | Description | Data type  |
| -------------------------- | ------------------------ | ----------- | ---------- |
| Location                   | gcal\_location           | Custom      | String     |
| eventStartTime             | gcal\_event\_start\_time | Custom      | Date       |
| eventEndTime               | gcal\_event\_end\_time   | Custom      | Date       |
| category                   | \_category               | Default     | String     |
| created                    | \_created\_at            | Default     | DateString |
| updated                    | \_last\_updated\_at      | Default     | Date       |
| htmlLink                   | \_source\_url            | Default     | String     |
| attendees                  | gcal\_attendees          | Custom      | String     |
| organizer                  | gcal\_organizer          | Custom      | String     |
| recurrence                 | gcal\_recurrence         | Custom      | String     |
