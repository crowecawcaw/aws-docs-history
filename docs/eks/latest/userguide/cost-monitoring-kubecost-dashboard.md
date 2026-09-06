

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access Kubecost Dashboard
<a name="cost-monitoring-kubecost-dashboard"></a>

## Prerequisites
<a name="kubecost-prereqs-dashboard"></a>

1. Make sure the Kubecost-related Pods' states are "Running".

```
kubectl get pods --namespace kubecost
```

## Access Kubecost Dashboard
<a name="kubecost-dashboard"></a>

1. On your device, enable port-forwarding to expose the Kubecost dashboard.
   + If Kubecost v3 is installed using Helm:

     ```
     kubectl port-forward deployment/kubecost-frontend 9090 --namespace kubecost
     ```
   + If Kubecost v1 or v2 is installed using Helm:

     ```
     kubectl port-forward deployment/kubecost-cost-analyzer 9090 --namespace kubecost
     ```
   + If Kubecost is installed using Amazon EKS add-on:

     ```
     kubectl port-forward deployment/cost-analyzer 9090 --namespace kubecost
     ```

     Alternatively, you can use the [AWS Load Balancer Controller](aws-load-balancer-controller.md) to expose Kubecost and use Amazon Cognito for authentication, authorization, and user management. For more information, see [How to use Application Load Balancer and Amazon Cognito to authenticate users for your Kubernetes web apps](https://aws.amazon.com/blogs/containers/how-to-use-application-load-balancer-and-amazon-cognito-to-authenticate-users-for-your-kubernetes-web-apps).

1. On the same device that you completed the previous step on, open a web browser and enter the following address.

   ```
   http://localhost:9090
   ```

   You see the Kubecost Overview page in your browser. It might take 5–10 minutes (or more) for Kubecost to gather metrics, depending on your cluster size. You can see your Amazon EKS spend, including cumulative cluster costs, associated Kubernetes asset costs, and monthly aggregated spend.

1. To track costs at a cluster level, tag your Amazon EKS resources for billing. For more information, see [Tagging your resources for billing](eks-using-tags.md#tag-resources-for-billing).
   +  **Cost allocation** – View monthly Amazon EKS costs and cumulative costs for each of your namespaces and other dimensions over the past seven days. This is helpful for understanding which parts of your application are contributing to Amazon EKS spend.
   +  **Assets** – View the costs of the AWS infrastructure assets that are associated with your Amazon EKS resources.