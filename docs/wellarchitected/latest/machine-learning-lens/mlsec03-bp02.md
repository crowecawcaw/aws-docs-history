

# MLSEC03-BP02 Secure data and modeling environment
<a name="mlsec03-bp02"></a>

 Secure your machine learning data and development environments to protect valuable information assets throughout the ML lifecycle. By implementing proper security measures for storage, compute, and network resources, you can maintain data integrity and confidentiality while enabling data scientists to work effectively. 

 **Desired outcome:** You have a secure foundation for storing, processing, and utilizing data for machine learning workloads. Your data is encrypted at rest and in transit, with access tightly controlled through identity management, infrastructure isolation, and secure coding practices. Your development environments are protected from unauthorized access while providing the necessary tools for your ML practitioners. 

 **Common anti-patterns:** 
+  Storing unencrypted training data in publicly accessible storage. 
+  Using default security configurations for ML environments. 
+  Allowing unrestricted internet access from ML environments. 
+  Using hard-coded credentials in ML code and notebooks. 
+  Installing ML packages from untrusted sources without validation. 
+  Granting excessive permissions to development environments. 

 **Benefits of establishing this best practice:** 
+  Protection of sensitive training data from unauthorized access or exfiltration. 
+  Reduced risk of compromised ML models and systems. 
+  Improves adherence to regulatory requirements for data handling. 
+  Improved governance of ML development environments. 
+  Enhanced ability to detect and respond to security events. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Securing your ML environments requires a comprehensive approach addressing data storage, compute resources, network isolation, and access controls. The ML lifecycle involves multiple stages where data could be exposed if proper security measures aren't implemented. By establishing secure foundations for your ML infrastructure, you can protect valuable intellectual property while still enabling productivity. 

 Start by securing your data repositories with encryption and access controls. Then build secure compute environments for model development that maintain isolation through private networking. Implement proper credential management to avoid exposure of secrets. Finally, verify that your package management practices block the introduction of malicious code into your ML pipeline. 

 Modern ML workloads often involve large datasets and complex algorithms, making security even more critical as the impact of a breach could be substantial. By implementing the measures in this best practice, you create a secure foundation for your ML initiatives. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build a secure analysis environment**. During the data preparation and feature engineering phases, leverage secure data exploration options on AWS. Use [Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) managed environments or [Amazon EMR](https://aws.amazon.com/emr/) for data processing. Alternatively, use managed services like [Amazon Athena](https://aws.amazon.com/athena/) and [AWS Glue](https://aws.amazon.com/glue/) to explore data without moving it from your data lake. For smaller datasets, use Amazon SageMaker AI Studio to explore, visualize, and engineer features, then scale up your feature engineering using managed ETL services like Amazon EMR or AWS Glue. 

1.  **Create dedicated IAM and KMS resources**. Limit the scope and impact of credentials and keys by creating dedicated [AWS IAM](https://aws.amazon.com/iam/) roles and [AWS KMS](https://aws.amazon.com/kms/) keys for ML workloads. Create private [Amazon S3](https://aws.amazon.com/s3/) buckets with versioning enabled to protect your data and intellectual property. Implement a centralized data lake using [AWS Lake Formation](https://aws.amazon.com/lake-formation/) on Amazon S3. Secure your data lake using a combination of services to encrypt data in transit and at rest. Monitor access with granular [AWS IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), [S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html), [S3 Access Logs](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html), [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). 

1.  **Use Secrets Manager and Parameter Store to protect credentials**. Replace hard-coded secrets in your code with API calls to programmatically retrieve and decrypt secrets using [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). Use [AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/features/#Parameter_Store) to store application configuration variables such as AMI IDs or license keys. Grant permissions to your SageMaker AI IAM role to access these services from your ML environments. 

1.  **Automate managing configuration**. Use lifecycle configuration scripts to manage ML environments. These scripts run when environments are created or restarted, allowing you to install custom packages, preload datasets, and set up source code repositories. Lifecycle configurations can be reused across multiple environments and updated centrally. Use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) infrastructure as code and [Service Catalog](https://aws.amazon.com/servicecatalog/) to simplify configuration for end users while maintaining security standards. 

1.  **Create private, isolated, network environments**. Use [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) to limit connectivity to only essential services and users. Deploy Amazon SageMaker AI resources in a VPC to enable network-level controls and capture network activity in [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html). For distributed training workloads, use [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html) which provides managed, resilient clusters with built-in VPC integration and multi-AZ deployment for enhanced security and availability. This deployment model also enables secure queries to data sources within your VPC, such as [Amazon RDS](https://aws.amazon.com/rds/) databases or [Amazon Redshift](https://aws.amazon.com/redshift/) data warehouses. Use IAM to restrict access to ML environment web UIs so they can only be accessed from within your VPC. Implement [AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html) to privately connect your SageMaker AI resources with supported AWS services, facilitating secure communication within the AWS network. Use [AWS KMS](https://aws.amazon.com/kms/) to encrypt data on the [Amazon EBS](https://aws.amazon.com/ebs/) volumes attached to SageMaker AI resources. 

1.  **Restrict access**. ML development environments provide web-based access to the underlying compute resources, typically with elevated privileges. Restrict this access to remove the ability to assume root permissions while still allowing users to control their local environment. Implement least privilege access controls for ML resources. 

1.  **Secure ML algorithms**. Amazon SageMaker AI uses container technology to train and host algorithms and models. When creating custom containers, publish them to a private container registry hosted on [Amazon Elastic Container Repository (Amazon ECR)](https://aws.amazon.com/ecr/). Encrypt containers hosted on Amazon ECR at rest using AWS KMS. Regularly scan containers for vulnerabilities and implement a secure container update process. 

1.  **Enforce code best practices**. Use secure git repositories for storing code. Implement code reviews, automated security scanning, and version control for ML code. Integrate security checks into your ML CI/CD pipeline to detect potential security issues early in the development process. 

1.  **Implement a package mirror for consuming approved packages**. Evaluate license terms to determine appropriate ML packages for your business across the ML lifecycle phases. Common ML Python packages include Pandas, PyTorch, Keras, NumPy, and Scikit-learn. Build an automated validation mechanism to check packages for security issues. Only download packages from approved and private repos. Validate package contents before importing. SageMaker AI supports [modifying package channel paths to a private repository](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/). When appropriate, use an internal repository as a proxy for public repositories to minimize network traffic and reduce overhead. 

1.  **Implement model security monitoring**. Deploy continuous monitoring solutions to detect unauthorized access attempts, unusual data access patterns, and potential data exfiltration from your ML environments. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), and [Amazon GuardDuty](https://aws.amazon.com/guardduty/) to create a comprehensive security monitoring solution for ML resources. 

1.  **Implement additional security controls for AI workloads**. For AI workloads, implement additional security controls around input validation and data leakage prevention. Implement [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to detect drift in production AI systems. Consider using [Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) to document model security characteristics and limitations. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Prerequisites for using SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html) 
+  [Storage Best Practices for Data and Analytics Applications](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html) 
+  [Configure security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html) 
+  [Protecting compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html) 
+  [Protecting data in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-in-transit.html) 
+  [7 ways to improve security of your machine learning workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/) 
+  [Building secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/) 
+  [Setting up secure, well-governed machine learning environments on AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/) 
+  [Private package installation in Amazon SageMaker AI running internet-free mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/) 
+  [Secure Deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/) 
+  [Apply fine-grained data access controls with AWS Lake Formation and Amazon EMR from Amazon SageMaker AI Studio](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-data-access-controls-with-aws-lake-formation-and-amazon-emr-from-amazon-sagemaker-studio/) 

 **Related videos:** 
+  [Security for AI/ML Models in AWS](https://www.youtube.com/watch?v=toDQL_c8Zug) 
+  [Security best practices the AWS Well-Architected way](https://www.youtube.com/watch?v=wfIVI-M7lbQ) 

 **Related examples:** 
+  [Secure Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture) 
+  [Amazon SageMaker AI Secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops) 