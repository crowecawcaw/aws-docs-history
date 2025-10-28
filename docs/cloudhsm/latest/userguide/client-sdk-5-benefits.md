# Benefits of AWS CloudHSM Client SDK 5

Compared to AWS CloudHSM Client SDK 3, Client SDK 5 is easier to manage, offers superior configurability,
and increased reliability. Client SDK 5 also provides some additional key advantages to Client SDK 3.

**Designed for serverless architecture**

Client SDK 5 does not require a client daemon, so you no longer need to manage a background service. This helps users in a few important ways:

- Simplifies the application startup process. All you need to do to get started with CloudHSM is configure the SDK before running your application.
- You don't need a constantly running process, which makes integration with serverless components like Lambda and Elastic Container Service (ECS) easier.

**Better third party integrations and easier portability**

Client SDK 5 follows the JCE specification closely and provides easier portability between different JCE providers and better third party integrations

**Improved user experience and configurability**

Client SDK 5 improves log message readability and provides clearer exceptions and error-handling mechanisms, all of which makes self-service triaging much easier for users. SDK 5 also offers a variety of configurations, which are
listed in the [Configure Tool page](configure-sdk-5.md "configure-sdk-5.md").

**Broader platform support**

Client SDK 5 offers more support for modern operating platforms. This includes support for ARM technologies and greater support for
[JCE](java-library_5.md "java-library_5.md"),
[PKCS#11](pkcs11-library.md "pkcs11-library.md"), and
[OpenSSL](openssl-library.md "openssl-library.md").
For more information, refer to [Supported platforms](client-supported-platforms.md "client-supported-platforms.md").

**IPv6 connection support**

Client SDK 5.14+ supports connections to dual-stack HSMs using IPv6.

**Additional features and mechanisms**

Client SDK 5 includes additional features and mechanisms that are not available in Client SDK 3, and Client SDK 5 will continue to add more mechanisms in the future.
