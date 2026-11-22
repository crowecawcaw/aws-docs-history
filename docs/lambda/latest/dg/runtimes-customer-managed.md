

# Customer-managed runtimes

A customer-managed runtime is a Lambda runtime that you create and manage as a standalone resource. Lambda Event Functions can use your customer-managed runtime instead of using one of the built-in Lambda-managed runtimes. Customer-managed runtimes aren't available for Lambda Web Functions. You build a runtime once, share it across functions and accounts, and roll out updates to every function that uses it, without redeploying those functions.

## Why use customer-managed runtimes
<a name="runtimes-customer-managed-why"></a>

Lambda provides managed runtimes for popular programming languages, automatically handling patches so that you can focus on your code. With these Lambda-managed runtimes, Lambda controls what each runtime contains, when it's updated, and when it's deprecated. In contrast, customer-managed runtimes give you full control over the runtime contents, updates, and lifecycle. You can include any language or language version, your organization's SDKs, security and monitoring tools, and other shared components. Developers using your runtime for their functions keep the .zip file development and automatic runtime updates experience they are familiar with from Lambda-managed runtimes.

Other approaches to customizing the function execution environment carry an operational cost for each function. When using [container images](images-create.md) or [Lambda layers](chapter-layers.md), any changes to shared components require you to redeploy every affected function. In addition, with container images you must rebuild and redeploy your images to apply runtime security patches or other runtime updates. Customer-managed runtimes separate runtime management from function management. The publisher updates the runtime once, and functions pick up the update automatically, without redeployment. You can roll out updates, including security patches, across large numbers of functions, and roll back the same way. For a detailed comparison, see [Comparing customer-managed runtimes to other deployment models](#runtimes-customer-managed-compare).

You can also share one runtime across teams, across accounts, or publicly, so that teams standardize on approved components. This central control makes customer-managed runtimes a good fit for the following use cases:
+ **Enterprise platform teams** – Give every team in your organization a runtime with your approved security and monitoring tools built in, and update those tools centrally.
+ **SaaS and PaaS providers** – Control the SDKs and libraries that run in your customers' functions, and keep them current.
+ **Third-party runtime publishers** – Publish runtimes for languages that Lambda doesn't provide a managed runtime for, such as PHP.
+ **Control over runtime patching** – Take control over runtime patching to meet your organization's change control policy or compliance constraints. Extend the runtime lifetime beyond the published end-of-life schedule.

**Note**  
Previously, Lambda supported 'custom runtimes' by including a runtime in the function's deployment package or in a layer. For clarity, we now call this approach bring your own language (BYOL). Lambda still supports [BYOL](runtimes-custom.md). However, customer-managed runtimes have significant advantages. They give you full control over the runtime contents, and they decouple runtime management from function management. They also let you manage runtimes at scale across large numbers of functions. For these reasons, we recommend customer-managed runtimes instead of BYOL for most applications.

## Runtime publishers and runtime consumers
<a name="runtimes-customer-managed-roles"></a>

Customer-managed runtimes split runtime management and function management into two separate roles, the *runtime publisher* and *runtime consumer*. For example, a central cloud platform team can publish a runtime, and application teams can consume it for their functions. This creates a clean separation between runtime management and application development. Runtime publishers get control and autonomy over the runtime contents. Runtime consumers can focus on their application, instead of on shared components or runtime customization. One team can also fill both roles, and the roles can span AWS accounts.

As a **runtime publisher**, you own the runtime resource and its contents, updates, access control, and lifecycle. You're responsible for the following tasks:
+ **Runtime contents** – The runtime contents typically include the operating system libraries, language runtime, and any shared components. Runtimes also require a *runtime interface client* (RIC), which acts as the bridge between the Lambda service and the function handler. You define the runtime contents as a container image in Amazon Elastic Container Registry (Amazon ECR). You can start from a [Lambda runtime base container image](cmr-base-images.md), or [build your own runtime image from scratch](cmr-images-from-scratch.md). For more information, see [Creating a runtime](cmr-create.md).
+ **Runtime updates, including security updates** – You're responsible for all runtime updates, including security patches for every component in the runtime. If you start from a Lambda base container image, you must rebuild and redeploy your runtime to pick up any updates. You must keep your updates backward compatible with existing functions. For more information, see [Building a runtime image from a Lambda base image](cmr-base-images.md).
+ **Update rollout** – You decide when and how updates reach functions. To roll out a new runtime version, you update a runtime alias. By default, Lambda then applies the new runtime version to functions automatically, the same as for functions that use Lambda-managed runtimes. You can choose how to stage the rollout, for example by environment. You monitor the rollout and roll back if needed. For more information, see [Runtime aliases](cmr-aliases.md), [Deploying runtime updates](cmr-deploy-updates.md), and [Monitoring customer-managed runtimes](cmr-monitoring.md).
+ **Access control** – You control who can use the runtime by using a resource-based policy. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).
+ **Lifecycle and consumer communication** – You manage the lifecycle of runtime versions, including deprecation. You also delete runtimes, runtime versions, and runtime aliases that you no longer need. Notifying consumers about updates, deprecations, and deletions is your responsibility. For more information, see [Runtime lifecycle](cmr-lifecycle.md) and [Deleting and restoring runtimes](cmr-delete.md).

As a **runtime consumer**, you configure your function to use the correct customer-managed runtime and runtime alias, instead of a Lambda-managed runtime identifier such as `python3.14`. You still deploy your function as a .zip file archive, and you don't see the container images that the runtime publisher uses. Read any guidance from the runtime publisher. For example, check the runtime's description and license information, and use the alias descriptions to choose the right alias. If the publisher defined a [deprecation lifecycle](cmr-lifecycle.md), plan your function updates around its dates. Otherwise, your function development experience is the same as with Lambda-managed runtimes. For more information, see [Using a customer-managed runtime](cmr-using.md).

Block dates stop function creates and updates, but they never stop invocations. If the publisher deletes a runtime alias or runtime version that your function depends on, your function enters the `Inactive` state. Existing execution environments continue to handle invocations, but invocations that require a cold start fail. For more information, see [Runtime lifecycle and function states](cmr-using.md#cmr-using-lifecycle), [Runtime lifecycle](cmr-lifecycle.md), and [Deleting and restoring runtimes](cmr-delete.md).

**Important**  
A runtime publisher can push updates to the runtime to apply security patches, bug fixes, or other updates. This means they can also push their code into the execution environments of functions that use the runtime. This code runs with the permissions of each function's execution role. Only use customer-managed runtimes from publishers that you trust. For third-party runtimes or critical applications, the publisher might make its runtime images available. If so, you can copy them to your own Amazon ECR repository and create your own customer-managed runtime from them. To control when your function picks up runtime updates, use the **Function update** or **Manual** runtime update mode. For more information, see [Controlling runtime updates](cmr-using.md#cmr-using-controls). To detect runtime changes, check the runtime version in the `INIT_START` log line. For more information, see [Check which runtime version your function uses](cmr-using.md#cmr-using-check-version).

## Resource model
<a name="runtimes-customer-managed-resources"></a>

Customer-managed runtimes use three types of resources: runtimes, runtime versions, and runtime aliases.
+ **Runtime** – The top-level resource that represents the runtime as a whole, such as a PHP 8 runtime for your organization. The runtime resource is the parent of its runtime versions and runtime aliases. Each runtime has a name, an Amazon Resource Name (ARN), and a description. For more information, see [Creating a runtime](cmr-create.md).

  You control access at the runtime level by using a resource-based policy. By default, only the account that owns a runtime can use it. You can share a runtime with specific AWS accounts, with an organization or organizational unit (OU) in AWS Organizations, or publicly. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).
+ **Runtime version** – Represents the contents of the runtime. That is, the file system of the execution environment where Lambda loads and invokes your function code. You package each runtime version as a container image in Amazon ECR.

  Runtime versions are immutable. To update a runtime, you create a new runtime version, then migrate functions to that version by updating your runtime aliases. Each runtime version points to a distinct container image. For more information, see [Runtime versions](cmr-versions.md).
+ **Runtime alias** – A named pointer to a runtime version. Functions consume a runtime through an alias. When you update an alias, functions that use it move to the new runtime version at their next cold start, unless you have [opted out of automatic runtime updates](runtime-management-configure-settings.md). Running execution environments keep the previous runtime version until Lambda replaces them, so during a rollout, invocations can run on both versions. For more information, see [Runtime aliases](cmr-aliases.md), [Check which runtime version your function uses](cmr-using.md#cmr-using-check-version), and [Monitoring customer-managed runtimes](cmr-monitoring.md).

Runtimes are Regional resources. You must create a runtime in each AWS Region where you want to use it. For details on how to deploy a runtime across multiple AWS Regions, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

You manage runtimes, runtime versions, and runtime aliases with the Lambda Core API (`aws lambda-core` in the AWS CLI). For functions, tags, and resource-based policies, you use the Lambda API (`aws lambda`).

## Comparing customer-managed runtimes to other deployment models
<a name="runtimes-customer-managed-compare"></a>

The following table compares customer-managed runtimes with Lambda-managed runtimes, [container images](images-create.md), and [bring your own language (BYOL)](runtimes-custom.md). With BYOL, you include the runtime in your function package or in a layer, and use an [OS-only runtime](lambda-runtimes.md#runtimes-provided).

Like customer-managed runtimes, container images give you full control over the file system of the execution environment. However, with container images, you must rebuild and redeploy each function to apply updates.


**Comparison of Lambda deployment models**  

| Feature | Lambda-managed runtime | Customer-managed runtime | Container image | BYOL | 
| --- | --- | --- | --- | --- | 
| Languages | Only languages that Lambda supports | Any language | Any language | Any language | 
| Cross-account sharing | Not applicable | Share the runtime by using a resource-based policy | Share the image across accounts in Amazon ECR | Share the runtime layer across accounts | 
| Runtime control | AWS | Runtime publisher | Function developer | Function developer | 
| Function deployment format | .zip file | .zip file | Container image | .zip file including language runtime and bootstrap file, or layer | 
| Update mechanism | Lambda applies updates automatically | Runtime publisher creates a new runtime version and updates one or more runtime aliases; functions pick up the update at their next cold start | Rebuild the image and redeploy the function | Update the runtime layer and redeploy each function | 
| OS patching responsibility | AWS | Runtime publisher | Function developer, by rebuilding from an updated base image | AWS, for the OS-only runtime; function developer for the language runtime or layer | 
| Update scale | Lambda-controlled, gradual rollout | Per alias (targeted rollout) | Per function | Per function | 
| Deprecation management | AWS | Runtime publisher | Function developer | AWS, for the OS-only runtime; function developer for the language runtime or layer | 

## Supported features and Regions
<a name="runtimes-customer-managed-features"></a>

Customer-managed runtimes work with Lambda Event Functions only. You can't use a customer-managed runtime with Lambda Web Functions. For information about runtimes for Web Functions, see [Lambda Web Function runtimes](web-functions-runtimes.md).

Functions that use customer-managed runtimes can use all Lambda features, with the following exceptions:
+ **[Lambda SnapStart](snapstart.md)** – Functions that use a customer-managed runtime can't use SnapStart.
+ **[Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)** – You can't use functions that use a customer-managed runtime with Lambda@Edge.

Some Lambda features, such as [Lambda Managed Instances](lambda-managed-instances.md) and [response streaming](configuration-response-streaming.md), work only if the runtime implements them. To find out which features a runtime supports, check the runtime publisher's documentation. For information about how runtimes support these features, see [Architectures and feature compatibility](cmr-building-images.md#cmr-building-images-capabilities).

If you're a runtime publisher, note the following limitations:
+ You can't encrypt runtime resources with an AWS KMS customer managed key.
+ You can't use [code signing](configuration-codesigning.md) to sign runtime images.
+ You can't publish or update customer-managed runtimes by using the [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).

If you're a runtime consumer, these publisher limitations don't apply to your functions. Functions that use a customer-managed runtime keep their existing support for AWS KMS customer managed keys and code signing.

For information about defining functions that use customer-managed runtimes with infrastructure as code tools, see [Infrastructure as code](cmr-using.md#cmr-using-iac).

Customer-managed runtimes are available in all commercial AWS Regions.

For quotas, see [Customer-managed runtimes](gettingstarted-limits.md#cmr-quotas) in [Lambda quotas](gettingstarted-limits.md).

## Pricing
<a name="runtimes-customer-managed-pricing"></a>

There's no additional charge for customer-managed runtimes. Functions that use a customer-managed runtime cost the same as functions that use a Lambda-managed runtime. There's no charge for each runtime version.

Publishers must keep the container image for each runtime version in Amazon ECR for as long as the runtime version exists. Standard Amazon ECR storage pricing applies. For more information, see [Amazon ECR pricing](https://aws.amazon.com/ecr/pricing/).

## Next steps
<a name="runtimes-customer-managed-next-steps"></a>

To get started with customer-managed runtimes, see the following topics:
+ Runtime publishers: To build a runtime image, see [Building runtime images](cmr-building-images.md). To create a runtime, see [Creating a runtime](cmr-create.md).
+ Runtime consumers: To configure a function to use a runtime, see [Using a customer-managed runtime](cmr-using.md).
+ For an end-to-end example, see [Tutorial: Creating and using a customer-managed runtime](cmr-tutorial.md).