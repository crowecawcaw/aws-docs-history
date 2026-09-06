

# Getting started with AWS Certificate Manager certificates
<a name="gs"></a>

ACM manages public, private, and imported certificates. Certificates are used to establish secure communications across the internet or within an internal network. You can request a publicly trusted certificate directly from ACM (an "ACM certificate"), import a publicly trusted certificate issued by a third party. Self-signed certificates are also supported. To provision your organization's internal PKI, you can issue ACM certificates signed by a private certificate authority (CA) created and managed by [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html). The CA may either reside in your account or be shared with you by a different account. 

You can also automate public certificate issuance using the Automated Certificate Management Environment (ACME) protocol for workloads running on customer-managed infrastructure. For more information, see [ACME certificate automation](acm-acme.md).

**Note**  
To automate public certificate issuance and renewal outside integrated services such as on Amazon EC2 instances, use the ACME protocol. For more information, see [ACME certificate automation](acm-acme.md). Alternatively, if you cannot use ACME, you can automate exportable certificates issued from ACM through [AWS Workload Credentials Provider](acm-certificate-automation.md).

**Note**  
Because certificates signed by a private CA are not trusted by default, administrators must install them in client trust stores.

To begin issuing certificates, sign into the AWS Management Console and open the ACM console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home). If the introductory page appears, choose **Get Started**. Otherwise, choose **Certificate Manager** or **Private CAs** in the left navigation pane. 

**Topics**
+ [Set up to use AWS Certificate Manager](setup.md)