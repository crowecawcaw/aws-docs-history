# AWS CloudHSM key management best practices

Follow the best practices in this section when managing keys in AWS CloudHSM.


## Choose the right key type


When using a session key, your transactions per second (TPS) will be limited to one HSM where the key exists. Extra HSMs in your cluster will not increase the throughput of requests for that key. 
 If you use a token key for the same application, your requests will be load balanced across all available HSMs in your cluster. For more information, see [Key synchronization and durability settings in AWS CloudHSM](manage-key-sync.md "manage-key-sync.md").


## Manage key storage limits


HSMs have limits on the maximum number of token and session keys that can be stored on an HSM at a single time. 
 For information on key storage limits, see [AWS CloudHSM quotas](limits.md "limits.md"). If your application requires more than the limit, 
 you can use one or more of the following strategies to effectively manage keys:


**Use trusted wrapping to store your keys in an external data store**: Using trusted key wrapping, you can overcome the key storage limit by storing all of your keys wrapped 
 inside an external data store. When you are required to use this key, you can unwrap the key into the HSM as a session key, use the key for your required operation, and then discard the session key. 
 The original key data remains safely stored in your data store for use whenever you need it. Using trusted keys to do this maximizes your protection. 
 
 


**Distribute keys across clusters**: Another strategy for overcoming the key storage limit is storing your keys in multiple clusters. 
 In this approach, you maintain a mapping of the keys that are stored in each cluster. Use this mapping to route your client requests to the cluster with the required key. 
 For information on how to connect to multiple clusters from the same client application, see the following topics:



* [Connecting to multiple AWS CloudHSM clusters with the JCE
 provider](java-lib-configs-multi.md "java-lib-configs-multi.md")
* [Multiple slot configuration with PKCS #11 library for
 AWS CloudHSM](pkcs11-library-configs-multi-slot.md "pkcs11-library-configs-multi-slot.md")

## Managing and securing key wrapping


Keys may be marked either extractable or non-extractable through the `EXTRACTABLE` attribute. By default, HSM keys are marked as extractable.


Extractable keys are keys that are permitted to be exported from the HSM through key wrapping. 
 Keys that are wrapped are encrypted, and must be unwrapped using the same wrapping key before they can be used.
 Non-extractable keys may not be exported from the HSM under any circumstance. There is no way to make a non-extractable key extractable. 
 For this reason, it is important to consider whether you require your keys to be extractable or not and to set the corresponding key attribute accordingly.


If you require key wrapping in your application, you should utilize trusted key wrapping to limit the ability of your HSM users to only wrap/unwrap keys which have been explicitly marked as trusted by an admin. 
 For more information, see topics on trusted key wrapping in [Keys in AWS CloudHSM](manage-keys.md "manage-keys.md").


Related resources



* [Wrap and Unwrap functions](pkcs11-mechanisms.md#pkcs11-mech-function-wrap-unwrap "pkcs11-mechanisms.md#pkcs11-mech-function-wrap-unwrap")
* [Cipher functions for JCE](java-lib-supported_5.md#java-ciphers_5 "java-lib-supported_5.md#java-ciphers_5")
* [Supported Java key attributes for AWS CloudHSM
 Client SDK 5](java-lib-attributes_5.md "java-lib-attributes_5.md")
* [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
