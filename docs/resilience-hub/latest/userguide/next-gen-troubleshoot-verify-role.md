

# Verifying role configuration
<a name="next-gen-troubleshoot-verify-role"></a>

Check that your invoker role is correctly configured using the following AWS CLI commands.

To verify that the role exists:

```
aws iam get-role --role-name AWSResilienceHubAssessmentRole
```

To verify the trust policy:

```
aws iam get-role --role-name AWSResilienceHubAssessmentRole \
  --query 'Role.AssumeRolePolicyDocument'
```

To simulate whether a principal can perform required actions:

```
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/AWSResilienceHubAssessmentRole \
  --action-names resiliencehub:GetService resiliencehub:StartFailureModeAssessment
```