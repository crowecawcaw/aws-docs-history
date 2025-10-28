# Remove third-party private

extensions from your account

To remove a third-party private extension or extension version, use the [deregister-type](../../../cli/latest/reference/cloudformation/deregister-type.md "../../../cli/latest/reference/cloudformation/deregister-type.md") command.

You can deregister a specific extension version, or the extension as a whole. To
deregister an extension, you must individually deregister all registered versions of
that extension. If an extension has only a single registered version, deregistering
that version results in the extension itself being deregistered. You can't
deregister the default version of an extension, unless it's the only registered
version of that extension, in which case the extension itself is deregistered as
well.

###### Warning

Deregistering a private extension can't be undone. This action will:

- Make the extension unusable in all CloudFormation operations.
- Cause failures in future stack updates that use this extension (for
  modules and resource types). Although you can reregister the extension
  privately later, this could cause failures if CloudFormation relies on an
  earlier version.
  Before proceeding, use the [list-stacks](../../../cli/latest/reference/cloudformation/list-stacks.md "../../../cli/latest/reference/cloudformation/list-stacks.md") and [get-template](../../../cli/latest/reference/cloudformation/get-template.md "../../../cli/latest/reference/cloudformation/get-template.md") commands to verify that no active stacks are using
  this extension.

## Example deregister extension

commands

This section provides examples that show the different ways to deregister
private extensions.

###### Deregister by type name

Use the [deregister-type](../../../cli/latest/reference/cloudformation/deregister-type.md "../../../cli/latest/reference/cloudformation/deregister-type.md") command with
`--type` and `--type-name` options to deregister
your extension.

```
aws cloudformation deregister-type \
  --type `MODULE` \
  --type-name `My::S3::SampleBucket::MODULE`
```

###### Deregister by type name and version

To deregister a specific version of your extension, specify the
`--version-id` option in the command.

```
aws cloudformation deregister-type \
  --type `MODULE` \
  --type-name `My::S3::SampleBucket::MODULE` \
  --version-id `00000001`
```

###### Tip

To set a different version of the extension as default first, use the
[set-type-default-version](../../../cli/latest/reference/cloudformation/set-type-default-version.md "../../../cli/latest/reference/cloudformation/set-type-default-version.md") command.

###### Deregister by ARN

Use the `--arn` option and specify your extension's ARN to
deregister it.

```
aws cloudformation deregister-type \
  --arn `arn:aws:cloudformation:us-west-2:123456789012:type/resource/Organization-Service-Resource`
```
