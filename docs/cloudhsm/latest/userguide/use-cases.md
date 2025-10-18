# AWS CloudHSM use cases

AWS CloudHSM can be used to accomplish a variety of goals. The content in this topic provides an overview of what you can do with AWS CloudHSM.



**Achieve regulatory compliance**
Businesses that need to align with enterprise security standards can use AWS CloudHSM to manage private keys that protect highly confidential data. The HSMs provided by AWS CloudHSM are FIPS 140-2 level 3 certified and comply with PCI DSS. 
 Additionally, AWS CloudHSM is PCI PIN compliant and PCI-3DS compliant. For more information, see [Compliance](fips-validation.md "fips-validation.md").




**Encrypt and decrypt data**
Use AWS CloudHSM to manage private keys that protect highly confidential data, encryption in transit, and encryption at rest.
 Additionally, AWS CloudHSM offers standards-compliant integration with multiple cryptographic SDKs.




**Sign and verify documents with private and public keys**
In cryptography, using a private key to **sign** a document allows recipients to use a public key to **verify** that you (and not someone else) actually sent the document.
 Use AWS CloudHSM to create asymmetric public and private key pairs that are specifically designed for this purpose.




**Authenticate messages using HMACs and CMACs**
In cryptography, Cipher Message Authentication Codes (CMACs) and Hash-based Message Authentication Codes (HMACs) are used to authenticate and ensure the integrity of messages sent over unsafe networks. 
 With AWS CloudHSM, you can securely create and manage symmetric keys that support HMACs and CMACs.




**Leverage the benefits of AWS CloudHSM and AWS Key Management Service**
Customers can combine AWS CloudHSM and [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to store key material in a single-tenant environment while also getting the key management, scaling, and cloud integration benefits of AWS KMS. 
 For details on how to do this, see [AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html "https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html") in the *AWS Key Management Service Developer Guide*.




**Offload SSL/TLS processing for web servers**
To securely send data over the internet, web servers use public–private key pairs and SSL/TLS public key certificate to establish HTTPS sessions. 
 This process involves a lot of computation for web servers, but you can reduce computational burden while providing extra security by offloading some of this to your AWS CloudHSM cluster. 
 For information about setting up SSL/TLS offload with AWS CloudHSM, see [SSL/TLS offload](ssl-offload.md "ssl-offload.md").




**Enable transparent data encryption (TDE)**
Transparent Data Encryption (TDE) is used to encrypt database files. Using TDE, database software encrypts data before storing it on disk.
 You can achieve greater security by storing the TDE master encryption key in HSMs in your AWS CloudHSM. For information about setting up Oracle TDE with AWS CloudHSM, see [Oracle database encryption](oracle-tde.md "oracle-tde.md").




**Manage the private keys of an issuing certificate authority (CA)**
A certificate authority (CA) is a trusted entity that issues digital certificates that bind a public key to an identity (a person or organization).
 To operate a CA, you must maintain trust by protecting the private key that signs certificates issued by your CA.
 You can store such private keys in your AWS CloudHSM cluster and then use your HSMs to perform cryptographic signing operations.




**Generate random numbers**
Generating random numbers to create encryption keys is core to online security. AWS CloudHSM can be used to securely generate random numbers in HSMs you control and are only visible to you.
