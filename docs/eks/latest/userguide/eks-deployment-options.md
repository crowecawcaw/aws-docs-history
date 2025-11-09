**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy Amazon EKS clusters across cloud and on-premises environments

## Understand Amazon EKS deployment options

Amazon Elastic Kubernetes Service (Amazon EKS) is a fully managed Kubernetes service that enables you to run Kubernetes seamlessly in the cloud and in your on-premises environments.

In the cloud, Amazon EKS automates Kubernetes cluster infrastructure management for the Kubernetes control plane and nodes. This is essential for scheduling containers, managing application availability, dynamically scaling resources, optimizing compute, storing cluster data, and performing other critical functions. With Amazon EKS, you get the robust performance, scalability, reliability, and availability of AWS infrastructure, along with native integrations with AWS networking, security, storage, and observability services.

To simplify running Kubernetes in your on-premises environments, you can use the same Amazon EKS clusters, features, and tools to [Create Amazon Linux nodes on AWS Outposts](eks-outposts-self-managed-nodes.md "eks-outposts-self-managed-nodes.md") or [Amazon EKS Hybrid Nodes](hybrid-nodes-overview.md "hybrid-nodes-overview.md") on your own infrastructure, or you can use [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/ "https://anywhere.eks.amazonaws.com/") for self-contained air-gapped environments.

## Amazon EKS in the cloud

You can use Amazon EKS with compute in AWS Regions, AWS Local Zones, and AWS Wavelength Zones. With Amazon EKS in the cloud, the security, scalability, and availability of the Kubernetes control plane is fully managed by AWS in the AWS Region. When running applications with compute in AWS Regions, you get the full breadth of AWS and Amazon EKS features, including Amazon EKS Auto Mode, which fully automates Kubernetes cluster infrastructure management for compute, storage, and networking on AWS with a single click. When running applications with compute in AWS Local Zones and AWS Wavelength Zones, you can use Amazon EKS self-managed nodes to connect Amazon EC2 instances for your cluster compute and can use the other available AWS services in AWS Local Zones and AWS Wavelength Zones. For more information see [AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/") and [AWS Wavelength Zones features](https://aws.amazon.com/wavelength/features/ "https://aws.amazon.com/wavelength/features/").

|                                      | Amazon EKS in AWS Regions                                                                                      | Amazon EKS in Local/Wavelength Zones                                                   |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Kuberenetes control plane management | AWS-managed                                                                                                    | AWS-managed                                                                            |
| Kubernetes control plane location    | AWS Regions                                                                                                    | AWS Regions                                                                            |
| Kubernetes data plane                | • Amazon EKS Auto Mode<br>• Amazon EKS Managed Node Groups<br>• Amazon EC2 self-managed nodes<br>• AWS Fargate | • Amazon EKS Managed Node Groups (Local Zones only)<br>• Amazon EC2 self-managed nodes |
| Kubernetes data plane location       | AWS Regions                                                                                                    | AWS Local or Wavelength Zones                                                          |

## Amazon EKS in your data center or edge environments

If you need to run applications in your own data centers or edge environments, you can use [Deploy Amazon EKS on-premises with AWS Outposts](eks-outposts.md "eks-outposts.md") or [Amazon EKS Hybrid Nodes](hybrid-nodes-overview.md "hybrid-nodes-overview.md"). You can use self-managed nodes with Amazon EC2 instances on AWS Outposts for your cluster compute, or you can use Amazon EKS Hybrid Nodes with your own on-premises or edge infrastructure for your cluster compute. AWS Outposts is AWS-managed infrastructure that you run in your data centers or co-location facilities, whereas Amazon EKS Hybrid Nodes runs on your physical or virtual machines that you manage in your on-premises or edge environments. Amazon EKS on AWS Outposts and Amazon EKS Hybrid Nodes require a reliable connection from your on-premises environments to an AWS Region, and you can use the same Amazon EKS clusters, features, and tools you use to run applications in the cloud. When running on AWS Outposts, you can alternatively deploy the entire Kubernetes cluster on AWS Outposts with Amazon EKS local clusters on AWS Outposts.

|                                      | Amazon EKS Hybrid Nodes                       | Amazon EKS on AWS Outposts               |
| ------------------------------------ | --------------------------------------------- | ---------------------------------------- |
| Kuberenetes control plane management | AWS-managed                                   | AWS-managed                              |
| Kubernetes control plane location    | AWS Regions                                   | AWS Regions or AWS Outposts              |
| Kubernetes data plane                | Customer-managed physical or virtual machines | Amazon EC2 self-managed nodes            |
| Kubernetes data plane location       | Customer data center or edge environment      | Customer data center or edge environment |

## Amazon EKS Anywhere for air-gapped environments

[Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/ "https://aws.amazon.com/eks/eks-anywhere/") simplifies Kubernetes cluster management through the automation of undifferentiated heavy lifting such as infrastructure setup and Kubernetes cluster lifecycle operations in on-premises and edge environments. Unlike Amazon EKS, Amazon EKS Anywhere is a customer-managed product and customers are responsible for cluster lifecycle operations and maintenance of Amazon EKS Anywhere clusters. Amazon EKS Anywhere is built on the Kubernetes sub-project Cluster API (CAPI) and supports a range of infrastructure including VMware vSphere, bare metal, Nutanix, Apache CloudStack, and AWS Snow. Amazon EKS Anywhere can be run in air-gapped environments and offers optional integrations with regional AWS services for observability and identity management. To receive support for Amazon EKS Anywhere and access to AWS-vended Kubernetes add-ons, you can purchase [Amazon EKS Anywhere Enterprise Subscriptions](https://aws.amazon.com/eks/eks-anywhere/pricing/ "https://aws.amazon.com/eks/eks-anywhere/pricing/").

|                                      | Amazon EKS Anywhere                           |
| ------------------------------------ | --------------------------------------------- |
| Kuberenetes control plane management | Customer-managed                              |
| Kubernetes control plane location    | Customer data center or edge environment      |
| Kubernetes data plane                | Customer-managed physical or virtual machines |
| Kubernetes data plane location       | Customer data center or edge environment      |

## Amazon EKS tooling

You can use the [Amazon EKS Connector](eks-connector.md "eks-connector.md") to register and connect any conformant Kubernetes cluster to AWS and view it in the Amazon EKS console. After a cluster is connected, you can see the status, configuration, and workloads for that cluster in the Amazon EKS console. You can use this feature to view connected clusters in Amazon EKS console, but the Amazon EKS Connector does not enable management or mutating operations for your connected clusters through the Amazon EKS console.

[Amazon EKS Distro](https://aws.amazon.com/eks/eks-distro/ "https://aws.amazon.com/eks/eks-distro/") is the AWS distribution of the underlying Kubernetes components that power all Amazon EKS offerings. It includes the core components required for a functioning Kubernetes cluster such as Kubernetes control plane components (etcd, kube-apiserver, kube-scheduler, kube-controller-manager) and networking components (CoreDNS, kube-proxy, CNI plugins). Amazon EKS Distro can be used to self-manage Kubernetes clusters with your choice of tooling. Amazon EKS Distro deployments are not covered by AWS Support Plans.
