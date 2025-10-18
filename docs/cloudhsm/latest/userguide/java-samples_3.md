# Code samples for the AWS CloudHSM software library for Java for
 Client SDK 3

This topic provides resources and information on Java code samples for AWS CloudHSM
 Client SDK 3.


## Prerequisites


 Before running the samples, you must set up your
 environment:



* Install and configure the [Java
 Cryptographic Extension (JCE) provider](java-library-install.md#install-java-library "java-library-install.md#install-java-library") and the [AWS CloudHSM client package](cmu-install-and-configure-client-linux.md "cmu-install-and-configure-client-linux.md").
* Set up a valid [HSM user name and
 password](manage-hsm-users.md "manage-hsm-users.md"). Cryptographic user (CU) permissions are sufficient for
 these tasks. Your application uses these credentials to log in to the HSM in
 each example.
* Decide how to provide credentials to the [JCE provider](java-library-install.md#java-library-credentials "java-library-install.md#java-library-credentials").

## Code samples


The following code samples show you how to use the [AWS CloudHSM
 JCE provider](java-library.md "java-library.md") to perform basic tasks. More code samples are available on [GitHub](https://github.com/aws-samples/aws-cloudhsm-jce-examples/ "https://github.com/aws-samples/aws-cloudhsm-jce-examples/").



* [Log in to an HSM](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/LoginRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/LoginRunner.java")
* [Manage keys](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java")
* [Generate an AES key](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/SymmetricKeys.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/SymmetricKeys.java")
* [Encrypt and decrypt with AES-GCM](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESGCMEncryptDecryptRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESGCMEncryptDecryptRunner.java")
* [Encrypt and decrypt with AES-CTR]( https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESCTREncryptDecryptRunner.java " https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESCTREncryptDecryptRunner.java")
* [Encrypt and decrypt with D3DES-ECB]( https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/DESedeECBEncryptDecryptRunner.java " https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/DESedeECBEncryptDecryptRunner.java")**see note [1](#java-samples-code-note-1 "#java-samples-code-note-1")**
* [Wrap and unwrap keys with AES-GCM](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESGCMWrappingRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESGCMWrappingRunner.java")
* [Wrap and unwrap keys with AES](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESWrappingRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/AESWrappingRunner.java")
* [Wrap and unwrap keys with RSA](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/RSAWrappingRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/RSAWrappingRunner.java")
* [Use supported key attributes](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/CustomKeyAttributesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/CustomKeyAttributesRunner.java")
* [Enumerate keys in the key store](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyStoreExampleRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyStoreExampleRunner.java")
* [Use the CloudHSM key store](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/CloudHSMKeyStoreExampleRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/CloudHSMKeyStoreExampleRunner.java")
* [Sign messages in a multi-threaded sample](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/SignThreadedRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/SignThreadedRunner.java")
* [Sign and Verify with EC Keys](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/ECOperationsRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/ECOperationsRunner.java")

[1] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details.
