# Switching to the extended registry policy scope

###### Important

For new users, your registries are automatically configured to use the `V2` registry policy upon creation. There is no action for you to take.
Amazon ECR doesn't recommend reverting to the previous registry policy `V1`
.

You can use the console or the CLI to view or change your registry policy
scope.

AWS Management Console
Use the following steps to view your account settings. To view or
update the registry policy scope, see the CLI procedure on this
page.

###### Turn on the enhanced registry policy for your private registry

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region.
3. In the navigation pane, choose **Private
   registry**, **Feature &
   Settings**, and then choose **Permissions**
   .
4. On the **Permissions** page, for **Registry
   policy** view your policy JSON. If you have the V1
   policy, a banner displays with instructions to update to V2.
   Choose **Enable**.

A banner displays indicating that the registry policy scope
has been updated to V2. 5. You can also optionally configure permissions with the CLI.
For more information, see [Private registry settings in Amazon ECR](registry-settings.md "registry-settings.md").

###### Note

To view or update the registry policy scope, see the CLI
procedure on this page.

AWS CLI
Amazon ECR generates the V2 registry policy. Use the following steps to
view or update the registry policy scope. You cannot view or change the
registry policy scope in the console

- To retrieve the registry policy you are currently
  using.

```
`aws ecr get-account-setting --name REGISTRY_POLICY_SCOPE`
```

The parameter name is a required field. If you don't provide
the name you will receive the following error:

```
 `aws: error: the following arguments are required: --name`
```

View the output for your registry policy command. In the
following example output, the registry policy version is
V1.

```
{
    "name": "REGISTRY_POLICY_SCOPE",
    "value": "V1"
}
```

You can change your registry policy version from `V1`
to `V2`. V1 is not the recommended registry policy
scope.

```
`aws ecr put-account-setting --name REGISTRY_POLICY_SCOPE --value `value``
```

For example, use the following command to update to V2.

```
`aws ecr put-account-setting --name REGISTRY_POLICY_SCOPE --value V2`
```

View the output for your registry policy command. In the
following example output, the registry policy version was
updated to V2.

```
{
    "name": "REGISTRY_POLICY_SCOPE",
    "value": "V2"
}
```
