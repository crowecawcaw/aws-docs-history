# Offload operations with AWS CloudHSM Client SDKs

Use a Client SDK to offload cryptographic operations from platform or language-based applications to hardware security modules
 (HSMs).
 

AWS CloudHSM offers two major versions, and Client SDK 5 is the latest. It offers a variety of advantages over Client SDK 3 (the previous series). For more information, see [Benefits of Client SDK 5](client-sdk-5-benefits.md "client-sdk-5-benefits.md"). For information about platform support, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md").
 

The following topics describe how to work with AWS CloudHSM Client SDKs.

AWS CloudHSM supports the following components:



**[PKCS #11 library for AWS CloudHSM Client SDK 5](pkcs11-library.md "pkcs11-library.md")**

 
 PKCS #11 is a standard for performing cryptographic operations on hardware security modules (HSMs). 
 AWS CloudHSM offers implementations of the PKCS #11 library that are compliant with PKCS #11 version 2.40.



**[OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5](openssl-library.md "openssl-library.md")**

The AWS CloudHSM OpenSSL Dynamic Engine allows you to offload cryptographic operations to your 
 CloudHSM cluster through the OpenSSL API.



**[JCE provider for AWS CloudHSM Client SDK 5](java-library.md "java-library.md")**

The AWS CloudHSM JCE provider is compliant with the Java Cryptographic Architecture (JCA).
 The provider allows you to perform cryptographic operations on the HSM.



**[Key storage provider (KSP) for AWS CloudHSM Client SDK 5](ksp-library.md "ksp-library.md")**

The AWS CloudHSM client for Windows includes CNG and KSP providers.



###### Topics

* [Check your AWS CloudHSM Client SDK version](check-client_version.md "check-client_version.md")
* [Compare AWS CloudHSM Client SDK component support](sdk3-compare.md "sdk3-compare.md")
* [Migrating from AWS CloudHSM Client SDK 3 to
 Client SDK 5](client-sdk-migration.md "client-sdk-migration.md")
* [Using Client SDK 5 to work with AWS CloudHSM](client-sdk5.md "client-sdk5.md")
* [Using previous SDK version to work with
 AWS CloudHSM](choose-client-sdk.md "choose-client-sdk.md")
