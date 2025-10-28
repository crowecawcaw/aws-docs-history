# Resilience in AWS Payment Cryptography

AWS global infrastructure is built around AWS Regions and Availability Zones. Regions
provide multiple physically separated and isolated Availability Zones, which are connected through
low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can
design and operate applications and databases that automatically fail over between zones without
interruption. Availability Zones are more highly available, fault tolerant, and scalable than
traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

## Regional isolation

AWS Payment Cryptography is a Regional service that is available in multiple regions.

The Regionally isolated design of AWS Payment Cryptography ensures that an availability issue in one AWS Region cannot affect AWS Payment Cryptography operation in any other Region. AWS Payment Cryptography is designed to ensure zero planned downtime, with all software updates and scaling operations performed seamlessly and imperceptibly.

The AWS Payment Cryptography Service Level Agreement (SLA) includes a service commitment of 99.99% for all Payment Cryptography APIs. To fulfill this commitment, AWS Payment Cryptography ensures that all data and authorization information required to execute an API request is available on all regional hosts that receive the request.

The AWS Payment Cryptography infrastructure is replicated in at least three Availability Zones (AZs) in each Region. To ensure that multiple host failures do not affect AWS Payment Cryptography performance, AWS Payment Cryptography is designed to service customer traffic from any of the AZs in a Region.

Changes that you make to the properties or permissions of a payment key are replicated to all hosts in the Region to ensure that subsequent request can be processed correctly by any host in the Region. Requests for cryptographic operations using your payment key are forwarded to a fleet of AWS Payment Cryptography hardware security modules (HSMs), any of which can perform the operation with the payment key.

## Multi-tenant design

The multi-tenant design of AWS Payment Cryptography enables it to fulfill the availability SLA, and to sustain high request rates, while protecting the confidentiality of your keys and data.

Multiple integrity-enforcing mechanisms are deployed to ensure that the payment key that you specified for the cryptographic operation is always the one that is used.

The plaintext key material for your Payment Cryptography keys is protected extensively. The key material is encrypted in the HSM as soon as it is created, and the encrypted key material is immediately moved to secure storage. The encrypted key is retrieved and decrypted within the HSM just in time for use. The plaintext key remains in HSM memory only for the time needed to complete the cryptographic operation. Plaintext key material never leaves the HSMs; it is never written to persistent storage.

For more information about the mechanisms that AWS Payment Cryptography uses to secure your keys, see AWS Payment Cryptography Cryptographic Details.
