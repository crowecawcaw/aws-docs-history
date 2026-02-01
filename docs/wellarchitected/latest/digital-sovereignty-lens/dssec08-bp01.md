# DSSEC08-BP01 Protect sensitive data during compute

If you hold sensitive datasets, you might require air-gapped
confidential compute environments for processing. This is in
addition to at-rest and in-transit encryption.

**Desired outcome:** Compute
environments remain isolated and hardened, blocking threat actors
from gaining access to data or the compute environment. Sensitive
data is protected during processing through confidential computing
capabilities.

**Common anti-patterns:**

- Assuming it is sufficient to protect data in storage and
  traversing networks, and overlooking the compute environment.
- Failure to isolate ongoing compute activity from neighboring
  activity in shared services or on shared hardware.
- Failure to initialize compute environments to a known-clean
  state, compromising compute activity.
- Failure to scrub residual traces of compute activity on
  completion, allowing the next user of shared hardware to
  retrieve previous state.
- Reinventing or reimplementing security primitives for each
  workload, not reusing trusted implementations.

**Benefits of establishing this best
practice:**

- Access is denied to threat actors, other AWS customers, AWS
  operators and personnel.
- Data is protected through its full lifecycle, removing
  opportunities for threat actor access during compute activity.
- Well-known and trusted encryption is applied to data in compute,
  blocking external or side-channel attacks from accessing
  plaintext data.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

When you process data marked as most sensitive, you often require
air-gapped environments, which are also referred to as
confidential compute environments. This may be driven by
motivations of protecting code and data from the operators
supporting the underlying cloud infrastructure or from the
customers' own operators.

### Implementation steps

1. **Use confidential compute**:
   The AWS Nitro System forms the foundation of AWS's
   confidential computing capabilities. It is designed with no
   operator access, meaning there is no mechanism for a system
   or person to log in to Amazon Elastic Compute Cloud (Amazon EC2) servers, read the memory of EC2 instances, or access
   data stored on instance storage and encrypted Amazon Elastic Block Store (Amazon EBS) volumes. The blog
   [Confidential
   computing: an AWS perspective](https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/ "https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/") is an introductory
   guide you can refer to. You can extend functionality offered
   by Nitro Systems with the following:
   - **Isolate and offload compute to
     Nitro enclaves**: Nitro Enclaves extends Nitro
     protection by creating isolated compute environments
     within EC2 instances. These enclaves are separate,
     hardened, and highly constrained virtual machines with
     _no persistent storage, no interactive access,
     and no external networking_. The isolation is
     achieved through the Nitro Hypervisor, which partitions
     physical resources and does not implement
     general-purpose administrative capabilities.

   A key aspect of Nitro Enclaves is that they inherit the
   same isolation and side-channel mitigations as other EC2
   instances running on the same server processor. When
   creating an enclave, you allocate a fixed number of
   virtual CPUs (vCPUs) and memory pages. These resources
   are subtracted from the parent instance and utilized by
   the Nitro Hypervisor to create another fully protected
   independent virtual machine (VM) environment.
   - **Isolate compute activity in
     dedicated hardware**: While Nitro Enclaves
     provide strong isolation for compute activity within an
     EC2 instance, the underlying hardware is not dedicated
     entirely to that workload. Some data sovereignty
     requirements may specify that workloads run on dedicated
     hardware, rather than the usual EC2 multi-tenant
     physical server model.

   An EC2 Dedicated Host is a physical server fully
   dedicated for your use. Dedicated Hosts provide
   visibility and the option to control how you place your
   EC2 instances on a specific, physical server. Amazon EC2
   instances placed on EC2 Dedicated Hosts use the same AWS
   Nitro System as described above, with the same benefits
   available.
   - **Enable memory
     encryption**: For additional defense in depth
     against physical attacks at the memory interface level,
     AWS offers memory encryption on various EC2 instance
     types. To use this, you must select an EC2 instance type
     that supports memory encryption.
     - You can enable hardware-enforced memory encryption
       on
       [EC2
       instances](../../../AWSEC2/latest/UserGuide/sev-snp.md#snp-requirements "../../../AWSEC2/latest/UserGuide/sev-snp.md#snp-requirements") that support AMD SEV-SNP. Refer to
       this
       [AMD
       whitepaper](https://docs.amd.com/v/u/en-US/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more "https://docs.amd.com/v/u/en-US/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more") to learn more about Secure
       Encrypted Virtualization (SEV) and Secure Nested
       Paging (SNP). In the context of EC2 instances, this
       has the effect of protecting the VM's memory
       contents from being deciphired by the hypervisor.
       Using mechanisms such as Reverse Map Table (RMP)
       protects VMs from data corruption, memory aliasing,
       memory re-mapping and replay related threats.
     - EC2 instances with AWS Graviton2 or later AWS
       Graviton processors support always-on memory
       encryption. The encryption keys are securely
       generated within the host system, do not leave the
       host system, and are destroyed when the host is
       rebooted or powered down.
     - EC2 instances with third generation Intel Xeon
       Scalable processors (Ice Lake), such as M6i
       instances, and fourth generation Intel Xeon Scalable
       processors (Sapphire Rapids), such as M7i instances,
       support always-on memory encryption using Intel
       Total Memory Encryption (TME).
     - EC2 instances with third generation AMD EPYC
       processors (Milan), such as M6a instances, and
       fourth generation AMD EPYC processors (Genoa), such
       as M7a instances, support always-on memory
       encryption using AMD Secure Memory Encryption (SME).

   - **Use Marketplace
     offerings**: Evaluate your Confidentiality,
     Integrity and Attestation
     [(confidentiality, integrity, and availability
     triad)](https://confidentialcomputing.io/2024/04/10/the-cia-triad-for-confidential-computing/ "https://confidentialcomputing.io/2024/04/10/the-cia-triad-for-confidential-computing/") requirements. The AWS Marketplace offers
     several
     [confidential
     compute solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=confidential+compute "https://aws.amazon.com/marketplace/search/results?searchTerms=confidential+compute") that complement the AWS Nitro
     System and assists in meeting confidentiality, integrity, and availability requirements unique to
     your workloads.

2. **Apply secure key management
   practices**: Proper key management is crucial to
   achieve digital sovereignty goals. It is necessary to
   correctly apply keys in encryption activity, and to
   correctly manage these keys. AWS KMS provides durable,
   secure, and redundant storage for AWS KMS keys, and many AWS
   services integrate with AWS KMS to support encryption of
   your data.

AWS Key Management Service (AWS KMS) uses FIPS 140-2 Level 3
validated hardware security modules to protect your
encryption keys. Because KMS keys remain within AWS KMS, you
must call AWS KMS to use a KMS key in a cryptographic
operation. There is no mechanism to export AWS KMS keys in
plain text, which keeps your sensitive cryptographic
material secure. When deploying workloads using a
multi-account strategy, we recommend keeping AWS KMS keys in
the same account as the workload that uses them.

Consider the full end to end journey of data and encryption
keys when workloads transport data into secure enclaves for
processing and then transport results back out. Neither the
data nor keys should be exposed during this process. If your
workload design requires that application data decryption
occurs only within a secure enclave boundary, for example
using keys stored outside AWS or in an AWS CloudHSM
instance, apply appropriate in-transit encryption of these
keys as they traverse the network.

## Resources

**Related best practices:**

- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")

**Related documents:**

- [Confidential
  computing: an AWS perspective](https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/ "https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/")
- [Building
  zero trust generative AI applications in healthcare with AWS
  Nitro Enclaves](https://aws.amazon.com/blogs/compute/building-zero-trust-generative-ai-applications-in-healthcare-with-aws-nitro-enclaves/ "https://aws.amazon.com/blogs/compute/building-zero-trust-generative-ai-applications-in-healthcare-with-aws-nitro-enclaves/")
- [AWS introduces Graviton5: the company's most powerful and
  efficient CPU](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2 "https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2")
- [AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/introduction.md "../../../prescriptive-guidance/latest/security-reference-architecture/introduction.md")
- [AWS KMS cryptography essentials](../../../kms/latest/developerguide/kms-cryptography.md "../../../kms/latest/developerguide/kms-cryptography.md")
- [Data
  protection in Amazon EC2](../../../AWSEC2/latest/UserGuide/data-protection.md "../../../AWSEC2/latest/UserGuide/data-protection.md")
- [Host
  and Instance Features](../../../whitepapers/latest/logical-separation/host-and-instance-features.md "../../../whitepapers/latest/logical-separation/host-and-instance-features.md")
- [What
  is Nitro Enclaves?](../../../enclaves/latest/user/nitro-enclave.md "../../../enclaves/latest/user/nitro-enclave.md")
- [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/ "https://aws.amazon.com/ec2/dedicated-hosts/")

**Related videos:**

- [AWS re:Invent 2025 - Deep Dive into the AWS Nitro System
  (CMP316)](https://www.youtube.com/watch?v=cD1mNQ9YbeA "https://www.youtube.com/watch?v=cD1mNQ9YbeA")
- [AWS re:Invent 2025 - Introducing Nitro Isolation Engine:
  Transparency through Mathematics (CMP359)](https://www.youtube.com/watch?v=b0P55gHhG4g "https://www.youtube.com/watch?v=b0P55gHhG4g")
- [AWS re:Invent 2020 - Deep dive on AWS Nitro Enclaves for
  applications running on Amazon EC2](https://www.youtube.com/watch?v=yDe_C_fpkfg "https://www.youtube.com/watch?v=yDe_C_fpkfg")

**Related services:**

- [Amazon Elastic Compute Cloud (EC2)](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md")
- [Amazon
  Nitro System](../../../whitepapers/latest/security-design-of-aws-nitro-system/the-components-of-the-nitro-system.md "../../../whitepapers/latest/security-design-of-aws-nitro-system/the-components-of-the-nitro-system.md")
- [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- [AWS CloudHSM](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md")
