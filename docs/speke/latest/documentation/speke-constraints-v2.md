# SPEKE API v2 - Customizations and constraints to the DASH-IF specification

The DASH Industry Forum [CPIX 2.3 specification](https://dashif.org/docs/CPIX2.3/Cpix.html "https://dashif.org/docs/CPIX2.3/Cpix.html") supports a number of use cases and topologies. The SPEKE API v2.0 specification defines both a CPIX Profile and an API for CPIX. In order to achieve these two goals, it adheres to the CPIX specification with the following customizations and constraints:

###### CPIX Profile

- SPEKE follows the Encryptor Consumer workflow.
- For encrypted content keys, SPEKE applies the following restrictions:
  - SPEKE doesn’t support digital signature verification (XMLDSIG) for request or response payloads.
  - SPEKE requires 2048 RSA-based certificates.

- SPEKE leverages only a subset of CPIX functionalities:
  - SPEKE omits the `UpdateHistoryItemList` functionality. If the list is present in the response, SPEKE ignores it.
  - SPEKE omits the root/leaf key functionality. If the `ContentKey@dependsOnKey` attribute is present in the response, SPEKE ignores it.
  - SPEKE omits the `BitrateFilter` element and the `VideoFilter@wcg` attribute. If these elements or attributes are present in the CPIX payload, SPEKE ignores it.

- Only the elements or attributes referenced as 'Supported' on the [Standard Payload Components page](standard-payload-components-v2.md "standard-payload-components-v2.md") or the [Encryption contract page](encryption-contract-v2.md "encryption-contract-v2.md") can be used in CPIX documents exchanged with SPEKE v2.
- When included in a CPIX request by the encryptor, all elements and attributes shall carry a valid value in the key provider CPIX response. If not, the encryptor shall stop and throw an error.
- SPEKE supports key rotation with `KeyPeriodFilter` elements. SPEKE uses only the `ContentKeyPeriod@index` to track the key period.
- For HLS signaling, multiple `DRMSystem.HLSSignalingData` elements must be used: one with a `DRMSystem.HLSSignalingData@playlist` attribute value of ‘media’, and another one with a `DRMSystem.HLSSignalingData@playlist` attribute value of ‘master’.
- When requesting keys, the encryptor might use the optional `@explicitIV` attribute on the `ContentKey` element. The key provider can respond with an IV using `@explicitIV`, even if the attribute is not included in the request.
- The encryptor creates the key identifier (`KID`), which stays the same for any given content ID and key period. The key provider includes the `KID` in its response to the request document.
- The encryptor shall include a value for the `CPIX@contentId` attribute. When receiving an empty value for this attribute, the key provider shall return an error with description 'Missing CPIX@contentId'. `CPIX@contentId` value cannot be overriden by the key provider.

`CPIX@id` value, if not null, shall be ignored by the key provider.

- The encryptor shall include a value for the `CPIX@version` attribute. When receiving an empty value for this attribute, the key provider shall return an error with description 'Missing CPIX@version'. When receiving a request with an unsupported version, the error description returned by the key provider shall be 'Unsupported CPIX@version'.

`CPIX@version` value cannot be overriden by the key provider.

- The encryptor shall include a value for the `ContentKey@commonEncryptionScheme` attribute for each requested key. When receiving an empty value for this attribute, the key provider shall return an error with description 'Missing ContentKey@commonEncryptionScheme for KID `id` '.

A unique CPIX document cannot mix multiple values for different `ContentKey@commonEncryptionScheme` attributes. When receiving such a combination, the key provider shall return an error with description 'Non compliant ContentKey@commonEncryptionScheme combination'.

Not all `ContentKey@commonEncryptionScheme` values are compatible with all DRM technologies. When receiving such a combination, the key provider shall return an error with description 'ContentKey@commonEncryptionScheme non compatible with DRMSystem `id` '.

`ContentKey@commonEncryptionScheme` value cannot be overriden by the key provider.

- When receiving different values for `DRMSystem@PSSH` and `DRMSystem.ContentProtectionData` innerXML `<pssh>` element in the CPIX response body, the encryptor shall stop and throw an error.

###### API for CPIX

- The key provider shall include a value for the `X-Speke-User-Agent` HTTP response header.
- A SPEKE-compliant encryptor acts as a client and sends POST operations to the key provider endpoint.
- The encryptor shall include a value for the `X-Speke-Version` HTTP request header, with the SPEKE version used with the request, formulated as MajorVersion.MinorVersion, like '2.0' for SPEKE v2.0. If the key provider doesn’t support the SPEKE version used by the encryptor for the current request, the key provider shall return an error with description 'Unsupported SPEKE version' and not try to process the CPIX document on a best effort basis.

The `X-Speke-Version` header value defined by the encryptor cannot be modified by the key provider in the response to the request.

- When receiving errors in the response body, the encryptor shall throw an error and not retry the request with a SPEKE v1.0 versioning.

If the key provider doesn’t return an error but fails to return a CPIX document that includes the mandatory information, the encryptor should stop and throw an error.
The following table summarizes the standard messages that must be returned by the key provider in the body of the message. The HTTP response code in error cases shall be a 4XX or a 5XX, never a 200. The 422 error code can be used for all errors related to SPEKE/CPIX.

| Error case                                                                       | Error message                                                                                                     |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| CPIX@contentId is not defined                                                    | Missing CPIX@contentId                                                                                            |
| CPIX@version is not defined                                                      | Missing CPIX@version                                                                                              |
| CPIX@version is not supported                                                    | Unsupported CPIX@version                                                                                          |
| ContentKey@commonEncryptionScheme is not defined                                 | Missing ContentKey@commonEncryptionScheme for KID `id` (where `id` equals ContentKey@kid value)                   |
| Multiple ContentKey@commonEncryptionScheme values used in a single CPIX document | Non compliant ContentKey@commonEncryptionScheme combination                                                       |
| ContentKey@commonEncryptionScheme is not compatible with DRM technology          | ContentKey@commonEncryptionScheme non compatible with DRMSystem `id` (where `id` equals DRMSystem@systemId value) |
| X-Speke-Version header value is not a supported SPEKE version                    | Unsupported SPEKE version                                                                                         |
| The encryption contract is malformed                                             | Malformed encryption contract                                                                                     |
| The encryption contract contradicts DRM security levels constraints              | Requested CPIX encryption contract not supported                                                                  |
| The encryption contract doesn’t include any VideoFilter or AudioFilter element   | Missing CPIX encryption contract                                                                                  |
