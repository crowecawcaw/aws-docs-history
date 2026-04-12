# Policy create and update: per-policy engine validation

When creating or updating policies directly (not through generation), validation and analysis takes into account the new policy as well as its interactions with **all preexisting policies** in the policy engine.

## How it works

1. The policy is validated against the Cedar schema for **all gateways** associated with the policy engine
2. Analysis runs in the context of the **entire policy engine**
3. The validation mode determines whether creation fails on findings. For more information about validation modes, see [Add policies to the Policy Engine](add-policies-to-engine.md "add-policies-to-engine.md")

## Example: Create a policy with validation

Create a policy with strict validation that rejects policies with any findings:

```
aws bedrock-agentcore-control create-policy \
  --policy-engine-id MyEngine-abc123 \
  --name RestrictRefunds \
  --validation-mode FAIL_ON_ANY_FINDINGS \
  --definition '{
    "cedar": {
      "statement": "forbid(\n  principal,\n  action == Action::\"processRefund\",\n  resource\n) when {\n  context.amount > 1000\n};"
    }
  }'
```

The response indicates the policy is being created:

```
{
  "policyId": "RestrictRefunds-ghi789",
  "status": "CREATING"
}
```

Check the policy status to confirm validation passed:

```
aws bedrock-agentcore-control get-policy \
  --policy-engine-id MyEngine-abc123 \
  --policy-id RestrictRefunds-ghi789
```

When validation passes, the policy becomes active:

```
{
  "policyId": "RestrictRefunds-ghi789",
  "status": "ACTIVE",
  "statusReasons": []
}
```

## Example: Validation failure

If a policy references an action that doesn’t exist in any associated gateway’s schema, validation fails:

```
aws bedrock-agentcore-control create-policy \
  --policy-engine-id MyEngine-abc123 \
  --name InvalidPolicy \
  --validation-mode FAIL_ON_ANY_FINDINGS \
  --definition '{
    "cedar": {
      "statement": "permit(\n  principal,\n  action == Action::\"nonExistentTool\",\n  resource\n);"
    }
  }'
```

When you check the policy status, the response shows the validation failure:

```
aws bedrock-agentcore-control get-policy \
  --policy-engine-id MyEngine-abc123 \
  --policy-id InvalidPolicy-jkl012
```

```
{
  "policyId": "InvalidPolicy-jkl012",
  "status": "CREATE_FAILED",
  "statusReasons": [
    "Validation failed: Action 'nonExistentTool' is not defined in the schema for any associated gateway"
  ]
}
```
