# AWS CloudHSM Management Utility (CMU)

The **cloudhsm_mgmt_util** command line tool helps crypto officers manage
users in the hardware security modules (HSMs) in AWS CloudHSM clusters. The AWS CloudHSM Management Utility
(CMU) includes tools that create, delete, and list users, and change user passwords.

The CMU and Key Management Utility (KMU) are part of [the
Client SDK 3 suite](choose-client-sdk.md "choose-client-sdk.md"). Client SDK 3 and its related command line tools (Key Management Utility and CloudHSM Management Utility) are only available in the HSM type _hsm1.medium_.

cloudhsm_mgmt_util also includes commands that allow crypto users (CUs) to share keys and get and set
key attributes. These commands complement the key management commands in the primary key
management tool, [key_mgmt_util](key_mgmt_util.md "key_mgmt_util.md").

For a quick start, see [Cloned clusters in AWS CloudHSM](cloudhsm_mgmt_util-getting-started.md "cloudhsm_mgmt_util-getting-started.md"). For detailed information about the cloudhsm_mgmt_util
commands and examples of using the commands, see [Reference for AWS CloudHSM Management Utility
commands](cloudhsm_mgmt_util-reference.md "cloudhsm_mgmt_util-reference.md") .

###### Topics

- [Supported platforms](cmu-support.md "cmu-support.md")
- [Getting started](cloudhsm_mgmt_util-getting-started.md "cloudhsm_mgmt_util-getting-started.md")
- [Install the client
  (Linux)](cmu-install-and-configure-client-linux.md "cmu-install-and-configure-client-linux.md")
- [Install the client
  (Windows)](cmu-install-and-configure-client-win.md "cmu-install-and-configure-client-win.md")
- [Reference](cloudhsm_mgmt_util-reference.md "cloudhsm_mgmt_util-reference.md")
