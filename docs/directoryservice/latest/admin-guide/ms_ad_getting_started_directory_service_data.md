# AWS Directory Service Data

AWS Directory Service Data is an extension of AWS Directory Service. You can create, read, update, and Active Directory (AD) users,
groups, and memberships from an AWS Directory Service for Microsoft Active Directory without deploying dedicated AD management
instances on an Amazon EC2 instance. You can also perform built-in object management tasks across
directories without any direct network connectivity. This simplifies provisioning and access
management to achieve fully automated deployments. For more information, see the [AWS Directory Service Data API Reference](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md") .

Directory Service Data supports user and group write operations, like `CreateUser` and
`CreateGroup`, within the AWS Managed Microsoft AD that's in your organizational unit (OU).
Directory Service Data supports read operations, like `ListUsers` and `ListGroups`, on all
users, groups, and group memberships within the AWS Managed Microsoft AD and across trusted realms. Directory Service Data
supports adding and removing group members from groups in your OU and the AWS Delegated Groups
OU, so you can delegate permissions by adding users to specific delegated group objects. For
more information, see [User and group management in AWS Managed Microsoft AD](ms_ad_manage_users_groups.md "ms_ad_manage_users_groups.md").

###### Note

Directory Service Data is only available in your Primary Region. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").

###### Topics

- [Replication and consistency](#replication_consistency "#replication_consistency")
- [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
- [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md")

## Replication and consistency

The Directory Service Data API connects to your AWS Managed Microsoft AD domain controllers to perform operations on
the underlying directory objects. Active Directory is an eventually consistent platform, and replication
is continuously occurring between Directory Service directory domain controllers. By default, every Directory Service
directory is created with two domain controllers.

Directory Service Data attempts to maintain a consistent experience by utilizing the same domain
controller across requests. In the event that a domain controller is unavailable, Directory Service Data
switches to an alternative domain controller. During these events, you might notice eventual
consistency across domain controllers while objects are replicated across domain controllers.

Directory limits vary by AWS Managed Microsoft AD edition:

- **Standard edition** – Supports 8 transactions per
  second for read operations and 4 TPS for write operations per directory.
- **Enterprise edition** – Supports 16 transactions per
  second for read operations and 8 TPS for write operations per directory.

###### Note

There's a concurrency limit of 10 concurrent requests for both Standard and Enterprise editions.

- **AWS account** – Supports a total of 100 transactions per
  second for Directory Service Data operations across all directories.
