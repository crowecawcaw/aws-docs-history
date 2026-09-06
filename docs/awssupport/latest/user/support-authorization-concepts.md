

# AWS Support authorization concepts
<a name="support-authorization-concepts"></a>

The following concepts help you understand how AWS Support authorization works.

## Support permits
<a name="support-authorization-concept-permits"></a>

A support permit is a resource that defines the scope and conditions under which AWS Support can access information about your services that might contain your data during support case resolution. Without a support permit, AWS Support can't access this information. Each support permit specifies which actions AWS Support can take and the resources on which AWS Support can take those actions, along with optional time-based conditions.

Support permits can't be modified after creation. To change the scope of an existing authorization, delete the support permit and create a new one.

## Support permit scope
<a name="support-authorization-concept-scope"></a>

The support permit scope defines what AWS Support is authorized to do. A support permit scope contains three elements:

Actions  
The specific operations that AWS Support can perform. You can permit all actions or specify individual actions.

Resources  
The AWS resources for which AWS Support can access information about your services that might contain your data. You can permit all resources in the Region or specify individual resource ARNs.

Conditions  
Optional time-based constraints. You can set an `allowAfter` time (the earliest time AWS Support is able to use the support permit to authorize an action) and an `allowBefore` time (the latest time AWS Support is able to use the support permit to authorize an action) to create a time window. A support permit supports a maximum of 2 conditions.

## Signing keys
<a name="support-authorization-concept-signing-key"></a>

The signing key is a customer-managed AWS KMS asymmetric key that provides verification for support permits. The key must meet the following requirements:
+ Key spec: `ECC_NIST_P384`
+ Key usage: `SIGN_VERIFY`
+ Location: Same Region as the support permit.

Your private key material never leaves AWS KMS. Your KMS key is called to perform the signing operation and receives only the resulting signature.

## Support permit requests
<a name="support-authorization-concept-request"></a>

A support permit request is a notification from AWS Support requesting access to information about your services that might contain your data for a specific resource to help resolve a support case. If you don't approve the request, AWS Support can't access the requested information and might not be able to proceed with the investigation.

When AWS Support submits a support permit request, you receive notifications through Amazon EventBridge events and AWS CloudTrail log entries. You can then review the requested scope and approve or reject the request.

## Permit states
<a name="support-authorization-concept-permit-states"></a>

A support permit transitions through the following states:

ACTIVE  
The support permit is active. AWS Support can receive a signed authorization—a cryptographically signed token that permits a specific action, for actions within the support permit scope.

INACTIVE  
New signed authorizations aren't issued for INACTIVE support permits. A support permit transitions to INACTIVE automatically when the linked support case closes. Support permits can also transition to INACTIVE if the linked support case closes while an account is isolated or a Region is opted out. To re-authorize access after these transitions, create a new support permit.

DELETING  
Deletion initiated. New signed authorizations stop being issued. Due to eventual consistency, there might be a brief delay before the change takes effect. The support permit is then removed. To help prevent further signing operations, revoke the grant on the associated AWS KMS key. For more information, see [Revoking AWS Support authorization access](support-authorization-kms.md#support-authorization-kms-revoke).

## Permit request states
<a name="support-authorization-concept-request-states"></a>

A support permit request transitions through the following states:

PENDING  
The request is awaiting your review.

ACCEPTED  
You created a support permit that satisfies the request.

REJECTED  
You rejected the request by calling `RejectSupportPermitRequest`.

CANCELLED  
AWS Support cancelled the request.

## Actions and resources
<a name="support-authorization-concept-actions-resources"></a>

Actions are service-specific operations that AWS Support can perform during support investigations, such as reading diagnostic logs or viewing operational metrics. Each action has a descriptive name, such as `rds:ReadClusterData` or `rds:ViewQueryLogsWithParameters`. You can view available actions for each service by using the `ListActions` and `GetAction` API operations. For more information, see [Discovering support actions](support-authorization-actions.md).

Resources are identified by their ARN. When you scope a support permit, you specify the resource ARNs for which AWS Support can access service information, or you can permit access to service information for all resources in the Region.