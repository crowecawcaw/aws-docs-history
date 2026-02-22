# Compliance validation for AWS CloudHSM

For clusters in FIPS mode, AWS CloudHSM provides FIPS-approved HSMs that meet PCI-PIN, PCI-3DS, and SOC2 compliance requirements. AWS CloudHSM also gives customers the option of choosing clusters that are non-FIPS mode.
For details on what certification and compliance requirements apply to each, see [AWS CloudHSM cluster modes](cluster-hsm-types.md "cluster-hsm-types.md").

Relying on a FIPS-validated HSM can help you meet corporate, contractual, and regulatory
compliance requirements for data security in the AWS Cloud.

**FIPS 140-2 Compliance**

The Federal Information Processing Standard (FIPS) Publication 140-2 is a US government security standard that specifies security requirements for cryptographic modules that protect sensitive information.
The AWS CloudHSM hsm1.medium instance type is FIPS 140-2 level 3 certified ([Certificate #4218](https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program/Certificate/4218 "https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program/Certificate/4218")). On January 4, 2026 the certificate for hsm1.medium moves to the historical list. We recommend customers migrate to hsm2m.medium, which is FIPS 140-3 certified ([Certificate #4703](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4703 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4703")).
For more information, refer to [FIPS validation for hardware](https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program "https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program").

**FIPS 140-3 Compliance**

The Federal Information Processing Standard (FIPS) Publication 140-3 is a US government security standard that specifies security requirements for cryptographic modules that protect sensitive information.
The type hsm2m.medium HSMs provided by AWS CloudHSM are FIPS 140-3 level 3 certified ([Certificate #4703](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4703 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4703")).
For more information, refer to [FIPS validation for hardware](https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program "https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program").

**[PCI DSS
Compliance](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/")**

The Payment Card Industry Data Security Standard (PCI DSS) is a proprietary
information security standard administered by the [PCI Security Standards
Council](https://www.pcisecuritystandards.org/ "https://www.pcisecuritystandards.org/"). The HSMs provided by AWS CloudHSM comply with PCI DSS.

**[PCI PIN Compliance](compliance-pci-pin-faqs.md "compliance-pci-pin-faqs.md")**

PCI PIN provides security requirement and assessment standards for transmitting, processing, and managing
personal identification number (PIN) data, information that is used for transactions at ATMs and point-of-sale
(POS) terminals. The hsm1.medium and hsm2m.medium HSMs that are provided by AWS CloudHSM are both PCI PIN compliant. For more information, refer to the article [AWS CloudHSM is now PCI PIN certified](https://aws.amazon.com/blogs/security/aws-cloudhsm-is-now-pci-pin-certified/ "https://aws.amazon.com/blogs/security/aws-cloudhsm-is-now-pci-pin-certified/").

**PCI-3DS Compliance**

PCI 3DS (or Three Domain Secure, 3-D Secure) provides security of data for EMV 3D secure e-commerce payments. PCI 3DS provides another layer of security for online shopping.
The hsm1.medium and hsm2m.medium HSMs that are provided by AWS CloudHSM are both PCI-3DS compliant.

**SOC2**

SOC2 is a framework to help service organizations demonstrate their cloud and data center security controls.
AWS CloudHSM has implemented SOC2 controls in critical areas to adhere to the trusted service principles.
For further information, refer to [The AWS SOC FAQs page](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/").
