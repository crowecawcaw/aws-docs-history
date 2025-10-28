# EKS Hybrid Nodes and network disconnections

The EKS Hybrid Nodes architecture can be new to customers who are accustomed to running local Kubernetes clusters entirely in their own data centers or edge locations. With EKS Hybrid Nodes, the Kubernetes control plane runs in an AWS Region and only the nodes run on-premises, resulting in a “stretched” or “extended” Kubernetes cluster architecture.

This leads to a common question, “What happens if my nodes get disconnected from the Kubernetes control plane?”

In this guide, we answer that question through a review of the following topics. It is recommended to validate the stability and reliability of your applications through network disconnections as each application may behave differently based on its dependencies, configuration, and environment. See the aws-samples/eks-hybrid-examples GitHub repo for test setup, procedures, and results you can reference to test network disconnections with EKS Hybrid Nodes and your own applications. The GitHub repo also contains additional details of the tests used to validate the behavior explained in this guide.

- [Best practices for stability through network disconnections](hybrid-nodes-network-disconnection-best-practices.md "hybrid-nodes-network-disconnection-best-practices.md")
- [Kubernetes pod failover behavior through network disconnections](hybrid-nodes-kubernetes-pod-failover.md "hybrid-nodes-kubernetes-pod-failover.md")
- [Application network traffic through network disconnections](hybrid-nodes-app-network-traffic.md "hybrid-nodes-app-network-traffic.md")
- [Host credentials through network disconnections](hybrid-nodes-host-creds.md "hybrid-nodes-host-creds.md")
