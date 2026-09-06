

# Troubleshooting AWS Batch
<a name="troubleshooting"></a>

You might need to troubleshoot issues that are related to your compute environments, job queues, job definitions, or jobs. This chapter describes how to troubleshoot and resolve such issues in your AWS Batch environment.

AWS Batch uses IAM policies, roles, and permissions, and runs on Amazon EC2, Amazon ECS, AWS Fargate, and Amazon Elastic Kubernetes Service infrastructure. To troubleshoot issues that are related to these services, see the following:
+ [Troubleshooting IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html) in the *IAM User Guide*
+ [Amazon ECS troubleshooting](https://docs.aws.amazon.com/AmazonECS/latest/userguide/troubleshooting.html) in the *Amazon Elastic Container Service Developer Guide*
+ [Amazon EKS troubleshooting](https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting.html) in the *Amazon EKS User Guide*
+ [Troubleshoot EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html) in the *Amazon EC2 User Guide*

**Contents**
+ [AWS Batch](batch-troubleshooting.md)
  + [Optimal instance type configuration to receive automatic instance family updates](optimal-default-instance-troubleshooting.md)
  + [`INVALID` compute environment](invalid_compute_environment.md)
    + [Incorrect role name or ARN](invalid_compute_environment.md#invalid_service_role_arn)
    + [Repair an `INVALID` compute environment](invalid_compute_environment.md#repairing_invalid_compute_environment)
  + [Jobs stuck in a `RUNNABLE` status](job_stuck_in_runnable.md)
    + [Jobs stuck in RUNNABLE due to capacity](job_stuck_in_runnable_capacity.md)
    + [Jobs stuck in RUNNABLE due to misconfiguration](job_stuck_in_runnable_misconfiguration.md)
    + [Jobs stuck in RUNNABLE due to invalid compute environments](job_stuck_in_runnable_invalid_ce.md)
    + [Jobs stuck in RUNNABLE with undetermined root cause](job_stuck_in_runnable_undetermined.md)
    + [Automatic remediation with `jobStateTimeLimitActions`](job_stuck_in_runnable_time_limit_actions.md)
    + [Common causes of jobs stuck in RUNNABLE without a `statusReason`](job_stuck_in_runnable_common_causes.md)
  + [Spot Instances not tagged on creation](spot-instance-no-tag.md)
  + [Spot Instances not scaling down](spot-fleet-not-authorized.md)
    + [Attach **AmazonEC2SpotFleetTaggingRole** managed policy to your Spot Fleet role in the AWS Management Console](spot-fleet-not-authorized.md#spot-fleet-not-authorized-console)
    + [Attach **AmazonEC2SpotFleetTaggingRole** managed policy to your Spot Fleet role with the AWS CLI](spot-fleet-not-authorized.md#spot-fleet-not-authorized-cli)
  + [Can't retrieve Secrets Manager secrets](troubleshooting-cant-specify-secrets.md)
  + [Can't override job definition resource requirements](override-resource-requirements.md)
  + [Error message when you update the `desiredvCpus` setting](error-desired-vcpus-update.md)
+ [AWS Batch on Amazon EKS](batch-eks-troubleshooting.md)
  + [`INVALID` compute environment](batch_eks_invalid_compute_environment.md)
    + [Unsupported Kubernetes version](batch_eks_invalid_compute_environment.md#invalid_kubernetes_version)
    + [Instance profile doesn't exist](batch_eks_invalid_compute_environment.md#instance_profile_not_exist)
    + [Invalid Kubernetes namespace](batch_eks_invalid_compute_environment.md#invalid_kubernetes_namespace)
    + [Deleted compute environment](batch_eks_invalid_compute_environment.md#deleted_compute_environment)
    + [Nodes don't join the Amazon EKS cluster](batch_eks_invalid_compute_environment.md#batch_eks_node_not_join_cluster)
  + [AWS Batch on Amazon EKS job is stuck in `RUNNABLE` status](batch_eks_job_stuck_in_runnable.md)
  + [AWS Batch on Amazon EKS job is stuck in `STARTING` status](batch-eks-job-stuck-in-starting.md)
    + [Scenario: Persisted Volume Claim Attach or Mount Failure](batch-eks-job-stuck-in-starting.md#batch-eks-job-stuck-in-starting-scenario)
  + [Verify that the `aws-auth ConfigMap` is configured correctly](verify-configmap-config.md)
  + [RBAC permissions or bindings aren't configured properly](batch_eks_rbac.md)
+ [AWS Batch for SageMaker Training jobs](batch-sm-troubleshooting.md)
  + [Jobs stuck in a `RUNNABLE` status](sm_job_stuck_in_runnable.md)
    + [Jobs stuck in `RUNNABLE` due to capacity](sm_job_stuck_in_runnable_capacity.md)
    + [Jobs stuck in `RUNNABLE` due to misconfiguration](sm_job_stuck_in_runnable_misconfiguration.md)
    + [Automatic remediation with `jobStateTimeLimitActions`](sm_job_stuck_in_runnable_time_limit_actions.md)