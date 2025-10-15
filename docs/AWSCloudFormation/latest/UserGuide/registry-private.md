# Use third-party private extensions that have been
 shared with you

To use third-party private extensions that have been shared with you, you must first
 *register* them with CloudFormation, in the accounts and Regions
 where you want to use them. Registering the extension uploads a copy of it to the
 CloudFormation registry in your account, and activates it. Once you're registered a private
 extension, it will appear in the CloudFormation registry for that AWS account and Region,
 and you can use it in your stack templates.

###### Topics

* [IAM permissions for registering a
 third-party private extension](#registry-register-permissions "#registry-register-permissions")
* [Commonly used
 AWS CLI commands for working with private extensions](#registry-commonly-used-commands-private-extensions "#registry-commonly-used-commands-private-extensions")
* [Register a third-party private
 extension in your account](registry-register-private-extension.md "registry-register-private-extension.md")
* [Remove third-party private
 extensions from your account](registry-private-deregister-extension.md "registry-private-deregister-extension.md")

## IAM permissions for registering a
 third-party private extension


As part of registering a private extension, you might specify an Amazon S3 bucket that
 contains the extension project package. This package contains any source files
 necessary for the extension you want to register. The user registering the extension
 must be able to access the project package in that Amazon S3 bucket. To do so, the user
 must have [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") permissions for the extension
 package.


This is true whether you're either using the [register-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html") command of the AWS CLI, or the [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html") command of the CloudFormation CLI.


For more information, see [Actions,
 Resources, and Condition Keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html") in the
 *Service Authorization Reference*.


## Commonly used
 AWS CLI commands for working with private extensions


The commonly used commands for working with private extensions include: 



* [register-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html") to register a private
 extension in your account.
* [describe-type-registration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type-registration.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type-registration.html") to return the
 current status of a registration request.
* [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html") to list the extensions in your
 account.
* [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html") to return detailed information
 about a specific extension or specific extension version, including current
 configuration data.
* [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html") to specify the
 configuration data for an extension in your account and to disable and
 enable Hooks.
* [set-type-default-version](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html") to specify which
 version of an extension is the default version.
* [deregister-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html") to remove a private
 extension or extension version from your account.
