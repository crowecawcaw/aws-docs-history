# AMS infrastructure automatic tagging

AMS can tag all resources created by AMS for management purposes,
in your multi-account landing zone (MALZ) and single-account landing zone (SALZ) accounts through a request for change (RFC) with the Deployment | Advanced stack components | Tag | Create (managed automation)
change type (ct-0176f0n99vcps). This can help you in identifying resources created by AMS for management purposes.

AMS can automatically identify AMS-created resources based on the naming
standards and check if the resource has the following tag keys and values - "AppName", "AppId",
"AMSResource", and "EnvironmentType". If the tag key does not exist, or the value is empty, those tag-keys can
be created automatically by AMS with tag-value "AMSInfrastructure".

You can customize the tags you want on AMS-created resources based on your organization's tagging
standards. You can include your own tag-keys and tag-values when
you submit the request to AMS. Follow these AWS tag naming standards: 
[Tagging Best Practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf")

###### Note

For MALZ accounts, custom tagging of AMS infrastructure is supported on Application accounts only. Custom tagging on core accounts is currently not supported.

If the tag-key name you provide in your RFC, already exists on the
resource, then the tag-value gets replaced with the new tag-value that you provided in the RFC. 

Total length of tag key:value pairs must not exceed 256 characters.

Include the following information in your RFC with the Deployment | Advanced stack components | Tag | Create (managed automation) change type (ct-0176f0n99vcps) for tagging AMS-created resources.

1. List of multi-account landing zone or single-account landing zone accounts where you would like to tag AMS-created resources for management
   purposes.
2. Required tag-key name and tag-value (if needed). By default,
   AMS can tag with tag-key name as "EnvironmentType" and tag-value as "AMSInfrastructure". If you need a custom
   tag-key name and tag-value, follow AWS tag naming standards: 
   [Tagging Best Practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf")

These resources are currently supported by AMS infrastructure tagging: 

```

    API Gateway
    Amazon CloudFront
    Amazon DynamoDB
    Amazon EBS
    Amazon EC2
    Amazon OpenSearch Service
    Amazon Quantum Ledger Database (QLDB)
    Amazon Redshift
    Amazon RDS
    Amazon S3 (specific buckets only*)
    Amazon Simple Queue Service (SQS)
    Amazon Simple Notification Service (SNS)
    Amazon VPC
    AWS Certificate Manager
    AWS CloudFormation
    AWS CloudTrail
    AWS CodeBuild
    AWS CodePipeline
    AWS Elastic Beanstalk
    AWS Lambda
    AWS Secrets Manager
    AWS Service Catalog
    AWS Systems Manager
    AWS WAF Regional
    Elastic Load Balancing
```

**\***   "arn:aws:s3:::awsms-a\*-patch-data-\*",
"arn:aws:s3:::ams-a\*-log-management-\*",
"arn:aws:s3:::cf-templates-\*",
"arn:aws:s3:::mc-a\*",
"arn:aws:s3:::ams-a\*-backup-reports-\*",
"arn:aws:s3:::ams-a\*-patch-data-customer-reports-\*",
"arn:aws:s3:::ams-a\*-patch-data-raw-\*",
"arn:aws:s3:::ams-a\*-patch-data-reporting-\*",
"arn:aws:s3:::ams-a\*-release-assets-\*",
"arn:aws:s3:::ams-cfn-drift-remediation-\*",
"arn:aws:s3:::ams-reporting-data-a\*"
