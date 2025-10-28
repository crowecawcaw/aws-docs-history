# Permissions required to run the login nodes pool

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
              - elasticloadbalancing:AddTags
              - elasticloadbalancing:CreateLoadBalancer
            Resource: '*'
            Effect: Allow
```
