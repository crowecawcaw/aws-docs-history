# Configure IAM roles for EMRFS requests to

Amazon S3

###### Note

The EMRFS role mapping capability described on this page has been improved upon
with the introduction of Amazon S3 Access Grants in Amazon EMR 6.15.0. For a scalable access control
solution for your data in Amazon S3, we recommend that you use [S3 Access Grants with Amazon EMR](emr-access-grants.md "emr-access-grants.md").

When an application running on a cluster references data using the
`s3://`mydata`` format,
Amazon EMR uses EMRFS to make the request. To interact with Amazon S3, EMRFS assumes the
permissions policies that are attached to your [Amazon EC2 instance profile](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md"). The same Amazon EC2 instance profile is used regardless
of the user or group running the application or the location of the data in Amazon S3.

If you have a cluster with multiple users who need different levels of access to data
in Amazon S3 through EMRFS, you can set up a security configuration with IAM roles for
EMRFS. EMRFS can assume a different service role for cluster EC2 instances based on the user or group
making the request, or based on the location of data in Amazon S3. Each IAM role for EMRFS
can have different permissions for data access in Amazon S3. For more information about the
service role for cluster EC2 instances, see [Service role for cluster EC2 instances (EC2
instance profile)](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md").

Using custom IAM roles for EMRFS is supported in Amazon EMR versions 5.10.0 and later. If
you use an earlier version or have requirements beyond what IAM roles for EMRFS
provide, you can create a custom credentials provider instead. For more information, see
[Authorizing access to
EMRFS data in Amazon S3](../ReleaseGuide/emr-plan-credentialsprovider.md "../ReleaseGuide/emr-plan-credentialsprovider.md").

When you use a security configuration to specify IAM roles for EMRFS, you set up
role mappings. Each role mapping specifies an IAM role that corresponds to
identifiers. These identifiers determine the basis for access to Amazon S3 through EMRFS. The
identifiers can be users, groups, or Amazon S3 prefixes that indicate a data location. When
EMRFS makes a request to Amazon S3, if the request matches the basis for access, EMRFS has
cluster EC2 instances assume the corresponding IAM role for the request. The IAM
permissions attached to that role apply instead of the IAM permissions attached to the
service role for cluster EC2 instances.

The users and groups in a role mapping are Hadoop users and groups that are defined on
the cluster. Users and groups are passed to EMRFS in the context of the application
using it (for example, YARN user impersonation). The Amazon S3 prefix can be a bucket
specifier of any depth (for example, `s3://amzn-s3-demo-bucket` or
`s3://amzn-s3-demo-bucket/myproject/mydata`). You can specify multiple identifiers
within a single role mapping, but they all must be of the same type.

###### Important

IAM roles for EMRFS provide application-level isolation between users of the
application. It does not provide host level isolation between users on the host. Any
user with access to the cluster can bypass the isolation to assume any of the
roles.

When a cluster application makes a request to Amazon S3 through EMRFS, EMRFS evaluates role
mappings in the top-down order that they appear in the security configuration. If a
request made through EMRFS doesn't match any identifier, EMRFS falls back to using the
service role for cluster EC2 instances. For this reason, we recommend that the policies attached to this
role limit permissions to Amazon S3. For more information, see [Service role for cluster EC2 instances (EC2
instance profile)](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md").

## Configure roles

Before you set up a security configuration with IAM roles for EMRFS, plan and
create the roles and permission policies to attach to the roles. For more
information, see [How do
roles for EC2 instances work?](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
_IAM User Guide_. When creating permissions policies, we
recommend that you start with the managed policy attached to the default Amazon EMR role
for EC2, and then edit this policy according to your requirements. The default role
name is `EMR_EC2_DefaultRole`, and the default managed policy to edit is
`AmazonElasticMapReduceforEC2Role`. For more information, see [Service role for cluster EC2 instances (EC2
instance profile)](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md").

### Updating trust policies to

assume role permissions

Each role that EMRFS uses must have a trust policy that allows the cluster's
Amazon EMR role for EC2 to assume it. Similarly, the cluster's Amazon EMR role for EC2
must have a trust policy that allows EMRFS roles to assume it.

The following example trust policy is attached to roles for EMRFS. The
statement allows the default Amazon EMR role for EC2 to assume the role. For example,
if you have two fictitious EMRFS roles, `EMRFSRole_First` and
`EMRFSRole_Second`, this policy statement is added to the trust
policies for each of them.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::123456789012:role/EMR_EC2_DefaultRole",
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```

In addition, the following example trust policy statement is added to the
`EMR_EC2_DefaultRole` to allow the two fictitious EMRFS roles to
assume it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/EMRFSRole_First",
 "arn:aws:iam::123456789012:role/EMRFSRole_Second"
 ],
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```

###### To update the trust policy of an IAM role

Open the IAM console at
[https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

1. Choose **Roles**, enter the name of the role in
   **Search**, and then select its **Role
   name**.
2. Choose **Trust relationships**, **Edit trust
   relationship**.
3. Add a trust statement according to the **Policy
   document** according to the guidelines above, and then
   choose **Update trust policy**.

### Specifying a role as a key

user

If a role allows access to a location in Amazon S3 that is encrypted using an
AWS KMS key, make sure that the role is specified as a key user. This gives
the role permission to use the KMS key. For more information, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users") in the
_AWS Key Management Service Developer Guide_.

## Set up a security configuration with

IAM roles for EMRFS

###### Important

If none of the IAM roles for EMRFS that you specify apply, EMRFS falls back
to the Amazon EMR role for EC2. Consider customizing this role to restrict
permissions to Amazon S3 as appropriate for your application and then specifying this
custom role instead of `EMR_EC2_DefaultRole` when you create a
cluster. For more information, see [Customize IAM roles with Amazon EMR](emr-iam-roles-custom.md "emr-iam-roles-custom.md") and [Specify custom IAM roles when you
create a cluster](emr-iam-roles-custom.md#emr-iam-roles-launch-jobflow "emr-iam-roles-custom.md#emr-iam-roles-launch-jobflow").

###### To specify IAM roles for EMRFS requests to Amazon S3 using the console

1. Create a security configuration that specifies role mappings:
   1. In the Amazon EMR console, select **Security
      configurations**, **Create**.
   2. Type a **Name** for the security configuration.
      You use this name to specify the security configuration when you
      create a cluster.
   3. Choose **Use IAM roles for EMRFS requests to
      Amazon S3**.
   4. Select an **IAM role** to apply, and under
      **Basis for access** select an identifier type
      (**Users**, **Groups**, or
      **S3 prefixes**) from the list and enter
      corresponding identifiers. If you use multiple identifiers, separate
      them with a comma and no space. For more information about each
      identifier type, see the [JSON configuration reference](#emrfs-seccfg-json "#emrfs-seccfg-json")
      below.
   5. Choose **Add role** to set up additional role
      mappings as described in the previous step.
   6. Set up other security configuration options as appropriate and
      choose **Create**. For more information, see [Create a security
      configuration with the Amazon EMR console or with the AWS CLI](emr-create-security-configuration.md "emr-create-security-configuration.md").

2. Specify the security configuration you created above when you create a
   cluster. For more information, see [Specify a security configuration
   for an Amazon EMR cluster](emr-specify-security-configuration.md "emr-specify-security-configuration.md").

###### To specify IAM roles for EMRFS requests to Amazon S3 using the AWS CLI

1. Use the `aws emr create-security-configuration` command,
   specifying a name for the security configuration, and the security
   configuration details in JSON format.

The example command shown below creates a security configuration with the
name `EMRFS_Roles_Security_Configuration`. It is based on a JSON
structure in the file `MyEmrfsSecConfig.json`, which is saved in
the same directory where the command is executed.

```
aws emr create-security-configuration --name `EMRFS_Roles_Security_Configuration` --security-configuration `file://MyEmrFsSecConfig.json`.
```

Use the following guidelines for the structure of the
`MyEmrFsSecConfig.json` file. You can specify this structure
along with structures for other security configuration options. For more
information, see [Create a security
configuration with the Amazon EMR console or with the AWS CLI](emr-create-security-configuration.md "emr-create-security-configuration.md").

The following is an example JSON snippet for specifying custom IAM roles for EMRFS within a security
configuration. It demonstrates role mappings for the three different identifier types,
followed by a parameter reference.

```
{
  "AuthorizationConfiguration": {
    "EmrFsConfiguration": {
      "RoleMappings": [{
        "Role": "`arn:aws:iam::123456789101:role/allow_EMRFS_access_for_user1`",
        "IdentifierType": "User",
        "Identifiers": [ "`user1`" ]
      },{
        "Role": "`arn:aws:iam::123456789101:role/allow_EMRFS_access_to_demo_s3_buckets`",
        "IdentifierType": "Prefix",
        "Identifiers": [ "`s3://amzn-s3-demo-bucket1/","s3://amzn-s3-demo-bucket2/`" ]
      },{
        "Role": "`arn:aws:iam::123456789101:role/allow_EMRFS_access_for_AdminGroup`",
        "IdentifierType": "Group",
        "Identifiers": [ "`AdminGroup`" ]
      }]
    }
  }
}

```

| Parameter                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"AuthorizationConfiguration":` | Required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `"EmrFsConfiguration":`         | Required. Contains role mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `"RoleMappings":`               | Required. Contains one or more role mapping definitions. Role mappings are evaluated in the top-down order that they appear. If a role mapping evaluates as true for an EMRFS call for data in Amazon S3, no further role mappings are evaluated and EMRFS uses the specified IAM role for the request. Role mappings consist of the following required parameters:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `"Role":`                       | Specifies the ARN identifier of an IAM role in the format `arn:aws:iam::`account-id`:role/`role-name``. This is the IAM role that Amazon EMR assumes if the EMRFS request to Amazon S3 matches any of the `Identifiers` specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `"IdentifierType":`             | Can be one of the following:<br>• `"User"` specifies that the identifiers are one or more Hadoop users, which can be Linux account users or Kerberos principals. When the EMRFS request originates with the user or users specified, the IAM role is assumed.<br>• `"Prefix"` specifies that the identifier is an Amazon S3 location. The IAM role is assumed for calls to the location or locations with the specified prefixes. For example, the prefix `s3://amzn-s3-demo-bucket/` matches `s3://amzn-s3-demo-bucket/mydir` and `s3://amzn-s3-demo-bucket/yetanotherdir`.<br>• `"Group"` specifies that the identifiers are one or more [Hadoop groups](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/GroupsMapping.html "https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/GroupsMapping.html"). The IAM role is assumed if the request originates from a user in the specified group or groups. |
| `"Identifiers":`                | Specifies one or more identifiers of the appropriate identifier type. Separate multiple identifiers by commas with no spaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

2. Use the `aws emr create-cluster` command to create a cluster
   and specify the security configuration you created in the previous step.

The following example creates a cluster with default core Hadoop
applications installed. The cluster uses the security configuration created
above as `EMRFS_Roles_Security_Configuration` and also uses a
custom Amazon EMR role for EC2, `EC2_Role_EMR_Restrict_S3`, which is
specified using the `InstanceProfile` argument of the
`--ec2-attributes` parameter.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name `MyEmrFsS3RolesCluster` \
--release-label `emr-7.11.0` --ec2-attributes InstanceProfile=`EC2_Role_EMR_Restrict_S3`,KeyName=`MyKey` \
--instance-type `m5.xlarge` --instance-count `3` \
--security-configuration `EMRFS_Roles_Security_Configuration`
```
