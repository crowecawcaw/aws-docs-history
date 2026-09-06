

# Security Hub recommendations
<a name="securityhub-v2-recommendations"></a>

 The following security services in AWS send findings to Security Hub in the OCSF format. After you enable Security Hub, enable these AWS services for additional security. 

**Security Hub CSPM**  
 When you [enable Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html), you get a comprehensive view of your security state in AWS. This helps you assess your environment against security industry standards and best practices. Although you can get started with Security Hub without enabling Security Hub CSPM, enabling Security Hub CSPM allows Security Hub to correlate security signals from Security Hub CSPM to improve your posture management. 

 If you [enable Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html), we also recommend [enabling the AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/enable-standards.html) for your account. This standard consists of a set of controls that detect when your AWS accounts and resources deviate from security best practices. When you enable the AWS Foundational Security Best Practices standard for your account, AWS Security Hub CSPM automatically enables all of its controls, including controls for the following resource types: 
+  Account controls 
+  Amazon DynamoDB controls 
+  Amazon Elastic Compute Cloud controls 
+  AWS Identity and Access Management (IAM) controls 
+  AWS Lambda controls 
+  Amazon Relational Database Service (Amazon RDS) controls 
+  Amazon Simple Storage Service controls 

 You can disable any of the controls in this list. However, if you disable any of these controls, you cannot receive exposure findings for supported resources. For information about controls that apply to the AWS Foundational Security Best Practices standard, see [AWS Foundational Security Best Practices v1.0.0 (FSBP) standard](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html). 

**GuardDuty**  
 When you [enable GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html), you can view all of your threats and security coverage findings in the dashboard of the Security Hub console. If you enable GuardDuty, GuardDuty automatically begins sending data to Security Hub in the OCSF format. 

**Amazon Inspector**  
 When you [enable Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html), you can view all of your exposures and security coverage findings in the dashboard of the Security Hub console. If you enable Amazon Inspector, Amazon Inspector automatically begins sending data to Security Hub in the OCSF format. 

 We recommend activating Amazon EC2 scanning and Lambda standard scanning. When you activate Amazon EC2 scanning, Amazon Inspector scans Amazon EC2 instances in your account for package vulnerabilities and network reachability issues. When you activate Lambda standard scanning, Amazon Inspector scans Lambda functions for software vulnerabilities in package dependencies. For more information, see [Activating a scan type](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html) in the *Amazon Inspector User Guide*. 

**Macie**  
 When you [enable Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html), you can detect additional exposures for your Amazon S3 buckets. We recommend configuring [automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-enable.html), so Macie can evaluate your Amazon S3 bucket inventory on a daily basis. 