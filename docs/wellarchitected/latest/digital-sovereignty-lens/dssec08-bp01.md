

# DSSEC08-BP01 Protect sensitive data during compute
<a name="dssec08-bp01"></a>

 If you store and process sensitive datasets, you might need to apply specialized data protection capabilities. This is in addition to at-rest and in-transit encryption. 

 **Desired outcome:** 
+  You can use specialized capabilities to protect sensitive data during compute. 

 **Common anti-patterns:** 
+  Assuming it is sufficient to protect data in storage and in-transit but overlooking the compute environment when processing sensitive data. 

 **Benefits of establishing this best practice:** 
+  Protects data from access by the operator of the underlying cloud infrastructure. 
+  Enables isolation of sensitive workloads from customers' own operators and software. 
+  Greater use of fully supported compute capabilities that enable data protection. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 When you process data marked as most sensitive, you might require confidential compute environments. Confidential computing has two distinct security and privacy dimensions. The first is protection of code and data from the operator of the underlying cloud infrastructure, and the second is protection of sensitive elements of customer code and data from customers' own operators and software. The blog [Confidential computing: an AWS perspective](https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/) describes these dimensions in more depth. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Use the AWS Nitro System**: The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) forms the foundation of modern EC2 instances. It is built from the ground up, with no mechanism for operators to access customer content. When you use [Nitro-based EC2 instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) you automatically fulfill the first dimension of confidential compute, meaning your content remains protected from operators of the cloud provider. 

1.  **Isolate and offload compute to Nitro Enclaves**: [Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/) extends Nitro protection by creating isolated compute environments within EC2 instances. Use it when you need to fulfill the second dimension of confidential compute, that is, protection from your own operators and software. Nitro Enclaves provides the ability to protect sensitive content from customers' own operators by delivering the capability to create isolated compute environments within their EC2 instances. 

    Nitro Enclaves are separate, hardened, and highly constrained virtual machines with no persistent storage, no interactive access, and no external networking. The isolation is achieved through the Nitro Hypervisor, which uses hardware virtualization features of the server processor to create isolated virtual machines, and doesn't implement general-purpose administrative capabilities. A key aspect of Nitro Enclaves is that they inherit the same isolation and side-channel mitigations as other EC2 instances running on the same server processor. 

    Nitro Enclaves includes [built-in support](https://docs.aws.amazon.com/enclaves/latest/user/kms.html) for attestation with AWS KMS. You use the [Nitro Enclaves SDK](https://github.com/aws/aws-nitro-enclaves-sdk-c) to [request a signed attestation document](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html#attestation-doc) from the Nitro Hypervisor. This document is then attached to requests from the enclave to an external service, allowing the external service to validate requests. See the KMS Tool [sample application](https://github.com/aws/aws-nitro-enclaves-sdk-c/blob/main/docs/kmstool.md) that demonstrates the cryptographic attestation process. 

1.  **Apply secure key management practices**: Proper key management is necessary to achieve digital sovereignty goals. It is necessary to correctly apply keys in encryption operations, and to correctly manage these keys. [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) provides durable, secure, and redundant storage for AWS KMS keys. AWS KMS uses FIPS 140-3 Level 3 validated hardware security modules to protect your encryption keys. There is no mechanism to export AWS KMS keys. Many AWS services integrate with AWS KMS to support encryption of your data. See the [service integration table](https://aws.amazon.com/kms/features/) for a list of supported services. 

    There are two broad approaches to managing AWS KMS keys in multi-account environments. Choose between a [centralized or decentralized model](https://docs.aws.amazon.com/kms/latest/developerguide/multi-account-key-management.html) aligning with your operating model and relevant compliance needs. 

1.  **Consider all aspects of data protection**: Specialized data protection measures succeed when built over secure foundations. See [Data protection in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html) for the range of data protection options available to you. Beyond data protection, consider [infrastructure protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) best practices outlined in the Security Pillar of the AWS Well-Architected Framework. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 

 **Related documents:** 
+  [Confidential computing: an AWS perspective](https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/) 
+  [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html) 
+  [AWS KMS cryptography essentials](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html) 
+  [Data protection in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html) 
+  [Host and Instance Features](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/host-and-instance-features.html) 
+  [What is Nitro Enclaves?](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) 
+  [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Deep Dive into the AWS Nitro System (CMP316)](https://www.youtube.com/watch?v=cD1mNQ9YbeA) 
+  [AWS re:Invent 2025 - Innovating with AWS Confidential Computing: An Integrated Approach (CMP407)](https://www.youtube.com/watch?v=R2QxpJDEmY4) 
+  [AWS re:Invent 2025 - Introducing Nitro Isolation Engine: Transparency through Mathematics (CMP359)](https://www.youtube.com/watch?v=hqqKi3E-oG8) 

 **Related services:** 
+  [Amazon Elastic Compute Cloud (EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) 
+  [Amazon Nitro System](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-components-of-the-nitro-system.html) 
+  [AWS Key Management Service (KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 