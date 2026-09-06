

# Deactivate third-party public extensions in your account
<a name="registry-public-deactivate-extension"></a>

When you no longer need an activated third-party public extension, use the following procedures to deactivate it in your account.

**Topics**
+ [Deactivate a public extension in your account (console)](#registry-public-deactivate-extension-console)
+ [Deactivate a public extension in your account (AWS CLI)](#registry-public-deactivate-extension-cli)
+ [Disable a Hook in your account (AWS CLI)](#registry-public-deactivate-extension-cli-hook)

## Deactivate a public extension in your account (console)
<a name="registry-public-deactivate-extension-console"></a>

**To deactivate a public extension in your account**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose your AWS Region.

1. From the navigation pane, under **Registry**, choose **Activated extensions**.

1. Find the extension you want to deactivate and select it. For more information, see [View the available and activated extensions in the CloudFormation registry](registry-view.md).

1. From the **Actions** menu, choose **Deactivate**.

1. Choose **Deactivate**.

## Deactivate a public extension in your account (AWS CLI)
<a name="registry-public-deactivate-extension-cli"></a>

Use the following [deactivate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) command.

```
aws cloudformation deactivate-type --type {{MODULE}} \
  --type-name {{Example::Test::Type::MODULE}} \
  --region {{us-west-2}}
```

## Disable a Hook in your account (AWS CLI)
<a name="registry-public-deactivate-extension-cli-hook"></a>

Disabling a Hook prevents the Hook from running in your AWS account without removing it.

Use the [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) command and specify `HookInvocationStatus` as `DISABLED` to disable a Hook.

The following example specifies the AWS Region and the Amazon Resource Name (ARN) of the Hook that's being disabled.

```
aws cloudformation set-type-configuration \
  --configuration {{"{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "DISABLED", "FailureMode": "FAIL", "Properties":{}}}}"}} \
  --type-arn {{"arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook"}} --region {{us-west-2}}
```

For more information, see [Disable and enable CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-disable-enable.html) in the *CloudFormation Hooks User Guide*.