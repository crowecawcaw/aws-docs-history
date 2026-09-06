

# Command Line and API Access
<a name="cli-and-api-access"></a>

You can use the command line interface (CLI), Query API, or REST interfaces to access AWS GovCloud (US) services. You can also use a language-specific software development kit (SDK). For more information about the CLI and SDK tools, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/).

For the CLI and APIs, users need programmatic access.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that’s accessing AWS.

To grant users programmatic access, choose one of the following options.


| Which user needs programmatic access? | To | By | 
| --- | --- | --- | 
| Workforce identity (Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br />\* For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*.<br />\* For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. | 
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*. | 
| IAM | (Not recommended) Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br />\* For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*.<br />\* For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*.<br />\* For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*. | 

After you have installed your preferred tool, you can access AWS GovCloud (US) by specifying the AWS GovCloud (US) Region [endpoint](https://docs.aws.amazon.com/general/latest/gr/rande.html#govcloud_region) for the AWS service that you want to access.

For information about setting Regions using the AWS SDKs, see [Available Region Endpoints for the AWS SDKs](https://aws.amazon.com/articles/3912) in the AWS Developer Center.

If you use the CLI, you can either specify the AWS GovCloud (US) endpoint every time you enter a command, or you can set an environment variable that specifies the endpoint. For more information, see the CLI documentation for the service.

```
#Example Call

aws s3 ls --endpoint-url https://s3-fips.us-gov-west-1.amazonaws.com --region us-gov-west-1
```