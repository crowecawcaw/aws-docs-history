# Register a third-party private

extension in your account

This topic covers the steps to register a third-party private extension that's
shared with you so it's available for use in your account.

###### Note

Before you continue, confirm that you have the required [IAM
permissions](registry-private.md#registry-register-permissions "registry-private.md#registry-register-permissions") to register a private
extension.

###### To register a private extension that's shared with you (AWS CLI)

1. Locate the Amazon S3 bucket that contains the project package for the private
   extension you want to register in your account.
2. Use the [register-type](../../../cli/latest/reference/cloudformation/register-type.md "../../../cli/latest/reference/cloudformation/register-type.md") command to register the
   private extension in your account.

For example, the following command registers the
`My::Resource::Example` resource type in the specified
AWS account.

```
aws cloudformation register-type --type `RESOURCE` \
  --type-name `My::Resource::Example` \
  --schema-handler-package `[s3 object path]` --region `us-west-2`
```

`RegisterType` is an asynchronous operation, and returns a
registration token you can use to track the progress of your registration
request.

```
{
    "RegistrationToken": "f5525280-104e-4d35-bef5-8f1fexample"
}
```

If your extension calls AWS APIs as part of its functionality, you must
create an IAM execution role that includes the necessary permissions to
call those AWS APIs, and provision that execution role in your account.
You can then specify this execution role using the
`--execution-role-arn` option. CloudFormation then assumes that
execution role to provide your resource type with the appropriate
credentials.

```
--execution-role-arn `arn:aws:iam::123456789012:role/MyIAMRole`
```

3. (Optional) Use the registration token with the [describe-type-registration](../../../cli/latest/reference/cloudformation/describe-type-registration.md "../../../cli/latest/reference/cloudformation/describe-type-registration.md") command to track
   the progress of your registration request.

When CloudFormation completes the registration request, it sets the progress
status of the request to `COMPLETE`.

The following example uses the registration token returned by the
`describe-type-registration` command above to return
registration status information.

```
aws cloudformation describe-type-registration \
  --registration-token `f5525280-104e-4d35-bef5-8f1fexample` \
  --region `us-west-2`
```

The command returns the following output.

```
{
    "ProgressStatus": "COMPLETE",
    "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Resource-Example",
    "Description": "Deployment is currently in DEPLOY_STAGE of status COMPLETED; ",
    "TypeVersionArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Resource-Example/00000001"
}
```

###### Important

If the extension you are registering is a Hook, this next step is required.
You must specify `ENABLED` for the `HookInvocationStatus`
property. This operation enables the Hook’s properties that are defined in the
Hook’s schema `properties` section. For more information, see [Hook configuration schema syntax reference](../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md "../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md") in the _AWS CloudFormation
Hooks User Guide_.

###### To specify the configuration data for a Hook (AWS CLI)

1. Get the ARN for your Hook and save it. You can get the ARN of a Hook using
   the AWS Management Console or AWS CLI. For more information see [View the available and activated extensions in the
   CloudFormation registry](registry-view.md "registry-view.md").

```
export HOOK_TYPE_ARN="`arn:aws:cloudformation:us-west-2:123456789012:type/hook/Organization-Service-Hook/`"
```

2. Use the [set-type-configuration](../../../cli/latest/reference/cloudformation/set-type-configuration.md "../../../cli/latest/reference/cloudformation/set-type-configuration.md") command to specify
   the configuration data. The JSON you pass for `--configuration`
   must validate against the Hook's configuration schema. To activate the Hook,
   you must set the `HookInvocationStatus` property to
   `ENABLED` in the `HookConfiguration`
   section.

```
aws cloudformation set-type-configuration \
  --configuration `"{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "ENABLED", "FailureMode": "FAIL", "Properties":{}}}}"` \
  --type-arn $`HOOK_TYPE_ARN` --region `us-west-2`
```

For more information, see [Hook configuration schema syntax reference](../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md "../../../cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.md") in the
_AWS CloudFormation Hooks User Guide_.
