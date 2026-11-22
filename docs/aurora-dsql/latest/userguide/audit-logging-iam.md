

# Configuring permissions

Audit logging requires the following permissions:
+ **Caller permissions** – To set up audit log delivery, your IAM identity needs permission to set up log delivery for the cluster, create the CloudWatch Logs delivery resources, and update the policy of your Amazon S3 bucket.
+ **Audit administration roles** – The database role that changes audit settings must be `admin` or a member of `pg_dsql_audit_admin`.
+ **Key policy** – If your cluster uses a customer managed AWS KMS key, the key policy must allow Aurora DSQL and CloudWatch Logs to use the key for audit records. For the statements to add, see [Key management](#audit-logging-key-management).

## Caller permissions
<a name="audit-logging-permissions"></a>

The IAM identity that sets up audit log delivery for a cluster needs permissions on the cluster, the CloudWatch Logs delivery resources, and the Amazon S3 bucket.

For more information about the CloudWatch Logs and Amazon S3 permissions, including an example policy, see [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html) in the *Amazon CloudWatch Logs User Guide*.

### Aurora DSQL cluster
<a name="audit-logging-permissions-cluster"></a>


| Permission | Needed to | 
| --- |--- |
| dsql:AllowVendedLogDeliveryForResource | Set up delivery. This permission-only action doesn't correspond to an API operation that you call. To grant it on all clusters, use \*. | 

The [AmazonAuroraDSQLFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLFullAccess) and [AmazonAuroraDSQLConsoleFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLConsoleFullAccess) managed policies include `dsql:AllowVendedLogDeliveryForResource`. These policies don't include the CloudWatch Logs and Amazon S3 permissions, so add them separately. If your cluster has a resource-based policy, make sure that the policy doesn't deny this action to the identity.

### CloudWatch Logs delivery source, delivery destination, and delivery
<a name="audit-logging-permissions-delivery"></a>


| Permissions | Needed to | 
| --- |--- |
| `logs:PutDeliverySource`<br />`logs:PutDeliveryDestination`<br />`logs:CreateDelivery` | Set up delivery. | 
| logs:UpdateDeliveryConfiguration | Change a delivery. | 
| `logs:DescribeDeliveries`<br />`logs:DeleteDelivery`<br />`logs:DeleteDeliverySource`<br />`logs:DeleteDeliveryDestination` | List and delete the delivery resources. | 

### Amazon S3 bucket
<a name="audit-logging-permissions-bucket"></a>


| Permissions | Needed to | 
| --- |--- |
| `s3:GetBucketPolicy`<br />`s3:PutBucketPolicy` | Set up delivery. CloudWatch Logs uses these permissions to add a statement to the bucket policy that lets it write audit records to the bucket. | 
| `s3:ListBucket`<br />`s3:GetObject` | List and read the audit log files. Grant s3:GetObject on the objects in the bucket. | 

## Audit administration roles
<a name="audit-logging-roles"></a>

Only database roles with audit administration privileges can change audit settings. By default, the built-in `admin` role has these privileges. If your compliance requirements call for separation of duties, give audit administration to a dedicated role. You can then let your database administrators manage the database without the ability to change audit settings.

The following table describes the built-in roles for audit administration.


| Role | Description | 
| --- |--- |
| admin | The built-in administrator role. It can change audit settings, and it can grant pg\_dsql\_audit\_admin and pg\_dsql\_admin to other roles. You connect as admin with an IAM identity that has the dsql:DbConnectAdmin permission. | 
| pg\_dsql\_audit\_admin | Grants audit administration privileges. Members can change audit settings with sys.set\_audit\_config and sys.reset\_audit\_config. | 
| pg\_dsql\_admin | Grants the database administration privileges of admin, without audit administration privileges. Members can't change audit settings or grant pg\_dsql\_audit\_admin to other roles. | 

**Note**  
You can't connect as `pg_dsql_audit_admin` or `pg_dsql_admin`. To use one of these roles, grant it to a database role that you create, and connect with that role.

The following example creates an audit administrator role and a database administrator role. It maps each role to a different IAM role. In the following SQL statements, replace {{audit\_admin}} and {{db\_admin}} with the names of the roles to create, {{111122223333}} with your AWS account ID, and {{AuditTeam}} and {{DbaTeam}} with the names of your IAM roles.

**Create an audit administrator role**  
Connect to your cluster as `admin`, and run the following SQL statements. The statements create the role, grant it `pg_dsql_audit_admin`, and map it to the IAM role of your audit team:

```sql
CREATE ROLE {{audit_admin}} WITH LOGIN;
GRANT pg_dsql_audit_admin TO {{audit_admin}};
AWS IAM GRANT {{audit_admin}} TO 'arn:aws:iam::{{111122223333}}:role/{{AuditTeam}}';
```

**Create a database administrator role**  
Run the following SQL statements. The statements create the role with the `CREATEROLE` attribute so that it can manage other roles. They also grant it `pg_dsql_admin`, and map it to the IAM role of your database administrators:

```sql
CREATE ROLE {{db_admin}} WITH LOGIN CREATEROLE;
GRANT pg_dsql_admin TO {{db_admin}};
AWS IAM GRANT {{db_admin}} TO 'arn:aws:iam::{{111122223333}}:role/{{DbaTeam}}';
```

**Update the IAM policies**  
Allow the `dsql:DbConnect` action in the IAM policies of the {{AuditTeam}} and {{DbaTeam}} roles. Then remove the `dsql:DbConnectAdmin` permission from IAM identities that don't need to connect as `admin`.

**Connect with the new roles**  
To connect as {{audit\_admin}} or {{db\_admin}}, generate an authentication token with `generate-db-connect-auth-token`, not `generate-db-connect-admin-auth-token`. For more information about authentication tokens, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md). If the connection fails with an access denied error, make sure that the policy of the IAM role allows `dsql:DbConnect` on the cluster.

**Warning**  
Any IAM identity that can connect as `admin` can change audit settings. Keep the `dsql:DbConnectAdmin` permission only for the identities that need it, and use CloudTrail to monitor connections as `admin`.

A role with the `CREATEROLE` attribute can create new roles. A new role has no audit settings. Aurora DSQL doesn't audit its statements until an audit administrator sets audit settings for it. To record when someone creates a role or maps it to an IAM identity, include the `role` class in the audit settings of the roles that have the `CREATEROLE` attribute.

## Data protection
<a name="audit-logging-data-protection"></a>

Aurora DSQL protects audit records from the time that it generates them until CloudWatch Logs delivers them to your bucket. After delivery, the encryption settings of your bucket protect the records. The following sections describe encryption at rest, encryption in transit, and key management for audit records. For a detailed explanation of encryption in Aurora DSQL, see [Data encryption for Amazon Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/data-encryption.html) in this guide.

**Important**  
The `statement_text` and `parameters` fields of audit records can contain sensitive data, such as literal values in SQL statements. If your SQL statements can contain sensitive data, we recommend that you use a customer managed key for your cluster. With a customer managed key, Aurora DSQL encrypts these fields with your key before it delivers the records. If your cluster uses an AWS owned key, Aurora DSQL doesn't encrypt these fields with a key that you control. Until CloudWatch Logs delivers the records to your bucket, they are protected by TLS in transit and by encryption at rest with keys that AWS owns and manages. For more information, see [Encryption in transit](#audit-logging-encryption-in-transit).

### Encryption at rest
<a name="audit-logging-encryption-at-rest"></a>

In your bucket, the encryption settings of the bucket protect audit records. If the bucket uses server-side encryption with AWS KMS keys (SSE-KMS), the policy of the bucket's key must also allow log delivery. For more information about bucket encryption for log delivery, see [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html) in the *Amazon CloudWatch Logs User Guide*.

### Encryption in transit
<a name="audit-logging-encryption-in-transit"></a>

Aurora DSQL and CloudWatch Logs use Transport Layer Security (TLS) to encrypt audit records in transit. If your cluster uses a customer managed key, Aurora DSQL also encrypts the `statement_text` and `parameters` fields of each audit record with that key. CloudWatch Logs decrypts these fields when it delivers the records to your bucket. For more information about the key policy statements that this requires, see [Key management](#audit-logging-key-management).

### Key management
<a name="audit-logging-key-management"></a>

If your cluster uses a customer managed AWS KMS key, add the following statements to the key policy. Replace {{region}} with the AWS Region of the cluster, and replace {{111122223333}} with your AWS account ID:

```json
{
  "Sid": "AllowAuroraDsqlToProtectAuditLogFields",
  "Effect": "Allow",
  "Principal": {
    "Service": "dsql.amazonaws.com"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "ArnLike": {
      "kms:EncryptionContext:SourceArn": "arn:aws:logs:{{region}}:{{111122223333}}:*"
    }
  }
},
{
  "Sid": "AllowLogDeliveryToReadAuditLogFields",
  "Effect": "Allow",
  "Principal": {
    "Service": "delivery.logs.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
    "ArnLike": {
      "kms:EncryptionContext:SourceArn": "arn:aws:logs:{{region}}:{{111122223333}}:*"
    }
  }
}
```

The statements provide the following permissions and protections:
+ `AllowAuroraDsqlToProtectAuditLogFields` – Allows Aurora DSQL to use the key to encrypt the `statement_text` and `parameters` fields.
+ `AllowLogDeliveryToReadAuditLogFields` – Allows CloudWatch Logs to use the key to decrypt these fields when it delivers the records to your bucket.
+ `kms:EncryptionContext:SourceArn` – Restricts key usage in both statements to requests whose encryption context refers to CloudWatch Logs resources in your AWS account and Region. This condition helps prevent the confused deputy problem. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md).

Aurora DSQL delivers the cluster's audit records only when the key policy includes these statements and the key is enabled. For more information about customer managed keys for Aurora DSQL, see [Key policy for a customer managed key](data-encryption.md#key-policy-customer-managed-key).

**Note**  
The key in these statements is the customer managed key of the cluster, not the key that encrypts your Amazon S3 bucket. For information about the bucket key, see [Encryption at rest](#audit-logging-encryption-at-rest).