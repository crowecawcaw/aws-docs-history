# The quorum category in CloudHSM CLI

In the CloudHSM CLI, **quorum** is a parent category for a group of commands
 that, when combined with **quorum**, creates a command specific to quorum
 authentication, or M of N operations. Currently, this category consists of the
 **token-sign** sub-category which consists of its own commands. Click the link
 below for details.


* [token-sign](cloudhsm_cli-qm-token.md "cloudhsm_cli-qm-token.md")

**Admin Services**: Quorum authentication is used for admin privileged services like creating users, deleting users, 
 changing user passwords, setting quorum values, and deactivating quorum and MFA capabilities.


**Crypto User Services**: Quorum authentication is used for crypto-user privileged services associated with a 
 specific key like signing with a key, sharing/unsharing a key, wrapping/unwrapping a key, and setting a key's attribute. The quorum value of an associated key is 
 configured when the key is generated, imported, or unwrapped. The quorum value must be equal to or less than the number of users that the key is associated with, 
 which includes users that the key is shared with and the key owner.


Each service type is further broken down into a qualifying service name, which contains a specific set of quorum supported service operations that can be performed.




| Service name | Service type | Service operations |
| --- | --- | --- |
| user | Admin | <br>• user create <br>• user delete <br>• user change-password <br>• user change-mfa |
| quorum | Admin | <br>• quorum token-sign set-quorum-value |
| cluster1 | Admin | <br>• cluster mtls register-trust-anchor <br>• cluster mtls deregister-trust-anchor <br>• cluster mtls set-enforcement |
| key-management | Crypto User | <br>• key wrap <br>• key unwrap <br>• key share <br>• key unshare <br>• key set-attribute |
| key-usage | Crypto User | <br>• key sign | [1] Cluster service is exclusively available on hsm2m.medium ## Related topics <br>• [Set up quorum authentication for AWS CloudHSM admins using CloudHSM CLI](quorum-auth-chsm-cli-first-time.md "quorum-auth-chsm-cli-first-time.md") <br>• [Manage quorum authentication (M of N access control) using CloudHSM CLI](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md")
