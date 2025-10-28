# Security Hub policy syntax and

examples

Security Hub policies follow a standardized JSON syntax that defines how Security Hub is enabled and
configured across your organization. Understanding the policy structure helps you create
effective policies for your security requirements.

## Considerations

Before creating Security Hub policies, understand these key points about policy
syntax:

- Both `enable_in_regions` and `disable_in_regions` lists
  are required in the policy, though they can be empty
- When processing effective policies, `disable_in_regions` takes
  precedence over `enable_in_regions`
- Child policies can modify parent policies using inheritance operators unless
  explicitly restricted
- The `ALL_SUPPORTED` designation includes both current and future
  regions
- Region names must be valid and available in Security Hub

## Basic policy structure

A Security Hub policy uses this basic structure:

```
{
  "securityhub": {
    "enable_in_regions": {
      "@@append": ["ALL_SUPPORTED"],
      "@@operators_allowed_for_child_policies": ["@@all"]
    },
    "disable_in_regions": {
      "@@append": [],
      "@@operators_allowed_for_child_policies": ["@@all"]
    }
  }
}
```

## Policy components

Security Hub policies contain these key components:

`securityhub`

The top-level container for policy settings

Required for all Security Hub policies

`enable_in_regions`

List of regions where Security Hub should be enabled

Can contain specific region names or `ALL_SUPPORTED`

Required field but can be empty

When using `ALL_SUPPORTED`, includes future regions

`disable_in_regions`

List of regions where Security Hub should be disabled

Can contain specific region names or `ALL_SUPPORTED`

Required field but can be empty

Takes precedence over `enable_in_regions` when regions appear
in both lists

Inheritance operators

@@assign - Overwrites inherited values

@@append - Adds new values to existing ones

@@remove - Removes specific values from inherited settings

## Security Hub policy examples

The following examples demonstrate common Security Hub policy configurations.

The example below enables Security Hub in all current and future regions. By using
`ALL_SUPPORTED` in the `enable_in_regions` list and leaving
`disable_in_regions` empty, this policy ensures comprehensive security
coverage as new regions become available.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      }
   }
}
```

This example disables Security Hub in all regions including any future regions since
`disable_in_regions` list takes precedence over
`enable_in_regions`.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2"
         ]
      },
      "disable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      }
   }
}
```

The following example demonstrates how child policies can modify parent policy
settings using inheritance operators. This approach allows for granular control while
maintaining the overall policy structure. The child policy adds a new region to
`enable_in_regions` and removes a region from
`disable_in_regions`.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@append":[
            "eu-central-1"
         ]
      },
      "disable_in_regions":{
         "@@remove":[
            "us-west-2"
         ]
      }
   }
}
```

This example shows how to enable Security Hub in multiple specific regions without using
`ALL_SUPPORTED`. This provides precise control over which regions have
Security Hub enabled, while leaving unspecified regions unmanaged by the policy.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      }
   }
}
```

The following example demonstrates how to handle regional compliance requirements by
enabling Security Hub in most regions while explicitly disabling it in specific locations. The
`disable_in_regions` list takes precedence, ensuring Security Hub remains
disabled in those regions regardless of other policy settings.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      },
      "disable_in_regions":{
         "@@assign":[
            "ap-east-1",
            "me-south-1"
         ]
      }
   }
}
```
