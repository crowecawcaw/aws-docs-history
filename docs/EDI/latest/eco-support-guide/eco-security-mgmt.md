

# Security management for EDI
<a name="eco-security-mgmt"></a>

ECO uses AWS Managed Services (AMS) for security management. AMS uses multiple controls to protect your information assets and to help you keep your AWS infrastructure secure. 

AMS maintains a library of AWS Config Rules and remediation actions so that all your accounts comply with industry standards for security and operational integrity. AWS Config Rules continuously tracks conﬁguration changes in your recorded resources. If a change violates rule conditions, ECO reports its ﬁndings and allows you to automatically remediate violations or request remediation according to its severity. AWS Config Rules facilitate compliance with standards set by the following organizations:
+ [The Center for Internet Security (CIS)](https://www.cisecurity.org/)
+ [The National Institute of Standards and Technology (NIST) Cloud Security Framework (CSF)](https://www.nist.gov/cyberframework)
+ [The Health Insurance Portability and Accountability Act (HIPAA)](https://www.ncbi.nlm.nih.gov/books/NBK500019/)
+ [The Payment Card Industry (PCI) Data Security Standard (DSS)](https://www.pcisecuritystandards.org/standards/)

AMS also uses Amazon GuardDuty to identify potentially unauthorized or malicious activity in your AWS environment. AMS monitors GuardDuty ﬁndings all day and week. AMS collaborates with you to understand the impact of the ﬁndings and identify remediation based on best practice recommendations. 

AMS also uses Amazon Macie to protect your sensitive data such as personal health information (PHI), personally identiﬁable information (PII) and ﬁnancial data.

For more information about security management for an AMS operations plan, see [Security management in AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec.html), in the *AMS Accelerate User guide*.