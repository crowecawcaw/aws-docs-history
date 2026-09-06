

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Harden Kubernetes RBAC in Amazon EKS
<a name="rbac-hardening"></a>

Kubernetes role-based access control (RBAC) controls what actions identities can perform inside a cluster. Many cluster components, including CSI drivers and other add-ons installed as DaemonSets, require broad permissions to function. Reviewing and scoping these permissions reduces the potential scope of any unintended access.

This topic describes the permission considerations for common cluster components and the recommended controls.

## DaemonSet service account permissions
<a name="_daemonset_service_account_permissions"></a>

DaemonSet Pods run on every node in the cluster, so their service account tokens and the RBAC permissions those tokens grant are present on every node.

An unauthorized process on a node may be able to access the service account tokens of other Pods running on the same node, including DaemonSet Pods. The RBAC permissions granted to DaemonSet service accounts are the same on every node in the cluster.

Components commonly deployed as DaemonSets include:
+ CSI node drivers (`ebs-csi-node`, `efs-csi-node`, `mountpoint-s3-csi-node`)
+ The Amazon VPC CNI plugin (`aws-node`)
+  `kube-proxy` 

If a DaemonSet Pod has AWS IAM credentials through EKS Pod Identity or IAM Roles for Service Accounts (IRSA), a process that gains access outside its container on the same node may also access those credentials. This extends the scope of impact beyond Kubernetes RBAC to any AWS API permissions granted to a DaemonSet’s IAM role.

**Important**  
When reviewing permissions, treat the Kubernetes RBAC permissions and the IAM permissions of every DaemonSet service account as accessible from every node in the cluster.

## CSI driver RBAC scope
<a name="_csi_driver_rbac_scope"></a>

CSI drivers commonly hold broad RBAC grants because they interact with nodes, persistent volumes, and storage APIs.

### Node object permissions
<a name="_node_object_permissions"></a>

CSI drivers may require RBAC permissions to modify Node objects to support features such as taint removal or other node management tasks. Due to Kubernetes RBAC limitations, these permissions apply to *all* Node objects in the cluster, not only the local node the driver is running on.

For the EBS CSI driver, the Helm chart provides a parameter (`node.serviceAccount.disableMutation`) that removes the node modification permission from the `ebs-csi-node` service account. Enabling this disables the taint removal feature.

### Service account token exposure
<a name="_service_account_token_exposure"></a>

CSI driver Pods may use projected service account tokens for authentication. On a node where an unauthorized process has gained access outside its container, those tokens may be accessible through the container filesystem or the kubelet API. If the service account is also associated with an IAM role through EKS Pod Identity or IRSA, an exposed token can be used to obtain AWS IAM credentials.

## Recommended controls
<a name="_recommended_controls"></a>

### Scope RBAC to least privilege
<a name="_scope_rbac_to_least_privilege"></a>
+ Review the ClusterRoles bound to CSI driver and DaemonSet service accounts. Remove permissions that are not required for your workloads.
+ For the EBS CSI driver, set `node.serviceAccount.disableMutation` to `true` if you don’t use the taint removal feature.
+ Use `kubectl auth can-i --list --as=system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT` to audit effective permissions.

### Enforce Pod security standards
<a name="_enforce_pod_security_standards"></a>

Apply the [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) using the built-in Pod Security Admission controller or a policy engine. At minimum, enforce the `baseline` profile cluster-wide and the `restricted` profile for workload namespaces. This limits the ability to create privileged containers outside of system namespaces.

### Use network policies
<a name="_use_network_policies"></a>

Apply network policies to restrict egress from CSI driver and DaemonSet Pods to only the endpoints they need (for example, the Kubernetes API server and AWS service endpoints). This reduces the scope of actions possible.

### Monitor RBAC activity
<a name="_monitor_rbac_activity"></a>

Enable Kubernetes audit logging and monitor for unexpected API calls from DaemonSet service accounts. Look for:
+ Node modifications from CSI driver service accounts
+ Pod creation in system namespaces
+ Unusual `get` or `list` calls on Secrets

For more information, see [Send control plane logs to CloudWatch Logs](control-plane-logs.md).