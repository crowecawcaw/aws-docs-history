# Using Amazon SageMaker Unified Studio with Trusted Identity Propagation on Amazon EMR on EC2

These tutorials demonstrate how to use Amazon Amazon SageMaker Unified Studio (Amazon SageMaker Unified Studio) with trusted identity propagation (TIP) on Amazon EMR on EC2 clusters. You can use either Full Table Access (FTA) mode or Fine-Grained Access Control (FGAC) mode depending on your access control requirements.

These tutorials cover the following:

- **Common setup** — Shared prerequisites for both FTA and FGAC, including IAM Identity Center, Lake Formation, and Amazon SageMaker Unified Studio domain configuration.
- **Connect existing clusters** — Steps to connect an existing TIP-enabled Amazon EMR on EC2 cluster to Amazon SageMaker Unified Studio.
- **Full Table Access (FTA)** — Grant authorized users access to full tables without row or column filtering.
- **Fine-Grained Access Control (FGAC)** — Enforce row-level, column-level, and cell-level permissions.

###### Note

The resources you create in these tutorials might result in charges to your AWS account. These tutorials create Amazon EMR on EC2 clusters, Amazon SageMaker Unified Studio domains and projects, and Lake Formation resources. To avoid ongoing charges, delete the resources when you are done, as described in the clean up steps at the end of each flow. For pricing information, see the applicable service pricing pages.

###### Topics

- [Common setup for Amazon SageMaker Unified Studio with TIP on Amazon EMR on EC2](emr-trusted-identity-smus-tip-common-setup.md "emr-trusted-identity-smus-tip-common-setup.md")
- [Full Table Access with Amazon SageMaker Unified Studio and TIP on Amazon EMR on EC2](emr-trusted-identity-smus-fta.md "emr-trusted-identity-smus-fta.md")
- [Fine-Grained Access Control with Amazon SageMaker Unified Studio and TIP on Amazon EMR on EC2](emr-trusted-identity-smus-fgac.md "emr-trusted-identity-smus-fgac.md")
