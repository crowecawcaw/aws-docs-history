

# SPEKE API v2.1 - Standard payload components
<a name="standard-payload-components-v2-1"></a>

Through a single SPEKE request, the encryptor can request multiple content keys, together with the necessary manifest signaling for multiple packaging formats, according to the encryption contract that the encryptor defines for the content.

To cover all these aspects, a standard CPIX document contains three mandatory list sections and an optional list section for live content key rotation.

**<cpix:ContentKeyList> section and top level <cpix:CPIX> element**  
This is a mandatory section, relevant for both Live and VOD streaming, defining the different content keys that need to be used by the encryptor. The `<cpix:ContentKeyList>` element can contain one or several `<cpix:ContentKey>` child elements, each of them describing a distinct content key.

According to the CPIX 2.4 specification, the value of the `ContentKey@commonEncryptionScheme` attribute shall be a 4-character Common Encryption protection scheme name as defined in ISO/IEC 23001-7:2016, or one of the encryption methods defined in the HTTP Live Streaming (HLS) specification. The 4-character Common Encryption protection scheme names are:
+ 'cenc': AES-CTR mode full sample and video NAL Subsample encryption
+ 'cbc1': AES-CBC mode full sample and video NAL Subsample encryption
+ 'cens': AES-CTR mode partial video NAL pattern encryption
+ 'cbcs': AES-CBC mode partial video NAL pattern encryption

The following example shows a CPIX document with a single, non encrypted, content key:

```
<cpix:CPIX contentId="abc123" version="2.4" xmlns:cpix="urn:dashif:org:cpix" xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc">
	<cpix:ContentKeyList>
		<cpix:ContentKey explicitIV="OFj2IjCsPJFfMAxmQxLGPw==" kid="98ee5596-cd3e-a20d-163a-e382420c6eff" commonEncryptionScheme="cbcs">
			<cpix:Data>
				<pskc:Secret>
					<pskc:PlainValue>5dGAgwGuUYu4dHeHtNlxJw==</pskc:PlainValue>
				</pskc:Secret>
			</cpix:Data>
		</cpix:ContentKey>
	</cpix:ContentKeyList>
	...
</cpix:CPIX>
```

By default, content keys are not encrypted, as in the preceding example. But the encryptor can request content key encryption by including the <cpix:DeliveryDataList> element. For more information, see [Content key encryption](content-key-encryption-v2-1.md).


| Element supported by SPEKE | Mandatory attributes | Optional attributes | Mandatory child elements | Optional child elements | 
| --- | --- | --- | --- | --- | 
| <cpix:CPIX> | contentId, version, xmlns:cpix, xmlns:pskc | name, xmlns:enc | one <cpix:ContentKeyList>, one <cpix:DRMSystemList>, one <cpix:ContentKeyUsageRuleList> | one <cpix:DeliveryDataList>, one <cpix:ContentKeyPeriodList> | 
| <cpix:ContentKeyList> | - | id | at least one <cpix:ContentKey> | - | 
| <cpix:ContentKey> | kid, commonEncryptionScheme | id, Algorithm, explicitIV | one <cpix:Data> (containing one <pskc:Secret>) | HDCPData | 
| <pskc:Secret> | - | - | PlainValue or EncryptedValue | ValueMAC, <enc:EncryptionMethod>, <enc:CipherData> | 
| <cpix:HDCPData> | - | HLSHDCPLevel | - | HDCPOutputProtectionData | 

**<cpix:DRMSystemList> section**  
This is a mandatory section, relevant for both Live and VOD streaming, defining the different DRM systems that need to be leveraged together with the content keys.

The following example shows a DRM system list with a single PlayReady DRM system specification:

```
<cpix:DRMSystemList>
	<cpix:DRMSystem kid="98ee5596-cd3e-a20d-163a-e382420c6eff" systemId="9a04f079-9840-4286-ab92-e65be0885f95">
		<cpix:HLSSignalingData playlist="media">HicXmbZ2m[...]4==</cpix:HLSSignalingData>
		<cpix:HLSSignalingData playlist="master">HicXmbZ2m[...]jEi</cpix:HLSSignalingData>
		<cpix:ContentProtectionData>t7WwH24FI[...]YCC</cpix:ContentProtectionData>
		<cpix:PSSH>FFFFanBzc[...]A==</cpix:PSSH>
		<cpix:SmoothStreamingProtectionHeaderData>s5RrJ12HL[...]UBB</cpix:SmoothStreamingProtectionHeaderData>
	</cpix:DRMSystem>
</cpix:DRMSystemList>
```

For a complete list of DRM systemIDs, see the [Content Protection section](https://dashif.org/identifiers/content_protection/) of the DASH-IF Identifiers repository.


| Element supported by SPEKE | Mandatory attributes | Optional attributes | Mandatory child elements | Optional child elements | 
| --- | --- | --- | --- | --- | 
| <cpix:DRMSystemList> | - | id | at least one <cpix:DRMSystem> | - | 
| <cpix:DRMSystem> | kid, systemId | id, name, PSSH, HLSAllowedCPC | - | ContentProtectionData, SmoothStreamingProtectionHeaderData, two <cpix:HLSSignalingData> elements with different playlist attribute value | 
| <cpix:ContentProtectionData> | - | robustness | - | - | 

 `DRMSystem@PSSH` is mandatory if ISO-BMFF encapsulation is applied to media segments. The encryptor uses the `DRMSystem.ContentProtectionData` innerXML `<pssh>` element only for manifest signaling purposes.

If `DRMSystem@PSSH` is present and `DRMSystem.ContentProtectionData` contains an innerXML `<pssh>` element, both values shall be identical.

To carry `DRMSystem` signaling in HLS manifests, include both a `<cpix:HLSSignalingData playlist="media">` element and a `<cpix:HLSSignalingData playlist="master">` element in the CPIX request and response.

SPEKE v2.1 can signal the expected DRM robustness or content protection level for each DRM system. DASH and HLS express this through different attributes, described in the following paragraphs.

In SPEKE v2.1, the `<cpix:ContentProtectionData>` element supports an optional `@robustness` attribute. The value of this attribute is DRM specific and announces the robustness level that is expected from the DRM system for the representations that are encrypted by the referenced content key. The encryptor uses this value as the `@robustness` attribute of the `ContentProtection` element in the DASH manifest for this DRM system.

In SPEKE v2.1, the `<cpix:DRMSystem>` element supports an optional `@HLSAllowedCPC` attribute. For the DRM identified by the `@systemId` value, this attribute specifies the value to add in the `ALLOWED-CPC` attribute of the `EXT-X-STREAM-INF` tag in the HLS multivariant playlist. The `ALLOWED-CPC` attribute announces the content protection configuration (CPC) that the DRM system supports for the associated content key. This attribute has meaning only when an HLS playlist is created for the media content.

**<cpix:ContentKeyPeriodList> section**  
This is an optional section, relevant for both Live and VOD streaming, defining the crypto periods applied to the content.

The `<cpix:ContentKeyPeriodList>` element can contain one or several `<cpix:ContentKeyPeriod>` child elements, each of them describing a distinct crypto period in the live timeline. Using UUIDs as part of the value of the id attribute is a commonly used approach.

In SPEKE v2.1, the encryptor can signal the time interval that a `<cpix:ContentKeyPeriod>` covers, in addition to the `@index`:
+ For Live content, the `@start` attribute is the wall clock time for the start of the period, and the `@end` attribute is the wall clock time for the end of the period. Both are of type `xs:dateTime`.
+ For VOD content, the `@startOffset` attribute is the start time for the period, and the `@endOffset` attribute is the end time for the period. Both are of type `xs:duration`.

```
<cpix:ContentKeyPeriodList>
	<cpix:ContentKeyPeriod id="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f" index="1" start="2026-01-01T00:00:00Z" end="2026-01-01T00:00:06Z" />
</cpix:ContentKeyPeriodList>
```


| Element supported by SPEKE | Mandatory attributes | Optional attributes | Mandatory child elements | Optional child elements | 
| --- | --- | --- | --- | --- | 
| <cpix:ContentKeyPeriodList> | - | id | at least one <cpix:ContentKeyPeriod> | - | 
| <cpix:ContentKeyPeriod> | id, index | start, end, startOffset, endOffset | - | - | 

If crypto periods are used, the encryption keys also need to be attached to one of the crypto periods in the CPIX document, as shown in the following section.

**<cpix:ContentKeyUsageRuleList> section**  
This is a mandatory section, relevant for both Live and VOD streaming, defining how the different content keys will protect tracks inside the streamset and across the crypto periods.

The <cpix:ContentKeyUsageRuleList> element can contain one or several <cpix:ContentKeyUsageRule> child elements, each of them describing the tracks to which a given content key is applied by the encryptor, potentially during a specific crypto period. At least one <cpix:AudioFilter> or one <cpix:VideoFilter> element is required to be present in a <cpix:ContentKeyUsageRule> element.

The following example shows a simple list with only one rule applying a single content key to all audio and video tracks during a specific crypto period.

```
<cpix:ContentKeyUsageRuleList>
	<cpix:ContentKeyUsageRule kid="98ee5596-cd3e-a20d-163a-e382420c6eff" intendedTrackType="ALL">
		<cpix:KeyPeriodFilter periodId="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f"/>
		<cpix:AudioFilter />
		<cpix:VideoFilter />
	</cpix:ContentKeyUsageRule>
</cpix:ContentKeyUsageRuleList>
```


| Element supported by SPEKE | Mandatory attributes | Optional attributes | Mandatory child elements | Optional child elements | 
| --- | --- | --- | --- | --- | 
| <cpix:ContentKeyUsageRuleList> | - | id | at least one <cpix:ContentKeyUsageRule> | - | 
| <cpix:ContentKeyUsageRule> | kid, intendedTrackType | - | at least one <cpix:AudioFilter> or one <cpix:VideoFilter> (\*) | <cpix:KeyPeriodFilter> | 
| <cpix:KeyPeriodFilter> | periodId | - | - | - | 
| <cpix:AudioFilter> | - | minChannels, maxChannels | - | - | 
| <cpix:VideoFilter> | - | minPixels, maxPixels, hdr, minFps, maxFps | - | - | 

 *(\*) For a detailed explanation on the use of single or of multiple content keys to protect one or several tracks in a streamset, see the [Encryption Contract](encryption-contract-v2-1.md) documentation section.\_* 