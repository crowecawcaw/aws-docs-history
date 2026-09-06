

# Coverage findings in Security Hub
<a name="coverage-findings"></a>

 Coverage findings for Security Hub provide visibility into which AWS security features are enabled and where there might be gaps in coverage in a standalone account or across an organization's member accounts. Coverage findings currently support reporting which services and features are enabled for Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Security Hub CSPM. These findings appear in the Security Coverage widget on the Security Hub dashboard with the ability to drill down into more detailed views by specific security capability. 

**Limitations**
+  For member accounts, coverage information is aggregated across linked AWS Regions, but only for that member account. 
+  Coverage information is not shown for accounts not onboarded to Security Hub. 

## Coverage findings for AWS Security Hub CSPM
<a name="security-hub-v2-coverage-findings-ash"></a>

 Security Hub CSPM coverage findings assess whether a qualified posture management security standard is enabled in an account. Enabling any Security Hub CSPM Standard will qualify, with the exception of AWS Control Tower and Resource Tagging standards. 

 It can take up to 24 hours to detect standards enabled by default when enabling Security Hub CSPM. 

## Coverage findings for Amazon GuardDuty
<a name="security-hub-v2-coverage-findings-gdu"></a>

 GuardDuty coverage findings assess whether GuardDuty is enabled and which GuardDuty features are enabled in an AWS account: 
+  GuardDuty Malware Protection for Amazon EC2 – Scans Amazon EC2 instances for potential malware. 
+  GuardDuty Amazon EKS Protection – Monitors Kubernetes audit logs for threats in Amazon EKS clusters. 
+  GuardDuty Lambda Protection – Analyzes Lambda function invocations for potential threats. 
+  GuardDuty Amazon S3 Protection – Analyzes data events for potential threats to Amazon S3 buckets. 
+  GuardDuty Amazon RDS Protection – Monitors for threats to Amazon RDS databases. 
+  GuardDuty Runtime Monitoring – Provides real-time monitoring of runtime behavior in Amazon EC2 instances. 
+  GuardDuty Foundational Coverage – Baseline GuardDuty features which are automatically turned on when GuardDuty is enabled. 

**Note**  
 For GuardDuty Foundational Coverage, coverage findings that indicate the feature is turned off mean GuardDuty is not enabled in the account for the coverage finding. 

 It can take up to 24 hours for updates to GuardDuty coverage to reflect across all member accounts in an organization. 

## Coverage findings for Amazon Inspector
<a name="security-hub-v2-coverage-findings-ins"></a>

 Amazon Inspector coverage findings assess whether Amazon Inspector is enabled and which features are enabled in an account: 
+  Inspector EC2 Scanning – Scans Amazon EC2 instances for vulnerabilities. 
+  Inspector ECR Scanning – Scans Amazon ECR container images for vulnerabilities. 
+  Inspector Lambda Standard Scanning – Scans Lambda functions for vulnerabilities. 
+  Inspector Lambda Code Scanning – Scans Lambda code functions for code vulnerabilities. 

## Coverage findings for Amazon Macie
<a name="security-hub-v2-coverage-findings-mce"></a>

 Macie coverage findings assess whether Macie is enabled across AWS accounts: 
+  Macie Automated Sensitive Data Discovery Coverage – Continuously evaluates your Amazon S3 data estate for sensitive data. 

 It can take up to 24 hours for updates to Macie automated sensitive data discovery for coverage findings to reflect across all member accounts in an organization. 

## Suppressing coverage findings
<a name="security-hub-v2-coverage-findings-suppress"></a>

 By default, security coverage findings evaluate which Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Security Hub CSPM features are enabled for an account and Region. If certain security capabilities are not applicable for you or are an accepted risk, you can use the suppression feature to suppress coverage findings similar to all other findings. When a coverage finding is suppressed, it is not included in the coverage calculations within the security coverage widget. The widget displays the following message: *Coverage for security capabilities has been excluded through suppressed coverage findings*. The message includes a count of suppressed findings. 

**To suppress a coverage finding in Security Hub**

1.  When viewing the security coverage widget choose the **percent covered** link. 

1.  From the coverage popup choose **View coverage findings**. Each finding with a status of **New** outlines an observed coverage gap. 

1.  Select the check box next to each finding that you want to suppress. 

1.  At the top of the page, choose **Update status**, and then choose **Suppressed**. 

1.  In the **Set status to Suppressed** dialog box, optionally enter a note that details the reason for changing the status. Then choose **Set status**. 