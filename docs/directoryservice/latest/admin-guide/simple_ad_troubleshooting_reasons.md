# Troubleshooting Simple AD directory

status messages

When a Simple AD is impaired or inoperable, the directory status message contains
additional information. The status message is displayed in the Directory Service console, or returned in
the [`DirectoryDescription.StageReason`](../devguide/API_DirectoryDescription.md#ADS-Type-DirectoryDescription-StageReason "../devguide/API_DirectoryDescription.md#ADS-Type-DirectoryDescription-StageReason") member by the [`DescribeDirectories`](../devguide/API_DescribeDirectories.md "../devguide/API_DescribeDirectories.md")
API. For more information about the directory status, see [Understanding your AWS Managed Microsoft AD directory status](ms_ad_directory_status.md "ms_ad_directory_status.md").

The following are the status messages for a Simple AD directory:

###### Topics

- [The directory service's elastic network interface is not
  attached](#sr_eni_detached "#sr_eni_detached")
- [Issue(s) detected by instance](#sr_internal_error "#sr_internal_error")
- [The critical Directory Service reserved user is missing
  from the directory](#sr_service_account_missing "#sr_service_account_missing")
- [The critical Directory Service reserved user needs to
  belong to the Domain Admins group](#sr_service_account_not_admin "#sr_service_account_not_admin")
- [The critical Directory Service reserved user is
  disabled](#sr_service_account_disabled "#sr_service_account_disabled")
- [The main domain controller does not have all FSMO
  roles](#sr_dc_fsmo_role "#sr_dc_fsmo_role")
- [Domain controller replication failures](#sr_dc_repl_failures "#sr_dc_repl_failures")

## The directory service's elastic network interface is not

attached

**Description**

The critical elastic network interface (ENI) that was created on your
behalf during directory creation to establish network connectivity with your
VPC is not attached to the directory instance. AWS applications backed by
this directory will not be functional. Your directory cannot connect to your
on-premises network.

**Troubleshooting**

If the ENI is detached but still exists, contact Support. If the ENI
is deleted, there is no way to resolve the issue and your directory is
permanently unusable. You must delete the directory and create a new one.

## Issue(s) detected by instance

**Description**

An internal error was detected by the instance. This usually signifies
that the monitoring service is actively attempting to recover the impaired
instances.

**Troubleshooting**

In most cases, this is a transient issue, and the directory eventually
returns to the Active state. If the problem persists, contact Support for more assistance.

## The critical Directory Service reserved user is missing

from the directory

**Description**

When a Simple AD is created, Directory Service creates a service account in the
directory with the name `AWSAdmin`D-xxxxxxxxx``. This error
is received when this service account cannot be found. Without this account,
Directory Service cannot perform administrative functions on the directory, rendering
the directory unusable.

**Troubleshooting**

To correct this issue, restore the directory to a previous snapshot that
was created before the service account was deleted. Automatic snapshots are
taken of your Simple AD directory one time a day. If it has been more than
five days after this account was deleted, you may not be able to restore the
directory to a state where this account exists. If you are not able to
restore the directory from a snapshot where this account exists, your
directory may become permanently unusable. If this is the case, you must
delete your directory and create a new one.

## The critical Directory Service reserved user needs to

belong to the Domain Admins group

**Description**

When a Simple AD is created, Directory Service creates a service account in the
directory with the name `AWSAdmin`D-xxxxxxxxx``. This error
 is received when this service account is not a member of the `Domain Admins` group. Membership in this group
is needed to give Directory Service the privileges it needs to perform maintenance and
recovery operations, such as transferring FSMO roles, domain joining new
directory controllers, and restoring from snapshots.

**Troubleshooting**

Use the Active Directory Users and Computers tool to re-add the service
account to the `Domain Admins` group.

## The critical Directory Service reserved user is

disabled

**Description**

When a Simple AD is created, Directory Service creates a service account in the
directory with the name `AWSAdmin`D-xxxxxxxxx``. This error
is received when this service account is disabled. This account must be
enabled so that Directory Service can perform maintenance and recovery operations on the
directory.

**Troubleshooting**

Use the Active Directory Users and Computers tool to re-enable the service
account.

## The main domain controller does not have all FSMO

roles

**Description**

All the FSMO roles are not owned by the Simple AD directory controller.
Directory Service cannot guarantee certain behavior and functionality if the FSMO roles
do not belong to the correct Simple AD directory controller.

**Troubleshooting**

Use Active Directory tools to move the FSMO roles back to the original
working directory controller. For more information about moving the FSMO
roles, go to [https://docs.microsoft.com/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds](https://docs.microsoft.com/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds "https://docs.microsoft.com/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds").
If this does not correct the problem, please contact Support for more
assistance.

## Domain controller replication failures

**Description**

The Simple AD directory controllers are failing to replicate with one
another. This can be caused by one or more of the following issues:

- The security groups for the directory controllers does not have
  the correct ports open.
- The network ACLs are too restrictive.
- The VPC route table is not routing network traffic between the
  directory controllers correctly.
- Another instance has been promoted to a domain controller in the
  directory.

**Troubleshooting**

For more information about your VPC network requirements, see either
AWS Managed Microsoft AD [Prerequisites for creating a
AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_prereqs "ms_ad_getting_started.md#ms_ad_getting_started_prereqs"), AD Connector [AD Connector prerequisites](ad_connector_getting_started.md#prereq_connector "ad_connector_getting_started.md#prereq_connector"), or Simple
AD [Simple AD prerequisites](simple_ad_getting_started.md#prereq_simple "simple_ad_getting_started.md#prereq_simple"). If there
is an unknown domain controller in your directory, you must demote it. If
your VPC network setup is correct, but the error persists, please contact
Support for more assistance.
