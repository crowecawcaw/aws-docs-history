# Network Exclusions

The AppStream 2.0 management network range (`198.19.0.0/16`) and
following ports and addresses should not be blocked by any
security / firewall or antivirus solutions within AppStream 2.0
instances.

_Table 7 — Ports in AppStream 2.0 streaming instances security software must not
interfere with_

| **Port** | **Usage**
|
| --- | --- |
| **8300** | This is used for establishing the streaming connection |
| **3128** | This is used for managing the streaming instance by AppStream 2.0 |
| **8000** | This is used for managing the streaming instance by AppStream 2.0 |
| **8443** | This is used for managing the streaming instance by AppStream 2.0 |
| **53** | DNS | _Table 8 — AppStream 2.0 managed service addresses security software must not interfere with_
| **Port** | **Usage** |
| --- | --- |
| **169.254.169.123** | NTP |
| **169.254.169.249** | NVIDIA GRID License Service |
| **169.254.169.250** | KMS |
| **169.254.169.251** | KMS |
| **169.254.169.253** | DNS |
| **169.254.169.254** | Metadata |
