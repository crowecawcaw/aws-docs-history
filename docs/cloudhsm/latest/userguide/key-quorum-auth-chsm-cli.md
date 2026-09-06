

# Manage quorum authentication (M of N access control) using CloudHSM CLI
<a name="key-quorum-auth-chsm-cli"></a>

The hardware security modules (HSMs) in your AWS CloudHSM cluster support quorum authentication, also known as M of N access control. With quorum authentication, no single user on the HSM can perform quorum-controlled operations. Instead, a minimum number of HSM users (at least 2) must cooperate to do these operations. Quorum authentication adds an extra layer of protection by requiring approvals from multiple HSM users.

Quorum authentication can control the following operations:
+ HSM key usage and management by a [crypto-user](understanding-users.md#crypto-user-chsm-cli) – Creating signatures with a key, or wrapping, unwrapping, sharing, unsharing, and setting an attribute of a key.

**Important considerations**
+ An HSM user can sign their own quorum token—that is, the requesting user can provide one of the required approvals for quorum authentication.
+ You choose the minimum number of quorum approvers for quorum-controlled operations. The smallest number you can choose is two (2), and the largest number you can choose is eight (8).
+ The HSM can store up to 1,024 quorum tokens. If the HSM already has 1,024 tokens when you try to create a new one, the HSM purges one of the expired tokens. By default, tokens expire ten minutes after their creation.
+ If multi-factor authentication (MFA) is enabled, the cluster uses the same key for quorum authentication and for MFA. For more information about using quorum authentication and MFA, see [Using CloudHSM CLI to manage MFA](login-mfa-token-sign.md).
+ Only one quorum operation can be active at a time per service. You must complete or delete the active quorum token for a service before you can generate a new one for the same service. For more information, see [Supported services and types](key-quorum-auth-chsm-cli-service-names.md).

The following topics provide more information about quorum authentication in AWS CloudHSM.

**Topics**
+ [Quorum authentication process for CloudHSM CLI](key-quorum-auth-chsm-cli-overview.md)
+ [Supported AWS CloudHSM service names and types for quorum authentication with CloudHSM CLI](key-quorum-auth-chsm-cli-service-names.md)
+ [Set up quorum authentication for AWS CloudHSM crypto-users using CloudHSM CLI](key-quorum-auth-chsm-cli-first-time.md)
+ [Key management and usage with quorum authentication enabled for AWS CloudHSM using CloudHSM CLI](key-quorum-auth-chsm-cli-crypto-user.md)