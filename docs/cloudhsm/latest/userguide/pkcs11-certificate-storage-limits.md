

# Certificate storage limits
<a name="pkcs11-certificate-storage-limits"></a>

 The following limits apply to certificate storage. You can't change these limits. The maximum number of stored certificates applies to each cluster. The read and write rate limits apply to each HSM, so the total rate that a cluster supports increases as you add HSMs. 


| Limit | Value | Scope | 
| --- | --- | --- | 
| Maximum stored certificates | 60 | Each cluster | 
| Read operations per second | 10 | Each HSM | 
| Write operations per second | 1 | Each HSM | 

 Read operations include `C_FindObjectsInit` and `C_GetAttributeValue`. Write operations include `C_CreateObject`, `C_SetAttributeValue`, and `C_DestroyObject`. 

The following behaviors apply when you exceed these limits:
+  If you exceed the maximum number of stored certificates, the `C_CreateObject` operation returns `CKR_FUNCTION_FAILED`, and certificate storage records a `MaxObjectsReached` error in your certificate storage audit logs. Your existing certificates remain readable. To store additional certificates, delete certificates that you no longer need. 
+  If you exceed the read or write rate limit, certificate storage throttles the request and operations return `CKR_FUNCTION_FAILED`, except for `C_GetAttributeValue`, which returns `CKR_DEVICE_ERROR` (see [Issue: `C_GetAttributeValue` returns `CKR_DEVICE_ERROR` when throttled](ki-pkcs11-sdk.md#ki-pkcs11-15)). The PKCS \#11 library does not retry throttled certificate storage operations (see [Issue: The PKCS \#11 library does not retry throttled certificate storage operations](ki-pkcs11-sdk.md#ki-pkcs11-16)), so your application must retry them with exponential backoff. For more information, see [HSM throttling](troubleshoot-hsm-throttling.md). 

 To stay within the read rate limit, reduce the number of read operations that your application sends. Each `C_GetAttributeValue` call counts as one read operation, whatever the number of attributes in the template. An application that requests every attribute it needs in one call uses one read operation. An application that makes a separate call for each attribute uses one read operation for each of them. Adding HSMs increases the total rate that your cluster supports, but it does not change this ratio. For more information, see [Retrieve attributes with the PKCS \#11 library for AWS CloudHSM Client SDK 5](pkcs11-attributes-retrieve.md). 