# AWS

managed policy: AmazonSageMakerHyperPodObservabilityAdminAccess

This policy provides administrative privileges required for setting up Amazon SageMaker HyperPod
observability. It enables access to Amazon Managed Service for Prometheus, Amazon Managed Grafana and Amazon Elastic Kubernetes Service add-ons. The policy
also includes broad access to Grafana HTTP APIs through ServiceAccountTokens across all
Amazon Managed Grafana workspaces in your account.

###### Permission details

The following list provides an overview of the permissions that are included in this
policy.

- `prometheus` – Create and manage Amazon Managed Service for Prometheus workspaces and rule
  groups
- `grafana` – Creates and manages Amazon Managed Grafana workspaces and service
  accounts
- `eks` – Creates and manages the
  `amazon-sagemaker-hyperpod-observability` Amazon EKS add-on
- `iam` – Passes specific IAM service roles to Amazon Managed Grafana and
  Amazon EKS
- `sagemaker` – Lists and describes SageMaker HyperPod clusters
- `sso` – Creates and manages IAM Identity Center application instances for
  Amazon Managed Grafana setup
- `tag` – Tags Amazon Managed Service for Prometheus, Amazon Managed Grafana, and Amazon EKS add-on resources
  To view the policy JSON, see [AmazonSageMakerHyperPodObservabilityAdminAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodObservabilityAdminAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerHyperPodObservabilityAdminAccess.md").
