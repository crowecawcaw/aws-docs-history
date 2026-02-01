• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Troubleshooting

AWS Systems Manager Distributor

The following information can help you troubleshoot problems that might occur when you
use Distributor, a tool in AWS Systems Manager.

###### Topics

- [Wrong package with the same name is
  installed](#distributor-tshoot-1 "#distributor-tshoot-1")
- [Error: Failed to retrieve manifest: Could not
  find latest version of package](#distributor-tshoot-2 "#distributor-tshoot-2")
- [Error: Failed to retrieve manifest:
  Validation exception](#distributor-tshoot-3 "#distributor-tshoot-3")
- [Package isn't supported (package is missing
  install action)](#distributor-tshoot-4 "#distributor-tshoot-4")
- [Error: Failed to download manifest : Document
  with name does not exist](#distributor-tshoot-5 "#distributor-tshoot-5")
- [Upload failed.](#distributor-tshoot-6 "#distributor-tshoot-6")
- [Error: Failed to find platform: no manifest
  found for platform: oracle, version 8.9, architecture x86_64](#distributor-tshoot-7 "#distributor-tshoot-7")

## Wrong package with the same name is

installed

**Problem:** You've installed a package, but Distributor
installed a different package instead.

**Cause:** During installation, Systems Manager finds AWS
published packages as results before user-defined external packages. If your
user-defined package name is the same as an AWS published package name, the AWS
package is installed instead of your package.

**Solution:** To avoid this problem, name your
package something different from the name for an AWS published package.

## Error: Failed to retrieve manifest: Could not

find latest version of package

**Problem:** You received an error like the
following.

```
Failed to retrieve manifest: ResourceNotFoundException: Could not find the latest version of package
arn:aws:ssm:::package/package-name status code: 400, request id: guid
```

**Cause:** You're using a version of SSM Agent with
Distributor that is earlier than version 2.3.274.0.

**Solution:** Update the version of SSM Agent to
version 2.3.274.0 or later. For more information, see [Updating the SSM Agent using
Run Command](run-command-tutorial-update-software.md#rc-console-agentexample "run-command-tutorial-update-software.md#rc-console-agentexample") or
[Walkthrough: Automatically update
SSM Agent with the AWS CLI](state-manager-update-ssm-agent-cli.md "state-manager-update-ssm-agent-cli.md").

## Error: Failed to retrieve manifest:

Validation exception

**Problem:** You received an error like the
following.

```
Failed to retrieve manifest: ValidationException: 1 validation error detected: Value 'documentArn'
at 'packageName' failed to satisfy constraint: Member must satisfy regular expression pattern:
arn:aws:ssm:region-id:account-id:package/package-name
```

**Cause:** You're using a version of SSM Agent with
Distributor that is earlier than version 2.3.274.0.

**Solution:** Update the version of SSM Agent to
version 2.3.274.0 or later. For more information, see [Updating the SSM Agent using
Run Command](run-command-tutorial-update-software.md#rc-console-agentexample "run-command-tutorial-update-software.md#rc-console-agentexample") or
[Walkthrough: Automatically update
SSM Agent with the AWS CLI](state-manager-update-ssm-agent-cli.md "state-manager-update-ssm-agent-cli.md").

## Package isn't supported (package is missing

install action)

**Problem:** You received an error like the
following.

```
Package is not supported (package is missing install action)
```

**Cause:** The package directory structure is
incorrect.

**Solution:** Don't zip a parent directory containing
the software and required scripts. Instead, create a `.zip` file
of all the required contents directly in the absolute path. To verify the
`.zip` file was created correctly, unzip the target platform
directory and review the directory structure. For example, the install script
absolute path should be
`/`ExamplePackage_targetPlatform`/install.sh`.

## Error: Failed to download manifest : Document

with name does not exist

**Problem:** You received an error like the
following.

```
Failed to download manifest - failed to retrieve package document description: InvalidDocument: Document with name `filename` does not exist.
```

**Cause 1:** Distributor can't find the package by the
package name when sharing a Distributor package from another account.

**Solution 1:** When sharing a package from another
account, use the full Amazon Resource Name (ARN) for the package and not just its
name.

**Cause 2:** When using a VPC, you haven't provided
your IAM instance profile with access to the AWS managed S3 bucket that contains
the document `AWS-ConfigureAWSPackage` for the AWS Region you
are targeting.

**Solution 2:** Ensure that your IAM instance
profile provides SSM Agent with access to the AWS managed S3 bucket that contains
the document `AWS-ConfigureAWSPackage` for the AWS Region you
are targeting, as explained in [SSM Agent communications with
AWS managed S3 buckets](ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions "ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions").

## Upload failed.

**Problem:** You received an error like the
following.

```
Upload failed. At least one of your files was not successfully uploaded to your S3 bucket.
```

**Cause:** The name of your software package includes
a space. For example, `Hello World.msi` would fail to upload.

## Error: Failed to find platform: no manifest

found for platform: oracle, version 8.9, architecture x86_64

**Problem:** You received an error like the
following.

```
Failed to find platform: no manifest found for platform: oracle, version 8.9, architecture x86_64
```

**Cause:** The error means that the JSON package
manifest does not have any definition for that platform, in this case, Oracle
Linux..

**Solution:** Download the package you want to
distribute from the [Trend Micro Deep
Security Software](https://help.deepsecurity.trendmicro.com/software.html "https://help.deepsecurity.trendmicro.com/software.html") site. Create an `.rpm` software package
using the [Create a
package using the Simple workflow](distributor-working-with-packages-create.md#distributor-working-with-packages-create-simple "distributor-working-with-packages-create.md#distributor-working-with-packages-create-simple"). Set the
following values for the package and complete the upload software package using
Distributor:

```
Platform version: _any
Target platform: oracle
Architecture: x86_64
```
