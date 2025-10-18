# Client SDKs for AWS CloudHSM

When using AWS CloudHSM, you perform cryptographic operations with [AWS CloudHSM Client Software Development Kits (SDKs)](use-hsm.md "use-hsm.md"). AWS CloudHSM Client SDKs include:


* Public Key Cryptography Standards #11 (PKCS #11)
* JCE provider
* OpenSSL Dynamic Engine
* Key Storage Provider (KSP) for Microsoft Windows
You can use any or all of these SDKS in your AWS CloudHSM cluster. Write your application code to use these SDKs to perform cryptographic operations in your HSMs. 
 To see what platforms and HSM types support each SDK, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md")

Utility and command line tools are needed not only to use SDKs but also to configure the credentials, policies, and settings of your application. For more information, refer to [AWS CloudHSM command line tools](command-line-tools.md "command-line-tools.md").


 For more information about installing and using the Client SDK or the security of the
 client connection, see [Client SDKs](use-hsm.md "use-hsm.md") and 
 [End-to-end encryption](client-end-to-end-encryption.md "client-end-to-end-encryption.md").
