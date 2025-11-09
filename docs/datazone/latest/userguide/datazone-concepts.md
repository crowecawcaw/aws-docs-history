# Amazon DataZone terminology and concepts

Amazon DataZone is a data management service that makes it faster and easier for you to catalog,
discover, share, and govern data stored across AWS, on premises, and third-party sources. With
Amazon DataZone, administrators and data stewards who oversee an organization's data assets can manage
and govern access to data using fine-grained controls. These controls are designed to ensure
access with the right level of privileges and context. Amazon DataZone makes it easier for engineers,
data scientists, product managers, analysts, and business users to access data throughout an
organization so that they can discover, use, and collaborate to derive data-driven
insights.

As you get started with Amazon DataZone, it is important that you understand its key concepts,
terminology, and components.

###### Topics

- [Amazon DataZone components](#main-components "#main-components")
- [What are Amazon DataZone domains?](#what-are-domains "#what-are-domains")
- [What are Amazon DataZone projects and environments?](#what-are-projects "#what-are-projects")
- [What are Amazon DataZone blueprints?](#what-are-environment-blueprints "#what-are-environment-blueprints")
- [What are Amazon DataZone inventory and publishing
  workflows?](#what-are-inventory-publish "#what-are-inventory-publish")
- [What are Amazon DataZone subscription and fulfillment
  workflows?](#what-are-subscribe-fulfill "#what-are-subscribe-fulfill")
- [The user personas of Amazon DataZone](#datazone-users "#datazone-users")
- [Amazon DataZone terminology](#datazone-terms "#datazone-terms")

## Amazon DataZone components

Amazon DataZone includes the following four main components:

- Business data catalog - you can use this component to catalog data across your
  organization with business context and thus enable everyone in your organization to ﬁnd and
  understand data quickly.
- Publish and subscribe workﬂows - you can use these automated workﬂows to secure data
  between producers and consumers in a self-service manner and to ensure that everyone in your
  organization has access to the right data for the right purpose.
- Projects and environments
  - In Amazon DataZone projects are business use case–based groupings of people, assets (data),
    and tools used to simplify access to the AWS analytics. Projects provide areas where
    project members can collaborate, exchange data, and share assets. By default, projects are
    conﬁgured so that only those who are explicitly added to the project are able to access the
    data and analytics tools within them. Projects manage the ownership of assets produced in
    accordance with project policies for data consumers to access.
  - Within Amazon DataZone projects, environments are collections of zero or more configured
    resources (for example, an Amazon S3 bucket, an AWS Glue database, or Amazon Athena workgroup) on which a
    given set of IAM principals (for example, users with a contributor permissions) can
    operate.

- Data portal (outside the AWS Management Console) - this is a browser-based web
  application where different users can go to catalog, discover, govern, share, and analyze data
  in a self-service fashion. The data portal authenticates users with IAM credentials or
  existing credentials from your identity provider through AWS IAM Identity Center.

## What are Amazon DataZone domains?

You can use Amazon DataZone domains to organize your assets, users, and their projects. By
associating additional AWS accounts with your Amazon DataZone domains, you can bring together your
data sources. You can then publish assets from these data sources to your domain's catalog, with
metadata forms and glossaries that improve metadata completeness and quality. You can also search
and browse these assets to see what data is published in the domain. Additionally, you can join
projects to collaborate with others users, subscribe to assets, and use project environments to
access analytics tools, including Amazon Athena and Amazon Redshift. Amazon DataZone domains enable
you with the flexibility to reflect the data and analytics needs of your organizational
structure, whether it's creating a single Amazon DataZone domain for your enterprise or multiple
Amazon DataZone domains for different business units.

## What are Amazon DataZone projects and environments?

Amazon DataZone enables teams and analytics users to collaborate on projects by creating use-case
based grouping of teams, tools, and data.

- In Amazon DataZone, projects enable a group of users to collaborate on various business use
  cases that involve publishing, discovering, subscribing to, and consuming data in the
  Amazon DataZone catalog. Project members consume assets from the Amazon DataZone catalog and produce new
  assets using one or more analytical workflows. Projects support the following activities within
  the data portal:
  - Project owners can add members with owner, contributor, consumer, steward, and viewer
    permissions
  - Project members can be SSO users, SSO groups, and IAM users
  - Project members can request subscription to the assets in the data catalog

  Subscription approvals are provided to the projects

|             | Create/delete projects              | Create/delete project profiles      | Create/delete environment profiles  | Create/delete environments          | Add/delete members to projects | Search and discovery | Create/delete metadata forms/glossaries | Create data source runs and ingest data | Publish data | Request subscriptions | Approve/reject subscription requests | Read subscribed data from Amazon Athena and Amazon Redshift |
| ----------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ------------------------------ | -------------------- | --------------------------------------- | --------------------------------------- | ------------ | --------------------- | ------------------------------------ | ----------------------------------------------------------- |
| Owner       | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | Yes                            | Yes                  | Yes                                     | Yes                                     | Yes          | Yes                   | Yes                                  | Yes                                                         |
| Contributor | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | Yes                                     | Yes                                     | Yes          | Yes                   | Yes                                  | Yes                                                         |
| Consumer    | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | No                                      | No                                      | No           | Yes                   | No                                   | Yes                                                         |
| Viewer      | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | No                                      | No                                      | No           | No                    | No                                   | Yes                                                         |
| Steward     | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | Yes                                     | Yes                                     | Yes          | No                    | Yes                                  | Yes                                                         |

- In a Amazon DataZone project, environments are collections of zero or more configured resources
  (for example, an Amazon S3, an AWS Glue database, or an Amazon Athena workgroup), with a given set of IAM
  principals who can operate on those resources. Environments are created by using environment
  proﬁles which are pre-configured sets of resources and blueprints that provide reusable
  templates for creating environments. Environment profiles
  define settings such as the AWS account or region in which
  environments are deployed.

## What are Amazon DataZone blueprints?

A blueprint with which the environment is created defines what AWS tools and services (for
example, AWS Glue or Amazon Redshift) members of the project to which the environment belongs can use as
they work with assets in the Amazon DataZone catalog.

In the current release of Amazon DataZone, the following default blueprints are supported:

| Blueprint name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Resources created                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Lake blueprint        | Enables Amazon DataZone project members to launch Data Lake producer and consumer services<br>within the environment.<br>As a _consumer_, it enables Amazon DataZone project members to access a<br>'read only' copy of Lake Formation-managed assets directly in Amazon Athena and in other Lake Formation-supported<br>query engines.<br>As a _producer_, it enables Amazon DataZone project members to create new<br>LakeFormation-managed tables using Amazon Athena and to publish them to the Amazon DataZone<br>catalog. | Provides users with the ability to create and query Lake Formation tables using Amazon Athena.<br>Amazon Athena workgroup, AWS Glue database with 'read only' Lake Formation permissions, 'read only' IAM<br>permissions, and access to Amazon S3 that is managed by the project. AWS Glue database with 'create'<br>and 'grant' Lake Formation permissions, 'read' and 'write' IAM permissions, AWS Glue ETL (extract,<br>transform, and load) with tagging. |
| Data Warehouse blueprint   | As a _consumer_, this blueprint enables Amazon DataZone project members<br>to connect to their own Amazon Redshift clusters to query remote data stores and to create and<br>store new data sets.<br>As a _producer_, this blueprint enables Amazon DataZone project members<br>to connect to their own Amazon Redshift clusters to query remote data stores, to create new<br>datasets, and to publish them to the Amazon DataZone catalog.                                                                                    | Access to the Amazon Redshift query editor, 'read' access to the subscribed data sources from<br>the Amazon DataZone catalog, the ability to create local assets in the configured Amazon Redshift<br>cluster. Access to the Amazon Redshift query editor, 'read' access to the subscribed data sources<br>from the Amazon DataZone catalog, the ability to create and publish assets from the configured<br>Amazon Redshift cluster.                         |
| Amazon Sagemaker blueprint | This blueprint help data producers and consumers to seamlessly switch to Amazon<br>SageMaker to collaborate on machine learning (ML) projects while enforcing access governance<br>to data and ML assets. With the new built-in integration between Amazon DataZone and Amazon<br>SageMaker, data consumers and producers can streamline ML governance across infrastructure<br>setup, collaborate on business initiatives, and easily govern data and ML assets.                                                               | You can create an Amazon SageMaker domain that can search, subscribe and publish data<br>and ML assets in Amazon DataZone. Also can subscribe and publish to AWS Glue databases and lake<br>formation as configured.                                                                                                                                                                                                                                          |

## What are Amazon DataZone inventory and publishing

workflows?

### Creating project inventory assets

In order to use Amazon DataZone to catalog your data, you must first bring your data (assets) as
inventory of your project in Amazon DataZone. Creating inventory for a project, makes the assets
discoverable only to that project’s members. Project inventory assets are not available to all
domain users in search/browse unless explicitly published. In the current release of Amazon DataZone,
you can add assets to the project inventory in the following ways:

- Create and run data sources via the data portal or by using the Amazon DataZone APIs. In the
  current release of Amazon DataZone, you can create and run data sources for AWS Glue and Amazon
  Redshift. By creating and running AWS Glue or Amazon Redshift data sources, you create
  assets in a chosen project inventory and import their technical metadata from the source
  database tables or data warehouses as inventory into Amazon DataZone.
- Using APIs, you can create assets from the available system asset types (AWS Glue,
  Amazon Redshift, Amazon S3 objects) or from your custom asset types.
  - Create custom asset types in a project inventory by using the Amazon DataZone APIs. The
    custom asset types can include ML models, dashboards, on-premises tables, etc.
  - Create assets from these custom asset types using Amazon DataZone APIs.

- Manually create assets for S3 objects using the Amazon DataZone data portal.

**Curating of your project inventory assets** - after creating
a project inventory, data owners can curate their inventory assets with the required business
metadata by adding or updating business names (asset and schema), descriptions (asset and
schema), read me, glossary terms (asset and schema), and metadata forms. You can do this via the
data portal or by using the Amazon DataZone APIs. Each edit to your asset creates a new inventory
version.

### Publishing project inventory assets to the Amazon DataZone

catalog

The next step of using Amazon DataZone to catalog your data, is to make your project’s inventory
assets discoverable by the domain users. You can do this by publishing the inventory assets to
the Amazon DataZone catalog. Only the latest version of the inventory asset can be published to the
catalog and only the latest published version is active in the discovery catalog. If an
inventory asset is updated after it's been published into the Amazon DataZone catalog, you must
explicitly publish it again in order for the latest version to be in the discovery catalog. In
the current release of Amazon DataZone, you can publish your project inventory assets to the
Amazon DataZone catalog in the following ways:

- Manually publish your project inventory assets to the Amazon DataZone catalog either via the
  data portal or by using the Amazon DataZone APIs.
- As part of creating or editing data sources, enable the optional **Publish your
  AWS Glue assets to the catalog** or **Publish your Amazon Redshift assets
  to the catalog** settings to be used during the scheduled or automated data source
  runs. When this setting is enabled, a data source run adds assets to your project's inventory
  and then also publishes the inventory assets to the Amazon DataZone catalog. Note that if you
  publish directly, the assets might not have any business metadata and will be made directly
  discoverable to all domain users. You can use this setting on your data sources either via the
  data portal or by using the Amazon DataZone APIs.

## What are Amazon DataZone subscription and fulfillment

workflows?

Once your assets are published to the Amazon DataZone catalog, your domain users can discover
these assets, request and gain access to these assets, and continue to use Amazon DataZone to govern,
share, and analyze these assets.

Users request access to an asset by subscribing to that asset on behalf of a project. Once a
subscription request is created, owners of the asset get a notification and can review the
subscription request and decide whether they want to approve or reject it. If the subscription
request is approved by the data owner, the subscribing project is granted access to that asset.

Once a subscription request is approved, Amazon DataZone begins a subscription fulfillment
workflow that automatically adds the asset to all the applicable environments within the project
by creating the necessary grants in AWS Lake Formation or Amazon Redshift. This enables the
subscribing project members to query the asset using one of the query tools (Amazon Athena or
Amazon Redshift query editor) in their environments.

Amazon DataZone can trigger this automated fulfillment logic only for managed assets (this
includes AWS Glue tables and Amazon Redshift tables and views). For all other asset types
(unmanaged assets), Amazon DataZone can't automatically trigger fulfillment but instead publishes an
event in Amazon Eventbridge with all the necessary details in the event payload so that you can
create the necessary grants outside of Amazon DataZone. Amazon DataZone also provides the
`updateSubscriptionStatus` API that enables you to update the status of the
subscription once it is fulfilled outside of Amazon DataZone so that Amazon DataZone can notify the project
members that they can start consuming the asset.

## The user personas of Amazon DataZone

The following are the primary Amazon DataZone user personas:

- Domain administrators who own setting up Amazon DataZone as the analytics platform for their
  organization.

In the context of Amazon DataZone, domain administrators install Amazon DataZone in AWS accounts,
create Amazon DataZone domains, and configure AWS account associations and identity providers
associations with Amazon DataZone domains. Domain administrators also use other AWS service
consoles such as AWS Organization and Service Catalog to configure Amazon DataZone.

- Data users who are the main users of Amazon DataZone (asset publishers and subscribers) for
  their analytics and machine learning tasks.

Data users include data analytics workers, data scientists, and system users who produce
and consume data assets. In the context of Amazon DataZone, data users create and join projects and
environments, subscribe and consume data assets with pre-configured analytics or machine
learning tools, and publish output data assets back to the Amazon DataZone domain catalog to share
with others.

- System developers who build custom infrastructure templates and integrate Amazon DataZone with
  internal catalogs or production systems.

In the context of Amazon DataZone, system developers build environment blueprints
(infrastructure templates) or Infrastructure-As-Code CI/CD pipeline as a Environment provider,
data pipelines to promote data assets across environments, catalog sync and subscription grant
fulfillment adapters to integrate with internal catalogs, or integrations between Amazon DataZone
APIs and internal user interfaces or production systems if needed.

- Data governance officers who own the definitions and risks of organizational security,
  privacy and other compliance policies and who make sure that the usage of Amazon DataZone in their
  organizations is in compliance with these definitions.

## Amazon DataZone terminology

**Domain**

An Amazon DataZone domain is the organizing entity for connecting together your assets, users,
and their projects. With Amazon DataZone domains, you have the flexibility to reflect the data and
analytics needs of your organizational structure, whether it's creating a single Amazon DataZone
domain for your enterprise or multiple datazone; domains for different business units or
teams.

**Domain unit**

Domain units enable you to easily organize your assets and other domain entities under
specific business units and teams. To set up secure and efficient data sharing within and
across business units of your organization, you can create domain units within Amazon DataZone and
enable selected users within each business unit to login and share their assets to the
catalog. Domain units can also be used to enable resource owners, such as AWS account
owners, to set up Amazon DataZone authorization permissions on their resources. Domain units
provide a delegated authority from account owners to domain unit owners and they can set up
authorization permissions on environment profiles (created using blueprint configurations), on
behalf of account owners. For more information, see [Domain units and authorization policies in
Amazon DataZone](working-with-domain-units.md "working-with-domain-units.md").

**Authorization policy**

Amazon DataZone authorization policies are a set of controls within Amazon DataZone applied to
entities such as projects, blueprints, environments, glossary, and metadata forms. These
policies define who can create these entities and manage their lifecycle in the Amazon DataZone
portal.

Within an Amazon DataZone domain unit, you can assign the following authorization policies to
your users and groups to grant them specific permissions:

- Domain unit creation policy
- Project creation policy
- Project membership policy
- Domain unit ownership assumption policy
- Project ownership assumption policy

For more information, see [Assign
authorization policies to users and groups within an Amazon DataZone domain unit](assign-authorization-policies-to-users-in-domain-unit.md "assign-authorization-policies-to-users-in-domain-unit.md").

Within an Amazon DataZone domain unit, you can assign the following authorization policies to
your projects to grant them specific permissions:

- Glossary creation policy
- Metadata forms creation policy
- Custom asset type creation policy

For more information, see [Assign
authorization policies to projects within an Amazon DataZone domain unit](assign-authorization-policies-to-projects-in-domain-unit.md "assign-authorization-policies-to-projects-in-domain-unit.md").

Within a specific blueprint configuration, you can assign the following authorization
policies to projects and domain unit owners:

- Create environment profiles using this blueprint - this policy can be assigned to
  Amazon DataZone projects and it authorizes them to create environment profiles using this
  blueprint.
- Grant permissions to create environment profiles using this blueprint - this policy can
  be assigned to domain unit owners and it authorizes them to grant permissions to projects to
  create environment profiles using this blueprint.

For more information, see [Assign authorization
policies within Amazon DataZone blueprint configurations](assign-authorization-policies-in-blueprint-config.md "assign-authorization-policies-in-blueprint-config.md").

**Associated account**

Associating your AWS accounts with Amazon DataZone domains enables you to publish data from
these AWS accounts into the Amazon DataZone catalog and create Amazon DataZone projects to work with
your data across multiple AWS accounts. Account association requests can only be initiated
in AWS accounts that own a Amazon DataZone domain. Account association requests can only be
accepted by the administrative users of the invited AWS accounts. Once an AWS account is
associated with an Amazon DataZone domain, you can register your data sources such as AWS Glue
catalog and Amazon Redshift in this account to this domain. Being associated also enables an
AWS account to create Amazon DataZone projects and environments.

An AWS account can be associated with one or more Amazon DataZone domain.

**Data source**

In Amazon DataZone, you can use data sources to import technical metadata of assets (data)
from the source databases or data warehouses into Amazon DataZone. In the current release of
Amazon DataZone, you can create and run data sources for AWS Glue and Amazon Redshift. By
creating a data source, you establish a connection between Amazon DataZone and the source
(AWS Glue Data Catalog or Amazon Redshift Warehouse) which enables you to read technical metadata, including
tables names, columns names, and data types. By creating a data source you also kick off the
initial data source run that creates new or updates existing assets in Amazon DataZone. While
creating a data source or after the data source is successfully created, you also have the
option to specify a schedule for your data source runs.

**Data source run**

In Amazon DataZone, a data source run is a task that Amazon DataZone performs in order to create
assets in project inventories and also optionally to publish project inventory assets to the
Amazon DataZone catalog. Data source runs can be automated (kicked off when a data source is
initially created) or scheduled or manual. Data selection criteria enables you to fine-tune
the existing and future data sets to be ingested into project inventories or the Amazon DataZone
catalog and the frequency of metadata updates to those inventory or catalog assets.

**Subscription target**

In Amazon DataZone, subscription targets enable you to access the data to which you have
subscribed in your projects. A subscription target specifies the location (for example, a
database or a schema) and the required permissions (for example, an IAM role) that
Amazon DataZone can use to establish a connection with the source data and to create the necessary
grants so that members of the Amazon DataZone project can start querying the data to which they
have subscribed.

**Subscription request**

In Amazon DataZone, a subscription request is a process that an Amazon DataZone project must follow
in order to be granted access to a speciﬁc asset. Subscription requests can be approved,
rejected, revoked, or granted.

**Asset**

In Amazon DataZone, an asset is an entity that presents a single physical data object (for
examples, a table, a dashboard, a file) or virtual data object (for example, a view).

**Asset type**

Asset types define how assets are represented in the Amazon DataZone catalog. An asset type
defines the schema for a specific type of asset. When assets are created, they are validated
against the schema defined by their asset type (by default, the latest version). When an asset
update occurs, Amazon DataZone creates a new asset version and enables Amazon DataZone users to operate
on all asset versions.

**Business glossary**

In Amazon DataZone, a business glossary is a collection of business terms that may be
associated with assets. A business glossary helps ensure that the same terms and definitions
are used across an organization throughout its various data analytics tasks.

The terms in a business glossary can be added to assets and columns to classify or
enhance the identification of those attributes during search. Glossary can be selected as the
value type for a field in a metadata form that is associated with an asset. When a particular
term is selected as the value for an asset's metadata form field, users can search for the
business glossary term and find the associated assets.

**Metadata form type**

A metadata form type is a template that defines the metadata that is collected and saved
when assets are created as inventory or published in a Amazon DataZone domain. Metadata form types
can be associated with a data asset. Metadata form types help domain administrators to define
metadata forms needed for that domain such as compliance information, regulation information,
or classifications. It enables domain administrators to customize additional metadata for
their assets. Amazon DataZone has system metadata form types such as
asset-common-details-form-type, column-business-metadata-form-type, glue-table-form-type,
glue-view-form-type, redshift-table-form-type, redshift-view-form-type,
s3-object-collection-form-type, subscription-terms-form-type, and suggestion-form-type.

**Metadata form**

In Amazon DataZone, metadata forms define the metadata that is collected and saved when assets
are created as inventory or published in a Amazon DataZone domain. Metadata form definitions are
created in the catalog domain by a domain administrator. A metadata form definition is
composed of one or more field definitions, with support for boolean, date, decimal, integer,
string, and business glossary field value data types.

A domain administrator applies a metadata form to assets in their domain by adding the
metadata form to their domain. Asset publishers then provide any optional and required field
values in the metadata form.

**Project**

In Amazon DataZone, projects enable a group of users to collaborate on various business use
cases that involve creating assets in project inventories and thus making them discoverable by
all project members, and then publishing, discovering, subscribing to, and consuming assets in
the Amazon DataZone catalog. Project members consume assets from the Amazon DataZone catalog and produce
new assets using one or more analytical workflows. Project members can be owners,
contributors, consumers, stewards, and viewers.

|             | Create/delete projects              | Create/delete project profiles      | Create/delete environment profiles  | Create/delete environments          | Add/delete members to projects | Search and discovery | Create/delete metadata forms/glossaries | Create data source runs and ingest data | Publish data | Request subscriptions | Approve/reject subscription requests | Read subscribed data from Amazon Athena and Amazon Redshift |
| ----------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ------------------------------ | -------------------- | --------------------------------------- | --------------------------------------- | ------------ | --------------------- | ------------------------------------ | ----------------------------------------------------------- |
| Owner       | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | Yes                            | Yes                  | Yes                                     | Yes                                     | Yes          | Yes                   | Yes                                  | Yes                                                         |
| Contributor | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | Yes                                     | Yes                                     | Yes          | Yes                   | Yes                                  | Yes                                                         |
| Consumer    | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | No                                      | No                                      | No           | Yes                   | No                                   | Yes                                                         |
| Viewer      | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | No                                      | No                                      | No           | No                    | No                                   | Yes                                                         |
| Steward     | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | To be managed by domain unit member | No                             | Yes                  | Yes                                     | Yes                                     | Yes          | No                    | Yes                                  | Yes                                                         |

Project owners can add or remove other users
as owners or contributors and they can modify or delete projects. Other restrictions on
contributors can be defined with policies. When a user creates a project, they become the
first owner of that project.

**Environment**

An environment is a collection of configured resources (for example, an Amazon S3 bucket, an
AWS Glue database, or an Amazon Athena workgroup), with a given set of IAM principals (with
assigned contributor permissions) who can operate on those resources. Each environment may
also have user principals who are authorized to access the resources and get access to data
via subscription and fulfillment. Environments are designed to store actionable links into
AWS services and external IDEs and consoles. Members of the project can access services such
as the Amazon Athena console and more via deep links configured within an environment. SSO
users and IAM users from the project can be further scoped down to use/access specific
environments.

**Environment profile**

In Amazon DataZone, an environment proﬁle is a template that you can use to create
environments. Environment profiles are created by using blueprints.

With environment profiles, domain administrators can wrap blueprints with preconfigured
parameters, and then data workers can quickly create any number of new environments by
selecting existing environment profiles and specifying names for the new environments. This
enables data workers to efficiently manage their projects and environments while ensuring that
they satisfy data governance policies enforced by their domain administrators.

**Blueprint**

A blueprint with which the environment is created defines what AWS tools and services
(for example, AWS Glue or Amazon Redshift) members of the project to which the environment belongs can
use as they work with assets in the Amazon DataZone catalog.

In the current release of Amazon DataZone the following default blueprints are
supported:

- Data lake blueprint
- Data warehouse blueprint
- Amazon Sagemaker blueprint

**User profile**

A user profile represents Amazon DataZone users. Amazon DataZone supports both IAM roles and SSO
identities to interact with the Amazon DataZone Management Console and the data portal for
different purposes. Domain administrators use IAM roles to perform the initial
administrative domain-related work in the Amazon DataZone Management Console, including creating
new Amazon DataZone domains, configuring metadata form types, and implementing policies. Data
workers use their SSO corporate identities via Identity Center to log into the Amazon DataZone Data
Portal and access projects where they have memberships.

**Group profile**

Group profiles represent groups of Amazon DataZone users. Groups can be manually created, or
mapped to Active Directory groups of enterprise customers. In Amazon DataZone, groups serve two
purposes. First, a group can map to a team of users in the organizational chart, and thus
reduce the administrative work of a Amazon DataZone project owner when there are new employees
joining or leaving a team. Second, corporate administrators use Active Directory groups to
manage and update user statuses and so Amazon DataZone domain administrators can use these group
memberships to implement Amazon DataZone domain policies.

**Domain administrator**

In Amazon DataZone, an IAM principal who creates an Amazon DataZone domain is the default domain
administrator of that domain. Domain administrators in Amazon DataZone perform key functionalities
for the domain, including creating domains, assigning other domain administrators, adding data
sources and subscription targets, creating projects and environments, and assigning project
owners.

**Publisher**

In Amazon DataZone, publishers publish assets into the Amazon DataZone catalog and can edit the
metadata of the assets they publish. If granted this authority, publishers can approve or
reject subscription requests to the assets they published in the Amazon DataZone catalog.

**Subscriber**

In Amazon DataZone, a subscriber is an Amazon DataZone project that wants to ﬁnd, access, and
consume assets in the Amazon DataZone catalog.

**AWS account owner**

In Amazon DataZone, AWS account owners create roles, policies, and permissions in their
AWS accounts that enable these AWS accounts to be associated with Amazon DataZone domains.
