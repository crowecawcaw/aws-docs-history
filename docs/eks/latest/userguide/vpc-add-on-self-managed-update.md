**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Update the Amazon VPC CNI (self-managed add-on)

###### Important

We recommend adding the Amazon EKS type of the add-on to your cluster instead of using the self-managed type of the add-on. If you’re not familiar with the difference between the types, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). For more information about adding an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). If you’re unable to use the Amazon EKS add-on, we encourage you to submit an issue about why you can’t to the [Containers roadmap GitHub repository](https://github.com/aws/containers-roadmap/issues "https://github.com/aws/containers-roadmap/issues").

1. Confirm that you don’t have the Amazon EKS type of the add-on installed on your cluster. Replace `my-cluster` with the name of your cluster.

```
aws eks describe-addon --cluster-name my-cluster --addon-name vpc-cni --query addon.addonVersion --output text
```

If an error message is returned, you don’t have the Amazon EKS type of the add-on installed on your cluster. To self-manage the add-on, complete the remaining steps in this procedure to update the add-on. If a version number is returned, you have the Amazon EKS type of the add-on installed on your cluster. To update it, use the procedure in [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md"), rather than using this procedure. If you’re not familiar with the differences between the add-on types, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). 2. See which version of the container image is currently installed on your cluster.

```
kubectl describe daemonset aws-node --namespace kube-system | grep amazon-k8s-cni: | cut -d : -f 3
```

An example output is as follows.

```
v1.20.0-eksbuild.1
```

Your output might not include the build number. 3. Backup your current settings so you can configure the same settings once you’ve updated your version.

```
kubectl get daemonset aws-node -n kube-system -o yaml > aws-k8s-cni-old.yaml
```

To review the available versions and familiarize yourself with the changes in the version that you want to update to, see [releases](https://github.com/aws/amazon-vpc-cni-k8s/releases "https://github.com/aws/amazon-vpc-cni-k8s/releases") on GitHub. Note that we recommend updating to the same `major`.`minor`.`patch` version listed in the latest available versions table, even if later versions are available on GitHub. For the latest available version table, see [Amazon VPC CNI versions](managing-vpc-cni.md#vpc-cni-latest-available-version "managing-vpc-cni.md#vpc-cni-latest-available-version"). The build versions listed in the table aren’t specified in the self-managed versions listed on GitHub. Update your version by completing the tasks in one of the following options:

    * If you don’t have any custom settings for the add-on, then run the command under the `To apply this release:` heading on GitHub for the [release](https://github.com/aws/amazon-vpc-cni-k8s/releases "https://github.com/aws/amazon-vpc-cni-k8s/releases") that you’re updating to.
    * If you have custom settings, download the manifest file with the following command. Change `https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/v1.20.0/config/master/aws-k8s-cni.yaml` to the URL for the release on GitHub that you’re updating to.



    ```
    curl -O https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/v1.20.3/config/master/aws-k8s-cni.yaml
    ```

    If necessary, modify the manifest with the custom settings from the backup you made in a previous step and then apply the modified manifest to your cluster. If your nodes don’t have access to the private Amazon EKS Amazon ECR repositories that the images are pulled from (see the lines that start with `image:` in the manifest), then you’ll have to download the images, copy them to your own repository, and modify the manifest to pull the images from your repository. For more information, see [Copy a container image from one repository to another repository](copy-image-to-repository.md "copy-image-to-repository.md").



    ```
    kubectl apply -f aws-k8s-cni.yaml
    ```

4. Confirm that the new version is now installed on your cluster.

```
kubectl describe daemonset aws-node --namespace kube-system | grep amazon-k8s-cni: | cut -d : -f 3
```

An example output is as follows.

```
v1.20.3
```

5. (Optional) Install the `cni-metrics-helper` to your cluster. It scrapes elastic network interface and IP address information, aggregates it at a cluster level, and publishes the metrics to Amazon CloudWatch. For more information, see [cni-metrics-helper](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md") on GitHub.
