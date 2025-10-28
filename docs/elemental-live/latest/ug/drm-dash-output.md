# DASH output

Encryption mode: Always AES CTR (AES-128)

Key rotation: Always Static

Support client players: Consult with the DRM solution provider (for SPEKE) or the DRM
Technology provider for supported players.

| Description                                                                                                                                                                                                | DRM technology provider     | Key provider (DRM implementer) | Version of server API from DRM implementer |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------ | ------------------------------------------ |
| The customer uses a SPEKE-compliant DRM solution for protecting DASH output using Widevine/CENC and PlayReady/CENC technology.                                                                             | CENC Widevine and PlayReady | SPEKE                          | SPEKE v1.0                                 |
| The customer uses a static PlayReady key for protecting DASH output using PlayReady/CENC technology.                                                                                                       | PlayReady                   | PlayReady                      | Not applicable                             |
| The customer uses a static Widevine key for protecting DASH output using Widevine/CENC technology.                                                                                                         | CENC/Widevine               | Generic                        | Not applicable                             |
| The customer uses the Piksel DRM solution for protecting DASH output using the Widevine/CENC standard. The end user will play the content on a player that is Widevine/CENC compliant and Piksel-approved. | CENC/Widevine               | Piksel                         | GetEncryptInfo v1.0                        |
