

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Verify Amazon EKS add-on version compatibility with a cluster
<a name="addon-compat"></a>

Before you create an Amazon EKS add-on you need to verify that the Amazon EKS add-on version is compatible with your cluster.

Use the [describe-addon-versions API](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html) to list the available versions of EKS add-ons, and which Kubernetes versions each addon version supports.

1. Verify the AWS CLI is installed and working with `aws sts get-caller-identity`. If this command doesn’t work, learn how to [Get started with the AWS CLI.](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) 

1. Determine the name of the add-on you want to retrieve version compatibility information for, such as `amazon-cloudwatch-observability`.

1. Determine the Kubernetes version of your cluster, such as `1.36`.

1. Use the AWS CLI to retrieve the addon versions that are compatible with the Kubernetes version of your cluster.

   ```
   aws eks describe-addon-versions --addon-name amazon-cloudwatch-observability --kubernetes-version 1.36
   ```

   An example output is as follows.

   ```
   {
       "addons": [
           {
               "addonName": "amazon-cloudwatch-observability",
               "type": "observability",
               "addonVersions": [
                   {
                       "addonVersion": "vX.X.X-eksbuild.X",
                       "architecture": [
                           "amd64",
                           "arm64"
                       ],
                       "computeTypes": [
                           "ec2",
                           "auto",
                           "hybrid"
                       ],
                       "compatibilities": [
                           {
                               "clusterVersion": "1.36",
                               "platformVersions": [
                                   "*"
                               ],
                               "defaultVersion": true
                           }
                       ],
                   }
               ]
           }
       ]
   }
   ```

   This output shows that addon version `vX.X.X-eksbuild.X` is compatible with Kubernetes cluster version `1.36`.

## Add-on compatibility with compute types
<a name="_add_on_compatibility_with_compute_types"></a>

The `computeTypes` field in the `describe-addon-versions` output indicates an add-on’s compatibility with EKS Auto Mode Managed Nodes or Hybrid Nodes. Add-ons marked `auto` work with EKS Auto Mode’s cloud-based, AWS-managed infrastructure, while those marked `hybrid` can run on on-premises nodes connected to the EKS cloud control plane.

For more information, see [Considerations for Amazon EKS Auto Mode](eks-add-ons.md#addon-consider-auto).