

# Using aliases for trust anchors, profiles, and CRLs

An *alias* is a readable name that you assign to a trust anchor, a profile, or a certificate revocation list (CRL). Aliases make configuration easier to read and to reuse. For example, a credential helper configuration that refers to a trust anchor by the alias `production-ca` shows which certificate authority it uses. If you assign the same alias to a trust anchor in each account and Region, your configurations differ only in the account and Region.

A resource with an alias has an *alias ARN*, such as `arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca`. The resource also keeps its *canonical ARN*, which contains the resource ID. You can use the alias ARN in place of the resource ID or the canonical ARN in many IAM Roles Anywhere operations, including `CreateSession` and the credential helper. An alias ARN is always a full ARN. You can't specify the alias name alone. For the list of operations, see [Use an alias ARN](#resource-aliases-use).

Use an alias ARN when you want your client to follow whichever resource currently holds the alias. Use the canonical ARN when your client must always use one specific resource, and in IAM policies and role trust policies. For recommendations, see [Security recommendations for aliases](#resource-aliases-security).

An alias is a property of the resource, so you set, change, and remove it with the existing create, import, and update operations. For permissions, see [Permissions and IAM policies for aliases](#resource-aliases-iam).

**Topics**
+ [Minimum versions to set and use an alias](#resource-aliases-versions)
+ [Manage an alias](#resource-aliases-manage)
+ [Use an alias ARN](#resource-aliases-use)
+ [Security recommendations for aliases](#resource-aliases-security)
+ [Considerations when you move an alias](#resource-aliases-moving)
+ [Aliases in CloudTrail logs](#resource-aliases-cloudtrail)
+ [Alias reference](#resource-aliases-reference)

## Minimum versions to set and use an alias
<a name="resource-aliases-versions"></a>

To set, change, or remove an alias with the AWS CLI or an AWS SDK, you need a version that supports the `--alias-name` option or the `aliasName` parameter. The following table lists the minimum version for each tool.


| Tool | Minimum version | 
| --- | --- | 
| AWS CLI version 2 | [2.40.3](https://github.com/aws/aws-cli/releases/tag/2.40.3) | 
| AWS CLI version 1 | Not supported | 
| AWS SDK for Python (Boto3) | [1.44.3](https://github.com/boto/boto3/releases/tag/1.44.3) | 
| AWS SDK for Java 2.x | [2.59.1](https://github.com/aws/aws-sdk-java-v2/releases/tag/2.59.1) | 
| AWS SDK for JavaScript v3 | [3.1169.0](https://github.com/aws/aws-sdk-js-v3/releases/tag/v3.1169.0) | 
| AWS SDK for Go v2 | [1.34.0](https://github.com/aws/aws-sdk-go-v2/releases/tag/service%2Frolesanywhere%2Fv1.34.0) | 
| AWS SDK for PHP | [3.403.6](https://github.com/aws/aws-sdk-php/releases/tag/3.403.6) | 
| AWS SDK for Ruby | [1.68.0](https://rubygems.org/gems/aws-sdk-rolesanywhere/versions/1.68.0) | 
| AWS SDK for .NET | [4.1.1.0](https://www.nuget.org/packages/AWSSDK.IAMRolesAnywhere/4.1.1.0) | 
| AWS SDK for C\+\+ | [1.11.929](https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.929) | 

### Minimum versions to use an alias ARN with CreateSession
<a name="resource-aliases-versions-createsession"></a>

The following table lists the minimum version of the credential helper to use an alias ARN as the trust anchor or profile in `CreateSession`.


| Tool | Minimum version | Notes | 
| --- | --- | --- | 
| [Credential helper](credential-helper.md) | All versions ([releases](https://github.com/aws/rolesanywhere-credential-helper/releases)) | The --trust-anchor-arn and --profile-arn options accept a canonical ARN or an alias ARN in every version, so you don't need to upgrade the credential helper to use aliases. | 

## Manage an alias
<a name="resource-aliases-manage"></a>

You can set an alias when you create a trust anchor, profile, or CRL, or add one later. In the console, enter a name in the optional **Alias** field for a trust anchor or profile. In the AWS CLI or API, use the `--alias-name` option or the `aliasName` parameter of the create, import, and update operations.

In an update request, `aliasName` works as follows:
+ To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource.
+ To remove the alias, specify an empty string (`""`).
+ To keep the current alias, omit `aliasName`.

A resource can't take an alias that another resource of the same type holds. To move an alias to a different resource, first remove it from the resource that holds it, and then set it on the other resource. Before you move an alias, read [Considerations when you move an alias](#resource-aliases-moving).

### Manage an alias (console)
<a name="resource-aliases-manage-console"></a>

When you create or edit a trust anchor or a profile in the [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home), enter the alias name in the optional **Alias** field. To remove an alias, clear the field and save your changes. The details page of the trust anchor or profile shows its alias ARN.

### Manage an alias (AWS CLI)
<a name="resource-aliases-manage-cli"></a>

You can manage the aliases of trust anchors, profiles, and CRLs with the AWS CLI by using the `--alias-name` option. The following examples show how to create a profile with an alias, change the alias of a trust anchor, and remove the alias of a CRL.

The following AWS CLI command creates a profile with the alias `web-servers`:

```bash
PROMPT> aws rolesanywhere create-profile \
    --name {{web-servers-profile}} \
    --role-arns {{arn:aws:iam::111122223333:role/WebServerRole}} \
    --alias-name web-servers
```

The `profile` object in the response includes the alias and the alias ARN, in addition to the profile ID and the canonical ARN.

```json
{
    "profile": {
        "profileId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "profileArn": "arn:aws:rolesanywhere:us-east-1:111122223333:profile/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "aliasName": "web-servers",
        "aliasArn": "arn:aws:rolesanywhere:us-east-1:111122223333:alias/profile/web-servers",
        "name": "web-servers-profile",
        ...
    }
}
```

The following AWS CLI command changes the alias of a trust anchor to `production-ca-2027`. The command identifies the trust anchor by its current alias ARN:

```bash
PROMPT> aws rolesanywhere update-trust-anchor \
    --trust-anchor-id arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca \
    --alias-name production-ca-2027
```

The response contains `"aliasName": "production-ca-2027"` and `"previousAliasName": "production-ca"`.

The following AWS CLI command removes the alias of a CRL:

```bash
PROMPT> aws rolesanywhere update-crl \
    --crl-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}} \
    --alias-name ""
```

The response doesn't contain `aliasName` or `aliasArn`, and it contains the removed alias in `previousAliasName`.

### Manage an alias (API)
<a name="resource-aliases-manage-api"></a>

The following table lists the operations that set or change an alias for each resource type.


| Resource | Set an alias when you create the resource | Set, change, or remove an alias later | 
| --- | --- | --- | 
| Trust anchor | [CreateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateTrustAnchor.html) | [UpdateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateTrustAnchor.html) | 
| Profile | [CreateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateProfile.html) | [UpdateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateProfile.html) | 
| CRL | [ImportCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ImportCrl.html) | [UpdateCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateCrl.html) | 

For the request syntax of each operation, see the [IAM Roles Anywhere API Reference](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/Welcome.html).

## Use an alias ARN
<a name="resource-aliases-use"></a>

You can use an alias ARN with the credential helper and `CreateSession`, and with the operations that manage trust anchors, profiles, and CRLs. An alias ARN identifies a resource only in the account and Region in the ARN, and it must be for the type of resource that the parameter expects. For example, you can't use a profile alias ARN as a `trustAnchorId`.

### Use alias ARNs with the credential helper
<a name="resource-aliases-use-credential-helper"></a>

The credential helper passes the trust anchor and profile ARNs to `CreateSession` as you specify them, so you can configure it with alias ARNs. As with canonical ARNs, the trust anchor and the profile must be in the same Region. The following example shows a credential process configuration that uses alias ARNs:

```text
[profile workload]
credential_process = ./aws_signing_helper credential-process \
    --certificate {{/path/to/certificate}} \
    --private-key {{/path/to/private-key}} \
    --trust-anchor-arn arn:aws:rolesanywhere:{{region}}:{{account}}:alias/trust-anchor/production-ca \
    --profile-arn arn:aws:rolesanywhere:{{region}}:{{account}}:alias/profile/web-servers \
    --role-arn arn:aws:iam::{{account}}:role/{{role-name-with-path}}
```

When `CreateSession` receives an alias ARN, IAM Roles Anywhere uses the trust anchor or profile that holds the alias at the time of the request. If no trust anchor or profile holds the alias, the request fails and no credentials are issued. The `aws:SourceArn` value that IAM Roles Anywhere sets when it assumes the role is always the canonical ARN of that trust anchor, even when the request used a trust anchor alias ARN.

### Use alias ARNs in management operations
<a name="resource-aliases-use-management"></a>

The following table lists the parameters that accept an alias ARN.


| Parameter | Operations | Accepted identifiers | 
| --- | --- | --- | 
| trustAnchorId | [GetTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetTrustAnchor.html), [UpdateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateTrustAnchor.html), [DeleteTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteTrustAnchor.html), [EnableTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableTrustAnchor.html), [DisableTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableTrustAnchor.html) | Resource ID, canonical ARN, or alias ARN | 
| profileId | [GetProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetProfile.html), [UpdateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateProfile.html), [DeleteProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteProfile.html), [EnableProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableProfile.html), [DisableProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableProfile.html), [PutAttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_PutAttributeMapping.html), [DeleteAttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteAttributeMapping.html) | Resource ID, canonical ARN, or alias ARN | 
| crlId | [GetCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetCrl.html), [UpdateCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateCrl.html), [DeleteCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteCrl.html), [EnableCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableCrl.html), [DisableCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableCrl.html) | Resource ID, canonical ARN, or alias ARN | 
| trustAnchorArn and profileArn | CreateSession | Canonical ARN or alias ARN | 

Other parameters, such as the `trustAnchorArn` parameter of `ImportCrl`, the `trustAnchorId` parameter of [PutNotificationSettings](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_PutNotificationSettings.html) and [ResetNotificationSettings](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ResetNotificationSettings.html), and the `resourceArn` parameter of the tagging operations, don't accept alias ARNs. For those parameters, use the identifier that the parameter's documentation describes.

The following AWS CLI command gets a trust anchor by its alias ARN:

```bash
PROMPT> aws rolesanywhere get-trust-anchor \
    --trust-anchor-id arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca
```

**Note**  
If you call the IAM Roles Anywhere API directly instead of through an AWS SDK or the AWS CLI, URL-encode an ARN that you pass in the request path.

## Security recommendations for aliases
<a name="resource-aliases-security"></a>

An alias ARN identifies whichever resource holds the alias when IAM Roles Anywhere handles the request. Any operation that you call with an alias ARN, including a delete operation, acts on that resource. Anyone who can move an alias can therefore change which resource your clients use, as follows:
+ **Trust anchors**—Workloads that use a trust anchor alias ARN authenticate against the trust anchor that currently holds the alias. If the alias moves to a trust anchor for a different certificate authority, certificates from that certificate authority can authenticate through the same configuration.
+ **Profiles**—Sessions created with a profile alias ARN use the roles, session policies, and attribute mappings of the profile that currently holds the alias.
+ **CRLs**—Operations that use a CRL alias ARN, such as `UpdateCrl`, `DisableCrl`, or `DeleteCrl`, act on the CRL that currently holds the alias.

To protect against an unexpected change of resource, we recommend the following:
+ In each role trust policy, use the `aws:SourceArn` condition key with the *canonical* ARN of the trust anchor that you expect. The condition stays bound to that trust anchor, so moving a trust anchor alias doesn't let a different trust anchor assume the role. For more information, see [Trust policy](trust-model.md#trust-policy).
+ Grant permission for the operations that set, change, or remove aliases only to the administrators who manage these resources. These operations are `CreateTrustAnchor`, `UpdateTrustAnchor`, `DeleteTrustAnchor`, `CreateProfile`, `UpdateProfile`, `DeleteProfile`, `ImportCrl`, `UpdateCrl`, and `DeleteCrl`. For how IAM evaluates requests that use an alias ARN, see [Permissions and IAM policies for aliases](#resource-aliases-iam).
+ When you remove an alias or delete the resource that holds it, any principal that can create or update a resource of the same type can claim the alias. If clients still use the alias ARN, set the alias on the replacement resource right away, or update those clients first.
+ Where a client must always use one specific resource, configure it with the canonical ARN instead of an alias ARN.
+ For operations that change or delete a specific resource, such as `DeleteTrustAnchor` or `DisableProfile`, identify the resource by its ID or canonical ARN, especially right after you move an alias.
+ Alias names are case sensitive, so a near-duplicate alias such as `Production-CA` and `production-ca` can identify two different resources and mislead anyone who reviews a configuration. Use one naming convention, for example lowercase letters only, and check for near-duplicate aliases before you create one.

### Permissions and IAM policies for aliases
<a name="resource-aliases-iam"></a>

In IAM policies and VPC endpoint policies, specify trust anchors, profiles, and CRLs by their canonical ARNs. In an IAM policy, a statement on a canonical ARN applies to every request for that resource, whether the request uses the resource ID, the canonical ARN, or the alias ARN. In a VPC endpoint policy, a `CreateSession` statement that names a trust anchor by its canonical ARN also applies when the request uses the trust anchor's alias ARN. In role trust policies, use the trust anchor's canonical ARN in the `aws:SourceArn` condition.

**Warning**  
Don't use an alias ARN in the `Resource` element of a policy. IAM accepts the statement, but it has no effect: an `Allow` doesn't grant access, and a `Deny` doesn't block it.

You can't write conditions on aliases. IAM Roles Anywhere doesn't provide condition keys for alias names or alias ARNs.

Aliases don't add IAM actions. To set, change, or remove an alias, you need permission for the operation that creates or updates the resource, such as `rolesanywhere:UpdateTrustAnchor`.

## Considerations when you move an alias
<a name="resource-aliases-moving"></a>

Move an alias only when the new resource can replace the old one for every client that uses the alias ARN, for example when you re-create a trust anchor or profile from infrastructure as code. For a trust anchor, the new trust anchor must accept the same certificates as the old one. An alias can't cover a period when both resources must be active, such as a certificate authority rotation. In that case, configure clients with canonical ARNs.

Before you move an alias, consider the following:
+ A move takes two updates. You remove the alias from one resource, and then set it on the other. Between the two updates, requests that use the alias ARN fail.
+ A change can take a short time to take effect. During that time, the alias ARN might still resolve to the previous resource or might not resolve yet.
+ Credentials that IAM Roles Anywhere already issued remain valid until they expire.

For security recommendations, see [Security recommendations for aliases](#resource-aliases-security).

## Aliases in CloudTrail logs
<a name="resource-aliases-cloudtrail"></a>

CloudTrail records the `aliasName` parameter that you send to the create, import, and update operations, and the `aliasName`, `aliasArn`, and `previousAliasName` fields in the responses of those operations. Error messages that name an alias, such as the message for an alias that is already in use, also appear in CloudTrail events. When a `CreateSession` request identifies the trust anchor or profile by its alias ARN, the alias ARN appears in the CloudTrail event for that request. Anyone who can read your CloudTrail events can see your alias names. For more information about IAM Roles Anywhere and CloudTrail, see [CloudTrail logs](logging-using-cloudtrail.md).

## Alias reference
<a name="resource-aliases-reference"></a>

### Alias ARN format
<a name="resource-aliases-arn"></a>

An alias ARN has the following format:

```text
arn:{{partition}}:rolesanywhere:{{region}}:{{account}}:alias/{{resource-type}}/{{alias-name}}
```

The {{resource-type}} is `trust-anchor`, `profile`, or `crl`. The alias ARN doesn't replace the canonical ARN. A resource with an alias has both ARNs, and IAM Roles Anywhere returns both.

The following table shows example canonical and alias ARNs for each resource type.


| Resource | Canonical ARN | Alias ARN | 
| --- | --- | --- | 
| Trust anchor | arn:aws:rolesanywhere:us-east-1:111122223333:trust-anchor/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 | arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca | 
| Profile | arn:aws:rolesanywhere:us-east-1:111122223333:profile/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 | arn:aws:rolesanywhere:us-east-1:111122223333:alias/profile/web-servers | 
| CRL | arn:aws:rolesanywhere:us-east-1:111122223333:crl/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333 | arn:aws:rolesanywhere:us-east-1:111122223333:alias/crl/revocation-prod | 

In the `TrustAnchorDetail`, `ProfileDetail`, and `CrlDetail` objects that IAM Roles Anywhere returns, the alias is in the `aliasName` field and the alias ARN is in the `aliasArn` field. Both fields are present only when the resource has an alias.

### Alias naming rules
<a name="resource-aliases-rules"></a>

**Important**  
Alias names appear in CloudTrail logs and in the responses of IAM Roles Anywhere operations. Don't put confidential or sensitive information in an alias name. For more information, see [Aliases in CloudTrail logs](#resource-aliases-cloudtrail).

An alias name must meet the following requirements:
+ It contains 1 to 256 characters.
+ It begins with a letter (A-Z or a-z).
+ It contains only letters (A-Z and a-z), numbers (0-9), underscores (\_), hyphens (-), and forward slashes (/). Periods (.), spaces, and other characters aren't allowed.
+ A forward slash can appear only between two other characters. An alias name can't end with a forward slash or contain two forward slashes in a row. For example, `prod/web-servers` is valid, and `prod/` and `prod//web-servers` aren't.
+ It doesn't begin with `aws/`, in any combination of uppercase and lowercase letters. IAM Roles Anywhere reserves this prefix.

**Uniqueness**

An alias name must be unique among the resources of the same type in your AWS account and Region. You can use the same alias name for a trust anchor and a profile, or for trust anchors in different Regions, because their alias ARNs differ.

**Case sensitivity**

Alias names are case sensitive. `Production-CA` and `production-ca` are different aliases, and two trust anchors can hold them at the same time. An alias ARN identifies a resource only when its alias name matches the case of the alias exactly. For a naming recommendation, see [Security recommendations for aliases](#resource-aliases-security).

**Limits**

Each trust anchor, profile, or CRL can have at most one alias. Aliases don't have their own quota.

### Alias behavior and error reference
<a name="resource-aliases-behavior"></a>

**The previousAliasName field**

When an update changes or removes an existing alias, the response includes `previousAliasName`, which contains the alias that the resource had before the request. The response doesn't include `previousAliasName` when the alias is unchanged or when the resource had no alias before the request. Other operations don't return it.

**An alias ARN that no resource holds**

If a request names an alias ARN that no resource holds, the error depends on your permissions:
+ If your policies allow the action on every resource of that type, IAM Roles Anywhere returns `ResourceNotFoundException`. For trust anchors, for example, that means a `Resource` element of `arn:aws:rolesanywhere:{{region}}:{{account}}:trust-anchor/*`.
+ Otherwise, IAM Roles Anywhere returns `AccessDeniedException`.

This applies to the `trustAnchorId`, `profileId`, and `crlId` parameters.