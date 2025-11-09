NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Importing your data inventory

The **Import** feature allows you to easily import your
inventory of servers, applications, and waves from a CSV file that is saved in your local disk
or an S3 bucket.

###### Topics

- [Define required permissions for importing](#import-required-permissions "#import-required-permissions")
- [Import parameters](#import-parameters "#import-parameters")
- [Importing your data inventory from a local disk](import-local-disk.md "import-local-disk.md")
- [Importing your data inventory from an S3 bucket](import-s3.md "import-s3.md")
- [View import history](import-history.md "import-history.md")

## Define required permissions for importing

In order to use the import feature, you will need to create a role with the following policies (or any extension of them):

**Managed policies:**

- [AWSApplicationMigrationFullAccess](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md "security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md")
- [AWSApplicationMigrationEC2Access](security-iam-awsmanpol-AWSApplicationMigrationEC2Access.md "security-iam-awsmanpol-AWSApplicationMigrationEC2Access.md")

**Additional policies:**

```
{
  "Sid":  "AllowS3Access",
   "Effect":  "Allow",
   "Action": [
     "s3:GetObject"
  ],
   "Resource":  "arn:aws:s3:::amzn-s3-demo-bucket"
}
```

When starting an import on an Amazon S3 bucket source that is owned by another account,
ensure that the role or user has access to the Amazon S3 objects. When using the API, the Amazon S3
bucket owner parameter defaults to the current user’s account ID.

The following is an example of an S3 bucket policy in the target account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExampleStatement",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/Dave"
 },
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
 }
 ]
}`

```

###### Note

If the Amazon S3 objects are encrypted with SSE-KMS, ensure that the role or user initiating
the import has access to decrypt using the AWS KMS key. This feature does not support SSE-C
encrypted Amazon S3 objects.

## Import parameters

The imported file can include multiple parameters, including:

|                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Parameter**                                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                       |
| **mgn:account-id**                                  | The ID of the account into which to import. This account must be managed by the calling account. Defaults to the calling account.                                                                                                                                                                                                                                                                                     |
| **mgn:app:description**                             | The description of the application being imported.                                                                                                                                                                                                                                                                                                                                                                    |
| **mgn:app:name**                                    | The name of the application being imported.                                                                                                                                                                                                                                                                                                                                                                           |
| **mgn:app:tag:appkey1**                             | The value of the application tag key (in this example, the tag key is appkey1).                                                                                                                                                                                                                                                                                                                                       |
| **mgn:launch:iam-instance-profile:name**            | The name of the instance profile associated with the launch instance.                                                                                                                                                                                                                                                                                                                                                 |
| **mgn:launch:instance-type**                        | The EC2 instance type of the launch instance (for example, m4.large).                                                                                                                                                                                                                                                                                                                                                 |
| **mgn:launch:nic:0:network-interface-id**           | The ID of the network interface that appears first in the launch template ("0" refers to the first network interface, "1" would refer to the second network interface, and so on).                                                                                                                                                                                                                                    |
| **mgn:launch:nic:0:private-ip:0**                   | The private IP that appears first in the network interface that appears first in the launch template.                                                                                                                                                                                                                                                                                                                 |
| **mgn:launch:nic:0:security-group-id:0**            | The security group that appears first in the network interface that appears first in the launch template.                                                                                                                                                                                                                                                                                                             |
| **mgn:launch:nic:0:subnet-id**                      | The subnet ID that appears first in the network interface that appears first in the launch template.                                                                                                                                                                                                                                                                                                                  |
| **mgn:launch:placement:host-id**                    | The host ID of the placement of the launch instance.                                                                                                                                                                                                                                                                                                                                                                  |
| **mgn:launch:placement:operating-system-licensing** | The operating system licensing approach, LI, (license Included) or BYOL (bring your own license).                                                                                                                                                                                                                                                                                                                     |
| **mgn:launch:placement:tenancy**                    | This tenancy of the launch instance.                                                                                                                                                                                                                                                                                                                                                                                  |
| **mgn:launch:tag:instance:key1**                    | The value of launch instance tag "key1" (in this example, the tag key is key1).                                                                                                                                                                                                                                                                                                                                       |
| **mgn:launch:volume:/dev/sda:type**                 | The type of the launch instance's volume whose name is /dev/sda (in this Linux machine example, the volume's name is /dev/sda; for a Windows machine, a typical volume name would be c:0).                                                                                                                                                                                                                            |
| **mgn:region**                                      | The AWS Region to which you are importing, which must be the Region of your MGN console. If left blank, defaults to the console Region.                                                                                                                                                                                                                                                                               |
| **mgn:server:fqdn-for-action-framework**            | The FQDN that the MGN connector uses to connect to the server.                                                                                                                                                                                                                                                                                                                                                        |
| **mgn:server:platform**                             | The server's platform (Linux or Windows).                                                                                                                                                                                                                                                                                                                                                                             |
| **mgn:server:tag:serverkey1**                       | The value of the server tag key (in this example, the tag key is serverkey1).                                                                                                                                                                                                                                                                                                                                         |
| **mgn:server:user-provided-id**                     | The server's user-provided ID. This parameter is used by Application Migration Service to consistently<br>recognize the server replication, and avoid duplication when importing inventory<br>from a CSV file. This parameter should be provided during the AWS replication<br>agent installation by the MGN connector or other installation method. Once<br>provided for a server this parameter cannot be modified. |
| **mgn:wave:description**                            | The description of the imported wave.                                                                                                                                                                                                                                                                                                                                                                                 |
| **mgn:wave:name**                                   | The name of the imported wave.                                                                                                                                                                                                                                                                                                                                                                                        |
| **mgn:wave:tag:appkey1**                            | The value of the wave tag key (in this example, the tag key is appkey1).                                                                                                                                                                                                                                                                                                                                              |
| **mgn:launch:transfer-server-tags**                 | The option to transfer any user-configured custom tags from your source servers onto your test or cutover instance.                                                                                                                                                                                                                                                                                                   |

### Additional considerations

Please note the following considerations regarding the import parameters:

1. Server entries must include either the server IP address, or the FQDN.
2. If a row provides a property of a resource (e.g. mgn:wave:description is a property of a wave),
   then that row should also provide a parameter that identifies that resource (as explained in the following considerations).
3. If a resource's ID (mgn:server:id, mgn:app:id, or mgn:wave:id) is provided, the service will look for this resource in
   order to update it. If this resource is not found, the import will fail.
4. If a resource's ID is not provided, the service will look for a resource's alternative identification:
   - For an application: mgn:app:name
   - For a wave: mgn:wave:name
   - For a server: mgn:server:user-provided-id

5. If a resource's alternative identification exists in AWS MGN,
   the service will update this resource with new values (if applicable).
6. If a resource's alternative identification does not exist in AWS MGN, the service will create the resource.
7. 2 rows that refer to the same resource need not provide the same parameters for that resource,
   but they must not conflict. For example, if 2 rows provide the same mgn:wave:name, it is acceptable for one row
   to provide mgn:wave:description and for the other row to leave the value blank. However, the 2 rows must not provide
   conflicting values of mgn:wave:description.
