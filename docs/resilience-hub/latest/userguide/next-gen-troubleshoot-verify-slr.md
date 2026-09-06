

# Verifying the service-linked role exists in a member account
<a name="next-gen-troubleshoot-verify-slr"></a>

From the member account, run the following command to verify the service-linked role exists:

```
aws iam get-role --role-name AWSServiceRoleForResilienceHub
```

If the role doesn't exist, verify that trusted access is enabled and wait for the reconciliation job, which runs every 12 hours.