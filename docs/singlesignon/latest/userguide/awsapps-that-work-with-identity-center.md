# AWS managed applications
 that you can use with IAM Identity Center

IAM Identity Center lets you connect your existing identity source or create users once. This 
 enables application administrators to manage access to the following AWS managed
 applications without separate federation or user and group synchronization. 

All of the AWS managed applications in the following table integrate with [organization instances of IAM Identity Center](organization-instances-identity-center.md "organization-instances-identity-center.md"). The table also provides information about the following for a supported AWS managed application:


* Whether the application also integrates with account instances of IAM Identity Center
* Whether the application can enable trusted identity propagation through IAM Identity Center
* Whether the application supports IAM Identity Center configured with a customer managed KMS key


AWS managed applications that integrate with IAM Identity Center| AWS managed application | Integrated with [account instances of IAM Identity Center](account-instances-identity-center.md "account-instances-identity-center.md") | Enables [trusted identity propagation](trustedidentitypropagation-overview.md "trustedidentitypropagation-overview.md") through IAM Identity Center | Supports IAM Identity Center configured with a [customer managed KMS key](encryption-at-rest.md "encryption-at-rest.md") |
| --- | --- | --- | --- |
| Amazon AppStream 2.0 |  No |  No |  No |
| Amazon Athena SQL |  Yes |  Yes |  Yes |
| Amazon CodeCatalyst |  Yes |  No |  No |
| Amazon Connect |  No |  No |  No |
| Amazon DataZone |  Yes |  Yes |  No |
| Amazon EMR on Amazon EC2 |  Yes |  Yes |  Yes |
| Amazon EMR Studio |  Yes |  Yes |  Yes |
| Amazon Kendra |  No |  No |  Yes |
| Amazon Managed Grafana |  No |  No |  No |
| Amazon Monitron |  No |  No |  No |
| Amazon OpenSearch Service |  Yes |  Yes |  No |
| Amazon OpenSearch Service Serverless Service |  Yes |  Yes |  Yes |
| OpenSearch user interface (Dashboards) |  Yes |  Yes |  Yes |
| Amazon Q Business |  Yes |  Yes |  Yes |
| Amazon Q Developer |  Yes\* |  No |  No |
| Amazon Quick Suite |  Yes |  Yes |  Yes |
| Amazon Redshift |  Yes |  Yes |  No |
| Amazon S3 Access Grants |  Yes |  Yes |  No |
| Amazon SageMaker Unified Studio |  Yes |  Yes |  Yes |
| Amazon SageMaker Studio |  No |  Yes |  No |
| Amazon WorkMail |  Yes |  Yes |  Yes |
| Amazon WorkSpaces |  Yes |  No |  No |
| Amazon WorkSpaces Secure Browser |  No |  No |  Yes |
| AWS App Studio |  Yes |  No |  No |
| AWS Client VPN |  No |  No |  No |
| AWS CLI |  No |  No |  No |
| AWS Deadline Cloud |  Yes |  No |  No |
| AWS Glue |  Yes |  Yes |
| AWS IoT Events |  No |  No |  No |
| AWS IoT Fleet Hub |  No |  No |  No |
| AWS IoT SiteWise |  No |  No |  No |
| AWS Lake Formation |  Yes |  Yes |  No |
| AWS re:Post Private |  Yes |  No |  No |
| AWS Supply Chain |  Yes |  No |  No |
| AWS Systems Manager |  No |  No |  Yes |
| AWS Transfer Family web apps |  Yes |  Yes |  No |
| AWS Transform |  Yes |  No |  Yes |
| AWS Verified Access |  No |  No |  Yes |
| Multi-party approval |  No |  Yes |  Yes | \* For Amazon Q Developer, account instances of IAM Identity Center are supported unless your users require access to the full set of Amazon Q Developer features on AWS websites. For more information, see [Setting up Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-q-dev.html "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-q-dev.html") in the *Amazon Q Developer User Guide*.
