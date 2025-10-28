# Using IPv6 addresses in IAM and AWS Private CA

Before trying to access AWS Private Certificate Authority over IPv6, ensure any IAM policies containing
IP address restrictions are updated to include IPv6 address ranges. IP based
policies that are not updated to handle IPv6 addresses may result in clients
incorrectly losing or gaining access when they start using IPv6. To learn more about
AWS Private CA and dual-stack support, see [Dual-stack endpoint support](dual-stack-endpoint-support.md "dual-stack-endpoint-support.md").

###### Important

These statements do not allow any actions. Use these statements in combination
with other statements that allow specific actions.

The following statement explicitly denies access to all AWS Private CA permissions for
requests originating from the `192.0.2.*` range of IPv4 addresses. Any IP
addresses outside of this range are not explicitly denied AWS Private CA permissions. Since
all IPv6 addresses are outside of the denied range, this statement does not
explicitly deny AWS Private CA permissions for any IPv6 addresses.

```

{
    "Sid": "DenyPrivateCAPermissions",
    "Effect": "Deny",
    "Action": [
        "acm-pca:*"
    ],
    "Resource": "*",
    "Condition": {
        "NotIpAddress": {
            "aws:SourceIp": [
                "192.0.2.0/24"
            ]
        }
    }
}
```

You can modify the `Condition` element to deny both IPv4
(`192.0.2.0/24`) and IPv6 (`2001:db8::/32`) address ranges
as shown in the following example:

```

{
    "Sid": "DenyPrivateCAPermissions",
    "Effect": "Deny",
    "Action": [
        "acm-pca:*"
    ],
    "Resource": "*",
    "Condition": {
        "NotIpAddress": {
            "aws:SourceIp": [
                "192.0.2.0/24",
                "2001:db8::/32"
            ]
        }
    }
}
```
