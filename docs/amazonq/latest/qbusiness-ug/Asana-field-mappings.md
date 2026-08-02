Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Amazon Q Business Asana data source connector field mappings (Preview)

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to
fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use
  reserved attributes to map commonly occurring document attributes in your data
  source to Amazon Q index fields.
- **Custom** – You can create custom attributes to
  map document attributes that are unique to your data to Amazon Q
  index fields.
  When you connect Amazon Q to a data source, Amazon Q
  automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a
  attribute mapping already available, or if you want to map additional document
  attributes to index fields, use the custom field mappings to specify how a data source
  attribute maps to an Amazon Q index field. You create field mappings by
  editing your data source after your application environment and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes-types.md "doc-attributes-types.md").

###### Important

Filtering using document attributes in chat is only supported through the
API.

The Amazon Q Asana connector supports the following entities
and the associated reserved and custom attributes.

###### Supported entities and field mappings

- [Projects](#Asana-field-mappings-projects "#Asana-field-mappings-projects")
- [Tasks](#Asana-field-mappings-tasks "#Asana-field-mappings-tasks")
- [Comments](#Asana-field-mappings-comments "#Asana-field-mappings-comments")

## Projects

Amazon Q supports crawling Asana Projects and offers the
following project field mappings.

| Asana field name    | Index field name       | Description | Data type   |
| ------------------- | ---------------------- | ----------- | ----------- |
| projectPermaLink    | \_source\_uri          | Default     | String      |
| projectCreatedDate  | \_created\_at          | Default     | Date        |
| projectModifiedDate | \_last\_updated\_at    | Default     | Date        |
| catagory            | \_catagory             | Default     | String      |
| isArchived          | asana\_archived        | Custom      | Custom      |
| dueOn               | asana\_dueOn           | Custom      | Date        |
| startOn             | asana\_startOn         | Custom      | String      |
| isPublicProject     | asana\_isPublicProject | Custom      | String      |
| ownerId             | asana\_ownerId         | Custom      | String      |
| ownerName           | asana\_ownerName       | Custom      | String      |
| teamId              | asana\_teamId          | Custom      | String list |
| teamName            | asana\_teamName        | Custom      | String list |
| workspaceId         | asana\_workspaceId     | Custom      | String      |
| workspaceName       | asana\_workspaceName   | Custom      | String      |
| isOrganization      | asana\_isOrganization  | Custom      | String      |

## Tasks

Amazon Q supports crawling Asana Tasks and offers the
following project field mappings.

| Asana field name | Index field name        | Description | Data type |
| ---------------- | ----------------------- | ----------- | --------- |
| taskPermaLink    | \_source\_uri           | Default     | String    |
| taskCreatedDate  | \_created\_at           | Default     | Date      |
| taskModifiedDate | \_last\_update\_at      | Default     | Date      |
| category         | \_category              | Default     | String    |
| assigneeId       | asana\_assigneeId       | Custom      | String    |
| assigneeName     | asana\_assigneeName     | Custom      | String    |
| isCompleted      | asana\_isCompleted      | Custom      | String    |
| dueOn            | asana\_dueOn            | Custom      | String    |
| isSubtask        | asana\_isSubtask        | Custom      | String    |
| topLevelTaskId   | asana\_topLevelTaskId   | Custom      | String    |
| topLevelTaskName | asana\_topLevelTaskName | Custom      | String    |
| section Id       | asana\_sectionId        | Custom      | String    |
| sectionName      | asana\_sectionName      | Custom      | String    |
| projectId        | asana\_projectId        | Custom      | String    |
| projectName      | asana\_projectName      | Custom      | String    |
| workspaceId      | asana\_workspaceId      | Custom      | String    |
| workspaceName    | asana\_workspaceName    | Custom      | String    |
| isOrganization   | asana\_isOrganization   | Custom      | String    |

## Comments

Amazon Q supports crawling Asana Comments and offers the
following project field mappings.

| Asana field name | Index field name      | Description | Data type |
| ---------------- | --------------------- | ----------- | --------- |
| commentPermaLink | \_source\_uri         | Default     | String    |
| category         | \_category            | Default     | String    |
| taskId           | asana\_taskId         | Custom      | String    |
| taskName         | asana\_taskName       | Custom      | String    |
| teamId           | asana\_teamId         | Custom      | String    |
| teamName         | asana\_teamName       | Custom      | String    |
| sectionId        | asana\_sectionId      | Custom      | String    |
| sectionName      | asana\_sectionName    | Custom      | String    |
| projectId        | asana\_projectId      | Custom      | String    |
| projectName      | asana\_projectName    | Custom      | String    |
| workspaceId      | asana\_workspaceId    | Custom      | String    |
| workspaceName    | asana\_workspaceName  | Custom      | String    |
| isOrganization   | asana\_isOrganization | Custom      | String    |
