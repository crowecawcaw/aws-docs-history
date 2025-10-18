# Create and use keys in AWS CloudHSM

Before you can create and use keys in your new cluster, create a hardware security module (HSM) user with the AWS CloudHSM CLI For more
 information, see [Understanding HSM User Management
 Tasks](understand-users.md "understand-users.md"), [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md"), 
 and [How to Manage HSM Users](manage-hsm-users.md "manage-hsm-users.md").

###### Note

If using Client SDK 3, use [CloudHSM Management Utility (CMU)](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md") instead of CloudHSM CLI.

After you create HSM users, you can sign in to the HSM and manage keys using any of
 these options: 


* Use [key management utility, a
 command line tool](key_mgmt_util-getting-started.md "key_mgmt_util-getting-started.md")
* Build a C application using the [PKCS #11 library](pkcs11-library.md "pkcs11-library.md")
* Build a Java application using the [JCE provider](java-library.md "java-library.md")
* Use the [OpenSSL Dynamic Engine directly from the command
 line](openssl-library.md "openssl-library.md")
* Use the OpenSSL Dynamic Engine for TLS offload with [NGINX and Apache web
 servers](ssl-offload.md "ssl-offload.md")
* Use the Key Storage Provider (KSP) for AWS CloudHSM with [Microsoft
 Windows Server Certificate Authority (CA)](win-ca-overview-sdk5.md "win-ca-overview-sdk5.md")
* Use the Key Storage Provider (KSP) for AWS CloudHSM with [Microsoft Sign
 Tool](signtool-sdk5.md "signtool-sdk5.md")
* Use the Key Storage Provider (KSP) for TLS offload with [Internet Information
 Server (IIS) web server](ssl-offload.md "ssl-offload.md")
