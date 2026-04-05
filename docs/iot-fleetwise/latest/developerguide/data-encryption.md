AWS IoT FleetWise will no longer be open to new customers starting April 30, 2026. If you would like to use AWS IoT FleetWise, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](iotfleetwise-availability-change.md "iotfleetwise-availability-change.md").

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
