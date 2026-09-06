

# Granular Account and Region Control over Data Collection
<a name="granular-data-collection-control"></a>

## Last Updated
<a name="last-updated"></a>

March 2026

## Author
<a name="author"></a>
+ Eric Christensen, Sr. Technical Account Manager, AWS

## Controlling Data Collection Scope
<a name="controlling-data-collection-scope"></a>

This guide explains how to customize which AWS accounts and regions the Cloud Intelligence Dashboards Data Collection framework processes. You can limit data collection to specific accounts, exclude certain accounts, or apply granular rules to accounts and OUs per module and region. No changes to the deployed CloudFormation stack are required. You only need to supply configuration files, per the description below and The Account Collector Lambda automatically detects and applies them.

**Note**  
You must be using the Data Collection framework version 3.14.4\+ to enable the Granular Control capability. See [Update](data-collection-update.md) for instructions on updating your deployment.

## Overview
<a name="overview"></a>

The Data Collection framework provides three methods to control how accounts are processed:


| Method | Use Case | Scope | 
| --- | --- | --- | 
|  [Inclusion List](#inclusion-list)  | Collect data only from specific accounts | All modules | 
|  [Exclusion List](#exclusion-list)  | Exclude specific accounts from collection | All modules | 
|  [Granular Control](#granular-execution-control)  | Fine-grained control by module, account, OU, and region | Per module | 

All configuration files should be placed in your CID data S3 bucket. The `CID-DC-account-collector` Lambda defines default values for these in the environment variable parameters. You may customize as needed. By default, the prefix will be `account-list/`. These files are not created or deployed automatically but must be manually created, per instructions below.

## Inclusion and Exclusion Lists
<a name="inclusion-and-exclusion-lists"></a>

These simple list-based methods apply globally to all data collection modules.

### Inclusion List
<a name="inclusion-list"></a>

Use an inclusion list when you want to collect data from only a specific set of accounts, and not use AWS Organizations to retrieve the list of all accounts in the Organization. This is useful if you have restrictions to accessing AWS Organizations. See also [Data Collection without AWS Organizations](data-collection-without-org.md).

The data fields needed are: `account_id`, `account_name`, and `payer_id`. Note the inclusion list config can be either a CSV or a JSON structure but you must ensure the file suffix matches the format.

 **File location (default):** `s3://<your-cid-bucket>/account-list/account-list.csv` or `account-list.json` 

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
<a name="exclusion-list"></a>

Use an exclusion list when you have access to your AWS Organizations but want to universally exclude specific accounts. For example, you may want to exclude one or more accounts that are used for security purposes. Note, this functionality does not process OUs. If you wish to exclude an entire OU, either specify each account in the file or consider the **Granular Execution Control** option described later.

 **File location (default):** `s3://<your-cid-bucket>/account-list/excluded-linked-account-list.csv` 

 **Format:** 

The format is a simple comma-separated list of 12-digit AWS account IDs (**Note:** ensure any leading 0s are included):

```
123456789012,234567890123,345678901234
```

List account IDs separated by commas on a single line. The framework will skip these accounts when iterating through your Organization.

### Choosing Between Inclusion and Exclusion
<a name="choosing-between-inclusion-and-exclusion"></a>
+ Use an **inclusion list** when you have a small number of accounts you want to monitor and/or you do not have access to AWS Organizations.
+ Use an **exclusion list** when you want to monitor most accounts but exclude a few (such as sandbox, security, or test accounts).

**Note**  
If both files exist, the inclusion list takes precedence and the exclusion list is ignored.

## Granular Execution Control
<a name="granular-execution-control"></a>

For advanced scenarios, granular execution control allows you to define allow and deny account-based rules at the module level, with optional region filtering. This approach follows IAM-style policy evaluation where deny rules always take precedence over allow rules, no matter where they are defined in a sequence. For example, if your first rule is to deny using a specific module, account, and region combination and your tenth rule is to allow that combination (or vice versa), that particular combination will still be denied unless you remove the deny-based line.

 **File location (default):** `s3://<your-cid-bucket>/account-list/granular-execution-config.csv` 

### File Format
<a name="file-format"></a>

```
module,policy_type,principal,regions,payload
```


| Field | Description | Required | 
| --- | --- | --- | 
|  `module`  | The module name (e.g., `budgets`, `inventory`, `health-events`). Leave blank or use `*` to apply the rule to all modules. | Yes | 
|  `policy_type`  |  `A` for Allow or `D` for Deny | Yes | 
|  `principal`  | An AWS account ID or Organization Unit ID (e.g., `123456789098`, `ou-xxxx-xxxxxxxx` or `r-xxxx`) | Yes | 
|  `regions`  | Colon-separated list of regions (e.g., `us-east-1:ap-southeast-2`). Leave blank or use `*` for all regions in scope. | No | 
|  `payload`  | Reserved for future use. Leave empty. | No | 

### Examples
<a name="examples"></a>

 **Allow all modules at the root OU level, then deny all regions to one account but only us-east-1 to another:** 

```
*,A,r-xxxx,,
*,D,345678901234,*
*,D,456789012345,us-east-1
```

 **Deny a specific account for the budgets module (all regions):** 

```
budgets,D,123456789012,*
```

 **Deny a specific account for the ec2 inventory in us-east-1 only:** 

```
inventory-ec2-instances,D,234567890123,us-east-1
```

**Note**  
The Inventory module has several sub-modules and you must define each one you wish to control

 **Allow an entire OU for the backup module:** 

```
backup,A,ou-abc1-12345678,*
```

 **Allow an OU but deny a specific account within it:** 

```
backup,A,ou-abc1-12345678,*
backup,D,345678901234,*
```

 **Deny multiple regions for a specific account for all modules:** 

```
*,D,456789012345,us-east-1:eu-west-1
```

 **Deny specific regions for all accounts for all modules:** 

```
*,D,*,us-east-1:eu-west-1
```

 **Deny all regions for all accounts for all modules. This rule would produce an error because nothing would be allowed:** 

```
*,D,*,*
```

### Wildcards and Blank Fields
<a name="wildcards-and-blank-fields"></a>

The `module` and `regions` fields support a wildcard (`*`) or can be left blank:
+  **Module field:** Leave blank or use `*` to apply the rule to all modules.
+  **Regions field:** Leave blank or use `*` to apply the rule to all regions in your deployment scope.

**Important**  
The wildcard `*` does not perform pattern matching. It is only valid as a standalone value in a field. Do not combine it with other characters (e.g., `budget*` is not valid). Use only `*` by itself or leave the field empty.

### Region Scope and Restrictions
<a name="region-scope-and-restrictions"></a>

The regional restriction in the granular policy works in conjunction with the top-level **Regions in Scope** parameter defined in the [Data Collection Stack deployment](data-collection-deployment.md). The granular policy can only restrict regions that are already included in that top-level scope — it cannot add regions that are not defined there.

For example, if your Data Collection Stack is deployed with `us-east-1:us-west-2:eu-west-1` as the regions in scope, a granular policy can deny `eu-west-1` for a specific module, but it cannot enable `ap-southeast-1` if that region is not in the top-level scope.

Ensure that the **Regions in Scope** parameter in your Data Collection Stack includes all regions you may want to collect from. Then use the granular policy to restrict specific modules or accounts to a subset of those regions as needed.

### Best Practices
<a name="best-practices"></a>

If you wish to deny one or a few specific accounts across all modules while allowing everything else, a recommended approach is:

1. Define an allow rule at the root OU level for all modules and all regions.

1. Add deny rules for the specific accounts you want to exclude.

For example:

```
*,A,r-xxxx
*,D,345678901234
*,D,456789012345
```

This ensures all accounts in the Organization are allowed by default, and you can then pare down the scope by adding targeted deny rules.

### Policy Evaluation
<a name="policy-evaluation"></a>

The granular configuration follows IAM-style policy evaluation:

1.  **Deny always wins** — If any deny rule matches an account, that account is excluded regardless of any allow rules.

1.  **OU expansion** — When you specify an OU ID, the rule applies to all accounts within that OU and its child OUs.

1.  **Region filtering** — When regions are specified, the rule applies only to those regions. An empty regions field means all regions.

This allows you to create broad allow rules (such as allowing an entire OU) and then carve out specific exceptions with deny rules.

### Precedence
<a name="precedence"></a>

When a granular execution config file exists and contains rules for a module:

1. The granular config is used for that module.

1. Any inclusion and exclusion lists (as described before the granular operation) are ignored for that module.

If the granular config file exists but has no rules for a specific module, that module falls back to the standard inclusion/exclusion list behavior.

## Troubleshooting
<a name="troubleshooting"></a>
+  **Configuration not applied:** Verify the file is in the correct S3 path and the filename matches exactly.
+  **Accounts still being collected:** Check for typos in module names and account IDs. Account IDs must be 12 digits.
+  **OU rules not working:** Ensure you are using the full OU ID format (e.g., `ou-xxxx-xxxxxxxx`) or root ID (`r-xxxx`).
+  **Region restrictions not taking effect:** Verify that the regions you are restricting are included in the top-level **Regions in Scope** parameter of the Data Collection Stack. The granular policy cannot add regions outside of that scope.
+  **Wildcard not working as expected:** The ` ` wildcard must be the only character in the field. It does not support pattern matching (e.g., `budget` is not valid).
+  **Unexpected behavior:** Review CloudWatch Logs for the Account Collector Lambda to see which configuration files were detected and how rules were applied. Set the Lambda’s logging level to `DEBUG` for detailed tracing of policy parsing, rule evaluation, and the final computed ruleset.