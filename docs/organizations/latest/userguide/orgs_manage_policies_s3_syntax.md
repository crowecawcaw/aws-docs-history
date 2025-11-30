# Amazon S3 policy syntax and

examples

An Amazon S3 policy is a plaintext file that is structured according to the rules of [JSON](http://json.org "http://json.org"). The syntax for Amazon S3 policies follows the syntax for all management policy types. For more information, see [Understanding management policy
inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md"). This topic focuses on applying that general syntax to the specific requirements of the Amazon S3 policies and the Block Public Access settings they help manage.

The following Amazon S3 policy example shows the basic policy syntax:

```
{
    "s3_attributes": {
        "public_access_block_configuration": {
            "@@assign": "all"
        }
    }
}
```

## The Amazon S3 policy syntax includes the following elements

`s3_attributes`

The top-level key for Amazon S3 policy configuration.

`public_access_block_configuration`

Defines the Block Public Access behavior for the organization.

`@@assign`

The assignment operator that accepts one of two values:

- `"all"` - Enables all four Amazon S3 Block Public Access settings at the organization level
- `"none"` - Disables organization-level control, allowing individual accounts to manage their own Block Public Access settings

Amazon S3 Block Public Access has four settings that control public access:

1. **BlockPublicAcls** - Amazon S3 will block public access permissions applied to newly added buckets or objects, and prevent the creation of new public access control lists (ACLs) for existing buckets and objects. This setting doesn't change any existing permissions that allow public access to Amazon S3 resources using ACLs.
2. **BlockPublicPolicy** - Amazon S3 will block new bucket and access point policies that grant public access to buckets and objects. This setting doesn't change any existing policies that allow public access to Amazon S3 resources.
3. **IgnorePublicAcls** - Amazon S3 will ignore all ACLs that grant public access to buckets and objects.
4. **RestrictPublicBuckets** - Amazon S3 will ignore public and cross-account access for buckets or access points with policies that grant public access to buckets and objects.

When you set `@@assign` to `"all"`, all four settings are consolidated and enabled at the organization level, providing comprehensive protection against public access across all accounts in your organization.
