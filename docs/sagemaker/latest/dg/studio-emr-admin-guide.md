# Admin guide

This section provides prerequisites, networking instructions for allowing the
communication between Studio or Studio Classic and Amazon EMR clusters. It covers different
deployment scenarios - when Studio and Amazon EMR are provisioned within private Amazon VPCs
without public internet access, as well as when they need to communicate over the
internet.

It walks through how administrators can use the AWS Service Catalog to make AWS CloudFormation templates available
to Studio, allowing data scientists to discover and self-provision Amazon EMR clusters
directly from within Studio. This involves creating a Service Catalog portfolio, granting
requisite permissions, referencing the Amazon EMR templates, and parameterizing them to enable
customizations during cluster creation.

Last, it provides guidance on configuring discoverability of existing running Amazon EMR
clusters from Studio, and Studio Classic, covering single account and cross-account access
scenarios along with the necessary IAM permissions.

###### Topics

- [Configure Amazon EMR CloudFormation
  templates in the Service Catalog](studio-notebooks-set-up-emr-templates.md "studio-notebooks-set-up-emr-templates.md")
- [Configure
  listing Amazon EMR clusters](studio-notebooks-configure-discoverability-emr-cluster.md "studio-notebooks-configure-discoverability-emr-cluster.md")
- [Configure IAM runtime roles for Amazon EMR
  cluster access in Studio](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md")
- [Reference policies](studio-set-up-emr-permissions-reference.md "studio-set-up-emr-permissions-reference.md")
