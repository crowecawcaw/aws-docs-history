# Troubleshooting AWS Batch

You might need to troubleshoot issues that are related to your compute environments, job
queues, job definitions, or jobs. This chapter describes how to troubleshoot and resolve such
issues in your AWS Batch environment.

AWS Batch uses IAM policies, roles, and permissions, and runs on Amazon EC2, Amazon ECS, AWS Fargate,
and Amazon Elastic Kubernetes Service infrastructure. To troubleshoot issues that are related to these services, see the
following:

- [Troubleshooting
  IAM](../../../IAM/latest/UserGuide/troubleshoot.md "../../../IAM/latest/UserGuide/troubleshoot.md") in the _IAM User Guide_
- [Amazon ECS
  troubleshooting](../../../AmazonECS/latest/userguide/troubleshooting.md "../../../AmazonECS/latest/userguide/troubleshooting.md") in the _Amazon Elastic Container Service Developer Guide_
- [Amazon EKS
  troubleshooting](../../../eks/latest/userguide/troubleshooting.md "../../../eks/latest/userguide/troubleshooting.md") in the _Amazon EKS User Guide_
- [Troubleshoot EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md "../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md") in the _Amazon EC2 User Guide_

###### Contents

- [AWS Batch](batch-troubleshooting.md "batch-troubleshooting.md")
  - [Optimal instance type configuration to
    receive automatic instance family updates](optimal-default-instance-troubleshooting.md "optimal-default-instance-troubleshooting.md")
  - [INVALID compute environment](invalid_compute_environment.md "invalid_compute_environment.md")
    - [Incorrect role name or ARN](invalid_compute_environment.md#invalid_service_role_arn "invalid_compute_environment.md#invalid_service_role_arn")
    - [Repair an INVALID compute
      environment](invalid_compute_environment.md#repairing_invalid_compute_environment "invalid_compute_environment.md#repairing_invalid_compute_environment")

  - [Jobs stuck in a RUNNABLE status](job_stuck_in_runnable.md "job_stuck_in_runnable.md")
  - [Spot Instances not tagged on creation](spot-instance-no-tag.md "spot-instance-no-tag.md")
  - [Spot Instances not scaling down](spot-fleet-not-authorized.md "spot-fleet-not-authorized.md")
    - [Attach
      AmazonEC2SpotFleetTaggingRole managed policy to your Spot Fleet role in
      the AWS Management Console](spot-fleet-not-authorized.md#spot-fleet-not-authorized-console "spot-fleet-not-authorized.md#spot-fleet-not-authorized-console")
    - [Attach
      AmazonEC2SpotFleetTaggingRole managed policy to your Spot Fleet role
      with the AWS CLI](spot-fleet-not-authorized.md#spot-fleet-not-authorized-cli "spot-fleet-not-authorized.md#spot-fleet-not-authorized-cli")

  - [Can't retrieve Secrets Manager secrets](troubleshooting-cant-specify-secrets.md "troubleshooting-cant-specify-secrets.md")
  - [Can't override job definition resource
    requirements](override-resource-requirements.md "override-resource-requirements.md")
  - [Error message when you update the
    desiredvCpus setting](error-desired-vcpus-update.md "error-desired-vcpus-update.md")

- [AWS Batch on Amazon EKS](batch-eks-troubleshooting.md "batch-eks-troubleshooting.md")
  - [INVALID compute
    environment](batch_eks_invalid_compute_environment.md "batch_eks_invalid_compute_environment.md")
    - [Unsupported Kubernetes version](batch_eks_invalid_compute_environment.md#invalid_kubernetes_version "batch_eks_invalid_compute_environment.md#invalid_kubernetes_version")
    - [Instance profile doesn't exist](batch_eks_invalid_compute_environment.md#instance_profile_not_exist "batch_eks_invalid_compute_environment.md#instance_profile_not_exist")
    - [Invalid Kubernetes namespace](batch_eks_invalid_compute_environment.md#invalid_kubernetes_namespace "batch_eks_invalid_compute_environment.md#invalid_kubernetes_namespace")
    - [Deleted compute environment](batch_eks_invalid_compute_environment.md#deleted_compute_environment "batch_eks_invalid_compute_environment.md#deleted_compute_environment")
    - [Nodes don't join the Amazon EKS cluster](batch_eks_invalid_compute_environment.md#batch_eks_node_not_join_cluster "batch_eks_invalid_compute_environment.md#batch_eks_node_not_join_cluster")

  - [AWS Batch on Amazon EKS job is stuck in
    RUNNABLE status](batch_eks_job_stuck_in_runnable.md "batch_eks_job_stuck_in_runnable.md")
  - [AWS Batch on Amazon EKS job is stuck in
    STARTING status](batch-eks-job-stuck-in-starting.md "batch-eks-job-stuck-in-starting.md")
    - [Scenario: Persisted Volume Claim Attach or Mount Failure](batch-eks-job-stuck-in-starting.md#batch-eks-job-stuck-in-starting-scenario "batch-eks-job-stuck-in-starting.md#batch-eks-job-stuck-in-starting-scenario")

  - [Verify that the aws-auth ConfigMap is
    configured correctly](verify-configmap-config.md "verify-configmap-config.md")
  - [RBAC permissions or bindings aren't configured properly](batch_eks_rbac.md "batch_eks_rbac.md")
