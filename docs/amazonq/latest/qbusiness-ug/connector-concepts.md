# Data source connector concepts

This topic outlines specific concepts and features of Amazon Q Business data
source connectors. These concepts are key to understanding how to configure your
connector setup. These terms recur on the AWS Management Console, AWS Command Line Interface (AWS CLI), and the
Amazon Q API.

###### Topics

- [Source and endpoint metadata](#connector-source "#connector-source")
- [Authorization](#connector-authorization "#connector-authorization")
- [Authentication](#connector-authentication "#connector-authentication")
- [Virtual private cloud](#connector-vpc "#connector-vpc")
- [Web proxy](#connector-web-proxy "#connector-web-proxy")
- [IAM role](#connector-iam "#connector-iam")
- [Identity crawler](#connector-identity-crawler "#connector-identity-crawler")
- [Sync scope](#connector-sync-scope "#connector-sync-scope")
- [Sync mode](#connector-sync-mode "#connector-sync-mode")
- [Sync run schedule](#connector-sync-run "#connector-sync-run")
- [Field mappings](#connector-field-mappings "#connector-field-mappings")

## Source and endpoint metadata

You enter your data source configuration information in the
**Source** section on the console. If you use the API, you
specify this information using the `configuration` parameter of the
`CreateDataSource` operation. Connection configuration
information varies depending on the data source. To make sure your connector
configures correctly, check the following details:

- You're following [connector configuration best
  practices](connector-best-practices.md "connector-best-practices.md").
- You've completed the prerequisites for data source configuration.
  Prerequisites information specific to your data source connector is on
  each connector's specific page.

## Authorization

Amazon Q Business connectors index access control list (ACL) information
that's attached to a document along with the document itself. For document
access control lists, Amazon Q Business indexes the following:

- user email address
- group name for the local group
- group name for the federated group (for example, if you have a
  Microsoft SharePoint data source integrated with Microsoft Entra
  ID (formerly Azure AD)

Then, Amazon Q Business stores the ACL information it indexes in the
[Amazon Q Business User Store](connector-principal-store.md "connector-principal-store.md") to create
user and group mappings and filter chat responses based on the end user's access
to documents.

An Amazon Q Business connector updates any changes in ACLs each time
that your data source content is crawled. To capture ACL changes to make sure
that the right end users have access to the right content, re-sync your data
source regularly.

Connectors support crawling ACL and identity information for all data sources
where the feature is supported. To index documents without ACLs (as public
documents) ensure these documents are already marked public in the enterprise
data source the connectors index the content from.

###### Note

Amazon Q Business supports crawling ACLs for document security by
default. As a general rule, turning off ACLs and identity crawling once they
have been enabled are no longer supported. In preparation for [connecting Amazon Q Business applications to
IAM Identity Center](migrate-application.md "migrate-application.md"), enable ACL indexing and identity crawling for secure
querying and re-sync your connector. Once you turn ACL and identity crawling
on you won't be able to turn them off. Certain connectors provide you with
the ability to manage ACLs by enabling or disabling them during data source
creation. To create a data source with ACLs disabled, you need specific
IAM permissions. For more information, see [Setting up](setting-up.md "setting-up.md").

If you delete a group in the User Store and then re-create it later with the
same name but with different group members, document ACLs which contain this
group may be impacted. We recommend that this type of change (deleting or
re-creating a group with the same name but with different group members) be done
in the data source instead of the Amazon Q Business User Store.

If you re-use an email address between users (for example a user leaves the
company and at a later time a new user joins the company and has the same email
address), you must delete the original user from the User Store. Amazon Q Business will verify if all the attributes of the new user from the
IAM Identity Center matches those of the user in the User Store. If an older user with the
same email address but with different attributes is found, the API calls for
that user (for example, the query request) will be denied.

###### Important

Inadvertent mistakes when you update the User Store’s user, group, group
membership, and mapping information can result in unintentional and
unacceptable changes in the accessibility of documents to users.

Treat the ability to update the User Store to create users, update users,
delete users, create groups, update groups, delete groups (i.e, create
update delete operations), and update the mappings, as a privileged
operation.

Ensure that access to the User Store APIs is provided only to admin who
fully understand how to use these APIs and the implications of these changes
on your document security. We recommend establishing a documented approval
process be followed for making such changes.

## Authentication

To authenticate Amazon Q Business to access your data source, you
provide your data source access credentials to Amazon Q Business using an
AWS Secrets Manager secret. If you use the console, you can choose to create a new secret
or use an existing one. If you use the API, you must provide the Amazon Resource
Name (ARN) of an existing Secrets Manager secret when you use the
`CreateDataSource` operation.

###### Note

You should regularly refresh or rotate your credentials and secret
details. Provide only the necessary access level for your own security.
Don't re-use credentials and secrets across data sources.

For on-premises or server data source connectors, Amazon Q Business
checks if the endpoint information included in Secrets Manager is the same
endpoint information specified in your data source configuration details. This
helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a security
issue. The problem occurs when a user doesn’t have permissions to perform an
action. But, by using Amazon Q Business as a proxy, the user can access
the configured secret and perform the action.

If you change your endpoint information later, you must create a new secret to
sync this information.

###### Note

If you change your authentication type and credentials, you must update
your IAM role to access the correct Secrets Manager secret
ID.

## Virtual private cloud

Amazon Q Business can connect to Amazon Virtual Private Cloud to index content stored in
data sources or databases running in your private cloud. If your data source or
database isn't running on Amazon VPC, you can connect your data source
or database to Amazon VPC using a virtual private network (VPN).

You can use Amazon VPC with either the console or the Amazon Q Business API. If you're using the API, you specify the
`vpcConfiguration` when you use the `CreateDataSource`
API operation.

If you're using Amazon VPC with Amazon Q Business, you need the
following information:

- The identifier of the subnet that contains the data source.
- The identifier of the security groups that grant access to the
  host.
- An IAM role with access to Amazon VPC and
  permissions to create and delete an elastic network interface in your
  subnets is also required.

You can find the subnet and security group IDs in the Amazon VPC
console. For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide_.

For more information about using Amazon VPC with Amazon Q Business, see [Using Amazon VPC with connectors.](connector-vpc.md "connector-vpc.md").

## Web proxy

For all supported data sources, you can use a web proxy to connect to your
data source instance. You must provide the host name and port number. For
example, `a.example.com` is the hostname of
`https://a.example.com/page1.html`, and the port is 443, which is
the standard port for HTTPS.

###### Important

For security reasons, Amazon Q Business only supports web proxy
using HTTPS protocol.

## IAM role

To create your data source connector, Amazon Q Business requires
permissions to interact with other services.

If you're using the console, you can choose an existing IAM
role or let Amazon Q Business create a role for you. If you're unsure if
an existing role is used for an application, choose **Create a new
role** to avoid an error.

###### Note

To **Create a new role** during connector configuration
on the console, you must have permissions to create an IAM
role.

If you're using the API, you must provide the ARN of an existing IAM role when you use the `CreateDataSource`
operation.

IAM roles used for applications can't be used for data
sources.

###### Note

Make sure your IAM role includes the permissions to support
your Amazon Q Business connector configurations.

## Identity crawler

Amazon Q Business crawls ACL information at the document level from
supported data sources. In addition, Amazon Q Business crawls and stores
principal information within each data source (local user alias, local group,
and federated group identity configurations) into the Amazon Q Business
[User Store](connector-principal-store.md "connector-principal-store.md"). This is useful when your
application environment is connected to multiple data sources with different authorization
and authentication systems, but you want to create a unified, access-controlled
chat experience for your end users.

Amazon Q Business indexes the following information from document access
control lists:

- user email address
- group name for the local group
- group name for the federated group (for example, if you have a
  Microsoft SharePoint data source integrated with Microsoft Entra
  ID (formerly Azure AD)

Amazon Q Business internally maps the local user and group IDs attached
to the document to the federated identities of users and groups. Mapping
identities streamlines user management and speeds up chat responses by reducing
ACL information retrieval time during chat requests. Identity crawling, along
with the [Authorization](connector-key-concepts.md#connector-authorization "connector-key-concepts.md#connector-authorization") feature, helps to filter and generate web experience
content restricted by end user context. For more information about this process,
[Amazon Q Business User Store](connector-principal-store.md "connector-principal-store.md").

Connectors support crawl ACL and identity information where applicable based
on the data source. To index documents without ACLs (as public documents) ensure
the documents you want to index from your data source are public documents in
the enterprise data source the connectors index the content from.

If you delete a group in the User Store and then re-create it later with the
same name but with different group members, document ACLs which contain this
group may be impacted. We recommend that this type of change (deleting or
re-creating a group with the same name but with different group members) be done
in the data source instead of the Amazon Q Business User Store.

If you re-use an email address between users (for example a user leaves the
company and at a later time a new user joins the company and has the same email
address), you must delete the original user from the User Store. Amazon Q Business will verify if all the attributes of the new user from the
IAM Identity Center matches those of the user in the User Store. If an older user with the
same email address but with different attributes is found, the API calls for
that user (for example, the query request) will be denied.

###### Important

Inadvertent mistakes when you update the User Store’s user, group, group
membership, and mapping information can result in unintentional and
unacceptable changes in the accessibility of documents to users.

Treat the ability to update the User Store to create users, update users,
delete users, create groups, update groups, delete groups (i.e, create
update delete operations), and update the mappings, as a privileged
operation.

Ensure that access to the User Store APIs is provided only to admin who
fully understand how to use these APIs and the implications of these changes
on your document security. We recommend establishing a documented approval
process for making such changes.

## Sync scope

You can choose to customize the content crawled and indexed by your data
source connector. The sync scope options available vary based on the data source
connector.

### Document deletion safeguard

You can protect your documents from accidental deletion during sync by
setting a **Document deletion safeguard**, a maximum
document deletion percentage. Setting a maximum document deletion percentage
prevents your indexed files from accidental excessive deletion and
accidental data loss due to issues such as crawler failures and temporary
data source unavailability.

The **Document deletion safeguard** is calculated in the
beginning of the crawl process during a sync job. The formula is
100\*(document to be deleted)/(document scanned + to be deleted). If the
number of documents to be deleted exceeds the configured threshold
percentage, the delete phase will be skipped during a sync job, and no
documents will be deleted from the index. The data source sync job will
still sync and index the new and modified content.

You set a **Document deletion safeguard** during data
source configuration in **Sync scope**. A value of 0% means
that no documents from this data source will be deleted from your index. A
value of 100% allows unlimited deletion during the sync process, meaning no
deletion protection.

You can view the number of documents protected from deletion during a sync
job in the **Protected from deletion** column in
**Sync run history**. The number in the column is a
hyperlink to CloudWatch where you can view additional information and run
queries.

## Sync mode

With sync mode, you can customize what content gets synced with your index
when your data source content changes. Choose from the following options:

**Console**

- **Full sync** – Sync all content
  regardless of the previous sync status.
- **New or modified content sync** –
  Sync only new or modified documents.
- **New, modified, or deleted content
  sync** – Sync only new, modified, and deleted
  documents.
- **Change log** – Crawl and sync
  only new, modified, and deleted content.

**API**

Specify the sync mode using the `configuration` parameter of the
[CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation.
Choose from the following options:

- **Forced full crawl** – Crawl and
  sync all content to your index.
- **Full crawl** – Crawl all content
  and sync only new, modified, or deleted content.
- **Change log** – Crawl and sync
  only new, modified, and deleted content.

###### Note

Available sync mode features vary across data source connectors.

###### Important

If you get a **`Resource not found exception`** when you
try to view your CloudWatch logs for a data source sync job in
progress, it's because the CloudWatch logs aren't available yet. Wait
for some time and check again.

## Sync run schedule

When you use the console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation, you can choose
to periodically sync your data source with your retriever on a custom schedule.
You can choose from the following frequency options:

- **Run on demand** – Sync a data
  source with your index only when you choose to.
- **Hourly** – Sync your data source
  with your index every hour. You can choose which minute the sync
  begins.
- **Daily** – Sync your data source
  with your index daily. You can choose the sync start time in UTC format
  in hours and minutes.
- **Weekly** – Sync your data source
  with your index weekly. You can choose the days to sync and the sync
  start time in hours and minutes (UTC format).
- **Monthly** – Sync your data
  source monthly with your index. You can choose the day of the month to
  start the sync and the sync start time in hours and minutes (UTC
  format).
- **Custom** – Sync your data source
  to your index using a cron expression. A cron expression is a string
  comprising five or six required fields, separated by white space. Cron
  expressions represent a set of times programmed to schedule events. For
  example, an expression to activate a rule every day at 12:00pm UTC can
  look like: `(0 12 * * ? *)`. Similarly, an expression to
  activate a rule every day at 10:15am UTC on the last Friday of each
  month during the years 2023 to 2025 can look like: `(15 10 ? * 6L
2023-2025)`.

###### Note

Amazon Q Business will not sync the data source (even for the first
time) until you select **Sync now** after you successfully
add the data source.

## Field mappings

When you connect Amazon Q Business to your data, your data source
connector crawls relevant metadata or attributes associated with a document.
Examples of metadata include date of creation, document id, and document name.
Then, Amazon Q maps the metadata to fields within your Amazon Q Business index.

You map data source document attributes to Amazon Q Business index
fields using the **Field mappings** feature on the console, or
the `configuration` parameter of the `CreateDataSource`
API operation. If a document attribute in your data source doesn't have a
attribute mapping already available, or if you want to map additional document
attributes to index fields, use the custom field mappings to specify how a data
source attribute maps to an Amazon Q index field. You create field
mappings by editing your data source after your application environment and retriever are
created.

Document attributes need to be enabled for search before they can be used to
customize end user chat experience. To learn more about document attributes and
how they work in Amazon Q, see [Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md"). To learn how
to enable document attributes for search, see [Configuring metadata controls in Amazon Q](mapping-doc-attributes.md "mapping-doc-attributes.md").

All fields and attributes have a size limit of 2048 characters. Fields or
attributes longer than this value are truncated before document
ingestion.

For more information, see the following topics:

- [Document attributes and types](doc-attributes.md "doc-attributes.md")
- [Filtering using metadata](metadata-filtering.md "metadata-filtering.md")
