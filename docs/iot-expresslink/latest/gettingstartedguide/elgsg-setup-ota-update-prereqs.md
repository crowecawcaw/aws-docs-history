# Prerequisites

You must have received a firmware image signed by the manufacturer of your ExpressLink
module. Along with the firmware image, you will also have additional signing
metadata such as:

- signature hashing algorithm used (Example: SHA-256)
- signature encryption algorithm used (Example: ECDSA)
- actual signature encoded using the base64 encoding format.
- (Optional) path name (a string) which identifies the location where the certificate
  is provisioned in the ExpressLink module
  Finally, before you proceed, you should create an OTA Update role in your AWS account
  using the steps outlined in
  [Create an OTA Update service role](../../../freertos/latest/userguide/create-service-role.md "../../../freertos/latest/userguide/create-service-role.md").
