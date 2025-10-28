# Set up AWS CloudHSM keys and certificates with

Jarsigner

Before you can sign AWS CloudHSM JAR files with Jarsigner, make sure you have set up or completed
the following steps:

1. Follow the guidance in the [AWS CloudHSM key store prerequisites](keystore-prerequisites_5.md "keystore-prerequisites_5.md") .
2. Set up your signing keys and the associated certificates and certificate
   chain which should be stored in the AWS CloudHSM key store of the current server or
   client instance. Create the keys on the AWS CloudHSM and then import associated
   metadata into your AWS CloudHSM key store. If you want to use keytool to set up the keys and
   certificates, see [Create new AWS CloudHSM keys with keytool](create_key_keytool_5.md "create_key_keytool_5.md"). If you use multiple client
   instances to sign your JARs, create the key and import the certificate
   chain. Then copy the resulting key store file to each client instance. If
   you frequently generate new keys, you may find it easier to individually
   import certificates to each client instance.
3. The entire certificate chain should be verifiable. For the certificate
   chain to be verifiable, you may need to add the CA certificate and
   intermediate certificates to the AWS CloudHSM key store. See the code snippet in
   [Sign a JAR file using
   AWS CloudHSM and Jarsigner](jarsigner_sign_jar_using_hsm_jarsigner_5.md "jarsigner_sign_jar_using_hsm_jarsigner_5.md") for instruction on using Java code
   to verify the certificate chain. If you prefer, you can use keytool to
   import certificates. For instructions on using keytool, see [Use keytool to import intermediate and root
   certificates into AWS CloudHSM key store](import_cert_using_keytool_5.md "import_cert_using_keytool_5.md") .
