# Use third-party public extensions from the CloudFormation
 registry

To use a third-party public extension in your template, you must first
 *activate* the extension for the account and Region where you
 want to use it. Activating an extension makes it usable in stack operations in the
 account and Region where it's activated. 

When you activate a third-party public extension, CloudFormation creates an entry in your
 account's extension registry for the activated extension as a private extension. This
 allows you to set any configuration properties the extension includes. Configuration
 properties define how the extension is configured for a given AWS account and
 Region.

In addition to setting configuration properties, you can also customize the extension
 in the following ways:


* Specify the execution role CloudFormation uses to activate the extension, in
 addition to configure logging for the extension.
* Specify whether the extension is automatically updated when a new minor or
 patch version becomes available.
* Specify an alias to use rather than the third-party public extension name.
 This can help avoid naming collisions between third-party extensions.
###### Topics

* [Configure an execution role
 with IAM permissions and a trust policy for public extension access](#registry-public-enable-execution-role "#registry-public-enable-execution-role")
* [Automatically use new versions of
 extensions](#registry-public-enable-auto "#registry-public-enable-auto")
* [Use aliases to refer to
 extensions](#registry-public-enable-alias "#registry-public-enable-alias")
* [Commonly used
 AWS CLI commands for working with public extensions](#registry-commonly-used-commands-public-extensions "#registry-commonly-used-commands-public-extensions")
* [Activate a third-party public
 extension in your account](registry-public-activate-extension.md "registry-public-activate-extension.md")
* [Update a public
 third-party extension in your account](registry-public-update-extension-console.md "registry-public-update-extension-console.md")
* [Deactivate third-party public
 extensions in your account](registry-public-deactivate-extension.md "registry-public-deactivate-extension.md")

## Configure an execution role
 with IAM permissions and a trust policy for public extension access


When you activate a public extension from the CloudFormation registry, you can provide
 an execution role that gives CloudFormation the necessary permissions to invoke that
 extension in your AWS account and Region.


The permissions required for the execution role are defined in the handler section
 of the extension schema. You must create an IAM policy that grants the specific
 permissions needed by the extension and attach it to the execution role. 


In addition to the permissions policy, the execution role must also have a trust
 policy that allows CloudFormation to assume the role. Follow the guidance at [Create a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html") in the
 *IAM User Guide* to create a role with a custom trust
 policy.


### Trust
 relationship


The following shows example trust policies you can use.


You can optionally restrict the scope of the permission for cross-service
 confused deputy prevention by using one or more global condition context keys
 with the `Condition` field. For more information, see [Cross-service confused deputy
 prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").



* Set the `aws:SourceAccount` value to your account
 ID.
* Set the `aws:SourceArn` value to your extension's
 ARN.

###### Example trust policy 1


The following is an example IAM role trust policy for a resource type
 extension.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "resources.cloudformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:cloudformation:us-west-2:`123456789012`:type/resource/Organization-Service-Resource"
 }
 }
 }
 ]
}`

```





###### Example trust policy 2


The following is an example IAM role trust policy for a Hook
 extension.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "resources.cloudformation.amazonaws.com",
 "hooks.cloudformation.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:cloudformation:us-west-2:`123456789012`:type/hook/Organization-Service-Hook"
 }
 }
 }
 ]
}`

```





## Automatically use new versions of
 extensions


When you activate an extension, you can also specify the extension type to use the
 latest minor version. Your extension type updates the minor version, whenever the
 publisher releases a new version on your activated extension.


For example, the next time you perform a stack operation, such as creating or
 updating a stack, using a template that includes that extension, CloudFormation uses the
 new minor version.


Updating to a new extension version, either automatically or manually and doesn't
 affect any extension instances already provisioned in stacks.


CloudFormation treats major version updates of extensions as potentially containing
 breaking changes, and so requires you to manually update to a new major version of
 an extension.


Extensions published by AWS are activated by default for all accounts and
 Regions where they're available, and always use the latest version available in each
 AWS Region.


###### Important

Because you control if and when extensions gets updated to the latest version
 in your account, you could end up with different versions of the same extension
 deployed in different accounts and Regions.

This might potentially lead to unexpected results when using the same
 template, containing that extension, across those accounts and Regions.


## Use aliases to refer to
 extensions


You can't activate more than one extension with a given name in a given
 AWS account and Region. Because different publishers may offer public extensions
 with the same extension name, CloudFormation lets you specify an alias for any
 third-party public extension you activate.


If you specify an alias for the extension, CloudFormation treats the alias as the
 extension type name within the account and Region. You must use the alias to refer
 to the extension in your templates, API calls, and CloudFormation console.


Extension aliases must be unique within a given account and Region. You can
 activate the same public resource multiple times in the same account and Region,
 using different type name aliases.


###### Important

While extension aliases are only required to be unique in a given account and
 Region, we strongly suggest that users *not* assign the same
 alias to different third-party public extensions across accounts and Regions.
 Doing so could lead to unexpected results when using a template that contains
 the extension alias across multiple accounts or Regions.


## Commonly used
 AWS CLI commands for working with public extensions


The commonly used commands for working with public extensions include: 



* [activate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html") to activate a public
 third-party module or resource type in your account.
* [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html") to specify the
 configuration data for an extension in your account and to disable and
 enable Hooks.
* [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html") to list the extensions in your
 account.
* [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html") to return detailed information
 about a specific extension or specific extension version, including current
 configuration data.
* [set-type-default-version](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html") to specify which
 version of an extension is the default version.
* [deactivate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html") to deactivate a public
 third-party module or resource type that was previously activated in your
 account.
