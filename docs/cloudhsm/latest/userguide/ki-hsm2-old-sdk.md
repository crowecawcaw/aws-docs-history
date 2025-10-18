# Known issues of operation failure using AWS CloudHSM client version 5.12.0 on hsm2.medium

The following issues impact AWS CloudHSM when using AWS CloudHSM client version 5.12.0


## Issue: Error during get-attribute operation


If you're migrating from hsm1.medium to hsm2m.medium and using CloudHSM Client SDK 5.12.0, you may observe errors related to attribute handling.


You might see the following error message in the client logs:

 `Error in deserialization of data: Invalid integer conversion`


**Impact: Below operations will fail using client version 5.12.0**



* In PKCS#11 SDK, calls to C\_GetAttributeValue fail
* In CloudHSM CLI, the key list command shows no attributes in the output
* In CloudHSM CLI, key generate-file may fail for keys generated using hsm1.medium

**Resolution:** We recommend upgrading to the latest version of the SDK which resolves this issue.
