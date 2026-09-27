

# AWS Elemental MediaPackage key rotation behavior
<a name="drm-content-key-rotation"></a>

When you enable key rotation on live content from TS and CMAF origin endpoints, AWS Elemental MediaPackage retrieves content keys before the live content begins. As the content progresses, MediaPackage retrieves new keys at the interval that you set on the origin endpoint, as described in [Encryption fields](endpoints-create.md#endpoints-encryption).

If MediaPackage is unable to retrieve the content key, it takes the following actions:
+ If MediaPackage successfully retrieved a content key for this endpoint before, it uses the last key that it fetched. This ensures that endpoints that worked previously continue to work. 
+ If MediaPackage has *not* successfully retrieved a content key for this endpoint before, MediaPackage responds to the playback request with error 404. 

## Signaling time-based key rotation with SPEKE v2.1
<a name="drm-time-based-key-rotation-signaling"></a>

With SPEKE v2.1, MediaPackage can signal the start and end times of each key rotation period to your DRM key provider. MediaPackage includes these times in the `ContentKeyPeriod` of each key request. Time-based key rotation signaling tells your key provider exactly when MediaPackage uses each content key. This helps your key provider return keys that stay consistent across AWS Regions.

With the default SPEKE v2.0 contract, MediaPackage signals the content key index in the `ContentKeyPeriod`. With SPEKE v2.1, you can also signal the start and end times. For more information about SPEKE v2.1, see [SPEKE API v2.1](https://docs.aws.amazon.com/speke/latest/documentation/the-speke-api-v2-1.html). For implementation details for DRM key providers, see [Implementing SPEKE with AWS Elemental MediaPackage](implementing-speke-v2.md).

**To enable time-based key rotation signaling**

To signal the start and end times to your key provider, configure the following settings on the SPEKE key provider for your origin endpoint:
+ Enable key rotation by setting a non-zero key rotation interval.
+ Set `SpekeVersion` to `V2_1`.
+ Set `ContentKeyPeriodConfiguration` to a `ContentKeyPeriodTiming` value of `START_END_ONLY` or `INDEX_WITH_START_END`.

The `ContentKeyPeriodTiming` value controls what MediaPackage signals in each `ContentKeyPeriod`.


| ContentKeyPeriodTiming | Description | 
| --- | --- | 
| INDEX\_ONLY | Signal only the content key index. This is the default, and it is supported for both SPEKE v2.0 and SPEKE v2.1. | 
| START\_END\_ONLY | Signal only the start and end times of each key period. This value requires SpekeVersion V2\_1. | 
| INDEX\_WITH\_START\_END | Signal both the content key index and the start and end times of each key period. This value requires SpekeVersion V2\_1. | 

**Note**  
Your DRM key provider must return the same start and end times that MediaPackage sends in each `ContentKeyPeriod`. The key provider can't override the key rotation time boundaries that MediaPackage sets.