# Remove third-party private
 extensions from your account

To remove a third-party private extension or extension version, use the [deregister-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html") command.

You can deregister a specific extension version, or the extension as a whole. To
 deregister an extension, you must individually deregister all registered versions of
 that extension. If an extension has only a single registered version, deregistering
 that version results in the extension itself being deregistered. You can't
 deregister the default version of an extension, unless it's the only registered
 version of that extension, in which case the extension itself is deregistered as
 well. 

###### Note

Before you deregister an extension, it's a good idea to use the [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html") command to confirm the extension exists. Then, use
 the [list-stacks](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stacks.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stacks.html") and [get-template](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/get-template.html") commands to check if any stacks are using the
 extension before you deregister it.


## Example deregister extension
 commands


This sections provides examples that show the different ways to deregister
 private extensions.


###### Deregister by type name


Use the [deregister-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html") command with
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
 [set-type-default-version](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html") command.


###### Deregister by ARN


Use the `--arn` option and specify your extension's ARN to
 deregister it.



```
aws cloudformation deregister-type \
  --arn `arn:aws:cloudformation:us-west-2:123456789012:type/resource/Organization-Service-Resource`
```
