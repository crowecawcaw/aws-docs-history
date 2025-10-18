# Trusted key attributes in AWS CloudHSM

The following attributes allow you to mark an AWS CloudHSM key as trusted, specify a data key can only be wrapped and unwrapped with a trusted key, and control what a data key can do after it is unwrapped:


* `CKA_TRUSTED`: Apply this attribute (in addition to
 `CKA_UNWRAP_TEMPLATE`) to the key that will wrap data keys to specify that an admin or crypto officer (CO) has done the necessary
 diligence and trusts this key. Only an admin or CO can set `CKA_TRUSTED`. The 
 crypto user (CU) owns the key, but only a CO can set its `CKA_TRUSTED` attribute.
* `CKA_WRAP_WITH_TRUSTED`: Apply this attribute to an exportable data key
 to specify that you can only wrap this key with keys marked as `CKA_TRUSTED`.
 Once you set `CKA_WRAP_WITH_TRUSTED` to true, the attribute becomes read-only
 and you cannot change or remove the attribute.
* `CKA_UNWRAP_TEMPLATE`: Apply this attribute to the wrapping key (in
 addition to `CKA_TRUSTED`) to specify which attribute names and values the
 service must automatically apply to data keys that the service unwraps. When an
 application submits a key for unwrapping, the application can also provide its own
 unwrap template. If you specify an unwrap template and the application provides its own
 unwrap template, the HSM uses both templates to apply attribute names and
 values to the key. However, if a value in the `CKA_UNWRAP_TEMPLATE` for the
 wrapping key conflicts with an attribute provided by the application during the unwrap
 request, then the unwrap request fails.
For more information about attributes, refer to the following topics:


* [PKCS #11 key attributes](pkcs11-attributes.md "pkcs11-attributes.md")
* [JCE key attributes](java-lib-attributes_5.md "java-lib-attributes_5.md")
* [CloudHSM CLI key attributes](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md")
