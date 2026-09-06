

# Target account role
<a name="next-gen-resilience-testing-iam-ma-target"></a>

Create a target role in each account that contains targeted resources. Its trust policy allows the orchestrator role to assume it. The `sts:ExternalId` condition restricts the assume operation to AWS FIS experiments owned by the orchestrator account. The `aws:PrincipalArn` condition pins the trust to the orchestrator role.

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Sid": "OrchestratorRoleAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "AWS": "{{orchestrator-account-id}}"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringLike": {
          "sts:ExternalId": "arn:aws:fis:*:{{orchestrator-account-id}}:experiment/*"
        },
        "ArnEquals": {
          "aws:PrincipalArn": "arn:aws:iam::{{orchestrator-account-id}}:role/{{orchestrator-role-name}}"
        }
      }
    }
  ]
}
```

Attach the permissions policy for the test template that your test uses. These policies grant the fault-injection permissions for the targeted resources. Experiment logging and lifecycle permissions are granted by the orchestrator role, not the target role.

**Topics**
+ [Availability Zone: recovery](next-gen-resilience-testing-iam-ma-az-recovery.md)
+ [Dependency validation](next-gen-resilience-testing-iam-ma-dependency-validation.md)
+ [Multi-Region: isolation](next-gen-resilience-testing-iam-ma-multi-region-isolation.md)
+ [Multi-Region: recovery](next-gen-resilience-testing-iam-ma-multi-region-recovery.md)