# MLSEC-04: Secure data and modeling environment

Secure any system or environment that hosts data or enables
model development. Store training data in secured storage and
repositories. Run data preparation in a secure cloud. Tightly
control access to the destination compute instances as data
moves from the data repositories to the instances. Encrypt data
at rest in the storage infrastructure and in transit to the
compute infrastructure.

## Implementation plan

- **Build a secure analysis
  environment** - During the data preparation and
  feature engineering phases, there are multiple options for
  secure data exploration on AWS. Data can be explored in an
  [Amazon](https://aws.amazon.com/sagemaker/getting-started/ "https://aws.amazon.com/sagemaker/getting-started/")
  [SageMaker AI](https://aws.amazon.com/sagemaker/getting-started/ "https://aws.amazon.com/sagemaker/getting-started/")
  managed notebook environment, or in an
  [Amazon EMR](https://aws.amazon.com/emr/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/emr/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc") notebook. You can also use managed services,
  such as
  [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") and
  [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/"), or a combination of the two, to explore the
  data without moving the data out of your data lake. Use an
  Amazon SageMaker AI Jupyter notebook instance to explore,
  visualize, and feature engineer a small subset of data.
  Scale up the feature engineering using a managed ETL
  service, such as Amazon EMR or AWS Glue.
- **Create dedicated**
  [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") **and**
  [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") **resources** –
  This approach limits the scope of impact of credentials
  and keys. Create a private
  [S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
  bucket and enable version control for the data and
  intellectual property (IP). In AWS, a centralized data
  lake is implemented using AWS Lake Formation on Amazon S3.
  Securing and monitoring a data lake on Amazon S3 is
  achieved using a combination of services and capabilities
  to encrypt data in transit and at rest. Monitor access
  using granular
  [AWS IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md"),
  [S3
  bucket policies](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md"),
  [S3
  Access](../../../AmazonS3/latest/dev/ServerLogs.md "../../../AmazonS3/latest/dev/ServerLogs.md")
  [Logs](../../../AmazonS3/latest/dev/ServerLogs.md "../../../AmazonS3/latest/dev/ServerLogs.md"),
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"), and
  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/").
- **Use Secrets Manager and Parameter
  Store to protect credentials** - Secrets Manager
  enables you to replace hard-coded secrets in your code,
  such as credentials, with an API call to decrypt and
  retrieve the secret programmatically. Parameter Store was
  designed for wider use cases than secrets or passwords,
  but allows you to store application configuration
  variables such as AMI IDs or license keys. With
  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager "https://aws.amazon.com/secrets-manager") and Parameter Store, you can store
  your credentials, and then grant permissions to your
  SageMaker AI IAM role to access Secrets Manager from your
  notebook.
- **Automate managing
  configuration** - Use lifecycle configurations
  scripts to manage Jupyter notebook instances. The scripts
  run when the notebook instance is first created, or every
  time it starts. They enable you to install custom
  packages, preload datasets, and set up source code
  repositories. Lifecycle configurations can be changed and
  reused across multiple notebook instances. You can make a
  change once and apply the updated configuration by
  restarting the managed notebook instances. This gives IT,
  operations, and security teams the flexibility and control
  they need, while supporting the needs of your developers
  and data scientists. Use
  [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") infrastructure as code, as well as
  [Service Catalog](https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc "https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc") to simplify configuration for end
  users.
- **Create private, isolated, network environments** - Use [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/?vpc-blogs.sort-by=item.additionalFields.createdDate&vpc-blogs.sort-order=desc "https://aws.amazon.com/vpc/?vpc-blogs.sort-by=item.additionalFields.createdDate&vpc-blogs.sort-order=desc") (Amazon VPC) to enable connectivity to only the services and users you need. Deploy the Amazon SageMaker AI notebook instance in an Amazon VPC to enable network level controls to limit communication to the hosted notebook. Additionally, network calls into and out of the
  notebook instance can be captured in [VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") to enable additional visibility and control at the network level. By deploying the notebook in your VPC, you will also be able to query data sources and systems accessible from within your VPC, such as
  relational databases in [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
  or [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/") data warehouses.
  Using IAM, you can further restrict access to the web-based UI of the notebook instance so that it can only be accessed from within your VPC.

Use [AWS PrivateLink](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md") to
privately connect your SageMaker AI notebook instance VPC with supported AWS services. This ensures secure communication between your notebook instance
and [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") within the AWS network.
Use [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to encrypt data
on the [EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") volumes attached to SageMaker AI notebook instances.

- **Restrict access** - The
  Jupyter notebook server provides web-based access to the
  underlying operating system on an EC2 instance. This gives
  you the ability to install additional software packages or
  Jupyter kernels to customize your environment. The access
  is granted by default to a user with root access or super
  user on the operating system, giving them total control of
  the underlying EC2 instance. This access should be
  restricted to remove the user's ability to assume root
  permissions but still give them control over their local
  user's environment.
- **Secure ML algorithms** -
  Amazon SageMaker AI uses container technology to train and
  host algorithms and models. When creating your own
  containers, publish them to a private container registry
  hosted on
  [Amazon
  Elastic Container](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/")
  [Repository
  (Amazon ECR)](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/"). Encrypt containers that are hosted on
  Amazon ECR at rest using AWS KMS.
- **Enforce code best
  practices** - Use secure git repositories for storing code.
- **Implement a package mirror for
  consuming approved packages** - Evaluate the
  license terms to determine which ML packages are
  appropriate for your business across the phases of the ML
  lifecycle. Examples of ML Python packages include: Pandas,
  PyTorch, Keras, NumPy, and Scikit-learn. Once you’ve
  determined the set and criteria, build a validation
  mechanism and automate it where possible. A sample
  automated mechanism can include a script that runs the
  download, installation, and package version and dependency
  checks.
  [Only
  download packages from approved and private repos.](https://www.youtube.com/watch?v=HlSEUvApDZE&t=578s "https://www.youtube.com/watch?v=HlSEUvApDZE&t=578s")
  Validate what is in the packages downloaded. This will
  enable importing safely and confirming the validity of
  packages.
  [Amazon SageMaker AI notebook instances](../../../sagemaker/latest/dg/nbi-add-external.md "../../../sagemaker/latest/dg/nbi-add-external.md") come with multiple
  environments already installed. These environments contain
  Jupyter kernels and Python packages. You can also install
  your own environments that contain your choice of packages
  and kernels. SageMaker AI enables
  [modifying
  package channel paths to a private repository](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/ "https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/").
  Where appropriate, use an internal repository as a proxy
  for public repositories to minimize the network and time
  overhead.

## Documents

- [Storage
  Best Practices for Data and Analytics Applications](../../../whitepapers/latest/building-data-lakes/building-data-lake-aws.md "../../../whitepapers/latest/building-data-lakes/building-data-lake-aws.md")
- [Security
  in Amazon SageMaker AI](../../../sagemaker/latest/dg/security.md "../../../sagemaker/latest/dg/security.md")
- [Amazon
  Well-Architected Security Pillar for Software
  Integrity](../security-pillar/protecting-compute.md "../security-pillar/protecting-compute.md")
- [Installing
  External Libraries and Kernels on Notebook
  Instances](../../../sagemaker/latest/dg/nbi-add-external.md "../../../sagemaker/latest/dg/nbi-add-external.md")
- [AWS Well Architected Framework Security Pillar : Protecting
  Data in Transit](../security-pillar/protecting-data-in-transit.md "../security-pillar/protecting-data-in-transit.md")

## Blogs

- [7
  ways to improve security of your machine learning](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")
- [Building
  secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/")
- [Setting
  up secure, well-governed machine learning environments on
  AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/ "https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/")
- [Private
  package installation in Amazon SageMaker AI running
  internet-free mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/ "https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/")
- [Secure
  Deployment of Amazon SageMaker AI resource](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/ "https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/")
- [Create
  a hosting VPC for PyPi package mirroring and consumption
  of approved packages](https://sagemaker-workshop.com/security_for_sysops/best_practice/best_practice_lab.html "https://sagemaker-workshop.com/security_for_sysops/best_practice/best_practice_lab.html")
- [Apply
  fine-grained data access controls with AWS Lake Formation
  and Amazon EMR from Amazon SageMaker AI Studio](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-data-access-controls-with-aws-lake-formation-and-amazon-emr-from-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-data-access-controls-with-aws-lake-formation-and-amazon-emr-from-amazon-sagemaker-studio/")

## Videos

- [Security
  for AI/ML Models in AWS](https://www.youtube.com/watch?v=toDQL_c8Zug "https://www.youtube.com/watch?v=toDQL_c8Zug")
- [AWS re:Invent 2020: Security best practices the AWS
  Well-Architected way](https://www.youtube.com/watch?v=wfIVI-M7lbQ "https://www.youtube.com/watch?v=wfIVI-M7lbQ")

## Examples

- [Secure
  Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture "https://github.com/aws-samples/secure-data-science-reference-architecture")
