

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Change authentication mode to use access entries
<a name="setting-up-access-entries"></a>

To begin using access entries, you must change the authentication mode of the cluster to either the `API_AND_CONFIG_MAP` or `API` modes. This adds the API for access entries.

## AWS Console
<a name="access-entries-setup-console"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of the cluster that you want to create an access entry in.

1. Choose the **Access** tab.

1. The **Authentication mode** shows the current authentication mode of the cluster. If the mode says EKS API, you can already add access entries and you can skip the remaining steps.

1. Choose **Manage access**.

1. For **Cluster authentication mode**, select a mode with the EKS API. Note that you can’t change the authentication mode back to a mode that removes the EKS API and access entries.

1. Choose **Save changes**. Amazon EKS begins to update the cluster, the status of the cluster changes to Updating, and the change is recorded in the **Update history** tab.

1. Wait for the status of the cluster to return to Active. When the cluster is Active, you can follow the steps in [Create access entries](creating-access-entries.md) to add access to the cluster for IAM principals.

## AWS CLI
<a name="access-setup-cli"></a>

1. Install the AWS CLI, as described in [Installing](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the * AWS Command Line Interface User Guide*.

1. Run the following command. Replace {{my-cluster}} with the name of your cluster. If you want to disable the `ConfigMap` method permanently, replace `API_AND_CONFIG_MAP` with `API`.

   Amazon EKS begins to update the cluster, the status of the cluster changes to UPDATING, and the change is recorded in the ** aws eks list-updates **.

   ```
   aws eks update-cluster-config --name my-cluster --access-config authenticationMode=API_AND_CONFIG_MAP
   ```

1. Wait for the status of the cluster to return to Active. When the cluster is Active, you can follow the steps in [Create access entries](creating-access-entries.md) to add access to the cluster for IAM principals.

## Required platform version
<a name="_required_platform_version"></a>

To use *access entries*, the cluster must have a platform version that is the same or later than the version listed in the following table, or a Kubernetes version that is later than the versions listed in the table. If your Kubernetes version is not listed, all platform versions support access entries.


| Kubernetes version | Platform version | 
| --- | --- | 
| Not Listed | All Supported | 
|  `1.30`  |  `eks.2`  | 
|  `1.29`  |  `eks.1`  | 
|  `1.28`  |  `eks.6`  | 

For more information, see [platform-versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html).