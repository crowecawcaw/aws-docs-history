# Creating a new Amazon FSx file system

fails

There are a number of potential causes when a file system creation request fails,
as described in the following section.

###### Topics

- [Misconfigured VPC security group and network ACLs](#network-acls-sg-config "#network-acls-sg-config")
- [Duplicate file system administrators group names](#w62aac37c11c15 "#w62aac37c11c15")
- [DNS servers or domain controllers unreachable](#w62aac37c11c17 "#w62aac37c11c17")
- [Invalid service account credentials](#w62aac37c11c19 "#w62aac37c11c19")
- [Amazon FSx can't access your Active Directory service account credentials in AWS Secrets Manager](#fsx-cant-access-ad-account-creds "#fsx-cant-access-ad-account-creds")
- [Insufficient service account permissions](#w62aac37c11c23 "#w62aac37c11c23")
- [Service account capacity exceeded](#w62aac37c11c25 "#w62aac37c11c25")
- [Amazon FSx can't access the organizational unit (OU)](#w62aac37c11c27 "#w62aac37c11c27")
- [Service account can't access the administrators group](#w62aac37c11c29 "#w62aac37c11c29")
- [Amazon FSx lost connectivity in domain](#w62aac37c11c31 "#w62aac37c11c31")
- [Service account does not have correct permissions](#w62aac37c11c33 "#w62aac37c11c33")
- [Unicode characters used in creation parameters](#w62aac37c11c35 "#w62aac37c11c35")
- [Switching storage type to HDD while restoring a backup fails](#create-fs-from-backup-fails "#create-fs-from-backup-fails")

## Misconfigured VPC security group and network ACLs

Make sure that the VPC security groups and network ACLs are configured using the recommended security group
configuration. For more information, see [Creating security groups](limit-access-security-groups.md#vpc-sg-step6 "limit-access-security-groups.md#vpc-sg-step6").

## Duplicate file system administrators group names

Creating a file system joined to your self-managed Active Directory fails with the following error message:

```
File system creation failed. Amazon FSx is unable to apply your Microsoft Active Directory configuration with the
specified file system administrators group. Please ensure that your Active Directory does not contain multiple domain
groups with the name: domain_group.
```

Amazon FSx did not create the file system because there are multiple administrator groups in the domain with the same name.

If you don't specify a group name, Amazon FSx will attempt to use the default value "Domain Admins" as the administrator group. The
request will fail if there is more than one group using the default "Domain Admins" name.

Use the following steps to resolve the issue.

1. Review the [prerequisites](self-managed-AD.md#self-manage-prereqs "self-managed-AD.md#self-manage-prereqs") for joining your file system to your self-managed Active Directory.
2. Use the [Amazon FSx Active Directory Validation Tool](validate-ad-config.md "validate-ad-config.md")
   to validate your self-managed Active Directory configuration prior to creating an FSx for Windows File Server file system that's joined
   to a self-managed Active Directory.
3. Create a new file system using the AWS Management Console or AWS CLI. For more information, see
   [Joining an Amazon FSx file system to a self-managed
   Microsoft Active Directory domain](creating-joined-ad-file-systems.md "creating-joined-ad-file-systems.md").
4. Provide a name for the file system administrator group that is unique in the domain for your self-managed Active Directory.

## DNS servers or domain controllers unreachable

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
Amazon FSx can't reach the DNS servers provided or the domain controllers for your self-managed directory in Microsoft Active Directory.
File system creation failed. Amazon FSx is unable to communicate with your Microsoft Active Directory domain controllers.
This is because Amazon FSx can't reach the DNS servers provided or domain controllers for your domain.
To fix this problem, delete your file system and create a new one with valid DNS servers and networking configuration that allows
traffic from the file system to the domain controller.
```

Use the following steps to troubleshoot and resolve the issue.

1. Verify that you followed the prerequisites for having network
   connectivity and routing established between the subnet where you're
   creating an Amazon FSx file system, and your self-managed Active Directory. For
   more information, see [Prerequisites](self-managed-AD.md#self-manage-prereqs "self-managed-AD.md#self-manage-prereqs").

Use the [Amazon FSx Active Directory Validation tool](validate-ad-config.md "validate-ad-config.md")
to test and verify these network settings.

###### Note

If you have multiple Active Directory sites defined, ensure that the
subnets in the VPC associated with your Amazon FSx file system are defined in an
Active Directory site and that no IP conflicts exist between the subnets in
your VPC and the subnets in your other sites. You can view and change these
settings using the Active Directory Sites and Services MMC snap-in. 2. Verify that you configured the VPC security groups that you associated
with your Amazon FSx file system, along with any VPC network ACLs, to allow
outbound network traffic on all ports.

###### Note

If you want to implement least privilege, you can allow outbound
traffic only to the specific ports required for communication with the
Active Directory domain controllers. For more information, see the
[Microsoft Active Directory documentation](https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts "https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts"). 3. Verify that the values for Microsoft Windows file server or network
administrative properties do not contain non-Latin-1 characters. For example,
the file system creation fails if you use `Domänen-Admins` as the
name of the file system administrators group. 4. Verify that your Active Directory domain's DNS servers and domain
controllers are active and able to respond to requests for the domain
provided. 5. Ensure that the functional level of your Active Directory domain is
Windows Server 2008 R2 or higher. 6. Make sure that the firewall rules on your Active Directory domain's
domain controllers allow traffic from your Amazon FSx file system. For more
information, see the [Microsoft Active Directory documentation](https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts "https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts").

## Invalid service account credentials

Creating a file system joined to a self-managed Active Directory fails with the
following error message:

```
Amazon FSx is unable to establish a connection with your Microsoft Active Directory domain controllers
because the service account credentials provided are invalid. To fix this problem, delete your file
system and create a new one using a valid service account.
```

Use the following steps to troubleshoot and resolve the issue.

**Case 1: If you are using an AWS Secrets Manager secret to store your Active Directory credentials**

1. Review [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows "self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows").
2. at the secret ARN is correct and follows the proper format: `arn:aws:secretsmanager:region:account-id:secret:secret-name-6chars`.
3. Verify that the secret contains both required fields with non-empty values:
   - `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME` – Your AD service account username.
   - `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD` – Your AD service account password.

4. Verify that the secret and key have a resource-based policy that grants the Amazon FSx service principal `fsx.amazonaws.com` permission to retrieve the secret value.

**Case 2: If you are using plaintext credentials to join your Active Directory**

1. Verify that you're entering only the user name as input for the
   **Service account username**, such as
   `ServiceAcct`, in the self-managed Active Directory
   configuration.

###### Important

DO NOT include a domain prefix (`corp.com\ServiceAcct`) or
domain suffix (`ServiceAcct@corp.com`) when entering the
service account user name.

DO NOT use the distinguished name (DN) when entering the service
account user name (CN=ServiceAcct,OU=example,DC=corp,DC=com). 2. Verify that the service account that you provided exists in your Active
Directory domain. 3. Make sure that you delegated the required permissions to the service
account that you provided. The service account must be able to create and
delete computer objects in the OU in the domain to which you're joining
the file system. The service account also needs, at a minimum, to have
permissions to do the following:

    * Reset passwords
    * Restrict accounts from reading and writing data
    * Validated ability to write to the DNS hostname
    * Validated ability to write to the service principal name

For more information about creating a service account with correct
permissions, see [Amazon FSx service account](self-managed-AD.md#self-managed-AD-service-account "self-managed-AD.md#self-managed-AD-service-account").

## Amazon FSx can't access your Active Directory service account credentials in AWS Secrets Manager

The following sections describe common issues and how to resolve them.

**Joining a file system to your self-managed Active Directory fails with the following error message:**

`You can't provide both username/password and a domain join service account secret to connect to your Active Directory. Provide only one set of credentials.`

###### To resolve this issue

1. Choose whether you want to provide credentials stored in a Secrets Manager secret, or in plaintext.
2. When joining an Active Directory, only provide one of those parameters and not both.

**Joining a file system to your self-managed Active Directory fails with the following error message:**

`The domain join service account secret ARN format you entered isn't valid. Use the format: arn:partition:secretsmanager:region:account-id:secret:secret-name-6chars`

###### To resolve this issue

1. Review [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows "self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows").
2. Verify that the ARN format you are entering is correct. A correct format example is `arn:aws:secretsmanager:us-east-1:123456789012:secret:MyDatabaseSecret-Ab3d5f`.

**Joining a file system to your self-managed Active Directory fails with the following error message:**

`Amazon FSx can't access the domain join service account secret [ARN]. Add a resource permission to the secret that grants the FSx service principal (fsx.amazonaws.com) permission to access it.`

###### To resolve this issue

1. Review [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows "self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows").
2. Verify that the Secrets Manager secret you are providing has the correct policies that allow Amazon FSx to use the secret.

**Joining a file system to your self-managed Active Directory fails with the following error message:**

`You don't have permission to access the domain join service account secret [ARN]. A resource permission needs to be added to the secret to grant you access.`

###### To resolve this issue

- The Secrets Manager secret owner or administrator needs to give your account access to use this secret. For more information, see [Identity-based policies](../../../secretsmanager/latest/userguide/auth-and-access_iam-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_iam-policies.md").

**Joining a file system to your self-managed Active Directory fails with the following error message:**

`The domain join service account secret format or content isn't valid. Make sure the secret includes both CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME and CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD fields with non-empty values.`

###### To resolve this issue

1. Review [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows "self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows").
2. Verify that the Secrets Manager secret you are providing has both of the required fields.

## Insufficient service account permissions

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
Amazon FSx is unable to establish a connection with your
Microsoft Active Directory domain controllers. This is because the service account provided does not
have permission to join the file system to the domain with the specified organizational unit.
To fix this problem, delete your file system and create a new one using a service account with
permission to join the file system to the domain with the specified organizational unit.
```

Use the following procedure to troubleshoot and resolve the issue.

- Make sure that you delegated the required permissions to the service
  account that you provided. The service account must be able to create and
  delete computer objects in the OU in the domain to which you're joining
  the file system. The service account also needs, at a minimum, to have
  permissions to do the following:
  - Reset passwords
  - Restrict accounts from reading and writing data
  - Validated ability to write to the DNS hostname
  - Validated ability to write to the service principal name
    For more information about creating a service account with correct
    permissions, see [Amazon FSx service account](self-managed-AD.md#self-managed-AD-service-account "self-managed-AD.md#self-managed-AD-service-account").

## Service account capacity exceeded

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
Amazon FSx can't establish a connection with your Microsoft Active Directory
domain controllers. This is because the service account provided has reached the
maximum number of computers that it can join to the domain. To fix this problem,
delete your file system and create a new one, supplying a service account that
is able to join new computers to the domain.
```

To resolve the issue, verify that the service account you provided has reached the
maximum number of computers it can join to the domain. If it has reached the
maximum limit, create a new service account with the correct permissions.
Use the new service account and create a new file system.
For more information, see [Amazon FSx service account](self-managed-AD.md#self-managed-AD-service-account "self-managed-AD.md#self-managed-AD-service-account").

## Amazon FSx can't access the organizational unit (OU)

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
Amazon FSx can't establish a connection with your Microsoft Active Directory domain controller(s).
This is because the organizational unit you specified either doesn't exist or isn't accessible
to the service account provided. To fix this problem, delete your file system and create a new one specifying an
organizational unit to which the service account can join the file system.
```

Use the following steps to troubleshoot and resolve the issue.

1. Verify that the OU you provided is in your Active Directory domain.
2. Make sure that you have delegated the required permissions to the service
   account that you provided. The service account must be able to create and
   delete computer objects in the OU in the domain that you're joining
   the file system to. The service account also needs to have, at a minimum,
   permissions to do the following:
   - Reset passwords
   - Restrict accounts from reading and writing data
   - Validated ability to write to the DNS hostname
   - Validated ability to write to the service principal name
   - Be delegated control to create and delete computer objects
   - Validated ability to read and write Account Restrictions
     For more information about creating a service account with the correct
     permissions, see [Amazon FSx service account](self-managed-AD.md#self-managed-AD-service-account "self-managed-AD.md#self-managed-AD-service-account").

## Service account can't access the administrators group

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
Amazon FSx is unable to apply your Microsoft Active Directory configuration. This is because the file system
administrators group you provided either doesn't exist or isn't accessible to the service account you
provided. To fix this problem, delete your file system and create a new one specifying a file
system administrators group in the domain that is accessible to the service account
provided.
```

Use the following steps to troubleshoot and resolve the issue.

1. Ensure that you’re providing just the name of the group as a string for the
   administrators group parameter.

###### Important

DO NOT include a domain prefix (`corp.com\FSxAdmins`) or
domain suffix (`FSxAdmins@corp.com`) when providing the group
name parameter.

DO NOT use the distinguished name (DN) for the group. An example of a
distinguished name is CN=FSxAdmins,OU=example,DC=corp,DC=com. 2. Ensure that the administrators group provided exists in the same Active
Directory domain as the one that you want to join the file
system to. 3. If you did not provide an administrator group parameter, Amazon FSx attempts
to use the `Builtin Domain Admins` group in your Active
Directory domain. If the name of this group has been changed, or if
you’re using a different group for domain administration, you need to
provide that name for the group.

## Amazon FSx lost connectivity in domain

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
Amazon FSx is unable to apply your Microsoft Active Directory configuration. To fix this problem, delete your file system and create a new one
meeting the pre-requisites described in the Amazon FSx user guide.
```

When creating your file system, Amazon FSx was able to reach your Active Directory
domain’s DNS servers and domain controllers, and join the file system
successfully to your Active Directory domain. However, while completing file
system creation, Amazon FSx lost connectivity to or membership in your domain. Use
the following steps to troubleshoot and resolve the issue.

1. Ensure that network connectivity continues to exist between your Amazon FSx file
   system and your Active Directory. And, ensure that network traffic continues to be
   allowed between them by using routing rules, VPC security group rules, VPC network ACLs,
   and domain controller firewall rules.
2. Ensure that the computer objects created by Amazon FSx for your file systems
   in your Active Directory domain are still active, and were not deleted
   or otherwise manipulated.

## Service account does not have correct permissions

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
File system creation failed. Amazon FSx is unable to establish a connection with your Microsoft Active Directory domain controller(s).
This is because the service account provided does not have permission to join the file system to the domain with the specified
organizational unit (OU). To fix this problem, delete your file system and create a new one using a service account with permission
to create computer objects and reset passwords within the specified organizational unit.
```

Make sure that you have delegated the required permissions to the service account
that you provided. Use the following steps to troubleshoot and resolve the
issue.

The service account needs to have, at a minimum, the following permissions:

- Be delegated control to create and delete computer objects in the OU that you’re joining the file system to
- Have the following permissions in the OU that you’re joining the file system to:

      + Ability to reset passwords
      + Ability to restrict accounts from reading and writing data
      + Validated ability to write to the DNS hostname
      + Validated ability to write to the service principal name
      + Ability (can be delegated) to create and delete computer objects
      + Validated ability to read and write Account Restrictions
      + Ability to modify permissions

  For more information about creating a service account with the correct permissions, see
  [Amazon FSx service account](self-managed-AD.md#self-managed-AD-service-account "self-managed-AD.md#self-managed-AD-service-account").

## Unicode characters used in creation parameters

Creating a file system joined to your self-managed Active Directory fails with the
following error message:

```
File system creation failed. Amazon FSx is unable to create a file system within the specified
Microsoft Active Directory. To fix this problem, please delete your file system and create a new one
meeting the pre-requisites described in the FSx for ONTAP User Guide.
```

Amazon FSx does not support Unicode characters. Verify that none of the creation
parameters have Unicode characters, such as accent marks. This includes
parameters that can be left blank where a default value is filled in automatically.
Ensure the corresponding default values in your Active Directory also do not
contain Unicode characters.

## Switching storage type to HDD while restoring a backup fails

Creating a file system from a backup fails with the following error message:

`Switching storage type to HDD while creating a file system from backup `backup_id`is not supported
 because a storage scaling activity was still under way on the source file system to increase storage
 capacity from less than 2000 GiB when the backup`backup_id` was taken, and the minimum storage capacity
 for HDD storage is 2000 GiB.`

This issue occurs when restoring a backup and you have changed the storage type from SSD to HDD. The restore from backup fails because the
backup that you are restoring was taken while a storage capacity increase was still in progress on the original file system. The file system's SSD storage
capacity before the increase request was less than 2000 GiB, which is the minimum storage capacity required to create an HDD file system.

Use the following procedure to resolve this issue.

1. Wait for the storage capacity increase request to complete and the file system has at least 2000 GiB of SSD storage capacity.
   For more information, see [Monitoring storage capacity
   increases](monitoring-storage-capacity-increase.md "monitoring-storage-capacity-increase.md").
2. Take a user-initiated backup of the file system. For more information, see [Working with user-initiated backups](using-backups.md#user-initiated-backups "using-backups.md#user-initiated-backups").
3. Restore the user-initiated backup to a new file system using HDD storage. For more information, see [Restoring backups to new file system](using-backups.md#restoring-backups "using-backups.md#restoring-backups").
