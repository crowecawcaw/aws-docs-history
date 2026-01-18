# Troubleshooting

This section helps you diagnose and resolve common issues with AWS Backint Agent for SAP ASE.
You’ll find information about logging locations, performance optimization techniques, and solutions to frequently encountered problems.

###### Topics

- [Prerequisites](#_prerequisites "#_prerequisites")
- [Logging](#ase-backint-logging "#ase-backint-logging")
- [Performance](#_performance "#_performance")
- [Common Issues and Solutions](#_common_issues_and_solutions "#_common_issues_and_solutions")
- [Best Practices](#_best_practices "#_best_practices")
- [Getting Help](#_getting_help "#_getting_help")

## Prerequisites

Before troubleshooting, ensure you have:

- AWS Backint Agent for ASE properly installed and configured
- Valid AWS credentials with appropriate permissions
- Access to AWS CloudTrail logs for permission debugging
- SAP ASE database administrator privileges

## Logging

Log files are located at the following locations.
To get help with issues, submit all log files to AWS Support through the AWS Support Center.

| Log Type           | Location                                                                      |
| ------------------ | ----------------------------------------------------------------------------- |
| Installation logs  | `install_aws_backint_YYYYMMDD_HHMMSS.log` in the current working directory    |
| Backint Agent logs | `/sybase/shared/aws-backint-agent-ase/logs/aws-backint-agent.log`             |
| Archive API logs   | `/sybase/shared/aws-backint-agent-ase/logs/aws-backint-agent-archive-api.log` |
| Backup Server log  | `<install_dir>/ASE-16_<minor_version>/install/<server_name>_BS.log`           |
| Database log       | `<install_dir>/ASE-16_<minor_version>/install/<server_name>.log`              |

### Enable Detailed Logging

1. Configure the Backint Agent for verbose logging
2. Monitor AWS CloudTrail for API call failures
3. Check SAP ASE error logs for database-specific issues

### Key AWS Log Locations

- AWS CloudTrail: AWS Management Console > CloudTrail

## Performance

This section contains information on common measures for optimizing performance of AWS Backint Agent for SAP ASE.

### Striping

Striping allows adjusting the number of simultaneous backup and restore streams to and from Amazon S3.
The optimal number of stripes depends on a variety of factors, such as database size, network, and Amazon EC2 instance type.
Three (3) to four (4) stripes are a reasonable choice for most database sizes.
For more information on striping, refer to [Backup Striping](ase-backint-dump-load.md#ase-backint-backup-striping "ase-backint-dump-load.md#ase-backint-backup-striping").

### Main Memory Consumption During LOAD Operations

Main memory consumption of AWS Backint Agent for SAP ASE typically ranges between 10 and 20 GiB during LOAD operations.
In case you experience significantly higher values, consider setting the following parameters in `/sybase/shared/aws-backint-agent-ase/aws-backint-agent-config.yaml`.

Lower values reduce memory consumption but may increase LOAD operation time.
The default values are shown below:

| Parameter                  | Value |
| -------------------------- | ----- |
| downloadConcurrencyDefault | 10    |
| downloadChannelSizeDefault | 5     |

## Common Issues and Solutions

This section covers common issues you may encounter while using AWS Backint Agent for SAP ASE.

### Install custom version

By default, the installer automatically downloads the latest available version of AWS Backint Agent for SAP ASE.
In case you need to install a specific version of the RPM, you can download the RPM package of any previous version from S3 and provide the RPM package to the installer.

```
 # Download installer
wget https://s3.amazonaws.com/awssap-backint-agent-ase/binary/<version>/install-aws-backint-agent-ase
# Download RPM package
wget https://s3.amazonaws.com/awssap-backint-agent-ase/binary/<version>/aws-backint-agent-ase.rpm
# Add execute permission to installer
chmod +x install-aws-backint-agent-ase
# Run installer
./install-aws-backint-agent-ase --location aws-backint-agent-ase.rpm
```

### S3 Permission Issues

#### S3 Access Denied During Backup Operations

**Problem**: Backup fails with `AccessDenied` error when attempting to write to S3 bucket.

**Symptoms**:

```
 Error creating upload id for bucket:<bucket-name> key:<object-key>
error:AccessDenied: User: arn:aws:sts::<account-id>:assumed-role/<role-name>/<instance-id>
is not authorized to perform: s3:PutObject on resource: "arn:aws:s3:::<bucket-name>/<object-path>"
because no identity-based policy allows the s3:PutObject action
```

**Root Cause**: The IAM role or user lacks the required S3 permissions for the specified bucket path.

**Solution**:

1. Verify the S3 bucket policy includes the correct resource path:

```
 {
  "Effect": "Allow",
  "Action": [
    "s3:PutObjectTagging",
    "s3:PutObject",
    "s3:GetObject",
    "s3:DeleteObject"
  ],
  "Resource": [
    "arn:aws:s3:::your-bucket-name/your-folder-name/*"
  ]
}
```

2. Ensure the resource path in your IAM policy matches the actual S3 prefix used by the Backint Agent.
3. Test permissions using AWS CLI:

```
 aws s3 cp test-file.txt s3://your-bucket-name/your-folder-name/
```

**Time to Resolution**: Typically 2-5 minutes once the correct path is identified.

#### S3 ListBucket Permission Denied During Restore

**Problem**: Database restore fails when the Backint Agent cannot list S3 bucket contents.

**Symptoms**:

```
 ListObjects error: User: arn:aws:sts::<account-id>:assumed-role/<role-name>/<instance-id>
is not authorized to perform: s3:ListBucket on resource: "arn:aws:s3:::<bucket-name>"
because no identity-based policy allows the s3:ListBucket action
```

**Root Cause**: Missing `s3:ListBucket` permission in the IAM policy.

**Solution**:

1. Add the `s3:ListBucket` permission to your IAM policy:

```
 {
  "Effect": "Allow",
  "Action": [
    "s3:ListBucket"
  ],
  "Resource": [
    "arn:aws:s3:::your-bucket-name"
  ]
}
```

#### S3 GetObject Permission Denied During Restore

**Problem**: Restore operation fails when attempting to download backup files from S3.

**Symptoms**:

```
 Key metadata fetch failed for bucket:<bucket-name> key:<object-key>
error:Forbidden: Forbidden
status code: 403
```

**Root Cause**: The IAM role lacks `s3:GetObject` permission for the backup files.

**Solution**:

1. Ensure your IAM policy includes `s3:GetObject` permission:

```
 {
  "Effect": "Allow",
  "Action": [
    "s3:GetObject"
  ],
  "Resource": [
    "arn:aws:s3:::your-bucket-name/your-folder-name/*"
  ]
}
```

2. Verify the object exists and the path is correct using AWS CLI:

```
 aws s3 ls s3://your-bucket-name/your-folder-name/
```

### Backup and Restore Configuration Issues

#### Stripe Count Mismatch During Restore

**Problem**: Restore fails due to mismatch between backup and restore stripe configuration.

**Symptoms**:

```
 Error: Mismatch stripe count, load requested with: 2 stripes instead of 1
```

**Root Cause**: The restore command specifies a different number of stripes than used during backup.

**Solution**:

1. Check the original backup configuration to determine the correct stripe count.
2. Use the same stripe count for restore as was used for backup:

```
 -- For single stripe backup
LOAD DATABASE your_db FROM "awsbackint::backup_prefix"

-- For multi-stripe backup
LOAD DATABASE your_db FROM "awsbackint::backup_prefix"
STRIPE ON "awsbackint::backup_prefix"
```

3. If unsure about the original stripe count, check the S3 bucket structure to count the stripe files.

#### Named Pipe Creation Failure

**Problem**: Backup fails when attempting to reuse the same prefix after a previous failed attempt.

**Symptoms**:

```
 Error creating named pipe for stripe 0: File exists
```

**Root Cause**: Previous backup attempt left temporary files that weren’t cleaned up.

**Solution**:

1. **Immediate workaround**: Use a different backup prefix:

```
 DUMP DATABASE your_db TO "awsbackint::new_unique_prefix"
```

2. **Long-term solution**: Clean up temporary files from the previous attempt:

```
 # Remove temporary pipes and files from the Backint Agent working directory
rm -f /sybase/shared/aws-backint-ase/pipes/<database>/<prefix>
```

3. **Best practice**: Always use unique prefixes for each backup operation.

### Configuration File Issues

#### Configuration File Permission Errors

**Problem**: Backint Agent fails to start due to incorrect file permissions on the configuration file.

**Symptoms**:

```
 Error reading config file Failed to validate config file permission,
other users outside of group cannot have execution permission.
```

**Root Cause**: The configuration file has overly permissive file permissions.

**Solution**:

1. Set correct permissions on the configuration file:

```
 chmod 640 /sybase/shared/aws-backint-agent-ase/aws-backint-agent-config.yaml
```

2. Ensure the file is owned by the correct user and group:

```
 chown sap_user:sap_group /sybase/shared/aws-backint-agent-ase/aws-backint-agent-config.yaml
```

3. Verify permissions:

```
 ls -la /sybase/shared/aws-backint-agent-ase/aws-backint-agent-config.yaml
```

#### Missing S3 Bucket Configuration

**Problem**: Backint Agent fails to start due to missing or incorrect S3 bucket configuration.

**Symptoms**:

```
 Error: S3 Bucket Name not found in aws-backint-agent-config.yaml
```

**Root Cause**: The configuration file is missing the S3 bucket name or has incorrect permissions.

**Solution**:

1. Verify the S3 bucket name is correctly specified in the configuration file.
2. Ensure the configuration file has proper read permissions.
3. Check that the IAM role has access to the specified S3 bucket.

### KMS Encryption Issues

#### KMS Key Type Mismatch

**Problem**: Backup fails when using an asymmetric KMS key for S3 encryption.

**Symptoms**:

```
 KMS.InvalidKeyUsageException: You cannot generate a data key with an asymmetric CMK
```

**Root Cause**: S3 server-side encryption requires a symmetric KMS key, but an asymmetric key was specified.

**Solution**:

1. Use a symmetric KMS key for S3 encryption.
2. Create a new symmetric key if needed:

```
 aws kms create-key --description "S3 encryption key for SAP backups" --key-usage ENCRYPT_DECRYPT
```

3. Update your S3 bucket configuration or Backint Agent configuration to use the symmetric key.

#### KMS Permission Denied

**Problem**: Backup fails due to insufficient KMS permissions.

**Symptoms**:

```
 AccessDenied: User: arn:aws:sts::<account-id>:assumed-role/<role-name>/<instance-id>
is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:kms:<region>:<account-id>:key/<key-id>
with an explicit deny in an identity-based policy
```

**Root Cause**: The IAM role lacks the required KMS permissions.

**Solution**:

1. Add KMS permissions to your IAM policy:

```
 {
  "Effect": "Allow",
  "Action": [
    "kms:GenerateDataKey",
    "kms:Decrypt"
  ],
  "Resource": [
    "arn:aws:kms:region:account-id:key/key-id"
  ]
}
```

2. Ensure there are no explicit deny policies blocking KMS access.
3. Test KMS access:

```
 aws kms generate-data-key --key-id your-key-id --key-spec AES_256
```

## Best Practices

### Backup Naming Convention

- Use consistent and descriptive prefixes
- Include timestamp information for easy identification
- Avoid special characters that might cause parsing issues

### S3 Path Structure

The Backint Agent creates the following S3 path structure:

```
 <bucket-name>/<path-prefix>/<SID>/sapci_<Database_Name>_COMPLETE_<custom_prefix>_<stripe_number>/<date>_<time>/
```

### Restore Command Format

When restoring, use the exact path format:

```
 LOAD DATABASE <DB_NAME> FROM "awsbackint::<backup_location_without_database_prefix>"
```

###### Note

Do not include the database name as a prefix in the restore path.

### IAM Policy Template

Use this comprehensive IAM policy template for the Backint Agent:

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name/*",
                "arn:aws:s3:::your-bucket-name"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:123456789012:key/your-kms-key-id"
        },
          {
              "Effect": "Allow",
              "Action": [
                  "s3:PutObjectTagging",
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:DeleteObject"
              ],
              "Resource": "arn:aws:s3:::your-bucket-name/your-folder-name/*"
          }
    ]
}
```

## Getting Help

If you continue to experience issues:

1. Check AWS Service Health Dashboard for S3 or KMS service issues
2. Review AWS CloudTrail logs for detailed error information
3. Contact AWS Support with specific error messages and request IDs
4. Consult the AWS Backint Agent for SAP documentation
