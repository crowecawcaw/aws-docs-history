

# AWS Secrets Manager best practices
<a name="best-practices"></a>

Secrets Manager provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don't represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

**Topics**
+ [Store credentials and other sensitive information in AWS Secrets Manager](#best-practices-store-secrets-safely)
+ [Find unprotected secrets in your code](#w2aab9b9)
+ [Choose an encryption key for your secret](#w2aab9c11)
+ [Use caching to retrieve secrets](#best-practices-caching)
+ [Rotate your secrets](#w2aab9c15)
+ [Mitigate risks of using CLI](#w2aab9c17)
+ [Limit access to secrets](#w2aab9c19)
+ [Replicate secrets](#w2aab9c21)
+ [Monitor secrets](#w2aab9c23)
+ [Run your infrastructure on private networks](#w2aab9c25)

## Store credentials and other sensitive information in AWS Secrets Manager
<a name="best-practices-store-secrets-safely"></a>

Secrets Manager can help improve your security posture and compliance, and reduce the risk of unauthorized access to your sensitive information. Secrets Manager encrypts secrets at rest using encryption keys that you own and store in AWS Key Management Service (AWS KMS). When you retrieve a secret, Secrets Manager decrypts the secret and transmits it securely over TLS to your local environment. For more information, see [Create an AWS Secrets Manager secret](create_secret.md).

## Find unprotected secrets in your code
<a name="w2aab9b9"></a>

CodeGuru Reviewer integrates with Secrets Manager to use a secrets detector that finds unprotected secrets in your code. The secrets detector searches for hardcoded passwords, database connection strings, user names, and more. For more information, see [Find unprotected secrets in your code with Amazon CodeGuru Reviewer](integrating-codeguru.md).

Amazon Q can scan your codebase for security vulnerabilities and code quality issues to improve the posture of your applications throughout the development cycle. For more information, see [Scanning your code with Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-scans.html) in the *Amazon Q Developer User Guide*.

## Choose an encryption key for your secret
<a name="w2aab9c11"></a>

For most cases, we recommend using the `aws/secretsmanager` AWS managed key to encrypt secrets. There is no cost for using it.

To be able to access a secret from another account or to apply a key policy to the encryption key, use a customer managed key to encrypt the secret.
+ In the key policy, assign the value `secretsmanager.<region>.amazonaws.com` to the [`kms:ViaService`](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition key. This limits use of the key to only requests from Secrets Manager.
+ To further limit use of the key to only requests from Secrets Manager with the correct context, use keys or values in the [Secrets Manager encryption context](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-encryption-context) as a condition for using the KMS key by creating:
  + A [string condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String) in an IAM policy or key policy
  + A [grant constraint](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html) in a grant

For more information, see [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md).

## Use caching to retrieve secrets
<a name="best-practices-caching"></a>

To use your secrets most efficiently, we recommend you use one of the following supported Secrets Manager caching components to cache your secrets and update them only when required:
+ [Java with client-side caching](retrieving-secrets_cache-java.md)
+ [Python with client-side caching](retrieving-secrets_cache-python.md)
+ [.NET with client-side caching](retrieving-secrets_cache-net.md)
+ [Go with client-side caching](retrieving-secrets_cache-go.md)
+ [Rust with client-side caching](retrieving-secrets_cache-rust.md)
+ [AWS Parameters and Secrets Lambda Extension](retrieving-secrets_lambda.md)
+ [Use AWS Secrets Manager secrets in Amazon Elastic Kubernetes Service](integrate_eks.md)
+ Use [Using the AWS Workload Credentials Provider](workload-credentials-provider.md) to standardize consumption of secrets from Secrets Manager across environments such as AWS Lambda, Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, and Amazon Elastic Compute Cloud. 

## Rotate your secrets
<a name="w2aab9c15"></a>

If you don't change your secrets for a long period of time, the secrets become more likely to be compromised. With Secrets Manager, you can set up automatic rotation as often as every four hours. Secrets Manager offers two strategies for rotation: [Single user](rotation-strategy.md#rotating-secrets-one-user-one-password) and [Alternating users](rotation-strategy.md#rotating-secrets-two-users). For more information, see [Rotate AWS Secrets Manager secrets](rotating-secrets.md).

## Mitigate risks of using CLI
<a name="w2aab9c17"></a>

When you use the AWS CLI to invoke AWS operations, you enter those commands in a command shell. Most command shells offer features that could compromise your secrets, such as logging and the ability to see the last entered command. Before you use the AWS CLI to enter sensitive information, be sure to [Mitigate the risks of using the AWS CLI to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md).

## Limit access to secrets
<a name="w2aab9c19"></a>

In IAM policy statements that control access to your secrets, use the principle of [least privileged access](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). You can use [IAM roles and policies](auth-and-access_iam-policies.md), [resource policies](auth-and-access_resource-policies.md), and [attribute-based access control (ABAC)](auth-and-access-abac.md). For more information, see [Authentication and access control for AWS Secrets Manager](auth-and-access.md).

**Topics**
+ [Block broad access to secrets](#iam-contextkeys-blockpublicpolicy)
+ [Use caution with IP address conditions in policies](#iam-contextkeys-ipaddress)
+ [Limit requests with VPC endpoint conditions](#iam-contextkeys-vpcendpoint)

### Block broad access to secrets
<a name="iam-contextkeys-blockpublicpolicy"></a>

In identity policies that allow the action `PutResourcePolicy`, we recommend you use `BlockPublicPolicy: true`. This condition means that users can only attach a resource policy to a secret if the policy doesn't allow broad access. 

Secrets Manager uses Zelkova automated reasoning to analyze resource policies for broad access. For more information about Zelkova, see [ How AWS uses automated reasoning to help you achieve security at scale](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/) on the AWS Security Blog.

The following example shows how to use `BlockPublicPolicy`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": "secretsmanager:PutResourcePolicy",
        "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName-AbCdEf}}",
    "Condition": {
            "Bool": {
                "secretsmanager:BlockPublicPolicy": "true"
            }
        }
    }
}
```

------

### Use caution with IP address conditions in policies
<a name="iam-contextkeys-ipaddress"></a>

Use caution when you specify the [IP address condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_IPAddress) or the `aws:SourceIp` condition key in a policy statement that allows or denies access to Secrets Manager. For example, if you attach a policy that restricts AWS actions to requests from your corporate network IP address range to a secret, then your requests as an IAM user invoking the request from the corporate network work as expected. However, if you enable other services to access the secret on your behalf, such as when you enable rotation with a Lambda function, that function calls the Secrets Manager operations from an AWS-internal address space. Requests impacted by the policy with the IP address filter fail.

Also, the `aws:sourceIP` condition key is less effective when the request comes from an Amazon VPC endpoint. To restrict requests to a specific VPC endpoint, use [Limit requests with VPC endpoint conditions](#iam-contextkeys-vpcendpoint).

### Limit requests with VPC endpoint conditions
<a name="iam-contextkeys-vpcendpoint"></a>

To allow or deny access to requests from a particular VPC or VPC endpoint, use `aws:SourceVpc` to limit access to requests from the specified VPC or `aws:SourceVpce` to limit access to requests from the specified VPC endpoint. See [Example: Permissions and VPCs](auth-and-access_resource-policies.md#auth-and-access_examples_vpc).
+ `aws:SourceVpc` limits access to requests from the specified VPC.
+ `aws:SourceVpce` limits access to requests from the specified VPC endpoint.

If you use these condition keys in a resource policy statement that allows or denies access to Secrets Manager secrets, you can inadvertently deny access to services that use Secrets Manager to access secrets on your behalf. Only some AWS services can run with an endpoint within your VPC. If you restrict requests for a secret to a VPC or VPC endpoint, then calls to Secrets Manager from a service not configured for the service can fail.

See [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md).

## Replicate secrets
<a name="w2aab9c21"></a>

Secrets Manager can automatically replicate your secrets to multiple AWS Regions to meet your resiliency or disaster recovery requirements. For more information, see [Replicate AWS Secrets Manager secrets across Regions](replicate-secrets.md).

## Monitor secrets
<a name="w2aab9c23"></a>

Secrets Manager enables you to audit and monitor secrets through integration with AWS logging, monitoring, and notification services. For more information, see:
+ [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md)
+ [Monitor AWS Secrets Manager with Amazon CloudWatch](monitoring-cloudwatch.md)
+ [Monitor AWS Secrets Manager secrets for compliance by using AWS Config](configuring-awsconfig-rules.md)
+ [Monitor Secrets Manager costs](monitor-secretsmanager-costs.md)
+ [Detect threats with Amazon GuardDuty](monitoring-guardduty.md)

## Run your infrastructure on private networks
<a name="w2aab9c25"></a>

We recommend that you run as much of your infrastructure as possible on private networks that are not accessible from the public internet. You can establish a private connection between your VPC and Secrets Manager by creating an *interface VPC endpoint*. For more information, see [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md).