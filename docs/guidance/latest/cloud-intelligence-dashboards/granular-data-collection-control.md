# Granular Account and Region Control over Data Collection

## Last Updated

March 2026

## Author

- Eric Christensen, Sr. Technical Account Manager, AWS

## Controlling Data Collection Scope

This guide explains how to customize which AWS accounts and regions the Cloud Intelligence Dashboards Data Collection framework processes. You can limit data collection to specific accounts, exclude certain accounts, or apply granular rules to accounts and OUs per module and region.

## Overview

The Data Collection framework provides three methods to control how accounts are processed:

| Method                                                                        | Use Case                                                | Scope       |
| ----------------------------------------------------------------------------- | ------------------------------------------------------- | ----------- |
| [Inclusion List](#inclusion-list "#inclusion-list")                           | Collect data from only specific accounts                | All modules |
| [Exclusion List](#exclusion-list "#exclusion-list")                           | Exclude specific accounts from collection               | All modules |
| [Granular Control](#granular-execution-control "#granular-execution-control") | Fine-grained control by module, account, OU, and region | Per module  |

All configuration files should be placed in your CID data S3 bucket. The `CID-DC-account-collector` Lambda defines default values for these in the environment variable parameters. You may customize as needed. By default, the prefix will be `account-list/`. These files are not created or deployed automatically but must be manually created, per instructions below.

## Inclusion and Exclusion Lists

These simple list-based methods apply globally to all data collection modules.

### Inclusion List

Use an inclusion list when you want to collect data from only a specific set of accounts, and not use AWS Organizations to retrieve the list of all accounts in the Organization. This is useful if you have restrictions to accessing AWS Organizations. See also [Data Collection without AWS Organizations](data-collection-without-org.md "data-collection-without-org.md").

The data fields needed are: `account_id`, `account_name`, and `payer_id`. Note the inclusion list config can be either a CSV or a JSON structure but you must ensure the file suffix matches the format.

**File location (default):**
`s3://<your-cid-bucket>/account-list/account-list.csv` or `account-list.json`

**CSV format:**

```
account_id,account_name,payer_id
123456789012,Production Account,111122223333
234567890123,Development Account,111122223333
345678901234,Staging Account,111122223333
```

**JSON format:**

```
[
  {"account_id": "123456789012", "account_name": "Production Account", "payer_id": "111122223333"},
  {"account_id": "234567890123", "account_name": "Development Account", "payer_id": "111122223333"}
]
```

When an inclusion list is present, the framework collects data only from the accounts in this file and ignores your AWS Organization structure.

### Exclusion List

Use an exclusion list when you have access to your AWS Organizations but want to universally exclude specific accounts. For example, you may want to exclude one or more accounts that are used for security purposes. Note, this functionality does not process OUs. If you wish to exclude an entire OU, either specify each account in the file or consider the **Granular Execution Control** option described later.

**File location (default):**
`s3://<your-cid-bucket>/account-list/excluded-linked-account-list.csv`

**Format:**

The format is a simple comma-separated list of 12-digit AWS account IDs (**Note:** ensure any leading 0s are included):

```
123456789012,234567890123,345678901234
```

List account IDs separated by commas on a single line. The framework will skip these accounts when iterating through your Organization.

### Choosing Between Inclusion and Exclusion

- Use an **inclusion list** when you have a small number of accounts you want to monitor and/or you do not have access to AWS Organizations.
- Use an **exclusion list** when you want to monitor most accounts but exclude a few (such as sandbox, security, or test accounts).

###### Note

If both files exist, the inclusion list takes precedence and the exclusion list is ignored.

## Granular Execution Control

For advanced scenarios, granular execution control allows you to define allow and deny account-based rules at the module level, with optional region filtering. This approach follows IAM-style policy evaluation where deny rules always take precedence over allow rules, no matter where they are defined in a sequence. For example, if your first rule is to deny using a specific module, account, and region combination and your tenth rule is to allow that combination (or vice versa), that particular combination will still be denied unless you remove the deny-based line.

**File location (default):**
`s3://<your-cid-bucket>/account-list/granular-execution-config.csv`

### File Format

```
module,policy_type,principal,regions,payload
```

| Field         | Description                                                                                      | Required |
| ------------- | ------------------------------------------------------------------------------------------------ | -------- |
| `module`      | The module name (e.g., `budgets`, `inventory`, `health-events`)                                  | Yes      |
| `policy_type` | `A` for Allow or `D` for Deny                                                                    | Yes      |
| `principal`   | An AWS account ID or Organization Unit ID (e.g., `123456789098`, `ou-xxxx-xxxxxxxx` or `r-xxxx`) | Yes      |
| `regions`     | Colon-separated list of regions (e.g., `us-east-1:ap-southeast-2`). Leave empty for all regions. | No       |
| `payload`     | Reserved for future use. Leave empty.                                                            | No       |

### Examples

**Deny a specific account for the budgets module (all regions):**

```
budgets,D,123456789012,,
```

**Deny a specific account for inventory in us-east-1 only:**

```
inventory,D,234567890123,us-east-1,
```

###### Note

For inventory the current capability is to manage all inventory sub-modules together.

**Allow an entire OU for the backup module:**

```
backup,A,ou-abc1-12345678,,
```

**Allow an OU but deny a specific account within it:**

```
backup,A,ou-abc1-12345678,,
backup,D,345678901234,,
```

**Deny multiple regions for a specific account:**

```
compute-optimizer,D,456789012345,us-east-1:eu-west-1,
```

### Policy Evaluation

The granular configuration follows IAM-style policy evaluation:

1. **Deny always wins** — If any deny rule matches an account, that account is excluded regardless of any allow rules.
2. **OU expansion** — When you specify an OU ID, the rule applies to all accounts within that OU and its child OUs.
3. **Region filtering** — When regions are specified, the rule applies only to those regions. An empty regions field means all regions.

This allows you to create broad allow rules (such as allowing an entire OU) and then carve out specific exceptions with deny rules.

### Precedence

When a granular execution config file exists and contains rules for a module:

1. The granular config is used for that module.
2. Any inclusion and exclusion lists (as described before the granular operation) are ignored for that module.

If the granular config file exists but has no rules for a specific module, that module falls back to the standard inclusion/exclusion list behavior.

## Configuration Summary

| File            | Path                                            | Purpose                                  |
| --------------- | ----------------------------------------------- | ---------------------------------------- |
| Inclusion list  | `account-list/account-list.csv` or `.json`      | Collect only these accounts              |
| Exclusion list  | `account-list/excluded-linked-account-list.csv` | Exclude these accounts from Organization |
| Granular config | `account-list/granular-execution-config.csv`    | Per-module allow/deny rules              |

### Quick Start

1. Navigate to your CID data S3 bucket (typically `cid-data-<account-id>`).
2. Create the `account-list/` folder if it doesn’t exist.
3. Upload the appropriate configuration file based on your requirements.
4. The next scheduled data collection run will use your configuration.

No changes to the deployed CloudFormation stack are required. The account collector Lambda automatically detects and applies these configuration files.

## Troubleshooting

- **Configuration not applied:** Verify the file is in the correct S3 path and the filename matches exactly.
- **Accounts still being collected:** Check for typos in module names and account IDs. Account IDs must be 12 digits.
- **OU rules not working:** Ensure you are using the full OU ID format (e.g., `ou-xxxx-xxxxxxxx`) or root ID (`r-xxxx`).
- **Unexpected behavior:** Review CloudWatch Logs for the account-collector Lambda to see which configuration files were detected and how rules were applied.
