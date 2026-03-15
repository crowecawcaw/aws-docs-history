# Design goals

AWS Payment Cryptography is designed to meet the following requirements:

- Trustworthy — Use of keys is protected
  by access control policies that you define and manage.
  There is no mechanism to export plaintext AWS Payment Cryptography keys. The confidentiality of your
  cryptographic keys is crucial. Multiple Amazon employees with role-specific
  access to quorum-based access controls are required to perform
  administrative actions on the HSMs. No Amazon employees have access to
  HSM main (or master) keys or backups. Main keys cannot be synchronized
  with HSMs that are not part of an AWS Payment Cryptography region. All other keys are protected
  by HSM main keys. Therefore, customer AWS Payment Cryptography keys are not usable outside
  of the AWS Payment Cryptography service operating within a customer's account.
- Low-latency and high throughput — AWS Payment Cryptography provides cryptographic operations at latency and throughput
  level suitable for managing payment cryptographic keys and processing payment transactions.
- Durability — The durability of cryptographic keys is designed to be equal that of the highest durability services in AWS.
  A single cryptographic key can be shared with a payment terminal, EMV chip card, or other secure cryptographic device (SCD) that is in use for many years.
- Independent Regions — AWS provides independent regions for customers who need to restrict data access in different regions
  or need to comply with data residency requirements. Key usage can be isolated within an AWS Region.
- Secure source of random numbers — Because strong cryptography depends on truly unpredictable random number generation, AWS Payment Cryptography provides
  a high-quality and validated source of random numbers. All key generation for AWS Payment Cryptography uses PCI PTS HSM-listed HSM, operating in PCI mode.
- Audit — AWS Payment Cryptography records the use and management of cryptographic keys in CloudTrail logs and service
  logs available via Amazon CloudWatch. You can use CloudTrail logs to
  inspect use of your cryptographic keys, including the use of keys by
  accounts that you have shared keys with. AWS Payment Cryptography is audited by third party
  assessors against applicable PCI, card brand, and regional payment security standards.
  Attestations and Shared Responsibility guides are available on AWS Artifact.
- Elastic — AWS Payment Cryptography scales out and in according to your demand. Instead of predicting and reserving HSM capacity, AWS Payment Cryptography provides payment cryptography on-demand.
  AWS Payment Cryptography takes responsibility for maintaining the security and compliance of HSM to provide sufficient capacity to meet customer’s peak demand.
