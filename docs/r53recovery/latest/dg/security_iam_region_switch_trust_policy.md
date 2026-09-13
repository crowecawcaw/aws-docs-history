

# Plan execution role trust policy
<a name="security_iam_region_switch_trust_policy"></a>

 Region switch assumes your plan's execution role to perform actions on your behalf. This trust policy authorizes the `arc-region-switch.amazonaws.com` service principal to assume the role. 

 Region switch assumes the execution role in two cases: 
+  Region switch assumes the execution role during plan evaluation to validate your plan configuration. For the complete list of warnings surfaced during plan evaluation, see [Plan evaluation for Region switch plans](working-with-rs-plan-evaluation.md). 
+  Region switch assumes the execution role during plan execution when an execution block acts on resources in your account, such as database failover, Auto Scaling capacity, Amazon ECS or Amazon EKS capacity, Lambda invocations, or routing-control blocks. 

 If the trust policy is missing, Region switch cannot assume the role. During plan evaluation, a warning is generated stating that the role cannot be assumed. During execution, any execution block that requires the execution role to act on resources in your account fails. The error states that the role could not be assumed. 

 The manual approval and Route 53 health check execution blocks do not assume the execution role as part of a plan execution. As a result, a plan composed only of these blocks can execute successfully even if the trust policy is missing. We recommend applying the trust policy to your execution role so that plan evaluation can identify any issues with your plan configuration. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "arc-region-switch.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------