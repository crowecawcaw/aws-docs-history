# Container and DRM system support with

SPEKE

MediaConvert supports both [SPEKE Version 1.0](../../../speke/latest/documentation/the-speke-api.md "../../../speke/latest/documentation/the-speke-api.md") and [SPEKE Version
2.0](../../../speke/latest/documentation/the-speke-api-v2.md "../../../speke/latest/documentation/the-speke-api-v2.md"). For more information, see the [SPEKE partner and customer guide](../../../speke/latest/documentation/speke-api-specification.md "../../../speke/latest/documentation/speke-api-specification.md").

**SPEKE v1.0 Supported containers and DRM systems**

The following table lists the different containers and digital rights management (DRM)
systems that SPEKE Version 1.0 supports.

SPEKE v1.0 DRM support| **Output group type** | **Apple Fairplay** | **Google Widevine** | **Microsoft PlayReady** |
| **DASH** | _Not supported_ | Supported | Supported |
| **Apple HLS** | Supported | _Not supported_ | _Not supported_ |
| **Microsoft Smooth** | _Not supported_ | _Not supported_ | Supported |
| **CMAF DASH** and **CMAF HLS** | Supported | Supported | Supported | **SPEKE v2.0 Supported containers and DRM systems** The following table lists the different containers and digital rights management (DRM) systems that SPEKE Version 2.0 supports. SPEKE v2.0 DRM support| **Output group type** | **Apple Fairplay** | **Google Widevine** | **Microsoft PlayReady** |
| **DASH** | _Not supported_ | Supported | Supported |
| **Apple HLS** | Supported (`Sample-AES`) | Supported | Supported |
| **Microsoft Smooth** | _Not supported_ | _Not supported_ | _Not supported_ |
| **CMAF DASH** and **CMAF HLS** | Supported (`CBCS`) | Supported (`CBCS` and `CENC`) | Supported (`CBCS` and `CENC`) | **Supported DRM system IDs** The following table lists the different DRM [system IDs](https://dashif.org/identifiers/content_protection/ "https://dashif.org/identifiers/content_protection/") that MediaConvert supports.
| | | | |
| --- | --- | --- | --- |
| **System IDs – Support matrix for DRM system** | **Apple FairPlay** | **Google Widevine** | **Microsoft PlayReady** |
| **System ID** | 94ce86fb-07ff-4f43-adb8-93d2fa968ca2 | edef8ba9-79d6-4ace-a3c8-27dcd51d21ed | 9a04f079-9840-4286-ab92-e65be0885f95 |
