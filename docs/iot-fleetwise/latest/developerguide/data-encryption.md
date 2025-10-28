# Data encryption in AWS IoT FleetWise

Data encryption refers to protecting data while in-transit (as it travels to and from
AWS IoT FleetWise, and between gateways and servers), and at rest (while it's stored on local devices or
in AWS services). You can protect data at rest using client-side encryption.

###### Note

AWS IoT FleetWise edge processing exposes APIs that are hosted within AWS IoT FleetWise gateways and are accessible
over the local network. These APIs are exposed over a TLS connection backed by a
server-certificate owned by the AWS IoT FleetWise Edge connector. For client authentication, these APIs
use an access-control password. The server-certificate private-key and the access-control
password are both stored on disk. AWS IoT FleetWise edge processing relies on file-system encryption
for the security of these credentials at rest.

For more information about server-side encryption and client-side encryption, review the
following topics.

###### Contents

- [Encryption at rest in AWS IoT FleetWise](encryption-at-rest.md "encryption-at-rest.md")
- [Key management in AWS IoT FleetWise](key-management.md "key-management.md")
