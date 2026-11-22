

# Understanding how Lambda manages runtime updates

Lambda keeps each managed runtime up to date with security updates, bug fixes, new features, performance enhancements, and support for minor version releases. These runtime updates are published as *runtime versions*. Lambda applies runtime updates to Lambda Event Functions by migrating the function from an earlier runtime version to a new runtime version.

By default, for functions that use Lambda-managed runtimes, Lambda applies runtime updates automatically. With automatic runtime updates, Lambda takes on the operational burden of patching the runtime versions. For most customers, automatic updates are the right choice. You can change this default behavior by [configuring runtime management settings](runtime-management-configure-settings.md).

If your function uses a [customer-managed runtime](runtimes-customer-managed.md), the runtime publisher creates the runtime versions and decides when to roll them out by updating runtime aliases. The runtime update modes on this page also apply to functions that use customer-managed runtimes. For more information, see [Controlling runtime updates](cmr-using.md#cmr-using-controls).

Lambda also publishes each new runtime version as a container image. To update runtime versions for container-based functions, you must [create a new container image](images-create.md) from the updated base image and redeploy your function.

Each runtime version is associated with a version number and an ARN (Amazon Resource Name). Runtime version numbers use a numbering scheme that Lambda defines, independent of the version numbers that the programming language uses. Runtime version numbers are not always sequential. For example, version 42 might be followed by version 45. The runtime version ARN is a unique identifier for each runtime version. You can view the ARN of your function's current runtime version in the Lambda console, or the [`INIT_START` line of your function logs](#runtime-management-identify). For information about managing runtime updates in health-critical applications, see [Controlling Lambda runtime update permissions for high-compliance applications](runtime-management-configure-settings.md#runtime-management-hc-applications).

Runtime versions should not be confused with runtime identifiers. Each runtime has a unique **runtime identifier**, such as `python3.14` or `nodejs24.x`. These correspond to each major programming language release. Runtime versions describe the patch version of an individual runtime.

**Note**  
The ARN for the same runtime version number can vary between AWS Regions and CPU architectures.

**Topics**
+ [Backward compatibility](#runtime-update-compatibility)
+ [Runtime update modes](#runtime-management-controls)
+ [Two-phase runtime version rollout](#runtime-management-two-phase)
+ [Identifying Lambda runtime version changes](#runtime-management-identify)
+ [Managing Lambda runtime updates](runtime-management-configure-settings.md)

## Backward compatibility
<a name="runtime-update-compatibility"></a>

Lambda strives to provide runtime updates that are backward compatible with existing functions. However, as with software patching, there are rare cases in which a runtime update can negatively impact an existing function. For example, security patches can expose an underlying issue with an existing function that depends on the previous, insecure behavior.

When building and deploying your function, it is important to understand how to manage your dependencies to avoid potential incompatibilities with a future runtime update. For example, suppose your function has a dependency on package A, which in turn depends on package B. Both packages are included in the Lambda runtime (for example, they could be parts of the SDK or its dependencies, or parts of the runtime system libraries).

Consider the following scenarios:


| Deployment | Patching compatible | Reason | 
| --- | --- | --- | 
|  +  **Package A:** Use from runtime <br />+  **Package B:** Use from runtime   | Yes | Future runtime updates to packages A and B are backward compatible. | 
|  +  **Package A:** In deployment package <br />+  **Package B:** In deployment package   | Yes | Your deployment takes precedence, so future runtime updates to packages A and B have no effect. | 
|  +  **Package A:** In deployment package <br />+  **Package B:** Use from runtime   | Yes\* | Future runtime updates to package B are backward compatible.<br />\*If A and B are tightly coupled, compatibility issues can occur. For example, the `boto3` and `botocore` packages in the AWS SDK for Python should be deployed together. | 
|  +  **Package A:** Use from runtime <br />+  **Package B:** In deployment package   | No | Future runtime updates to package A might require an updated version of package B. However, the deployed version of package B takes precedence, and might not be forward compatible with the updated version of package A. | 

To maintain compatibility with future runtime updates, follow these best practices:
+ **When possible, package all dependencies:** Include all required libraries, including the AWS SDK and its dependencies, in your deployment package. This ensures a stable, compatible set of components.
+ **Use runtime-provided SDKs sparingly:** Only rely on the runtime-provided SDK when you can't include additional packages (for example, when using the Lambda console code editor or inline code in an AWS CloudFormation template).
+ **Avoid overriding system libraries:** Don't deploy custom operating system libraries that might conflict with future runtime updates.

If you publish a customer-managed runtime, you're responsible for keeping your runtime updates backward compatible with the functions that use it. For more information, see [Compatibility constraints on updates](cmr-deploy-updates.md#cmr-deploy-updates-compatibility).

## Runtime update modes
<a name="runtime-management-controls"></a>

Lambda strives to provide runtime updates that are backward compatible with existing functions. However, as with software patching, there are rare cases in which a runtime update can negatively impact an existing function. For example, security patches can expose an underlying issue with an existing function that depends on the previous, insecure behavior. Lambda runtime management controls help reduce the risk of impact to your workloads in the rare event of a runtime version incompatibility. For each [function version](configuration-versions.md) (`$LATEST` or published version), you can choose one of the following runtime update modes:
+ **Auto (default)** – Automatically update to the most recent and secure runtime version using [Two-phase runtime version rollout](#runtime-management-two-phase). We recommend this mode for most customers so that you always benefit from runtime updates.
+ **Function update** – Update to the most recent and secure runtime version when you update your function. When you update your function, Lambda updates the runtime of your function to the most recent and secure runtime version. This approach synchronizes runtime updates with function deployments, giving you control over when Lambda applies runtime updates. With this mode, you can detect and mitigate rare runtime update incompatibilities early. When using this mode, you must regularly update your functions to keep their runtime up to date.
+ **Manual** – Manually update your runtime version. You specify a runtime version in your function configuration. The function uses this runtime version indefinitely.

  In the rare case in which a new runtime version is incompatible with an existing function, you can use this mode to roll back your function to an earlier runtime version. We recommend against using **Manual** mode to try to achieve runtime consistency across deployments. For more information, see [Rolling back a Lambda runtime version](runtime-management-configure-settings.md#runtime-management-rollback).

Responsibility for applying runtime updates to your functions varies according to which runtime update mode you choose. For more information, see [Understanding the shared responsibility model for Lambda runtime management](runtime-management-configure-settings.md#runtime-management-shared).

## Two-phase runtime version rollout
<a name="runtime-management-two-phase"></a>

For Lambda-managed runtimes, Lambda introduces new runtime versions in the following order:

1. In the first phase, Lambda applies the new runtime version whenever you create or update a function. A function gets updated when you call the [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html) or [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html) API operations.

1. In the second phase, Lambda updates any function that uses the **Auto** runtime update mode and that hasn't already been updated to the new runtime version. 

The overall duration of the rollout process varies according to multiple factors, including the severity of any security patches included in the runtime update.

If you're actively developing and deploying your functions, you most likely pick up new runtime versions during the first phase. This synchronizes runtime updates with function updates. In the rare event that the latest runtime version negatively impacts your application, this approach gives you the opportunity to take prompt corrective action. Functions that aren't in active development still receive the operational benefit of automatic runtime updates during the second phase.

This approach doesn't affect functions set to **Function update** or **Manual** mode. Functions using **Function update** mode receive the latest runtime updates only when you create or update them. Functions using **Manual** mode don't receive runtime updates.

The two-phase rollout applies only to Lambda-managed runtimes. For customer-managed runtimes, the runtime publisher controls the rollout by updating runtime aliases. For example, the publisher can update a `dev` alias first and a `prod` alias later, Region by Region. Functions in **Auto** mode pick up the new runtime version at their next cold start. For more information, see [Runtime aliases](cmr-aliases.md) and [Deploying runtime updates](cmr-deploy-updates.md).

Lambda publishes new runtime versions in a gradual, rolling fashion across AWS Regions. If your functions are set to **Auto** or **Function update** modes, it's possible that functions deployed at the same time to different Regions, or at different times in the same Region, pick up different runtime versions. If you require guaranteed runtime version consistency across your environments, consider the following options:
+ **Use a customer-managed runtime** – With a [customer-managed runtime](runtimes-customer-managed.md), you or your organization's runtime publisher controls which runtime versions exist and when runtime aliases move. Your functions get new runtime versions on your schedule.
+ **Use container images** – [Deploy your functions as container images](images-create.md). You choose when to rebuild your image from an updated base image and redeploy your function.

The **Manual** mode is designed as a temporary mitigation to enable runtime version rollback in the rare event that a runtime version is incompatible with your function.

## Identifying Lambda runtime version changes
<a name="runtime-management-identify"></a>

The [runtime version number](runtimes-update.md) and ARN are logged in the `INIT_START` log line, which Lambda emits to CloudWatch Logs each time that it creates a new [execution environment](concepts-basics.md#gettingstarted-concepts-runtime). Because the execution environment uses the same runtime version for all function invocations, Lambda emits the `INIT_START` log line only when Lambda executes the init phase. Lambda doesn't emit this log line for each function invocation. Lambda emits the log line to CloudWatch Logs, but it is not visible in the console. Lambda emits the `INIT_START` log line for functions that use Lambda-managed runtimes and for functions that use customer-managed runtimes. The runtime version and runtime version ARN formats differ between the two.

**Note**  
Runtime version numbers are not always sequential. For example, version 42 might be followed by version 45.
+ **Lambda-managed runtimes** – The runtime version has the format `{{runtime}}:{{language-version}}.v{{number}}`, such as `python:3.13.v14`. The runtime version ARN has the format `arn:aws:lambda:{{region}}::runtime:{{hash}}`, with no account ID.
+ **Customer-managed runtimes** – The runtime version has the format `{{runtime-name}}:{{version-name}}`, such as `companyphp8:v8.3.2`. The runtime version ARN has the format `arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}/version/{{version-name}}`. For more information, see [Check which runtime version your function uses](cmr-using.md#cmr-using-check-version).

**Example INIT\_START log line (Lambda-managed runtime)**  

```
INIT_START Runtime Version: python:3.13.v14    Runtime Version ARN: arn:aws:lambda:eu-south-1::runtime:7b620fc2e66107a1046b140b9d320295811af3ad5d4c6a011fad1fa65127e9e6
```

**Example INIT\_START log line (customer-managed runtime)**  

```
INIT_START Runtime Version: companyphp8:v8.3.2    Runtime Version ARN: arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2
```

Rather than working directly with the logs, you can use [Amazon CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-CreateRule.html) to identify transitions between runtime versions. The following rule counts the distinct runtime versions from each `INIT_START` log line. To use the rule, replace the example log group name `/aws/lambda/*` with the appropriate prefix for your function or group of functions. The rule works for both Lambda-managed runtimes and customer-managed runtimes.

```
{
  "Schema": {
    "Name": "CloudWatchLogRule",
    "Version": 1
  },
  "AggregateOn": "Count",
  "Contribution": {
    "Filters": [
      {
        "Match": "eventType",
        "In": [
          "INIT_START"
        ]
      }
    ],
    "Keys": [
      "runtimeVersion",
      "runtimeVersionArn"
    ]
  },
  "LogFormat": "CLF",
  "LogGroupNames": [
    "{{/aws/lambda/*}}"
  ],
  "Fields": {
    "1": "eventType",
    "4": "runtimeVersion",
    "8": "runtimeVersionArn"
  }
}
```

The following CloudWatch Contributor Insights report shows an example of a runtime version transition as captured by the preceding rule. The orange line shows execution environment initialization for the earlier runtime version (**python:3.13.v12**), and the blue line shows execution environment initialization for the new runtime version (**python:3.13.v14**).

![Graph showing the transition from one runtime version to another.](https://docs.aws.amazon.com/lambda/latest/dg/images/runtime_version_graph.png)
