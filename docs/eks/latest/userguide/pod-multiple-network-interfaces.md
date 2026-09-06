

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Attach multiple network interfaces to Pods
<a name="pod-multiple-network-interfaces"></a>

By default, the Amazon VPC CNI plugin assigns one IP address to each pod. This IP address is attached to an *elastic network interface* that handles all incoming and outgoing traffic for the pod. To increase the bandwidth and packet per second rate performance, you can use the *Multi-NIC feature* of the VPC CNI to configure a multi-homed pod. A multi-homed pod is a single Kubernetes pod that uses multiple network interfaces (and multiple IP addresses). By running a multi-homed pod, you can spread its application traffic across multiple network interfaces by using concurrent connections. This is especially useful for Artificial Intelligence (AI), Machine Learning (ML), and High Performance Computing (HPC) use cases.

The following diagram shows a multi-homed pod running on a worker node with multiple network interface cards (NICs) in use.

![A multi-homed pod with two network interfaces attached one network interface with ENA and one network interface with ENA and EFA](http://docs.aws.amazon.com/eks/latest/userguide/images/multi-homed-pod.png)


## Background
<a name="pod-multi-nic-background"></a>

On Amazon EC2, an *elastic network interface* is a logical networking component in a VPC that represents a virtual network card. For many EC2 instance types, the network interfaces share a single network interface card (NIC) in hardware. This single NIC has a maximum bandwidth and packet per second rate.

If the multi-NIC feature is enabled, the VPC CNI doesn’t assign IP addresses in bulk, which it does by default. Instead, the VPC CNI assigns one IP address to a network interface on each network card on-demand when a new pod starts. This behavior reduces the rate of IP address exhaustion, which is increased by using multi-homed pods. Because the VPC CNI is assigning IP address on-demand, pods might take longer to start on instances with the multi-NIC feature enabled.

## Considerations
<a name="pod-multi-nic-considerations"></a>
+ Ensure that your Kubernetes cluster is running VPC CNI version `1.20.0` and later. The multi-NIC feature is only available in version `1.20.0` of the VPC CNI or later.
+ Enable the `ENABLE_MULTI_NIC` environment variable in the VPC CNI plugin. You can run the following command to set the variable and start a deployment of the DaemonSet.
  +  `kubectl set env daemonset aws-node -n kube-system ENABLE_MULTI_NIC=true` 
+ Ensure that you create worker nodes that have multiple network interface cards (NICs). For a list of EC2 instances that have multiple network interface cards, see [Network cards](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#network-cards) in the **Amazon EC2 User Guide**.
+ If the multi-NIC feature is enabled, the VPC CNI doesn’t assign IP addresses in bulk, which it does by default. Because the VPC CNI is assigning IP address on-demand, pods might take longer to start on instances with the multi-NIC feature enabled. For more information, see the previous section [Background](#pod-multi-nic-background).
+ With the multi-NIC feature enabled, pods don’t have multiple network interfaces by default. You must configure each workload to use multi-NIC. Add the `k8s.amazonaws.com/nicConfig: multi-nic-attachment` annotation to workloads that should have multiple network interfaces.

### `IPv6` Considerations
<a name="pod-multi-nic-considerations-ipv6"></a>
+  **Custom IAM policy** - For `IPv6` clusters, create and use the following custom IAM policy for the VPC CNI. This policy is specific to multi-NIC. For more general information about using the VPC CNI with `IPv6` clusters, see [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md).

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "AmazonEKSCNIPolicyIPv6MultiNIC",
              "Effect": "Allow",
              "Action": [
                  "ec2:CreateNetworkInterface",
                  "ec2:DescribeInstances",
                  "ec2:AssignIpv6Addresses",
                  "ec2:DetachNetworkInterface",
                  "ec2:DescribeNetworkInterfaces",
                  "ec2:DescribeTags",
                  "ec2:ModifyNetworkInterfaceAttribute",
                  "ec2:DeleteNetworkInterface",
                  "ec2:DescribeInstanceTypes",
                  "ec2:UnassignIpv6Addresses",
                  "ec2:AttachNetworkInterface",
                  "ec2:DescribeSubnets"
              ],
              "Resource": "*"
          },
          {
              "Sid": "AmazonEKSCNIPolicyENITagIPv6MultiNIC",
              "Effect": "Allow",
              "Action": "ec2:CreateTags",
              "Resource": "arn:aws:ec2:*:*:network-interface/*"
          }
      ]
  }
  ```
+  `IPv6` **transition mechanism not available** - If you use the multi-NIC feature, the VPC CNI doesn’t assign an `IPv4` address to pods on an `IPv6` cluster. Otherwise, the VPC CNI assigns a host-local `IPv4` address to each pod so that a pod can communicate with external `IPv4` resources in another Amazon VPC or the internet.

## Usage
<a name="pod-multi-NIC-usage"></a>

After the multi-NIC feature is enabled in the VPC CNI and the `aws-node` pods have restarted, you can configure each workload to be multi-homed. The following is an example of a YAML configuration with the required annotation:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-deployment
  namespace: ecommerce
  labels:
    app: orders
spec:
  replicas: 3
  selector:
    matchLabels:
      app: orders
  template:
    metadata:
      annotations:
         k8s.amazonaws.com/nicConfig: multi-nic-attachment
      labels:
        app: orders
    spec:
...
```

## Frequently Asked Questions
<a name="pod-multi-nic-faqs"></a>

### **1. What is a network interface card (NIC)?**
<a name="pod-multi-nic-faqs-nic"></a>

A network interface card (NIC), also simply called a network card, is a physical device that enables network connectivity for the underlying cloud compute hardware. In modern EC2 servers, this refers to the Nitro network card. An Elastic Network Interface (ENI) is a virtual representation of this underlying network card.

Some EC2 instance types have multiple NICs for greater bandwidth and packet rate performance. For such instances, you can assign secondary ENIs to the additional network cards. For example, ENI \#1 can function as the interface for the NIC attached to network card index 0, whereas ENI \#2 can function as the interface for the NIC attached to a separate network card index.

### **2. What is a multi-homed pod?**
<a name="pod-multi-nic-faqs-pod"></a>

A multi-homed pod is a single Kubernetes pod with multiple network interfaces (and by implication multiple IP addresses). Each pod network interface is associated with an [Elastic Network Interface (ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html), and these ENIs are logical representations of separate NICs on the underlying worker node. With multiple network interfaces, a multi-homed pod has additional data transfer capacity, which also raises its data transfer rate.

**Important**  
The VPC CNI can only configure multi-homed pods on instance types that have multiple NICs.

### **3. Why should I use this feature?**
<a name="pod-multi-nic-faqs-why"></a>

If you need to scale network performance in your Kubernetes-based workloads, you can use the multi-NIC feature to run multi-homed pods that interface with all the underlying NICs that have an ENA device attached to it. Leveraging additional network cards raises the bandwidth capacity and packet rate performance in your applications by distributing application traffic across multiple concurrent connections. This is especially useful for Artificial Intelligence (AI), Machine Learning (ML), and High Performance Computing (HPC) use cases.

### **4. How do I use this feature?**
<a name="pod-multi-nic-faqs-how-to-enable"></a>

1. First, you must ensure that your Kubernetes cluster is using VPC CNI version 1.20 or later. For the steps to update the VPC CNI as an EKS add-on, see [Update the Amazon VPC CNI (Amazon EKS add-on)](vpc-add-on-update.md).

1. Then, you have to enable multi-NIC support in the VPC CNI by using the `ENABLE_MULTI_NIC` environment variable.

1. Then, you must ensure that you make and join nodes that have multiple network cards. For a list of EC2 instance types that have multiple network cards, see [Network cards](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#network-cards) in the *Amazon EC2 User Guide*.

1. Finally, you configure each workload to use either multiple network interfaces (multi-homed pods) or use a single network interface.

### **5. How do I configure my workloads to use multiple NICs on a supported worker node?**
<a name="pod-multi-nic-faqs-how-to-workloads"></a>

To use multi-homed pods, you need to add the following annotation: `k8s.amazonaws.com/nicConfig: multi-nic-attachment`. This will attach an ENI from every NIC in the underlying instance to the pod (one to many mapping between a pod and the NICs).

If this annotation is missing, the VPC CNI assumes that your pod only requires 1 network interface and assigns it an IP from an ENI on any available NIC.

### **6. What network interface adapters are supported with this feature?**
<a name="pod-multi-nic-faqs-adapters"></a>

You can use any network interface adapter if you have at least one ENA attached to the underlying network card for IP traffic. For more information about ENA, see [Elastic Network Adapter (ENA)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html) in the *Amazon EC2 User Guide*.

Supported network device configurations:
+  **ENA** interfaces provide all of the traditional IP networking and routing features that are required to support IP networking for a VPC. For more information, see [Enable enhanced networking with ENA on your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html).
+  **EFA** **(EFA** **with ENA)** interfaces provide both the ENA device for IP networking and the EFA device for low-latency, high-throughput communication.

**Important**  
If a network card only has an **EFA-only** adapter attached to it, the VPC CNI will skip it when provisioning network connectivity for a multi-homed pod. However, if you combine an **EFA-only** adapter with an **ENA** adapter on a network card, then the VPC CNI will manage ENIs on this device as well. To use EFA-only interfaces with EKS clusters, see [Run machine learning training on Amazon EKS with Elastic Fabric Adapter](node-efa.md).

### **7. Can I see if a node in my cluster has ENA support?**
<a name="pod-multi-nic-faqs-node-ena"></a>

Yes, you can use the AWS CLI or EC2 API to retrieve network information about an EC2 instance in your cluster. This provides details on whether or not the instance has ENA support. In the following example, replace `<your-instance-id>` with the EC2 instance ID of a node.

 AWS CLI example:

```
aws ec2 describe-instances --instance-ids <your-instance-id> --query "Reservations[].Instances[].EnaSupport"
```

Example output:

```
[ true ]
```

### **8. Can I see the different IP addresses associated with a pod?**
<a name="pod-multi-nic-faqs-list-ips"></a>

No, not easily. However, you can use `nsenter` from the node to run common network tools such as `ip route show` and see the additional IP addresses and interfaces.

### **9. Can I control the number of network interfaces for my pods?**
<a name="pod-multi-nic-faqs-number-of-enis"></a>

No. When your workload is configured to use multiple NICs on a supported instance, a single pod automatically has an IP address from every network card on the instance. Alternatively, single-homed pods will have one network interface attached to one NIC on the instance.

**Important**  
Network cards that *only* have an **EFA-only** device attached to it are skipped by the VPC CNI.

### **10. Can I configure my pods to use a specific NIC?**
<a name="pod-multi-nic-faqs-specify-nic"></a>

No, this isn’t supported. If a pod has the relevant annotation, then the VPC CNI automatically configures it to use every NIC with an ENA adapter on the worker node.

### **11. Does this feature work with the other VPC CNI networking features?**
<a name="pod-multi-nic-faqs-modes"></a>

Yes, the multi-NIC feature in the VPC CNI works with both *custom networking* and *enhanced subnet discovery*. However, the multi-homed pods don’t use the custom subnets or security groups. Instead, the VPC CNI assigns IP addresses and network interfaces to the multi-homed pods with the same subnet and security group configuration as the node. For more information about custom networking, see [Deploy Pods in alternate subnets with custom networking](cni-custom-network.md).

The multi-NIC feature in the VPC CNI doesn’t work with and can’t be combined with *security groups for pods*.

### **12. Can I use network policies with this feature?**
<a name="pod-multi-nic-faqs-netpol"></a>

Yes, you can use Kubernetes network policies with multi-NIC. Kubernetes network policies restrict network traffic to and from your pods. For more information about applying network policies with the VPC CNI, see [Limit Pod traffic with Kubernetes network policies](cni-network-policy.md).

### **13. Is multi-NIC support enabled in EKS Auto Mode?**
<a name="pod-multi-nic-faqs-auto-mode"></a>

Multi-NIC isn’t supported for EKS Auto Mode clusters.