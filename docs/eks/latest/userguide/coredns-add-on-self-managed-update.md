**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Update the CoreDNS Amazon EKS self-managed add-on

###### Important

We recommend adding the Amazon EKS type of the add-on to your cluster instead of using the self-managed type of the add-on. If you’re not familiar with the difference between the types, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). For more information about adding an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). If you’re unable to use the Amazon EKS add-on, we encourage you to submit an issue about why you can’t to the [Containers roadmap GitHub repository](https://github.com/aws/containers-roadmap/issues "https://github.com/aws/containers-roadmap/issues").

Before you begin, review the upgrade considerations. For more information, see [Important CoreDNS upgrade considerations](managing-coredns.md#coredns-upgrade "managing-coredns.md#coredns-upgrade").

1. Confirm that you have the self-managed type of the add-on installed on your cluster. Replace `my-cluster` with the name of your cluster.

```
aws eks describe-addon --cluster-name my-cluster --addon-name coredns --query addon.addonVersion --output text
```

If an error message is returned, you have the self-managed type of the add-on installed on your cluster. Complete the remaining steps in this procedure. If a version number is returned, you have the Amazon EKS type of the add-on installed on your cluster. To update the Amazon EKS type of the add-on, use the procedure in [Update the CoreDNS Amazon EKS add-on](coredns-add-on-update.md "coredns-add-on-update.md"), rather than using this procedure. If you’re not familiar with the differences between the add-on types, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). 2. See which version of the container image is currently installed on your cluster.

```
kubectl describe deployment coredns -n kube-system | grep Image | cut -d ":" -f 3
```

An example output is as follows.

```
v1.8.7-eksbuild.2
```

3. If your current CoreDNS version is `v1.5.0` or later, but earlier than the version listed in the [CoreDNS versions](managing-coredns.md#coredns-versions "managing-coredns.md#coredns-versions") table, then skip this step. If your current version is earlier than `1.5.0`, then you need to modify the `ConfigMap` for CoreDNS to use the forward add-on, rather than the proxy add-on.
   1. Open the `ConfigMap` with the following command.

   ```
   kubectl edit configmap coredns -n kube-system
   ```

   2. Replace `proxy` in the following line with `forward`. Save the file and exit the editor.

   ```
   proxy . /etc/resolv.conf
   ```

4. If you originally deployed your cluster on Kubernetes `1.17` or earlier, then you may need to remove a discontinued line from your CoreDNS manifest.

###### Important

You must complete this step before updating to CoreDNS version `1.7.0`, but it’s recommended that you complete this step even if you’re updating to an earlier version.

    1. Check to see if your CoreDNS manifest has the line.



    ```
    kubectl get configmap coredns -n kube-system -o jsonpath='{$.data.Corefile}' | grep upstream
    ```

    If no output is returned, your manifest doesn’t have the line and you can skip to the next step to update CoreDNS. If output is returned, then you need to remove the line.
    2. Edit the `ConfigMap` with the following command, removing the line in the file that has the word `upstream` in it. Do not change anything else in the file. Once the line is removed, save the changes.



    ```
    kubectl edit configmap coredns -n kube-system -o yaml
    ```

5. Retrieve your current CoreDNS image version:

```
kubectl describe deployment coredns -n kube-system | grep Image
```

An example output is as follows.

```
602401143452.dkr.ecr.region-code.amazonaws.com/eks/coredns:v1.8.7-eksbuild.2
```

6. If you’re updating to CoreDNS `1.8.3` or later, then you need to add the `endpointslices` permission to the `system:coredns` Kubernetes `clusterrole`.

```
kubectl edit clusterrole system:coredns -n kube-system
```

Add the following lines under the existing permissions lines in the `rules` section of the file.

```
[...]
- apiGroups:
  - discovery.k8s.io
  resources:
  - endpointslices
  verbs:
  - list
  - watch
[...]
```

7. Update the CoreDNS add-on by replacing `602401143452` and `region-code` with the values from the output returned in a previous step. Replace `v1.11.3-eksbuild.1` with the CoreDNS version listed in the [latest versions table](managing-coredns.md#coredns-versions "managing-coredns.md#coredns-versions") for your Kubernetes version.

```
kubectl set image deployment.apps/coredns -n kube-system  coredns=602401143452.dkr.ecr.region-code.amazonaws.com/eks/coredns:v1.11.3-eksbuild.1
```

An example output is as follows.

```
deployment.apps/coredns image updated
```

8. Check the container image version again to confirm that it was updated to the version that you specified in the previous step.

```
kubectl describe deployment coredns -n kube-system | grep Image | cut -d ":" -f 3
```

An example output is as follows.

```
v1.11.3-eksbuild.1
```
