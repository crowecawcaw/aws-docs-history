# Launch conversion errors

The following errors can occur during the conversion phase when you launch a drill
or recovery instance in AWS Elastic Disaster Recovery (Elastic Disaster Recovery). The conversion phase prepares your replicated
volumes for use in the target AWS environment.

###### Topics

- [Error: Failed to connect using HTTP channel](#Error-Failed-to-connect-using-HTTP-channel "#Error-Failed-to-connect-using-HTTP-channel")
- [Error: Conversion server launch failed](#error-conversion-server-launch-failed "#error-conversion-server-launch-failed")
- [Error: Conversion failed](#error-conversion-failed "#error-conversion-failed")
- [Error: Failed to take snapshot](#error-snapshot-failed "#error-snapshot-failed")

## Error: Failed to connect using HTTP channel

**Error message:**
**`Failed to connect using HTTP channel`**

**Cause:** The Conversion server cannot communicate
with AWS endpoints on TCP port 443. The Conversion server is a separate instance from
the replication server and might be affected by network changes made after replication
was established.

**Resolution:**

Console

###### To resolve using the console

1. Open the Amazon VPC console and verify the staging area subnet's route table
   allows outbound traffic on TCP port 443.
2. Verify that the security group associated with the staging area subnet
   allows outbound TCP port 443 traffic.
3. Verify that the network ACL for the staging area subnet allows outbound
   TCP port 443 traffic.
4. Check for recent network changes that might affect connectivity from the
   staging area to AWS service endpoints.

CLI

###### To resolve using the CLI

1. Test connectivity from the staging area to the Elastic Disaster Recovery, Amazon S3, and
   Amazon EC2 endpoints. Run one of the following commands depending on your
   operating system:

   - Linux:

   ```
   curl -v https://drs.`region`.amazonaws.com
   ```
   - Windows:

   ```
   Test-NetConnection -ComputerName drs.`region`.amazonaws.com -Port 443
   ```

2. Verify the route tables for the staging area subnet:

```
aws ec2 describe-route-tables \
    --filters "Name=association.subnet-id,Values=`subnet-id`"
```

3. Confirm that a route to `0.0.0.0/0` exists and points to an
   internet gateway, NAT gateway, or VPC endpoint that allows traffic to AWS
   service endpoints on port 443.

If the issue persists after verifying network configuration, create an
AWS Support case with details about your staging area network configuration.

## Error: Conversion server launch failed

**Error message:**
**`Conversion server launch failed`**

**Cause:** The conversion server could not be launched
or did not become available. This can be caused by Amazon EC2 capacity constraints, IAM
permission issues, or subnet configuration problems.

**Resolution:**

###### To resolve this error

1. Retry the launch from the Elastic Disaster Recovery console.
2. If the error persists, create an AWS Support case. Include the recovery job ID,
   which you can find in the Elastic Disaster Recovery console.

## Error: Conversion failed

**Error message:**
**`Conversion failed`**

**Cause:** The volume conversion process did not
complete. This can occur due to disk corruption on the source, unsupported filesystem
types, or internal conversion errors.

**Resolution:**

###### To resolve this error

1. Retry the launch from the Elastic Disaster Recovery console.
2. If the error persists, create an AWS Support case. Include the recovery job ID
   from the Elastic Disaster Recovery console.

## Error: Failed to take snapshot

**Error message:**
**`Failed to take snapshot`**

**Cause:** Elastic Disaster Recovery could not create a point-in-time
snapshot. If you use a custom AWS KMS key for EBS encryption, the key might be missing,
disabled, or the Elastic Disaster Recovery service roles might lack permissions.

**Resolution:**

###### To resolve this error

1. Verify that the AWS KMS key exists and is enabled.
2. Verify that the Elastic Disaster Recovery service roles have
   `kms:CreateGrant` and `kms:DescribeKey` permissions
   on the key.
3. Retry the launch from the Elastic Disaster Recovery console.
4. If the error persists, create an AWS Support case. Include the recovery job ID
   from the Elastic Disaster Recovery console.
