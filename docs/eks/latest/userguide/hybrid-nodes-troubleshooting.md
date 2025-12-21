**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshooting hybrid nodes

This topic covers some common errors that you might see while using Amazon EKS Hybrid Nodes and how to fix them. For other troubleshooting information, see [Troubleshoot problems with Amazon EKS clusters and nodes](troubleshooting.md "troubleshooting.md") and [Knowledge Center tag for Amazon EKS](https://repost.aws/tags/knowledge-center/TA4IvCeWI1TE66q4jEj4Z9zg/amazon-elastic-kubernetes-service "https://repost.aws/tags/knowledge-center/TA4IvCeWI1TE66q4jEj4Z9zg/amazon-elastic-kubernetes-service") on _AWS re:Post_. If you cannot resolve the issue, contact AWS Support.

**Node troubleshooting with `nodeadm debug`**
You can run the `nodeadm debug` command from your hybrid nodes to validate networking and credential requirements are met. For more information on the `nodeadm debug` command, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md").

**Detect issues with your hybrid nodes with cluster insights**
Amazon EKS cluster insights includes _insight checks_ that detect common issues with the configuration of EKS Hybrid Nodes in your cluster. You can view the results of all insight checks from the AWS Management Console, AWS CLI, and the AWS SDKs. For more information about cluster insights, see [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md "cluster-insights.md").

## Installing hybrid nodes troubleshooting

The following troubleshooting topics are related to installing the hybrid nodes dependencies on hosts with the `nodeadm install` command.

**`nodeadm` command failed `must run as root`**

The `nodeadm install` command must be run with a user that has root or `sudo` privileges on your host. If you run `nodeadm install` with a user that does not have root or `sudo` privileges, you will see the following error in the `nodeadm` output.

```
"msg":"Command failed","error":"must run as root"
```

**Unable to connect to dependencies**

The `nodeadm install` command installs the dependencies required for hybrid nodes. The hybrid nodes dependencies include `containerd`, `kubelet`, `kubectl`, and AWS SSM or AWS IAM Roles Anywhere components. You must have access from where you are running `nodeadm install` to download these dependencies. For more information on the list of locations that you must be able to access, see [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md"). If you do not have access, you will see errors similar to the following in the `nodeadm install` output.

```
"msg":"Command failed","error":"failed reading file from url: ...: max retries achieved for http request"
```

**Failed to update package manager**

The `nodeadm install` command runs `apt update` or `yum update` or `dnf update` before installing the hybrid nodes dependencies. If this step does not succeed you might see errors similar to the following. To remediate, you can run `apt update` or `yum update` or `dnf update` before running `nodeadm install` or you can attempt to re-run `nodeadm install`.

```
failed to run update using package manager
```

**Timeout or context deadline exceeded**

When running `nodeadm install`, if you see issues at various stages of the install process with errors that indicate there was a timeout or context deadline exceeded, you might have a slow connection that is preventing the installation of the hybrid nodes dependencies before timeouts are met. To work around these issues, you can attempt to use the `--timeout` flag in `nodeadm` to extend the duration of the timeouts for downloading the dependencies.

```
nodeadm install K8S_VERSION --credential-provider CREDS_PROVIDER --timeout `20m0s`

```

## Connecting hybrid nodes troubleshooting

The troubleshooting topics in this section are related to the process of connecting hybrid nodes to EKS clusters with the `nodeadm init` command.

**Operation errors or unsupported scheme**

When running `nodeadm init`, if you see errors related to `operation error` or `unsupported scheme`, check your `nodeConfig.yaml` to make sure it is properly formatted and passed to `nodeadm`. For more information on the format and options for `nodeConfig.yaml`, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md").

```
"msg":"Command failed","error":"operation error ec2imds: GetRegion, request canceled, context deadline exceeded"
```

**Hybrid Nodes IAM role missing permissions for the `eks:DescribeCluster` action**

When running `nodeadm init`, `nodeadm` attempts to gather information about your EKS cluster by calling the EKS `DescribeCluster` action. If your Hybrid Nodes IAM role does not have permission for the `eks:DescribeCluster` action, then you must pass your Kubernetes API endpoint, cluster CA bundle, and service IPv4 CIDR in the node configuration you pass to `nodeadm` when you run `nodeadm init`. For more information on the required permissions for the Hybrid Nodes IAM role, see [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md").

```
"msg":"Command failed","error":"operation error EKS: DescribeCluster, https response error StatusCode: 403 ... AccessDeniedException"
```

**Hybrid Nodes IAM role missing permissions for the `eks:ListAccessEntries` action**

When running `nodeadm init`, `nodeadm` attempts to validate whether your EKS cluster has an access entry of type `HYBRID_LINUX` associated with the Hybrid Nodes IAM role by calling the EKS `ListAccessEntries` action. If your Hybrid Nodes IAM role does not have permission for the `eks:ListAccessEntries` action, then you must pass the `--skip cluster-access-validation` flag when you run the `nodeadm init` command. For more information on the required permissions for the Hybrid Nodes IAM role, see [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md").

```
"msg":"Command failed","error":"operation error EKS: ListAccessEntries, https response error StatusCode: 403 ... AccessDeniedException"
```

**Node IP not in remote node network CIDR**

When running `nodeadm init`, you might encounter an error if the node’s IP address is not within the specified remote node network CIDRs. The error will look similar to the following example:

```
node IP 10.18.0.1 is not in any of the remote network CIDR blocks [10.0.0.0/16 192.168.0.0/16]
```

This example shows a node with IP 10.18.0.1 attempting to join a cluster with remote network CIDRs 10.0.0.0/16 and 192.168.0.0/16. The error occurs because 10.18.0.1 isn’t within either of the ranges.

Confirm that you’ve properly configured your `RemoteNodeNetworks` to include all node IP addresses. For more information on networking configuration, see [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md").

- Run the following command in the region your cluster is located to check your `RemoteNodeNetwork` configurations. Verify that the CIDR blocks listed in the output include the IP range of your node and is the same as the CIDR blocks listed in the error message. If they do not match, confirm the cluster name and region in your `nodeConfig.yaml` match your intended cluster.

```
aws eks describe-cluster --name `CLUSTER_NAME` --region `REGION_NAME` --query cluster.remoteNetworkConfig.remoteNodeNetworks
```

- Verify you’re working with the intended node:
  - Confirm you’re on the correct node by checking its hostname and IP address match the one you intend to register with the cluster.
  - Confirm this node is in the correct on-premises network (the one whose CIDR range was registered as `RemoteNodeNetwork` during cluster setup).

If your node IP is still not what you expected, check the following:

- If you are using IAM Roles Anywhere, `kubelet` performs a DNS lookup on the IAM Roles Anywhere `nodeName` and uses an IP associated with the node name if available. If you maintain DNS entries for your nodes, confirm that these entries point to IPs within your remote node network CIDRs.
- If your node has multiple network interfaces, `kubelet` might select an interface with an IP address outside your remote node network CIDRs as default. To use a different interface, specify its IP address using the `--node-ip`
  `kubelet` flag in your `nodeConfig.yaml`. For more information, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md"). You can view your node’s network interfaces and its IP addresses by running the following command on your node:

```
ip addr show
```

**Hybrid nodes are not appearing in EKS cluster**

If you ran `nodeadm init` and it completed but your hybrid nodes do not appear in your cluster, there might be issues with the network connection between your hybrid nodes and the EKS control plane, you might not have the required security group permissions configured, or you might not have the required mapping of your Hybrid Nodes IAM role to Kubernetes Role-Based Access Control (RBAC). You can start the debugging process by checking the status of `kubelet` and the `kubelet` logs with the following commands. Run the following commands from the hybrid nodes that failed to join your cluster.

```
systemctl status kubelet
```

```
journalctl -u kubelet -f
```

**Unable to communicate with cluster**

If your hybrid node was unable to communicate with the cluster control plane, you might see logs similar to the following.

```
"Failed to ensure lease exists, will retry" err="Get ..."
```

```
"Unable to register node with API server" err="Post ..."
```

```
Failed to contact API server when waiting for CSINode publishing ... dial tcp <ip address>: i/o timeout
```

If you see these messages, check the following to ensure it meets the hybrid nodes requirements detailed in [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md").

- Confirm the VPC passed to EKS cluster has routes to your Transit Gateway (TGW) or Virtual Private Gateway (VGW) for your on-premises node and optionally pod CIDRs.
- Confirm you have an additional security group for your EKS cluster has inbound rules for your on-premises node CIDRs and optionally pod CIDRs.
- Confirm your on-premises router is configured to allow traffic to and from the EKS control plane.

**Unauthorized**

If your hybrid node was able to communicate with the EKS control plane but was not able to register, you might see logs similar to the following. Note the key difference in the log messages below is the `Unauthorized` error. This signals that the node was not able to perform its tasks because it does not have the required permissions.

```
"Failed to ensure lease exists, will retry" err="Unauthorized"
```

```
"Unable to register node with API server" err="Unauthorized"
```

```
Failed to contact API server when waiting for CSINode publishing: Unauthorized
```

If you see these messages, check the following to ensure it meets the hybrid nodes requirements details in [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md") and [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md "hybrid-nodes-cluster-prep.md").

- Confirm the identity of the hybrid nodes matches your expected Hybrid Nodes IAM role. This can be done by running `sudo aws sts get-caller-identity` from your hybrid nodes.
- Confirm your Hybrid Nodes IAM role has the required permissions.
- Confirm that in your cluster you have an EKS access entry for your Hybrid Nodes IAM role or confirm that your `aws-auth` ConfigMap has an entry for your Hybrid Nodes IAM role. If you are using EKS access entries, confirm your access entry for your Hybrid Nodes IAM role has the `HYBRID_LINUX` access type. If you are using the `aws-auth` ConfigMap, confirm your entry for the Hybrid Nodes IAM role meets the requirements and formatting detailed in [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md "hybrid-nodes-cluster-prep.md").

### Hybrid nodes registered with EKS cluster but show status `Not Ready`

If your hybrid nodes successfully registered with your EKS cluster, but the hybrid nodes show status `Not Ready`, the first thing to check is your Container Networking Interface (CNI) status. If you have not installed a CNI, then it is expected that your hybrid nodes have status `Not Ready`. Once a CNI is installed and running successfully, nodes are updated to the status `Ready`. If you attempted to install a CNI but it is not running successfully, see [Hybrid nodes CNI troubleshooting](#hybrid-nodes-troubleshooting-cni "#hybrid-nodes-troubleshooting-cni") on this page.

**Certificate Signing Requests (CSRs) are stuck Pending**

After connecting hybrid nodes to your EKS cluster, if you see that there are pending CSRs for your hybrid nodes, your hybrid nodes are not meeting the requirements for automatic approval. CSRs for hybrid nodes are automatically approved and issued if the CSRs for hybrid nodes were created by a node with `eks.amazonaws.com/compute-type: hybrid` label, and the CSR has the following Subject Alternative Names (SANs): at least one DNS SAN equal to the node name and the IP SANs belong to the remote node network CIDRs.

**Hybrid profile already exists**

If you changed your `nodeadm` configuration and attempt to reregister the node with the new configuration, you might see an error that states that the hybrid profile already exists but its contents have changed. Instead of running `nodeadm init` in between configuration changes, run `nodeadm uninstall` followed by a `nodeadm install` and `nodeadm init`. This ensures a proper clean up with the changes in configuration.

```
"msg":"Command failed","error":"hybrid profile already exists at /etc/aws/hybrid/config but its contents do not align with the expected configuration"
```

**Hybrid node failed to resolve Private API**

After running `nodeadm init`, if you see an error in the `kubelet` logs that shows failures to contact the EKS Kubernetes API server because there is `no such host`, you might have to change your DNS entry for the EKS Kubernetes API endpoint in your on-premises network or at the host level. See [Forwarding inbound DNS queries to your VPC](../../../Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.md "../../../Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.md") in the _AWS Route53 documentation_.

```
Failed to contact API server when waiting for CSINode publishing: Get ... no such host
```

**Can’t view hybrid nodes in the EKS console**

If you have registered your hybrid nodes but are unable to view them in the EKS console, check the permissions of the IAM principal you are using to view the console. The IAM principal you’re using must have specific minimum IAM and Kubernetes permissions to view resources in the console. For more information, see [View Kubernetes resources in the AWS Management Console](view-kubernetes-resources.md "view-kubernetes-resources.md").

## Running hybrid nodes troubleshooting

If your hybrid nodes registered with your EKS cluster, had status `Ready`, and then transitioned to status `Not Ready`, there are a wide range of issues that might have contributed to the unhealthy status such as the node lacking sufficient resources for CPU, memory, or available disk space, or the node is disconnected from the EKS control plane. You can use the steps below to troubleshoot your nodes, and if you cannot resolve the issue, contact AWS Support.

Run `nodeadm debug` from your hybrid nodes to validate networking and credential requirements are met. For more information on the `nodeadm debug` command, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md").

**Get node status**

```
kubectl get nodes -o wide
```

**Check node conditions and events**

```
kubectl describe node `NODE_NAME`

```

**Get pod status**

```
kubectl get pods -A -o wide
```

**Check pod conditions and events**

```
kubectl describe pod `POD_NAME`

```

**Check pod logs**

```
kubectl logs `POD_NAME`

```

**Check `kubectl` logs**

```
systemctl status kubelet
```

```
journalctl -u kubelet -f
```

**Pod liveness probes failing or webhooks are not working**

If applications, add-ons, or webhooks running on your hybrid nodes are not starting properly, you might have networking issues that block the communication to the pods. For the EKS control plane to contact webhooks running on hybrid nodes, you must configure your EKS cluster with a remote pod network and have routes for your on-premises pod CIDR in your VPC routing table with the target as your Transit Gateway (TGW), virtual private gateway (VPW), or other gateway you are using to connect your VPC with your on-premises network. For more information on the networking requirements for hybrid nodes, see [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md"). You additionally must allow this traffic in your on-premises firewall and ensure your router can properly route to your pods. See [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md") for more information on the requirements for running webhooks on hybrid nodes.

A common pod log message for this scenario is shown below the following where ip-address is the Cluster IP for the Kubernetes service.

```
dial tcp <ip-address>:443: connect: no route to host
```

**`kubectl logs` or `kubectl exec` commands not working (`kubelet` API commands)**

If `kubectl attach`, `kubectl cp`, `kubectl exec`, `kubectl logs`, and `kubectl port-forward` commands time out while other `kubectl` commands succeed, the issue is likely related to remote network configuration. These commands connect through the cluster to the `kubelet` endpoint on the node. For more information see [kubelet endpoint](hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-kubelet-api "hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-kubelet-api").

Verify that your node IPs and pod IPs fall within the remote node network and remote pod network CIDRs configured for your cluster. Use the commands below to examine IP assignments.

```
kubectl get nodes -o wide
```

```
kubectl get pods -A -o wide
```

Compare these IPs with your configured remote network CIDRs to ensure proper routing. For network configuration requirements, see [Prepare networking for hybrid nodes](hybrid-nodes-networking.md "hybrid-nodes-networking.md").

## Hybrid nodes CNI troubleshooting

If you run into issues with initially starting Cilium or Calico with hybrid nodes, it is most often due to networking issues between hybrid nodes or the CNI pods running on hybrid nodes, and the EKS control plane. Make sure your environment meets the requirements in Prepare networking for hybrid nodes. It’s useful to break down the problem into parts.

EKS cluster configuration

Are the RemoteNodeNetwork and RemotePodNetwork configurations correct?

VPC configuration

Are there routes for the RemoteNodeNetwork and RemotePodNetwork in the VPC routing table with the target of the Transit Gateway or Virtual Private Gateway?

Security group configuration

Are there inbound and outbound rules for the RemoteNodeNetwork and RemotePodNetwork ?

On-premises network

Are there routes and access to and from the EKS control plane and to and from the hybrid nodes and the pods running on hybrid nodes?

CNI configuration

If using an overlay network, does the IP pool configuration for the CNI match the RemotePodNetwork configured for the EKS cluster if using webhooks?

**Hybrid node has status `Ready` without a CNI installed**

If your hybrid nodes are showing status `Ready`, but you have not installed a CNI on your cluster, it is possible that there are old CNI artifacts on your hybrid nodes. By default, when you uninstall Cilium and Calico with tools such as Helm, the on-disk resources are not removed from your physical or virtual machines. Additionally, the Custom Resource Definitions (CRDs) for these CNIs might still be present on your cluster from an old installation. For more information, see the Delete Cilium and Delete Calico sections of [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md").

**Cilium troubleshooting**

If you are having issues running Cilium on hybrid nodes, see [the troubleshooting steps](https://docs.cilium.io/en/stable/operations/troubleshooting/ "https://docs.cilium.io/en/stable/operations/troubleshooting/") in the Cilium documentation. The sections below cover issues that might be unique to deploying Cilium on hybrid nodes.

**Cilium isn’t starting**

If the Cilium agents that run on each hybrid node are not starting, check the logs of the Cilium agent pods for errors. The Cilium agent requires connectivity to the EKS Kubernetes API endpoint to start. Cilium agent startup will fail if this connectivity is not correctly configured. In this case, you will see log messages similar to the following in the Cilium agent pod logs.

```
msg="Unable to contact k8s api-server"
level=fatal msg="failed to start: Get \"https://<k8s-cluster-ip>:443/api/v1/namespaces/kube-system\": dial tcp <k8s-cluster-ip>:443: i/o timeout"
```

The Cilium agent runs on the host network. Your EKS cluster must be configured with `RemoteNodeNetwork` for the Cilium connectivity. Confirm you have an additional security group for your EKS cluster with an inbound rule for your `RemoteNodeNetwork`, that you have routes in your VPC for your `RemoteNodeNetwork`, and that your on-premises network is configured correctly to allow connectivity to the EKS control plane.

If the Cilium operator is running and some of your Cilium agents are running but not all, confirm that you have available pod IPs to allocate for all nodes in your cluster. You configure the size of your allocatable Pod CIDRs when using cluster pool IPAM with `clusterPoolIPv4PodCIDRList` in your Cilium configuration. The per-node CIDR size is configured with the `clusterPoolIPv4MaskSize` setting in your Cilium configuration. See [Expanding the cluster pool](https://docs.cilium.io/en/stable/network/concepts/ipam/cluster-pool/#expanding-the-cluster-pool "https://docs.cilium.io/en/stable/network/concepts/ipam/cluster-pool/#expanding-the-cluster-pool") in the Cilium documentation for more information.

**Cilium BGP is not working**

If you are using Cilium BGP Control Plane to advertise your pod or service addresses to your on-premises network, you can use the following Cilium CLI commands to check if BGP is advertising the routes to your resources. For steps to install the Cilium CLI, see [Install the Cilium CLI](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/#install-the-cilium-cli "https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/#install-the-cilium-cli") in the Cilium documentation.

If BGP is working correctly, you should your hybrid nodes with Session State `established` in the output. You might need to work with your networking team to identify the correct values for your environment’s Local AS, Peer AS, and Peer Address.

```
cilium bgp peers
```

```
cilium bgp routes
```

If you are using Cilium BGP to advertise the IPs of Services with type `LoadBalancer`, you must have the same label on both your `CiliumLoadBalancerIPPool` and Service, which should be used in the selector of your `CiliumBGPAdvertisement`. An example is shown below. Note, if you are using Cilium BGP to advertise the IPs of Services with type LoadBalancer, the BGP routes might be disrupted during Cilium agent restart. For more information, see [Failure Scenarios](https://docs.cilium.io/en/latest/network/bgp-control-plane/bgp-control-plane-operation/#failure-scenarios "https://docs.cilium.io/en/latest/network/bgp-control-plane/bgp-control-plane-operation/#failure-scenarios") in the Cilium documentation.

**Service**

```
kind: Service
apiVersion: v1
metadata:
  name: guestbook
  labels:
    app: guestbook
spec:
  ports:
  - port: 3000
    targetPort: http-server
  selector:
    app: guestbook
  type: LoadBalancer
```

**CiliumLoadBalancerIPPool**

```
apiVersion: cilium.io/v2alpha1
kind: CiliumLoadBalancerIPPool
metadata:
  name: guestbook-pool
  labels:
    app: guestbook
spec:
  blocks:
  - cidr: <CIDR to advertise>
  serviceSelector:
    matchExpressions:
      - { key: app, operator: In, values: [ guestbook ] }
```

**CiliumBGPAdvertisement**

```
apiVersion: cilium.io/v2alpha1
kind: CiliumBGPAdvertisement
metadata:
  name: bgp-advertisements-guestbook
  labels:
    advertise: bgp
spec:
  advertisements:
    - advertisementType: "Service"
      service:
        addresses:
          - ExternalIP
          - LoadBalancerIP
      selector:
        matchExpressions:
          - { key: app, operator: In, values: [ guestbook ] }
```

**Calico troubleshooting**

If you are having issues running Calico on hybrid nodes, see [the troubleshooting steps](https://docs.tigera.io/calico/latest/operations/troubleshoot/ "https://docs.tigera.io/calico/latest/operations/troubleshoot/") in the Calico documentation. The sections below cover issues that might be unique to deploying Calico on hybrid nodes.

The table below summarizes the Calico components and whether they run on the node or pod network by default. If you configured Calico to use NAT for outgoing pod traffic, your on-premises network must be configured to route traffic to your on-premises node CIDR and your VPC routing tables must be configured with a route for your on-premises node CIDR with your transit gateway (TGW) or virtual private gateway (VGW) as the target. If you are not configuring Calico to use NAT for outgoing pod traffic, your on-premises network must be configured to route traffic to your on-premises pod CIDR and your VPC routing tables must be configured with a route for your on-premises pod CIDR with your transit gateway (TGW) or virtual private gateway (VGW) as the target.

| Component                         | Network |
| --------------------------------- | ------- |
| Calico API server                 | Node    |
| Calico Controllers for Kubernetes | Pod     |
| Calico node agent                 | Node    |
| Calico `typha`                    | Node    |
| Calico CSI node driver            | Pod     |
| Calico operator                   | Node    |

**Calico resources are scheduled or running on cordoned nodes**

The Calico resources that don’t run as a DaemonSet have flexible tolerations by default that enable them to be scheduled on cordoned nodes that are not ready for scheduling or running pods. You can tighten the tolerations for the non-DaemonSet Calico resources by changing your operator installation to include the following.

```
installation:
  ...
  controlPlaneTolerations:
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  calicoKubeControllersDeployment:
    spec:
      template:
        spec:
          tolerations:
          - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
          - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
  typhaDeployment:
    spec:
      template:
        spec:
          tolerations:
          - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
          - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
```

## Credentials troubleshooting

For both AWS SSM hybrid activations and AWS IAM Roles Anywhere, you can validate that credentials for the Hybrid Nodes IAM role are correctly configured on your hybrid nodes by running the following command from your hybrid nodes. Confirm the node name and Hybrid Nodes IAM Role name are what you expect.

```
sudo aws sts get-caller-identity
```

```
{
    "UserId": "ABCDEFGHIJKLM12345678910:<node-name>",
    "Account": "<aws-account-id>",
    "Arn": "arn:aws:sts::<aws-account-id>:assumed-role/<hybrid-nodes-iam-role/<node-name>"
}
```

**AWS Systems Manager (SSM) troubleshooting**

If you are using AWS SSM hybrid activations for your hybrid nodes credentials, be aware of the following SSM directories and artifacts that are installed on your hybrid nodes by `nodeadm`. For more information on the SSM agent, see [Working with the SSM agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in the _AWS Systems Manager User Guide_.

| Description     | Location                                                                                                        |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| SSM agent       | Ubuntu<br>• `/snap/amazon-ssm-agent/current/amazon-ssm-agent`<br>RHEL & AL2023<br>• `/usr/bin/amazon-ssm-agent` |
| SSM agent logs  | `/var/log/amazon/ssm`                                                                                           |
| AWS credentials | `/root/.aws/credentials`                                                                                        |
| SSM Setup CLI   | `/opt/ssm/ssm-setup-cli`                                                                                        |

**Restarting the SSM agent**

Some issues can be resolved by restarting the SSM agent. You can use the commands below to restart it.

**AL2023 and other operating systems**

```
systemctl restart amazon-ssm-agent
```

**Ubuntu**

```
systemctl restart snap.amazon-ssm-agent.amazon-ssm-agent
```

**Check connectivity to SSM endpoints**

Confirm you can connect to the SSM endpoints from your hybrid nodes. For a list of the SSM endpoints, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). Replace `us-west-2` in the command below with the AWS Region for your AWS SSM hybrid activation.

```
ping ssm.us-west-2.amazonaws.com
```

**View connection status of registered SSM instances**

You can check the connection status of the instances that are registered with SSM hybrid activations with the following AWS CLI command. Replace the machine ID with the machine ID of your instance.

```
aws ssm get-connection-status --target `mi-012345678abcdefgh`

```

**SSM Setup CLI checksum mismatch**

When running `nodeadm install` if you see an issue with the `ssm-setup-cli` checksum mismatch you should confirm there are not older existing SSM installations on your host. If there are older SSM installations on your host, remove them and re-run `nodeadm install` to resolve the issue.

```
Failed to perform agent-installation/on-prem registration: error while verifying installed ssm-setup-cli checksum: checksum mismatch with latest ssm-setup-cli.
```

**SSM `InvalidActivation`**

If you see an error registering your instance with AWS SSM, confirm the `region`, `activationCode`, and `activationId` in your `nodeConfig.yaml` are correct. The AWS Region for your EKS cluster must match the region of your SSM hybrid activation. If these values are misconfigured, you might see an error similar to the following.

```
ERROR Registration failed due to error registering the instance with AWS SSM. InvalidActivation
```

**SSM `ExpiredTokenException`: The security token included in the request is expired**

If the SSM agent is not able to refresh credentials, you might see an `ExpiredTokenException`. In this scenario, if you are able to connect to the SSM endpoints from your hybrid nodes, you might need to restart the SSM agent to force a credential refresh.

```
"msg":"Command failed","error":"operation error SSM: DescribeInstanceInformation, https response error StatusCode: 400, RequestID: eee03a9e-f7cc-470a-9647-73d47e4cf0be, api error ExpiredTokenException: The security token included in the request is expired"
```

**SSM error in running register machine command**

If you see an error registering the machine with SSM, you might need to re-run `nodeadm install` to make sure all of the SSM dependencies are properly installed.

```
"error":"running register machine command: , error: fork/exec /opt/aws/ssm-setup-cli: no such file or directory"
```

**SSM `ActivationExpired`**

When running `nodeadm init`, if you see an error registering the instance with SSM due to an expired activation, you need to create a new SSM hybrid activation, update your `nodeConfig.yaml` with the `activationCode` and `activationId` of your new SSM hybrid activation, and re-run `nodeadm init`.

```
"msg":"Command failed","error":"SSM activation expired. Please use a valid activation"
```

```
ERROR Registration failed due to error registering the instance with AWS SSM. ActivationExpired
```

**SSM failed to refresh cached credentials**

If you see a failure to refresh cached credentials, the `/root/.aws/credentials` file might have been deleted on your host. First check your SSM hybrid activation and ensure it is active and your hybrid nodes are configured correctly to use the activation. Check the SSM agent logs at `/var/log/amazon/ssm` and re-run the `nodeadm init` command once you have resolved the issue on the SSM side.

```
"Command failed","error":"operation error SSM: DescribeInstanceInformation, get identity: get credentials: failed to refresh cached credentials"
```

**Clean up SSM**

To remove the SSM agent from your host, you can run the following commands.

```
dnf remove -y amazon-ssm-agent
sudo apt remove --purge amazon-ssm-agent
snap remove amazon-ssm-agent
rm -rf /var/lib/amazon/ssm/Vault/Store/RegistrationKey
```

**AWS IAM Roles Anywhere troubleshooting**

If you are using AWS IAM Roles Anywhere for your hybrid nodes credentials, be aware of the following directories and artifacts that are installed on your hybrid nodes by `nodeadm`. For more information on the troubleshooting IAM Roles Anywhere, see [Troubleshooting AWS IAM Roles Anywhere identity and access](../../../rolesanywhere/latest/userguide/security_iam_troubleshoot.md "../../../rolesanywhere/latest/userguide/security_iam_troubleshoot.md") in the _AWS IAM Roles Anywhere User Guide_.

| Description                           | Location                            |
| ------------------------------------- | ----------------------------------- |
| IAM Roles Anywhere CLI                | `/usr/local/bin/aws_signing_helper` |
| Default certificate location and name | `/etc/iam/pki/server.pem`           |
| Default key location and name         | `/etc/iam/pki/server.key`           |

**IAM Roles Anywhere failed to refresh cached credentials**

If you see a failure to refresh cached credentials, review the contents of `/etc/aws/hybrid/config` and confirm that IAM Roles Anywhere was configured correctly in your `nodeadm` configuration. Confirm that `/etc/iam/pki` exists. Each node must have a unique certificate and key. By default, when using IAM Roles Anywhere as the credential provider, `nodeadm` uses `/etc/iam/pki/server.pem` for the certificate location and name, and `/etc/iam/pki/server.key` for the private key. You might need to create the directories before placing the certificates and keys in the directories with `sudo mkdir -p /etc/iam/pki`. You can verify the content of your certificate with the command below.

```
openssl x509 -text -noout -in server.pem
```

```
open /etc/iam/pki/server.pem: no such file or directory
could not parse PEM data
Command failed {"error": "... get identity: get credentials: failed to refresh cached credentials, process provider error: error in credential_process: exit status 1"}
```

**IAM Roles Anywhere not authorized to perform `sts:AssumeRole`**

In the `kubelet` logs, if you see an access denied issue for the `sts:AssumeRole` operation when using IAM Roles Anywhere, check the trust policy of your Hybrid Nodes IAM role to confirm the IAM Roles Anywhere service principal is allowed to assume the Hybrid Nodes IAM Role. Additionally confirm that the trust anchor ARN is configured properly in your Hybrid Nodes IAM role trust policy and that your Hybrid Nodes IAM role is added to your IAM Roles Anywhere profile.

```
could not get token: AccessDenied: User: ... is not authorized to perform: sts:AssumeRole on resource: ...
```

**IAM Roles Anywhere not authorized to set `roleSessionName`**

In the `kubelet` logs, if you see an access denied issue for setting the `roleSessionName`, confirm you have set `acceptRoleSessionName` to true for your IAM Roles Anywhere profile.

```
AccessDeniedException: Not authorized to set roleSessionName
```

## Operating system troubleshooting

### RHEL

**Entitlement or subscription manager registration failures**

If you are running `nodeadm install` and encounter a failure to install the hybrid nodes dependencies due to entitlement registration issues, ensure you have properly set your Red Hat username and password on your host.

```
This system is not registered with an entitlement server
```

### Ubuntu

**GLIBC not found**

If you are using Ubuntu for your operating system and IAM Roles Anywhere for your credential provider with hybrid nodes and see an issue with GLIBC not found, you can install that dependency manually to resolve the issue.

```
GLIBC_2.32 not found (required by /usr/local/bin/aws_signing_helper)
```

Run the following commands to install the dependency:

```
ldd --version
sudo apt update && apt install libc6
sudo apt install glibc-source
```

### Bottlerocket

If you have the Bottlerocket admin container enabled, you can access it with SSH for advanced debugging and troubleshooting with elevated privileges. The following sections contain commands that need to be run on the context of the Bottlerocket host. Once you are on the admin container, you can run `sheltie` to get a full root shell in the Bottlerocket host.

```
sheltie
```

You can also run the commands in the following sections from the admin container shell by prefixing each command with `sudo chroot /.bottlerocket/rootfs`.

```
sudo chroot /.bottlerocket/rootfs <command>
```

**Using logdog for log collection**

Bottlerocket provides the `logdog` utility to efficiently collect logs and system information for troubleshooting purposes.

```
logdog
```

The `logdog` utility gathers logs from various locations on a Bottlerocket host and combines them into a tarball. By default, the tarball will be created at `/var/log/support/bottlerocket-logs.tar.gz`, and is accessible from host containers at `/.bottlerocket/support/bottlerocket-logs.tar.gz`.

**Accessing system logs with journalctl**

You can check the status of the various system services such as `kubelet`, `containerd`, etc and view their logs with the following commands. The `-f` flag will follow the logs in real time.

For checking `kubelet` service status and retrieving `kubelet` logs, you can run:

```
systemctl status kubelet
journalctl -u kubelet -f
```

For checking `containerd` service status and retrieving the logs for the orchestrated `containerd` instance, you can run:

```
systemctl status containerd
journalctl -u containerd -f
```

For checking `host-containerd` service status and retrieving the logs for the host `containerd` instance, you can run:

```
systemctl status host-containerd
journalctl -u host-containerd -f
```

For retrieving the logs for the bootstrap containers and host containers, you can run:

```
journalctl _COMM=host-ctr -f
```
