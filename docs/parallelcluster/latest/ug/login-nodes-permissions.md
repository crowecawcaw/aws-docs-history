

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Permissions required to run the login nodes pool
<a name="login-nodes-permissions"></a>

In order to manage the login nodes pool the cluster administrator must have the following additional permissions: 

```
            - Action:
              - iam:CreateServiceLinkedRole
              - autoscaling:DeleteAutoScalingGroup
              - autoscaling:DeleteLifecycleHook
              - autoscaling:Describe*
              - autoscaling:PutLifecycleHook
              - autoscaling:UpdateAutoScalingGroup
              - elasticloadbalancing:CreateListener
              - elasticloadbalancing:CreateTargetGroup
              - elasticloadbalancing:DeleteListener
              - elasticloadbalancing:DeleteLoadBalancer
              - elasticloadbalancing:DeleteTargetGroup
              - elasticloadbalancing:Describe*
              - elasticloadbalancing:ModifyLoadBalancerAttributes
            Resource: '*'
            Condition:
              ForAllValues:StringEquals:
                aws:TagKeys: [ "parallelcluster:cluster-name" ]
            - Action:
              - autoscaling:CreateAutoScalingGroup
              - autoscaling:DeleteTags
              - autoscaling:CreateOrUpdateTags
              - elasticloadbalancing:AddTags
              - elasticloadbalancing:CreateLoadBalancer
              - elasticloadbalancing:RemoveTags
              - elasticloadbalancing:ModifyTargetGroup
            Resource: '*'
            Effect: Allow
```