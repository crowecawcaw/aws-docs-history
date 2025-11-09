# Compare AWS CloudHSM Client SDK component support

In addition to the command-line tools, Client SDK 3 contains components that
enable off-loading cryptographic operations to the HSM from various platform or
language-based applications. Client SDK 5 has parity with Client SDK 3, except it does not yet support CNG and KSP providers. The following table compares component availability in Client SDK 3 and Client SDK 5.

| Component                                                                       | Client SDK 5 | Client SDK 3 |
| ------------------------------------------------------------------------------- | ------------ | ------------ |
| PKCS #11 library                                                                | Yes          | Yes          |
| JCE provider                                                                    | Yes          | Yes          |
| OpenSSL Dynamic Engine                                                          | Yes          | Yes          |
| Key Storage Provider (KSP)                                                      | Yes          | Yes          |
| CloudHSM Management Utility (CMU)[1](#sdk-compare-note-1 "#sdk-compare-note-1") | Yes          | Yes          |
| Key Management Utility (KMU)[1](#sdk-compare-note-1 "#sdk-compare-note-1")      | Yes          | Yes          |
| Configure tool                                                                  | Yes          | Yes          |

[1] CMU and KMU components are included in CloudHSM CLI with Client SDK 5.

The following sections describe the components.

## PKCS #11 library

PKCS #11 is a standard for performing cryptographic operations on hardware security
modules (HSMs). AWS CloudHSM offers implementations of the PKCS #11 library that are compliant with PKCS #11
version 2.40.

- For Client SDK 3, the PKCS #11 library is a Linux only component that matches Linux base support. For
  more information, see [Linux support for AWS CloudHSM Client SDK 3](sdk3-linux.md "sdk3-linux.md").
- For Client SDK 5, the PKCS #11 library is a cross-platform component that matches Linux and Windows
  Client SDK 5 base support. For more information, see [Linux support for AWS CloudHSM Client SDK 5](sdk8-linux.md "sdk8-linux.md") and [Windows support for AWS CloudHSM Client SDK 5](sdk8-windows.md "sdk8-windows.md").

## CloudHSM Management Utility (CMU)

The CloudHSM Management Utility (CMU) command line tool helps crypto officers manage users in the HSMs. It includes tools that create, delete, and list users, and change user passwords. For more information,
see [AWS CloudHSM Management Utility (CMU)](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md").

## Key Management Utility (KMU)

The Key Management Utility (KMU) is a command line tool that helps crypto users (CU) manage keys on the hardware security modules (HSM). For more information,
see [AWS CloudHSM Key Management Utility (KMU)](key_mgmt_util.md "key_mgmt_util.md").

## JCE provider

The AWS CloudHSM JCE provider is compliant with the Java Cryptographic Architecture (JCA). The
provider allows you to perform cryptographic operations on the HSM.

The JCE provider is a Linux only component that matches Linux base support. For more information,
see [Linux support for AWS CloudHSM Client SDK 3](sdk3-linux.md "sdk3-linux.md").

- For Client SDK 3 requires OpenJDK 1.8

## OpenSSL Dynamic Engine

The AWS CloudHSM OpenSSL Dynamic Engine allows you to offload cryptographic operations to your CloudHSM
cluster through the OpenSSL API.

- For Client SDK 3, the OpenSSL Dynamic Engine is Linux only component that does _not_ match Linux base support. See the exclusions below.

      + Requires OpenSSL 1.0.2[f+]

  **Unsupported platforms:**

      + CentOS 8
      + Red Hat Enterprise Linux (RHEL) 8
      + Ubuntu 18.04 LTS

  These platforms ship with a version of OpenSSL incompatible with OpenSSL Dynamic Engine for Client SDK 3. AWS CloudHSM
  supports these platforms with OpenSSL Dynamic Engine for Client SDK 5.

- For Client SDK 5, the OpenSSL Dynamic Engine is a Linux only component that requires OpenSSL 1.0.2, 1.1.1, or 3.x.

## Key storage provider (KSP)

Key Storage Provider (KSP) is a cryptographic API specific to the Microsoft Windows operating system.

For Client SDK 3, the CNG and KSP providers is a Windows only component that matches Windows base support. For
more information, see [Windows support for AWS CloudHSM Client SDK 3](sdk3-windows.md "sdk3-windows.md").

For Client SDK 5, the Key Storage Provider (KSP) is a Windows only component that matches Windows base support. For more
information, see [Windows support for AWS CloudHSM Client SDK 5](sdk8-windows.md "sdk8-windows.md").
