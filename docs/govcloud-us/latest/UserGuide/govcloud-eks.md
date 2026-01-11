# Amazon Elastic Kubernetes Service in AWS GovCloud (US)

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that makes it easy for you to run Kubernetes on AWS without needing to stand up or maintain your own Kubernetes control plane. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.

## How Amazon EKS differs for AWS GovCloud (US)

- [Amazon EKS on Fargate](../../../eks/latest/userguide/fargate.md "../../../eks/latest/userguide/fargate.md") isn’t available.
- [Amazon Managed Service for Prometheus](../../../eks/latest/userguide/prometheus.md "../../../eks/latest/userguide/prometheus.md") isn’t available.
- The Mountpoint for Amazon S3 CSI driver isn’t available as an Amazon EKS add-on and self-managed installation isn’t officially supported.
- Amazon EKS Anywhere isn’t available.
- Amazon EKS Hybrid Nodes isn’t available.

## Documentation for Amazon EKS

[Amazon EKS documentation](../../../eks.md "../../../eks.md").

Amazon Application Recovery Controller’s (ARC) Zonal Shift in Amazon EKS is supported. For more information, see [Learn about Amazon Application Recovery Controller’s (ARC) Zonal Shift in Amazon EKS](../../../eks/latest/userguide/zone-shift.md "../../../eks/latest/userguide/zone-shift.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Do not enter export-controlled data in the following fields:
  - Cluster name
  - Fargate profile name
  - Node group name

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
