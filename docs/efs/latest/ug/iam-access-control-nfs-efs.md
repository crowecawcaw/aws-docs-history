# Using IAM to control access to file

systems

You can use both IAM identity policies and resource policies to control client access to
Amazon EFS resources in a way that is scalable and optimized for cloud environments. Using IAM,
you can permit clients to perform specific actions on a file system, including read-only,
write, and root access. An "allow" permission on an action in _either_ an
IAM identity policy _or_ a file system resource policy allows access for
that action. The permission does not need to be granted in _both_ an
identity _and_ a resource policy.

NFS clients can identify themselves using an IAM role when connecting to an
EFS file system. When a client connects to a file system, Amazon EFS evaluates the file
system’s IAM resource policy, which is called a file system policy, along with any
identity-based IAM policies to determine the appropriate file system access permissions to
grant.

When you use IAM authorization for NFS clients, client connections and IAM authorization decisions are logged to
AWS CloudTrail. For more information about how to log Amazon EFS API calls with CloudTrail, see
[Logging Amazon EFS API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

###### Important

You must use the EFS mount helper to mount your EFS file systems in order to use
IAM authorization to control client access. For more information, see
[Mounting with IAM authorization](mounting-IAM-option.md "mounting-IAM-option.md").

## Default EFS file system policy

The default EFS file system policy does not use IAM to authenticate, and grants full access to any anonymous client
that can connect to the file system using a mount target. The default policy is in effect
whenever a user-configured file system policy is not in effect, including at file system creation.
Whenever the default file system policy is in
effect, a `DescribeFileSystemPolicy`
API operation returns a `PolicyNotFound` response.

## EFS actions for clients

You can specify the following actions for clients accessing a file system using a file system policy.

| Action                                     | Description                                                                                                                                                                            |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `elasticfilesystem:ClientMount`            | Provides read-only access to a file system.                                                                                                                                            |
| `elasticfilesystem:ClientWrite`            | Provides write permissions on a file system.                                                                                                                                           |
| `elasticfilesystem:ClientRootAccess`       | Provides use of the root user when accessing a file system.                                                                                                                            | ## EFS condition keys for clients To express conditions, you use predefined condition keys. Amazon EFS has the following predefined condition keys for NFS clients. Any other condition keys are not enforced when using IAM controls to secure access to EFS file systems. |
| EFS Condition Key                          | Description                                                                                                                                                                            | Operator                                                                                                                                                                                                                                                                    |
| ---                                        | ---                                                                                                                                                                                    | ---                                                                                                                                                                                                                                                                         |
| `aws:SecureTransport`                      | Use this key to require clients to use TLS when connecting to an EFS file system.                                                                                                      | Boolean                                                                                                                                                                                                                                                                     |
| `aws:SourceIp`                             | Use this key to compare the requester's IP address with the IP address that you specify in the policy. The `aws:SourceIp` condition key can only be used for public IP address ranges. | String                                                                                                                                                                                                                                                                      |
| `elasticfilesystem:AccessPointArn`         | ARN of the EFS access point to which the client is connecting.                                                                                                                         | String                                                                                                                                                                                                                                                                      |
| `elasticfilesystem:AccessedViaMountTarget` | Use this key to prevent access to an EFS file system by clients that are not using file system mount targets.                                                                          | Boolean                                                                                                                                                                                                                                                                     | ## File system policy examples To view examples of Amazon EFS file system policies, see [Resource-based policy examples for Amazon EFS](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md"). |
