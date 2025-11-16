# Internal operations

This topic describes internal requirements implemented by the service to secure customer keys and cryptographic operations for a globally distributed and scalable payment cryptography and key management service.

###### Topics

- [HSM protection](#w4aac36c22b7 "#w4aac36c22b7")
- [General key management](#w4aac36c22b9 "#w4aac36c22b9")
- [Management of customer keys](#w4aac36c22c11 "#w4aac36c22c11")
- [Communication security](#w4aac36c22c13 "#w4aac36c22c13")
- [Logging and monitoring](#w4aac36c22c15 "#w4aac36c22c15")

## HSM protection

### HSM specifications and lifecycle

AWS Payment Cryptography uses a fleet of commercially available HSMs. The HSMs are FIPS 140-2 Level 3 validated and also use firmware versions and the security policy listed on the
PCI Security Standards Council [approved PCI PTS Devices list](https://listings.pcisecuritystandards.org/assessors_and_solutions/pin_transaction_devices "https://listings.pcisecuritystandards.org/assessors_and_solutions/pin_transaction_devices") as PCI HSM v3 complaint.
The PCI PTS HSM standard includes additional requirements for the manufacturing, shipment, deployment, management, and destruction of HSM hardware which are important for payment security and compliance
but not addressed by FIPS 140.

Third party assessors verify HSM make model, firmware, configuration, lifecycle physical management, change control, operator access controls, main key management, and all PCI PIN and P2PE
requirements related to HSMs and HSM operations.

All HSMs are operated in PCI Mode and configured with the PCI PTS HSM security policy. Only functions required to support AWS Payment Cryptography use cases are enabled. AWS Payment Cryptography does not provide for printing,
display, or return of clear text PINs.

### HSM device physical security

Only HSMs that have device keys signed by an AWS Payment Cryptography certificate authority (CA) by the manufacturer prior to delivery can be used by the service.
The AWS Payment Cryptography is a sub-CA of the manufacturer’s CA that is the root of trust for HSM manufacturer and device certificates.
The manufacturer’s CA has attested compliance with PCI PIN Security Annex A and PCI P2PE Annex A.
The manufacturer verifies that all HSM with device keys signed by the AWS Payment Cryptography CA are shipped to AWS’ designated receiver.

As required by PCI PIN Security, the manufacturer supplies a list of serial numbers via a different communication channel than the HSM shipment. These serial numbers are checked at each step
in the process of HSM installation into AWS data centers. Finally, AWS Payment Cryptography operators validate the list of installed HSM against the manufacturer’s list before adding the serial number to list of
HSM permitted to receive AWS Payment Cryptography keys.

HSMs are in secure storage or under dual control at all times, which includes:

- Shipment from the manufacturer to an AWS rack assembly facility.
- During rack assembly.
- Shipment from the rack assembly facility to a data center.
- Receipt and installation into a data center secure processing room. HSM racks enforce dual control with card access-controlled locks, alarmed door sensors, and cameras.
- During operations.
- During decommissioning and destruction.

A complete chain-of-custody, with individual accountability, is maintained and monitored for each HSM.

### HSM initialization

An HSM is only initialized as part of the AWS Payment Cryptography fleet after its identity and integrity are validated by serial numbers, manufacturer installed device keys, and firmware checksum.
After the authenticity and integrity of an HSM validated, it is configured, including enabling PCI Mode. Then AWS Payment Cryptography region main keys and profile main keys are established and the HSM is
available to the service.

### HSM service and repair

HSM have serviceable components that do not require violation of the device’s cryptographic boundary. These components include cooling fans, power supplies, and batteries.
If an HSM or another device within the HSM rack needs service, dual control is maintained during the entire period that the rack is open.

### HSM decommissioning

Decommissioning occurs due to end-of-life or failure of an HSM. HSM are logically zeroized before removal from their rack, if functional, then destroyed within secure processing rooms of AWS data centers.
They are never returned to the manufacturer for repair, used for another purpose, or otherwise removed from a secure processing room before destruction.

### HSM firmware update

HSM firmware updates are applied when required to maintain alignment with PCI PTS HSM and FIPS 140-2 (or FIPS 140-3) listed versions, if an update is security related, or it is
determined that customers can benefit from features in a new version. AWS Payment Cryptography HSMs run off-the-shelf firmware, matching PCI PTS HSM-listed versions. New firmware versions are
validated for integrity with the PCI or FIPS certified firmware versions then tested for functionality before rollout to all HSMs.

### Operator access

Operators can have non-console access to HSM for troubleshooting in rare cases that information gathered from HSM during normal operations is insufficient to identify a problem
or plan a change. The following steps are executed:

- Troubleshooting activities are developed and approved and the non-console session is scheduled.
- An HSM is removed from customer processing service.
- Main keys are deleted, under dual control.
- Operator is permitted non-console access to the HSM to perform approved troubleshooting activities, under dual control.
  - After termination of the non-console session, the initial provisioning process is performed on the HSM, returning the standard firmware and configuration, then
    synchronizing the main key, before returning the HSM to serving customers.
  - Records of the session are recorded in change tracking.
  - Information obtained from the session is used for planning future changes.

All non-console access records are reviewed for process compliance and potential changes to HSM monitoring, the non-console-access management process, or operator training.

## General key management

All HSM in a region are synchronized to a Region Main Key. A Region Main Key protects at least one Profile Main Key. A Profile Main Key protects customer keys.

All main keys are generated by an HSM and distributed to by symmetric key distribution using asymmetric techniques, aligned with ANSI X9 TR 34 and PCI PIN Annex A.

### Generation

AES 256 bit Main keys are generated on one of the HSM provisioned for the service HSM fleet, using the PCI PTS HSM random number generator.

### Region main key synchronization

HSM region main keys are synchronized by the service across the regional fleet with mechanisms defined by ANSI X9 TR-34, which include:

- Mutual authentication using key distribution host (KDH) and key receiving device (KRD) keys and certificates to provide authentication and integrity of for
  public keys.
- Certificates are signed by a certificate authority (CA) that meets the requirements of PCI PIN Annex A2, except for asymmetric algorithms and key strengths
  appropriate for protecting AES 256 bit keys.
- Identification and key protection for the distributed symmetric keys is consistent with ANSI X9 TR-34 and PCI PIN Annex A1, except for asymmetric algorithms and key
  strengths appropriate for protecting AES 256 bit keys.

Region main keys are established for HSMs that have been authenticated and provisioned for a region by:

- A main key is generated on an HSM in the region. That HSM is designated as the key distribution host.
- All provisioned HSMs in the region generate KRD authentication token, which contain the public key of the HSM and non-replayable authentication information.
- KRD tokens are added to the KDH allow list after the KDH validates the identity and permission of the HSM to receive keys.
- The KDH produces an authenticable main key token for each HSM. Tokens contain KDH authentication information and encrypted main key that is loadable only on an HSM that it
  has been created for.
- Each HSM is sent the main key token built for it. After validating the HSM’s own authentication information and the KDH authentication information, the main key is decrypted
  by the KRD private key and loaded into the main key.

In the event that a single HSM must be re-synchronized with a region:

- It is re-validated and provisioned with firmware and configuration.
- If it is new to the region:
  - The HSM generates a KRD authentication token.
  - The KDH adds the token to its allow list.
  - The KDH generates a main key token for the HSM.
  - The HSM loads the main key.
  - The HSM is made available to the service.

This assures that:

- Only HSM validated for AWS Payment Cryptography processing within a region can receive that region’s master key.
- Only a master key from an AWS Payment Cryptography HSM can be distributed to an HSM in the fleet.

### Region main key rotation

Region main keys are rotated at the expiration of the crypto period, in the unlikely event of a suspected key compromise, or after changes
to the service that are determined to impact the security of the key.

A new region main key is generated and distributed as with initial provisioning. Saved profile main keys must be translated to the new region main key.

Region main key rotation does not impact customer processing.

### Profile main key synchronization

Profile main keys are protected by region main keys. This restricts a profile to a specific region.

Profile main keys are provisioned accordingly:

- A profile main key is generated on an HSM that has the region main key synchronized.
- The profile main key is stored and encrypted with the profile configuration and other context.
- The profile is used for customer cryptographic functions by any HSM in the region with the region main key.

### Profile main key rotation

Profile main keys are rotated at the expiration of the crypto period, after suspected key compromise, or after changes to the service that are determined to impact the security of the key.

Rotation steps:

- A new profile main key is generated and distributed as a pending main key as with initial provisioning.
- A background process translates customer key material from the established profile main key to the pending main key.
- When all customer keys have been encrypted with the pending key, the pending key is promoted to the profile main key.
- A background process deletes customer key material protected by the expired key.

Profile main key rotation does not impact customer processing.

### Protection

Keys depend only on the key hierarchy for protection. Protection of main keys is critical to prevent loss or compromise all customer keys.

Region main keys are restorable from backup only to HSM authenticated and provisioned for the service. These keys can only be stored as mutually authenticable,
encrypted main key tokens from a specific KDH for a specific HSM.

Profile master keys are stored with profile configuration and context information encrypted by region.

Customer keys are stored in key blocks, protected by a profile master key.

All keys exist exclusively within an HSM or stored protected by another key of equal or stronger cryptographic strength.

### Durability

Customer keys for transaction cryptography and business functions must be available even in extreme situations that would typically cause outages. AWS Payment Cryptography utilizes
a multiple level redundancy model across availability zones and AWS regions. Customer’s requiring higher availability and durability for payment cryptographic operations
than what is provided by the service should implement multi-region architectures.

HSM authentication and main key tokens are saved and may be used to restore a main key or synchronize with a new main key, in the event that an HSM must be reset. The
tokens are archived and used only under dual control when required.

### Operator access to HSM main keys

Main keys exist only in HSM managed by the service and secured in secure AWS facilities. Main keys cannot be exported from any HSM or synchronized to an HSM that is
not initialized by the manufacturer for use in the service. AWS operators cannot obtain main keys in any form that could be loaded into an HSM not managed by the service.

## Management of customer keys

At AWS, customer trust is our top priority. You maintain full control of your keys that you import to or create in the service under your AWS account. You retain responsibility
for configuring access to keys.

AWS Payment Cryptography is a service provider that uses HSMs and manages keys on behalf of customers, similar to long-standing payment service providers. The service has complete responsibility for HSM
physical and logical security. Key management responsibility is shared between the service and customers because the customer must provide accurate information about keys created by or imported to the
service, which the service uses to enforce correct key use and management. AWS data segregation protections are used to ensure that compromise of keys belonging one AWS account
cannot compromise keys belonging to another.

AWS Payment Cryptography has full responsibility for the HSM physical compliance and key management for keys managed by the service. This requires ownership and management of HSM
main keys and protection of customer keys managed by the AWS Payment Cryptography.

### Customer key space separation

AWS Payment Cryptography enforces key policies for all key use, including limiting principals to the account owning the key, unless a key is explicitly shared with another account.

AWS accounts provide complete environment segregation between customers or applications analogous to non-cloud implementations in different data centers. Each account provides isolated access control,
networking, compute resources, data storage, cryptographic keys for data protection and payment transactions, and all AWS resources. AWS services like Organizations and Control Tower enable enterprise
management of separate application accounts, analogous to cages or rooms within an enterprise data center.

### Operator access to customer keys

Customer keys managed by the service are stored protected by partition main keys and can only be used by the owning customer account or account the owner has specifically configured for key sharing. AWS operators
cannot export or perform key management or cryptographic operations
with customer keys using manual access to the service, which is managed by AWS manual operator access mechanisms.

Service code that implements customer key management and use is subject to AWS secure code practices as assessed per the AWS PCI DSS assessment.

### Backup and recovery

Keys and key information stored internally by the service for a region is backed up to encrypted archives by AWS. Archives require dual control by AWS to restore.

### Key blocks

All keys are stored and processed in ANSI X9.143 format key blocks.

Keys may be imported into the service from cryptograms or other key block formats supported by ImportKey. Similarly, keys may be exported, if they are exportable, to
other key block formats or cryptograms supported by key export profiles.

### Key use

Key use is restricted to the configured KeyUsage by the service. The service will fail any requests with inappropriate key usage, mode of use, or algorithm for the requested cryptographic operation.

### Key exchange relationships

PCI PIN Security and PCI P2PE require that organizations that share keys that encrypt PINs or carddata, including the key exchange keys (KEK) used to share those keys, not share the same keys with any other organizations.
It is a best practice that symmetric keys are shared between only 2 parties for a single purpose, including within the same organization. This minimizes the impact of suspected key compromises that force replacing impacted keys.

Even business cases that require sharing keys between more than 2 parties, should keep the number of parties to the minimum number.

AWS Payment Cryptography provides key tags that can be used to track and enforce key usage within those requirements.

For example, KEK and BDK for different key injection facilities can by identified by setting a “KIF”=“POSStation” for all keys shared with that service provider.
Another example would be to tag keys shared with payment networks with “Network”=“PayCard”. Tagging enables you to create access controls and create audit reports to enforce and demonstrate your key
management practices.

### Key deletion

DeleteKey marks keys in the database for deletion after a customer-configurable period.
After this period the key is irretrievably deleted. This is a safety mechanism to prevent the accidental or malicious deletion of a key.
Keys marked for deletion are not available for any actions except RestoreKey.

Deleted keys remain in service backups for 7 days after deletion. They are not restorable during this period.

Keys belonging to closed AWS accounts are marked for deletion. If the account is reactivated before the deletion period is reached any keys marked for deletion are restored, but disabled.
They must be re-enabled by you in order to use them for cryptographic operations.

## Communication security

### External

AWS Payment Cryptography API endpoints meet AWS security standards including TLS at or above 1.2 and Signature Version 4 for authentication and integrity of requests.

Incoming TLS connections are terminated on network load balancers and forwarded to API handlers over internal TLS connections.

### Internal

Internal communications between service components and between service components and other AWS service are protected by TLS using strong cryptography.

HSM are on a private, non-virtual network that is only reachable from service components. All connections between HSM and service components are secured with mutual TLS (mTLS), at or above TLS 1.2.
Internal certificates for TLS and mTLS are managed by Amazon Certificate Manager using an AWS Private Certificate Authority.
Internal VPCs and the HSM network are monitored for unexpected activities and configuration changes.

## Logging and monitoring

Internal service logs include:

- CloudTrail logs of AWS service calls made by the service
- CloudWatch logs of both events directly logged to CloudWatch logs or events from HSM
- Log files from HSM and service systems
- Log archives

All log sources monitor and filter for sensitive information, including about keys.
Logs are systematically reviewed to ensure that they contain do not contain sensitive customer information.

Access to logs is restricted to individuals needed for completing job roles.

All logs are retained in alignment with AWS log retention policies.
