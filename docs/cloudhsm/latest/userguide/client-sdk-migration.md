# Migrating from AWS CloudHSM Client SDK 3 to
 Client SDK 5

In AWS CloudHSM, customer applications perform cryptographic operations using the AWS CloudHSM Client
 Software Development Kit (SDK). Client SDK 5 is the primary SDK that continues to have new features
 and platform support added to it.

Client SDK 3 includes two separate command line tools: the CMU for managing users and the KMU
 for managing keys and performing operations with keys. Client SDK 5 consolidates the functions of
 the CMU and KMU (tools that were offered with Client SDK 3) into a single tool, the [AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli.md "cloudhsm_cli.md"). User management operations can be found
 under the subcommands [The user category in CloudHSM CLI](cloudhsm_cli-user.md "cloudhsm_cli-user.md") and
 [The quorum category in CloudHSM CLI](cloudhsm_cli-qm.md "cloudhsm_cli-qm.md"). Key management operations
 can be found under the [key subcommand](cloudhsm_cli-key.md "cloudhsm_cli-key.md"), and cryptographic
 operations can be found under the [crypto subcommand](cloudhsm_cli-crypto.md "cloudhsm_cli-crypto.md").
 See [Reference for CloudHSM CLI commands](cloudhsm_cli-reference.md "cloudhsm_cli-reference.md") for a
 complete list of commands.

For benefits on migrating, see [Benefits of AWS CloudHSM Client SDK 5](client-sdk-5-benefits.md "client-sdk-5-benefits.md").

See the following topics for detailed instructions on migrating from Client SDK 3 to Client SDK 5.
 The latest version of AWS CloudHSM Client SDK is 5.16.


* [Migrate your AWS CloudHSM PKCS #11 library from Client SDK 3 to
 Client SDK 5](pkcs11-migrate-to-sdk-5.md "pkcs11-migrate-to-sdk-5.md")
* [Migrate your OpenSSL Dynamic Engine from AWS CloudHSM Client SDK 3 to
 Client SDK 5](openssl-migrate-to-sdk-5.md "openssl-migrate-to-sdk-5.md")
* [Migrate your Key Storage Provider (KSP) from AWS CloudHSM Client SDK 3 to
 Client SDK 5](ksp-migrate-to-sdk-5.md "ksp-migrate-to-sdk-5.md")
* [Migrate your JCE provider from AWS CloudHSM Client SDK 3
 to Client SDK 5](java-lib-migrate_to_sdk5.md "java-lib-migrate_to_sdk5.md")
For functionality or use cases that are not supported by CloudHSM CLI, contact [AWS Support](https://support.console.aws.amazon.com/support/home#/ "https://support.console.aws.amazon.com/support/home#/").
