

# Encrypting data written by DataBrew jobs
<a name="encryption-security-configuration"></a>

DataBrew jobs can write to encrypted Amazon S3 targets and encrypted Amazon CloudWatch Logs. 

**Topics**
+ [Setting up DataBrew to use encryption](#encryption-setup-DataBrew)
+ [Creating a route to AWS KMS for VPC jobs](#encryption-kms-vpc-endpoint)
+ [Setting up encryption with AWS KMS keys](#console-security-configurations-wizard)

## Setting up DataBrew to use encryption
<a name="encryption-setup-DataBrew"></a>

Follow this procedure to set up your DataBrew environment to use encryption.

**To set up your DataBrew environment to use encryption**

1. Create or update your AWS KMS keys to give AWS KMS permissions to the AWS Identity and Access Management (IAM) roles that are passed to DataBrew jobs. These IAM roles are used to encrypt CloudWatch Logs and Amazon S3 targets. For more information, see [Encrypt Log Data in CloudWatch Logs Using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html) in the *Amazon CloudWatch Logs User Guide*. 

   In the following example, {{`"role1"`}}, {{`"role2"`}}, and {{`"role3"`}} are IAM roles that are passed to DataBrew jobs. This policy statement describes a KMS key policy that gives permission to the listed IAM roles to encrypt and decrypt with this KMS key.

   ```
      {
          "Effect": "Allow",
          "Principal": {
              "Service": "logs.{{region}}.amazonaws.com",
              "AWS": [
                  "{{role1}}",
                  "{{role2}}",
                  "{{role3}}"
              ]
          },
          "Action": [
              "kms:Encrypt*",
              "kms:Decrypt*",
              "kms:ReEncrypt*",
              "kms:GenerateDataKey*",
              "kms:Describe*"
          ],
          "Resource": "*"
      }
   ```

   The `Service` statement, shown as `"Service": "logs.{{region}}.amazonaws.com"`, is required if you use the key to encrypt CloudWatch Logs.

1. Ensure that the AWS KMS key is set to `ENABLED` before it is used.

For more information about specifying permissions using AWS KMS key policies, see [Using key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html).

## Creating a route to AWS KMS for VPC jobs
<a name="encryption-kms-vpc-endpoint"></a>

You can connect directly to AWS KMS through a private endpoint in your virtual private cloud (VPC) instead of connecting over the internet. When you use a VPC endpoint, communication between your VPC and AWS KMS is conducted entirely within the AWS network.

You can create an AWS KMS VPC endpoint within a VPC. Without this step, your DataBrew jobs might fail with a `kms timeout`. For detailed instructions, see [Connecting to AWS KMS Through a VPC Endpoint](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html) in the *AWS Key Management Service Developer Guide*. 

As you follow these instructions, on the [VPC console](https://console.aws.amazon.com//vpc), make sure to do the following:
+ Choose **Enable Private DNS name**.
+ For **Security group**, choose the security group (including a self-referencing rule) that you use for your DataBrew job that accesses Java Database Connectivity (JDBC).

When you run a DataBrew job that accesses JDBC data stores, DataBrew must have a route to the AWS KMS endpoint. You can provide the route with a network address translation (NAT) gateway or with an AWS KMS VPC endpoint. To create a NAT gateway, see [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.

## Setting up encryption with AWS KMS keys
<a name="console-security-configurations-wizard"></a>

When you enable encryption on a job, it applies to both Amazon S3 and CloudWatch. The IAM role that is passed must have the following AWS KMS permissions.

For more information, see the following topics in the *Amazon Simple Storage Service User Guide*:
+ For information about `SSE-S3`, see [Protecting Data Using Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html). 
+ For information about `SSE-KMS`, see [Protecting Data Using Server-Side Encryption with AWS KMS–Managed Keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html). 