

# SEC07-BP03 Automate identification and classification

 Automating identification and classification finds sensitive data, confirms that the right controls apply, and flags data stored or handled in unauthorized ways. Apply it before data reaches production and continually in running environments. 

 **Desired outcome:** 
+  You can verify whether the correct controls are in place for the sensitivity of each data set. 
+  Your automated tools identify and classify the sensitivity level of your data. 
+  Your environments are continuously monitored, and you are alerted when data is stored or handled in unauthorized ways so you can act quickly. 

 **Common anti-patterns:** 
+  Teams rely solely on manual processes to identify and classify data, which is slow and error-prone as data volumes grow. 
+  Organizations have no mechanism to track and manage data assets across the environment. 
+  Teams classify data once and overlook the need to monitor and reclassify it as it moves and changes. 

 **Benefits of establishing this best practice:** 
+  Data protection controls apply more consistently, because classification no longer depends on manual effort. 
+  Human error in classifying data drops. 
+  Visibility into sensitive data access and movement improves, so unauthorized handling is detected and corrected. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Before data reaches production, scan representative or test data to learn its sensitivity and catch protection gaps. Build this into unit and integration tests so a build fails when sensitive data turns up where it was not expected. Load data sets into [Amazon S3](https://aws.amazon.com/s3/) and scan them with [Amazon Macie](https://aws.amazon.com/macie/), [Amazon Comprehend](https://aws.amazon.com/comprehend/), or [Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/). Sensitive data detection in [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html), [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-managed-data-identifiers.html), and [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) identifies personally identifiable information and takes mitigating action. 

 No tool defines sensitive data exactly the way your policy does. Each tool ships with its own detectors, and the data that matters to your organization may not match. Understand how a tool decides what is sensitive, then augment it with additional detectors or human review for the cases it misses. 

 Ongoing monitoring catches sensitive data stored in non-compliant ways. Examples include data emitted into log files or copied into an analytics environment without redaction. A full scan gives the most complete picture at the greatest cost, so sampling is often the right first pass. Reserve a deeper scan for the stores that warrant it. Use [Amazon Macie](https://aws.amazon.com/macie/) for ongoing monitoring of stores such as [Amazon S3](https://aws.amazon.com/s3/). Its [automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) samples objects across your buckets, so you get sensitivity coverage without scanning every object. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Align automation to your classification scheme:** Review your organization's data classification scheme, described in [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md), so your automated identification and classification match your policies. 

1.  **Run an initial scan of your environments:** Perform a broad scan to understand where sensitive data resides. Where a full scan is too costly up front, use sampling to produce a preliminary view, then run a deeper scan on the data stores that need it. Apply the access controls from [SEC07-BP02 Apply data protection controls based on data sensitivity](sec07-bp02.md) to the resources you find. 

1.  **Configure ongoing scans:** Schedule continuous scans to detect newly stored sensitive data. Exclude the stores that are authorized to hold sensitive data using an allow list, so alerts focus on the unexpected. 

1.  **Build classification into your development and test pipeline:** Give developers tools to scan data for sensitivity during development, and run those scans in integration testing to block deployment when sensitive data appears where it does not belong. 

1.  **Act automatically when data is found in the wrong place:** Define a runbook or automated remediation that restricts access to misplaced sensitive data, such as moving it to a restricted location, tagging it for attribute-based access control, or masking it. Alert your data protection and incident response teams to investigate the root cause. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 
+  [SEC07-BP02 Apply data protection controls based on data sensitivity](sec07-bp02.md) 
+  [SEC07-BP04 Define scalable data lifecycle management](sec07-bp04.md) 

 **Related documents:** 
+  [AWS Glue: detect and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html) 
+  [Using managed data identifiers in Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-managed-data-identifiers.html) 
+  [Amazon CloudWatch Logs: help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) 

 **Related tools:** 
+  [Amazon Macie](https://aws.amazon.com/macie/) 
+  [Amazon Comprehend](https://aws.amazon.com/comprehend/) 
+  [Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 