

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Serverless data retention for AWS Wickr
<a name="serverless-method"></a>

AWS Wickr data retention can retain all conversations in your network, including direct message conversations and conversations in Groups or Rooms between in-network (internal) members and those with other teams (external) with whom your network is federated. Serverless data retention is available only if you have an AWS Wickr Premium plan and opt in. It is not available for AWS Wickr Enterprise.

**Note**  
 Data retention service is currently only available in the following regions: US East (N. Virginia), Canada (Central), Asia Pacific (Sydney), Europe (Frankfurt), Europe (Stockholm), Asia Pacific (Tokyo), Asia Pacific (Singapore), Europe (Zurich), AWS GovCloud (US-West).

**Note**  
 AWS does not support configuring Wickr data retention bot using [Wickr Admin SDK](https://us-west-2.console.aws.amazon.com/servicecatalog/home?region=us-west-2#portfolios?activeTab=importedAdminPortfolios). The configuration has to be performed using the AWS console.

The serverless data retention service provides a cloud-native alternative to the traditional Docker container-based data retention bot. This new method offers simplified deployment, managed infrastructure, automatic scaling, and comprehensive monitoring with reasonable tradeoffs related to Wickr's end-to-end encryption (E2EE) model.

**Key Benefits of Serverless Method**
+ **Simplified Deployment**: Console-guided setup with minimal configuration steps, completed in minutes rather than hours
+ **Managed Infrastructure**: No need to provision or maintain EC2 instances, Docker containers, or monitor bot health
+ **Automatic Scaling**: Dynamically handles message volume fluctuations without manual intervention
+ **Enhanced Monitoring**: Pre-configured CloudWatch dashboards, metrics, and configurable alerting
+ **Improved Reliability**: Fault-tolerant message delivery with automatic recovery 

**How It Works**

When you enable the serverless data retention service, all messages and files shared in your network are retained in accordance with your organization's compliance policies. The service uses AWS Nitro Enclaves to Wickr decrypt message content and then uses Customer Managed KMS keys to reencrypt content for transit to your S3 bucket. You can then decrypt messages on demand to access encrypted content.

**Note**  
 Wickr never accesses your messages and files. All decryption occurs within secure Nitro Enclaves using your KMS keys, and decrypted content is stored only in your AWS account.

## Where data retention components run
<a name="where-components-run"></a>

The data retention *processing* infrastructure runs in a Wickr-managed service account, not in your AWS account. Within the AWS Nitro Enclave, Wickr decrypts messages and re-encrypts them with your customer managed KMS key before sending them to your encrypted retention Amazon S3 bucket. You do not deploy, patch, or scale these components.

The CloudFormation template that you launch from Service Catalog creates only resources that you own. You control these resources in your account:
+ The encrypted retention Amazon S3 bucket and the decrypted output Amazon S3 bucket
+ The KMS keys that protect your retained data (or references to the keys you supply)
+ The cross-account IAM role that the service assumes to use your key and write to your bucket
+ The on-demand decryption workflow (Step Functions state machine and Lambda functions) 
+ The CloudWatch dashboard and alarm for your network

### Why Wickr cannot see your message content
<a name="why-wickr-cannot-see-content"></a>

Wickr cannot see your message content for the following reasons:
+ The sender's device encrypts every message end-to-end. Every component outside the enclave handles only Wickr-encrypted ciphertext. This includes Wickr message routing.
+ Plaintext exists only in the memory of the Nitro Enclave. The enclave has no persistent storage, no network interface, and no interactive access (no SSH or shell). It communicates only with its parent host over a local socket. The host relays only ciphertext.
+ Content leaves the enclave only after it is encrypted with your customer managed KMS key. The enclave's private keys and account state are likewise stored only in encrypted form, protected by your key.
+ Each request that the enclave makes with your key includes a Nitro Enclave attestation document. AWS KMS records values from the attestation document in CloudTrail, so you can inspect which enclave image used your key. You can disable your key at any time to stop all decryption.
+ The service makes state changes on your behalf only inside the enclave. There, Wickr decrypts messages, re-encrypts them with your customer managed KMS key, and replenishes the data retention bot's keys. Every use of your key is logged in CloudTrail in your account.

For more information, see [What is AWS Nitro Enclaves?](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) in the *AWS Nitro Enclaves User Guide* and [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) in the *AWS CloudTrail User Guide*.

## Prerequisites
<a name="serverless-prerequisites"></a>

Before enabling serverless data retention, ensure you have the following:
+ **AWS Wickr Premium Plan**: Data retention is only available to premium plan subscribers
+ **AWS Account**: An active AWS account with appropriate permissions on KMS and S3.
+ **IAM Permissions**: Ability to import Service Catalog portfolios and deploy CloudFormation templates

**Topics**
+ [Where data retention components run](#where-components-run)
+ [Prerequisites](#serverless-prerequisites)
+ [Configure serverless method](configure-serverless-method.md)
+ [Architecture Overview](architecture.md)
+ [Access retained data](retained-data.md)
+ [Monitoring and management](monitor-manage.md)
+ [Expected costs](expected-costs.md)
+ [Migration from docker method](migration-process.md)
+ [Security considerations](considerations-security.md)
+ [Best practices](best-practices.md)