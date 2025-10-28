# Working with the dashboard in Amazon Inspector

The dashboard provides a snapshot of aggregated statistics for resources that Amazon Inspector scans.
Use the dashboard to learn about coverage for your environment and critical findings.

###### Note

If your account is the delegated administrator account for an organization, the dashboard shows information for your account and every other account in the organization.

This topic describes how to view the dashboard and understand the components that make up the dashboard.

###### Topics

- [Viewing the dashboard](#displaying-the-dashboard "#displaying-the-dashboard")
- [Understanding dashboard components and interpreting data](#understanding-dashboard-components "#understanding-dashboard-components")

## Viewing the dashboard

The dashboard shows an overview of the coverage for your environment and critical findings.
The dashboard refreshes data automatically every five minutes.
You can refresh data manually by choosing the refresh icon near the top-right corner of the screen.
You can view supporting data for an item by choosing the item.

###### Note

If your account is the delegated administrator account for an organization, you can view aggregated statistics for a member account by entering the member account ID in the **Account** field.

**To view the dashboard:**

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Dashboard**.

## Understanding dashboard components and interpreting data

Each section of the dashboard provides insight into key metrics and findings data, so you can understand the vulnerability posture of your AWS resources in your current AWS Region.

**Environment coverage**

The **Environment coverage** section provides statistics
about the resources scanned by Amazon Inspector. In this section, you can see the count
and percentage of Amazon EC2 instances, Amazon ECR images and AWS Lambda functions scanned
by Amazon Inspector. If you manage multiple accounts through AWS Organizations as an Amazon Inspector
delegated administrator, you will also see the total number of organization
accounts, the number with Amazon Inspector activated, and the resulting coverage
percentage for the organization. You can also use this section to determine
which resources are not covered by Amazon Inspector. These resources may contain
vulnerabilities that could be exploited to put your organization at risk.
For more details, see [Assessing Amazon Inspector coverage of your AWS environment](assessing-coverage.md "assessing-coverage.md").

Choosing a coverage group takes you to the **Account
management** page for the grouping you select. The account
management page shows you details about which accounts, Amazon EC2 instances, and
Amazon ECR repositories are covered by Amazon Inspector.

The following coverage groups are available:

- Account
- Instances
- Container repositories
- Container images
- Lambda

**Critical findings**

The **Critical findings** section provides a count of the
critical vulnerabilities in your environment and a total count of all
findings in your environment. In this section, the counts are shown per
resource and assessment type. For more information about critical findings
and how Amazon Inspector determines criticality, see [Understanding Amazon Inspector findings](findings-understanding.md "findings-understanding.md").

Choosing a critical finding group takes you to the **All
findings** page and automatically applies filters to show all
critical findings that match the grouping you selected.

The following critical finding groups are available:

- Amazon Inspector code scan findings
- Amazon EC2 instance findings
- Amazon ECR container image findings
- Lambda function findings

**Risk-based remediations**

The **Risk-based remediations** section shows the top
five software packages with critical vulnerabilities that affect the most
resources in your environment. Remediating these packages can significantly
reduce the number of critical risks to your environment. Choose the software
package name to see associated vulnerability details and affected resources.

**Accounts with the most critical
findings**

The **Accounts with the most critical findings** section
shows the top five AWS accounts in your environment with the most critical
findings, and the total number of findings for that account. This section is
only viewable from the delegated administrator account when Amazon Inspector is
configured for multi-account scanning with AWS Organizations. This view helps
delegated administrators understand which accounts may be most at risk
within the organization.

Choose **Account ID** to see more information about the
affected member account.

**Amazon ECR repositories with most critical
findings**

The **Elastic Container Registry (ECR) Repositories with most
critical findings** section shows the top five Amazon ECR
repositories in your environment with the most critical container image
findings. The view shows the repository name, AWS account identifier, the
repository creation date, number of critical vulnerabilities, and total
number of vulnerabilities. This view helps you identify which repositories
may be most at risk.

Choose **Repository name** to see more information about
the affected repository.

**Container images with most critical
findings**

The **Container images with most critical findings**
section shows the top five container images in your environment with the
most critical findings. The view shows image tag data, repository name,
image digest, AWS account identifier, number of critical vulnerabilities,
and total number of vulnerabilities. This view helps application owners
identify which container images may need to be rebuilt and
relaunched.

Choose **Container image** to see more information about
the affected container image.

**Instances with most critical findings**

The **Instances with most critical findings** section
shows the top five Amazon EC2 instances with the most critical findings. The view
shows instance identifier, AWS account identifier, Amazon Machine Image
(AMI) identifier, number of critical vulnerabilities, and total number of
vulnerabilities. This view helps infrastructure owners identify which
instances may require patching.

Choose **Instance ID** to see more information about the
affected Amazon EC2 instance.

**Amazon Machine Images (AMI) with most critical
findings**

The **Amazon Machine Images (AMIs) with most critical
findings** section shows the top five AMIs in your environment
with the most critical findings. The view shows the AMI identifier, AWS
account identifier, number of affected EC2 instances running in the
environment, the AMI creation date, the operating system platform of the
AMI, the number of critical vulnerabilities, and the total number of
vulnerabilities. This view helps infrastructure owners identify which AMIs
may require rebuilding.

Choose **Affected instances** to see more information
about the instances launched from the affected AMI.

**AWS Lambda functions with most critical
findings**

The **AWS Lambda functions with most critical findings**
section shows the top five Lambda functions in your environment with the most
critical findings. The view shows the Lambda function name, AWS account
identifier, runtime environment, the number of critical vulnerabilities, the
number of high vulnerabilities, and the total number of vulnerabilities.
This view helps infrastructure owners identify which Lambda functions may require
remediation.

Choose **Function name** to see more information about
the affected AWS Lambda function.

**Amazon Inspector code scans with the most critical findings**

The **Projects with the most critical code vulnerabilities** section shows the top five projects with critical findings.
You can choose a project to view details about the findings.
When you choose a project, you're directed to the repository where the findings are located.
The findings tab shows the names of your findings and their severity ratings.
It shows what type of analysis was used to generate your findings.
It also shows how old your findings are and their statuses.
