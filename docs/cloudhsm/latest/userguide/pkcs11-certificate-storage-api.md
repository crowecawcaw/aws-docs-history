# Certificate storage API operations

The following PKCS #11 operations support the certificate object type (`CKO_CERTIFICATE`):

## General certificate operations

**`C_CreateObject`**

Creates a new certificate object.

**`C_DestroyObject`**

Deletes an existing certificate object.

**`C_GetAttributeValue`**

Gets the value of one or more attributes of a certificate object.

**`C_SetAttributeValue`**

Updates the value of one or more attributes of a certificate object.

## Certificate object search operations

**`C_FindObjectsInit`**

Starts a search for certificate objects.

**`C_FindObjects`**

Continues a search for certificate objects.

**`C_FindObjectsFinal`**

Ends a search for certificate objects.

###### Throttling return codes

When certificate storage throttles an operation for exceeding the read or write rate
limit, the return code depends on the operation. Write operations
(`C_CreateObject`, `C_SetAttributeValue`, and
`C_DestroyObject`) and the `C_FindObjectsInit` read
operation return `CKR_FUNCTION_FAILED`. `C_GetAttributeValue`
currently returns `CKR_DEVICE_ERROR`. In all cases, follow the best
practices for handling throttling in
[HSM throttling](troubleshoot-hsm-throttling.md "troubleshoot-hsm-throttling.md").
