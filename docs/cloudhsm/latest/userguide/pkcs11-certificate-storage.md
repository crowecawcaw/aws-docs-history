# Certificate storage with the PKCS #11 library


 The AWS CloudHSM PKCS #11 library supports storing public key certificates as "public objects" (as defined in PKCS #11 2.40) on hsm2m.medium clusters. This feature allows both public and private PKCS #11 sessions to create, retrieve, modify, and delete public key certificates.
 


 To use certificate storage with the PKCS #11 library, you need to enable it in your client configuration. Once enabled, you can manage certificate objects from your PKCS #11 applications. Operations that apply to both certificate and key objects, such as [C\_FindObjects](http://docs.oasis-open.org/pkcs11/pkcs11-base/v2.40/os/pkcs11-base-v2.40-os.html#_Toc323205461 "http://docs.oasis-open.org/pkcs11/pkcs11-base/v2.40/os/pkcs11-base-v2.40-os.html#_Toc323205461"), will return results from both key and certificate storage.
 

###### Topics

* [Enable certificate storage](pkcs11-certificate-storage-configuration.md "pkcs11-certificate-storage-configuration.md")
* [Certificate storage API](pkcs11-certificate-storage-api.md "pkcs11-certificate-storage-api.md")
* [Certificate attributes](pkcs11-certificate-storage-attributes.md "pkcs11-certificate-storage-attributes.md")
* [Certificate storage audit logs](pkcs11-certificate-storage-audit-logs.md "pkcs11-certificate-storage-audit-logs.md")
