# Use AMS SSP to provision AWS Private Certificate Authority in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Private Certificate Authority capabilities directly in your AMS managed account. Private certificates are used for identifying and securing communication between connected
resources on private networks, such as servers, mobile, and IoT devices and applications.
AWS Private CA is a managed private CA service that helps you easily and securely manage the lifecycle
of your private certificates. AWS Private CA provides you a highly-available private CA service without
the upfront investment and ongoing maintenance costs of operating your own private CA.
AWS Private CA extends ACM’s certificate management capabilities to private certificates, enabling you
to create and manage public and private certificates centrally. You can easily create and deploy private
certificates for your AWS resources using the AWS Management Console or the ACM API. For
EC2 instances, containers, IoT devices, and on-premises resources, you can easily create and track
private certificates and use your own client-side automation code to deploy them. You also have the
flexibility to create private certificates and manage them yourself for applications that require custom
certificate lifetimes, key algorithms, or resource names
To learn more, see
[AWS Private CA](https://aws.amazon.com/certificate-manager/private-certificate-authority/ "https://aws.amazon.com/certificate-manager/private-certificate-authority/").

## AWS Private CA in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access AWS Private CA in my AMS account?**

Request access through the submission of the AWS Services RFC (Management
| AWS service | Compatible Service). Through this RFC the following IAM role will be provisioned in your account: `customer_acm_pca_role`. Once provisioned in your account, you must onboard the role in your federation solution. **Q: What are the restrictions to using the AWS Private CA?** Currently, AWS Resource Access Manager (AWS RAM) cannot be used to share your AWS Private CA cross-account. **Q: What are the prerequisites or dependencies to using AWS Private CA?** 1. If you plan to create a CRL, you need an S3 bucket to store it in. AWS Private CA automatically deposits the CRL in the Amazon S3 bucket you designate and updates it periodically. It is a pre requisite that the S3 bucket has the below bucket policy before you can set-up a CRL. In order to proceed with this request; create a RFC with ct-0fpjlxa808sh2 (Management | Advanced stack components | S3 storage | Update policy) as follows: <br>• Provide the S3 bucket name or ARN. <br>• Copy the below policy onto RFC and replace `bucket-name` with your desired S3 bucket name. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Principal":{ "Service":"acm-pca.amazonaws.com" }, "Action":[ "s3:PutObject", "s3:PutObjectAcl", "s3:GetBucketAcl", "s3:GetBucketLocation" ], "Resource":[ "arn:aws:s3:::bucket-name/*", "arn:aws:s3:::bucket-name" ] } ] }` `` 2. If the above S3 bucket is encrypted, then the Service Principal acm-pca.amazonaws.com requires permissions to decrypt. In order to proceed with this request; create a RFC with ct-3ovo7px2vsa6n (Management | Advanced stack components | KMS key | Update) as follows: <br>• Provide the KMS Key ARN on which the policy must be updated. <br>• Copy the below policy onto RFC and replace `bucket-name` with your desired S3 bucket name. `{ "Sid":"Allow ACM-PCA use of the key", "Effect":"Allow", "Principal":{ "Service":"acm-pca.amazonaws.com" }, "Action":[ "kms:GenerateDataKey", "kms:Decrypt" ], "Resource":"*", "Condition":{ "StringLike":{ "kms:EncryptionContext:aws:s3:arn":[ "arn:aws:s3:::bucket_name/acm-pca-permission-test-key", "arn:aws:s3:::bucket_name/acm-pca-permission-test-key-private", "arn:aws:s3:::bucket_name/audit-report/*", "arn:aws:s3:::bucket_name/crl/*" ] } } }` 3. AWS Private CA CRLs don't support the S3 setting "Block public access to buckets and objects granted through new access control lists (ACLs)". You must disable this setting with the S3 account and bucket in order to allow the AWS Private CA to write CRLs as mentioned in [How to securely create and store your CRL for ACM Private CA](https://aws.amazon.com/blogs/security/how-to-securely-create-and-store-your-crl-for-acm-private-ca/ "https://aws.amazon.com/blogs/security/how-to-securely-create-and-store-your-crl-for-acm-private-ca/") If you would like to disable, create a new RFC with ct-0xdawir96cy7k (Management | Other | Other | Update) and attach a Risk Acceptance. If you have any questions on risk acceptance, reach out to your Cloud Architect.
