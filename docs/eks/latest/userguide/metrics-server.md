**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View resource usage with the Kubernetes Metrics Server

The Kubernetes Metrics Server is an aggregator of resource usage data in your cluster, and it isn’t deployed by default in Amazon EKS clusters. For more information, see [Kubernetes Metrics Server](https://github.com/kubernetes-sigs/metrics-server "https://github.com/kubernetes-sigs/metrics-server") on GitHub. The Metrics Server is commonly used by other Kubernetes add ons, such as the [Scale pod deployments with Horizontal Pod Autoscaler](horizontal-pod-autoscaler.md "horizontal-pod-autoscaler.md") or the [Kubernetes Dashboard](eks-managing.md "eks-managing.md"). For more information, see [Resource metrics pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/ "https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/") in the Kubernetes documentation. This topic explains how to deploy the Kubernetes Metrics Server on your Amazon EKS cluster.

###### Important

The metrics are meant for point-in-time analysis and aren’t an accurate source for historical analysis. They can’t be used as a monitoring solution or for other non-auto scaling purposes. For information about monitoring tools, see [Monitor your cluster performance and view logs](eks-observe.md "eks-observe.md").

## Considerations

- If manually deploying Kubernetes Metrics Server onto Fargate nodes using the manifest, configure the `metrics-server` deployment to use a port other than its default of `10250`. This port is reserved for Fargate. The Amazon EKS add-on version of Metrics Server is pre-configured to use port `10251`.
- Ensure security groups and network ACLs allow port `10250` between the `metrics-server` Pods and all other nodes and Pods. The Kubernetes Metrics Server still uses port `10250` to collect metrics from other endpoints in the cluster. If you deploy on Fargate nodes, allow both the configured alternate Metrics Server port and port `10250`.

## Deploy as community add-on with Amazon EKS Add-ons

**New: You can now deploy Metrics Server as a community add-on using the AWS console or Amazon EKS APIs.**

### Deploy with AWS console

1. Open your EKS cluster in the AWS console
2. From the "Add-ons" tab, select **Get More Add-ons**.
3. From the "Community add-ons" section, select **Metrics Server** and then **Next**
4. EKS determines the appropriate version of the add-on for your cluster. You can change the version using the **Version** dropdown menu.
5. Select **Next** and then **Create** to install the add-on.

### Additional resources

Learn more about [Community add-ons](community-addons.md "community-addons.md").

You install or update community add-ons in the same way as other Amazon EKS Add-ons.

- [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md")
- [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md")
- [Remove an Amazon EKS add-on from a cluster](removing-an-add-on.md "removing-an-add-on.md")

## Deploy with manifest

**New: You can now deploy Metrics Server as a community add-on using the AWS console or Amazon EKS APIs. These manifest install instructions will be archived.**

1. Deploy the Metrics Server with the following command:

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

If you are using Fargate, you will need to change this file. In the default configuration, the metrics server uses port 10250. This port is reserved on Fargate. Replace references to port 10250 in components.yaml with another port, such as 10251. 2. Verify that the `metrics-server` deployment is running the desired number of Pods with the following command.

```
kubectl get deployment metrics-server -n kube-system
```

An example output is as follows.

```
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
metrics-server   1/1     1            1           6m
```

3. Test the metrics server is working by displaying resource (CPU/memory) usage of nodes.

```
kubectl top nodes
```

4. If you receive the error message `Error from server (Forbidden)`, you need to update your Kubernetes RBAC configuration. Your Kubernetes RBAC identity needs sufficent permissions to read cluster metrics. Review the [minimum required Kubernetes API permissions for reading metrics](https://github.com/kubernetes-sigs/metrics-server/blob/e285375a49e3bf77ddd78c08a05aaa44f2249ebd/manifests/base/rbac.yaml#L5C9-L5C41 "https://github.com/kubernetes-sigs/metrics-server/blob/e285375a49e3bf77ddd78c08a05aaa44f2249ebd/manifests/base/rbac.yaml#L5C9-L5C41") on GitHub. Learn how to [grant AWS IAM Identities such as Roles access to Kubernetes APIs](grant-k8s-access.md#authentication-modes "grant-k8s-access.md#authentication-modes").
