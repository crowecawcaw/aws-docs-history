

# Controlling console access with resource-based policies and resource control policies
<a name="console-access-control"></a>

**Important**  
Console sign-in access is enabled by default. AWS Sign-In allows unrestricted console access initially. To add restrictions, enable console authorization configuration for your account or organization. The resource permission statements that you create have no effect until you enable console authorization. See [Getting started with console access control using resource policies](#console-access-control-getting-started).

AWS Sign-In supports resource-based policies and resource control policies (RCPs) to control access to AWS Sign-In. Use these policies to verify user identity and network location throughout AWS Management Console access – before, during, and after authentication. For root users, these policies validate network location and user identity before credential collection begins. Credentials can be entered only when access originates from expected networks.

AWS Sign-In resource-based policies:
+ Apply to individual AWS accounts.
+ Let account administrators restrict console access based on network parameters and principal identities.

Resource control policies (RCPs):
+ Apply organization-wide through AWS Organizations.
+ Provide centralized governance across all member accounts.

Both policy types verify access before authentication. This blocks principals from accessing the sign-in page from unexpected networks.

These policies do not replace IAM identity-based policies, which continue to apply.

**Note**  
For complete documentation on resource control policies, including organization-level configuration and management, see [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the *AWS Organizations User Guide*. This section focuses primarily on AWS Sign-In resource-based policies.

AWS Sign-In resource-based policies and RCPs apply to the following authentication methods:
+ **AWS Management Console** – Direct sign-in using the console login page.
+ **Federated identity providers** – Sign-in through SAML or OIDC federation.
+ **Applications integrated with AWS Sign-In** – Amazon Connect, Amazon QuickSight, AWS Health Dashboard, Amazon AppStream, Amazon Lightsail.

**Note**  
Console access through the IAM Identity Center portal is not currently compatible with AWS Sign-In policies that restrict access based on network condition keys. Enabling network-based restrictions will block console access for user in IAM Identity Center users.

These controls do not apply to programmatic access using access keys (AWS SDKs or API calls signed with SigV4).

## How AWS Sign-In evaluates resource-based policies
<a name="console-access-control-how-it-works"></a>

AWS Sign-In evaluates the applicable resource-based policies or resource control policies (RCPs) at two points during console access: before authentication (the pre-authentication phase) and after successful authentication (the post-authentication phase). Each evaluation checks the condition keys defined in your policy. The keys available depend on the phase and action. For details, see [Supported condition keys](#console-access-control-condition-keys).

**Note**  
For root user sign-in, an access attempt from unexpected networks is blocked before the password prompt appears. This prevents submission of credentials from unexpected networks.

After authentication, the evaluation also considers the principal's identity-based policies. An IAM policy that denies the relevant sign-in action can prevent the console session from being granted, even when network conditions are met.

## Supported actions
<a name="console-access-control-supported-actions"></a>

AWS Sign-In resource policies (resource-based policies and RCPs) support the following actions:

`signin:Authenticate`  
This is an evaluation-only (not callable) action that is assessed when a sign-in request is received. This is a pre-authentication check and happens when either the principal enters credentials on the sign-in page (root user, IAM user) or initiates console sign-in using credentials from an identity provider or AWS STS (federated user, role).  
**Supported condition keys:** `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:VpcSourceIp`, `aws:RequestedRegion`, `signin:PrincipalArn`.  
Principal-based global condition keys (`aws:PrincipalArn`, `aws:PrincipalAccount`) are not available for this action because the user's identity has not yet been confirmed.

`signin:AuthorizeOAuth2Access`  
Used for OAuth authorization code generation. After successful authentication, this action is triggered when the system generates an OAuth authorization code. At this point, the user is authenticated and principal-based condition keys are available.  
**Supported condition keys:** `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:VpcSourceIp`, `aws:RequestedRegion`, `aws:PrincipalArn`, `aws:PrincipalAccount`.

`signin:CreateOAuth2Token`  
This post-authentication action is used for OAuth token creation and exchange. This action is triggered when redeeming authorization codes for access tokens, refreshing tokens, or performing token exchange operations. Principal-based condition keys are available during this phase.  
**Supported condition keys:** `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:VpcSourceIp`, `aws:RequestedRegion`, `aws:PrincipalArn`, `aws:PrincipalAccount`.

**Important**  
When creating AWS Sign-In policies (resource-based policies or RCPs), cover all three actions across your policy – `signin:Authenticate` in a pre-authentication statement, and `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token` in a post-authentication statement. Console sign-in uses OAuth 2.0, which flows through all three actions sequentially. If your policy omits an action, the corresponding phase is not protected. For VPC endpoint policy actions including `signin:CreateAccount`, see [AWS Management Console Private Access](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/console-private-access.html).

## Supported condition keys
<a name="console-access-control-condition-keys"></a>

AWS Sign-In supports the following condition keys in resource-based policies and resource control policies (RCPs). Use these keys to control console access based on network location and principal identity:
+ **Network-based (all actions):** `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:VpcSourceIp`, `aws:RequestedRegion`.
+ **Identity-based (post-authentication actions):** `aws:PrincipalArn`, `aws:PrincipalAccount`.
+ **Service-specific (pre-authentication only):** `signin:PrincipalArn`.

For detailed usage rules, operator compatibility, combination restrictions, and the availability matrix by action, see [AWS Sign-In condition keys reference](reference-signin-condition-keys.md).

## Getting started with console access control using resource policies
<a name="console-access-control-getting-started"></a>

**Prerequisites**
+ AWS CLI installed and configured.
+ Appropriate IAM permissions (see [AWS managed policy: AWSSignInResourcePolicyManagement](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSSignInResourcePolicyManagement)).
+ Identified network perimeters (IP ranges, VPCs, or VPC endpoints).
+ Designated excluded principals to retain access (recommended but optional).
+ If your network uses egress filtering, allowlist the AWS Sign-In control plane endpoint (see [AWS Sign-In administration domains to allowlist](allowlist-domains.md#allowlist-domains-admin)).

**Important**  
Before enabling console authorization in production, AWS recommends configuring at least one excluded principal to maintain emergency recovery access. All principals, including root user, are subject to the policy unless explicitly excluded. Excluded principals are optional, but omitting them increases the risk of account lockout if network conditions change unexpectedly.

Specify `--region us-east-1` for all write operations on AWS Sign-In policies. AWS replicates policies globally from this Region. Read operations can target any Region.

### Step 1: Create resource permission statements
<a name="console-access-control-step1-statements"></a>

Create permission statements that define your access controls. All write operations require `--region us-east-1` (the AWS Sign-In service accepts policy changes only in this Region). The remaining parameters (`--source-vpc`, `--source-ip`, `--requested-region`, `--excluded-principal`) define the conditions in your policy. For example, `--requested-region us-west-2` adds a condition restricting sign-in to the us-west-2 regional sign-in endpoint.

**Example – Restrict access to corporate VPC:**

```
aws signin put-resource-permission-statement \
  --source-vpc vpc-0abc123def456789 \
  --requested-region us-west-2 \
  --excluded-principal "arn:aws:iam::123456789012:user/EmergencyAdmin" \
  --client-token unique-request-id-12345 \
  --region us-east-1
```

**Example – Restrict access to specific IP range:**

```
aws signin put-resource-permission-statement \
  --source-ip "{{IP_ADDRESS}}" \
  --excluded-principal "arn:aws:iam::123456789012:role/BreakGlassRole" \
  --region us-east-1
```

**Note**  
The `--excluded-principal` parameter designates an excluded principal that bypasses the network restrictions, preserving emergency access if network conditions change.

### Step 2: Enable console authorization configuration
<a name="console-access-control-step2-enable"></a>

The following step activates policy enforcement for the console sign-in process on your account or organization. Resource permission statements can be created at any time, but they are not evaluated until console authorization is enabled.

**Warning**  
Enabling console authorization can lock out principals if your network conditions are misconfigured, or if an existing service control policy (SCP) or resource control policy (RCP) denies the AWS Sign-In actions. Before you enable console authorization, confirm your permission statements are correct, and remove or adjust any SCP or RCP that denies `signin:Authenticate`, `signin:AuthorizeOAuth2Access`, or `signin:CreateOAuth2Token`.

For standalone accounts:

```
aws signin put-console-authorization-configuration \
  --target-id <your-aws-account-id> \
  --region us-east-1
```

For AWS Organizations:

```
aws signin put-console-authorization-configuration \
  --target-id <your-aws-organization-id> \
  --region us-east-1
```

Verify the configuration:

```
aws signin get-console-authorization-configuration \
  --target-id <your-target-id> \
  --region <your-region>
```

Delete the console authorization configuration:

```
aws signin delete-console-authorization-configuration \
  --target-id <your-target-id> \
  --region us-east-1
```

### Step 3: Verify your policy
<a name="console-access-control-step3-verify"></a>

List all permission statements:

```
aws signin list-resource-permission-statements \
  --max-results 50 \
  --region <your-region>
```

Retrieve the complete consolidated policy:

```
aws signin get-resource-policy \
  --region <your-region>
```

The `get-resource-policy` command returns the complete resource-based policy composed of all your permission statements. Review this policy to confirm it reflects your intended access controls before testing console access.

### Regional availability
<a name="console-access-control-regional-availability"></a>

Console authorization APIs are available in all AWS commercial Regions. You can call these APIs from any Region where you operate.

**Important**  
Write operations (`put-console-authorization-configuration`, `put-resource-permission-statement`, `delete-console-authorization-configuration`, `delete-resource-permission-statement`) must be performed in the `us-east-1` Region. Policies created in `us-east-1` automatically replicate globally. Read operations (`get-console-authorization-configuration`, `list-resource-permission-statements`, `get-resource-policy`) can be performed from any Region.

### Understanding the policy structure
<a name="console-access-control-policy-structure"></a>

AWS Sign-In policies contain two statements that protect different phases of the console sign-in flow:
+ **Pre-authentication statement (Action: `signin:Authenticate`):** Evaluated when the sign-in request is received, before authentication completes. The global key `aws:PrincipalArn` is not available at this phase because the principal's identity is unconfirmed. In this phase `signin:PrincipalArn` is available to exempt specific principals from network restrictions. Network-based condition keys are available for evaluation in this phase.
+ **Post-authentication statement (Action: `signin:AuthorizeOAuth2Access`, `signin:CreateOAuth2Token`):** Evaluated after authentication, during OAuth token exchange. Uses `aws:PrincipalArn` to exempt specific principals. All network-based and identity-based condition keys are available for evaluation in this phase.

Both statements are required because console sign-in uses OAuth 2.0, which flows through all three actions sequentially. A policy with only one statement leaves the other phase unprotected. `signin:PrincipalArn` supports root user, IAM user, and role principal types. `aws:PrincipalArn` supports all principal types (root user, IAM user, federated user, role).

## Policy examples
<a name="console-access-control-policy-examples"></a>

### Example 1: RCP with network perimeter and excluded principals
<a name="console-access-control-example-rcp"></a>

The following resource control policy (RCP) denies AWS Management Console sign-in from outside your corporate network across all accounts in your organization. Designated excluded principals are exempted for emergency access. Since VPC IDs are unique only within a Region, the policy includes a third statement that pins VPC-based access to the expected Region.

The `EnforceNetworkPerimeterPreAuth` statement uses `signin:PrincipalArn` to exempt excluded principals during the pre-authentication phase. The `EnforceNetworkPerimeterPostAuth` statement uses `aws:PrincipalArn` to exempt excluded principals after authentication. The `EnforceSourceVPCRegion` statement ensures the request Region matches the VPC Region, restricting access to the expected Region for the specified VPC.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "EnforceNetworkPerimeterPreAuth",
      "Effect": "Deny",
      "Principal": "*",
      "Action": ["signin:Authenticate"],
      "Resource": "*",
      "Condition": {
        "ArnNotEquals": {
          "signin:PrincipalArn": [
            "arn:aws:iam::111122223333:root",
            "arn:aws:iam::444455556666:root",
            "arn:aws:iam::777788889999:user/EmergencyUser",
            "arn:aws:iam::777788889999:role/OrgBreakGlassRole"
          ]
        },
        "NotIpAddressIfExists": {
          "aws:SourceIp": "<my-corporate-cidr>"
        },
        "StringNotEquals": {
          "aws:SourceVpc": "<my-vpc>"
        }
      }
    },
    {
      "Sid": "EnforceNetworkPerimeterPostAuth",
      "Effect": "Deny",
      "Principal": "*",
      "Action": ["signin:CreateOAuth2Token", "signin:AuthorizeOAuth2Access"],
      "Resource": "*",
      "Condition": {
        "ArnNotEquals": {
          "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:root",
            "arn:aws:iam::444455556666:root",
            "arn:aws:iam::777788889999:user/EmergencyUser",
            "arn:aws:iam::777788889999:role/OrgBreakGlassRole"
          ]
        },
        "NotIpAddressIfExists": {
          "aws:SourceIp": "<my-corporate-cidr>"
        },
        "StringNotEquals": {
          "aws:SourceVpc": "<my-vpc>"
        }
      }
    },
    {
      "Sid": "EnforceSourceVPCRegion",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "signin:Authenticate",
        "signin:CreateOAuth2Token",
        "signin:AuthorizeOAuth2Access"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceVpc": "<my-vpc>"
        },
        "StringNotEqualsIfExists": {
          "aws:RequestedRegion": "<my-vpc-region>"
        }
      }
    }
  ]
}
```

This policy:
+ Denies access to the sign-in page unless the request originates from the corporate IP range or corporate VPC. Excluded root accounts and IAM users are exempted via `signin:PrincipalArn` (pre-authentication).
+ Denies OAuth token exchange unless from the corporate IP range or VPC. Excluded root accounts, IAM users, and roles are exempted via `aws:PrincipalArn` (post-authentication global key).
+ If a request comes from the specified VPC but the Region does not match, access is denied. AWS VPC IDs are unique within a Region, and the same VPC ID can exist in different Regions.
+ Applies globally across your AWS Organization when configured as an RCP.

### Example 2: Resource-based policy for IP-based access with excluded principal
<a name="console-access-control-example-rbp"></a>

The following resource-based policy denies console access to all principals making requests from outside the specified IP range, with an excluded principal exempted. The policy contains two statements: a pre-authentication statement that uses the service-specific `signin:PrincipalArn` key, and a post-authentication statement that uses the global `aws:PrincipalArn` key.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": { "AWS": "*" },
      "Action": ["signin:Authenticate"],
      "Resource": "*",
      "Condition": {
        "ArnNotEquals": {
          "signin:PrincipalArn": "<excluded-principal-arn>"
        },
        "NotIpAddress": {
          "aws:SourceIp": "<my-corporate-cidr>"
        },
        "StringEquals": {
          "aws:ResourceAccount": "<my-aws-account-id>"
        }
      }
    },
    {
      "Effect": "Deny",
      "Principal": { "AWS": "*" },
      "Action": ["signin:CreateOAuth2Token", "signin:AuthorizeOAuth2Access"],
      "Resource": "*",
      "Condition": {
        "ArnNotEquals": {
          "aws:PrincipalArn": "<excluded-principal-arn>"
        },
        "NotIpAddress": {
          "aws:SourceIp": "<my-corporate-cidr>"
        },
        "StringEquals": {
          "aws:ResourceAccount": "<my-aws-account-id>"
        }
      }
    }
  ]
}
```

This policy:
+ Denies access to all principals unless they connect from the IP range `<my-corporate-cidr>`.
+ Exempts the excluded principal from network restrictions using `signin:PrincipalArn` (pre-authentication) and `aws:PrincipalArn` (post-authentication).
+ Applies only to the specific account where the resource-based policy is configured (identified by `<my-aws-account-id>`).

## Best practices
<a name="console-access-control-best-practices"></a>

### Configure excluded principals for emergency recovery access
<a name="console-access-control-bp-breakglass"></a>

AWS recommends configuring at least one excluded user before enforcing console authorization policies in production. At the pre-authentication stage, the `signin:PrincipalArn` condition key exempts root user, IAM user, and role principals. At the post-authentication stage, the `aws:PrincipalArn` condition key exempts all principal types (root user, IAM user, federated user, role).

Excluded principals are optional, but omitting them increases the risk of account lockout if network conditions change unexpectedly or if policies are misconfigured.

Recommended excluded-principal configuration steps:

1. Create an excluded IAM role (for example, `BreakGlassRole`).

1. For excluded roles, require MFA in the role trust policy.

1. Grant the excluded identity only the minimum permissions needed for emergency recovery.

1. Include the excluded principal ARN in both pre-authentication (`signin:PrincipalArn`) and post-authentication (`aws:PrincipalArn`) policy statements.

1. Document the recovery procedure and store it securely outside AWS.

1. Test excluded principal access periodically to confirm it works when needed.

### Maintain recovery access paths
<a name="console-access-control-bp-recovery"></a>

In addition to the excluded principal described above, ensure alternative access methods are available in case console authorization policies block sign-in unexpectedly:
+ **Role-based programmatic access:** Console authorization policies apply only to interactive console sign-in. They do not apply to API requests signed with SigV4. If you have programmatic access (for example, existing access keys, a cross-account role), use it to call `signin:DeleteConsoleAuthorizationConfiguration` and remove the restricting policy. The credentials must include `signin:DeleteConsoleAuthorizationConfiguration` permission (included in the `AWSSignInResourcePolicyManagement` managed policy). AWS recommends temporary credentials over long-term IAM user access keys. For member accounts, management account administrators can assume `OrganizationAccountAccessRole` in the member account (`aws sts assume-role`) to obtain these temporary credentials.
+ **AWS support recovery:** Keep your root user account email and phone number current. If excluded-principal and programmatic access are both unavailable, AWS Support can provide a recovery portal link after identity verification. See [I am locked out of my account after enabling console authorization](#console-access-control-ts-lockout) for the full recovery process.

### Test before production deployment
<a name="console-access-control-bp-testing"></a>

AWS recommends that you don't attach restrictive RCPs to the root of your organization without thoroughly testing the impact that the policy has on accounts. Instead, create an OU that you can move your accounts into one at a time, or at least in small numbers, to ensure that you don't inadvertently lock users out of key accounts.

Testing workflow:

1. Create a single permission statement with your primary network restrictions.

1. Enable console authorization in a non-production account.

1. Test console access from both allowed and denied networks.

1. Review Amazon CloudTrail logs to confirm policy evaluation behavior.

1. Test access using your excluded principal.

1. Gradually expand to additional networks and accounts.

1. Monitor before enforcing in production accounts.

### Design with defense-in-depth
<a name="console-access-control-bp-defense"></a>

Use AWS Sign-In resource-based policies and resource control policies as one layer within a broader security strategy. AWS Sign-In policies restrict console access based on network location and principal identity. Combine them with other policy types to create comprehensive access controls:
+ **AWS Sign-In policies (resource-based policies and RCPs):** Restrict console access based on network location and principal identity before, during, and after authentication.
+ **IAM policies:** Control what actions users can perform after signing in.
+ **Service control policies (SCPs):** Apply organization-wide permission guardrails across all principals.
+ **VPC endpoint policies:** Control which services and accounts can be accessed through VPC endpoints.

### Monitor and audit continuously
<a name="console-access-control-bp-monitoring"></a>

AWS CloudTrail automatically records all AWS Sign-In policy evaluations and configuration changes. View these events in CloudTrail Event history for up to 90 days. For longer retention, deliver events to Amazon S3 by creating a trail (see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)). For real-time alerting, create Amazon EventBridge rules that match AWS Sign-In events, configure your trail to deliver to a CloudWatch Logs log group for metric filter-based alarms, or forward events to your existing SIEM solution.

## Use cases
<a name="console-access-control-use-cases"></a>

Network perimeter enforcement  
Restrict console access to corporate VPCs or approved IP ranges. Use resource-based policies for individual accounts or resource control policies (RCPs) for organization-wide enforcement to ensure that users can only sign in from trusted network locations, preventing unauthorized access from public or untrusted networks.  
**Example scenario:** A company requires all console access to originate from their corporate network or approved AWS VPCs. They configure a resource-based policy for a single account, or an RCP across their organization, that denies access from all other networks while maintaining emergency recovery access for emergency administrators.

Compliance requirements  
Meet regulatory requirements for network-based access controls. Many compliance frameworks require organizations to restrict access to sensitive systems based on network location. AWS Sign-In policies provide auditable, enforceable controls that demonstrate compliance with these requirements.  
**Example scenario:** A financial services company must comply with regulations requiring console access only from approved networks. They use RCPs to enforce organization-wide network restrictions and maintain AWS CloudTrail logs as evidence of compliance.

Multi-account governance  
Implement consistent console access policies across AWS Organizations. Use RCPs to enforce standard network restrictions across all member accounts, ensuring consistent security posture without requiring individual account-level configuration.  
**Example scenario:** An enterprise with 100\+ AWS accounts uses RCPs to enforce a policy requiring all console access to originate from VPC endpoints within their organization, confirming consistent network controls across all accounts.

Third-party access control  
Grant temporary console access to partners or contractors from specific networks. Organizations can create time-limited, network-restricted console access for external parties without compromising overall security posture.  
**Example scenario:** A company needs to grant a consulting firm temporary console access. They create a resource-based policy that allows access only from the consulting firm's known IP ranges and only for the IAM roles assigned to the consultants.

Restrict console access to specific principals  
Allow only a defined set of principals to sign in to the AWS Management Console, and deny all others, regardless of network location. This is useful for customers who are not using VPC endpoints and want identity-based console restrictions. Principals that are denied console sign-in keep their programmatic access; AWS Sign-In policies gate only console sign-in, and only the principals you exempt can sign in.  
**Example scenario:** A company wants only its administrators to use the console. They configure an RCP that denies console sign-in for all principals except the administrator principal ARNs. An Amazon EC2 instance role with valid credentials cannot sign in to the console, because it is not an exempted principal, even though it retains its programmatic permissions. This addresses the common case of instance-role credentials being used for console sign-in.

## Troubleshooting console access control
<a name="console-access-control-troubleshooting"></a>

### I cannot sign in due to network conditions in Sign-in resource-based policies
<a name="console-access-control-ts-network"></a>

You may see one of the following error messages when access is denied by a AWS Sign-In policy:
+ "Your authentication information is incorrect. Please try again." (pre-authentication denial by resource-based policy)
+ "Authentication failed Invalid request" (pre-authentication denial by RCP)
+ "Authentication failed: To access this account, sign in from a different network, or contact your administrator for more information" (post-authentication denial)

If you see any of these errors and believe your access should be allowed, contact your AWS administrator. They can review CloudTrail logs for `ConsoleLogin` events with `errorMessage` "Authorization denied because of a resource-based policy" or "Authorization denied because of a resource control policy" to identify which policy statement denied access.

**Possible causes:**
+ Your source IP address is not in the allowed CIDR range.
+ You are not connected to the required VPC or VPC endpoint.
+ You are accessing a regional sign-in endpoint that does not match the expected Region in the policy.
+ Your principal ARN is not correctly listed in the policy's excluded principals.
+ The policy was recently updated, and the change has not yet replicated globally.

**Resolution:**

**IAM Identity Center portal users:** Console access through the IAM Identity Center portal is not currently compatible with AWS Sign-In policies that restrict access based on network condition keys. To restore access for user in IAM Identity Center users, remove or adjust the network-based condition keys in your policy, or direct those users to sign in through an alternative authentication method.
+ Verify you are connected to your corporate network or VPN.
+ Confirm you are accessing through the correct VPC endpoint if VPC endpoint-based restrictions are configured.
+ Contact your AWS administrator to verify the policy configuration and confirm which networks are authorized.
+ If you are configured as an excluded principal, verify that your principal ARN is correctly configured in the excluded principals list.
+ If policy changes were recently made, wait a few minutes for global replication to complete.

**For administrators diagnosing this issue:**
+ Review AWS CloudTrail logs for policy evaluation events to identify which policy statement denied access.
+ Use `aws signin get-resource-policy` to review the current policy configuration.
+ Verify that the user's network location matches the conditions in the policy.
+ Confirm that excluded principals are correctly configured if the user should be exempted from network restrictions.

### I am locked out of my account after enabling console authorization
<a name="console-access-control-ts-lockout"></a>

If you configured console authorization and can no longer access your account, you may not have configured excluded principals before enforcing the policy.

There are multiple paths to regain access, depending on your account type and available credentials.

**Option 1: Use programmatic access (AWS CLI or SDK)**

Console authorization policies apply only to interactive console sign-in. They do not apply to API requests signed with SigV4. If you have programmatic access (for example, existing access keys, a cross-account role), use it to call `signin:DeleteConsoleAuthorizationConfiguration` and remove the restricting policy. The credentials you use must have permission to call `signin:DeleteConsoleAuthorizationConfiguration`. The `AWSSignInResourcePolicyManagement` managed policy includes this permission. AWS recommends temporary credentials over long-term IAM user access keys. For member accounts, management account administrators can assume `OrganizationAccountAccessRole` in the member account to obtain temporary credentials. This role is not automatically created in accounts that were invited to join the organization.

```
aws signin delete-console-authorization-configuration \
  --target-id <your-aws-account-id> \
  --region us-east-1
```

Or delete specific permission statements:

```
# First, list statements to get the statement ID
aws signin list-resource-permission-statements \
  --region us-east-1

# Then delete the problematic statement
aws signin delete-resource-permission-statement \
  --statement-id <statement-id> \
  --region us-east-1
```

**Option 2: Contact AWS Support**

If you do not have programmatic access and cannot use the `OrganizationAccountAccessRole` for account access, contact AWS Support to initiate the lockout recovery process.

The recovery process works as follows:

1. If you cannot resolve the issue using the options above, open a support case at the AWS Support Center. AWS Support will verify your identity before examining your account. Verification methods may include confirming the root user account email address, responding to a phone verification call, or answering account security questions.

1. AWS Support confirms that the console access issue is caused by a resource-based policy lockout.

1. AWS Support shares a recovery portal link. Use this link to sign in with an IAM principal in the account that has `signin:DeleteConsoleAuthorizationConfiguration` permission. This permission allows the principal to delete the console authorization configuration causing the lockout.

**Important**  
The recovery portal removes the entire console authorization configuration for the account, including all resource permission statements. The recovery portal does not allow reconfiguration of AWS Sign-In resource-based policies.

The recovery portal link expires 72 hours after AWS Support shares it. If you do not complete recovery within that window, contact AWS Support to restart the process.

**After regaining access:**
+ Review and update your resource permission statements to include properly configured excluded principals.
+ Test console access from expected networks before re-enabling console authorization.
+ Document your recovery procedures for future reference.

### Changes that I make are not always immediately visible
<a name="console-access-control-ts-replication"></a>

Policy changes replicate globally, but replication may take a few minutes.

**Resolution:**
+ Wait a few minutes after making policy changes for global replication to complete.
+ Verify your changes using the `get-resource-policy` command:

```
aws signin get-resource-policy --region <your-region>
```
+ Check AWS CloudTrail logs for policy evaluation events to confirm the new policy is being evaluated.
+ Confirm you are using the correct Region for your operations (write operations must use `us-east-1`).
+ If using VPC endpoint-based conditions, verify that the VPC endpoint policies are also correctly configured.

**Common policy replication issues:**
+ **Cached sign-in page:** Browsers may cache the sign-in page. Clear your browser cache or use an incognito window to test policy changes.
+ **Conflicting statements:** If you have multiple permission statements, confirm they do not conflict with each other. Use `get-resource-policy` to review the consolidated policy.
+ **VPC endpoint policies:** AWS Sign-In policies work in conjunction with VPC endpoint policies. Both must allow the desired access.