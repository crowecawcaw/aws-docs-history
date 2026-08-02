# Create the role and attach it to your test

Save the trust policy as `trust-policy.json` and the permissions policy as `permissions-policy.json`, then create the role with the AWS CLI.

```
aws iam create-role \
  --role-name `my-resilience-testing-role` \
  --assume-role-policy-document file://trust-policy.json

aws iam put-role-policy \
  --role-name `my-resilience-testing-role` \
  --policy-name resilience-testing \
  --policy-document file://permissions-policy.json
```

Set the role on your test so that Resilience Hub uses it for test runs.

```
aws resiliencehubv2 update-test \
  --test-id `test-id` \
  --role-name `my-resilience-testing-role`
```
