# WorkSpaces Pools troubleshooting notification codes

The following are notification codes and resolution steps for issues with domain
join that you might encounter when you set up and use Active Directory with
WorkSpaces.

**DOMAIN_JOIN_ERROR_ACCESS_DENIED**

**Message**: Access is denied.

**Resolution**: The service account specified in
the directory does not have permissions to create the computer object or reuse
an existing one. Validate the permissions and start the WorkSpaces pool.

**DOMAIN_JOIN_ERROR_LOGON_FAILURE**

**Message**: The username or password is
incorrect.

**Resolution**: The service account specified in
the directory has an invalid username or password. Update the credentials in the
AWS Secrets Manager secret configured in the directory, and start the WorkSpaces pool
again.

**DOMAIN_JOIN_NERR_PASSWORD_EXPIRED**

**Message**: The password of this user
has expired.

**Resolution**: The password for the service
account in the AWS Secrets Manager secret has expired. First, stop the WorkSpaces pool. Next,
change the password for the secret specified in the WorkSpaces directory. Then, start
the WorkSpaces pool.

**DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED**

**Message**: Your computer could not be
joined to the domain. You have exceeded the maximum number of computer
accounts you are allowed to create in this domain. Contact your system
administrator to have this limit reset or increased.

**Resolution**: The service account specified on
the directory does not have permissions to create the computer object or reuse
an existing one. Validate the permissions and start the WorkSpaces pool.

**DOMAIN_JOIN_ERROR_INVALID_PARAMETER**

**Message**: A parameter is incorrect.
This error is returned if the `LpName` parameter is NULL or the `NameType`
parameter is specified as `NetSetupUnknown` or an unknown nametype.

**Resolution**: This error can occur when
the distinguished name for the OU is incorrect. Validate the OU and try again. If you continue to encounter this error,
contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_MORE_DATA**

**Message**: More data is
available.

**Resolution**: This error can occur when the distinguished
name for the OU is incorrect. Validate the OU and try again. If you continue to encounter this error, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN**

**Message**: The specified domain either
does not exist or could not be contacted.

**Resolution**: The streaming instance was unable
to contact your Active Directory domain. To ensure network connectivity, confirm
your VPC, subnet, and security group settings.

**DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED**

**Message**: The Workstation service has
not been started.

**Resolution**: An error occurred
starting the Workstation service. Ensure that the service is enabled in
your image. If you continue to encounter this error, contact AWS Support. For
more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_NOT_SUPPORTED**

**Message**: The request is not
supported. This error is returned if a remote computer was specified in
the `lpServer` parameter and this call is not supported on the remote
computer.

**Resolution**: Contact AWS Support for
assistance. For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_FILE_NOT_FOUND**

**Message**: The system cannot find the
file specified.

**Resolution**: This error occurs when an invalid
organizational unit (OU) distinguished name is provided. The distinguished name
must start with `OU=`. Validate the OU distinguished name
and try again.

**DOMAIN_JOIN_INTERNAL_SERVICE_ERROR**

**Message**: The account already exists.

**Resolution**: This error can occur in the following scenarios:

- If the issue isn't permissions-related, check the Netdom logs
  for errors and make sure that you provided the correct
  OU.
- The service account specified in the directory does not have
  permissions to create the computer object or reuse an existing one. If
  this is the case, validate the permissions and start the WorkSpaces pool.
- After WorkSpaces creates the computer object, it is moved from the OU in
  which it was created. In this case, the first WorkSpaces pool is created
  successfully, but any new WorkSpaces pool that uses the computer object
  fails. When Active Directory searches for the computer object in the
  specified OU and detects that an object with the same name exists
  elsewhere in the domain, the domain join is not successful.
- The name of the OU specified in the WorkSpaces directory includes spaces
  before or after the commas in the directory. In this case, when a WorkSpaces
  pool attempts to rejoin the Active Directory domain, WorkSpaces cannot cycle
  the computer objects correctly and the domain rejoin does not succeed.
  To resolve this issue for a WorkSpaces pool, do the following:

      1. Stop the WorkSpaces pool.
      2. Edit the Active Directory domain settings for the WorkSpaces pool
       to remove the directory and Directory OU to which the WorkSpaces pool
       is joined.
      3. Update the WorkSpaces directory to specify an OU that doesn't
       contain spaces.
      4. Edit the Active Directory domain settings for the WorkSpaces pool
       to specify the directory with the updated Directory OU.

  To resolve this issue for a WorkSpaces pool, do the following:

      1. Delete the WorkSpaces pool.
      2. Update the WorkSpaces directory to specify an OU that doesn't
       contain spaces.
      3. Create a new WorkSpaces pool and specify the directory with the
       updated Directory OU.

**WORKSPACES_POOL_SESSION_RESERVATION_ERROR**

**Message**: We currently do not have sufficient capacity for
requested sessions in the availability zones [us-west-1] for subnets associated with your WorkSpaces Pool.
Our system will be working on provisioning additional capacity. Meanwhile, please change or associate
a different subnet using one of the following AZs [us-west-2, us-west-3].

**Resolution**: Wait until EC2 has enough capacity or update subnets
in other AZs on the directory.

**INSUFFICIENT_CAPACITY_ERROR_WORKSPACES_POOL_AZ**

**Message**: We currently don't have sufficient capacity for requested
sessions in availability zone (AZs) [<impacted az>]. Our system will be working on provisioning additional capacity.
Meanwhile please change or associate another subnet using other AZs to your WorkSpaces Pool.

**Resolution**: Wait until Amazon EC2 has enough capacity or update subnets in other AZs on the directory.

**INVALID_CUSTOMER_SUBNET_CIDR_BLOCK**

**Message**: Your subnet includes use of an unavailable CIDR range.
Please update your subnets outside of the current /18 range.”.

**Resolution**: Wait until EC2 has enough capacity or update subnets in other AZs on the directory.
