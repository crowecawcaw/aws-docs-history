# Onboard to monitoring and incident management for Amazon EKS in AMS Accelerate

Perform the following steps to onboard to monitoring and incident management for Amazon EKS.

1. **Enable Amazon EKS cost optimization tags:** See
   [Tagging your resources for billing](../../../eks/latest/userguide/eks-using-tags.md#tag-resources-for-billing "../../../eks/latest/userguide/eks-using-tags.md#tag-resources-for-billing") in the
   **Amazon EKS User Guide**.
2. **Initiate onboarding of monitoring and incident management for EKS:**
   Contact your Cloud Service Delivery Manager (CSDM) with account IDs and cluster names to onboard.
3. **Validate requirements:** Your Cloud Architect (CA) validates that all [requirements](acc-requirements.md "acc-requirements.md") are
   met before onboarding begins.
4. **Update Kubernetes role-based access control (RBAC):** AMS shares the `eksctl` commands to implement these changes.
   You can review these changes
   and then deploy. You must deploy RBAC updates so that AMS has permissions to run commands on your behalf.
   These updates include mapping the AMS IAM role to a Kubernetes user, creating a new Kubernetes cluster role for AMS, and binding the AMS Kubernetes cluster role to the
   user.
5. **Deploy cluster components:** AMS deploys the following components in an AMS-managed namespace on your cluster:
   - Prometheus server
   - Prometheus node exporter (not applicable for AWS Fargate)
   - kube-state-metrics

6. **Perform Prometheus configuration updates:** AMS configures Prometheus to enable remote-write for metrics.
7. **(Optional) Configure dashboards:** Your CA helps you configure Amazon Managed Grafana dashboards in your account.

###### Note

After your Amazon EKS cluster is onboarded, AMS analyzes alert signals and performs a baseline assessment to identify existing issues in your cluster. After the baseline
assessment is complete, AMS shares findings and remediation recommendations through Trusted Advisor and a service request that you can use to address issues in your cluster.
From the assessment, AMS creates an Amazon EKS monitoring baseline specific to your EKS clusters by adjusting our account-level alarm thresholds.
To eliminate duplicate AMS responses against these findings, we adjust our monitoring to exclude those alert signals. We readjust our monitoring to include the signals when
your CSDM informs us that the underlying issues have been remediated.
