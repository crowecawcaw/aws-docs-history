

# Managing cluster extensions

The commands are the same for every extension. Only the extension name and the configuration change. The examples use the observability extension. Before you start, make sure that your cluster meets the [Prerequisites and IAM permissions for cluster extensions](sagemaker-hyperpod-slurm-extensions-prerequisites.md).

## Manage extensions by using the console
<a name="sagemaker-hyperpod-slurm-extensions-manage-manage-extensions-by-using-the-console"></a>

**To install an extension**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On your cluster's details page, choose the **Extensions** tab.

1. On the extension's card, choose **Actions**, and then choose an install option.

For the steps for each extension, see [Installing the observability extension with the console](sagemaker-hyperpod-cluster-observability-slurm-extension.md#sagemaker-hyperpod-cluster-observability-slurm-extension-console) and [Installing the extension](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-installing-the-extension).

The **Extensions** tab shows each extension's status. To see its configuration and health issues, choose **Details** on the card.

**To update or delete an extension**

1. On the extension's card, choose **Actions**, and then choose **Edit**, **Update version**, or **Delete**. You can also use the same buttons on the extension's **Details** page.

1. To delete, type `confirm`, and then choose **Delete**.

The console installs and updates to the latest version of an extension. To choose a specific version, use the AWS CLI.

## Create an extension
<a name="sagemaker-hyperpod-slurm-extensions-manage-create-an-extension"></a>

1. (Optional) Prepare a configuration file in JSON format with the extension's settings. Each extension's configuration page describes its settings. The observability extension can run with all defaults. The user management extension requires a configuration with at least `userSources`.

1. Run `create-cluster-extension` to install the extension.

   ```
   aws sagemaker create-cluster-extension \
      --cluster-arn arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh \
      --extension-name sagemaker-observability \
      --configuration-values file://observability-config.json
   ```

The following list describes the parameters.
+ `--cluster-arn` (required) – The Amazon Resource Name (ARN) of the cluster. A cluster name isn't accepted.
+ `--extension-name` (required) – `sagemaker-observability` or `sagemaker-user-management`.
+ `--extension-version` – The version to install. If you omit it, HyperPod installs the latest version.
+ `--configuration-values` – The settings as a JSON string, or `file://` and a path. The maximum length is 10,240 characters.

This returns the ARN of the new extension. Save it, because the other commands use it. You can also get it at any time from `list-cluster-extensions`.

```
{
    "ExtensionArn": "arn:aws:sagemaker:us-west-2:111122223333:extension/sagemaker-abcd1234efgh/sagemaker-observability/0a1b2c3d4e5f"
}
```

The extension's status is `Creating` while HyperPod installs it on the cluster's nodes. Installation usually starts within a minute and takes a few minutes per node.

## Describe an extension
<a name="sagemaker-hyperpod-slurm-extensions-manage-describe-an-extension"></a>

Run `describe-cluster-extension` to check an extension's version, configuration, and status.

```
aws sagemaker describe-cluster-extension \
    --cluster-arn arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh \
    --extension-arn {{extension-arn}}
```

The response shows the extension's version, status, and configuration, and the node counts in `NodeSummary`. If some nodes have a problem, it also contains `Health`. For what each code means and how to retry, see [Health issues](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-health-issues).

**Tip**  
To see only the status, node counts, and health issues, add `--query '{Status: ExtensionDetails.Status, Nodes: NodeSummary, Health: Health}'`. Polling every 30–60 seconds is enough.

## List the extensions on a cluster
<a name="sagemaker-hyperpod-slurm-extensions-manage-list-the-extensions-on-a-cluster"></a>

Run `list-cluster-extensions` to list the extensions on a cluster.

```
aws sagemaker list-cluster-extensions \
    --cluster-arn arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh
```

The response lists each extension's ARN, name, version, and status.

## Update an extension
<a name="sagemaker-hyperpod-slurm-extensions-manage-update-an-extension"></a>

Run `update-cluster-extension` to change an extension's configuration or version. Send only the settings that you want to change. For how the change is merged, see [Updates](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-updates).

```
aws sagemaker update-cluster-extension \
    --cluster-arn arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh \
    --extension-arn {{extension-arn}} \
    --configuration-values '{"metricsProvider":{"acceleratedComputeMetrics":{"level":"ADVANCED"}}}'
```

The status is `Updating` while HyperPod applies the change, and returns to `Active` when every node has it. The following list describes update behavior.
+ To return a setting to its default value, set it to `null`.
+ To move to a later version, add `--extension-version`. You can't move to an earlier version.
+ You can update an extension in any status except `Deleting`. A newer request replaces one that's still in progress.
+ An update that doesn't change the version or configuration retries the nodes where an install or update failed. For more information, see [Retrying failed nodes](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-retrying-failed-nodes).
+ If the request fails with `Failure due to concurrent operations. Please try again`, retry it.

## Delete an extension
<a name="sagemaker-hyperpod-slurm-extensions-manage-delete-an-extension"></a>

Run `delete-cluster-extension` to remove an extension from a cluster.

```
aws sagemaker delete-cluster-extension \
    --cluster-arn arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh \
    --extension-arn {{extension-arn}}
```

The status is `Deleting` until HyperPod removes the extension from every node. You can delete an extension in any status. Metrics that the observability extension already sent aren't deleted. The user management extension keeps users, groups, and home directories on the nodes, but SSH is no longer limited to the groups that you granted, so remove users first, as described in [Delete the extension](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-delete-the-extension). To install an extension again, wait until it no longer appears in `list-cluster-extensions`. Deleting a cluster deletes its extensions.

## List the available versions of an extension
<a name="sagemaker-hyperpod-slurm-extensions-manage-list-the-available-versions-of-an-extension"></a>

Run `list-cluster-extension-versions` to list the versions of an extension that you can install, from highest to lowest.

```
aws sagemaker list-cluster-extension-versions \
    --extension-name sagemaker-observability
```

```
{
    "ExtensionVersions": [
        { "ExtensionVersion": "1.0.0" }
    ]
}
```

Use a version from the list as `--extension-version`. Versions that HyperPod no longer offers don't appear.

## Request limits
<a name="sagemaker-hyperpod-slurm-extensions-manage-request-limits"></a>

The following table lists the request limits for the cluster extension APIs.


| API | Requests per second, per account | 
| --- | --- | 
| CreateClusterExtension, UpdateClusterExtension, DeleteClusterExtension | 1 | 
| DescribeClusterExtension | 5 (burst 100) | 
| ListClusterExtensions | 2 (burst 10) | 
| ListClusterExtensionVersions | 2 (burst 10) | 

## Troubleshooting
<a name="sagemaker-hyperpod-slurm-extensions-manage-troubleshooting"></a>

### The request fails with ValidationException
<a name="sagemaker-hyperpod-slurm-extensions-manage-the-request-fails-with-validationexception"></a>

The following table lists the validation errors and how to resolve them.


| Message | Resolution | 
| --- | --- | 
| … is only supported for cluster with NodeProvisioningMode set to Continuous | Use a cluster with continuous provisioning. | 
| Cluster extensions are only supported for Slurm clusters | Cluster extensions aren't available for clusters orchestrated by Amazon Elastic Kubernetes Service (Amazon EKS). | 
| Cluster extensions are not supported on instance groups that use a custom AMI … | Use the SageMaker HyperPod default AMI for every instance group. | 
| AMI … is too old to install cluster extensions … or AMI … used by the cluster's instance groups could not be found … | Run update-cluster-software to move the cluster to the latest default AMI, and then create the extension. | 
| Extension … is not available in the extension catalog | Check the extension name and version. To see the versions that you can install, run list-cluster-extension-versions. | 
| ConfigurationValues must be a valid JSON object | Pass a JSON object, not an array, string, or YAML. If you use file://, make sure that the file contains valid JSON. | 
| ConfigurationValues does not match the schema … | Fix each setting that the message lists. For more information, see the extension's configuration page. | 
| Cannot downgrade extension … | Delete the extension, and create it again with the version that you want. | 
| Extension … is being deleted and cannot be updated | Wait until the deletion completes, and then create the extension again. | 
| The sagemaker-observability extension cannot be created for this account because it is onboarded to on-AMI observability … | Contact AWS Support to move off on-AMI observability. Other extensions aren't affected. | 

### CreateClusterExtension fails with ResourceInUse
<a name="sagemaker-hyperpod-slurm-extensions-manage-createclusterextension-fails-with-resourceinuse"></a>

The cluster already has an extension with this name, or one with this name is still being deleted. Run `list-cluster-extensions`. If the extension's status is `Deleting`, wait until it no longer appears in the list.

### DescribeClusterExtension returns ResourceNotFound
<a name="sagemaker-hyperpod-slurm-extensions-manage-describeclusterextension-returns-resourcenotfound"></a>

The ARN belongs to an extension that was deleted. When you delete an extension and create it again, the new extension has a new ARN. Get the current ARN from `list-cluster-extensions`.

### The request fails with AccessDeniedException
<a name="sagemaker-hyperpod-slurm-extensions-manage-the-request-fails-with-accessdeniedexception"></a>

Make sure that your policy allows the action on both the cluster ARN and the extension ARN. `ListClusterExtensions` needs only the cluster ARN, and `ListClusterExtensionVersions` needs `*`. Use `*` for the last part of the extension ARN. For more information, see [Prerequisites and IAM permissions for cluster extensions](sagemaker-hyperpod-slurm-extensions-prerequisites.md).