# Working with

SigV4 for MediaPackage Version 2

Signature Version 4 (SigV4) for MediaPackage v2 is a signing protocol used to
authenticate requests to MediaPackage v2 over HTTP. When you use SigV4 for MediaPackage v2, MediaTailor
includes a signed authorization header in the HTTP request to the MediaPackage v2 endpoint
used as your origin. If the signed authorization header is valid, your origin
fulfills the request. If it isn't valid, the request fails.

For general information about SigV4 for MediaPackage v2, see the [Authenticating
Requests (AWS Signature Version 4)](../../../mediapackage/latest/userguide/sig-v4-authenticating-requests.md "../../../mediapackage/latest/userguide/sig-v4-authenticating-requests.md") topic in the _MediaPackage v2 API reference_.

## Requirements

If you activate SigV4 for MediaPackage v2 authentication for your source location,
you must meet these requirements:

- You must allow MediaTailor to access your MediaPackage v2 endpoint by granting
  **mediatailor.amazonaws.com** principal access in
  an Origin Access Policy on the endpoint.
- Your MediaTailor source location base URL must be a MediaPackage v2
  endpoint.
- The caller of the API must have
  **mediapackagev2:GetObject** IAM permissions to
  read all multivariant playlists referenced by the MediaTailor source packaging
  configurations.
