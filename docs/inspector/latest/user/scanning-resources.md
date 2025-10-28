# Automated scan types in Amazon Inspector

Amazon Inspector uses a purpose-built scanning engine that monitors your resources for actionable software vulnerabilities and unintended network exposure.
When Amazon Inspector detects a software vulnerability or unintended network exposure, it creates a [finding](findings-understanding.md "findings-understanding.md").
When you activate Amazon Inspector for the first time, your account is automatically enrolled in [all scan types](scanning-resources.md#scan-types "scanning-resources.md#scan-types"), which include Amazon Amazon EC2 scanning, Amazon ECR Scanning, and Lambda standard scanning.

###### Note

Lambda code scanning is an optional layer of Lambda function scanning that you can activate at any time.

###### Topics

- [Overview of Amazon Inspector scan types](#scan-types "#scan-types")
- [Activating a scan type](activate-scans.md "activate-scans.md")
- [Scanning Amazon EC2 instances with Amazon Inspector](scanning-ec2.md "scanning-ec2.md")
- [Scanning Amazon Elastic Container Registry container images with Amazon Inspector](scanning-ecr.md "scanning-ecr.md")
- [Scanning AWS Lambda functions with Amazon Inspector](scanning-lambda.md "scanning-lambda.md")
- [Deactivating a scan type in Amazon Inspector](deactivate-scans.md "deactivate-scans.md")

## Overview of Amazon Inspector scan types

Amazon Inspector provides different scan types, which focus on specific resource types in your AWS environment.

**Amazon EC2 scanning**

When you activate Amazon EC2 scanning, Amazon Inspector scans your EC2 instances for common vulnerabilities and exposures (CVEs), network exposure issues, network reachability issues, operating system and programming language package vulnerabilities.
Amazon Inspector performs scans through the use of the SSM agent installed on your instance or through Amazon EBS snapshots of instances.
For more information, see [Scanning Amazon EC2 instances with Amazon Inspector](scanning-ec2.md "scanning-ec2.md").
By default, when you activate Amazon EC2 scanning, you automatically enable hybrid scanning mode.
For more information, see [Agentless scanning](scanning-ec2.md#agentless "scanning-ec2.md#agentless").

**Amazon ECR scanning**

When you activate Amazon ECR scanning, Amazon Inspector converts all of the repositories in your private registry from basic scanning container repositories to enhanced scanning repositories.
You can configure this setting with inclusion rules to scan on-push only or to scan select repositories.
Amazon Inspector scans all images pushed within the last 30 days or pulled within the last 90 days.
Amazon Inspector continues to monitor images for 90 days by default.
You can change this setting at any time.
For more information, see [Scanning Amazon Elastic Container Registry container images with Amazon Inspector](scanning-ecr.md "scanning-ecr.md").

**Lambda standard scanning**

When you activate Lambda standard scanning, Amazon Inspector discovers all of the Lambda functions in your account and immediately scans them for vulnerabilities.
Amazon Inspector scans new Lambda functions and layers when they're deployed.
Amazon Inspector rescans them when they're updated or when new CVEs are published.
For more information, scanning, see [Scanning AWS Lambda functions with Amazon Inspector](scanning-lambda.md "scanning-lambda.md").

**Lambda standard scanning + Lambda code scanning**

When you activate Lambda code scanning, Amazon Inspector discovers the Lambda functions and layers in your account and scans them for code vulnerabilities.
This type of scanning evaluates application package dependencies used in a Lambda function for CVEs.
When you activate this scan type, you also activate Lambda standard scanning.
For more information, see [Scanning AWS Lambda functions with Amazon Inspector](scanning-lambda.md "scanning-lambda.md").

**Code Security for Amazon Inspector**

This scan type leverages the Amazon Q Developer scanning engine to scan first-party application code, third-party application dependencies, and Infrastructure as Code for vulnerabilities
For more information, see [Code Security for Amazon Inspector](code-security-assessments.md "code-security-assessments.md").
