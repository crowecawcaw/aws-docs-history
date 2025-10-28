# Filtering on user context

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

You can filter a user's search results based on the user or their group access to
documents. You can use a user token, user ID, or user attribute to filter
documents.

User context filtering is a kind of personalized search with the benefit of
controlling access to documents. For example, not all teams that search the company
portal for information should access top-secret company documents, nor are these
documents relevant to all users. Only specific users or groups of teams given access to
top-secret documents should see these documents in their search results.

When a document is indexed into Amazon Kendra, a corresponding access control
list (ACL) is ingested for most documents. The ACL specifies which user names and group
names are allowed or denied access to the document. Documents without an ACL are public
documents.

Amazon Kendra can extract the user or group information associated with each
document for most data sources. For example, a document in Quip can include a 'share'
list of select users that are given access to the document. If you use an S3 bucket as a
data source, you provide a [JSON file](s3-acl.md "s3-acl.md") for your ACL and include the S3
path to this file as part of the data source configuration. If you add documents
directly to an index, you specify the ACL in the [Principal](../APIReference/API_Principal.md "../APIReference/API_Principal.md") object as part
of the document object in the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
API.

If you're using an Amazon Kendra Enterprise or Developer Edition index, you can use the [CreateAccessControlConfiguration](../APIReference/API_CreateAccessControlConfiguration.md "../APIReference/API_CreateAccessControlConfiguration.md") API to re-configure your existing document
level access control without indexing all of your documents again. For example, your
index contains top-secret company documents that only certain employees or users should
access. One of these users leaves the company or switches to a team that should be
blocked from accessing top-secret documents. The user still has access to top-secret
documents because the user had access when your documents were previously indexed. You
can create a specific access control configuration for the user with deny access. You
can later update the access control configuration to allow access in the case the user
returns to the company and re-joins the 'top-secret' team. You can re-configure access
control for your documents as circumstances change.

To apply your access control configuration to certain documents, you call the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API with the `AccessControlConfigurationId`
included in the [Document](../APIReference/API_Document.md "../APIReference/API_Document.md") object. If you
use an S3 bucket as a data source, you update the `.metadata.json` with the
`AccessControlConfigurationId` and synchronize your data source. Amazon Kendra currently only supports access control configuration for S3 data sources
and documents indexed using the `BatchPutDocument` API.

## Filtering by user token

###### Important

Amazon Kendra GenAI Enterprise Edition indices don't support token-based user access
control.

When you query an index, you can use a user token to filter search results based
on the user or their group access to documents. When you issue a query, Amazon Kendra extracts and validates the token, pulls and checks the user and group
information, and runs the query. All of the documents the user has access to,
including public documents, are returned. For more information, see [Token-based user access control](create-index-access-control.md "create-index-access-control.md").

You provide the user token in the [UserContext](../APIReference/API_UserContext.md "../APIReference/API_UserContext.md") object
and pass this in the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API.

The following shows how to include a user token.

```
response = kendra.query(
    QueryText = query,
    IndexId = index,
    UserToken = {
        Token = "`token`"
    })
```

You can map users to groups. When you use user-context filtering, it is not
required to include all of the groups that a user belongs to when you issue the
query. With the [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md") API, you can map users to their groups. If you do
not want to use the `PutPrincipalMapping` API, you must provide the user
name and all the groups the user belongs to when you issue a query. You can also
fetch access levels of groups and users in your IAM Identity Center identity source by using the
[UserGroupResolutionConfiguration](../APIReference/API_UserGroupResolutionConfiguration.md "../APIReference/API_UserGroupResolutionConfiguration.md") object.

## Filtering by user ID and

group

When you query an index, you can use the user ID and group to filter search
results based on the user or their group access to documents. When you issue a
query, Amazon Kendra checks the user and group information and runs the query.
All of the documents relevant to the query that the user has access to, including
public documents, are returned.

You can also filter search results by data sources that users and groups have
access to. Specifying a data source is useful if a group is tied to multiple data
sources, but you only want the group to access documents of a certain data source.
For example, the groups "Research", "Engineering", and "Sales and Marketing" are all
tied to the company's documents stored in the data sources Confluence and
Salesforce. However, "Sales and Marketing" team only needs access to
customer-related documents stored in Salesforce. So when sales and marketing users
search for customer-related documents, they can see documents from Salesforce in
their results. Users who do not work in sales and marketing do not see Salesforce
documents in their search results.

You provide the user, groups and data sources information in the [UserContext](../APIReference/API_UserContext.md "../APIReference/API_UserContext.md") object and pass this in the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API. The user ID,
and the list of groups and data sources should match the name you specify in the
[Principal](../APIReference/API_Principal.md "../APIReference/API_Principal.md") object to identify the user, groups, and data sources. With
the `Principal` object, you can add a user, group, or data source to
either an allow list or a deny list for accessing a document.

You are required to provide one of the following:

- User and groups information, and (optional) data sources
  information.
- Only the user information if you map your users to groups and data sources
  using the [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md") API. You can also fetch access levels of
  groups and users in your IAM Identity Center identity source by using the [UserGroupResolutionConfiguration](../APIReference/API_UserGroupResolutionConfiguration.md "../APIReference/API_UserGroupResolutionConfiguration.md") object.

If this information is not included in the query, Amazon Kendra returns all
documents. If you provide this information, only documents with matching user IDs,
groups, and data sources are returned.

The following shows how to include user ID, groups, and data sources.

```
response = kendra.query(
    QueryText = query,
    IndexId = index,
    UserContext={'Token': '`string`', 'UserId': '`string`', 'Groups': [ '`string`', ], 'DataSourceGroups': [ { 'GroupId': '`string`', 'DataSourceId': '`string`' }, ] },)
```

## Filtering by user attribute

When you query an index, you can use built-in attributes `_user_id` and
`_group_id` to filter search results based on the user and their
group access to documents. You can set up to 100 group identifiers. When you issue a
query, Amazon Kendra checks the user and group information and runs the query.
All documents relevant to the query that the user has access to, including public
documents, are returned.

You provide the user and group attributes in the [AttributeFilter](../APIReference/API_AttributeFilter.md "../APIReference/API_AttributeFilter.md") object and pass this in the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API.

The following example shows a request that filters the query response based on the
user ID and the groups "HR" and "IT", which the user belongs to. The query will
return any document that has the user or the "HR" or "IT" groups in the allow list.
If the user or either group is in the deny list for a document, the document is not
returned.

```
response = kendra.query(
        QueryText = query,
        IndexId = index,
        AttributeFilter = {
            "OrAllFilters": [
                {
                    "EqualsTo": {
                        "Key": "_user_id",
                        "Value": {
                            "StringValue": "user1"
                        }
                     }
                },
                {
                    "EqualsTo": {
                        "Key": "_group_ids",
                        "Value": {
                            "StringListValue": ["HR", "IT"]
                        }
                    }
                }
            ]
        }
        )
```

You can also specify which data source a group can access in the
`Principal` object.

###### Note

User context filtering isn't an authentication or authorization control for
your content. It doesn't do user authentication on the user and groups sent to
the `Query` API. It is up to your application to ensure that the user
and group information sent to `Query` API is authenticated and
authorized.

There is an implementation of user context filtering for each data source. The
following section describes each implementation.

###### Topics

- [User context filtering for documents added
  directly to an index](#context-filter-batch "#context-filter-batch")
- [User context filtering for frequently asked
  questions](#context-filter-faq "#context-filter-faq")
- [User context filtering for data
  sources](#datasource-context-filter "#datasource-context-filter")

## User context filtering for documents added

directly to an index

When you add documents directly to an index using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API, Amazon Kendra gets user and group
information from the `AccessControlList` field of the document. You
provide an access control list (ACL) for your documents and the ACL is ingested with
your documents.

You specify the ACL in the [Principal](../APIReference/API_Principal.md "../APIReference/API_Principal.md") object as
part of the [Document](../APIReference/API_Document.md "../APIReference/API_Document.md") object in
the `BatchPutDocument` API. You provide the following information:

- The access that the user or group should have. You can say
  `ALLOW` or `DENY`.
- The type of entity. You can say `USER` or
  `GROUP`.
- The name of the user or group.

You can add up to 200 entries in the `AccessControlList` field.

## User context filtering for frequently asked

questions

When you [add a FAQ](../APIReference/API_CreateFaq.md "../APIReference/API_CreateFaq.md") to an
index, Amazon Kendra gets user and group information from the
`AccessControlList` object/field of the FAQ JSON file. You can also
use a FAQ CSV file with custom fields or attributes for access control.

You provide the following information:

- The access that the user or group should have. You can say
  `ALLOW` or `DENY`.
- The type of entity. You can say `USER` or
  `GROUP`.
- The name of the user or group.

For more information, see [FAQ files](in-creating-faq.md "in-creating-faq.md").

## User context filtering for data

sources

Amazon Kendra also crawls user and group access control list (ACL)
information from supported data source connectors. This is useful for user context
filtering, where search results are filtered based on the user or their group access
to documents.

###### Important

Amazon Kendra GenAI Enterprise Edition indices support only v2.0 Amazon Kendra data source
connectors.

###### Topics

- [User context filtering for Adobe Experience
  Manager data sources](#context-filter-aem "#context-filter-aem")
- [User context filtering for Alfresco
  data sources](#context-filter-alfresco "#context-filter-alfresco")
- [User context filtering for Aurora (MySQL) data sources](#context-filter-aurora-mysql "#context-filter-aurora-mysql")
- [User context filtering for
  Aurora (PostgreSQL) data sources](#context-filter-aurora-postgresql "#context-filter-aurora-postgresql")
- [User context filtering for Amazon FSx data sources](#context-filter-fsx "#context-filter-fsx")
- [User context filtering for database data
  sources](#context-filter-jdbc "#context-filter-jdbc")
- [User context filtering for
  Amazon RDS (Microsoft SQL Server) data sources](#context-filter-rds-ms-sql-server "#context-filter-rds-ms-sql-server")
- [User context filtering for Amazon RDS (MySQL) data sources](#context-filter-rds-mysql "#context-filter-rds-mysql")
- [User context filtering for Amazon RDS (Oracle) data sources](#context-filter-rds-oracle "#context-filter-rds-oracle")
- [User context filtering for
  Amazon RDS (PostgreSQL) data sources](#context-filter-rds-postgresql "#context-filter-rds-postgresql")
- [User context filtering for Amazon S3
  data sources](#context-filter-s3 "#context-filter-s3")
- [User context filtering for Box data
  sources](#context-filter-box "#context-filter-box")
- [User context filtering for
  Confluence data sources](#context-filter-confluence "#context-filter-confluence")
- [User context filtering for Dropbox data
  sources](#context-filter-dropbox "#context-filter-dropbox")
- [User context filtering for Drupal data
  sources](#context-filter-drupal "#context-filter-drupal")
- [User context filtering for GitHub data
  sources](#context-filter-github "#context-filter-github")
- [User context filtering for Gmail data
  sources](#context-filter-gmail "#context-filter-gmail")
- [User context filtering for Google Drive
  data sources](#context-filter-google "#context-filter-google")
- [User context filtering for IBM DB2 data
  sources](#context-filter-ibm-db2 "#context-filter-ibm-db2")
- [User context filtering for Jira data
  sources](#context-filter-jira "#context-filter-jira")
- [User context filtering for Microsoft
  Exchange data sources](#context-filter-exchange "#context-filter-exchange")
- [User context filtering for Microsoft
  OneDrive data sources](#context-filter-onedrive "#context-filter-onedrive")
- [User context filtering for Microsoft
  OneDrive v2.0 data sources](#context-filter-onedrivev2 "#context-filter-onedrivev2")
- [User context filtering for
  Microsoft SharePoint data sources](#context-filter-sharepoint-online "#context-filter-sharepoint-online")
- [User context filtering for
  Microsoft SQL Server data sources](#context-filter-ms-sql-server "#context-filter-ms-sql-server")
- [User context filtering for Microsoft
  Teams data sources](#context-filter-teams "#context-filter-teams")
- [User context filtering for Microsoft
  Yammer data sources](#context-filter-yammer "#context-filter-yammer")
- [User context filtering for MySQL data
  sources](#context-filter-mysql "#context-filter-mysql")
- [User context filtering for
  Oracle Database data sources](#context-filter-oracle-database "#context-filter-oracle-database")
- [User context filtering for
  PostgreSQL data sources](#context-filter-postgresql "#context-filter-postgresql")
- [User context filtering for Quip data
  sources](#context-filter-quip "#context-filter-quip")
- [User context filtering for
  Salesforce data sources](#context-filter-salesforce "#context-filter-salesforce")
- [User context filtering for
  ServiceNow data sources](#context-filter-servicenow "#context-filter-servicenow")
- [User context filtering for Slack data
  sources](#context-filter-slack "#context-filter-slack")
- [User context filtering for Zendesk data
  sources](#context-filter-zendesk "#context-filter-zendesk")

### User context filtering for Adobe Experience

Manager data sources

When you use an Adobe Experience Manager data source, Amazon Kendra gets
the user and group information from the Adobe Experience Manager
instance.

The group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in Adobe Experience
  Manager content where there are set access permissions. They are mapped
  from the names of the groups in Adobe Experience Manager.
- `_user_id`—User IDs exist in Adobe Experience
  Manager content where there are set access permissions. They are mapped
  from the user emails as the IDs in Adobe Experience Manager.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Alfresco

data sources

When you use an Alfresco data source, Amazon Kendra gets the user and
group information from the Alfresco instance.

The group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in Alfresco on files
  where there are set access permissions. They are mapped from the system
  names of the groups (not display names) in Alfresco.
- `_user_id`—User IDs exist in Alfresco on files where
  there are set access permissions. They are mapped from the user emails
  as the IDs in Alfresco.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Aurora (MySQL) data sources

When you use a Aurora (MySQL) data source, Amazon Kendra gets
user and group information from a column in the source table. You specify this
column in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Aurora (MySQL) database data source has the following
limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for

Aurora (PostgreSQL) data sources

When you use a Aurora (PostgreSQL) data source, Amazon Kendra
gets user and group information from a column in the source table. You specify
this column in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Aurora (PostgreSQL) database data source has the following
limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Amazon FSx data sources

When you use an Amazon FSx data source, Amazon Kendra gets user
and group information from the directory service of the Amazon FSx
instance.

The Amazon FSx group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in Amazon FSx
  on files where there are set access permissions. They are mapped from
  the system group names in the directory service of Amazon FSx.
- `_user_id`—User IDs exist in Amazon FSx on
  files where there are set access permissions. They are mapped from the
  system user names in the directory service of Amazon FSx.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for database data

sources

When you use a database data source, such as Amazon Aurora PostgreSQL,
Amazon Kendra gets user and group information from a column in the
source table. You specify this column in the [AclConfiguration](../APIReference/API_AclConfiguration.md "../APIReference/API_AclConfiguration.md") object as part of the [DatabaseConfiguration](../APIReference/API_DatabaseConfiguration.md "../APIReference/API_DatabaseConfiguration.md") object in the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A database data source has the following limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for

Amazon RDS (Microsoft SQL Server) data sources

When you use a Amazon RDS (Microsoft SQL Server) data source, Amazon Kendra gets user and group information from a column in the source
table. You specify this column in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Amazon RDS (Microsoft SQL Server) database data source has the
following limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Amazon RDS (MySQL) data sources

When you use a Amazon RDS (MySQL) data source, Amazon Kendra gets
user and group information from a column in the source table. You specify this
column in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Amazon RDS (MySQL) database data source has the following
limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Amazon RDS (Oracle) data sources

When you use a Amazon RDS (Oracle) data source, Amazon Kendra
gets user and group information from a column in the source table. You specify
this column in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Amazon RDS (Oracle) database data source has the following
limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for

Amazon RDS (PostgreSQL) data sources

When you use a Amazon RDS (PostgreSQL) data source, Amazon Kendra
gets user and group information from a column in the source table. You specify
this column in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Amazon RDS (PostgreSQL) database data source has the following
limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Amazon S3

data sources

You add user context filtering to a document in an Amazon S3 data
source using a metadata file associated with the document. You add the
information to the `AccessControlList` field in the JSON document.
For more information about adding metadata to the documents indexed from an
Amazon S3 data source, see [S3 document metadata](s3-metadata.md "s3-metadata.md").

You provide three pieces of information:

- The access that the entity should have. You can say `ALLOW`
  or `DENY`.
- The type of entity. You can say `USER` or
  `GROUP`.
- The name of the entity.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Box data

sources

When you use a Box data source, Amazon Kendra gets user and group
information from the Box instance.

The Box group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in Box on files where
  there are set access permissions. They are mapped from the names of the
  groups in Box.
- `_user_id`—User IDs exist in Box on files where
  there are set access permissions. They are mapped from the user emails
  as the user IDs in Box.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for

Confluence data sources

When you use a Confluence data source, Amazon Kendra gets user and group
information from the Confluence instance.

You configure user and group access to spaces using the space permissions
page. For pages and blogs, you use the restrictions page. For more information
about space permissions, see [Space Permissions Overview](https://confluence.atlassian.com/doc/space-permissions-overview-139521.html "https://confluence.atlassian.com/doc/space-permissions-overview-139521.html") on the Confluence Support website. For
more information about page and blog restrictions, see [Page Restrictions](https://confluence.atlassian.com/doc/page-restrictions-139414.html "https://confluence.atlassian.com/doc/page-restrictions-139414.html") on the Confluence Support website.

The Confluence group and user names are mapped as follows:

- `_group_ids`—Group names are present on spaces,
  pages, and blogs where there are restrictions. They are mapped from the
  name of the group in Confluence. Group names are always lower
  case.

- `_user_id`—User names are present on the space,
  page, or blog where there are restrictions. They are mapped depending on
  the type of Confluence instance that you are using.

**For Confluence connector v1.0**

    + Server—The `_user_id` is the user name. The
     username is always lower case.
    + Cloud—The `_user_id` is the account ID of
     the user.

**For Confluence connector v2.0**

    + Server—The `_user_id` is the user name. The
     username is always lower case.
    + Cloud—The `_user_id` is the email ID of the
     user.

###### Important

For user context filtering to work correctly for your Confluence
connector, you need to make sure that the visibility of a user
granted access to a Confluence page is set to
**Anyone**. For more information, see [Set your email visibility](https://support.atlassian.com/confluence-cloud/docs/configure-user-email-visibility/ "https://support.atlassian.com/confluence-cloud/docs/configure-user-email-visibility/") in Atlassian Developer
Documentation.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Dropbox data

sources

When you use a Dropbox data source, Amazon Kendra gets the user and group
information from the Dropbox instance.

The group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in Dropbox on files
  where there are set access permissions. They are mapped from the names
  of the groups in Dropbox.
- `_user_id`—User IDs exist in Dropbox on files where
  there are set access permissions. They are mapped from the user emails
  as the IDs in Dropbox.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Drupal data

sources

When you use a Drupal data source, Amazon Kendra gets the user and group
information from the Drupalinstance.

The group and user IDs are mapped as follows:

- `_group_ids` – Group IDs exist in Drupal on files
  where there are set access permissions. They are mapped from the names
  of the groups in Drupal.
- `_user_id` – User IDs exist in Drupal on files where
  there are set access permissions. They are mapped from the user emails
  as the IDs in Drupal.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for GitHub data

sources

When you use a GitHub data source, Amazon Kendra gets user information
from the GitHub instance.

The GitHub user IDs are mapped as follows:

- `_user_id`—User IDs exist in GitHub on files where
  there are set access permissions. They are mapped from the user emails
  as the IDs in GitHub.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Gmail data

sources

When you use a Gmail data source, Amazon Kendra gets the user information
from the Gmail instance.

The user IDs are mapped as follows:

- `_user_id` – User IDs exist in Gmail on files where
  there are set access permissions. They are mapped from the user emails
  as the IDs in Gmail.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Google Drive

data sources

A Google Workspace Drive data source returns user and group information for
Google Drive users and groups. Group and domain membership are mapped to the
`_group_ids` index field. The Google Drive user name is mapped to
the `_user_id` field.

When you provide one or more user email addresses in the `Query`
API, only documents that have been shared with those email addresses are
returned. The following `AttributeFilter` parameter only returns
documents shared with "martha@example.com".

```
"AttributeFilter": {
                "EqualsTo":{
                   "Key": "_user_id",
                   "Value": {
                       "StringValue": "martha@example.com"
                   }
               }
           }
```

If you provide one or more group email addresses in the query, only documents
shared with the groups are returned. The following `AttributeFilter`
parameter only returns documents shared with the "hr@example.com" group.

```
"AttributeFilter": {
                "EqualsTo":{
                   "Key": "_group_ids",
                   "Value": {
                       "StringListValue": ["hr@example.com"]
                   }
               }
           }
```

If you provide the domain in the query, all documents shared with the domain
are returned. The following `AttributeFilter` parameter returns
documents shared with the "example.com" domain.

```
"AttributeFilter": {
                "EqualsTo":{
                   "Key": "_group_ids",
                   "Value": {
                       "StringListValue": ["example.com"]
                   }
               }
           }
```

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for IBM DB2 data

sources

When you use a IBM DB2 data source, Amazon Kendra gets user and group
information from a column in the source table. You specify this column in the
console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A IBM DB2 database data source has the following limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Jira data

sources

When you use a Jira data source, Amazon Kendra gets user and group
information from the Jira instance.

The Jira user IDs are mapped as follows:

- `_user_id`—User IDs exist in Jira on files where
  there are set access permissions. They are mapped from the user emails
  as the user IDs in Jira.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Microsoft

Exchange data sources

When you use a Microsoft Exchange data source, Amazon Kendra gets the
user information from the Microsoft Exchange instance.

The Microsoft Exchange user IDs are mapped as follows:

- `_user_id`—User IDs exist in Microsoft Exchange
  permissions for users to access certain content. They are mapped from
  the user names as the IDs in Microsoft Exchange.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Microsoft

OneDrive data sources

Amazon Kendra retrieves user and group information from Microsoft
OneDrive when it indexes the documents on the site. The user and group
information is taken from the underlying Microsoft SharePoint site that hosts
OneDrive.

When you use a OneDrive user or group for filtering search results, calculate
the ID as follows:

1. Get the site name. For example,
   `https://host.onmicrosoft.com/sites/siteName.`
2. Take the MD5 hash of the site name. For example,
   `430a6b90503eef95c89295c8999c7981`.
3. Create the user email or group ID by concatenating the MD5 hash with a
   vertical bar (|) and the ID. For example, if a group name is
   "localGroupName", the group ID would be:

`"`430a6b90503eef95c89295c8999c7981 |
localGroupName`"`

###### Note

Include a space before and after the vertical bar. The vertical
bar is used to identify `localGroupName` with its MD5
hash.

For the user name "someone@host.onmicrosoft.com," the user ID would be
the following:

`"`430a6b90503eef95c89295c8999c7981 |
someone@host.onmicrosoft.com`"`

Send the user or group ID to Amazon Kendra as the `_user_id`
or `_group_id` attribute when you call the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API. For example, the AWS CLI command that uses a
group to filter the search results looks like this:

```
aws kendra  query \
                --index-id `index ID`
                --query-text "`query text`"
                --attribute-filter '{
                   "EqualsTo":{
                     "Key": "_group_id",
                     "Value": {"StringValue": "430a6b90503eef95c89295c8999c7981 | localGroupName"}
                  }}'
```

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Microsoft

OneDrive v2.0 data sources

A Microsoft OneDrive v2.0 data source returns section and page information
from OneDrive access control list (ACL) entities. Amazon Kendra uses the
OneDrive tenant domain to connect to the OneDrive instance and then can filter
search results based on user or group access to sections and file names.

For standard objects, the `_user_id` and `_group_id` are
used as follows:

- `_user_id`— Your Microsoft OneDrive user email ID is
  mapped to the `_user_id` field.
- `_group_id`— Your Microsoft OneDrive group email is
  mapped to the `_group_id` field.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for

Microsoft SharePoint data sources

Amazon Kendra retrieves user and group information from Microsoft
SharePoint when it indexes the site documents. To filter search results based on
user or group access, provide user and group information when you call the
`Query` API.

To filter using a user name, use the user's email address. For example,
johnstiles@example.com.

When you use a SharePoint group for filtering search results, calculate the
group ID as follows:

**For local groups**

1. Get the site name. For example,
   `https://host.onmicrosoft.com/sites/siteName.`
2. Take the SHA256 hash of the site name. For example,
   `430a6b90503eef95c89295c8999c7981`.
3. Create the group ID by concatenating the SHA256 hash with a vertical
   bar (|) and the group name. For example, if the group name is
   "localGroupName", the group ID would be:

`"`430a6b90503eef95c89295c8999c7981 |
localGroupName`"`

###### Note

Include a space before and after the vertical bar. The vertical
bar is used to identify `localGroupName` with its SHA256
hash.

Send the group ID to Amazon Kendra as the `_group_id`
attribute when you call the [Query API](../APIReference/API_Query.md "../APIReference/API_Query.md"). For
example, the AWS CLI command looks like this:

```
aws kendra  query \
                --index-id `index ID`
                --query-text "`query text`"
                --attribute-filter '{
                   "EqualsTo":{
                     "Key": "_group_id",
                     "Value": {"StringValue": "430a6b90503eef95c89295c8999c7981 | localGroupName"}
                  }}'
```

**For AD groups**

1. Use the AD group ID for configuring filtering of search
   results.

Send the group ID to Amazon Kendra as the `_group_id`
attribute when you call the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API. For
example, the AWS CLI command looks like this:

```
aws kendra  query \
                --index-id `index ID`
                --query-text "`query text`"
                --attribute-filter '{
                   "EqualsTo":{
                     "Key": "_group_id",
                     "Value": {"StringValue": "AD group"}
                  }}'
```

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for

Microsoft SQL Server data sources

When you use a Microsoft SQL Server data source, Amazon Kendra gets user
and group information from a column in the source table. You specify this column
in the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Microsoft SQL Server database data source has the following
limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Microsoft

Teams data sources

Amazon Kendra retrieves user information from Microsoft Teams when it
indexes the documents. The user information is taken from the underlying
Microsoft Teams instance.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Microsoft

Yammer data sources

Amazon Kendra retrieves user information from Microsoft Yammer when it
indexes the documents. The user and group information is taken from the
underlying Microsoft Yammer instance.

The Microsoft Yammer user IDs are mapped as follows:

- `_email_id`— The Microsoft email ID mapped to the
  `_user_id` field.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for MySQL data

sources

When you use a MySQL data source, Amazon Kendra gets user and group
information from a column in the source table. You specify this column in the
console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A MySQL database data source has the following limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for

Oracle Database data sources

When you use a Oracle Database data source, Amazon Kendra gets user and
group information from a column in the source table. You specify this column in
the console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A Oracle Database database data source has the following limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for

PostgreSQL data sources

When you use a PostgreSQL data source, Amazon Kendra gets user and group
information from a column in the source table. You specify this column in the
console or using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object as part of the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

A PostgreSQL database data source has the following limitations:

- You can only specify an allow list for a database data source. You
  can't specify a deny list.
- You can only specify groups. You can't specify individual users for
  the allow list.
- The database column should be a string containing a semicolon
  delimited list of groups.

### User context filtering for Quip data

sources

When you use a Quip data source, Amazon Kendra gets the user information
from the Quip instance.

The Quip user IDs are mapped as follows:

- `_user_id`—User IDs exist in Quip on files where
  there are set access permissions. They are mapped from the user emails
  as the IDs in Quip.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for

Salesforce data sources

A Salesforce data source returns user and group information from Salesforce
access control list (ACL) entities. You can apply user context filtering to
Salesforce standard objects and chatter feeds. User context filtering is not
available for Salesforce knowledge articles.

If you map any Salesforce field to Amazon Kendra document title and document body
fields, Amazon Kendra will use data from the document title and body fields in search
responses.

For standard objects, the `_user_id` and `_group_ids`
are used as follows:

- `_user_id`—The user name of the Salesforce
  user.
- `_group_ids`—
  - Name of the Salesforce `Profile`
  - Name of the Salesforce `Group`
  - Name of the Salesforce `UserRole`
  - Name of the Salesforce `PermissionSet`

For chatter feeds, the `_user_id` and `_group_ids` are
used as follows:

- `_user_id`—The user name of the Salesforce user.
  Only available if the item is posted in the user's feed.
- `_group_ids`—Group IDs are used as follows. Only
  available if the feed item is posted in a chatter or collaboration
  group.
  - The name of the chatter or collaboration group.
  - If the group is public, `PUBLIC:ALL`.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for

ServiceNow data sources

User context filtering for ServiceNow is supported only for the
TemplateConfiguration API and ServiceNow Connector v2.0. ServiceNowConfiguration
API and ServiceNow Connector v1.0. do not support user context filtering.

When you use a ServiceNow data source, Amazon Kendra gets the user and
group information from the ServiceNow instance.

The group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in ServiceNow on files
  where there are set access permissions. They are mapped from the role
  names of `sys_ids` in ServiceNow.
- `_user_id`—User IDs exist in ServiceNow on files
  where there are set access permissions. They are mapped from the user
  emails as the IDs in ServiceNow.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Slack data

sources

When you use a Slack data source, Amazon Kendra gets the user information
from the Slack instance.

The Slack user IDs are mapped as follows:

- `_user_id`—User IDs exist in Slack on messages and
  channels where there are set access permissions. They are mapped from
  the user emails as the IDs in Slack.

You can add up to 200 entries in the `AccessControlList`
field.

### User context filtering for Zendesk data

sources

When you use a Zendesk data source, Amazon Kendra gets the user and group
information from the Zendesk instance.

The group and user IDs are mapped as follows:

- `_group_ids`—Group IDs exist in Zendesk tickets and
  articles where there are set access permissions. They are mapped from
  the names of the groups in Zendesk.
- `_user_id`—Group IDs exist in Zendesk tickets and
  articles where there are set access permissions. They are mapped from
  the user emails as the IDs in Zendesk.

You can add up to 200 entries in the `AccessControlList`
field.
