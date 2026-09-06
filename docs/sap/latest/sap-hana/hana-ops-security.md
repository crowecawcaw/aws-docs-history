

# Security
<a name="hana-ops-security"></a>

Here are additional AWS security resources to help you achieve the level of security you require for your SAP HANA environment on AWS.
+  [AWS Cloud Security Center](https://aws.amazon.com/security/) 
+  [CIS AWS Foundations Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html) 
+  [Introduction to AWS Security](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html) 
+  [AWS Well-Architected Framework – Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 

## OS Hardening
<a name="hana-ops-os-hardening"></a>

You may want to lock down the OS configuration further, for example, to avoid providing a DB administrator with root credentials when logging into an instance.

You can also refer to the following SAP notes:
+  [1730999](https://me.sap.com/notes/1730999): *Configuration changes in HANA appliance* 
+  [1731000](https://me.sap.com/notes/1731000): *Unrecommended configuration changes* 

## Disabling HANA Services
<a name="hana-ops-disabling-services"></a>

HANA services such as HANA XS are optional and should be deactivated if they are not needed. For instructions, see [SAP Note 1697613](https://me.sap.com/notes/1697613): *Remove XS Engine out of SAP HANA database*. In case of service deactivation, you should also remove the TCP ports from the SAP HANA AWS security groups for complete security.

## API Call Logging
<a name="hana-ops-api-logging"></a>

 [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service.

With CloudTrail, you can get a history of AWS API calls for your account, including API calls made via the AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as AWS CloudFormation). The AWS API call history produced by CloudTrail enables security analysis, resource change tracking, and compliance auditing.

## Notifications on Access
<a name="hana-ops-notifications"></a>

You can use [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) or third-party applications to set up notifications on SSH login to your email address or mobile phone.