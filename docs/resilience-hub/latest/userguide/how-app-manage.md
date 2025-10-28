# Select how this application is managed

In addition to AWS CloudFormation stacks, AWS Resource Groups, myApplications applications, and Terraform state
files, you can add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters. That is, AWS Resilience Hub
allows you to add resources that are located on your Amazon EKS clusters as optional resources. This
section provides the following options, which help you to determine the location of your
application resources.

- **Resource collections** – Select this option if you want to
  discover resources from one of the resource collections. Resource collections include AWS CloudFormation
  stacks, AWS Resource Groups, myApplications applications, and Terraform state files.

If you select this option, you must complete one of the procedures in [Add resource collections](discover-structure.md#resource-collection "discover-structure.md#resource-collection").

- **EKS only** – Select this option if you want to discover
  resources from namespaces within the Amazon EKS clusters.

If you select this option, you must complete the procedure in [Add EKS clusters](discover-structure.md#add-eks-clusters "discover-structure.md#add-eks-clusters")

- **Resource collections & EKS** – Select this option if you
  want to discover resources from AWS CloudFormation stacks, AWS Resource Groups, Terraform state files, and Amazon EKS
  clusters.

If you select this option, complete one of the procedures in [Add resource collections](discover-structure.md#resource-collection "discover-structure.md#resource-collection") and then complete the procedure in [Add EKS clusters](discover-structure.md#add-eks-clusters "discover-structure.md#add-eks-clusters").

###### Note

For information about the number of resources supported per application, see [Service
Quotas](../../../general/latest/gr/resiliencehub.md#limits_resiliencehub "../../../general/latest/gr/resiliencehub.md#limits_resiliencehub").

## Next

[Add resource collections](discover-structure.md "discover-structure.md")
