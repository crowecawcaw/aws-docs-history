# Coverage findings in Security Hub

###### Note

Security Hub is in preview release and is subject to change.

Coverage findings for Security Hub provide visibility into which AWS security features are enabled and where there might be gaps in coverage in a standalone account or across an organization's member accounts.
Coverage Findings currently support reporting which services and features are enabled for Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Security Hub CSPM.
These findings appear in the Security Coverage widget on the Security Hub dashboard with the ability to drill down into more detailed views by specific security capability.

###### Limitations

- For member accounts, coverage information is aggregated across linked AWS Regions, but only for that member account.
- Coverage information is not shown for accounts not onboarded to Security Hub.

## Coverage findings for AWS Security Hub CSPM

Security Hub CSPM Coverage Findings assess whether a qualified posture management security standard is enabled in an account.
Enabling any Security Hub CSPM Standard will qualify, with the exception of AWS Control Tower and Resource Tagging standards.

It can take up to 24 hours to detect standards enabled by default when enabling Security Hub CSPM.

## Coverage findings for Amazon GuardDuty

GuardDuty coverage findings assess whether GuardDuty is enabled and which GuardDuty features are enabled in an AWS account:

- GuardDuty Malware Protection for Amazon EC2 – Scans Amazon EC2 instances for potential malware
- GuardDuty Amazon EKS Protection – Monitors Kubernetes audit logs for threats in Amazon EKS clusters
- GuardDuty Lambda Protection – Analyzes Lambda function invocations for potential threats
- GuardDuty Amazon S3 Protection – Analyzes data events for potential threats to Amazon S3 buckets
- GuardDuty Amazon RDS Protection – Monitors for threats to Amazon RDS databases
- GuardDuty Runtime Monitoring – Provides real-time monitoring of runtime behavior in Amazon EC2 instances
- GuardDuty Foundational Coverage – Baseline GuardDuty features which are automatically turned on when GuardDuty is enabled

###### Note

For GuardDuty Foundational Coverage, coverage findings that indicate the feature is turned off mean GuardDuty is not enabled in the account for the coverage finding.

It can take up to 24 hours for updates to GuardDuty coverage to reflect across all member accounts in an organization.

## Coverage findings for Amazon Inspector

Amazon Inspector coverage findings assess whether Amazon Inspector is enabled and which features are enabled in an account:

- Inspector EC2 Scanning – Scans Amazon EC2 instances for vulnerabilities
- Inspector ECR Scanning – Scans Amazon ECR container images for vulnerabilities
- Inspector Lambda Standard Scanning – Scans Lambda functions for vulnerabilities
- Inspector Lambda Code Scanning – Scans Lambda code functions for code vulnerabilities

## Coverage findings for Amazon Macie

Macie coverage findings assess whether Macie is enabled across AWS accounts:

- Macie Automated Sensitive Data Discovery Coverage – Continuously evaluates your Amazon S3 data estate for sensitive data.

It can take up to 24 hours for updates to Macie automated sensitive data discovery for coverage findings to reflect across all member accounts in an organization.

## Suppressing coverage findings

By default, security coverage findings evaluate which Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Security Hub CSPM features are enabled for an account and Region.
If certain security capabilities are not applicable for you or are an accepted risk, you can use the suppression feature to suppress coverage findings similar to all other findings.
When a coverage finding is suppressed it will not be included in the coverage calculations within security coverage widget and the widget will display a message of _Coverage for security capabilities has been excluded through suppressed coverage findings_ followed by a count of how many findings have been suppressed.

###### To suppress a coverage finding in Security Hub

1. When viewing the security coverage widget choose the **percent covered** link.
2. From the coverage popup choose **View coverage findings**. Each finding with a status of **New** will be a finding that outlines an observed coverage gap.
3. Click the checkbox next to each finding that you would like to suppress.
4. At the top of the page, choose **Update status**, and then choose **Suppressed**.
5. In the **Set status to Suppressed** dialog box, optionally enter a note that details the reason for changing the status. Then choose **Set status**.
