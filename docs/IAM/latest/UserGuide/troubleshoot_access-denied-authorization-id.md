

# Troubleshoot access denied error messages with authorization ID

## Overview
<a name="access-troubleshooter-overview"></a>

 Access Troubleshooter is a feature of AWS Identity and Access Management that gives you visibility into the full authorization context behind access denied errors, so you can resolve them yourself quickly. 

 When AWS denies a request for a supported API, the access denied error response usually includes an authorization ID. This ID references the authorization evaluation for that denied request. To retrieve the details of the evaluation and identify what caused the denial, make a request to the `GetRequestAuthorizationDetails` API and provide the authorization ID, or open the link in the error message. This lets you identify the cause of a denied request in a single call, rather than resolving denials one at a time. 

 To inspect the policy document that AWS evaluated at the time of the denial, call `GetRequestAuthorizationPolicy` with the same authorization ID and a [policy identifier](#access-troubleshooter-policy-uri) returned by `GetRequestAuthorizationDetails`. 

 The following example shows an access denied error message that includes a link to Access Troubleshooter in the [AWS Management Console](https://console.aws.amazon.com/) and an authorization ID: 

```
User: arn:aws:iam::000111222333:user/janedoe is not authorized to perform: iam:CreateInstanceProfile
on resource: arn:aws:iam::000111222333:instance-profile/my-instance-profile
with an explicit deny in a service control policy: arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111.
Go to https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/authorization-details/a0b1c2d3e4f5g6h7i8j9k0l1m for complete details,
or call the GetRequestAuthorizationDetails API with the following authorization id: a0b1c2d3e4f5g6h7i8j9k0l1m
```

**Note**  
 AWS automatically includes an authorization ID in access denied error responses for supported APIs, but authorization IDs are not guaranteed. [In some cases](#access-troubleshooter-no-authorization-id), the error response does not include an authorization ID. When details are recorded, they might not be available immediately, because AWS records them asynchronously. If a call to `GetRequestAuthorizationDetails` returns a not-found response, wait a short time and try again. AWS retains authorization details for at least 24 hours after the denial. 

## Concepts and definitions
<a name="access-troubleshooter-concepts"></a>
+  **Authorization details.** The authorization details include the request context, the evaluations performed, and the policies that were evaluated. 
+  **Authorization ID.** A unique identifier included in a supported access denied error response. It references the authorization evaluation for that denied request, and is the value you pass to the `GetRequestAuthorizationDetails` API. 
+  **Check.** One authorization requirement, such as the caller's identity-based permissions or an organization's service control policies. For more information about checks, check types, and relevant policy types, see [How checks work](#access-troubleshooter-policy-checks). 
+  **Evaluation.** For each action/resource pair in the request, the condition context keys that applied, the evaluated result, and the checks that produced that result. The result is `ALLOW`, `EXPLICIT_DENY` (a policy explicitly denied the action), or `IMPLICIT_DENY` (at least one required check had no matching allow statement). 
+  **Policies evaluated during authorization.** All the policies AWS considered for the request, including policies that did not match the action/resource pair. Each entry gives the policy type (for example, identity-based, resource-based, SCP, RCP, permissions boundary, or session policy) and the same Amazon Resource Name ([ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns)) (for managed policies) or URI used in the evaluations (for inline and other non-managed policies). Use the [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) or URI to match a policy back to the evaluation that referenced it. The "Attached to" field lists the entities that the evaluated policy is attached to: the principal [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) for identity-based policies, session policies, and permissions boundaries; the resource [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) for resource-based policies; and one or more [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns)s of the root, OU, or account for SCPs and RCPs. 
+  **Policy URI.** An identifier returned in the `uri` field of `GetRequestAuthorizationDetails`. For a managed policy, this is the policy [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns). For an inline policy, AWS generates the identifier. 
+  **Request context.** The values of the condition context keys evaluated for the request. This includes global condition context keys and service-specific condition context keys. 

 Use these results together to identify which policy denied access and why. The evaluation reflects the policies as they were at the time of the denial. Policies might have changed since then. 

## Troubleshoot using the IAM console
<a name="access-troubleshooter-console"></a>

 Choose the link in the access denied error message to open the authorization details in the IAM console. 
+  **What to look for.** The IAM console shows the evaluation for each action/resource pair in the request, the result of each one (`ALLOW`, `EXPLICIT_DENY`, or `IMPLICIT_DENY`), and the policies that were considered. Find the pairs that were denied and the policies that caused the denial. In the following example, the console shows two evaluations. The evaluation for `iam:CreateInstanceProfile` is an explicit deny. Under the relevant policies, the `Service control policies for 000111222333` check is an explicit deny because an SCP attached to the account contains a `Deny` statement named `DenyCreateInstanceProfile`. The evaluation for `iam:TagInstanceProfile` is an implicit deny:   
![IAM console with an explicit deny for iam:CreateInstanceProfile and an implicit deny for iam:TagInstanceProfile.](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/AccessTroubleshooterConsoleExample.png)
+  **Determine whether the denial was intended.** Review the evaluation before changing a policy. A denial can be correct, and the cause is sometimes the request context rather than the policy. For example, a request might be missing an expected session tag or coming from an unexpected network path. 
+  **How to resolve the denial.** Locate the corresponding policy and update it to resolve the access issue. For an explicit deny, remove or narrow the `Deny` statement for the action. For an implicit deny, add an `Allow` statement for the action. For more information, see [Edit IAM policies](access_policies_manage-edit.md). 

 **Who can see the authorization details.** For a request within a single account or a single organization, anyone who is granted access to `iam:GetRequestAuthorizationDetails` can view the details of the request. For a request that spans more than one organization, a user in each organization can view only the details that pertain to their own organization. 

## Troubleshoot using AWS API or AWS CLI
<a name="access-troubleshooter-api-cli"></a>

 To troubleshoot a denial using the AWS API or AWS CLI: 

1. Locate the authorization ID in the access denied error response.

1.  Call `GetRequestAuthorizationDetails` with the authorization ID in the same AWS Region where the denial occurred. The following AWS CLI command uses `us-east-1`: 

   ```bash
   aws iam-toolbox get-request-authorization-details \
       --region us-east-1 \
       --authorization-id a0b1c2d3e4f5g6h7i8j9k0l1m
   ```

1.  Review each evaluation whose `evaluatedEffect` is `EXPLICIT_DENY` or `IMPLICIT_DENY`. Within the evaluation, find each denied check. Use `relevantPolicyTypes` to identify the policy types to review. For an explicit deny, use the check's `matchedPolicies` to find the policy and statement that denied the action. The evaluation-level `matchedPolicies` field is deprecated. Use `checks` instead. For an implicit deny, add an `Allow` to a relevant policy type. For an explicit deny, remove or narrow the `Deny`. For more information, see [How checks work](#access-troubleshooter-policy-checks). 

1.  To inspect a policy document at the time of the denial, call `GetRequestAuthorizationPolicy`. See [Retrieve a policy evaluated for the denied request](#access-troubleshooter-retrieve-policy). 

1.  Update the identified policies to resolve the access issue. For more information, see [Edit IAM policies](access_policies_manage-edit.md). 

### Retrieve a policy evaluated for the denied request
<a name="access-troubleshooter-retrieve-policy"></a>

 `GetRequestAuthorizationPolicy` returns the policy document that AWS recorded when it evaluated your request. Use this document to review the policy at the time of the denial. The operation doesn't retrieve the current version of the policy, which might have changed since the denial. 

 Pass the authorization ID as `authorizationId` and the `uri` value of an entry in the `policies` list returned by `GetRequestAuthorizationDetails` as `policyUri`. Both calls must use the same authorization ID. 

 In the example error, the policy URI is `arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111`. The following AWS CLI command retrieves the recorded policy document: 

```bash
aws iam-toolbox get-request-authorization-policy \
    --region us-east-1 \
    --authorization-id a0b1c2d3e4f5g6h7i8j9k0l1m \
    --policy-uri arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111
```

 The response contains the captured policy document as a JSON object in `policyDocument`. For this example, the response is: 

```json
{
    "policyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "DenyCreateInstanceProfile",
                "Effect": "Deny",
                "Action": "iam:CreateInstanceProfile",
                "Resource": "*"
            }
        ]
    }
}
```

 If the operation returns `ResourceNotFoundException`, verify that the authorization ID is correct, that you used the AWS Region where the denial occurred, and that the policy URI is from the `policies` list for that authorization ID. Also check that you meet the account or organization requirements described in [Additional considerations](#access-troubleshooter-considerations). The recorded authorization details might also have expired. 

## How checks work
<a name="access-troubleshooter-policy-checks"></a>

 When AWS evaluates a request, it checks every authorization requirement that applies to it, such as the organization's service control policies (SCPs), the caller's identity-based permissions, and the session policy. Each of these requirements is a *check*. AWS allows the request only when every applicable check allows the action. If any check results in an implicit or explicit deny, the request is denied. 

 The `GetRequestAuthorizationDetails` response groups each evaluation into checks. Because the checks that you can view show every requirement that was not met, not only the first one, you can resolve an implicit deny, where a required policy never matched, at the same time as an explicit deny. The following terms help you read the checks in the response: 
+  **Check.** One authorization requirement, such as the caller's identity-based permissions or an organization's service control policies. Each check has its own result and identifies the policy types that can change that result. A check lists the matched policies and statements that appear in the policies evaluated during authorization, so the list can be empty even when the check allows the action. 
+  **Check type.** The authorization requirement represented by a check, such as `PRINCIPAL` or `SESSION`. The [check types](#access-troubleshooter-checks-table) table lists each check type and the policy types that can satisfy it. 
+  **Relevant policy types.** The policy types to review when a check denies the request. They include the policy types typically used for the check, plus the type of every policy evaluated for the check, whether or not it matched. A type in this list doesn't mean that a policy of that type matched. The [check types](#access-troubleshooter-checks-table) table lists the policy types typically relevant to each check. 
+  **Policy target.** For an organization-level check, the root, organizational unit (OU), or account that the evaluated policy is applied to. One check appears per target, so a multi-level organization produces one check per level. 

 Each check has one of the following results: 
+ **Allow** – The check allowed the action.
+ **Implicit deny** – No policy in the check allowed the action.
+ **Explicit deny** – A policy in the check explicitly denied the action.
+ **No impact** – The check neither allowed nor denied the action. None of its deny statements matched, and it didn't need to allow the action because access was granted elsewhere.

 In the response, checks are returned in this order: resource control policies (RCPs) from the root to the account, SCPs from the root to the account, VPC endpoint, resource, principal, permissions boundary, and session. 

 Not every check appears in every response. The `PRINCIPAL`, `PERMISSIONS_BOUNDARY`, and `SESSION` checks appear whenever they apply to the principal that made the request, even if none of their policies matched. Other checks appear only when at least one of their policies is among the policies evaluated during authorization. You can view the checks only when your organization matches the principal organization recorded for the denied request. If no principal organization was recorded, your account must match the recorded principal account. If you can't view the checks, that doesn't mean that no checks applied. 

 To decide which policy to update for a denied check, use the following table. It lists each check type and the policy types typically relevant to it. 


| Check type | Relevant policy types | Description | 
| --- | --- | --- | 
| `RESOURCE_CONTROL_POLICY` | `RESOURCE_CONTROL_POLICY` | The RCPs attached to one organization target (root, OU, or account) that apply to the resource. One check appears per target. | 
| `SERVICE_CONTROL_POLICY` | `SERVICE_CONTROL_POLICY` | The SCPs attached to one organization target (root, OU, or account) that apply to the principal. One check appears per target. | 
| `VPC_ENDPOINT` | `VPC_ENDPOINT_POLICY` | The VPC endpoint that the request passed through. | 
| `RESOURCE` | `RESOURCE_BASED_POLICY` |  | 
| `PRINCIPAL` | `IDENTITY_BASED_POLICY`<br />`RESOURCE_BASED_POLICY` |  | 
| `PERMISSIONS_BOUNDARY` | `PERMISSIONS_BOUNDARY` | The role or user whose permissions boundary applies. | 
| `SESSION` | `SESSION_POLICY`<br />`RESOURCE_BASED_POLICY` | The session, scoped by its session policy. | 

## When you don't receive an authorization ID
<a name="access-troubleshooter-no-authorization-id"></a>

 AWS does not return an authorization ID in the following cases: 
+  **The authorization is too large to record.** When a request involves a large number of policies, recording the authorization details could affect service availability, so AWS prioritizes the request itself. 
+  **The service isn't supported by Access Troubleshooter yet.** See [Supported services](#access-troubleshooter-supported-services). 
+  **The API isn't supported by Access Troubleshooter yet.** Some APIs within a supported service don't return an authorization ID. 
+  **The request type isn't supported by Access Troubleshooter yet.** This includes requests made by a service on your behalf and anonymous requests. 

 If you don't receive an authorization ID, see [Troubleshoot access denied error messages](troubleshoot_access-denied.md) for other ways to diagnose the denial. 

## Additional considerations
<a name="access-troubleshooter-considerations"></a>

 **Required permissions.** To call `GetRequestAuthorizationDetails`, you must have permissions for the `iam:GetRequestAuthorizationDetails` action. To retrieve a policy document with `GetRequestAuthorizationPolicy`, you must have permissions for the `iam:GetRequestAuthorizationPolicy` action. 

 **Who can retrieve policy documents.** When AWS records a denied request, it records the caller's AWS account and organization, if any. If an organization was recorded, you must call `GetRequestAuthorizationPolicy` from an account in that organization. Otherwise, you must call it from the recorded account. 

 **Cross-organization requests.** When a denied request involves more than one AWS organization, `GetRequestAuthorizationDetails` returns only the details that belong to your own organization. This applies in both directions: 
+ If you are in the organization of the denied caller, you see only the details that pertain to that organization.
+ If you are in the organization of the denied resource, you see only the details that pertain to that organization.

 Details owned by another organization, such as that organization's policies or context key values, are not returned. 

 **Regional APIs.** `GetRequestAuthorizationDetails` and `GetRequestAuthorizationPolicy` are regional APIs. You must call them in the same AWS Region where you received the access denied error. 

 If you get an access denied error from a service or AWS Region that does not yet include an authorization ID, see [Troubleshoot access denied error messages](troubleshoot_access-denied.md). 

## Supported services
<a name="access-troubleshooter-supported-services"></a>

 Support for Access Troubleshooter is rolling out gradually across AWS services and AWS Regions. Some of the APIs for the following services support Access Troubleshooter: 
+ AWS CodeDeploy
+ AWS Identity and Access Management
+ AWS Key Management Service
+ AWS Security Token Service
+ AWS Step Functions
+ Amazon Elastic Compute Cloud
+ Amazon Elastic Container Registry
+ Amazon Kinesis Data Streams
+ Amazon Simple Queue Service