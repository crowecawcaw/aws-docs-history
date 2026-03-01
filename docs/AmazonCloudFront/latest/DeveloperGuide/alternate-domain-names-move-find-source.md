# Find the source standard distribution or distribution tenant

Before you can move an alternate domain name from one distribution (standard or
tenant) to another, find the _source distribution_.
This is the resource that the alternate domain name is already associated with. When you
know the AWS account ID of both the source and target distribution resources, you can
determine how to move the alternate domain name.

###### Notes

- We recommend that you use the [ListDomainConflicts](../../../cloudfront/latest/APIReference/API_ListDomainConflicts.md "../../../cloudfront/latest/APIReference/API_ListDomainConflicts.md") API operation, because it supports both
  standard distributions and distribution tenants.
- The [ListConflictingAliases](../../../cloudfront/latest/APIReference/API_ListConflictingAliases.md "../../../cloudfront/latest/APIReference/API_ListConflictingAliases.md") API operation only supports
  standard distributions.
  Follow these examples to find the source distribution (standard or tenant).

list-domain-conflicts

###### Tip

- For a standard distribution, you must have the
  `cloudfront:GetDistribution` and
  `cloudfront:ListDomainConflicts`
  permissions.
- For a distribution tenant, you must have the
  `cloudfront:GetDistributionTenant` and
  `cloudfront:ListDomainConflicts`
  permissions.

###### To use `list-domain-conflicts` to find the source standard distribution or distribution tenant

1. Use the `list-domain-conflicts` command as shown in the
   following example.
   1. Replace `www.example.com` with
      the domain name.
   2. For the `domain-control-validation-resource`, specify the ID of the target
      standard distribution or distribution tenant [that
      you set up previously](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md"). You must have a standard distribution
      or distribution tenant that is associated with a certificate that
      covers the specified domain.
   3. Run this command using the credentials that are in the
      same AWS account as the target standard distribution or distribution tenant.**Request**

This example specifies a distribution tenant.

```
aws cloudfront list-domain-conflicts \
--domain `www.example.com` \
--domain-control-validation-resource "DistributionTenantId=`dt_2x9GhoK0TZRsohWzv1b9It8JABC`"
```

**Response**

For each domain name in the command’s output, you can see the
following:

    * The resource type that the domain is associated
     with
    * The resource ID
    * The AWS account ID that owns the resource

The resource ID and the account ID are partially hidden. This
allows you to identify the standard distribution or distribution tenant that belongs to your
account, and helps to protect the information of ones that you don’t
own.

```
{
    "DomainConflicts": [
        {
            "Domain": "www.example.com",
            "ResourceType": "distribution-tenant",
            "ResourceId": "***************ohWzv1b9It8JABC",
            "AccountId": "******112233"
        }
    ]
}
```

The response lists all the domain names that conflict or overlap
with the one that you specified.

###### Example

    * If you specify
     `tenant1.example.com`, the
     response includes tenant1.example.com and the overlapping
     wildcard alternate domain name (\*.example.com if it
     exists).
    * If you specify
     `*.tenant1.example.com`, the
     response includes \*.tenant1.example.com and any alternate
     domain names covered by that wildcard (for example,
     test.tenant1.example.com,
     dev.tenant1.example.com, and so on).

2. In the response, find the source standard distribution or distribution tenant for the alternate
   domain name that you're moving, and note the AWS account ID.
3. Compare the account ID of the _source_
   standard distribution or distribution tenant with the account ID where you created the
   _target_ standard distribution or distribution tenant in the [previous
   step](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md"). You can then determine whether the source and
   target are in the same AWS account. This helps you determine how
   to move the alternate domain name.

For more information, see the [list-domain-conflicts](../../../cli/latest/reference/cloudfront/list-domain-conflicts.md "../../../cli/latest/reference/cloudfront/list-domain-conflicts.md") command in the
_AWS Command Line Interface Reference_.

list-conflicting-aliases (standard distributions only)

###### Tip

You must have the `cloudfront:GetDistribution` and
`cloudfront:ListConflictingAliases` permissions on the
target standard distribution.

###### To use `list-conflicting-aliases` to find the source standard distribution

1. Use the `list-conflicting-aliases` command as shown in
   the following example.
   1. Replace `www.example.com` with
      the alternate domain name, and
      `EDFDVBD6EXAMPLE` with the ID of
      the target standard distribution [that
      you set up previously](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md").
   2. Run this command using credentials that are in the same
      AWS account as the target standard distribution.**Request**

This example specifies a standard distribution.

```
aws cloudfront list-conflicting-aliases \
--alias `www.example.com` \
--distribution-id `EDFDVBD6EXAMPLE`
```

**Response**

For each alternate domain name in the command’s output, you can
see the ID of the standard distribution that it’s associated with, and the
AWS account ID that owns the standard distribution. The standard distribution and account
IDs are partially hidden, which allows you to identify the
standard distributions and accounts that you own, and helps to protect the
information of ones that you don’t own.

```
{
    "ConflictingAliasesList": {
        "MaxItems": 100,
        "Quantity": 1,
        "Items": [
            {
                "Alias": "`www.example.com`",
                "DistributionId": "*******EXAMPLE",
                "AccountId": "******112233"
            }
        ]
    }
}
```

The response lists the alternate domain names that conflict or
overlap with the one that you specified.

###### Example

    * If you specify `www.example.com`,
     the response includes www.example.com and the overlapping
     wildcard alternate domain name (\*.example.com) if it
     exists.
    * If you specify `*.example.com`,
     the response includes \*.example.com and any alternate domain
     names covered by that wildcard (for example,
     www.example.com, test.example.com, dev.example.com, and so
     on).

2. Find the standard distribution for the alternate domain name that you're
   moving, and note the AWS account ID. Compare this account ID with
   the account ID where you created the target standard distribution in the [previous
   step](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md"). You can then determine whether these two standard distributions
   are in the same AWS account and how to move the alternate domain
   name.

For more information, see the [list-conflicting-aliases](../../../cli/latest/reference/cloudfront/list-conflicting-aliases.md "../../../cli/latest/reference/cloudfront/list-conflicting-aliases.md") command in
the _AWS Command Line Interface Reference_.

Next, see the following topic to move the alternate domain name.
