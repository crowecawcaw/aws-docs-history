# Create the roles and attach them to your test

In the orchestrator account, create the orchestrator role.

```
aws iam create-role \
  --role-name `my-orchestrator-role` \
  --assume-role-policy-document file://orchestrator-trust-policy.json

aws iam put-role-policy \
  --role-name `my-orchestrator-role` \
  --policy-name resilience-testing-orchestrator \
  --policy-document file://orchestrator-permissions-policy.json
```

In each target account, create the target role with the permissions policy for your test template.

```
aws iam create-role \
  --role-name `my-target-role` \
  --assume-role-policy-document file://target-trust-policy.json

aws iam put-role-policy \
  --role-name `my-target-role` \
  --policy-name resilience-testing-target \
  --policy-document file://target-permissions-policy.json
```

Set the orchestrator role as the execution role on your test.

```
aws resiliencehubv2 update-test \
  --test-id `test-id` \
  --role-name `my-orchestrator-role`
```
