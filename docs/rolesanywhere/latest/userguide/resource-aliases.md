

# Using aliases for trust anchors, profiles, and CRLs
<a name="resource-aliases"></a>

An *alias* is a readable name that you assign to a trust anchor, a profile, or a certificate revocation list (CRL). When a resource has an alias, IAM Roles Anywhere gives it a second ARN, called its *alias ARN*. You can use the alias ARN in place of the resource ID or the resource ARN in many of the IAM Roles Anywhere operations that identify that resource, including `CreateSession` and the credential helper. For the list, see [Use an alias ARN](#resource-aliases-use).

Aliases make configuration easier to read and to reuse. For example, a credential helper configuration with the alias ARN `arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca` shows which certificate authority it uses. If you create a trust anchor with the same alias in each account and Region, the configurations differ only in the Region and account parts of the ARN. An alias ARN is always a full ARN. You can't specify the alias name alone.

An alias is a property of the resource. You set, change, and remove it with the existing create, import, and update operations. There are no separate alias operations and no separate alias permissions.

**Topics**
+ [Alias ARN format](#resource-aliases-arn)
+ [Alias naming rules](#resource-aliases-rules)
+ [Set, change, and remove an alias](#resource-aliases-manage)
+ [Use an alias ARN](#resource-aliases-use)
+ [Considerations when you move an alias](#resource-aliases-moving)
+ [Aliases and IAM policies](#resource-aliases-iam)
+ [Aliases in CloudTrail logs](#resource-aliases-cloudtrail)

## Alias ARN format
<a name="resource-aliases-arn"></a>

An alias ARN has the following format:

```
arn:{{partition}}:rolesanywhere:{{region}}:{{account}}:alias/{{resource-type}}/{{alias-name}}
```

The {{resource-type}} is `trust-anchor`, `profile`, or `crl`. The alias ARN doesn't replace the resource ARN that contains the resource ID. In this guide, that ARN is called the *canonical ARN*. A resource with an alias has both ARNs, and IAM Roles Anywhere returns both.

The following table shows example canonical and alias ARNs for each resource type.


| Resource | Canonical ARN | Alias ARN | 
| --- | --- | --- | 
| Trust anchor | arn:aws:rolesanywhere:us-east-1:111122223333:trust-anchor/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 | arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca | 
| Profile | arn:aws:rolesanywhere:us-east-1:111122223333:profile/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 | arn:aws:rolesanywhere:us-east-1:111122223333:alias/profile/web-servers | 
| CRL | arn:aws:rolesanywhere:us-east-1:111122223333:crl/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333 | arn:aws:rolesanywhere:us-east-1:111122223333:alias/crl/revocation-prod | 

In the `TrustAnchorDetail`, `ProfileDetail`, and `CrlDetail` objects that IAM Roles Anywhere returns, the alias is in the `aliasName` field and the alias ARN is in the `aliasArn` field. Both fields are present only when the resource has an alias.

## Alias naming rules
<a name="resource-aliases-rules"></a>

An alias name must meet the following requirements:
+ It contains 1 to 256 characters.
+ It begins with a letter (A-Z or a-z).
+ It contains only letters (A-Z and a-z), numbers (0-9), underscores (\_), hyphens (-), and forward slashes (/). Periods (.), spaces, and other characters aren't allowed.
+ A forward slash can appear only between two other characters. An alias name can't end with a forward slash or contain two forward slashes in a row. For example, `prod/web-servers` is valid, and `prod/` and `prod//web-servers` aren't.
+ It doesn't begin with `aws/`, in any combination of uppercase and lowercase letters. IAM Roles Anywhere reserves this prefix.

**Uniqueness**

An alias name must be unique among the resources of the same type in your AWS account and Region. You can use the same alias name for a trust anchor and a profile, or for trust anchors in different Regions, because their alias ARNs differ.

**Case sensitivity**

Alias names are case sensitive. `Production-CA` and `production-ca` are different aliases, and two trust anchors can hold them at the same time. An alias ARN identifies a resource only when its alias name matches the case of the alias exactly.

**Limits**

Each trust anchor, profile, or CRL can have at most one alias. Aliases don't have their own quota.

**Important**  
Alias names appear in CloudTrail logs and in the responses of IAM Roles Anywhere operations. Don't put confidential or sensitive information in an alias name. For more information, see [Aliases in CloudTrail logs](#resource-aliases-cloudtrail).

## Set, change, and remove an alias
<a name="resource-aliases-manage"></a>

You manage an alias with the `aliasName` parameter. The following table lists the operations that set or change an alias for each resource type.


| Resource | Set an alias when you create the resource | Set, change, or remove an alias later | 
| --- | --- | --- | 
| Trust anchor | CreateTrustAnchor | UpdateTrustAnchor | 
| Profile | CreateProfile | UpdateProfile | 
| CRL | ImportCrl | UpdateCrl | 

In an update request, `aliasName` works as follows:
+ To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource.
+ To remove the alias, specify an empty string (`""`).
+ To keep the current alias, omit `aliasName`.

When an update changes or removes an existing alias, the response includes `previousAliasName`, which contains the alias that the resource had before the request. The response doesn't include `previousAliasName` when the alias is unchanged or when the resource had no alias before the request. Other operations don't return it.

When you remove an alias or delete the resource that holds it, IAM Roles Anywhere releases the alias, and you can assign it to another resource of the same type. If you reuse an alias immediately after you release it, IAM Roles Anywhere might still report the alias as in use and the request might fail. If that happens, wait a short time and try again.

A resource can't take an alias that another resource of the same type holds. To move an alias to a different resource, first remove it from the resource that holds it, and then set it on the other resource. Before you move an alias, read [Considerations when you move an alias](#resource-aliases-moving).

### Manage an alias (console)
<a name="resource-aliases-manage-console"></a>

When you create or edit a trust anchor or a profile in the [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home), enter the alias name in the optional **Alias** field. To remove an alias, clear the field and save your changes. The details page of the trust anchor or profile shows its alias ARN. To manage the alias of a CRL, use the API or the AWS CLI.

### Manage an alias (AWS CLI)
<a name="resource-aliases-manage-cli"></a>

The following AWS CLI command creates a profile with the alias `web-servers`:

```
PROMPT> aws rolesanywhere create-profile \
    --name {{web-servers-profile}} \
    --role-arns {{arn:aws:iam::111122223333:role/WebServerRole}} \
    --alias-name web-servers
```

The `profile` object in the response includes the alias and the alias ARN, in addition to the profile ID and the canonical ARN.

```
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

The `--trust-anchor-id` value can be the trust anchor ID, its canonical ARN, or its current alias ARN. The following AWS CLI command changes the alias of a trust anchor to `production-ca-2027`:

```
PROMPT> aws rolesanywhere update-trust-anchor \
    --trust-anchor-id arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca \
    --alias-name production-ca-2027
```

The response contains `"aliasName": "production-ca-2027"` and `"previousAliasName": "production-ca"`.

The following AWS CLI command removes the alias of a CRL:

```
PROMPT> aws rolesanywhere update-crl \
    --crl-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}} \
    --alias-name ""
```

The response doesn't contain `aliasName` or `aliasArn`, and it contains the removed alias in `previousAliasName`.

## Use an alias ARN
<a name="resource-aliases-use"></a>

Wherever the following parameters accept a resource ID or a canonical ARN, they also accept the alias ARN of a resource of the same type:
+ `trustAnchorId` in `GetTrustAnchor`, `UpdateTrustAnchor`, `DeleteTrustAnchor`, `EnableTrustAnchor`, and `DisableTrustAnchor`.
+ `profileId` in `GetProfile`, `UpdateProfile`, `DeleteProfile`, `EnableProfile`, `DisableProfile`, `PutAttributeMapping`, and `DeleteAttributeMapping`.
+ `crlId` in `GetCrl`, `UpdateCrl`, `DeleteCrl`, `EnableCrl`, and `DisableCrl`.
+ `trustAnchorArn` and `profileArn` in `CreateSession`, and the matching `--trust-anchor-arn` and `--profile-arn` options of the credential helper. These parameters accept a canonical ARN or an alias ARN, but not a resource ID.

Other parameters, such as the `trustAnchorArn` parameter of `ImportCrl`, the `trustAnchorId` parameter of `PutNotificationSettings` and `ResetNotificationSettings`, and the `resourceArn` parameter of the tagging operations, don't accept alias ARNs. For those parameters, use the identifier that the parameter's documentation describes.

The alias ARN must be for the type of resource that the parameter expects. For example, you can't use a profile alias ARN as a `trustAnchorId`. An alias ARN identifies a resource only in the account and Region in the ARN.

The following AWS CLI command gets a trust anchor by its alias ARN:

```
PROMPT> aws rolesanywhere get-trust-anchor \
    --trust-anchor-id arn:aws:rolesanywhere:us-east-1:111122223333:alias/trust-anchor/production-ca
```

**Note**  
If you call the IAM Roles Anywhere API directly instead of through an AWS SDK or the AWS CLI, URL-encode an ARN that you pass in the request path.

### Use alias ARNs with the credential helper
<a name="resource-aliases-use-credential-helper"></a>

The credential helper passes the trust anchor and profile ARNs to `CreateSession` as you specify them, so you can configure it with alias ARNs. As with canonical ARNs, the trust anchor and the profile must be in the same Region. The following example shows a credential process configuration that uses alias ARNs:

```
[profile workload]
credential_process = ./aws_signing_helper credential-process \
    --certificate {{/path/to/certificate}} \
    --private-key {{/path/to/private-key}} \
    --trust-anchor-arn arn:aws:rolesanywhere:{{region}}:{{account}}:alias/trust-anchor/production-ca \
    --profile-arn arn:aws:rolesanywhere:{{region}}:{{account}}:alias/profile/web-servers \
    --role-arn arn:aws:iam::{{account}}:role/{{role-name-with-path}}
```

When `CreateSession` receives an alias ARN, IAM Roles Anywhere uses the trust anchor or profile that holds the alias at the time of the request. If no trust anchor or profile holds the alias, the request fails and no credentials are issued. The `aws:SourceArn` value that IAM Roles Anywhere sets when it assumes the role is always the canonical ARN of that trust anchor, even when the request used an alias ARN.

## Considerations when you move an alias
<a name="resource-aliases-moving"></a>

When you configure a client with an alias ARN, the client follows the alias, not a specific resource. Any operation that you call with an alias ARN, including a delete operation, acts on the resource that IAM Roles Anywhere finds for the alias when it handles the request. When you move the alias to a different resource, your clients start to use the new resource without a configuration change, after the short delay described at the end of this section.

This helps when you replace a trust anchor or a profile. It also means that anyone who can move an alias can change which resource your clients use, as follows:
+ **Trust anchors**—Workloads that use a trust anchor alias ARN authenticate against the trust anchor that currently holds the alias. If the alias moves to a trust anchor for a different certificate authority, certificates from that certificate authority can authenticate through the same configuration.
+ **Profiles**—Sessions created with a profile alias ARN use the roles, session policies, and attribute mappings of the profile that currently holds the alias. If the alias moves to a profile with broader session policies, or with no session policies, the sessions get the broader permissions. No role trust policy condition binds a session to a specific profile. Protect profile aliases with the permissions recommendation that follows.
+ **CRLs**—Operations that use a CRL alias ARN, such as `UpdateCrl`, `DisableCrl`, or `DeleteCrl`, act on the CRL that currently holds the alias.

To reduce this risk, we recommend the following:
+ In each role trust policy, use the `aws:SourceArn` condition key with the *canonical* ARN of the trust anchor that you expect. The condition stays bound to that trust anchor, so moving a trust anchor alias doesn't let a different trust anchor assume the role. For more information, see [Trust policy](trust-model.md#trust-policy).
+ Grant permission for the operations that set, change, or remove aliases only to the administrators who manage these resources. These operations are `CreateTrustAnchor`, `UpdateTrustAnchor`, `DeleteTrustAnchor`, `CreateProfile`, `UpdateProfile`, `DeleteProfile`, `ImportCrl`, `UpdateCrl`, and `DeleteCrl`. You can't limit these permissions to specific alias names.
+ When you remove an alias or delete the resource that holds it, any principal that can create or update a resource of the same type can claim the alias. If clients still use the alias ARN, set the alias on the replacement resource right away, or update those clients first.
+ Where a client must always use one specific resource, configure it with the canonical ARN instead of an alias ARN.
+ For operations that change or delete a specific resource, such as `DeleteTrustAnchor` or `DisableProfile`, identify the resource by its ID or canonical ARN, especially right after you move an alias.
+ A move takes two update requests, and between them no resource holds the alias, so requests that use the alias ARN fail. Plan the move for a time when clients that use the alias ARN can tolerate failed requests.

After you set, change, or remove an alias, requests that use the alias ARN might continue to resolve to the previous state for a short time: a new alias might not resolve yet, and a changed or removed alias might still resolve to the previous resource.

## Aliases and IAM policies
<a name="resource-aliases-iam"></a>

Write IAM policies with the canonical ARN of each resource. When a request identifies a resource by its alias ARN or its canonical ARN, IAM Roles Anywhere resolves it to the resource and authorizes the request against the canonical ARN. A policy statement that allows or denies access to a canonical ARN therefore applies however the request identifies the resource: by resource ID, by canonical ARN, or by alias ARN. In a VPC endpoint policy, a `CreateSession` statement that names a trust anchor by its canonical ARN applies when the request names that trust anchor by its alias ARN.

An alias ARN in the `Resource` element of a policy statement doesn't apply to the resource that holds the alias. IAM accepts such a statement, but it doesn't allow or deny access to that resource. IAM Roles Anywhere doesn't provide condition keys for alias names or alias ARNs, so you can't allow or deny a request based on the alias that it uses.

Aliases don't add IAM actions. To set an alias, you need permission for the operation that creates or updates the resource, such as `rolesanywhere:UpdateTrustAnchor`.

If the `trustAnchorId`, `profileId`, or `crlId` parameter of a request is an alias ARN that no resource holds, IAM Roles Anywhere returns `ResourceNotFoundException` only if your policies allow the action on every resource of that type. Otherwise, it returns `AccessDeniedException`. For example, for trust anchors, a policy allows the action on every resource of the type when its `Resource` element is `arn:aws:rolesanywhere:{{region}}:{{account}}:trust-anchor/*`.

## Aliases in CloudTrail logs
<a name="resource-aliases-cloudtrail"></a>

CloudTrail records the `aliasName` parameter that you send to the create, import, and update operations, and the `aliasName`, `aliasArn`, and `previousAliasName` fields in the responses of those operations. Error messages that name an alias, such as the message for an alias that is already in use, also appear in CloudTrail events. Anyone who can read your CloudTrail events can see your alias names. For more information about IAM Roles Anywhere and CloudTrail, see [CloudTrail logs](logging-using-cloudtrail.md).