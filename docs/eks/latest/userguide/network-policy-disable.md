**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disable Kubernetes network policies for Amazon EKS Pod network traffic

Disable Kubernetes network policies to stop restricting Amazon EKS Pod network traffic

1. List all Kubernetes network policies.

```
kubectl get netpol -A
```

2. Delete each Kubernetes network policy. You must delete all network policies before disabling network policies.

```
kubectl delete netpol <policy-name>
```

3. Open the aws-node DaemonSet in your editor.

```
kubectl edit daemonset -n kube-system aws-node
```

4. Replace the `true` with `false` in the command argument `--enable-network-policy=true` in the `args:` in the `aws-network-policy-agent` container in the VPC CNI `aws-node` daemonset manifest.

```
     - args:
        - --enable-network-policy=true
```
