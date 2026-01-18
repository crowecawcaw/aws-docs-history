# SPEKE API v2 - Content key encryption

You can optionally add content key encryption to your SPEKE implementation. Content key encryption guarantees full end-to-end protection by encrypting the content keys for transit, in addition to encrypting the content itself. If you don’t implement this for your key provider, you rely on the transport layer encryption plus strong authentication for security.

To use content key encryption for encryptors running in AWS Cloud, customers import certificates into the AWS Certificate Manager and then use the resulting certificate ARNs for their encryption activities. The encryptor uses the certificate ARNs and the ACM service to provide encrypted content keys to the DRM key provider.

###### Restrictions

SPEKE supports content key encryption as specified in the DASH-IF CPIX specification with the following restrictions:

- SPEKE doesn’t support digital signature verification (XMLDSIG) for request or response payloads.
- SPEKE requires 2048 RSA-based certificates.
  These restrictions are also listed in [Customizations and constraints to the DASH-IF specification](speke-constraints-v2.md "speke-constraints-v2.md").

###### Implement content key encryption

To provide content key encryption, include the following in your DRM key provider implementations:

- Handle the element `<cpix:DeliveryDataList>` in the request and response payloads.
- Provide encrypted values in the `<cpix:ContentKeyList>` of the response payloads.
  For more information about these elements, see the [DASH-IF CPIX 2.3 specification](https://dashif.org/docs/CPIX2.3/Cpix.html "https://dashif.org/docs/CPIX2.3/Cpix.html").

_Example Content Key Encryption Element `_<cpix:DeliveryDataList>_` in the Request Payload_

```
 <cpix:CPIX contentId="abc123"
    version="2.3"
    xmlns:cpix="urn:dashif:org:cpix"
    xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc">
    <cpix:DeliveryDataList>
        <cpix:DeliveryData id="<ORIGIN SERVER ID>">
            <cpix:DeliveryKey>
                <ds:X509Data>
                    <ds:X509Certificate><X.509 CERTIFICATE, BASE-64 ENCODED></ds:X509Certificate>
                </ds:X509Data>
            </cpix:DeliveryKey>
        </cpix:DeliveryData>
    </cpix:DeliveryDataList>
    <cpix:ContentKeyList>
     ...
    </cpix:ContentKeyList>
</cpix:CPIX>
```

_Example Content Key Encryption Element `_<cpix:DeliveryDataList>_` in the Response Payload_

```
 <cpix:CPIX contentId="abc123"
    version="2.3"
    xmlns:cpix="urn:dashif:org:cpix"
    xmlns:pskc="urn:ietf:params:xml:ns:keyprov:pskc">
    <cpix:DeliveryDataList>
        <cpix:DeliveryData id="<ORIGIN SERVER ID>">
            <cpix:DeliveryKey>
                <ds:X509Data>
                    <ds:X509Certificate><X.509 CERTIFICATE, BASE-64 ENCODED></ds:X509Certificate>
                </ds:X509Data>
            </cpix:DeliveryKey>
            <cpix:DocumentKey Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc">
                <cpix:Data>
                    <pskc:Secret>
                        <pskc:EncryptedValue>
                            <enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p" />
                            <enc:CipherData>
                                <enc:CipherValue><RSA CIPHER VALUE></enc:CipherValue>
                            </enc:CipherData>
                        </pskc:EncryptedValue>
                        <pskc:ValueMAC>qnei/5TsfUwDu+8bhsZrLjDRDngvmnUZD2eva7SfXWw=</pskc:ValueMAC>
                    </pskc:Secret>
                </cpix:Data>
            </cpix:DocumentKey>
            <cpix:MACMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#hmac-sha512">
                <cpix:Key>
                    <pskc:EncryptedValue>
                        <enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p" />
                        <enc:CipherData>
                            <enc:CipherValue><RSA CIPHER VALUE></enc:CipherValue>
                        </enc:CipherData>
                    </pskc:EncryptedValue>
                    <pskc:ValueMAC>DGqdpHUfFKxdsO9+EWrPjtdTCVfjPLwwtzEcFC/j0xY=</pskc:ValueMAC>
                </cpix:Key>
            </cpix:MACMethod>
        </cpix:DeliveryData>
    </cpix:DeliveryDataList>
    <cpix:ContentKeyList>
     ...
    </cpix:ContentKeyList>
</cpix:CPIX>
```

_Example Content Key Encryption Element `_<cpix:ContentKeyList>_` in the Response Payload_

The following example shows encrypted content key handling in the `<cpix:ContentKeyList>` element of the response payload. This uses the `<pskc:EncryptedValue>` element:

```
 <cpix:ContentKeyList>
     <cpix:ContentKey explicitIV="OFj2IjCsPJFfMAxmQxLGPw==" kid="98ee5596-cd3e-a20d-163a-e382420c6eff" commonEncryptionScheme="cbcs">
         <cpix:Data>
             <pskc:Secret>
                 <pskc:EncryptedValue>
                     <enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc" />
                     <enc:CipherData>
                         <enc:CipherValue>NJYebfvJ2TdMm3k6v+rLNVYb0NoTJoTLBBdbpe8nmilEfp82SKa7MkqTn2lmQBPB</enc:CipherValue>
                     </enc:CipherData>
                 </pskc:EncryptedValue>
                 <pskc:ValueMAC>t9lW4WCebfS1GP+dh0IicMs+2+jnrAmfDa4WU6VGHc4=</pskc:ValueMAC>
             </pskc:Secret>
         </cpix:Data>
     </cpix:ContentKey>
 </cpix:ContentKeyList>
```

By comparison, the following example shows a similar response payload with the content key delivered unencrypted, as a clear key. This uses the `<pskc:PlainValue>` element:

```
 <cpix:ContentKeyList>
    <cpix:ContentKey explicitIV="OFj2IjCsPJFfMAxmQxLGPw==" kid="98ee5596-cd3e-a20d-163a-e382420c6eff" commonEncryptionScheme="cbcs">
        <cpix:Data>
            <pskc:Secret>
                <pskc:PlainValue>5dGAgwGuUYu4dHeHtNlxJw==</pskc:PlainValue>
            </pskc:Secret>
        </cpix:Data>
    </cpix:ContentKey>
</cpix:ContentKeyList>
```
