# AWS IoT SiteWise identity-based

policies

IAM policies let you control who can do what in AWS IoT SiteWise. You can decide what actions
are allowed or not and set specific conditions for these actions. For example, you can make
rules about who can see or change information in AWS IoT SiteWise. AWS IoT SiteWise supports specific actions,
resources, and condition keys. To learn about all of the elements that you use in a JSON
policy, see [IAM JSON policy
elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

## Policy

actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS IoT SiteWise use the following prefix before the action:
`iotsitewise:`. For example, to grant someone permission to upload
asset property data to AWS IoT SiteWise with the `BatchPutAssetPropertyValue` API
operation, you include the `iotsitewise:BatchPutAssetPropertyValue`
action in their policy. Policy statements must include either an `Action` or
`NotAction` element. AWS IoT SiteWise defines its own set of actions that describe
tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": [
  "iotsitewise:`action1`",
  "iotsitewise:`action2`"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action.

```
`"Action": "iotsitewise:Describe*"`
```

To see a list of AWS IoT SiteWise actions, see [Actions defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions") in the
_IAM User Guide_.

### BatchPutAssetPropertyValue authorization

AWS IoT SiteWise authorizes access to the [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") action in an unusual way. For
most actions, when you allow or deny access, that action returns an error if permissions
aren't granted. With `BatchPutAssetPropertyValue`, you can send multiple data
entries to different assets and asset properties in a single API request. AWS IoT SiteWise
authorizes each data entry independently. For any individual entry that fails
authorization in the request, AWS IoT SiteWise includes an `AccessDeniedException` in
the returned list of errors. AWS IoT SiteWise receives the data for any entry that authorizes and
succeeds, even if another entry in the same request fails.

###### Important

Before you ingest data to a data stream, do the following:

- Authorize the `time-series` resource if you use a property alias to
  identify the data stream.
- Authorize the `asset` resource if you use an asset ID to identify
  the asset that contains the associated asset property.

## Policy

resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Each IAM policy statement applies to the resources that you specify using their
ARNs. An ARN has the following general syntax.

```
arn:${Partition}:${Service}:${Region}:${Account}:${ResourceType}/${ResourcePath}
```

For more information about the format of ARNs, see [Identify AWS resources with Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md").

For example, to specify the asset with ID `a1b2c3d4-5678-90ab-cdef-22222EXAMPLE` in your statement, use
the following ARN.;

```
"Resource": "arn:aws:iotsitewise:`region`:`123456789012`:asset/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE"
```

To specify all data streams that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:iotsitewise:`region`:`123456789012`:time-series/*"
```

To specify all assets that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:iotsitewise:`region`:`123456789012`:asset/*"
```

Some AWS IoT SiteWise actions, such as those for creating resources, can't be performed on a
specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
  "`resource1`",
  "`resource2`"
]
```

To see a list of AWS IoT SiteWise resource types and their ARNs, see [Resource types defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-resources-for-iam-policies")
in the _IAM User Guide_. To learn with which actions you can specify
the ARN of each resource, see [Actions defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions").

## Policy

condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

###### Important

Many condition keys are specific to a resource, and some API actions use multiple
resources. If you write a policy statement with a condition key, use the
`Resource` element of the statement to specify the resource to which the
condition key applies. If you don't do so, the policy might prevent users from
performing the action at all, because the condition check fails for the resources to
which the condition key doesn't apply. If you don't want to specify a resource, or if
you've written the `Action` element of your policy to include multiple API
actions, then you must use the `...IfExists` condition type to ensure that
the condition key is ignored for resources that don't use it. For more information, see
[...IfExists conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IfExists "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IfExists") in the _IAM User Guide_.

AWS IoT SiteWise defines its own set of condition keys and also supports using some global
condition keys. To see all AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

| AWS IoT SiteWise condition keys             | Condition key                                                                                                                                                                                                                                                                                             | Description  | Types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iotsitewise:isAssociatedWithAssetProperty` | Whether data streams are associated with an asset property. Use this condition key to define permissions based on the existence of an associated asset property for data streams. Example value: `true`                                                                                                   | String       |
| `iotsitewise:assetHierarchyPath`            | The asset's hierarchy path, which is a string of asset IDs each separated by a forward slash. Use this condition key to define permissions based on a subset of your hierarchy of all assets in your account. Example value: `/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE/a1b2c3d4-5678-90ab-cdef-66666EXAMPLE` | String       |
| `iotsitewise:propertyId`                    | The ID of an asset property. Use this condition key to define permissions based on a specified property of an asset model. This condition key applies to all assets of that model. Example value: `a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`                                                                  | String       |
| `iotsitewise:childAssetId`                  | The ID of an asset being associated as a child to another asset. Use this condition key to define permissions based on child assets. To define permissions based on parent assets, use the resource section of a policy statement. Example value: `a1b2c3d4-5678-90ab-cdef-66666EXAMPLE`                  | String       |
| `iotsitewise:iam`                           | The ARN of an IAM identity when listing access policies. Use this condition key to define access policy permissions for an IAM identity. Example value: `arn:aws:iam::123456789012:user/JohnDoe`                                                                                                          | String, Null |
| `iotsitewise:propertyAlias`                 | The alias that identifies an asset property or data stream. Use this condition key to define permissions based on the alias.                                                                                                                                                                              | String       |
| `iotsitewise:user`                          | The ID of an IAM Identity Center user when listing access policies. Use this condition key to define access policy permissions for an IAM Identity Center user. Example value: `a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE`                                                                          | String, Null |
| `iotsitewise:group`                         | The ID of an IAM Identity Center group when listing access policies. Use this condition key to define access policy permissions for an IAM Identity Center group. Example value: `a1b2c3d4e5-a1b2c3d4-5678-90ab-cdef-bbbbbEXAMPLE`                                                                        | String, Null |
| `iotsitewise:portal`                        | The ID of a portal in an access policy. Use this condition key to define access policy permissions based on a portal. Example value: `a1b2c3d4-5678-90ab-cdef-77777EXAMPLE`                                                                                                                               | String, Null |
| `iotsitewise:project`                       | The ID of a project in an access policy, or the ID of a project for a dashboard. Use this condition key to define dashboard or access policy permissions based on a project. Example value: `a1b2c3d4-5678-90ab-cdef-88888EXAMPLE`                                                                        | String, Null | To learn with which actions and resources you can use a condition key, see [Actions defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions"). ## Examples To view examples of AWS IoT SiteWise identity-based policies, see [AWS IoT SiteWise identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). |
