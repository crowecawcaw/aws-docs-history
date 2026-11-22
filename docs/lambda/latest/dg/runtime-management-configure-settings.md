

# Managing Lambda runtime updates

Most Lambda Event Functions use the default **Auto** [runtime update mode](runtimes-update.md#runtime-management-controls), in which Lambda applies runtime version updates automatically. This page explains how to override that default by choosing a different runtime update mode, rolling back a runtime version, or controlling who can change these settings. It also explains how your choice of runtime update mode affects the shared responsibility model. These settings apply to functions that use Lambda-managed runtimes and to functions that use [customer-managed runtimes](runtimes-customer-managed.md).

## Configuring the runtime update mode
<a name="runtime-management-configure-settings-procedures"></a>

You can configure runtime management settings for your Lambda Event Functions using the Lambda console or the AWS Command Line Interface (AWS CLI). The same steps apply to functions that use Lambda-managed runtimes and to functions that use customer-managed runtimes. The only difference is the format of the runtime version ARN that you specify for **Manual** mode. For more information, see [Identifying Lambda runtime version changes](runtimes-update.md#runtime-management-identify).

**Note**  
You can configure runtime management settings separately for each [function version](configuration-versions.md).

**To configure how Lambda updates your runtime version (console)**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of an Event Function.

1. On the **Code** tab, under **Runtime settings**, choose **Edit runtime management configuration**.

1. Under **Runtime management configuration**, choose one of the following:
   + To have your function update to the latest runtime version automatically, choose **Auto**.
   + To have your function update to the latest runtime version when you change the function, choose **Function update**.
   + To pin your function to a specific runtime version, choose **Manual**, and then enter the runtime version ARN. You can find the runtime version ARN under **Runtime management configuration**. You can also find the ARN in the `INIT_START` line of your function logs. The ARN format differs for Lambda-managed runtimes and customer-managed runtimes. For more information, see [Identifying Lambda runtime version changes](runtimes-update.md#runtime-management-identify).

   For more information about these options, see [Runtime update modes](runtimes-update.md#runtime-management-controls).

1. Choose **Save**.

**To configure how Lambda updates your runtime version (AWS CLI)**

To configure runtime management for a function, run the [put-runtime-management-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-runtime-management-config.html) AWS CLI command. When using `Manual` mode, you must also provide the runtime version ARN. For functions that use a customer-managed runtime, specify a runtime version ARN of that runtime, such as `arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1`. To pin a function to a version of a customer-managed runtime, you also need additional permissions. For more information, see [Pin your function to a runtime version](cmr-using.md#cmr-using-pin).

```
aws lambda put-runtime-management-config \
  --function-name {{my-function}} \
  --update-runtime-on Manual \
  --runtime-version-arn {{arn:aws:lambda:us-east-2::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1}}
```

You should see output similar to the following:

```
{
  "UpdateRuntimeOn": "Manual",
  "FunctionArn": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
  "RuntimeVersionArn": "arn:aws:lambda:us-east-2::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1"
}
```

## Rolling back a Lambda runtime version
<a name="runtime-management-rollback"></a>

In the rare event that a new runtime version is incompatible with your existing Event Function, you can roll back its runtime version to an earlier one. This keeps your application working and minimizes disruption, providing time to remedy the incompatibility before returning to the latest runtime version.

Lambda doesn't impose a time limit on how long you can use any particular runtime version. However, we strongly recommend updating to the latest runtime version as soon as possible to benefit from the latest security patches, performance improvements, and features. Lambda provides the option to roll back to an earlier runtime version only as a temporary mitigation in the rare event of a runtime update compatibility issue. Functions using an earlier runtime version for an extended period might eventually experience degraded performance or issues, such as a certificate expiry, which can cause them to stop working properly.

You can roll back the runtime version for functions that use Lambda-managed runtimes and for functions that use customer-managed runtimes. To pin a function that uses a customer-managed runtime to an earlier runtime version, you need the `lambda:AssociateRuntimeVersion` permission on the runtime version ARN, in addition to `lambda:PutRuntimeManagementConfig`. For more information, see [How access to customer-managed runtimes works](cmr-permissions.md#cmr-permissions-how) and [Pin your function to a runtime version](cmr-using.md#cmr-using-pin). For a customer-managed runtime, the runtime publisher can also roll back a runtime alias for all functions that use it. For more information, see [Roll back a runtime update](cmr-aliases.md#cmr-aliases-rollback).

You can roll back a runtime version in the following ways:
+ [Using the Manual runtime update mode](#runtime-management-rollback-manual)
+ [Using published function versions](#runtime-management-rollback-published)

For more information, see [Introducing AWS Lambda runtime management controls](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-runtime-management-controls/) on the AWS Compute Blog.

### Roll back a runtime version using Manual runtime update mode
<a name="runtime-management-rollback-manual"></a>

If your function version uses the **Auto** or **Function update** runtime update mode, you can roll back your runtime version using the **Manual** mode. For the [function version](configuration-versions.md) you want to roll back, change the runtime version update mode to **Manual** and specify the ARN of the previous runtime version. For more information about finding the ARN of the previous runtime version, see [Identifying Lambda runtime version changes](runtimes-update.md#runtime-management-identify). For customer-managed runtimes, specify a runtime version of the same runtime. The version must support your function's architecture.

**Note**  
If the `$LATEST` version of your function is configured to use **Manual** mode, then you can't change the CPU architecture or runtime version that your function uses. To make these changes, you must change to **Auto** or **Function update** mode.

### Roll back a runtime version using published function versions
<a name="runtime-management-rollback-published"></a>

Published [function versions](configuration-versions.md) are an immutable snapshot of the `$LATEST` function code and configuration at the time that you created them. In **Auto** mode, Lambda automatically updates the runtime version of published function versions during phase two of the runtime version rollout. In **Function update** mode, Lambda doesn't update the runtime version of published function versions.

Published function versions using **Function update** mode therefore create a static snapshot of the function code, configuration, and runtime version. By using **Function update** mode with function versions, you can synchronize runtime updates with your deployments. You can also coordinate rollback of code, configuration, and runtime versions by redirecting traffic to an earlier published function version.

You can integrate this approach into your continuous integration and continuous delivery (CI/CD) for fully automatic rollback in the rare event of runtime update incompatibility. When using this approach, you must update your function regularly and publish new function versions to pick up the latest runtime updates. For more information, see [Understanding the shared responsibility model for Lambda runtime management](#runtime-management-shared).

This approach works the same way for functions that use Lambda-managed runtimes and for functions that use customer-managed runtimes. For customer-managed runtimes, published function versions in **Auto** mode follow the runtime alias, the same as `$LATEST`. For more information, see [Controlling runtime updates](cmr-using.md#cmr-using-controls).

## Controlling Lambda runtime update permissions for high-compliance applications
<a name="runtime-management-hc-applications"></a>

To meet patching requirements, Lambda customers typically rely on automatic runtime updates. If your application is subject to strict patching freshness requirements, you might want to limit use of earlier runtime versions. You can restrict Lambda's runtime management controls by using AWS Identity and Access Management (IAM) to deny users in your AWS account access to the [PutRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutRuntimeManagementConfig.html) API operation. This operation is used to choose the runtime update mode for an Event Function.

Denying access to this operation causes all functions to default to the **Auto** mode. You can apply this restriction across your organization by using a [service control policies (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). If you must roll back a function to an earlier runtime version, you can grant a policy exception on a case-by-case basis.

For functions that use customer-managed runtimes, pinning a function to a runtime version also requires the `lambda:AssociateRuntimeVersion` permission. You can deny this action to prevent pinning to specific runtime versions. For more information, see [How access to customer-managed runtimes works](cmr-permissions.md#cmr-permissions-how).

## Understanding the shared responsibility model for Lambda runtime management
<a name="runtime-management-shared"></a>

Lambda is responsible for curating and publishing security updates for all supported managed runtimes and container images. Responsibility for updating existing Event Functions to use the latest runtime version varies depending on which runtime update mode you use.

Lambda is responsible for applying runtime updates to all functions configured to use the **Auto** runtime update mode.

For functions configured with the **Function update** runtime update mode, you're responsible for regularly updating your function. Lambda is responsible for applying runtime updates when you make those updates. If you don't update your function, then Lambda doesn't update the runtime. If you don't regularly update your function, then we strongly recommend configuring it for automatic runtime updates so that it continues to receive security updates.

For functions configured to use the **Manual** runtime update mode, you're responsible for updating your function to use the latest runtime version. We strongly recommend that you use this mode only to roll back the runtime version as a temporary mitigation in the rare event of runtime update incompatibility. We also recommend that you change to **Auto** mode as quickly as possible to minimize the time in which your functions aren't patched.

If you're [using container images to deploy your functions](images-create.md), then Lambda is responsible for publishing updated base images. In this case, you're responsible for rebuilding your function's container image from the latest base image and redeploying the container image.

If your function uses a [customer-managed runtime](runtimes-customer-managed.md), the runtime publisher, rather than Lambda, is responsible for publishing runtime versions with the latest patches and for updating runtime aliases. Lambda applies the runtime version that the alias points to, based on the function's runtime update mode. The function owner's responsibilities for each mode are the same as for Lambda-managed runtimes.

This is summarized in the following table:



| Deployment mode | Lambda's responsibility | Customer's responsibility | 
| --- | --- | --- | 
| Managed runtime, Auto mode | Publish new runtime versions containing the latest patches.<br />Apply runtime patches to existing functions. | Roll back to a previous runtime version in the rare event of a runtime update compatibility issue. Follow best practices for [backward compatibility](runtimes-update.md#runtime-update-compatibility). | 
| Managed runtime, Function update mode | Publish new runtime versions containing the latest patches. | Update functions regularly to pick up the latest runtime version.<br />Switch a function to **Auto** mode when you're not regularly updating the function.<br />Roll back to a previous runtime version in the rare event of a runtime update compatibility issue. Follow best practices for [backward compatibility](runtimes-update.md#runtime-update-compatibility). | 
| Managed runtime, Manual mode | Publish new runtime versions containing the latest patches. | Use this mode only for temporary runtime rollback in the rare event of a runtime update compatibility issue.<br />Switch functions to **Auto** or **Function update** mode and the latest runtime version as soon as possible. | 
| Container image | Publish new container images containing the latest patches. | Redeploy functions regularly using the latest container base image to pick up the latest patches. | 
| Customer-managed runtime | Apply the runtime version that the runtime alias points to, according to the function's runtime update mode. | Runtime publisher: Publish new runtime versions containing the latest patches, and update runtime aliases. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).<br />Function owner: Choose the appropriate runtime alias for the function. Otherwise, the same responsibilities as for a Lambda-managed runtime in the selected runtime update mode. | 

For more information about shared responsibility with AWS, see [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).