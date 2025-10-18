# AWS CloudHSM extracting keys using JCE

Use the following sections to troubleshoot issues extracting AWS CloudHSM keys using JCE.


## getEncoded, getPrivateExponent, or getS returns null


`getEncoded`, `getPrivateExponent`, and `getS` will return null because they are by default disabled. To enable them, refer to [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md "java-lib-configs-getencoded.md").


If `getEncoded`, `getPrivateExponent`, and `getS` return null after being enabled, your key does not meet the right prerequisites. For more information, refer to [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md "java-lib-configs-getencoded.md").


## getEncoded, getPrivateExponent, or getS return key bytes outside of the HSM


You or someone with access to your system has enabled clear key extraction. 
 See the following pages for more information, including how to reset this configuration to 
 the default disabled state.



* [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md "java-lib-configs-getencoded.md")
* [Protecting and extracting keys from an HSM](bp-hsm-key-management.md#best-practices-key-protection "bp-hsm-key-management.md#best-practices-key-protection")
