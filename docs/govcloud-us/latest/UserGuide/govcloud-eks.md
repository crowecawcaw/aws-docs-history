

# Amazon Elastic Kubernetes Service (Amazon EKS) in AWS GovCloud (US)
<a name="govcloud-eks"></a>

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that makes it easy for you to run Kubernetes on AWS without needing to stand up or maintain your own Kubernetes control plane. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon EKS differs
<a name="govcloud-eks-diffs"></a>

The following differences apply to Amazon EKS:
+  [Amazon EKS on Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html) isn’t available.
+  [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html) isn’t available.
+  Amazon EKS Anywhere isn’t available.
+  Amazon EKS Hybrid Nodes isn’t available.
+  [Amazon Application Recovery Controller’s (ARC) Zonal Shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in Amazon EKS is supported.

## Documentation
<a name="govcloud-eks-docs"></a>
+  [Amazon EKS documentation](https://docs.aws.amazon.com/eks/) 

## Export-controlled content
<a name="govcloud-eks-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Do not enter export-controlled data in the following fields:
  + Cluster name
  + Fargate profile name
  + Node group name

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md).