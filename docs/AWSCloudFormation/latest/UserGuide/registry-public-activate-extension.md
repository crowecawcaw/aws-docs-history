# Activate a third-party public

extension in your account

The following topic shows you how to activate a third-party public extension in
your account, which makes it usable in the account and Region it was activated
in.

###### Note

Before you continue, confirm that you have created the [IAM
role](registry-public.md#registry-public-enable-execution-role "registry-public.md#registry-public-enable-execution-role") that you'll
use with this extension.

###### Topics

- [Activate a public
  extension (console)](#registry-public-activate-extension-console "#registry-public-activate-extension-console")
- [Activate a public
  extension (AWS CLI)](#registry-public-activate-extension-cli "#registry-public-activate-extension-cli")

## Activate a public

extension (console)

Follow the steps in this section to use the console to:

- Activate a third-party public extension
- Specify additional extension configuration data for your
  account

###### To activate a public extension for use in your account

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your
   AWS Region.
3. From the navigation pane, under **Registry**, choose
   **Public extensions**.
4. Use the **Filter** to choose the extension type, and
   choose **Third party**. (Extensions published by AWS
   are activated by default.)
5. Choose the extension, then choose
   **Activate**.

If multiple versions of an extension are available, you can use the
**Version** menu to choose the version of the
extension you want to activate. The default is the most current
version. 6. For **Extension name**, you can either keep
**Use default** selected, or choose
**Override default**, and then enter the extension
type alias you want to use with this extension. The alias must follow
the recommended format for the extension type. For more information, see
[Use aliases to refer to
extensions](registry-public.md#registry-public-enable-alias "registry-public.md#registry-public-enable-alias"). 7. If the extension you are activating is a Hook or resource type, for
**Execution role ARN**, specify the IAM role for
CloudFormation to assume when invoking the extension. For more information,
see [Configure an execution role
with IAM permissions and a trust policy for public extension access](registry-public.md#registry-public-enable-execution-role "registry-public.md#registry-public-enable-execution-role"). 8. For **Logging config**, specify logging configuration
information for an extension, if desired. For example:

```
{
    "logRoleArn": "arn:aws:iam::`account`:role/`rolename`",
    "logGroupName": "`log-group-name`"
}
```

Logging configuration information isn't required but it's recommended
for debugging purposes. To use logging configuration with Hooks, add the
same trust policy as the execution role specified, so that the log role
can write logs to your log group.

`logRoleArn` and `logGroupName` key names are
case-sensitive. 9. For **Versioning**, **Automatic
updates**, choose how to receive updates.

    * **On** – Automatically updates to the
     latest minor version. Major versions are updated
     manually.
    * **Off** – Never automatically update
     to the latest version. All versions are updated manually.

For more information, see [Automatically use new versions of
extensions](registry-public.md#registry-public-enable-auto "registry-public.md#registry-public-enable-auto").

If the extension requires additional configuration, you have the option to
specify the configuration data now, or after the extension has been
activated.

###### Important

If the extension you are activating is a Hook, this step is required. You
must specify `ENABLED` for the `HookInvocationStatus`
property. This operation enables the Hook’s properties that are defined in
the Hook’s schema `properties` section. For more information, see
[Hook configuration schema syntax reference](../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md "../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md") in the
_AWS CloudFormation Hooks User Guide_.

###### To specify the configuration data

1. For **Configuration**, choose **Configure
   now**, and then choose **Activate
   extension**.

CloudFormation displays the **Configure extension** page.
To view the current configuration schema for the extension, make sure
**View configuration schema** is activated. 2. In the **Configuration JSON** text box, enter a JSON
string that represents the configuration data you want to specify for
this extension. The JSON you specify must validate against the
extension's configuration schema. 3. Choose **Configure extension**.

If you prefer to configure the extension after activation, you can skip this
step and provide the configuration data at a later time.

1. For **Configuration**, choose **Configure
   later**, and then choose **Activate
   extension**.
2. After the extension is activated, you can configure it by navigating
   to the extension from the activated extensions page and providing the
   configuration data.

## Activate a public

extension (AWS CLI)

Follow the steps in this section to use the AWS CLI to:

- Activate a third-party public extension
- Specify additional extension configuration data for your
  account

### Activate public

Hooks

By activating Hooks in your account, you are authorizing a Hook to use
defined permissions from your AWS account. CloudFormation removes non-required
permissions before passing your permissions to the Hook. CloudFormation
recommends customers or Hook users to review the Hook permissions and be
aware of what permissions the Hooks are allowed to before activating Hooks
in your account.

###### To activate a public Hook for use in your account (AWS CLI)

1. Get the ARN for your Hook and save it. You can get the ARN of a
   Hook using the AWS Management Console or AWS CLI. For more information see [View the available and activated extensions in the
   CloudFormation registry](registry-view.md "registry-view.md").

```
export HOOK_TYPE_ARN="`arn:aws:cloudformation:us-west-2:123456789012:type/hook/Organization-Service-Hook/`"
```

2. Use the [set-type-configuration](../../../cli/latest/reference/cloudformation/set-type-configuration.md "../../../cli/latest/reference/cloudformation/set-type-configuration.md") command to
   specify the configuration data. The JSON you pass for
   `--configuration` must validate against the Hook's
   configuration schema. To activate the Hook for all stack operations,
   you must set the `HookInvocationStatus` property to
   `ENABLED` in the `HookConfiguration`
   section.

```
aws cloudformation set-type-configuration \
  --configuration `"{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "ENABLED", "FailureMode": "FAIL", "Properties":{}}}}"` \
  --type-arn $`HOOK_TYPE_ARN` --region `us-west-2`
```

For more information on the `HookConfiguration`
configuration options, see [Hook configuration schema syntax reference](../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md "../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md") in the
_AWS CloudFormation Hooks User Guide_.

### Activate public

modules and resource types

###### To

activate a public extension for use in your account (AWS CLI)

- Use the [activate-type](../../../cli/latest/reference/cloudformation/activate-type.md "../../../cli/latest/reference/cloudformation/activate-type.md") command to activate
  the extension, and specify whether to auto update the extension
  whenever a new minor version of the extension is published.

The example below specifies the public Amazon Resource Name (ARN)
of a public extension to activate for this account. In addition, it
specifies that CloudFormation updates the extension whenever a new minor
version is published.

```
aws cloudformation activate-type \
  --public-type-arn `public_extension_ARN` \
  --execution-role-arn `arn:aws:iam::123456789012:role/my-execution-role` \
  --auto-update `true` --region `us-west-2`
```

This command returns an ARN of the activated extension.

```
{
    "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Resource-Example"
}
```

### Update the version

of a public extension (AWS CLI)

Use [activate-type](../../../cli/latest/reference/cloudformation/activate-type.md "../../../cli/latest/reference/cloudformation/activate-type.md") to activate the extension
again.

Use the `--version-bump` option to specify whether to update
the extension to the newest `MAJOR` version or newest
`MINOR` version.

```
aws cloudformation activate-type --type `RESOURCE` \
  --type-name `Example::Test::1234567890abcdef0` \
  --type-name-alias `Example::Test::Alias` \
  --version-bump `MAJOR` --region `us-west-2`
```
