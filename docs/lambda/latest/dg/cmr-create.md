

# Creating a runtime

As a runtime publisher, you start by creating a runtime. The runtime is the top-level resource for a customer-managed runtime. It holds the name, Amazon Resource Name (ARN), description, license information, and lifecycle information for the runtime as a whole. It's also where you control who can use the runtime. For an overview of customer-managed runtimes and the resource model, see [Customer-managed runtimes](runtimes-customer-managed.md).

This topic explains runtime properties, tags, and access, and then shows you how to create, update, and tag a runtime.

**Topics**
+ [About the runtime resource](#cmr-create-about)
+ [Runtime properties](#cmr-create-properties)
+ [Runtime tags](#cmr-create-tags)
+ [Runtime access](#cmr-create-access)
+ [Prerequisites](#cmr-create-prereqs)
+ [Create a runtime](#cmr-create-procedure)
+ [Update a runtime](#cmr-create-update)
+ [Manage runtime tags](#cmr-create-manage-tags)
+ [Next steps](#cmr-create-next-steps)
+ [Runtime versions](cmr-versions.md)
+ [Runtime aliases](cmr-aliases.md)

## About the runtime resource
<a name="cmr-create-about"></a>

A runtime is the parent of its runtime versions and runtime aliases. Runtime versions define the contents of the runtime, and runtime aliases point functions to a runtime version. Runtimes are Regional resources. You must create a runtime in each AWS Region where you want to use it. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

Functions can't use a new runtime yet. A new runtime has no runtime versions and no runtime aliases. To make a runtime available to functions, complete the following workflow:

1. Build a runtime image and push it to Amazon ECR. For more information, see [Building runtime images](cmr-building-images.md).

1. Create the runtime, as described in this topic.

1. Create a runtime version from the image. For more information, see [Runtime versions](cmr-versions.md).

1. Create a runtime alias that points to the runtime version. For more information, see [Runtime aliases](cmr-aliases.md).

1. Grant other accounts access to the runtime, if needed. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

You can create the runtime before or after you build the image. You must create the runtime before you create any runtime versions or runtime aliases.

Lambda creates a runtime synchronously. The runtime is available as soon as the create request succeeds.

## Runtime properties
<a name="cmr-create-properties"></a>

A runtime has the following properties:

`Name`  
The name of the runtime. The name is required, and you can't change it after you create the runtime. Lambda uses the name as part of the runtime ARN. The name must meet the following requirements:  
+ Contain 2–128 characters
+ Contain only lowercase letters, numbers, underscores (`_`), periods (`.`), and hyphens (`-`)
+ Start and end with a lowercase letter or a number
+ Be unique among the runtimes in your account in the AWS Region
We recommend that you include the language or framework and its major version in the name, for example, `companyphp8` or `mynode24`. This helps runtime consumers identify the runtime. You can also create a separate runtime for each major version.

`Description`  
(Optional) A description of the runtime. Use the description to tell runtime consumers what the runtime is for and what it contains.

`LicenseInfo`  
(Optional) License information for the runtime. A runtime image often includes third-party software, such as a language runtime, libraries, and tools. Use this property to list the licenses for this software. For example, you can list the license names or provide a link to a page that describes them.  
If you omit `Description` or `LicenseInfo`, Lambda returns an empty string for it.

`ReleaseLifecycle`  
(Optional) The release state and deprecation dates for the runtime. You can set this property when you create the runtime or later. You can also set lifecycle information on individual runtime aliases. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

After you create a runtime, Lambda also returns the following read-only properties:
+ `Arn` – The ARN of the runtime.
+ `Created` – The time when you created the runtime.
+ `LastModified` – The time when you last updated the runtime.
+ `State` – The state of the runtime. This property appears in the output only when the runtime is scheduled for deletion. In that case, its value is `PENDING_DELETION`.
+ `PendingDeletionAt` – The date and time when Lambda permanently deletes the runtime. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

A runtime ARN has the format `arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}`.

For example, the ARN of a runtime named `companyphp8` in account `123456789012` in the US East (N. Virginia) Region is `arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8`. The ARNs of runtime versions and runtime aliases extend the runtime ARN. For more information, see [Runtime versions](cmr-versions.md) and [Runtime aliases](cmr-aliases.md).

Operations on runtime versions and runtime aliases accept either the runtime name or the full runtime ARN to identify the runtime.

## Runtime tags
<a name="cmr-create-tags"></a>

You can add tags to a runtime to organize your resources, track costs, and control access. You can add tags when you create the runtime. To add, change, or remove tags later, use the Lambda tagging operations `TagResource`, `UntagResource`, and `ListTags` with the runtime ARN.

The response from creating a runtime doesn't include tags. To view the tags on a runtime, use `ListTags`.

You can tag runtimes only. You can't tag runtime versions or runtime aliases.

You can use tags in IAM policies to control access to runtimes with attribute-based access control (ABAC). For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md) and [Using attribute-based access control in Lambda](attribute-based-access-control.md). For general information about tags in Lambda, see [Using tags on Lambda Event Functions](configuration-tags.md).

Runtime operations support the `aws:RequestTag/{{key}}`, `aws:TagKeys`, and `aws:ResourceTag/{{key}}` condition keys. For runtime versions and aliases, `aws:ResourceTag` uses the runtime's tags.

## Runtime access
<a name="cmr-create-access"></a>

By default, only the AWS account that owns a runtime can use it. To share the runtime with other accounts, with an organization, or publicly, you attach a resource-based policy to the runtime. You control access at the runtime level. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

**Important**  
If you share a runtime publicly, any AWS account can use the runtime in its functions. Before you share a runtime publicly, review what the runtime image contains. Also review the licenses of the software that the image includes. For more information, see [Share a runtime publicly](cmr-permissions.md#cmr-permissions-share-public).

## Prerequisites
<a name="cmr-create-prereqs"></a>

Before you create a runtime, make sure that you meet the following requirements.

### Required permissions
<a name="cmr-create-iam"></a>

To create and manage runtimes, runtime versions, and runtime aliases, your IAM identity needs IAM permissions. For a list of the IAM actions for customer-managed runtimes, see [IAM actions](cmr-permissions.md#cmr-permissions-actions). For more information about access control for customer-managed runtimes, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Create a runtime
<a name="cmr-create-procedure"></a>

You can create a runtime by using the Lambda console or the AWS CLI.

### Create a runtime (console)
<a name="cmr-create-console"></a>

**To create a runtime (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose **Create runtime**.

1. In the **Runtime basic information** pane, for **Runtime name**, enter a name for your runtime.

1. Optionally, expand **Additional settings**, and then enter a **Runtime description** and **License information**.

1. In the **Runtime version configuration** pane, for **Runtime version name**, enter a name for the first runtime version.

1. For **Image source**, do one of the following:
   + To use an image in your account, make sure that **Owned by you** is selected. Choose **Browse ECR**, and then select the Amazon ECR repository and the runtime version image.
   + To use an image that another account shared with you, select **Shared with you**, and then paste the URI of the container image.

1. Optionally, enter **Release notes** for the runtime version.

1. Optionally, to also create a runtime alias, in the **Runtime alias configuration** pane, enter a **Runtime alias name**. You can also enter an **Alias description**.

In addition to the runtime, the console creates your first runtime version. If you entered an alias name, the console also creates a runtime alias that points to that runtime version.

### Create a runtime (AWS CLI)
<a name="cmr-create-cli"></a>

**To create a runtime (AWS CLI)**

1. To create the runtime, run the `create-runtime` command. The following example creates a runtime named `companyphp8` with a description, license information, and two tags.

   ```bash
   aws lambda-core create-runtime \
     --name {{companyphp8}} \
     --description "{{PHP 8 runtime with company-approved extensions}}" \
     --license-info "{{PHP License v3.01. Includes components under the MIT and Apache-2.0 licenses.}}" \
     --tags {{Team=platform,Project=runtimes}}
   ```

   You should see output similar to the following:

   ```json
   {
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
       "Name": "companyphp8",
       "Description": "PHP 8 runtime with company-approved extensions",
       "LicenseInfo": "PHP License v3.01. Includes components under the MIT and Apache-2.0 licenses.",
       "Created": "2026-10-05T17:21:09.112Z",
       "LastModified": "2026-10-05T17:21:09.112Z"
   }
   ```

   The output doesn't include `ReleaseLifecycle` because you didn't set it. The output doesn't include tags.

   If a runtime with the same name already exists in your account and Region, the command fails.

1. Save the value of `Arn` from the output. You use the runtime ARN to grant access to the runtime and to manage its tags. Runtime consumers use it to configure their functions.

1. To verify the runtime, run the `get-runtime` command. You can specify the runtime name or the runtime ARN.

   ```bash
   aws lambda-core get-runtime --runtime-name {{companyphp8}}
   ```

   The output contains the same properties as the output of `create-runtime`.

1. (Optional) To list all runtimes in your account in the current Region, run the `list-runtimes` command.

   ```bash
   aws lambda-core list-runtimes
   ```

   You should see output similar to the following:

   ```json
   {
       "Items": [
           {
               "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
               "Name": "companyphp8",
               "Description": "PHP 8 runtime with company-approved extensions",
               "LicenseInfo": "PHP License v3.01. Includes components under the MIT and Apache-2.0 licenses.",
               "Created": "2026-10-05T17:21:09.112Z",
               "LastModified": "2026-10-05T17:21:09.112Z"
           }
       ]
   }
   ```

   The command returns all runtimes. To limit the output, use `--max-items`.

Your runtime now exists, but functions can't use it yet. Next, create a runtime version and a runtime alias. For more information, see [Next steps](#cmr-create-next-steps).

## Update a runtime
<a name="cmr-create-update"></a>

After you create a runtime, you can update its description, license information, and lifecycle information. You can't change the runtime name. To use a different name, create a new runtime.

When you update a runtime, Lambda changes only the properties that you specify. Properties that you omit keep their current values, except for `ReleaseLifecycle`. The lifecycle that you specify replaces the existing lifecycle. Lambda doesn't merge it field by field. If you omit `ReleaseLifecycle`, Lambda clears the existing lifecycle. To change one lifecycle field, or to keep the lifecycle when you update other properties, specify the complete lifecycle in your request. For more information about lifecycle settings, see [Rules for release states and dates](cmr-lifecycle.md#cmr-lifecycle-consistency).

### Update a runtime (console)
<a name="cmr-create-update-console"></a>

**To update a runtime (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the runtime to update.

1. Choose **Runtime actions**, and then choose **Edit basic information**.

1. Update the **Runtime description**, the **License information**, or both.

1. Choose **Save basic information**.

The **Runtime configuration** panel shows the updated runtime description and license information.

### Update a runtime (AWS CLI)
<a name="cmr-create-update-cli"></a>

**To update a runtime (AWS CLI)**

1. To update the runtime, run the `update-runtime` command. The following example changes the description of the `companyphp8` runtime. The license information doesn't change. The example doesn't include the `--release-lifecycle` option, so it also clears any lifecycle on the runtime. To keep the lifecycle, run the `get-runtime` command to get the current lifecycle. Then pass the complete lifecycle in the `--release-lifecycle` option.

   ```bash
   aws lambda-core update-runtime \
     --runtime-name {{companyphp8}} \
     --description "{{PHP 8 runtime with company-approved extensions and monitoring agent}}"
   ```

   You should see output similar to the following:

   ```json
   {
       "Arn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
       "Name": "companyphp8",
       "Description": "PHP 8 runtime with company-approved extensions and monitoring agent",
       "LicenseInfo": "PHP License v3.01. Includes components under the MIT and Apache-2.0 licenses.",
       "Created": "2026-10-05T17:21:09.112Z",
       "LastModified": "2026-10-05T18:02:44.508Z"
   }
   ```

   To update license information, use the `--license-info` option. To update lifecycle information, use the `--release-lifecycle` option. For examples of lifecycle updates, see [Runtime lifecycle](cmr-lifecycle.md).

1. To verify the change, run the `get-runtime` command and check the updated property and the `LastModified` value.

   ```bash
   aws lambda-core get-runtime --runtime-name {{companyphp8}}
   ```

## Manage runtime tags
<a name="cmr-create-manage-tags"></a>

To add, view, and remove tags on an existing runtime, use the Lambda tagging commands with the runtime ARN. Tags that you add with `tag-resource` are added to any existing tags. If a tag key already exists, the new value replaces the existing value.

**To manage runtime tags (AWS CLI)**

1. To add or change tags, run the `tag-resource` command.

   ```bash
   aws lambda tag-resource \
     --resource {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}} \
     --tags {{CostCenter=1234}}
   ```

   This command doesn't produce any output.

1. To view the tags on the runtime, run the `list-tags` command.

   ```bash
   aws lambda list-tags \
     --resource {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}}
   ```

   You should see output similar to the following:

   ```json
   {
       "Tags": {
           "Team": "platform",
           "Project": "runtimes",
           "CostCenter": "1234"
       }
   }
   ```

1. To remove tags, run the `untag-resource` command with the keys of the tags to remove.

   ```bash
   aws lambda untag-resource \
     --resource {{arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8}} \
     --tag-keys {{CostCenter}}
   ```

   This command doesn't produce any output. To verify that Lambda removed the tag, run the `list-tags` command again.

## Next steps
<a name="cmr-create-next-steps"></a>

After you create a runtime, complete the following tasks to make it available to functions:
+ To build and push a runtime image to Amazon ECR, see [Building runtime images](cmr-building-images.md).
+ To create a runtime version from your image, see [Runtime versions](cmr-versions.md).
+ To create a runtime alias that functions can reference, see [Runtime aliases](cmr-aliases.md).
+ To share the runtime with other accounts, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).