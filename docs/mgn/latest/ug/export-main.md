NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Exporting your data inventory

The **Export** feature allows you to easily export your
inventory of servers, applications, and waves to a CSV file that is saved in your local disk
or an S3 bucket.

###### Note

The export feature is not supported for IPv6.

## Defining required permissions for export

In order to use the export feature, you will need to create a role with the following policies (or any extension of them):

**Managed policies:**

- AWSApplicationMigrationReadOnlyAccess

**Additional policies:**

```
{
  "Sid":  "AllowS3Access",
   "Effect":  "Allow",
   "Action": [
     "s3:GetObject"
  ],
   "Resource":  "arn:aws:s3:::amzn-s3-demo-bucket"
},
{
   "Sid": "AllowMgnStartExport",
   "Effect": "Allow",
   "Action": [
     "mgn:StartExport"
  ],
   "Resource": "*"
}
```

When starting an export on an Amazon S3 bucket source that is owned by another account,
ensure that the role or user has access to the Amazon S3 objects. When using the API, the Amazon S3
bucket owner parameter defaults to the current user’s account ID.

The following is an example of an Amazon S3 bucket policy in the target account:

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
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
 }
 ]
}`

```

###### Note

If the Amazon S3 objects are encrypted with SSE-KMS, ensure that the role or user initiating
the export has access to decrypt using the AWS KMS key. This feature does not support SSE-C
encrypted Amazon S3 objects.

## Required Amazon S3 bucket permissions

Before you create an export job, you must create the destination S3 bucket to export to.
AWS Application Migration Service doesn't create the S3 bucket for you. The S3 bucket that you specify can't be
publicly accessible, and can't be configured as a [Requester Pays](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") bucket. After you create the S3 bucket, confirm that the bucket
has the required permissions policy to allow AWS Application Migration Service to write the export files to
it.

## Export parameters

The exported file can include multiple parameters, including:

|                                                     |                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Parameter**                                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                              |
| **mgn:account-id**                                  | The ID of the account being exported.                                                                                                                                                                                                                                                                                                                                                                        |
| **mgn:app:description**                             | The description of the application being exported.                                                                                                                                                                                                                                                                                                                                                           |
| **mgn:app:id**                                      | The ID of the application being exported.                                                                                                                                                                                                                                                                                                                                                                    |
| **mgn:app:name**                                    | The name of the application being exported.                                                                                                                                                                                                                                                                                                                                                                  |
| **mgn:app:tag:appkey1**                             | The value of the application tag key (in this example, the tag key is appkey1).                                                                                                                                                                                                                                                                                                                              |
| **mgn:launch:iam-instance-profile:name**            | The name of the instance profile associated with the launch instance.                                                                                                                                                                                                                                                                                                                                        |
| **mgn:launch:instance-type**                        | The EC2 instance type of the launch instance (for example, m4.large).                                                                                                                                                                                                                                                                                                                                        |
| **mgn:launch:nic:0:network-interface-id**           | The ID of the network interface that appears first in the launch template ("0" refers to the first network interface, "1" would refer to the second network interface, and so on).                                                                                                                                                                                                                           |
| **mgn:launch:nic:0:private-ip:0**                   | The private IP that appears first in the network interface that appears first in the launch template.                                                                                                                                                                                                                                                                                                        |
| **mgn:launch:nic:0:security-group-id:0**            | The security group that appears first in the network interface that appears first in the launch template.                                                                                                                                                                                                                                                                                                    |
| **mgn:launch:nic:0:subnet-id**                      | The subnet ID that appears first in the network interface that appears first in the launch template.                                                                                                                                                                                                                                                                                                         |
| **mgn:launch:placement:host-id**                    | The host ID of the placement of the launch instance.                                                                                                                                                                                                                                                                                                                                                         |
| **mgn:launch:placement:operating-system-licensing** | The operating system licensing approach, LI, (license Included) or BYOL (bring your own license).                                                                                                                                                                                                                                                                                                            |
| **mgn:launch:placement:tenancy**                    | This tenancy of the launch instance. Expected values: default, dedicated, or host.                                                                                                                                                                                                                                                                                                                           |
| **mgn:launch:tag:instance:key1**                    | The value of launch instance tag "key1" (in this example, the tag key is key1).                                                                                                                                                                                                                                                                                                                              |
| **mgn:launch:volume:/dev/sda:type**                 | The type of the launch instance's volume whose name is /dev/sda (in this example, the volume's name is /dev/sda).                                                                                                                                                                                                                                                                                            |
| **mgn:region**                                      | The AWS Region to which you are importing, which must be the Region of your MGN console.<br>If left blank, defaults to the console Region.                                                                                                                                                                                                                                                                   |
| **mgn:server:fqdn-for-action-framework**            | The FQDN that the MGN connector uses to connect to the server.                                                                                                                                                                                                                                                                                                                                               |
| **mgn:server:id**                                   | The server ID.                                                                                                                                                                                                                                                                                                                                                                                               |
| **mgn:server:lifecycle-state**                      | The server's lifecycle state.                                                                                                                                                                                                                                                                                                                                                                                |
| **mgn:server:platform**                             | The server's platform (Linux or Windows).                                                                                                                                                                                                                                                                                                                                                                    |
| **mgn:server:replication-type**                     | The type of the replication (agent-based or agentless).                                                                                                                                                                                                                                                                                                                                                      |
| **mgn:server:replication-state**                    | The state of the replication.                                                                                                                                                                                                                                                                                                                                                                                |
| **mgn:server:tag:serverkey1**                       | The value of the server tag key (in this example, the tag key is serverkey1).                                                                                                                                                                                                                                                                                                                                |
| **mgn:server:user-provided-id**                     | The server's user-provided ID. This parameter is used by Application Migration Service to consistently recognize the server replication, and avoid duplication when importing inventory from a CSV file. This parameter should be provided during the<br>AWS replication agent installation by the MGN connector or other installation method. Once provided for a server this parameter cannot be modified. |
| **mgn:wave:description**                            | The description of the exported wave.                                                                                                                                                                                                                                                                                                                                                                        |
| **mgn:wave:id**                                     | The ID of the exported wave.                                                                                                                                                                                                                                                                                                                                                                                 |
| **mgn:wave:name**                                   | The name of the exported wave.                                                                                                                                                                                                                                                                                                                                                                               |
| **mgn:wave:tag:appkey1**                            | The value of the wave tag key (in this example, the tag key is appkey1).                                                                                                                                                                                                                                                                                                                                     |
| **mgn:launch:transfer-server-tags**                 | The option to transfer any user-configured custom tags from your source servers onto your test or cutover instance.                                                                                                                                                                                                                                                                                          |

###### Note

If the bucket you're exporting to is encrypted with customer managed keys (KMS), that KMS
key's policies must give AWS MGN permission to use it. This permission is given through
the user or role that initiates the export job.

If you choose to encrypt your export using a key protected by AWS Key Management Service (AWS KMS),
the key must be in the same Region as the destination S3 bucket.
