

# Implementing SPEKE v2.0 with AWS Elemental MediaPackage
<a name="implementing-speke-v2"></a>

This topic supplements the [SPEKE API v2 — Customizations and constraints to the DASH-IF specification](https://docs.aws.amazon.com/speke/latest/documentation/speke-constraints-v2.html) with practical implementation guidance verified through production integration testing with AWS Elemental MediaPackage v2.

**Note**  
This guide does not cover [SPEKE API v2 — Content Key Encryption](https://docs.aws.amazon.com/speke/latest/documentation/content-key-encryption-v2.html). Examples show content keys returned in `pskc:PlainValue` (cleartext base64), protected by HTTPS transport encryption.

**Topics**
+ [HTTP protocol requirements](#speke-v2-http-requirements)
+ [CPIX document structure](#speke-v2-cpix-structure)
+ [DRM system signaling](#speke-v2-drm-signaling)
+ [Key delivery to players](#speke-v2-key-delivery)
+ [Testing and verification](#speke-v2-testing)
+ [Implementation checklist](#speke-v2-checklist)

## HTTP protocol requirements
<a name="speke-v2-http-requirements"></a>

**Request headers (from MediaPackage)**


| Header | Required | Value | 
| --- | --- | --- | 
| Content-Type | Yes | application/xml | 
| X-Speke-Version | Yes | 2.0 | 

**Response headers (from key provider)**


| Header | Required | Value | 
| --- | --- | --- | 
| Content-Type | Yes | application/xml | 
| X-Speke-Version | Yes | Echo back the request value | 
| X-Speke-User-Agent | Yes | Your server identifier | 

**Error responses (HTTP 422)**


| Condition | Error message | 
| --- | --- | 
| Missing contentId | Missing CPIX@contentId | 
| Missing version | Missing CPIX@version | 
| Unsupported version | Unsupported CPIX@version | 
| Missing encryption scheme | Missing ContentKey@commonEncryptionScheme for KID {id} | 
| Mixed encryption schemes | Non compliant ContentKey@commonEncryptionScheme combination | 
| Unsupported SPEKE version | Unsupported SPEKE version | 

## CPIX document structure
<a name="speke-v2-cpix-structure"></a>

Every SPEKE v2.0 exchange uses CPIX v2.3 XML with the namespaces `xmlns:cpix="urn:dashif:org:cpix"` and `xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc"`.

### Root element: cpix:CPIX
<a name="speke-v2-cpix-root"></a>


| Attribute | Required | Description | 
| --- | --- | --- | 
| contentId | Yes | Content identifier from MediaPackage. Must not be empty. | 
| version | Yes | Must be 2.3. Return error if missing or unsupported. | 

The key provider must NOT modify `contentId` or `version` in the response. However, the key provider may override the `kid` value on `ContentKey` elements — see [Overriding the key identifier](https://docs.aws.amazon.com/speke/latest/documentation/kid-override-v2.html).

### ContentKeyList (mandatory)
<a name="speke-v2-content-key-list"></a>

Contains one or more `ContentKey` elements. Each represents an encryption key.


| Attribute | Required | Description | 
| --- | --- | --- | 
| kid | Yes | Key ID in UUID format | 
| commonEncryptionScheme | Yes | One of: cenc, cbc1, cbcs | 
| explicitIV | Optional | Base64-encoded 16-byte initialization vector | 

All ContentKey elements in a single request must use the same `commonEncryptionScheme`. The response must include `cpix:Data/pskc:Secret/pskc:PlainValue` with a base64-encoded 16-byte AES key.

### DRMSystemList (mandatory)
<a name="speke-v2-drm-system-list"></a>

Contains one `DRMSystem` element per key per DRM system. Example: 2 keys x 3 DRM systems = 6 DRMSystem elements.


| Attribute | Required | Description | 
| --- | --- | --- | 
| kid | Yes | Key ID this DRM system applies to | 
| systemId | Yes | DRM system UUID | 

**Mandatory HLS signaling rules:**

1. All `HLSSignalingData` content must be base64-encoded.

1. Both `playlist="media"` and `playlist="master"` must be present.

1. Decoded media and master tags must have identical attributes. Only the tag name differs.

1. HLS tags must NOT contain a `SCHEME` attribute.

1. Each DRMSystem must reference exactly one `kid` with exactly one HLS tag.

### ContentKeyPeriodList (live streaming)
<a name="speke-v2-content-key-period-list"></a>

Must be echoed back unchanged from the request. MediaPackage sends this even without key rotation.

### ContentKeyUsageRuleList (mandatory)
<a name="speke-v2-usage-rule-list"></a>

Defines which keys protect which tracks. The AWS SPEKE v2 spec explicitly requires the key provider to echo back the ContentKeyUsageRuleList unchanged — MediaPackage defines the encryption contract (which keys protect which tracks), and the DRM server must not alter it.


| Attribute | Required | Description | 
| --- | --- | --- | 
| kid | Yes | Key ID this rule applies to | 
| intendedTrackType | Yes | ALL, VIDEO, AUDIO, SD, HD, UHD, etc. | 

At least one `VideoFilter` or `AudioFilter` child element is required.

## DRM system signaling
<a name="speke-v2-drm-signaling"></a>

**System IDs**


| System ID | Reference | Encryption Schemes | 
| --- | --- | --- | 
| 94ce86fb-07ff-4f43-adb8-93d2fa968ca2 | FairPlay | cbcs only | 
| edef8ba9-79d6-4ace-a3c8-27dcd51d21ed | Widevine | cenc, cbcs | 
| 9a04f079-9840-4286-ab92-e65be0885f95 | PlayReady | cenc, cbcs | 
| 3ea8778f-7742-4bf9-b18b-e834b2acbd47 | Clear Key AES-128 | cbc1 only | 

### FairPlay signaling
<a name="speke-v2-fairplay"></a>

**Response XML structure:**

```
<cpix:DRMSystem kid="8fe6f4de-..." systemId="94ce86fb-07ff-4f43-adb8-93d2fa968ca2">
  <cpix:HLSSignalingData playlist="media">BASE64_ENCODED_EXT_X_KEY</cpix:HLSSignalingData>
  <cpix:HLSSignalingData playlist="master">BASE64_ENCODED_EXT_X_SESSION_KEY</cpix:HLSSignalingData>
</cpix:DRMSystem>
```

FairPlay uses only HLS signaling (no PSSH or ContentProtectionData).

**Decoded HLS signaling (media and master identical except tag name):**

```
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://<BASE64_JSON>",KEYFORMAT="com.apple.streamingkeydelivery",KEYFORMATVERSIONS="1"
#EXT-X-SESSION-KEY:METHOD=SAMPLE-AES,URI="skd://<BASE64_JSON>",KEYFORMAT="com.apple.streamingkeydelivery",KEYFORMATVERSIONS="1"
```

The `skd://` URI contains a base64-encoded JSON payload — NOT just the kid hex:

```
{"ContentId":"101","KeyId":"8fe6f4de-841a-3acd-a81a-be516f356bbb","IV":"base64-encoded-IV=="}
```

**Important**  
The `KeyId` must use UUID format with hyphens. Do NOT include a separate `IV=0x...` attribute in the HLS tag — the IV is inside the JSON payload only.

### Widevine signaling
<a name="speke-v2-widevine"></a>

**Response XML structure:**

```
<cpix:DRMSystem kid="dda7afc9-..." systemId="edef8ba9-79d6-4ace-a3c8-27dcd51d21ed">
  <cpix:PSSH>BASE64_ENCODED_PSSH_BOX</cpix:PSSH>
  <cpix:ContentProtectionData>BASE64_ENCODED_CENC_PSSH_XML</cpix:ContentProtectionData>
  <cpix:HLSSignalingData playlist="media">BASE64_ENCODED_EXT_X_KEY</cpix:HLSSignalingData>
  <cpix:HLSSignalingData playlist="master">BASE64_ENCODED_EXT_X_SESSION_KEY</cpix:HLSSignalingData>
</cpix:DRMSystem>
```

Widevine includes PSSH box, ContentProtectionData, and HLS signaling. All values are base64-encoded.

**PSSH Box:** Base64-encoded binary data containing the Widevine PSSH box. The box structure is:

```
  [4 bytes] Box size (big-endian uint32)
  [4 bytes] Box type: "pssh"
  [1 byte]  Version: 0
  [3 bytes] Flags: 0
  [16 bytes] System ID: edef8ba9-79d6-4ace-a3c8-27dcd51d21ed (Widevine)
  [4 bytes] Data size (big-endian uint32)
  [N bytes] Widevine PSSH data (protobuf-encoded, contains key IDs and provider)
```

**ContentProtectionData (base64-decoded):** Must use the standard CENC PSSH XML format:

```
<cenc:pssh xmlns:cenc="urn:mpeg:cenc:2013">PSSH_BOX_BASE64</cenc:pssh>
```

The PSSH\_BOX\_BASE64 inside `cenc:pssh` is the same base64-encoded PSSH box as in the `cpix:PSSH` element.

**Decoded HLS signaling:** The URI must be a data URI with the PSSH box embedded inline:

```
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="data:text/plain;base64,<PSSH_BOX_BASE64>",KEYFORMAT="urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed",KEYFORMATVERSIONS="1"
```

**Important**  
The URI must be a `data:text/plain;base64,` data URI containing the PSSH box — NOT a license server URL (e.g., `https://widevine.example.com/license`). ContentProtectionData must use the `cenc:pssh` format — NOT custom wrappers like `<ContentProtectionData><PSSH>...</PSSH></ContentProtectionData>`. Do NOT include a `SCHEME` attribute in HLS tags.

### PlayReady signaling
<a name="speke-v2-playready"></a>

**Response XML structure:**

```
<cpix:DRMSystem kid="566209fc-..." systemId="9a04f079-9840-4286-ab92-e65be0885f95">
  <cpix:PSSH>BASE64_ENCODED_PSSH_BOX</cpix:PSSH>
  <cpix:ContentProtectionData>BASE64_ENCODED_CENC_PSSH_AND_MSPR_PRO</cpix:ContentProtectionData>
  <cpix:HLSSignalingData playlist="media">BASE64_ENCODED_EXT_X_KEY</cpix:HLSSignalingData>
  <cpix:HLSSignalingData playlist="master">BASE64_ENCODED_EXT_X_SESSION_KEY</cpix:HLSSignalingData>
</cpix:DRMSystem>
```

PlayReady includes PSSH box, ContentProtectionData (with both CENC and PRO elements), and HLS signaling.

**PSSH Box:** Base64-encoded binary data containing the PlayReady PSSH box. The box structure is:

```
  [4 bytes] Box size (big-endian uint32)
  [4 bytes] Box type: "pssh"
  [1 byte]  Version: 0
  [3 bytes] Flags: 0
  [16 bytes] System ID: 9a04f079-9840-4286-ab92-e65be0885f95 (PlayReady)
  [4 bytes] Data size (big-endian uint32)
  PlayReady Object (PRO) record:
    [4 bytes] Record count (little-endian uint32, always 1)
    [4 bytes] Record size (little-endian uint32)
    [N bytes] WRM Header XML (UTF-16LE encoded)
```

The WRM Header XML contains `KID`, `CHECKSUM`, `LA_URL` (license acquisition URL), `ALGID`, and `KEYLEN` elements for each content key.

**ContentProtectionData (base64-decoded):** Must contain BOTH `cenc:pssh` AND `mspr:pro` elements:

```
<cenc:pssh xmlns:cenc="urn:mpeg:cenc:2013">PSSH_BASE64</cenc:pssh>
<mspr:pro xmlns:mspr="urn:microsoft:playready">PRO_RECORD_BASE64</mspr:pro>
```

The `cenc:pssh` contains the full PSSH box. The `mspr:pro` contains the PlayReady Object record (count \+ size \+ WRM Header XML in UTF-16LE).

**Decoded HLS signaling (attribute order: METHOD, KEYFORMAT, KEYFORMATVERSIONS, URI):** The data URI must use `charset=UTF-16` and contain the PlayReady Object record (PRO), NOT the raw PSSH box:

```
#EXT-X-KEY:METHOD=SAMPLE-AES,KEYFORMAT="com.microsoft.playready",KEYFORMATVERSIONS="1",URI="data:text/plain;charset=UTF-16;base64,<PRO_RECORD_BASE64>"
```

**Important**  
The data URI must use `charset=UTF-16` and embed the PlayReady Object record, NOT the raw PSSH box. The PRO record structure: count(4 bytes LE) \+ size(4 bytes LE) \+ WRM Header XML (UTF-16LE). Attribute order must be METHOD, KEYFORMAT, KEYFORMATVERSIONS, URI. ContentProtectionData must include BOTH `cenc:pssh` AND `mspr:pro`. Omitting either will cause failures. Do NOT include a `SCHEME` attribute.

### Clear Key AES-128 signaling
<a name="speke-v2-clearkey-aes128"></a>

**Response XML structure:**

```
<cpix:DRMSystem kid="136436ea-..." systemId="3ea8778f-7742-4bf9-b18b-e834b2acbd47">
  <cpix:HLSSignalingData playlist="media">BASE64_ENCODED_EXT_X_KEY</cpix:HLSSignalingData>
  <cpix:HLSSignalingData playlist="master">BASE64_ENCODED_EXT_X_SESSION_KEY</cpix:HLSSignalingData>
</cpix:DRMSystem>
```

Clear Key AES-128 uses only HLS signaling (no PSSH or ContentProtectionData).

**Decoded HLS signaling:**

```
#EXT-X-KEY:METHOD=AES-128,URI="https://<key_server>/client/<content_id>/<kid>",KEYFORMAT="identity",KEYFORMATVERSIONS="1"
```

The key delivery endpoint must return the raw 16-byte binary key (not base64) with CORS headers. No DRM license server is needed — the player fetches the key directly.

## Key delivery to players
<a name="speke-v2-key-delivery"></a>


| DRM System | Player-side key delivery | License server required | 
| --- | --- | --- | 
| Clear Key AES-128 | Player GETs raw 16-byte key from HTTPS URL in manifest | No | 
| FairPlay | Player contacts FPS license server using skd:// URI | Yes (Apple FPS license) | 
| Widevine | Player uses EME API with PSSH from data URI | Yes (Google/3rd party) | 
| PlayReady | Player uses EME API with PRO from data URI | Yes (Microsoft/3rd party) | 

## Testing and verification
<a name="speke-v2-testing"></a>

**Verify your SPEKE v2.0 implementation**

1. **Test SPEKE endpoint directly.** Send a POST request with a CPIX XML body and verify the response contains `contentId`, `version="2.3"`, `PlainValue` with 16-byte base64 key, `explicitIV`, base64-encoded HLSSignalingData, and echoed ContentKeyPeriodList.

1. **Verify key determinism.** Send the same request twice. The `PlainValue` should be identical both times.

1. **Verify HLS signaling.** Decode the base64 HLSSignalingData and verify: FairPlay uses `skd://` with JSON payload, Widevine uses `data:text/plain;base64,` with PSSH, PlayReady uses `data:text/plain;charset=UTF-16;base64,` with PRO, no SCHEME attribute, media and master tags match.

1. **Test with MediaPackage.** Configure a MediaPackage endpoint with SPEKE encryption, start a live stream, check server logs for requests, and verify playback.

## Implementation checklist
<a name="speke-v2-checklist"></a>
+ HTTP endpoint accepts POST with `Content-Type: application/xml`
+ Validates and echoes `X-Speke-Version` header
+ Returns `X-Speke-User-Agent` response header
+ Validates `contentId`, `version`, `commonEncryptionScheme`
+ Returns HTTP 422 with exact error messages per SPEKE specification
+ Generates deterministic 16-byte AES keys with `explicitIV`
+ Generates per-kid DRMSystem elements
+ Base64-encodes all HLSSignalingData, PSSH, and ContentProtectionData
+ FairPlay: `skd://` URI contains base64-encoded JSON with ContentId, KeyId (with hyphens), and IV
+ Widevine: HLS URI uses `data:text/plain;base64,<PSSH>`; ContentProtectionData uses `cenc:pssh`
+ PlayReady: HLS URI uses `data:text/plain;charset=UTF-16;base64,<PRO>`; ContentProtectionData includes both `cenc:pssh` and `mspr:pro`; attribute order METHOD, KEYFORMAT, KEYFORMATVERSIONS, URI
+ Clear Key AES-128: provides GET endpoint returning raw 16-byte key with CORS headers
+ HLS media and master tags have identical attributes; no SCHEME attribute
+ Echoes ContentKeyPeriodList and ContentKeyUsageRuleList unchanged
+ Includes VideoFilter and/or AudioFilter in usage rules