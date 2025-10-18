# AWS CloudHSM PCI-PIN compliance FAQs

PCI PIN provides security requirement and assessment standards for transmitting, processing, and managing personal identification number (PIN) data, information that is used for transactions at ATMs and point-of-sale (POS) terminals.

The PCI-PIN Attestation of Compliance (AOC) and Responsibility Summary is available to customers through AWS Artifact, a self-service portal for on-demand access to AWS compliance reports. For more information, 
 sign in to [AWS Artifact in the AWS Management Console](https://console.aws.amazon.com/artifact "https://console.aws.amazon.com/artifact"), or learn more at [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").


## FAQs


**Q: What is the Attestation of Compliance and Responsibility Summary?**


Attestation Of Compliance (AOC) is produced by a Qualified PIN Assessor (QPA) attesting AWS CloudHSM meets the applicable controls in the PCI-PIN standard. 
 The responsibility summary matrix describes the controls which are the respective responsibilities of AWS CloudHSM and its customers.


**Q: How do I obtain the AWS CloudHSM Attestation of Compliance?**


The PCI-PIN Attestation of Compliance (AOC) is available to customers through AWS Artifact, a self-service portal for on-demand access to AWS compliance reports. For more information, 
 sign in to [AWS Artifact in the AWS Management Console](https://console.aws.amazon.com/artifact "https://console.aws.amazon.com/artifact"), or learn more at [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").


**Q: How can I learn which PCI PIN controls I am responsible for?**


For detailed information please see "AWS CloudHSM PCI PIN Responsibility Summary" from the AWS PCI PIN Compliance Package, available to customers through AWS Artifact, a self-service portal for on-demand access to AWS compliance reports.
 For more information, sign in to [AWS Artifact in the AWS Management Console](https://console.aws.amazon.com/artifact "https://console.aws.amazon.com/artifact"), or learn more at [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").


**Q: As an AWS CloudHSM customer, can I rely on PCI-PIN Attestation of Compliance (AOC)?** 


Customers must manage their own PCI-PIN compliance. You are required to go through a formal PCI-PIN attestation process through a Qualified PIN Assessor (QPA) to verify that your payment workload satisfies all PCI-PIN controls/requirements. 
 However, for the controls which AWS is responsible for, your QPA can rely on AWS CloudHSM Attestation of Compliance (AOC) without further testing.


**Q: Is AWS CloudHSM responsible for PCI-PIN requirements related to Key Management Life cycle?**


AWS CloudHSM is responsible for the physical device lifecycle of the HSMs. Customers are responsible for the key management life cycle requirements in the PCI-PIN standard.


**Q: Which AWS CloudHSM controls are PCI-PIN compliant?**


The AOC summarizes the AWS CloudHSM controls which are assessed by QPA. The PCI-PIN Responsibility Summary is available to customers through AWS Artifact, a self-service portal for on-demand access to AWS compliance reports.


**Q: Does AWS CloudHSM support payment functions such as PIN translation and DUKPT?**


No, AWS CloudHSM provides general purpose HSMs. Over time we may provide payment functions. Although the service does not perform payment functions directly, the AWS CloudHSM PCI PIN attestation of compliance enables customers 
 to attain their own PCI compliance for their services running on AWS CloudHSM. If you are interested in using AWS Payment Cryptography services for your workload, please refer to 
 the blog ["Move Payment Processing to the Cloud with AWS Payment Cryptography."](https://aws.amazon.com/blogs/aws/new-move-payment-processing-to-the-cloud-with-aws-payment-cryptography/ "https://aws.amazon.com/blogs/aws/new-move-payment-processing-to-the-cloud-with-aws-payment-cryptography/")
