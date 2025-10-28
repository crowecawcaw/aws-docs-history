# Amazon EKS Audit Logs in Security Lake

When you add Amazon EKS Audit Logs as a source, Security Lake starts collecting in-depth information
about the activities performed on the Kubernetes resources running in your Elastic
Kubernetes Service (EKS) clusters. EKS Audit Logs help you detect potentially suspicious
activities in your EKS clusters within the Amazon Elastic Kubernetes Service.

Security Lake consumes EKS Audit Log events directly from the Amazon EKS control plane logging
feature through an independent and duplicative stream of audit logs. This process is
designed to not require additional set up or affect existing Amazon EKS control plane logging
configurations that you might have. For more information, see [Amazon EKS
control plane logging](../../../eks/latest/userguide/control-plane-logs.md "../../../eks/latest/userguide/control-plane-logs.md") in the **Amazon EKS User Guide**.

Amazon EKS audit logs is supported only in OCSF v1.1.0. For information about how Security Lake
normalizes EKS Audit Logs events to OCSF, see the mapping reference in the [GitHub OCSF repository for Amazon EKS Audit Logs events (v1.1.0)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/EKS Audit Logs "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/EKS Audit Logs").
