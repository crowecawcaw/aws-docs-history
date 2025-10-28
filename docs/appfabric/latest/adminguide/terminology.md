# Terminology and concepts in AppFabric

This topic describes the key terminology and concepts in AWS AppFabric to help you get
started.

###### App bundle

An AppFabric _app bundle_ stores all of your AppFabric app
authorizations and ingestions (see the following definition of ingestions). You can
create one app bundle per AWS account per AWS Region.

###### AppClient (also app client and application client)

An OAuth AppClient for the data recipient app. Each data recipient app needs to
register an AppClient to access AppFabric data. A developer user needs an AWS account to
register AppClient. Each AWS account can only register one AppClient. AppFabric will vend
access tokens based on AppClient. AppClient will contain information around the data
recipient app that will be accessing AppFabric data through this AppClient.

###### App authorization

An _app authorization_ grants AppFabric permission to
connect and interact with your applications. It allows ingestion of audit logs from your
applications, with OAuth (Open Authorization - an open standard for access delegation to
grant applications access) or personal access token (PAT) credentials. You can set up
multiple app authorizations (up to 50) per app bundle. This allows AppFabric to ingest audit
logs from multiple tenants of applications, by repeating the app authorization creation
step as needed for each tenant of the application. The credentials that are shared are
encrypted with an AWS owned key or a customer managed key from the AWS Key Management Service (AWS KMS), and are
stored in AppFabric.

###### Ingestion

An AppFabric _ingestion_ uses an app authorization to
pull audit logs from an application through the application’s public APIs. It then
delivers the audit logs to one or more (up to five) destinations.

###### Client ID

When you create an app authorization to connect with an application that uses the
OAuth flow, AppFabric might ask you for the client ID and client secret. The client ID and
client secret can be found in your application’s authentication app. For instructions on
where to find the client ID in a given authentication app, see [Supported applications](supported-applications.md "supported-applications.md"). The client ID and
client secret that are shared are encrypted with an AWS owned key or a customer managed key
AWS KMS key and stored in AppFabric.

###### Client secret

When you create an app authorization to connect with an application that uses the
OAuth flow, AppFabric might ask you for the client ID and client secret. The client ID and
client secret can be found in your application’s authentication app. For instructions on
where to find the client secret in a given authentication app, see [Supported applications](supported-applications.md "supported-applications.md"). The client ID and
client secret that are shared are encrypted with an AWS owned key or a customer managed key
AWS KMS key and stored in AppFabric.

###### Ingestion destination

An _ingestion destination_ defines where the audit
logs pulled from an ingestion should be stored. Each ingestion can deliver audit logs to
one or more destinations (up to five), which are an Amazon Simple Storage Service (Amazon S3) bucket or an
Amazon Data Firehose in your AWS account. For each destination, you can define whether you would
like the logs to be in raw form or normalized into an Open Cybersecurity Schema
Framework (OCSF) schema. When you select the OCSF schema, you can define the format of
the logs (JSON or Apache
Parquet). The Apache
Parquet format can be used only if Amazon S3 is selected as the
destination.

###### Data recipient apps

Apps that will call AppFabric to get generated insights from AppFabric.

###### OAuth

OAuth is an open protocol to allow secure authorization in a simple and standard
method from web, mobile, and desktop applications. AppFabric uses OAuth to create some app
authorizations.

###### Open Cybersecurity Schema Framework (OCSF)

The Open Cybersecurity Schema Framework (OCSF) is an open-source project delivering an
extensible framework for developing schemas, along with a vendor-agnostic core security
schema. Vendors and other data producers can adopt and extend the schema for their
specific domains. The goal is to provide an open standard, adopted in any environment,
application, or solution, while complementing existing security standards and processes.
AppFabric has extended this schema to create a software as a service (SaaS)-centric event
structure that all SaaS app audit logs supported by AppFabric will be normalized to. For
more information, see [Open Cybersecurity Schema Framework for AWS AppFabric](ocsf-schema.md "ocsf-schema.md").

###### Personal access token (PAT)

A _personal access token_ (PAT) is a string of
characters that can be used to access a computer system instead of the usual password.
When you create an app authorization to connect with an application that uses the PAT
flow, AppFabric might ask you for a PAT. The PAT can be found in your application’s
authentication app. For instructions on where to find the PAT in a specific
authentication app, see [Supported
applications](supported-applications.md "supported-applications.md"). The service account tokens that are shared are encrypted with
an AWS owned key or a customer managed key AWS KMS key and stored in AppFabric.

###### Service account token

When you create an AppFabric app authorization to connect with an application, some
applications will require a service account to be created for application
authentication. AppFabric might ask for the _service account
token_ as part of the app authorization process. For instructions on where
to find the service account token in a given authentication app, see [Supported applications](supported-applications.md "supported-applications.md"). The service account
tokens that are shared are encrypted with an AWS owned key or a customer managed key AWS KMS key
and stored in AppFabric.

###### Tenant ID

When you create an app authorization, AppFabric might ask you for the tenant ID and tenant
name of your app. The _tenant ID_ is a unique
identifier for your application tenant. Each application might have different terms for
a tenant such as _Workspace ID_ for
Slack or _Domain ID_ for
Asana. For instructions on where to find the tenant ID in a specific
application, see [Supported
applications](supported-applications.md "supported-applications.md").

###### Tenant name

When you create an app authorization, AppFabric might ask you for the tenant ID and tenant
name of your app. The _tenant name_ is a unique name
that you give to the tenant ID, to be used within an app bundle. This value is used to
label the app authorization and any related ingestion.
