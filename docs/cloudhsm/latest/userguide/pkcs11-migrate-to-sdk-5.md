# Migrate your AWS CloudHSM PKCS #11 library from Client SDK 3 to
 Client SDK 5

Use this topic to migrate your AWS CloudHSM [PKCS #11 library](pkcs11-library.md "pkcs11-library.md") from
 Client SDK 3 to Client SDK 5. For benefits on migrating, see [Benefits of AWS CloudHSM Client SDK 5](client-sdk-5-benefits.md "client-sdk-5-benefits.md").

In AWS CloudHSM, customer applications perform cryptographic operations using the AWS CloudHSM Client Software Development Kit (SDK).
 Client SDK 5 is the primary SDK that continues to have new features and platform support added to it.

To review migration instructions for all providers, see [Migrating from AWS CloudHSM Client SDK 3 to
 Client SDK 5](client-sdk-migration.md "client-sdk-migration.md").


## Prepare by addressing breaking changes


Review these breaking changes and update your application in your development environment accordingly.


### Wrap mechanisms have changed




| Client SDK 3 mechanism | Equivalent Client SDK 5 mechanism |
| --- | --- |
| `CKM_AES_KEY_WRAP` | `CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD` |
| `CKM_AES_KEY_WRAP_PAD` | `CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD` |
| `CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD` | `CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD` |
| `CKM_CLOUDHSM_AES_KEY_WRAP_NO_PAD` | `CKM_CLOUDHSM_AES_KEY_WRAP_NO_PAD` |
| `CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD` | `CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD` | ### ECDH In Client SDK 3, you can use ECDH and specify a KDF. This functionality is not currently available in Client SDK 5. If your application needs this functionality, please reach out to [support](https://support.console.aws.amazon.com/support/home#/ "https://support.console.aws.amazon.com/support/home#/"). ### Key handles are now session-specific To successfully use key handles in Client SDK 5, you must obtain key handles each time you run an application. If you have existing applications that will use the same key handles across different sessions, you must modify your code to obtain the key handle each time you run the application. For information on retrieving key handles, see [this AWS CloudHSM PKCS #11 example](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/find_objects/find_objects.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/find_objects/find_objects.c"). This change is in compliance with the [PKCS #11 2.40 specification](http://docs.oasis-open.org/pkcs11/pkcs11-base/v2.40/os/pkcs11-base-v2.40-os.html#_Toc416959689 "http://docs.oasis-open.org/pkcs11/pkcs11-base/v2.40/os/pkcs11-base-v2.40-os.html#_Toc416959689"). ## Migrate to Client SDK 5 Follow the instructions in this section to migrate from Client SDK 3 to Client SDK 5. ###### Note Amazon Linux, Ubuntu 16.04, Ubuntu 18.04, CentOS 6, CentOS 8, and RHEL 6 are not currently supported with Client SDK 5. If you are currently using one of these platforms with Client SDK 3, you will need to choose a different platform when migrating to Client SDK 5. 1. Uninstall the PKCS #11 library for Client SDK 3. Amazon Linux 2 ``` `$` `sudo yum remove cloudhsm-client-pkcs11` ``` CentOS 7 ``` `$` `sudo yum remove cloudhsm-client-pkcs11` ``` RHEL 7 ``` `$` `sudo yum remove cloudhsm-client-pkcs11` ``` RHEL 8 ``` `$` `sudo yum remove cloudhsm-client-pkcs11` ``` Ubuntu 16.04 LTS ``` `$` `sudo apt remove cloudhsm-client-pkcs11` ``` Ubuntu 18.04 LTS ``` `$` `sudo apt remove cloudhsm-client-pkcs11` ``` 2. Stop the Client Daemon for Client SDK 3. Amazon Linux 2 ``` `$` `sudo service cloudhsm-client stop` ``` CentOS 7 ``` `$` `sudo service cloudhsm-client stop` ``` RHEL 7 ``` `$` `sudo service cloudhsm-client stop` ``` RHEL 8 ``` `$` `sudo service cloudhsm-client stop` ``` Ubuntu 16.04 LTS ``` `$` `sudo systemctl stop cloudhsm-client` ``` Ubuntu 18.04 LTS ``` `$` `sudo systemctl stop cloudhsm-client` ``` 3. Uninstall the Client Daemon for Client SDK 3. Amazon Linux 2 ``` `$` `sudo yum remove cloudhsm-client` ``` CentOS 7 ``` `$` `sudo yum remove cloudhsm-client` ``` RHEL 7 ``` `$` `sudo yum remove cloudhsm-client` ``` RHEL 8 ``` `$` `sudo yum remove cloudhsm-client` ``` Ubuntu 16.04 LTS ``` `$` `sudo apt remove cloudhsm-client` ``` Ubuntu 18.04 LTS ``` `$` `sudo apt remove cloudhsm-client` ``` ###### Note Custom configurations need to be enabled again. 4. Install the Client SDK PKCS #11 library by following the steps in [Install the PKCS #11 library for AWS CloudHSM Client SDK 5](pkcs11-library-install.md "pkcs11-library-install.md") . 5. Client SDK 5 introduces a new configuration file format and command-line bootstrapping tool. To bootstrap your Client SDK 5 PKCS #11 library, follow the instructions listed in the user guide under [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to"). 6. In your development environment, test your application. Make updates to your existing code to resolve your breaking changes before your final migration. ## Related topics <br>• [Best practices for AWS CloudHSM](best-practices.md "best-practices.md")
