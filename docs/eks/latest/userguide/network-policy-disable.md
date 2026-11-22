

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disable Kubernetes network policies for Amazon EKS Pod network traffic

Disable Kubernetes network policies to stop restricting Amazon EKS Pod network traffic.

1. List all Kubernetes network policies.

   ```bash
   kubectl get netpol -A
   ```

1. Delete each Kubernetes network policy. You must delete all network policies before disabling network policies.

   ```bash
   kubectl delete netpol <policy-name>
   ```

1. Open the aws-node DaemonSet in your editor.

   ```bash
   kubectl edit daemonset -n kube-system aws-node
   ```

1. Replace the `true` with `false` in the command argument `--enable-network-policy` in the `args:` in the `aws-network-policy-agent` container in the VPC CNI `aws-node` daemonset manifest.

   ```yaml
        - args:
           - --enable-network-policy=false
   ```