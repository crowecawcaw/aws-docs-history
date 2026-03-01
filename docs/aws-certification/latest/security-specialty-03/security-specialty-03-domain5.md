# Content Domain 5: Data Protection

###### Tasks

- [Task 5.1: Design and implement controls for data in transit](#security-specialty-03-domain5-task1 "#security-specialty-03-domain5-task1")
- [Task 5.2: Design and implement controls for data at rest](#security-specialty-03-domain5-task2 "#security-specialty-03-domain5-task2")
- [Task 5.3: Design and implement controls to protect confidential data, credentials, secrets, and cryptographic key materials](#security-specialty-03-domain5-task3 "#security-specialty-03-domain5-task3")

## Task 5.1: Design and implement controls for data in transit

Skills in:

- Skill 5.1.1: Design and configure mechanisms to require encryption when connecting to connect to resources (for example, by configuring Elastic Load Balancing [ELB] security policies, by enforcing TLS configurations).
- Skill 5.1.2: Design and configure mechanisms for secure and private access to resources (for example, AWS PrivateLink, VPC endpoints, AWS Client VPN, AWS Verified Access).
- Skill 5.1.3: Design and configure inter-resource encryption in transit (for example, inter-node encryption configurations for Amazon EMR, Amazon Elastic Kubernetes Service [Amazon EKS], SageMaker AI, Nitro encryption).

## Task 5.2: Design and implement controls for data at rest

Skills in:

- Skill 5.2.1: Design, implement, and configure data encryption at rest based on specific requirements (for example, by selecting the appropriate encryption key service such as AWS CloudHSM or AWS Key Management Service [AWS KMS] or by selecting the appropriate encryption type such as client-side encryption or server-side encryption).
- Skill 5.2.2: Design and configure mechanisms to protect data integrity (for example, S3 Object Lock, S3 Glacier Vault Lock, versioning, digital code signing, file validation).
- Skill 5.2.3: Design automatic lifecycle management and retention solutions for data (for example, S3 Lifecycle policies, S3 Object Lock, Amazon Elastic File System [Amazon EFS] Lifecycle policies, Amazon FSx for Lustre backup policies).
- Skill 5.2.4: Design and configure secure data replication and backup solutions (for example, Amazon Data Lifecycle Manager, AWS Backup, ransomware protection, AWS DataSync).

## Task 5.3: Design and implement controls to protect confidential data, credentials, secrets, and cryptographic key materials

Skills in:

- Skill 5.3.1: Design management and rotation of credentials and secrets (for example, AWS Secrets Manager).
- Skill 5.3.2: Manage and use imported key material (for example, by managing and rotating imported key material, by managing and configuring external key stores).
- Skill 5.3.3: Describe the differences between imported key material and AWS generated key material.
- Skill 5.3.4: Mask sensitive data (for example, CloudWatch Logs data protection policies, Amazon Simple Notification Service [Amazon SNS] message data protection).
- Skill 5.3.5: Create and manage encryption keys and certificates across a single AWS Region or multiple Regions (for example, AWS KMS customer managed AWS KMS keys, AWS Private Certificate Authority).
