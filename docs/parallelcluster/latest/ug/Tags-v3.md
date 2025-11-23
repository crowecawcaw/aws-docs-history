# `Tags` section

**(Optional), Array** Defines the tags that are used by CloudFormation and
propagated to all the cluster resources. For more information, see [CloudFormation resource
tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md") in the _AWS CloudFormation User Guide_.

```
Tags:
  - Key: `string`
    Value: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `Tags` properties

`Key` (**Required**,
`String`)

Defines the name of the tag.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Value` (**Required**,
`String`)

Defines the value of the tag.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")
