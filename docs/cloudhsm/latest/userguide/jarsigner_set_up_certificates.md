# Set up AWS CloudHSM keys and certificates with
 Jarsigner

Before you can sign AWS CloudHSM JAR files with Jarsigner, make sure you have set up or completed
 the following steps: 


1. Follow the guidance in the [AWS CloudHSM Key store prerequisites](keystore-prerequisites.md "keystore-prerequisites.md") .
2. Set up your signing keys and the associated certificates and certificate
 chain which should be stored in the AWS CloudHSM key store of the current server or
 client instance. Create the keys on the AWS CloudHSM and then import associated
 metadata into your AWS CloudHSM key store. Use the code sample in [Registering
 Pre-existing Keys with AWS CloudHSM Key Store](register-pre-existing-keys-with-keystore.md "register-pre-existing-keys-with-keystore.md") to import metadata
 into the key store. If you want to use keytool to set up the keys and
 certificates, see [Create new AWS CloudHSM keys with keytool](create_key_keytool.md "create_key_keytool.md"). If you use multiple client
 instances to sign your JARs, create the key and import the certificate
 chain. Then copy the resulting key store file to each client instance. If
 you frequently generate new keys, you may find it easier to individually
 import certificates to each client instance.
3. The entire certificate chain should be verifiable. For the certificate
 chain to be verifiable, you may need to add the CA certificate and
 intermediate certificates to the AWS CloudHSM key store. See the code snippet in
 [Sign a JAR file
 using AWS CloudHSM and Jarsigner](jarsigner_sign_jar_using_hsm_jarsigner.md "jarsigner_sign_jar_using_hsm_jarsigner.md") for instruction on using Java code
 to verify the certificate chain. If you prefer, you can use keytool to
 import certificates. For instructions on using keytool, see [Using Keytool to import intermediate
 and root certificates into AWS CloudHSM Key Store](import_cert_using_keytool.md "import_cert_using_keytool.md").
