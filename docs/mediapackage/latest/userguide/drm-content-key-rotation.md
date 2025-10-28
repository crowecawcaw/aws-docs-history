# AWS Elemental MediaPackage key rotation behavior

When you enable key rotation on live content from TS and CMAF origin endpoints,
AWS Elemental MediaPackage retrieves content keys before the live content begins. As the content
progresses, MediaPackage retrieves new keys at the interval that you set on the origin
endpoint, as described in [Encryption fields](endpoints-create.md#endpoints-encryption "endpoints-create.md#endpoints-encryption").

If MediaPackage is unable to retrieve the content key, it takes the following
actions:

- If MediaPackage successfully retrieved a content key for this endpoint before, it
  uses the last key that it fetched. This ensures that endpoints that worked previously
  continue to work.
- If MediaPackage has _not_ successfully retrieved a content key for
  this endpoint before, MediaPackage responds to the playback request with **`error
404`**.
