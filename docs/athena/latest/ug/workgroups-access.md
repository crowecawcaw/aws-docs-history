# Configure access to workgroups and tags

A workgroup is a resource managed by Athena. Therefore, if your workgroup policy uses
actions that take `workgroup` as an input, you must specify the workgroup's
ARN as follows, where `workgroup-name` is the name
of your workgroup:

```
"Resource": [arn:aws:athena:`region`:`AWSAcctID`:workgroup/`workgroup-name`]
```

For example, for a workgroup named `test_workgroup` in the
`us-west-2` region for Amazon Web Services account `123456789012`,
specify the workgroup as a resource using the following ARN:

```
"Resource":["arn:aws:athena:us-east-2:123456789012:workgroup/test_workgroup"]
```

To access trusted identity propagation (TIP) enabled workgroups, IAM Identity Center users must be
assigned to the `IdentityCenterApplicationArn` that is returned by the
response of the Athena [GetWorkGroup](../APIReference/API_GetWorkGroup.md "../APIReference/API_GetWorkGroup.md") API
action.

- For a list of workgroup policies, see [Example workgroup policies](example-policies-workgroup.md "example-policies-workgroup.md").
- For a list of tag-based policies for workgroups, see [Use tag-based IAM access control
  policies](tags-access-control.md "tags-access-control.md").
- For more information about creating IAM policies for workgroups, see [Use IAM policies to control workgroup
  access](workgroups-iam-policy.md "workgroups-iam-policy.md").
- For a complete list of Amazon Athena actions, see the API action names in the
  [Amazon Athena API Reference](../APIReference.md "../APIReference.md").
- For more information about IAM policies, see [Creating policies with the visual editor](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-visual-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-visual-editor") in the
  _IAM User Guide_.
  Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.
