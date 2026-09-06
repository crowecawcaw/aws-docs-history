

# ROSA architecture
<a name="rosa-architecture-models"></a>

 Red Hat OpenShift Service on AWS (ROSA) has the following cluster topologies:
+ Hosted control plane (HCP) - The control plane is hosted within Red Hat’s AWS account and managed by Red Hat. Worker nodes are deployed in the customer’s AWS account.
+ Classic – The control plane and worker nodes are deployed in the customer’s AWS account.

ROSA with HCP offers a more efficient control plane architecture that helps reduce the AWS infrastructure fees incurred when running ROSA and allows for faster cluster creation times. Both ROSA with HCP and ROSA classic can be enabled in the AWS ROSA console. You have the choice to select which architecture you want to use when you provision ROSA clusters using the ROSA CLI.

**Note**  
 ROSA offers FedRAMP High and HIPAA Qualified compliance certifications in AWS GovCloud on both classic and hosted control plane architectures. For more information, see [Compliance](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/policies-and-service-definition#rosa-policy-process-security) in the Red Hat documentation.
 ROSA offers Federal Information Processing Standard (FIPS) endpoints in AWS GovCloud on both classic and hosted control plane architectures.

## Comparing ROSA with HCP and ROSA classic
<a name="rosa-architecture-differences"></a>

The following table compares ROSA with HCP and ROSA classic architecture models.


|  |  **ROSA with HCP**  |  **ROSA classic**  | 
| --- | --- | --- | 
| Cluster infrastructure hosting | Control plane components, such as etcd, API server, and oauth, are hosted in a Red Hat-owned AWS account. | Control plane components, such as etcd, API server, and oauth, are hosted in a customer-owned AWS account. | 
|  Amazon VPC  | Worker nodes communicate with the control plane over [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). | Worker nodes and control plane nodes are deployed in the customer’s VPC. | 
|  AWS Identity and Access Management  | Uses AWS managed policies. | Uses customer managed policies that are defined by the service. | 
| Multi-zone deployment | The control plane is deployed across multiple Availability Zones (AZs). | The control plane can be deployed within a single AZ or across multiple AZs. | 
| Infrastructure nodes | Doesn’t use dedicated infrastructure nodes. Platform components are deployed to worker nodes. | Uses two single-AZ or three multi-AZ dedicated nodes to host platform components. | 
| OpenShift capabilities | Platform monitoring, image registry, and the ingress controller are deployed in the worker nodes. | Platform monitoring, image registry, and the ingress controller are deployed in dedicated infrastructure nodes. | 
| Cluster upgrades | The control plane and each machine pool can be upgraded separately. | The entire cluster must be upgraded at the same time. | 
| Minimum Amazon EC2 footprint | Two Amazon EC2 instances are needed to create a cluster. | Seven single-AZ or nine multi-AZ Amazon EC2 instances are needed to create a cluster. | 
|  AWS Regions  | For AWS Region availability, see [Red Hat OpenShift Service on AWS endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/rosa.html) in the * AWS General Reference Guide*. | For AWS Region availability, see [Red Hat OpenShift Service on AWS endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/rosa.html) in the * AWS General Reference Guide*. | 