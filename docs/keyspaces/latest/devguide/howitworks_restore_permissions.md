# Configure restore table IAM permissions for Amazon Keyspaces PITR

This section summarizes how to configure permissions for
an AWS Identity and Access Management (IAM) principal to restore Amazon Keyspaces tables. In IAM, the
AWS managed policy `AmazonKeyspacesFullAccess` includes the permissions to restore
Amazon Keyspaces tables. To implement a custom policy with minimum required permissions, consider the requirements outlined in the next section.

To successfully restore a table, the IAM principal needs the following minimum permissions:

- `cassandra:Restore` – The restore action is required for the target table to be restored.
- `cassandra:Select` – The select action is required to read from the source table.
- `cassandra:TagResource` – The tag action is optional, and only required if the restore operation adds tags.
  This is an example of a policy that grants minimum required permissions to a user to restore tables in keyspace `mykeyspace`.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Restore",
            "cassandra:Select"
         ],
         "Resource":[
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/*",
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      }
   ]
}
```

Additional permissions to restore a table might be required based on other selected
features. For example, if the source table is encrypted at rest with a customer managed
key, Amazon Keyspaces must have permissions to access the
customer managed key of the source table to successfully restore the table. For more information, see [PITR restore of encrypted tables](PointInTimeRecovery_HowItWorks.md#howitworks_backup_encryption "PointInTimeRecovery_HowItWorks.md#howitworks_backup_encryption").

If you are using IAM policies with [condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") to
restrict incoming traffic to specific sources, you must ensure that Amazon Keyspaces has permission to perform a restore operation on your principal's behalf.
You must add an `aws:ViaAWSService` condition key to your IAM policy if your policy restricts incoming traffic to any of the following:

- VPC endpoints with `aws:SourceVpce`
- IP ranges with `aws:SourceIp`
- VPCs with `aws:SourceVpc`
  The `aws:ViaAWSService` condition key allows access when any
  AWS service makes a request using the principal's credentials. For more information,
  see [IAM JSON policy
  elements: Condition key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

The following is an example of a policy that restricts source traffic to a specific IP address and allows Amazon Keyspaces to restore a table on the principal's behalf.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"CassandraAccessForCustomIp",
         "Effect":"Allow",
         "Action":"cassandra:*",
         "Resource":"*",
         "Condition":{
            "Bool":{
               "aws:ViaAWSService":"false"
            },
            "ForAnyValue:IpAddress":{
               "aws:SourceIp":[
                  "123.45.167.89"
               ]
            }
         }
      },
      {
         "Sid":"CassandraAccessForAwsService",
         "Effect":"Allow",
         "Action":"cassandra:*",
         "Resource":"*",
         "Condition":{
            "Bool":{
               "aws:ViaAWSService":"true"
            }
         }
      }
   ]
}
```

For
an example policy using the `aws:ViaAWSService` global condition key, see [VPC endpoint policies and Amazon Keyspaces point-in-time
recovery (PITR)](vpc-endpoints.md#VPC_PITR_restore "vpc-endpoints.md#VPC_PITR_restore").
