

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot local Amazon EKS clusters on AWS Outposts configured with EC2 instance store
<a name="eks-outposts-instance-store-troubleshooting"></a>

This topic covers common errors that you might see while using local Amazon EKS clusters on AWS Outposts configured with EC2 instance store and how to troubleshoot them.

## `kubectl` not working after configuring `kubeconfig`
<a name="eks-outposts-instance-store-troubleshooting-kubectl"></a>

If you see the following error after running `aws eks update-kubeconfig`:

```
Either parameter --cluster-name or --cluster-id must be specified.
```

Or:

```
couldn't get current server API group list: getting credentials: exec: executable aws failed with exit code 1
```

Verify that your `kubeconfig` (`~/.kube/config`) specifies `--cluster-name` in the `exec` args, not `--cluster-id`:

```
      args:
        - --region
        - region-code
        - eks
        - get-token
        - --cluster-name
        - my-cluster
        - --output
        - json
      command: aws
```

## Nodes not joining the cluster
<a name="eks-outposts-instance-store-troubleshooting-nodes-not-joining"></a>

If your nodes don’t appear when you run `kubectl get nodes`:

1.  **Check `kubelet` logs on the node.** Access the node with SSM or SSH and run:

   ```
   systemctl status kubelet -l
   ```

1.  **Check for unauthorized errors.** Unauthorized errors can indicate missing node role permissions or `aws-auth` ConfigMap issues. Verify that the node’s instance role is correctly mapped in the `aws-auth` ConfigMap.

1.  **Check CSR status.** Verify that the node’s certificate signing request was approved:

   ```
   kubectl get csr
   ```

   If the CSR is in `Pending` state, approve it:

   ```
   kubectl certificate approve node-csr-EXAMPLE
   ```

## Cluster stuck in `CREATING` state
<a name="eks-outposts-instance-store-troubleshooting-creating"></a>

If your cluster enters FAILED status:
+  **Insufficient capacity:** Verify that your Outpost has sufficient virtualized capacity for 6 control plane instances (3 `etcd` \+ 3 API server) of the specified instance types. The instance types must be slotted on your Outpost.
+  **Spread topology can’t be met:** If you specified a `spreadLevel` of `host`, verify that at least 3 hosts are configured with the chosen instance type. If you specified `rack`, verify that at least 3 racks have hosts with the chosen instance type.
+  **Subnet issues:** Verify that the subnets you specified are in the Availability Zone to which the Outpost is homed, and that each subnet has at least 3 available IP addresses. See [Create a VPC and subnets for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-vpc-subnet-requirements.md).

## Cluster stuck in `UPDATING` state
<a name="eks-outposts-instance-store-troubleshooting-updating"></a>

If your cluster remains in the `UPDATING` state during a Kubernetes version or platform version update:
+  **Insufficient capacity:** During updates, control plane instances are deleted before re-instantiation. If the freed capacity is consumed by another workload before the replacement instance can be provisioned, the update stalls. Verify that your Outpost has available capacity for the control plane instance types.

## `etcd` quorum loss
<a name="eks-outposts-instance-store-troubleshooting-etcd-quorum"></a>

If you lose the ability to perform Kubernetes API operations and your Outpost is disconnected:
+  `etcd` may have lost quorum. This occurs if more than one `etcd` instance becomes unavailable during a disconnect.
+ Workloads that are already running continue to operate, but Kubernetes API operations are unavailable.
+ When connectivity is restored, Amazon EKS will recover your cluster state from the most recent `etcd` snapshot.

Contact [AWS Support Center](https://console.aws.amazon.com/support/home).