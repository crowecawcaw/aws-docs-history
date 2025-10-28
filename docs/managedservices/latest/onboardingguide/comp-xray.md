# Use AMS SSP to provision AWS X-Ray in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS X-Ray (X-Ray) capabilities directly in your AMS managed account. AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a
microservices architecture. With X-Ray, you can understand how your application and its underlying services are
performing, to identify and troubleshoot the root cause of performance issues and errors. X-Ray provides an
end-to-end view of requests as they travel through your application, and shows a map of your application’s
underlying components. You can use X-Ray to analyze both applications in development and in production, from
simple three-tier applications, to complex microservices applications consisting of thousands of services.
To learn more, see [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/").

## X-Ray in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS X-Ray in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type. This RFC provisions the
following IAM role to your account: `customer_xray_console_role`. After it's provisioned in your account, you
must onboard the role in your federation solution. Additionally, you must have the `customer_xray_daemon_write_instance_profile` to push
data from your Amazon EC2 instances to X-Ray. This instance profile is created when you receive the `customer_xray_console_role`.

You can submit a service request to AMS Operations to assign the `customer_xray_daemon_write_policy` to the existing instance
profile, or you can use the instance profile that is created when AMS Operations enables X-Ray for you.

**Q: What are the restrictions to using AWS X-Ray in my AMS account?**

Full functionality of AWS X-Ray is available in your AMS account except for encryption with
AWS KMS key (KMS key). AWS X-Ray encrypts all trace data by default. By default, X-Ray encrypts traces and related data at rest. If you need
to encrypt data at rest with a key, you can choose either AWS-managed KMS key (aws/xray) or KMS Customer-Managed key. For KMS Customer-Managed key for
X-Ray encryption, submit a Management | Other | Other | Create change type (ct-1e1xtak34nx76).

**Q: What are the prerequisites or dependencies to using AWS X-Ray in my AMS account?**

AWS X-Ray has a dependency on Amazon S3, CloudWatch, and CloudWatch Logs, which are already implemented in AMS accounts. Transitive dependencies vary
based on data sources and other AWS service AWS X-Ray that features may be interacting with (for example, Amazon Redshift, Amazon RDS, Athena).
