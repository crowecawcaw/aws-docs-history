# Deactivate third-party public
 extensions in your account

When you no longer need an activated third-party public extension, use the
 following procedures to deactivate it in your account.

###### Topics

* [Deactivate a
 public extension in your account (console)](#registry-public-deactivate-extension-console "#registry-public-deactivate-extension-console")
* [Deactivate a public
 extension in your account (AWS CLI)](#registry-public-deactivate-extension-cli "#registry-public-deactivate-extension-cli")
* [Disable a Hook
 in your account (AWS CLI)](#registry-public-deactivate-extension-cli-hook "#registry-public-deactivate-extension-cli-hook")

## Deactivate a
 public extension in your account (console)


###### To deactivate a public extension in your account

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your
 AWS Region.
3. From the navigation pane, under **Registry**, choose
 **Activated extensions**.
4. Find the extension you want to deactivate and select it. For more
 information, see [View the available and activated extensions in the
 CloudFormation registry](registry-view.md "registry-view.md").
5. From the **Actions** menu, choose
 **Deactivate**.
6. Choose **Deactivate**.

## Deactivate a public
 extension in your account (AWS CLI)


Use the following [deactivate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html") command.



```
aws cloudformation deactivate-type --type `MODULE` \
  --type-name `Example::Test::Type::MODULE` \
  --region `us-west-2`
```

## Disable a Hook
 in your account (AWS CLI)


Disabling a Hook prevents the Hook from running in your AWS account without
 removing it.


Use the [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html") command and specify
 `HookInvocationStatus` as `DISABLED` to disable a
 Hook.


The following example specifies the AWS Region and the Amazon Resource Name
 (ARN) of the Hook that's being disabled.



```
aws cloudformation set-type-configuration \
  --configuration `"{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "DISABLED", "FailureMode": "FAIL", "Properties":{}}}}"` \
  --type-arn `"arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook"` --region `us-west-2`
```

For more information, see [Disable and enable AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-disable-enable.html "https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-disable-enable.html") in the *AWS CloudFormation Hooks User
 Guide*.
