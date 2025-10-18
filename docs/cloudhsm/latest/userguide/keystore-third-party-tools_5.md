# Use Client SDK 5 to integrate AWS CloudHSM with Java
 Keytool and Jarsigner

AWS CloudHSM key store is a special-purpose JCE key store that utilizes certificates associated
 with keys on your hardware security module (HSM) through third-party tools such as
 `keytool` and `jarsigner`. AWS CloudHSM does not store certificates on
 the HSM, as certificates are public, non-confidential data. The AWS CloudHSM key store stores the
 certificates in a local file and maps the certificates to corresponding keys on your HSM. 

When you use the AWS CloudHSM key store to generate new keys, no entries are generated in the
 local key store file – the keys are created on the HSM. Similarly, when you use the AWS CloudHSM
 key store to search for keys, the search is passed on to the HSM. When you store
 certificates in the AWS CloudHSM key store, the provider verifies that a key pair with the
 corresponding alias exists on the HSM, and then associates the certificate provided with the
 corresponding key pair. 

###### Topics

* [Prerequisites](keystore-prerequisites_5.md "keystore-prerequisites_5.md")
* [Use key store with
 keytool](using_keystore_with_keytool_5.md "using_keystore_with_keytool_5.md")
* [Use key store with Jarsigner](using_keystore_jarsigner_5.md "using_keystore_jarsigner_5.md")
* [Known issues](known-issues-keytool-jarsigner_5.md "known-issues-keytool-jarsigner_5.md")
