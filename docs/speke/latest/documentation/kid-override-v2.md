# SPEKE API v2 - Overriding the key identifier

The encryptor creates a new key identifier (KID) each time that it rotates keys. It passes the KID to the DRM key provider in its requests. Almost always, the key provider responds using the same KID, but it can provide a different value for the KID in the response.

The following is an example request with the KID `11111111-1111-1111-1111-111111111111`:

```
<cpix:CPIX contentId="abc123" version="2.3" xmlns:cpix="urn:dashif:org:cpix" xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc">
	<cpix:ContentKeyList>
		<cpix:ContentKey explicitIV="OFj2IjCsPJFfMAxmQxLGPw==" kid="11111111-1111-1111-1111-111111111111" commonEncryptionScheme="cbcs"></cpix:ContentKey>
	</cpix:ContentKeyList>
	<cpix:DRMSystemList>
		<!-- Widevine -->
		<cpix:DRMSystem kid="11111111-1111-1111-1111-111111111111" systemId="edef8ba9-79d6-4ace-a3c8-27dcd51d21ed">
			<cpix:HLSSignalingData playlist="media"></cpix:HLSSignalingData>
			<cpix:HLSSignalingData playlist="master"></cpix:HLSSignalingData>
			<cpix:ContentProtectionData></cpix:ContentProtectionData>
			<cpix:PSSH></cpix:PSSH>
		</cpix:DRMSystem>
	</cpix:DRMSystemList>
	<cpix:ContentKeyPeriodList>
		<cpix:ContentKeyPeriod id="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f" index="1" />
	</cpix:ContentKeyPeriodList>
	<cpix:ContentKeyUsageRuleList>
		<cpix:ContentKeyUsageRule kid="11111111-1111-1111-1111-111111111111" intendedTrackType="VIDEO">
			<cpix:KeyPeriodFilter periodId="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f"/>
			<cpix:VideoFilter />
		</cpix:ContentKeyUsageRule>
	</cpix:ContentKeyUsageRuleList>
</cpix:CPIX>
```

The following response overrides the KID to `22222222-2222-2222-2222-222222222222`:

```
<cpix:CPIX contentId="abc123" version="2.3" xmlns:cpix="urn:dashif:org:cpix" xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc">
	<cpix:ContentKeyList>
		<cpix:ContentKey explicitIV="OFj2IjCsPJFfMAxmQxLGPw==" kid="22222222-2222-2222-2222-222222222222" commonEncryptionScheme="cbcs">
			<cpix:Data>
				<pskc:Secret>
					<pskc:PlainValue>5dGAgwGuUYu4dHeHtNlxJw==</pskc:PlainValue>
				</pskc:Secret>
			</cpix:Data>
		</cpix:ContentKey>
	</cpix:ContentKeyList>
	<cpix:DRMSystemList>
		<!-- Widevine -->
		<cpix:DRMSystem kid="22222222-2222-2222-2222-222222222222" systemId="edef8ba9-79d6-4ace-a3c8-27dcd51d21ed">
			<cpix:HLSSignalingData playlist="media">Ifa2V5LWl[...]nNB</cpix:HLSSignalingData>
			<cpix:HLSSignalingData playlist="master">oIARIQeSI[...]Nd2l</cpix:HLSSignalingData>
			<cpix:ContentProtectionData>RoNd2lkZXZ[...]Nib</cpix:ContentProtectionData>
			<cpix:PSSH>AAAAanBzc[...]A==</cpix:PSSH>
		</cpix:DRMSystem>
	</cpix:DRMSystemList>
	<cpix:ContentKeyPeriodList>
		<cpix:ContentKeyPeriod id="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f" index="1" />
	</cpix:ContentKeyPeriodList>
	<cpix:ContentKeyUsageRuleList>
		<cpix:ContentKeyUsageRule kid="22222222-2222-2222-2222-222222222222" intendedTrackType="VIDEO">
			<cpix:KeyPeriodFilter periodId="keyPeriod_0909829f-40ff-4625-90fa-75da3e53278f"/>
			<cpix:VideoFilter />
		</cpix:ContentKeyUsageRule>
	</cpix:ContentKeyUsageRuleList>
</cpix:CPIX>
```
