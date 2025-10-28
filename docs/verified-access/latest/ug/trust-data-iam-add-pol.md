# Verified Access example policies

You can use Verified Access policies to grant access to your applications to specific users
and devices.

###### Example policies

- [Example 1: Grant access to a group in IAM Identity Center](#example-policy-iam-identity-center "#example-policy-iam-identity-center")
- [Example 2: Grant access to a group in a third-party provider](#example-policy-oidc-provider "#example-policy-oidc-provider")
- [Example 3: Grant access using CrowdStrike](#example-policy-crowdstrike "#example-policy-crowdstrike")
- [Example 4: Allow or deny a specific IP address](#example-policy-ip-address "#example-policy-ip-address")

## Example 1: Grant access to a group in IAM Identity Center

When using AWS IAM Identity Center, it is better to refer to groups by using their IDs. This helps
to avoid breaking a policy statement if you change the name of the group.

The following example policy allows access only to users in the specified group
with a verified email address. The group ID is c242c5b0-6081-1845-6fa8-6e0d9513c107.

```
permit(principal,action,resource)
when {
    context.`policy-reference-name`.groups has "`c242c5b0-6081-1845-6fa8-6e0d9513c107`"
    && context.`policy-reference-name`.user.email.verified == true
};
```

The following example policy allows access only when the user is in the specified group,
the user has a verified email address, and the Jamf device risk score is `LOW`.

```
permit(principal,action,resource)
when {
    context.`policy-reference-name`.groups has "`c242c5b0-6081-1845-6fa8-6e0d9513c107`"
    && context.`policy-reference-name`.user.email.verified == true
    && context.jamf.risk == "LOW"
};
```

For more information about the trust data, see [AWS IAM Identity Center context for Verified Access trust data](trust-data-iam.md "trust-data-iam.md").

## Example 2: Grant access to a group in a third-party provider

The following example policy allows access only when the user is in the specified
group, the user has a verified email address, and the Jamf device risk score is LOW.
The name of the group is "finance".

```
permit(principal,action,resource)
when {
     context.`policy-reference-name`.groups.contains("`finance`")
     && context.`policy-reference-name`.email_verified == true
     && context.jamf.risk == "LOW"
};
```

For more information about the trust data, see [Third-party trust provider context for Verified Access trust data](trust-data-third-party-trust.md "trust-data-third-party-trust.md").

## Example 3: Grant access using CrowdStrike

The following example policy allows access when the overall assessment score is greater
than 50.

```
permit(principal,action,resource)
when {
    context.crwd.assessment.overall > 50
};
```

## Example 4: Allow or deny a specific IP address

The following example policy allows HTTP requests from the specified IP address.

```
permit(principal, action, resource)
when {
    context.http_request.client_ip == "`192.0.2.1`"
};
```

The following example policy denies HTTP requests from the specified IP address.

```
forbid(principal,action,resource)
when {
    ip(context.http_request.client_ip).isInRange(ip("`192.0.2.1/32`"))
};
```

The following example policy allows TCP requests from the specified IP address.

```
permit(principal, action, resource)
when {
    context.tcp_flow.client_ip == "`192.0.2.1`"
};
```
