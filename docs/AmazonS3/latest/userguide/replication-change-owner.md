# Changing the replica owner

In replication, the owner of the source object also owns the replica by default. However,
when the source and destination buckets are owned by different AWS accounts, you might
want to change the replica ownership. For example, you might want to change the ownership to
restrict access to object replicas. In your replication configuration, you can add optional
configuration settings to change replica ownership to the AWS account that owns the
destination buckets.

To change the replica owner, you do the following:

- Add the _owner override_ option to the replication
  configuration to tell Amazon S3 to change replica ownership.
- Grant Amazon S3 the `s3:ObjectOwnerOverrideToBucketOwner` permission to
  change replica ownership.
- Add the `s3:ObjectOwnerOverrideToBucketOwner` permission in the
  destination bucket policy to allow changing replica ownership. The
  `s3:ObjectOwnerOverrideToBucketOwner` permission allows the owner of
  the destination buckets to accept the ownership of object replicas.
  For more information, see [Considerations for the ownership
  override option](#repl-ownership-considerations "#repl-ownership-considerations") and [Adding the owner override option
  to the replication configuration](#repl-ownership-owneroverride-option "#repl-ownership-owneroverride-option"). For a working example with
  step-by-step instructions, see [How to change the replica owner](#replication-walkthrough-3 "#replication-walkthrough-3").

###### Important

Instead of using the owner override option, you can use the bucket owner enforced
setting for Object Ownership. When you use replication and the source and destination
buckets are owned by different AWS accounts, the bucket owner of the destination
bucket can use the bucket owner enforced setting for Object Ownership to change replica
ownership to the AWS account that owns the destination bucket. This setting disables
object access control lists (ACLs).

The bucket owner enforced setting mimics the existing owner override behavior without
the need of the `s3:ObjectOwnerOverrideToBucketOwner` permission. All objects
that are replicated to the destination bucket with the bucket owner enforced setting are
owned by the destination bucket owner. For more information about Object Ownership, see
[Controlling ownership of objects and disabling ACLs
for your bucket](about-object-ownership.md "about-object-ownership.md").

## Considerations for the ownership

override option

When you configure the ownership override option, the following considerations
apply:

- By default, the owner of the source object also owns the replica. Amazon S3
  replicates the object version and the ACL associated with it.

If you add the owner override option to your replication configuration, Amazon S3
replicates only the object version, not the ACL. In addition, Amazon S3 doesn't
replicate subsequent changes to the source object ACL. Amazon S3 sets the ACL on the
replica that grants full control to the destination bucket owner.

- When you update a replication configuration to enable or disable the owner
  override, the following behavior occurs:
  - If you add the owner override option to the replication
    configuration:

  When Amazon S3 replicates an object version, it discards the ACL that's
  associated with the source object. Instead, Amazon S3 sets the ACL on the
  replica, giving full control to the owner of the destination bucket.
  Amazon S3 doesn't replicate subsequent changes to the source object ACL.
  However, this ACL change doesn't apply to object versions that were
  replicated before you set the owner override option. ACL updates on
  source objects that were replicated before the owner override was set
  continue to be replicated (because the object and its replicas continue
  to have the same owner).
  - If you remove the owner override option from the replication
    configuration:

  Amazon S3 replicates new objects that appear in the source bucket and the
  associated ACLs to the destination buckets. For objects that were
  replicated before you removed the owner override, Amazon S3 doesn't replicate
  the ACLs because the object ownership change that Amazon S3 made remains in
  effect. That is, ACLs put on the object version that were replicated
  when the owner override was set continue to be not replicated.

## Adding the owner override option

to the replication configuration

###### Warning

Add the owner override option only when the source and destination buckets are
owned by different AWS accounts. Amazon S3 doesn't check if the buckets are owned by
the same or different accounts. If you add the owner override when both buckets are
owned by same AWS account, Amazon S3 applies the owner override. This option grants
full permissions to the owner of the destination bucket and doesn't replicate
subsequent updates to the source objects' access control lists (ACLs). The replica
owner can directly change the ACL associated with a replica with a
`PutObjectAcl` request, but not through replication.

To specify the owner override option, add the following to each
`Destination` element:

- The `AccessControlTranslation` element, which tells Amazon S3 to change
  replica ownership
- The `Account` element, which specifies the AWS account of the
  destination bucket owner

```
<ReplicationConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    ...
    <Destination>
      ...
      **<AccessControlTranslation>
 <Owner>Destination</Owner>
 </AccessControlTranslation>
 <Account>`destination-bucket-owner-account-id`</Account>**
    </Destination>
  </Rule>
</ReplicationConfiguration>
```

The following example replication configuration tells Amazon S3 to replicate objects that
have the `Tax` key prefix to the
`amzn-s3-demo-destination-bucket` destination bucket and change ownership
of the replicas. To use this example, replace the `user input
 placeholders` with your own information.

```
<?xml version="1.0" encoding="UTF-8"?>
<ReplicationConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Role>arn:aws:iam::`account-id`:role/`role-name`</Role>
   <Rule>
      <ID>`Rule-1`</ID>
      <Priority>`1`</Priority>
      <Status>Enabled</Status>
      <DeleteMarkerReplication>
         <Status>`Disabled`</Status>
      </DeleteMarkerReplication>
      <Filter>
         <Prefix>`Tax`</Prefix>
      </Filter>
      <Destination>
         <Bucket>arn:aws:s3:::`amzn-s3-demo-destination-bucket`</Bucket>
         <Account>`destination-bucket-owner-account-id`</Account>
         <AccessControlTranslation>
            <Owner>Destination</Owner>
         </AccessControlTranslation>
      </Destination>
   </Rule>
</ReplicationConfiguration>
```

## Granting Amazon S3 permission to change

replica ownership

Grant Amazon S3 permissions to change replica ownership by adding permission for the
`s3:ObjectOwnerOverrideToBucketOwner` action in the permissions policy
that's associated with the AWS Identity and Access Management (IAM) role. This role is the IAM role that you
specified in the replication configuration that allows Amazon S3 to assume and replicate
objects on your behalf. To use the following example, replace
`amzn-s3-demo-destination-bucket` with the name of the destination bucket.

```
...
{
    "Effect":"Allow",
         "Action":[
       "s3:ObjectOwnerOverrideToBucketOwner"
    ],
    "Resource":"arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
}
...
```

## Adding permission in the

destination bucket policy to allow changing replica ownership

The owner of the destination bucket must grant the owner of the source bucket
permission to change replica ownership. The owner of the destination bucket grants the
owner of the source bucket permission for the
`s3:ObjectOwnerOverrideToBucketOwner` action. This permission allows the
destination bucket owner to accept ownership of the object replicas. The following
example bucket policy statement shows how to do this. To use this example, replace the
`user input placeholders` with your own
information.

```
...
{
    "Sid":"1",
    "Effect":"Allow",
    "Principal":{"AWS":"`source-bucket-account-id`"},
    "Action":["s3:ObjectOwnerOverrideToBucketOwner"],
    "Resource":"arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
}
...
```

## How to change the replica owner

When the source and destination buckets in a replication configuration are owned by
different AWS accounts, you can tell Amazon S3 to change replica ownership to the AWS account
that owns the destination bucket. The following examples show how to use the Amazon S3 console,
the AWS Command Line Interface (AWS CLI), and the AWS SDKs to change replica ownership.

For step-by-step instructions, see [Configuring replication for buckets in the same
account](replication-walkthrough1.md "replication-walkthrough1.md"). This topic provides instructions for
setting up a replication configuration when the source and destination buckets are
owned by the same and different AWS accounts.

The following procedure shows how to change replica ownership by using the AWS CLI.
In this procedure, you do the following:

- Create the source and destination buckets.
- Enable versioning on the buckets.
- Create an AWS Identity and Access Management (IAM) role that gives Amazon S3 permission to replicate
  objects.
- Add the replication configuration to the source bucket.
- In the replication configuration, you direct Amazon S3 to change the replica
  ownership.
- You test your replication configuration.

###### To change replica ownership when the source and destination buckets are owned

by different AWS accounts (AWS CLI)

To use the example AWS CLI commands in this procedure, replace the
`user input placeholders` with
your own information.

1. In this example, you create the source and destination buckets in two
   different AWS accounts. To work with these two accounts, configure the
   AWS CLI with two named profiles. This example uses profiles named
   `acctA` and
   `acctB`, respectively. For
   information about setting credential profiles and using named profiles, see
   [Configuration and
   credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface User Guide_.

###### Important

The profiles that you use for this procedure must have the necessary
permissions. For example, in the replication configuration, you specify
the IAM role that Amazon S3 can assume. You can do this only if the profile
that you use has the `iam:PassRole` permission. If you use
administrator user credentials to create a named profile, then you can
perform all of the tasks in this procedure. For more information, see
[Granting a
user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the
_IAM User Guide_. 2. Create the source bucket and enable versioning. This example creates a
source bucket named `amzn-s3-demo-source-bucket` in the
US East (N. Virginia) (`us-east-1`) Region.

```
aws s3api create-bucket \
--bucket `amzn-s3-demo-source-bucket` \
--region `us-east-1` \
--profile `acctA`
```

```
aws s3api put-bucket-versioning \
--bucket `amzn-s3-demo-source-bucket` \
--versioning-configuration Status=Enabled \
--profile `acctA`
```

3. Create a destination bucket and enable versioning. This example creates a
   destination bucket named `amzn-s3-demo-destination-bucket` in the
   US West (Oregon) (`us-west-2`) Region. Use an AWS account
   profile that's different from the one that you used for the source
   bucket.

```
aws s3api create-bucket \
--bucket `amzn-s3-demo-destination-bucket` \
--region `us-west-2` \
--create-bucket-configuration LocationConstraint=`us-west-2` \
--profile `acctB`
```

```
aws s3api put-bucket-versioning \
--bucket `amzn-s3-demo-destination-bucket` \
--versioning-configuration Status=Enabled \
--profile `acctB`
```

4. You must add permissions to your destination bucket policy to allow
   changing the replica ownership.
   1. Save the following policy to a file named
      ``destination-bucket-policy`.json`.
Make sure to replace the ``user input
      placeholders`` with your own
      information.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "`destination_bucket_policy_sid`",
    "Principal": {
    "AWS": "`source-bucket-owner-123456789012`"
    },
    "Action": [
    "s3:ReplicateObject",
    "s3:ReplicateDelete",
    "s3:ObjectOwnerOverrideToBucketOwner",
    "s3:ReplicateTags",
    "s3:GetObjectVersionTagging"
    ],
    "Effect": "Allow",
    "Resource": [
    "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
    ]
    }
    ]
   }`

   ```

   2. Add the preceding policy to the destination bucket by using the
      following `put-bucket-policy` command:

   ```
   aws s3api put-bucket-policy --region `$` {`destination-region`} --bucket `$` {`amzn-s3-demo-destination-bucket`} --policy file://`destination_bucket_policy`.json
   ```

5. Create an IAM role. You specify this role in the replication
   configuration that you add to the source bucket later. Amazon S3 assumes this
   role to replicate objects on your behalf. You create an IAM role in two
   steps:
   - Create the role.
   - Attach a permissions policy to the role.
   1. Create the IAM role.
      1. Copy the following trust policy and save it to a file
         named
         ``s3-role-trust-policy`.json`
         in the current directory on your local computer. This policy
         grants Amazon S3 permissions to assume the role.

      JSON

      ```
      `{
       "Version":"2012-10-17",
       "Statement":[
       {
       "Effect":"Allow",
       "Principal":{
       "Service":"s3.amazonaws.com"
       },
       "Action":"sts:AssumeRole"
       }
       ]
      }`

      ```

      2. Run the following AWS CLI `create-role` command
         to create the IAM role:

      ```
      `$` aws iam create-role \
      --role-name `replicationRole` \
      --assume-role-policy-document file://`s3-role-trust-policy`.json  \
      --profile `acctA`
      ```

      Make note of the Amazon Resource Name (ARN) of the IAM
      role that you created. You will need this ARN in a later
      step.

   2. Attach a permissions policy to the role.
      1. Copy the following permissions policy and save it to a
         file named
         ``s3-role-perm-pol-changeowner`.json`
         in the current directory on your local computer. This policy
         grants permissions for various Amazon S3 bucket and object
         actions. In the following steps, you attach this policy to
         the IAM role that you created earlier.

      JSON

      ```
      `{
       "Version":"2012-10-17",
       "Statement":[
       {
       "Effect":"Allow",
       "Action":[
       "s3:GetObjectVersionForReplication",
       "s3:GetObjectVersionAcl"
       ],
       "Resource":[
       "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
       ]
       },
       {
       "Effect":"Allow",
       "Action":[
       "s3:ListBucket",
       "s3:GetReplicationConfiguration"
       ],
       "Resource":[
       "arn:aws:s3:::amzn-s3-demo-source-bucket"
       ]
       },
       {
       "Effect":"Allow",
       "Action":[
       "s3:ReplicateObject",
       "s3:ReplicateDelete",
       "s3:ObjectOwnerOverrideToBucketOwner",
       "s3:ReplicateTags",
       "s3:GetObjectVersionTagging"
       ],
       "Resource":"arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
       }
       ]
      }`

      ```

      2. To attach the preceding permissions policy to the role,
         run the following `put-role-policy`
         command:

      ```
      `$` aws iam put-role-policy \
      --role-name `replicationRole` \
      --policy-document file://`s3-role-perm-pol-changeowner`.json \
      --policy-name `replicationRolechangeownerPolicy` \
      --profile `acctA`
      ```

6. Add a replication configuration to your source bucket.
   1. The AWS CLI requires specifying the replication configuration as
      JSON. Save the following JSON in a file named
      ``replication`.json`in the current directory on your local computer. In the
configuration, the`AccessControlTranslation` specifies
      the change in replica ownership from the source bucket owner to the
      destination bucket owner.

   ```
   {
      "Role":"`IAM-role-ARN`",
      "Rules":[
         {
            "Status":"Enabled",
            "Priority":1,
            "DeleteMarkerReplication":{
               "Status":"Disabled"
            },
            "Filter":{
            },
            "Status":"Enabled",
            "Destination":{
               "Bucket":"arn:aws:s3:::`amzn-s3-demo-destination-bucket`",
               "Account":"`destination-bucket-owner-account-id`",
               "AccessControlTranslation":{
                  "Owner":"Destination"
               }
            }
         }
      ]
   }
   ```

   2. Edit the JSON by providing values for the destination bucket name,
      the destination bucket owner account ID, and the
      `IAM-role-ARN`.
      Replace `IAM-role-ARN` with
      the ARN of the IAM role that you created earlier. Save the
      changes.
   3. To add the replication configuration to the source bucket, run the
      following command:

   ```
   `$` aws s3api put-bucket-replication \
   --replication-configuration file://`replication`.json \
   --bucket `amzn-s3-demo-source-bucket` \
   --profile `acctA`
   ```

7. Test your replication configuration by checking replica ownership in the
   Amazon S3 console.
   1. Sign in to the AWS Management Console and open the Amazon S3 console at
      [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
   2. Add objects to the source bucket. Verify that the destination
      bucket contains the object replicas and that the ownership of the
      replicas has changed to the AWS account that owns the destination
      bucket.
      For a code example to add a replication configuration, see [Using the AWS SDKs](replication-walkthrough1.md#replication-ex1-sdk "replication-walkthrough1.md#replication-ex1-sdk"). You must
      modify the replication configuration appropriately. For conceptual information, see
      [Changing the replica owner](replication-change-owner.md "replication-change-owner.md").
