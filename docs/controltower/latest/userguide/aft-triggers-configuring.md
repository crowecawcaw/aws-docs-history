# Configuring customization triggers

To enable customization triggers, set the `aft_customization_triggers`
variable in your AFT deployment module:

```
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"

  aft_customization_triggers = ["account_move"]

  # ... other variables
}
```

The only valid value is `"account_move"`. To disable customization
triggers, set the variable to an empty list (`[]`). The feature is disabled
by default.

To exclude a specific account from automatic trigger processing, set the
`account_skip_customization_triggers` attribute to `"true"`
for the target account in the account request Terraform file. When this attribute is
set, AFT skips customization invocation for that account even when it detects an OU
change. This is useful for accounts undergoing planned migrations where automatic
re-customization is not desired.
