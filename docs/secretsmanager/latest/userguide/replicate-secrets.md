# Replicate AWS Secrets Manager secrets across Regions

You can replicate your secrets in multiple AWS Regions to support applications spread
across those Regions to meet Regional access and low latency requirements. If you later need to,
you can [promote a replica secret to a standalone](standalone-secret.md "standalone-secret.md") and then set it up for replication
independently. Secrets Manager replicates the encrypted secret data and metadata such as tags and resource
policies across the specified Regions.

The ARN for a replicated secret is the same as the primary secret except for the Region, for example:

- Primary secret:
  `arn:aws:secretsmanager:`Region1`:123456789012:secret:MySecret-a1b2c3`
- Replica secret:
  `arn:aws:secretsmanager:`Region2`:123456789012:secret:MySecret-a1b2c3`
  For pricing information for replica secrets, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/").

When you store database credentials for a source database that is replicated to other
Regions, the secret contains connection information for the source database. If you then
replicate the secret, the replicas are copies of the source secret and contain the same
connection information. You can add additional key/value pairs to the secret for regional
connection information.

If you turn on rotation for your primary secret, Secrets Manager rotates the secret in the primary
Region, and the new secret value propagates to all of the associated replica secrets. You don't
have to manage rotation individually for all of the replica secrets.

You can replicate secrets across all of your enabled AWS Regions. However, if you use
Secrets Manager in special AWS Regions such as AWS GovCloud (US) or China Regions, you can only configure
secrets and the replicas within these specialized AWS Regions. You can't replicate a secret in
your enabled AWS Regions to a specialized Region or replicate secrets from a specialized
region to a commercial region.

Before you can replicate a secret to another Region, you must enable that Region. For more
information, see [Managing AWS
Regions.](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable")

It is possible to use a secret across multiple Regions without replicating it by calling the
Secrets Manager endpoint in the Region where the secret is stored. For a list of endpoints, see [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints"). To use
replication to improve your workload's resilience, see [Disaster
Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/ "https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/").

Secrets Manager generates a CloudTrail log entry when you replicate a secret. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

###### To replicate a secret to other Regions (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. From the list of secrets, choose your secret.
3. On the secret details page, on the **Replication** tab, do one of the following:
   - If your secret is not replicated, choose **Replicate
     secret**.
   - If your secret is replicated, in the **Replicate secret** section,
     choose **Add Region**.

4. In the **Add replica regions** dialog box, do the following:
   1. For **AWS Region**, choose the Region you want to replicate the
      secret to.
   2. (Optional) For **Encryption key**, choose a KMS key to encrypt
      the secret with. The key must be in the replica Region.
   3. (Optional) To add another Region, choose **Add more
      regions**.
   4. Choose **Replicate**.You return to the secret details page. In the **Replicate secret**
      section, the **Replication status** shows for each Region.

## AWS CLI

###### Example Replicate a secret to another region

The following [`replicate-secret-to-regions`](../../../cli/latest/reference/secretsmanager/replicate-secret-to-regions.md "../../../cli/latest/reference/secretsmanager/replicate-secret-to-regions.md") example replicates a secret to eu-west-3. The replica is encrypted with the AWS managed key **aws/secretsmanager**.

```
aws secretsmanager replicate-secret-to-regions \
        --secret-id MyTestSecret \
        --add-replica-regions Region=eu-west-3
```

###### Example Create a secret and replicate it

The following [example](../../../cli/latest/reference/secretsmanager/create-secret.md "../../../cli/latest/reference/secretsmanager/create-secret.md") creates a secret and replicates it to eu-west-3. The replica is encrypted with the AWS managed key **aws/secretsmanager**.

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --description "My test secret created with the CLI." \
    --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"
    --add-replica-regions Region=eu-west-3
```

## AWS SDK

To replicate a secret, use the [`ReplicateSecretToRegions`](../apireference/API_ReplicateSecretToRegions.md "../apireference/API_ReplicateSecretToRegions.md") command. For more information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
