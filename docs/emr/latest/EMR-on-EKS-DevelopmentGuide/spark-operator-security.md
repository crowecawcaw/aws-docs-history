# Security and the Spark operator with

Amazon EMR on EKS

There are a couple ways to set up cluster-access permissions when you use the Spark operator. The first is to use role-based access control, Role-based access control (RBAC) restricts access based on a person's role within an organization. It has
become a primary way to handle access. The second access method is to assume an AWS Identity and Access Management role, which provides resource access by means of
specific assigned permissions.

###### Topics

- [Setting up cluster access permissions
  with role-based access control (RBAC)](spark-operator-security-rbac.md "spark-operator-security-rbac.md")
- [Setting up cluster access permissions
  with IAM roles for service accounts (IRSA)](spark-operator-security-irsa.md "spark-operator-security-irsa.md")
