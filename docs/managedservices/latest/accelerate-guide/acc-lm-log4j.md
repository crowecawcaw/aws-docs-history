# Use the Log4j SSM Document to discover occurrences in Accelerate

The Log4j AWS Systems Manager document (SSM document) assists you with searching for the Apache Log4j2 library within ingested workloads.
The automation document provides a report of the Process ID of the Java application(s) that the Log4j2 library is active in.

The report includes information about the Java Archives (JAR Files), found within the specified environment that contains the JndiLookup class.
It's a best practice to upgrade the discovered libraries to the latest available version. This upgrade mitigates the Remote Code Execution (RCE) identified through CVE-2021-44228.
Download the latest version of the Log4j library from Apache. For more information, see
[Download Apache Log4j 2](https://logging.apache.org/log4j/2.x/download.html "https://logging.apache.org/log4j/2.x/download.html").

The document is shared to all the Regions onboarded to Accelerate,. To access the document, complete the following steps:

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Documents**.
3. Choose **Shared with me**.
4. In the search box, enter **AWSManagedServices-GatherLog4jInformation**.
5. Use [rate control](../../../systems-manager/latest/userguide/automation-working-targets-and-rate-controls.md "../../../systems-manager/latest/userguide/automation-working-targets-and-rate-controls.md") to run the document at scale.
   The AWSManagedServices-GatherLog4jInformation document gathers the following parameters:

- **InstanceId**: (Required) ID of your EC2 instance.
- **S3Bucket**: (Optional) The S3 pre-signed URL or S3 URI (s3://BUCKET_NAME) to upload the results to.
- **AutomationAssumeRole**: (Required) The ARN of the role that allows the autoomation to perform actions on your behalf.
  It's a best practice to run this document using rate control. You can set the rate control parameter to be the **InstanceId**, and assign either a
  list of instances to it, or apply a tag-key combination to target all EC2 instances that have a certain tag. AWS Managed Services also recommends that you provide
  an Amazon Simple Storage Service (Amazon S3) bucket to upload the results to, so that you can build a report from the data stored in S3.
  For an example of how to aggregate the results in S3, see
  [EC2 Instance Stack | Gather Log4j Information](../ctref/management-advanced-ec2-instance-stack-gather-log4j-information.md "../ctref/management-advanced-ec2-instance-stack-gather-log4j-information.md").

If you are unable to upgrade the package, follow the guidelines outlined by AWS Security at
[Using AWS security services to protect against, detect, and respond to the Log4j vulnerability](https://aws.amazon.com/blogs/security/using-aws-security-services-to-protect-against-detect-and-respond-to-the-log4j-vulnerability/ "https://aws.amazon.com/blogs/security/using-aws-security-services-to-protect-against-detect-and-respond-to-the-log4j-vulnerability/").
To mitigate vulnerabilities by removing the JndiLookup class functionality, run the Log4j hot patch inline with your Java application(s). For more information about the hot patch, see
[Hotpatch for Apache Log4j](https://aws.amazon.com/fr/blogs/opensource/hotpatch-for-apache-log4j/ "https://aws.amazon.com/fr/blogs/opensource/hotpatch-for-apache-log4j/").

For questions about the output of the automation or how to proceed with additional mitigations, submit a service request.
