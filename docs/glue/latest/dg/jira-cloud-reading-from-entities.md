

# Reading from Jira Cloud entities
<a name="jira-cloud-reading-from-entities"></a>

**Prerequisite**

A Jira Cloud object you would like to read from. You will need the object name such as Audit Record or Issue. The following table shows the supported entities.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Audit Record | Yes | Yes | No | Yes | Yes | 
| Issue | Yes | Yes | No | Yes | Yes | 
| Issue Field | No | No | No | Yes | No | 
| Issue Field Configuration | Yes | Yes | No | Yes | Yes | 
| Issue Link Type | No | No | No | Yes | No | 
| Issue Notification Scheme | Yes | Yes | No | Yes | Yes | 
| Issue Security Scheme | No | No | No | Yes | No | 
| Issue Type Scheme | Yes | Yes | Yes | Yes | Yes | 
| Issue Type Screen Scheme | Yes | Yes | Yes | Yes | Yes | 
| Issue Type | No | No | No | Yes | No | 
| Jira Setting | Yes | No | No | Yes | No | 
| Jira Setting Advanced | No | No | No | Yes | No | 
| Jira Setting Global | No | No | No | Yes | No | 
| Label | No | No | No | Yes | Yes | 
| Myself | Yes | No | No | Yes | No | 
| Permission | No | No | No | Yes | No. | 
| Project | Yes | Yes | Yes | Yes | Yes | 
| Project Category | No | No | No | Yes | No | 
| Project Type | No | No | No | Yes | No | 
| Server Info | No | No | No | Yes | No | 
| Users | No | No | No. | Yes | No | 
| Workflow | Yes | Yes | Yes | Yes | Yes | 
| Workflow Scheme | No | Yes | No | Yes | Yes | 
| Workflow Scheme Project Association | Yes | No | No | Yes | No | 
| Workflow Status | No | No | No | Yes | No | 
| Workflow Status Category | No | No | No | Yes | No | 

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



- **Audit Record**
  - **Field:** filter / **Data type:** String / **Filter operators supported:** "="
  - **Field:** from / **Data type:** DateTime / **Filter operators supported:** "="
  - **Field:** to / **Data type:** DateTime / **Filter operators supported:** "="
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** summary / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** remoteAddress / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** authorAccountId / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** created / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** category / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** eventSource / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** objectItem / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** changedValues / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** associatedItems / **Data type:** List / **Filter operators supported:** N/A

- **Groups**
  - **Field:** groupName / **Data type:** List / **Filter operators supported:** "="
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** groupId / **Data type:** String / **Filter operators supported:** "="

- **Issue**
  - **Field:** affectedVersion / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** assignee / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** category / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** component / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** creator / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** due / **Data type:** DateTime / **Filter operators supported:** N/A
  - **Field:** epic\_link / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** filter / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** fixVersion / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** hierarchyLevel / **Data type:** Integer / **Filter operators supported:** "=, \!="
  - **Field:** issueKey / **Data type:** String / **Filter operators supported:** "=, \!=, >, <, >=, <="
  - **Field:** issueLink / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** issueLinkType / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** labels / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** lastViewed / **Data type:** DateTime / **Filter operators supported:** "=, >, <, >=, <=, between"
  - **Field:** level / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** parent / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** priority / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** project / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** projectType / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** reporter / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** resolution / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** resolved / **Data type:** DateTime / **Filter operators supported:** "=, >, <, >=, <=, between"
  - **Field:** sprint / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** status / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** type / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** updated / **Data type:** DateTime / **Filter operators supported:** "=, >, <, >=, <=, between"
  - **Field:** voter / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** votes / **Data type:** Integer / **Filter operators supported:** "=, \!=, <, >, <=, >=, between"
  - **Field:** watcher / **Data type:** String / **Filter operators supported:** "=, \!="
  - **Field:** watchers / **Data type:** Integer / **Filter operators supported:** "=, \!=, <, >, <=, >=, between"
  - **Field:** workRatio / **Data type:** Integer / **Filter operators supported:** "=, \!=, <, >, <=, >=, between"
  - **Field:** validateQuery / **Data type:** String / **Filter operators supported:** "="
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** fieldByKeys / **Data type:** Boolean / **Filter operators supported:** "="
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** renderedFields / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** properties / **Data type:** List / **Filter operators supported:** "="
  - **Field:** names / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** schema / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** transitions / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** operations / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** editmeta / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** changelog / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** versionedRepresentations / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** fields / **Data type:** List / **Filter operators supported:** "="
  - **Field:** fieldsToInclude / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** warningMessages / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** created / **Data type:** DateTime / **Filter operators supported:** N/A
  - **Field:** worklogDate / **Data type:** DateTime / **Filter operators supported:** N/A

- **IssueEvents**
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A

- **Issue Fields**
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** custom / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** orderable / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** navigable / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** searchable / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** clauseNames / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** scope / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** schema / **Data type:** Struct / **Filter operators supported:** N/A

- **Issue Field Configurations**
  - **Field:** isDefault / **Data type:** Boolean / **Filter operators supported:** "="
  - **Field:** query / **Data type:** String / **Filter operators supported:** "="
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** "="
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A

- **Issue Link Type**
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** inward / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** outward / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A

- **Issue Notification Schemes**
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** notificationSchemeEvents / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** scope / **Data type:** Struct / **Filter operators supported:** N/A

- **Issue Priority**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** statusColor / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** iconUrl / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** isDefault / **Data type:** Boolean / **Filter operators supported:** N/A

- **Issue Resolutions**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A

- **Issue Security Scheme**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** defaultSecurityLevelId / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** levels / **Data type:** List / **Filter operators supported:** N/A

- **Issue Type**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** iconUrl / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** subtask / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** avatarId / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** entityId / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** hierarchyLevel / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** scope / **Data type:** Struct / **Filter operators supported:** N/A

- **Issue Type Scheme**
  - **Field:** orderBy / **Data type:** String / **Filter operators supported:** "="
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** queryString / **Data type:** String / **Filter operators supported:** "="
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** defaultIssueTypeId / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** isDefault / **Data type:** Boolean / **Filter operators supported:** N/A

- **Issue Type Screen Scheme**
  - **Field:** queryString / **Data type:** String / **Filter operators supported:** "="
  - **Field:** orderBy / **Data type:** String / **Filter operators supported:** "="
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** id / **Data type:** String / **Filter operators supported:** "="
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A

- **Jira Settings**
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** keyFilter / **Data type:** String / **Filter operators supported:** "="
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** value / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** desc / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** type / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** defaultValue / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** example / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** allowedValues / **Data type:** List / **Filter operators supported:** N/A

- **Jira Settings Advanced**
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** value / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** desc / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** type / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** defaultValue / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** example / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** allowedValues / **Data type:** List / **Filter operators supported:** N/A

- **Jira Settings Global**
  - **Field:** votingEnabled / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** watchingEnabled / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** unassignedIssuesAllowed / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** subTasksEnabled / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** issueLinkingEnabled / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** timeTrackingEnabled / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** attachmentsEnabled / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** timeTrackingConfiguration / **Data type:** Struct / **Filter operators supported:** N/A

- **Label**
  - **Field:** values
  - **Data type:** List
  - **Filter operators supported:** N/A

- **Myself**
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** accountId / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** accountType / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** emailAddress / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** avatarUrls / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** displayName / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** active / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** timeZone / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** locale / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** groups / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** applicationRoles / **Data type:** Struct / **Filter operators supported:** N/A

- **Permission**
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** type / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** havePermission / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** deprecatedKey / **Data type:** Boolean / **Filter operators supported:** N/A

- **Project**
  - **Field:** orderBy / **Data type:** String / **Filter operators supported:** "="
  - **Field:** keys / **Data type:** List / **Filter operators supported:** "="
  - **Field:** query / **Data type:** String / **Filter operators supported:** "="
  - **Field:** typeKey / **Data type:** String / **Filter operators supported:** "="
  - **Field:** categoryId / **Data type:** Integer / **Filter operators supported:** "="
  - **Field:** action / **Data type:** String / **Filter operators supported:** "="
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** status / **Data type:** List / **Filter operators supported:** "="
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** "="
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** lead / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** components / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** issueTypes / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** url / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** email / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** assigneeType / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** versions / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** roles / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** avatarUrls / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** projectCategory / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** projectTypeKey / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** simplified / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** style / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** favourite / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** isPrivate / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** issueTypeHierarchy / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** permissions / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** properties / **Data type:** List / **Filter operators supported:** "="
  - **Field:** uuid / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** insight / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** deleted / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** retentionTillDate / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** deletedDate / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** deletedBy / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** archived / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** archivedDate / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** archivedBy / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** landedPageInfo / **Data type:** Struct / **Filter operators supported:** N/A

- **Project Category**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A

- **Project Type**
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** formattedKey / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** descriptionI18nKey / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** icon / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** color / **Data type:** String / **Filter operators supported:** N/A

- **Server Info**
  - **Field:** baseUrl / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** version / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** versionNumbers / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** deploymentType / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** buildNumber / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** buildDate / **Data type:** DateTime / **Filter operators supported:** N/A
  - **Field:** serverTime / **Data type:** DateTime / **Filter operators supported:** N/A
  - **Field:** scmInfo / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** serverTitle / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** healthChecks / **Data type:** List / **Filter operators supported:** N/A

- **Users**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** accountId / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** accountType / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** emailAddress / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** avatarUrls / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** displayName / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** active / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** timeZone / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** locale / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** groups / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** applicationRoles / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** expand / **Data type:** String / **Filter operators supported:** N/A

- **Workflow**
  - **Field:** workflowName / **Data type:** String / **Filter operators supported:** "="
  - **Field:** expand / **Data type:** String / **Filter operators supported:** "="
  - **Field:** queryString / **Data type:** String / **Filter operators supported:** "="
  - **Field:** orderBy / **Data type:** String / **Filter operators supported:** "="
  - **Field:** isActive / **Data type:** Boolean / **Filter operators supported:** "="
  - **Field:** id / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** transitions / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** statuses / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** isDefault / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** schemes / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** projects / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** hasDraftWorkflow / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** operations / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** created / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** updated / **Data type:** String / **Filter operators supported:** N/A

- **Workflow Scheme**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** Integer / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** defaultWorkflow / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** issueTypeMappings / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** originalDefaultWorkflow / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** originalIssueTypeMappings / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** draft / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** lastModifiedUser / **Data type:** Struct / **Filter operators supported:** N/A
  - **Field:** lastModified / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** updateDraftIfNeeded / **Data type:** Boolean / **Filter operators supported:** N/A
  - **Field:** issueTypes / **Data type:** Struct / **Filter operators supported:** N/A

- **Workflow Scheme Project Association**
  - **Field:** projectId / **Data type:** Integer / **Filter operators supported:** "="
  - **Field:** projectIds / **Data type:** List / **Filter operators supported:** N/A
  - **Field:** workflowScheme / **Data type:** Struct / **Filter operators supported:** N/A

- **Workflow Status**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** description / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** iconUrl / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** StatusCategory / **Data type:** Struct / **Filter operators supported:** N/A

- **Workflow Status Category**
  - **Field:** self / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** id / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** key / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** colorName / **Data type:** String / **Filter operators supported:** N/A
  - **Field:** name / **Data type:** String / **Filter operators supported:** N/A



## Partitioning queries
<a name="jira-cloud-reading-partitioning-queries"></a>

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With this parameter, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `NUM_PARTITIONS`: the number of partitions.

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