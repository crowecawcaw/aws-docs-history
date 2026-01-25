# SPEKE API v2 - Standard payload components

Through a single SPEKE request, the encryptor can request multiple content keys, together with the necessary manfest signaling for multiple packaging formats, according to the encryption contract that is defined for a given content.

In order to cover all these aspects, a standard CPIX document is composed of three mandatory list sections, plus an optional list section for live content key rotation.

###### <cpix:ContentKeyList> section and top level <cpix:CPIX> element

This is a mandatory section, relevant for both Live and VOD streaming, defining the different content keys that need to be used by the encryptor. The `<cpix:ContentKeyList>` element can contain one or several `<cpix:ContentKey>` child elements, each of them describing a distinct content key.

As per the CPIX specification, the possible values of the `ContentKey@commonEncryptionScheme` attribute are defined in the Common encryption in ISO base media file format files specification (ISO/IEC 23001-7:2016):

- 'cenc': AES-CTR mode full sample and video NAL Subsample encryption
- 'cbc1': AES-CBC mode full sample and video NAL Subsample encryption
- 'cens': AES-CTR mode partial video NAL pattern encryption
- 'cbcs': AES-CBC mode partial video NAL pattern encryption
  The following example shows a CPIX document with a single, non encrypted, content key:

```
<cpix:CPIX contentId="abc123" version="2.3" xmlns:cpix="urn:dashif:org:cpix" xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc">
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

By default, content keys are not encrypted, as in the example below. But the encryption of content keys can be requested by the encryptor through the inclusion of the <cpix:DeliveryDataList> element. Please refer to the Content Key Encryption section for more details.

| Element supported by SPEKE | Mandatory attributes                       | Optional attributes       | Mandatory child elements                                                                | Optional child elements                                      |
| -------------------------- | ------------------------------------------ | ------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| <cpix:CPIX>                | contentId, version, xmlns:cpix, xmlns:pskc | name, xmlns:enc           | one <cpix:ContentKeyList>, one <cpix:DRMSystemList>, one <cpix:ContentKeyUsageRuleList> | one <cpix:DeliveryDataList>, one <cpix:ContentKeyPeriodList> |
| <cpix:ContentKeyList>      | -                                          | id                        | at least one <cpix:ContentKey>                                                          | -                                                            |
| <cpix:ContentKey>          | kid, commonEncryptionScheme, Data          | id, Algorithm, explicitIV | one <pskc:Secret>                                                                       | -                                                            |
| <pskc:Secret>              | PlainValue or EncryptedValue               | ValueMAC                  | -                                                                                       | <enc:EncryptionMethod>, <enc:CipherData>                     |

###### <cpix:DRMSystemList> section

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

For a complete list of DRM systemIDs, please refer to the [Content Protection section](https://dashif.org/identifiers/content_protection/ "https://dashif.org/identifiers/content_protection/") of the DASH-IF Identifiers repository.

| Element supported by SPEKE | Mandatory attributes | Optional attributes | Mandatory child elements      | Optional child elements                                                                                                                  |
| -------------------------- | -------------------- | ------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| <cpix:DRMSystemList>       | -                    | id                  | at least one <cpix:DRMSystem> | -                                                                                                                                        |
| <cpix:DRMSystem>           | kid, systemId        | id, name, PSSH      | -                             | ContentProtectionData, SmoothStreamingProtectionHeaderData, two <cpix:HLSSignalingData> elements with different playlist attribute value |

`DRMSystem@PSSH` is mandatory if ISO-BMFF encapsulation is applied to media segments. `DRMSystem.ContentProtectionData` innerXML `<pssh>` element is leveraged by the encryptor only for manifest signaling purposes.

If `DRMSystem@PSSH` is present and `DRMSystem.ContentProtectionData` contains a innerXML `<pssh>` element, both values shall be identical.

If `DRMSystem` signaling is to be carried in HLS manifests, both a `<cpix:HLSSignalingData playlist="media">` and a `<cpix:HLSSignalingData playlist="master">` elements must be included in the CPIX request and response.

###### <cpix:ContentKeyPeriodList> section

This is an optional section, relevant only for Live streaming, defining the crypto periods applied to the content.

The `<cpix:ContentKeyPeriodList>` element can contain one or several `<cpix:ContentKeyPeriod>` child elements, each of them describing a distinct crypto period in the live timeline. Using UUIDs as part of the value of the id attribute is a commonly used approach.

```
<cpix:ContentKeyPeriodList>
	<cpix:ContentKeyPeriod id="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f" index="1" />
</cpix:ContentKeyPeriodList>
```

| Element supported by SPEKE  | Mandatory attributes | Optional attributes | Mandatory child elements             | Optional child elements |
| --------------------------- | -------------------- | ------------------- | ------------------------------------ | ----------------------- |
| <cpix:ContentKeyPeriodList> | -                    | id                  | at least one <cpix:ContentKeyPeriod> | -                       |
| <cpix:ContentKeyPeriod>     | id, index            | -                   | -                                    | -                       |

If crypto periods are used, the encryption keys also need to be attached to one of the crypto periods in the CPIX document, as shown in the section below.

###### <cpix:ContentKeyUsageRuleList> section

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

| Element supported by SPEKE     | Mandatory attributes   | Optional attributes                       | Mandatory child elements                                       | Optional child elements |
| ------------------------------ | ---------------------- | ----------------------------------------- | -------------------------------------------------------------- | ----------------------- |
| <cpix:ContentKeyUsageRuleList> | -                      | id                                        | at least one <cpix:ContentKeyUsageRule>                        | -                       |
| <cpix:ContentKeyUsageRule>     | kid, intendedTrackType | -                                         | at least one <cpix:AudioFilter> or one <cpix:VideoFilter> (\*) | <cpix:KeyPeriodFilter>  |
| <cpix:KeyPeriodFilter>         | periodId               | -                                         | -                                                              | -                       |
| <cpix:AudioFilter>             | -                      | minChannels, maxChannels                  | -                                                              | -                       |
| <cpix:VideoFilter>             | -                      | minPixels, maxPixels, hdr, minFps, maxFps | -                                                              | -                       |

_(\*) For a detailed explanation on the use of single or of multiple content keys to protect one or several tracks in a streamset, please refer to the [Encryption Contract](encryption-contract-v2.md "encryption-contract-v2.md") documentation section.\__
