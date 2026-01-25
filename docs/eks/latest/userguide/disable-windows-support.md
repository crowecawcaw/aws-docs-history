**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disable Windows support

1. If your cluster contains Amazon Linux nodes and you use [security groups for Pods](security-groups-for-pods.md "security-groups-for-pods.md") with them, then skip this step.

Remove the `AmazonVPCResourceController` managed IAM policy from your [cluster role](cluster-iam-role.md "cluster-iam-role.md"). Replace `eksClusterRole` with the name of your cluster role.

```
aws iam detach-role-policy \
    --role-name eksClusterRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonEKSVPCResourceController
```

2. Disable Windows IPAM in the `amazon-vpc-cni` ConfigMap.

```
kubectl patch configmap/amazon-vpc-cni \
                    -n kube-system \
                    --type merge \
                    -p '{"data":{"enable-windows-ipam":"false"}}'
```
