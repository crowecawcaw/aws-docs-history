# Reading from Jira Cloud entities

**Prerequisite**

A Jira Cloud object you would like to read from. You will need the object name such as Audit Record or Issue. The following table shows the supported entities.

**Supported entities for source**:

| Entity                              | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ----------------------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Audit Record                        | Yes             | Yes            | No                | Yes                | Yes                   |
| Issue                               | Yes             | Yes            | No                | Yes                | Yes                   |
| Issue Field                         | No              | No             | No                | Yes                | No                    |
| Issue Field Configuration           | Yes             | Yes            | No                | Yes                | Yes                   |
| Issue Link Type                     | No              | No             | No                | Yes                | No                    |
| Issue Notification Scheme           | Yes             | Yes            | No                | Yes                | Yes                   |
| Issue Security Scheme               | No              | No             | No                | Yes                | No                    |
| Issue Type Scheme                   | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Issue Type Screen Scheme            | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Issue Type                          | No              | No             | No                | Yes                | No                    |
| Jira Setting                        | Yes             | No             | No                | Yes                | No                    |
| Jira Setting Advanced               | No              | No             | No                | Yes                | No                    |
| Jira Setting Global                 | No              | No             | No                | Yes                | No                    |
| Label                               | No              | No             | No                | Yes                | Yes                   |
| Myself                              | Yes             | No             | No                | Yes                | No                    |
| Permission                          | No              | No             | No                | Yes                | No.                   |
| Project                             | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Project Category                    | No              | No             | No                | Yes                | No                    |
| Project Type                        | No              | No             | No                | Yes                | No                    |
| Server Info                         | No              | No             | No                | Yes                | No                    |
| Users                               | No              | No             | No.               | Yes                | No                    |
| Workflow                            | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Workflow Scheme                     | No              | Yes            | No                | Yes                | Yes                   |
| Workflow Scheme Project Association | Yes             | No             | No                | Yes                | No                    |
| Workflow Status                     | No              | No             | No                | Yes                | No                    |
| Workflow Status Category            | No              | No             | No                | Yes                | No                    |

**Example**:

```
jiracloud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="JiraCloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "audit-record",
        "API_VERSION": "v3"
    }
```

**Jira Cloud entity and field details**:

| Object                              | Field           | Data type                      | Filter operators supported |
| ----------------------------------- | --------------- | ------------------------------ | -------------------------- |
| Audit Record                        | filter          | String                         | "="                        |
| from                                | DateTime        | "="                            |
| to                                  | DateTime        | "="                            |
| id                                  | Integer         | N/A                            |
| summary                             | String          | N/A                            |
| remoteAddress                       | String          | N/A                            |
| authorAccountId                     | String          | N/A                            |
| created                             | String          | N/A                            |
| category                            | String          | N/A                            |
| eventSource                         | String          | N/A                            |
| description                         | String          | N/A                            |
| objectItem                          | Struct          | N/A                            |
| changedValues                       | List            | N/A                            |
| associatedItems                     | List            | N/A                            |
| Groups                              | groupName       | List                           | "="                        |
| name                                | String          | N/A                            |
| groupId                             | String          | "="                            |
| Issue                               | affectedVersion | String                         | "=, !="                    |
| assignee                            | String          | "=, !="                        |
| category                            | String          | "=, !="                        |
| component                           | String          | "=, !="                        |
| creator                             | String          | "=, !="                        |
| due                                 | DateTime        | N/A                            |
| epic_link                           | String          | "=, !="                        |
| filter                              | String          | "=, !="                        |
| fixVersion                          | String          | "=, !="                        |
| hierarchyLevel                      | Integer         | "=, !="                        |
| issueKey                            | String          | "=, !=, >, <, >=, <="          |
| issueLink                           | String          | "=, !="                        |
| issueLinkType                       | String          | "=, !="                        |
| labels                              | String          | "=, !="                        |
| lastViewed                          | DateTime        | "=, >, <, >=, <=, between"     |
| level                               | String          | "=, !="                        |
| parent                              | String          | "=, !="                        |
| priority                            | String          | "=, !="                        |
| project                             | String          | "=, !="                        |
| projectType                         | String          | "=, !="                        |
| reporter                            | String          | "=, !="                        |
| resolution                          | String          | "=, !="                        |
| resolved                            | DateTime        | "=, >, <, >=, <=, between"     |
| sprint                              | String          | "=, !="                        |
| status                              | String          | "=, !="                        |
| type                                | String          | "=, !="                        |
| updated                             | DateTime        | "=, >, <, >=, <=, between"     |
| voter                               | String          | "=, !="                        |
| votes                               | Integer         | "=, !=, <, >, <=, >=, between" |
| watcher                             | String          | "=, !="                        |
| watchers                            | Integer         | "=, !=, <, >, <=, >=, between" |
| workRatio                           | Integer         | "=, !=, <, >, <=, >=, between" |
| validateQuery                       | String          | "="                            |
| expand                              | String          | "="                            |
| fieldByKeys                         | Boolean         | "="                            |
| id                                  | String          | N/A                            |
| self                                | String          | N/A                            |
| key                                 | String          | N/A                            |
| renderedFields                      | Struct          | N/A                            |
| properties                          | List            | "="                            |
| names                               | Struct          | N/A                            |
| schema                              | Struct          | N/A                            |
| transitions                         | List            | N/A                            |
| operations                          | Struct          | N/A                            |
| editmeta                            | Struct          | N/A                            |
| changelog                           | Struct          | N/A                            |
| versionedRepresentations            | Struct          | N/A                            |
| fields                              | List            | "="                            |
| fieldsToInclude                     | Struct          | N/A                            |
| warningMessages                     | List            | N/A                            |
| created                             | DateTime        | N/A                            |
| worklogDate                         | DateTime        | N/A                            |
| IssueEvents                         | id              | Integer                        | N/A                        |
| name                                | String          | N/A                            |
| Issue Fields                        | id              | String                         | N/A                        |
| key                                 | String          | N/A                            |
| name                                | String          | N/A                            |
| custom                              | Boolean         | N/A                            |
| orderable                           | Boolean         | N/A                            |
| navigable                           | Boolean         | N/A                            |
| searchable                          | Boolean         | N/A                            |
| clauseNames                         | List            | N/A                            |
| scope                               | Struct          | N/A                            |
| schema                              | Struct          | N/A                            |
| Issue Field Configurations          | isDefault       | Boolean                        | "="                        |
| query                               | String          | "="                            |
| id                                  | Integer         | "="                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| Issue Link Type                     | id              | String                         | N/A                        |
| name                                | String          | N/A                            |
| inward                              | String          | N/A                            |
| outward                             | String          | N/A                            |
| self                                | String          | N/A                            |
| Issue Notification Schemes          | expand          | String                         | "="                        |
| self                                | String          | N/A                            |
| id                                  | Integer         | N/A                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| notificationSchemeEvents            | List            | N/A                            |
| scope                               | Struct          | N/A                            |
| Issue Priority                      | self            | String                         | N/A                        |
| statusColor                         | String          | N/A                            |
| description                         | String          | N/A                            |
| iconUrl                             | String          | N/A                            |
| name                                | String          | N/A                            |
| id                                  | String          | N/A                            |
| isDefault                           | Boolean         | N/A                            |
| Issue Resolutions                   | self            | String                         | N/A                        |
| id                                  | String          | N/A                            |
| description                         | String          | N/A                            |
| name                                | String          | N/A                            |
| Issue Security Scheme               | self            | String                         | N/A                        |
| id                                  | Integer         | N/A                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| defaultSecurityLevelId              | Integer         | N/A                            |
| levels                              | List            | N/A                            |
| Issue Type                          | self            | String                         | N/A                        |
| id                                  | String          | N/A                            |
| description                         | String          | N/A                            |
| iconUrl                             | String          | N/A                            |
| name                                | String          | N/A                            |
| subtask                             | Boolean         | N/A                            |
| avatarId                            | Integer         | N/A                            |
| entityId                            | String          | N/A                            |
| hierarchyLevel                      | Integer         | N/A                            |
| scope                               | Struct          | N/A                            |
| Issue Type Scheme                   | orderBy         | String                         | "="                        |
| expand                              | String          | "="                            |
| queryString                         | String          | "="                            |
| id                                  | String          | N/A                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| defaultIssueTypeId                  | String          | N/A                            |
| isDefault                           | Boolean         | N/A                            |
| Issue Type Screen Scheme            | queryString     | String                         | "="                        |
| orderBy                             | String          | "="                            |
| expand                              | String          | "="                            |
| id                                  | String          | "="                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| Jira Settings                       | key             | String                         | N/A                        |
| keyFilter                           | String          | "="                            |
| id                                  | String          | N/A                            |
| value                               | String          | N/A                            |
| name                                | String          | N/A                            |
| desc                                | String          | N/A                            |
| type                                | String          | N/A                            |
| defaultValue                        | String          | N/A                            |
| example                             | String          | N/A                            |
| allowedValues                       | List            | N/A                            |
| Jira Settings Advanced              | id              | String                         | N/A                        |
| key                                 | String          | N/A                            |
| value                               | String          | N/A                            |
| name                                | String          | N/A                            |
| desc                                | String          | N/A                            |
| type                                | String          | N/A                            |
| defaultValue                        | String          | N/A                            |
| example                             | String          | N/A                            |
| allowedValues                       | List            | N/A                            |
| Jira Settings Global                | votingEnabled   | Boolean                        | N/A                        |
| watchingEnabled                     | Boolean         | N/A                            |
| unassignedIssuesAllowed             | Boolean         | N/A                            |
| subTasksEnabled                     | Boolean         | N/A                            |
| issueLinkingEnabled                 | Boolean         | N/A                            |
| timeTrackingEnabled                 | Boolean         | N/A                            |
| attachmentsEnabled                  | Boolean         | N/A                            |
| timeTrackingConfiguration           | Struct          | N/A                            |
| Label                               | values          | List                           | N/A                        |
| Myself                              | expand          | String                         | "="                        |
| self                                | String          | N/A                            |
| accountId                           | String          | N/A                            |
| accountType                         | String          | N/A                            |
| emailAddress                        | String          | N/A                            |
| avatarUrls                          | String          | N/A                            |
| displayName                         | String          | N/A                            |
| active                              | Boolean         | N/A                            |
| timeZone                            | String          | N/A                            |
| locale                              | String          | N/A                            |
| groups                              | Struct          | N/A                            |
| applicationRoles                    | Struct          | N/A                            |
| Permission                          | id              | String                         | N/A                        |
| key                                 | String          | N/A                            |
| name                                | String          | N/A                            |
| type                                | String          | N/A                            |
| description                         | String          | N/A                            |
| havePermission                      | Boolean         | N/A                            |
| deprecatedKey                       | Boolean         | N/A                            |
| Project                             | orderBy         | String                         | "="                        |
| keys                                | List            | "="                            |
| query                               | String          | "="                            |
| typeKey                             | String          | "="                            |
| categoryId                          | Integer         | "="                            |
| action                              | String          | "="                            |
| expand                              | String          | "="                            |
| status                              | List            | "="                            |
| self                                | String          | N/A                            |
| id                                  | Integer         | "="                            |
| key                                 | String          | N/A                            |
| description                         | String          | N/A                            |
| lead                                | Struct          | N/A                            |
| components                          | List            | N/A                            |
| issueTypes                          | List            | N/A                            |
| url                                 | String          | N/A                            |
| email                               | String          | N/A                            |
| assigneeType                        | String          | N/A                            |
| versions                            | List            | N/A                            |
| name                                | String          | N/A                            |
| roles                               | Struct          | N/A                            |
| avatarUrls                          | Struct          | N/A                            |
| projectCategory                     | Struct          | N/A                            |
| projectTypeKey                      | String          | N/A                            |
| simplified                          | Boolean         | N/A                            |
| style                               | String          | N/A                            |
| favourite                           | Boolean         | N/A                            |
| isPrivate                           | Boolean         | N/A                            |
| issueTypeHierarchy                  | Struct          | N/A                            |
| permissions                         | Struct          | N/A                            |
| properties                          | List            | "="                            |
| uuid                                | String          | N/A                            |
| insight                             | Struct          | N/A                            |
| deleted                             | Boolean         | N/A                            |
| retentionTillDate                   | String          | N/A                            |
| deletedDate                         | String          | N/A                            |
| deletedBy                           | Struct          | N/A                            |
| archived                            | Boolean         | N/A                            |
| archivedDate                        | String          | N/A                            |
| archivedBy                          | Struct          | N/A                            |
| landedPageInfo                      | Struct          | N/A                            |
| Project Category                    | self            | String                         | N/A                        |
| id                                  | String          | N/A                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| Project Type                        | key             | String                         | N/A                        |
| formattedKey                        | String          | N/A                            |
| description                         | String          | N/A                            |
| descriptionI18nKey                  | String          | N/A                            |
| icon                                | String          | N/A                            |
| color                               | String          | N/A                            |
| Server Info                         | baseUrl         | String                         | N/A                        |
| version                             | String          | N/A                            |
| versionNumbers                      | List            | N/A                            |
| deploymentType                      | String          | N/A                            |
| buildNumber                         | Integer         | N/A                            |
| buildDate                           | DateTime        | N/A                            |
| serverTime                          | DateTime        | N/A                            |
| scmInfo                             | String          | N/A                            |
| serverTitle                         | String          | N/A                            |
| healthChecks                        | List            | N/A                            |
| Users                               | self            | String                         | N/A                        |
| accountId                           | String          | N/A                            |
| accountType                         | String          | N/A                            |
| emailAddress                        | String          | N/A                            |
| avatarUrls                          | Struct          | N/A                            |
| displayName                         | String          | N/A                            |
| active                              | Boolean         | N/A                            |
| timeZone                            | String          | N/A                            |
| locale                              | String          | N/A                            |
| groups                              | Struct          | N/A                            |
| applicationRoles                    | Struct          | N/A                            |
| expand                              | String          | N/A                            |
| Workflow                            | workflowName    | String                         | "="                        |
| expand                              | String          | "="                            |
| queryString                         | String          | "="                            |
| orderBy                             | String          | "="                            |
| isActive                            | Boolean         | "="                            |
| id                                  | Struct          | N/A                            |
| description                         | String          | N/A                            |
| transitions                         | List            | N/A                            |
| statuses                            | List            | N/A                            |
| isDefault                           | Boolean         | N/A                            |
| schemes                             | List            | N/A                            |
| projects                            | List            | N/A                            |
| hasDraftWorkflow                    | Boolean         | N/A                            |
| operations                          | Struct          | N/A                            |
| created                             | String          | N/A                            |
| updated                             | String          | N/A                            |
| Workflow Scheme                     | self            | String                         | N/A                        |
| id                                  | Integer         | N/A                            |
| name                                | String          | N/A                            |
| description                         | String          | N/A                            |
| defaultWorkflow                     | String          | N/A                            |
| issueTypeMappings                   | Struct          | N/A                            |
| originalDefaultWorkflow             | String          | N/A                            |
| originalIssueTypeMappings           | Struct          | N/A                            |
| draft                               | Boolean         | N/A                            |
| lastModifiedUser                    | Struct          | N/A                            |
| lastModified                        | String          | N/A                            |
| updateDraftIfNeeded                 | Boolean         | N/A                            |
| issueTypes                          | Struct          | N/A                            |
| Workflow Scheme Project Association | projectId       | Integer                        | "="                        |
| projectIds                          | List            | N/A                            |
| workflowScheme                      | Struct          | N/A                            |
| Workflow Status                     | self            | String                         | N/A                        |
| description                         | String          | N/A                            |
| iconUrl                             | String          | N/A                            |
| name                                | String          | N/A                            |
| id                                  | String          | N/A                            |
| StatusCategory                      | Struct          | N/A                            |
| Workflow Status Category            | self            | String                         | N/A                        |
| id                                  | String          | N/A                            |
| key                                 | String          | N/A                            |
| colorName                           | String          | N/A                            |
| name                                | String          | N/A                            |

## Partitioning queries

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With this parameter, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `NUM_PARTITIONS`: the number of partitions.

Example:

```
jiraCloud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="JiraCloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "issue",
        "API_VERSION": "v3",
        "NUM_PARTITIONS": "10"
    }
```
