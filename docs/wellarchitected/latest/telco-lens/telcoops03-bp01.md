

# TELCOOPS03-BP01 Implement a cloud-based IPAM solution optimized for workloads requiring secondary network interfaces

 Telco container network functions attach secondary interfaces for user-plane separation, DPDK, or SR-IOV. Each interface needs IP addresses that the cloud network can route. An IP address management (IPAM) solution that ignores Elastic Network Interface (ENI) limits or fails to reflect addresses on the ENI produces undetected packet loss. 

 **Desired outcome:** 
+  An IPAM solution that manages secondary IP allocation with awareness of ENI constraints and subnet capacity. 
+  Assigned Pod IPs are reflected on the parent ENI, enabling correct routing and observability for secondary interfaces. 
+  The IPAM solution handles both kernel-space and user-space (DPDK) interface IP assignment through a unified management plane. 

 **Common anti-patterns:** 
+  Using upstream IPAM solutions such as Whereabouts without validating their behavior against AWS ENA constraints, which leads to IP exhaustion or routing failures. 
+  Assigning Pod IPs that are not reflected on the parent ENI, causing asymmetric routing or broken observability for secondary interfaces. 
+  Managing kernel-space and DPDK interface IPs through separate, uncoordinated systems that can allocate unroutable addresses. 
+  Not accounting for subnet capacity limits when planning secondary IP ranges for large CNF deployments. 

 **Benefits of establishing this best practice:** 
+  All assigned IPs are reflected on ENIs, which allows symmetric routing and correct security-group enforcement. 
+  IPAM respects ENI secondary-IP limits and subnet capacity, which prevents allocation failures at scale. 
+  A single IPAM plane manages IPs across kernel and user-space interfaces, which reduces operational complexity. 
+  IP allocation scales with the CNF deployment without manual subnet expansion or IP range management. 

 **Level of risk exposed if this best practice is not established:** Medium \#\# Implementation guidance IPAM for secondary interfaces in the cloud is a fundamentally different problem from its on-premises equivalent. On-premises, IP addresses come from pre-allocated pools, and the network fabric routes them without a per-interface mapping. In a VPC, the networking layer requires a record of every IP assigned to an interface, because routing and security-group enforcement depend on that mapping. The Amazon VPC CNI plugin handles this for primary Pod interfaces by managing ENI attachment and secondary IP assignment. This integration does not extend to secondary interfaces managed by Multus or a similar multi-CNI setup. An external IPAM such as Whereabouts or host-local can assign a Pod an address not registered on the ENI. The VPC then drops packets destined for that address. While the Pod seems to have a working interface, the control plane and data plane are in disagreement about which IPs exist. To address this, you can extend the VPC CNI to manage secondary-interface IPs, run a controller or sidecar that synchronizes external IPAM assignments onto ENI secondary IPs through the Amazon EC2 API, or use VPC-native IP ranges that are routable without per-IP ENI assignment. For DPDK interfaces, the kernel does not manage the IP stack, so synchronization must come from a control-plane component. Amazon VPC IPAM manages pool allocation across accounts and Regions, but ENI reflection requires a separate controller layer. \#\#\# Implementation steps 
+  Assess the current IPAM architecture and gaps: document how secondary-interface IPs are managed today, whether they are reflected on ENIs, and what fails when they are not synchronized with the VPC networking layer. 
+  Design an addressing scheme within VPC constraints that accounts for per-instance-type ENI secondary-IP limits, subnet CIDR capacity, and growth. Use Amazon VPC IPAM to manage pool allocation across accounts and Regions. 
+  Implement ENI-aware IP synchronization by deploying a controller or operator that synchronizes IPAM-assigned secondary IPs onto the ENI through the AssignPrivateIpAddresses API, so VPC routing and security groups apply to secondary-interface traffic. 
+  Handle DPDK interfaces through a control-plane sidecar: for user-space interfaces where the kernel doesn't manage the IP stack, run a sidecar that manages IP assignment and drives the ENI synchronization controller, keeping DPDK and kernel interfaces on one plane. 
+  Monitor capacity and alert before exhaustion by tracking subnet IP usage and ENI secondary-IP counts, alerting above 80% usage so subnets can be expanded or instances migrated before allocation fails. 
+  Validate routing and security-group enforcement after synchronization is in place, confirming that traffic to secondary-interface IPs routes correctly and that security-group rules apply, testing both intra-VPC and cross-VPC patterns. \#\# Resources **Key AWS services:** 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [Amazon VPC IP Address Manager (IPAM)](https://aws.amazon.com/vpc/) 
+  [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 