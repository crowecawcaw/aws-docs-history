# Deploy Windows-based stacks using
 CloudFormation

This page provides links to technical reference documentation for CloudFormation resources
 commonly used in Windows-based deployments.

CloudFormation provides support for deploying and managing Microsoft Windows
 stacks through Infrastructure as Code (IaC). You can use CloudFormation for
 automated provisioning of Windows-based EC2 instances, SQL Server on Amazon RDS,
 and Microsoft Active Directory through AWS Directory Service.

AWS provides pre-configured Amazon Machine Images (AMIs) specifically designed for
 Windows platforms to help you quickly deploy applications on Amazon EC2. These AMIs include
 default Microsoft settings and AWS-specific customizations. With CloudFormation, you can
 choose an appropriate AMI, launch an instance, and access it using Remote Desktop Connection,
 just as you would with any other Windows Server. The AMIs contain essential software
 components, including EC2Launch (versions vary by Windows Server edition),
 AWS Systems Manager, CloudFormation, AWS Tools for PowerShell, and various network, storage, and graphics drivers to
 ensure optimal performance and compatibility with AWS services. For more information, see
 the [AWS Windows AMI Reference](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-amis.html "https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-amis.html").

CloudFormation also supports software configuration tools, such as `UserData`
 scripts, which can run PowerShell or batch commands when an EC2 instance first boots up. It
 also offers helper scripts (`cfn-init`, `cfn-signal`,
 `cfn-get-metadata`, and `cfn-hup`) and supports the
 `AWS::CloudFormation::Init` metadata for managing packages, files, and services
 on Windows instances.

For enterprise environments, CloudFormation enables domain joining, Windows license
 management through EC2 licensing models, and secure credential handling with AWS Secrets Manager.
 Combined with version-controlled templates and repeatable deployments, CloudFormation helps
 organizations maintain consistent, secure, and scalable Windows environments across
 multiple AWS Regions and accounts.

For details on CloudFormation resources commonly used in Windows-based deployments, see
 the following technical reference topics.



| Resource type | Description |
| --- | --- |
| [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html") | For launching Windows EC2 instances. |
| [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") | To define firewall rules for Windows workloads. |
| [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")
[AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html") | For scaling Windows EC2 instances. |
| [AWS::DirectoryService::MicrosoftAD](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directoryservice-microsoftad.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directoryservice-microsoftad.html") | For deploying Microsoft Active Directory. |
| [AWS::FSx::FileSystem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-filesystem.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-filesystem.html") | For deploying FSx for Windows File Server. |
| [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") | For provisioning SQL Server on Amazon RDS. |
| [AWS::CloudFormation::Init](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-init.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-init.html") | Used within EC2 metadata for configuring instances. 
For more information, see [Bootstrapping Windows-based
 CloudFormation stacks](cfn-windows-stacks-bootstrapping.md "cfn-windows-stacks-bootstrapping.md"). |
| [AWS::SecretsManager::Secret](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-secretsmanager-secret.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-secretsmanager-secret.html") | For securely managing credentials and Windows passwords. |
| [AWS::SSM::Parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-parameter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-parameter.html") | For storing configuration values securely. |
| [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html")
[AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html") | For granting permissions to applications running on EC2 instances. |
