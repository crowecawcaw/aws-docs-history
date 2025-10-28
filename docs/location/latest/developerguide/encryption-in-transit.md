# Data in transit encryption for Amazon Location Service

Amazon Location protects data in transit, as it travels to and from the service, by
automatically encrypting all inter-network data using the Transport Layer Security (TLS)
1.2 encryption protocol. Direct HTTPS requests sent to the Amazon Location Service APIs are signed by
using the [AWS
Signature Version 4 Algorithm](../../../general/latest/gr/sigv4_signing.md "../../../general/latest/gr/sigv4_signing.md") to establish a secure connection.
