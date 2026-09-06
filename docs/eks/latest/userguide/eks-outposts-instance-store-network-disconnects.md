

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Prepare local Amazon EKS clusters on AWS Outposts configured with EC2 instance store for network disconnects
<a name="eks-outposts-instance-store-network-disconnects"></a>

If the AWS Outposts service link connecting your local network to the AWS Cloud has lost connectivity, you can continue to use your local Amazon EKS cluster on an Outpost. This topic covers how to prepare your local cluster for network disconnects and related considerations.
+ Local clusters enable stability and continued operations during temporary, unplanned network disconnects. AWS Outposts remains a fully connected offering that acts as an extension of the AWS Cloud in your data center. In the event of network disconnects between your Outpost and the AWS Cloud, we recommend attempting to restore your connection. For instructions, see [AWS Outposts rack network troubleshooting checklist](https://docs.aws.amazon.com/outposts/latest/userguide/network-troubleshoot.html) in the * AWS Outposts User Guide*.
+ Outposts emit a `ConnectedStatus` metric that you can use to monitor the connectivity state of your Outpost. For more information, see [Outposts Metrics](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html#outposts-metrics) in the * AWS Outposts User Guide*.

## Authentication during network disconnects
<a name="eks-outposts-instance-store-network-disconnects-authentication"></a>

Local clusters support multiple authentication mechanisms. Their availability during network disconnects varies:


| Authentication mechanism | Available during disconnect? | 
| --- | --- | 
|  AWS IAM (access entries, `aws-auth` ConfigMap) | No. IAM requires connectivity to the AWS Region. | 
| OIDC (customer-provided provider) | Depends on provider location. If the OIDC provider is reachable from the Outpost’s local network, authentication continues to work. | 
| x.509 client certificates | Yes. Certificates are validated locally by the Kubernetes API server. | 
| IRSA (IAM Roles for Service Accounts) | No. See [IRSA and Pod Identity during disconnects](#eks-outposts-instance-store-network-disconnects-irsa). | 
| EKS Pod Identity | No. See [IRSA and Pod Identity during disconnects](#eks-outposts-instance-store-network-disconnects-irsa). | 

### x.509 client certificates
<a name="eks-outposts-instance-store-network-disconnects-x509"></a>

To maintain `kubectl` access during network disconnects, create a client x.509 certificate before the disconnect occurs.

To create an admin certificate:

1. Generate a private key and certificate signing request (CSR):

   ```
   openssl req -new -newkey rsa:4096 -nodes \
       -keyout admin.key -out admin.csr -subj "/CN=admin"
   ```

1. Create a Kubernetes `CertificateSigningRequest` resource and approve it:

   ```
   cat admin.csr | base64 | tr -d '\n' > admin.csr.b64
   ```

   ```
   apiVersion: certificates.k8s.io/v1
   kind: CertificateSigningRequest
   metadata:
     name: admin-csr
   spec:
     request: <base64-encoded-csr>
     signerName: kubernetes.io/kube-apiserver-client
     usages:
       - client auth
   ```

   ```
   kubectl apply -f admin-csr.yaml
   kubectl certificate approve admin-csr
   ```

1. Retrieve the signed certificate:

   ```
   kubectl get csr admin-csr -o jsonpath='{.status.certificate}' | base64 --decode > admin.crt
   ```

1. Create a `ClusterRoleBinding` to grant admin access:

   ```
   kubectl create clusterrolebinding admin --clusterrole=cluster-admin \
       --user=admin --group=system:masters
   ```

1. Build a `kubeconfig` that uses the certificate:

   ```
   kubectl config --kubeconfig admin.kubeconfig set-cluster my-cluster \
       --certificate-authority=ca.crt --server $APISERVER_ENDPOINT --embed-certs
   kubectl config --kubeconfig admin.kubeconfig set-credentials admin \
       --client-certificate=admin.crt --client-key=admin.key --embed-certs
   kubectl config --kubeconfig admin.kubeconfig set-context admin@my-cluster \
       --cluster my-cluster --user admin
   kubectl config --kubeconfig admin.kubeconfig use-context admin@my-cluster
   ```

### Cluster endpoint DNS resolution during disconnects
<a name="eks-outposts-instance-store-network-disconnects-cluster-dns"></a>

The Kubernetes API server endpoint for a local cluster is hosted in Amazon Route 53 and resolves to the private IP addresses of the cross-account elastic network interfaces (ENIs) that Amazon EKS creates in your subnets. These ENIs have static private IP addresses that don’t change during normal cluster operation.

During a network disconnect, the Outpost can’t reach Route 53, so the cluster endpoint hostname doesn’t resolve unless you’ve prepared a local resolution path. Three categories of clients need to reach the API server:
+  **Cluster administrators** running `kubectl`.
+  **Worker nodes** (`kubelet`) sending node heartbeats and pulling specs.
+  ** `kube-proxy` ** on each node, which sets up cluster Service IPs.

#### Option 1: local DNS solution (recommended)
<a name="_option_1_local_dns_solution_recommended"></a>

 AWS recommends deploying a local DNS solution that caches the cluster endpoint records and serves them while the Outpost is disconnected. You can run your own DNS server in your on-premises environment that caches the cluster endpoint records.

If you use a local DNS solution, we recommend pointing your `kubeconfig` and your worker-node AMIs at the cluster endpoint hostname (not at ENI IP addresses) so that resolution is consistent with the local DNS solution.

#### Option 2: static IP-based access
<a name="_option_2_static_ip_based_access"></a>

If you don’t want to run a local DNS solution, you can use static IP-based access.
+  **Administrators:** Configure your `kubeconfig` to point directly to a cross-account ENI private IP address. Find the ENIs by searching for network interfaces with the description `Amazon EKS {{cluster-name}} ` in your AWS account. Each ENI’s IP address is stable for the lifetime of the cluster under normal operation.
+  **Worker nodes (Amazon EKS optimized AMIs):** When you launch worker nodes from an Amazon EKS optimized AMI, the bootstrap script adds the cluster endpoint to `/etc/hosts` with the ENI IP addresses. No additional configuration is needed.
+  **Worker nodes (custom AMIs):** Add the cluster endpoint hostname and ENI IP addresses to `/etc/hosts` in your custom bootstrap. Otherwise, `kubelet` and `kube-proxy` can’t reach the API server during a disconnect.

**Important**  
If a cross-account ENI is deleted or its IP address changes — for example, if you delete it or modify it in a way that prevents Amazon EKS from re-attaching it — every node and every administrator using static IP-based access must be updated manually. With a local DNS solution, no manual intervention is required.

### Pod DNS resolution during disconnects
<a name="eks-outposts-instance-store-network-disconnects-pod-dns"></a>

To prevent DNS failures during disconnected operation, configure your worker node launch template to override `kubelet’s `resolvConf` setting. In your userdata, create a custom `resolv.conf` file (for example, `/etc/kubernetes/resolv.conf`) containing only `nameserver 10.0.0.2` (without the VPC search domain), then set `spec.kubelet.config.resolvConf: /etc/kubernetes/resolv.conf` in your `NodeConfig`. This removes the ` {{region-code}}.compute.internal` search domain from pod DNS configuration, preventing queries from being forwarded to the unreachable VPC DNS resolver while disconnected.

The following example shows worker node userdata:

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="BOUNDARY"

--BOUNDARY
Content-Type: text/x-shellscript; charset="us-ascii"

#!/bin/bash
mkdir -p /etc/kubernetes
echo "nameserver 10.0.0.2" > /etc/kubernetes/resolv.conf

--BOUNDARY
Content-Type: application/node.eks.aws

---
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  cluster:
    name: my-cluster
    ...
  kubelet:
    config:
      resolvConf: /etc/kubernetes/resolv.conf

--BOUNDARY--
```

### IRSA and Pod Identity during disconnects
<a name="eks-outposts-instance-store-network-disconnects-irsa"></a>

**Important**  
IRSA and EKS Pod Identity depend on AWS STS, which runs in the AWS Region. During a network disconnect, workloads that use IRSA or Pod Identity cannot obtain new credentials. Existing credentials expire after a period of time.

We do not recommend taking functional or operational dependencies on Region-based AWS services for workloads that must remain available during network disconnects.

## `etcd` behavior during disconnects
<a name="eks-outposts-instance-store-network-disconnects-etcd"></a>

During network disconnects, `etcd` snapshots cannot be backed up. If more than one `etcd` instance becomes unavailable during a disconnect, `etcd` loses quorum and Kubernetes API operations are not available until your Outpost reconnects and `etcd` quorum has been restored. Workloads that are already running continue to operate.

## Control plane logging during disconnects
<a name="eks-outposts-instance-store-network-disconnects-cp-logs"></a>

During network disconnects, control plane logs are cached locally on the control plane instances. When connectivity is restored, the logs are sent to Amazon CloudWatch Logs in the parent AWS Region. You do not need to install or maintain any logging agent on the control plane.

## Local observability
<a name="eks-outposts-instance-store-network-disconnects-local-observability"></a>

You can monitor your cluster locally during disconnects by using [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), or other third-party solutions to scrape the Kubernetes API server metrics endpoint.

## Local image repository
<a name="eks-outposts-instance-store-network-disconnects-image-repo"></a>

To scale deployments with additional replicas or to recover from pod failures during disconnects, you must have a local container image repository (such as a Docker registry), or the images must be cached on the node before disconnection. Amazon ECR is not available during network disconnects.

## Tune Kubernetes pod failover behavior
<a name="eks-outposts-instance-store-network-disconnects-pod-failover"></a>

During a network disconnect, the Kubernetes control plane cannot communicate with the AWS Region. If a node becomes unreachable, the default Kubernetes behavior is to evict pods after a timeout period. You can tune this behavior using tolerations and `tolerationSeconds` on your pod specifications to control how quickly pods are rescheduled during partitions. For detailed guidance and examples, see https://docs.aws.amazon.com/eks/latest/best-practices/hybrid-nodes-network-disconnection-best-practices.html\#*tune\_kubernetes\_pod\_failover\_behavior[Tune Kubernetes pod failover behavior] in the \_Amazon EKS Best Practices Guide*.

## Simulate a network disconnect
<a name="eks-outposts-instance-store-network-disconnects-simulate"></a>

Before you go into production with your local cluster, simulate a disconnect to verify that you can access your cluster when it’s in a disconnected state.

1. Apply firewall rules on the networking devices that connect your Outpost to the AWS Region. This disconnects the service link of the Outpost.

1. Test the connection to your local cluster using the x.509 certificate you created:

   ```
   kubectl --kubeconfig admin.kubeconfig get nodes
   ```

**Note**  
If you have services already in production on your Outpost, do not simulate a disconnect. Disconnecting the service link affects all services running on the Outpost.