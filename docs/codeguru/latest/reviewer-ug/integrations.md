Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Product and service integrations

By default, Amazon CodeGuru Reviewer is integrated with the following products and services. The
information provided in the following table can help you configure CodeGuru Reviewer to integrate with the
products and services you use.

Products and services that are integrated with Amazon CodeGuru Reviewer| **AWS CloudTrail** | [CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
captures AWS API calls and related events made by or on behalf of an AWS account
and delivers log files to an Amazon S3 bucket that you specify. You can configure CloudTrail to
capture API calls from the CodeGuru Reviewer console, CodeGuru Reviewer commands from the AWS Command Line Interface (AWS CLI),
and from the CodeGuru Reviewer API. |
| **Amazon CloudWatch** | You can use Amazon CloudWatch to monitor the number of recommendations created for your source code in an associated repository over time. For more information, see [Monitoring CodeGuru Reviewer with Amazon CloudWatch](monitoring.md "monitoring.md"). |
| **AWS CodeCommit** | You can configure CodeGuru Reviewer to provide analysis and recommendations for repositories in CodeCommit. For more information about CodeCommit, see the [AWS CodeCommit User Guide](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md"). |
| **CodeConnections** | CodeConnections is a service that allows CodeGuru Reviewer to connect to third-party repository source providers such as Bitbucket. You don't need an CodeConnections account to get analysis and recommendations for repositories. |
| **AWS Secrets Manager** | AWS Secrets Manager is a service that automatically integrates with CodeGuru Reviewer to find unprotected secrets in your code. For more information, see [Secrets detection](recommendations.md#secrets-detection "recommendations.md#secrets-detection") and [Create a secret](../../../secretsmanager/latest/userguide/manage_create-basic-secret.md "../../../secretsmanager/latest/userguide/manage_create-basic-secret.md") in the _AWS Secrets Manager User Guide_. |
| **Bitbucket** | You can configure CodeGuru Reviewer to [provide analysis and recommendations for repositories in Bitbucket](create-bitbucket-association.md "create-bitbucket-association.md"). To do this, you must have created a Bitbucket account and at least one Bitbucket repository. |
| **GitHub** | You can configure CodeGuru Reviewer to [provide analysis and recommendations for repositories in GitHub](create-github-association.md "create-github-association.md"). To do this, you must have created a GitHub account and at least one GitHub repository. |
| **GitHub Enterprise Cloud** | You can configure CodeGuru Reviewer to [provide analysis and recommendations for repositories in GitHub Enterprise Cloud](create-github-association.md "create-github-association.md") in the same way that you would for other GitHub repositories. To do this, you must have created a GitHub Enterprise Cloud organization in your account and at least one repository. |
| **GitHub Enterprise Server** | You can configure CodeGuru Reviewer to [provide analysis and recommendations for repositories in GitHub Enterprise Server](create-github-enterprise-association.md "create-github-enterprise-association.md"). To do this, you must have created a GitHub Enterprise Server account and at least one repository. You should have already configured your network or virtual private cloud (VPC). You also must already have created your instance and, if you plan to connect with your VPC, launched your instance into your VPC. |
