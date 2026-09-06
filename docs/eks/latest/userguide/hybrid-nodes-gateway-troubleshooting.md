

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Hybrid Nodes gateway troubleshooting
<a name="hybrid-nodes-gateway-troubleshooting"></a>

This page provides guidance for diagnosing and resolving common issues with the Amazon EKS Hybrid Nodes gateway. Each section describes a symptom, possible causes, diagnostic steps, and resolutions. For operational details, see [Amazon EKS Hybrid Nodes gateway operations](hybrid-nodes-gateway-operations.md).

## Pods on hybrid nodes unreachable from VPC
<a name="hybrid-nodes-gateway-ts-unreachable"></a>

Pods running on hybrid nodes are not reachable from resources in the VPC, such as EC2 instances, load balancers, or the Kubernetes control plane.

 **Possible causes:** 
+ VPC route table entries are missing or point to the wrong ENI.
+ The gateway leader pod is not running or has not completed setup.
+ Cilium VTEP is not enabled or configured on the hybrid nodes.
+ Source/destination check is enabled on the gateway EC2 instance.

 **Diagnostic steps:** 

1.  **Check VPC route table entries.** Verify that routes for your hybrid pod CIDRs exist and point to the active gateway instance’s primary ENI:

   ```
   aws ec2 describe-route-tables \
     --route-table-ids {{ROUTE_TABLE_ID}} \
     --query "RouteTables[].Routes[?DestinationCidrBlock=='POD_CIDR']"
   ```

   If routes are missing, check the gateway logs for route table errors. If routes point to the wrong ENI, a failover may not have completed successfully.

1.  **Check gateway pod status and leader election.** Confirm that two gateway pods are running and one holds the leader lease:

   ```
   kubectl get pods -n eks-hybrid-nodes-gateway
   kubectl get lease -n eks-hybrid-nodes-gateway
   ```

   If no pod holds the lease, see [Leader election issues](#hybrid-nodes-gateway-ts-leader).

1.  **Check Cilium VTEP configuration on hybrid nodes.** Verify that the `CiliumVTEPConfig` resource exists and contains the leader’s node IP:

   ```
   kubectl get ciliumvtepconfig hybrid-gateway -o yaml
   ```

   The `spec.endpoints[0].tunnelEndpoint` should match the leader gateway node’s IP address. If the resource is missing or has a stale IP, the gateway may not have completed leader setup.

1.  **Check source/destination check.** Verify that source/destination check is disabled on the gateway EC2 instances:

   ```
   aws ec2 describe-instance-attribute \
     --instance-id {{GATEWAY_INSTANCE_ID}} \
     --attribute sourceDestCheck
   ```

   If `sourceDestCheck` is `true`, disable it. See [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md).

## Webhook calls to hybrid nodes fail
<a name="hybrid-nodes-gateway-ts-webhooks"></a>

The Kubernetes API server cannot reach webhook endpoints running on hybrid nodes. Webhook admission requests time out or return connection errors.

 **Possible causes:** 
+ The gateway is not routing traffic from the control plane to hybrid pods.
+ The `CiliumVTEPConfig` resource is missing or has a stale endpoint IP.

 **Diagnostic steps:** 

1.  **Verify the control plane can reach the gateway node IP.** The control plane sends traffic to the VPC route table, which forwards it to the gateway’s ENI. Confirm the VPC route table entries are correct using the steps in [Pods on hybrid nodes unreachable from VPC](#hybrid-nodes-gateway-ts-unreachable).

1.  **Check the CiliumVTEPConfig resource.** Verify the resource exists and the `tunnelEndpoint` matches the current leader’s node IP:

   ```
   kubectl get ciliumvtepconfig hybrid-gateway -o yaml
   ```

   If the tunnel endpoint is stale (points to a previous leader), the gateway may not have completed the leader setup sequence. Check the gateway logs for errors during `CiliumVTEPConfig` upsert.

## VPC route table updates fail
<a name="hybrid-nodes-gateway-ts-routes"></a>

The gateway logs show errors related to VPC route table operations, and routes for hybrid pod CIDRs are not created or updated.

 **Possible causes:** 
+ The gateway’s IAM role does not have the required EC2 permissions.
+ The route table IDs in the configuration are incorrect or the route tables do not exist.
+ The gateway cannot reach the EC2 API endpoint.

 **Diagnostic steps:** 

1.  **Verify IAM permissions.** The gateway requires the following IAM actions:
   +  `ec2:DescribeRouteTables` 
   +  `ec2:CreateRoute` 
   +  `ec2:ReplaceRoute` 
   +  `ec2:DescribeInstances` 

     Check the IAM role attached to the gateway node’s instance profile or pod identity configuration.

1.  **Check route table IDs in the configuration.** Verify that the `ROUTE_TABLE_IDS` environment variable contains valid route table IDs in the gateway deployment:

   ```
   kubectl get deployment eks-hybrid-nodes-gateway -n eks-hybrid-nodes-gateway -o jsonpath='{.spec.template.spec.containers[0].env}' | jq .
   ```

   Confirm the route table IDs exist in your VPC:

   ```
   aws ec2 describe-route-tables --route-table-ids {{ROUTE_TABLE_ID}}
   ```

1.  **Check gateway logs for route table errors.** Look for error messages related to route table operations:

   ```
   kubectl logs -n eks-hybrid-nodes-gateway {{LEADER_POD}} | grep -i "route table"
   ```

   Common error messages include:
   +  `Failed to verify route table access` — The gateway cannot describe the route table. Check IAM permissions and route table IDs.
   +  `Failed to update route tables` — The gateway cannot create or replace routes. Check IAM permissions.
   +  `failed to access route table` — The route table ID may be incorrect or the IAM role lacks `ec2:DescribeRouteTables`.

## Gateway pods fail to start or are unhealthy
<a name="hybrid-nodes-gateway-ts-pods"></a>

Gateway pods are in `CrashLoopBackOff`, `Error`, or `Pending` state, or the health endpoint returns an error.

 **Possible causes:** 
+ Required environment variables (`VPC_CIDR`, `POD_CIDRS`, `ROUTE_TABLE_IDS`) are not set.
+ IP forwarding is not enabled on the gateway node.
+ Node label or anti-affinity constraints prevent scheduling.

 **Diagnostic steps:** 

1.  **Check pod logs.** View the logs for the failing pod to identify the error:

   ```
   kubectl logs -n eks-hybrid-nodes-gateway {{LEADER_POD}}
   ```

1.  **Check required environment variables.** The gateway requires `NODE_IP`, `VPC_CIDR`, and `POD_CIDRS`. If any are missing, the gateway exits immediately. Verify the pod spec:

   ```
   kubectl get pod -n eks-hybrid-nodes-gateway {{LEADER_POD}} -o jsonpath='{.spec.containers[0].env}' | jq .
   ```
   +  `NODE_IP` is set automatically from `status.hostIP` in the pod spec. If it is empty, the pod may not be scheduled on a node yet.
   +  `VPC_CIDR` and `POD_CIDRS` come from the Helm values. Verify they are set correctly.

1.  **Check IP forwarding.** The gateway checks that IP forwarding is enabled at startup and exits if it is not. Look for the error message `IP forwarding is not enabled` in the pod logs. Enable IP forwarding on the node:

   ```
   # Check current setting
   cat /proc/sys/net/ipv4/ip_forward
   
   # Enable if not set
   sudo sysctl -w net.ipv4.ip_forward=1
   ```

   For a persistent setting, configure IP forwarding through the kubelet or add `net.ipv4.ip_forward=1` to `/etc/sysctl.d/`.

1.  **Check node label and scheduling constraints.** The gateway pods require nodes with the `hybrid-gateway-node=true` label. Pod anti-affinity ensures each pod runs on a separate node. If pods are `Pending`, check for scheduling issues:

   ```
   kubectl describe pod -n eks-hybrid-nodes-gateway {{LEADER_POD}}
   ```

   Look for events indicating insufficient nodes, missing labels, or anti-affinity conflicts.

## Leader election issues
<a name="hybrid-nodes-gateway-ts-leader"></a>

The gateway pods are running but no pod acquires the leader lease, or leadership transitions happen frequently.

 **Possible causes:** 
+ RBAC permissions for Lease objects are missing.
+ Network connectivity between gateway pods and the Kubernetes API server is unreliable.
+ Leader election parameters are misconfigured.

 **Diagnostic steps:** 

1.  **Check the Lease object.** Verify the Lease exists and inspect its current holder:

   ```
   kubectl get lease -n eks-hybrid-nodes-gateway hybrid-gateway-leader -o yaml
   ```

   The `spec.holderIdentity` field shows the current leader. The `spec.renewTime` shows when the lease was last renewed. If `renewTime` is stale, the leader may have lost connectivity to the API server.

1.  **Check RBAC permissions.** The gateway service account needs permissions to get, create, and update Lease objects in the gateway namespace. Verify the Role and RoleBinding:

   ```
   kubectl get role -n eks-hybrid-nodes-gateway
   kubectl get rolebinding -n eks-hybrid-nodes-gateway
   ```

   The Role should include `get`, `create`, and `update` verbs for the `leases` resource in the `coordination.k8s.io` API group.

1.  **Check pod logs for lease errors.** Look for leader election errors in the pod logs:

   ```
   kubectl logs -n eks-hybrid-nodes-gateway {{LEADER_POD}} | grep -i "leader\|lease"
   ```

   Common issues include:
   +  `Failed to acquire lease` — The pod cannot create or update the Lease object. Check RBAC permissions.
   + Frequent `Leadership ended` followed by `Leader setup complete` messages — The leader is losing and re-acquiring the lease. This may indicate network instability between the pod and the API server. Consider increasing `--leader-election-lease-duration`.

1.  **Check leader election parameters.** Verify the configured values:

   ```
   kubectl get deployment eks-hybrid-nodes-gateway -n eks-hybrid-nodes-gateway -o jsonpath='{.spec.template.spec.containers[0].args}'
   ```

   Ensure `--leader-election-renew-deadline` is less than `--leader-election-lease-duration`. If the renew deadline exceeds the lease duration, the leader loses the lease before it can renew. For more information, see [Leader election tuning](hybrid-nodes-gateway-configuration.md#hybrid-nodes-gateway-leader-tuning).

## Common error messages
<a name="hybrid-nodes-gateway-ts-errors"></a>

The following table lists error messages you may see in the gateway pod logs and their resolutions.


| Error message | Cause | Resolution | 
| --- | --- | --- | 
|  `IP forwarding is not enabled`  | The kernel parameter `net.ipv4.ip_forward` is not set to `1` on the gateway node. | Enable IP forwarding through the kubelet configuration or by running `sysctl -w net.ipv4.ip_forward=1`. | 
|  `Failed to setup VXLAN`  | The gateway cannot create the VXLAN network interface. This typically occurs when the pod lacks the `NET_ADMIN` capability. | Verify the Deployment spec includes `NET_ADMIN` in `securityContext.capabilities.add`. Check that the Helm chart is deployed correctly. | 
|  `Failed to verify route table access`  | The gateway cannot describe one or more VPC route tables at startup. | Verify the IAM role has `ec2:DescribeRouteTables` permission and the route table IDs in the configuration are correct. | 
|  `Failed to update route tables`  | The gateway cannot create or replace routes in the VPC route tables. | Verify the IAM role has `ec2:CreateRoute` and `ec2:ReplaceRoute` permissions. | 
|  `Failed to create route table manager`  | The gateway cannot initialize the AWS EC2 client or retrieve the instance’s primary ENI. | Verify the IAM role has `ec2:DescribeInstances` permission and the instance metadata service (IMDS) is accessible. | 
|  `NODE_IP is required`  | The `NODE_IP` environment variable or `--node-ip` flag is not set. | Verify the pod spec sets `NODE_IP` from `status.hostIP` using a `fieldRef`. Check that the Helm chart is deployed correctly. | 
|  `Invalid NODE_IP`  | The value provided for `NODE_IP` is not a valid IP address. | Check the `NODE_IP` environment variable value in the pod spec. | 
|  `pod-cidrs and vpc-cidr are required`  | The `POD_CIDRS` or `VPC_CIDR` environment variable is empty. | Set the `podCIDRs` and `vpcCIDR` Helm values during installation. | 
|  `No valid route table IDs provided`  | The `ROUTE_TABLE_IDS` value was set but contains no valid route table IDs after parsing. | Check the `routeTableIDs` Helm value for formatting errors. Route table IDs should be comma-separated (for example, `rtb-abc123,rtb-def456`). | 
|  `Failed to auto-detect AWS region`  | The gateway cannot retrieve the AWS Region from EC2 instance metadata. | Verify the instance metadata service (IMDS) is accessible. Alternatively, set the `--aws-region` flag or `AWS_REGION` environment variable explicitly. | 
|  `Failed to auto-detect AWS instance ID`  | The gateway cannot retrieve the instance ID from EC2 instance metadata. | Verify the instance metadata service (IMDS) is accessible. Alternatively, set the `--aws-instance-id` flag or `AWS_INSTANCE_ID` environment variable explicitly. | 
|  `CiliumNode has no internal IP`  | A hybrid node’s `CiliumNode` object does not have an internal IP address in its spec. | Verify the hybrid node is registered correctly and the Cilium agent is running. Check the `CiliumNode` resource for the node. | 
|  `CiliumNode <name> has no pod CIDRs allocated`  | A hybrid node’s `CiliumNode` object does not have pod CIDRs allocated by Cilium IPAM. | Verify Cilium IPAM is configured correctly on the hybrid node. Check the `CiliumNode` resource for the node’s IPAM status. | 
|  `Failed to upsert CiliumVTEPConfig`  | The gateway cannot create or update the `CiliumVTEPConfig` custom resource. | Verify the CRD is installed in the cluster and the gateway service account has permissions to manage `CiliumVTEPConfig` resources. | 
|  `Unable to create manager`  | The controller-runtime manager failed to initialize. | Check the pod logs for additional context. Common causes include invalid kubeconfig or inability to reach the Kubernetes API server. | 
|  `Failed to add gateway setup`  | The leader-elected runnable could not be registered with the controller manager. | This is typically an internal error. Check the full pod logs for additional context and report the issue on the [GitHub repository](https://github.com/aws/eks-hybrid-nodes-gateway). | 
|  `Unable to create Node controller`  | The CiliumNode reconciler could not be registered with the controller manager. | Check the pod logs for additional context. Verify that the CiliumNode CRD is installed in the cluster. | 
|  `Problem running manager`  | The controller manager exited unexpectedly. | Check the pod logs for the underlying error. Common causes include loss of connectivity to the Kubernetes API server or a port conflict on the metrics or health probe bind addresses. | 
|  `failed to access route table <id>`  | The gateway cannot describe a specific VPC route table during the startup verification check. | Verify the IAM role has `ec2:DescribeRouteTables` permission and the route table ID is correct. The route table must exist in the same Region as the gateway instance. | 

## Related topics
<a name="hybrid-nodes-gateway-ts-related"></a>
+  [Amazon EKS Hybrid Nodes gateway](hybrid-nodes-gateway-overview.md) — Overview of the gateway architecture and use cases.
+  [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md) — Prerequisites and installation instructions.
+  [Amazon EKS Hybrid Nodes gateway configuration reference](hybrid-nodes-gateway-configuration.md) — Complete reference for Helm values, CLI flags, and environment variables.
+  [Amazon EKS Hybrid Nodes gateway operations](hybrid-nodes-gateway-operations.md) — Monitoring, failover behavior, and scaling guidance.