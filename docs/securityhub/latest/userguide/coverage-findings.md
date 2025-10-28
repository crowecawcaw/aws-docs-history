# Coverage findings in Security Hub

###### Note

Security Hub is in preview release and is subject to change.

Coverage findings for Security Hub provide visibility into which AWS security features are enabled and where there might be gaps in coverage in a standalone account or across an organization's member accounts.
Enabling additional security features will enhance the detection capabilities of Security Hub.
Coverage Findings evaluate what GuardDuty, Amazon Inspector, Macie, and Security Hub CSPM features are enabled for an account.
These findings appear in the Security Coverage widget on the Security Hub dashboard with the ability to drill down into more detailed views by specific security capability.
For the delegated administrator, this widget shows coverage breakdown across all Security Hub enabled member accounts.

###### Limitations

- For member accounts, coverage information is aggregated across linked AWS Regions, but only for that member account.
- Coverage information is not shown for accounts not onboarded to Security Hub

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
