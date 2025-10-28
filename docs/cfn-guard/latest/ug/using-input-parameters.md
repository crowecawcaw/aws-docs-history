# Using input parameters with AWS CloudFormation Guard

rules

AWS CloudFormation Guard allows you to use input parameters for dynamic data lookups during
validation. This feature is particularly useful when you need to reference external data in your
rules. However, when specifying input parameter keys, Guard requires that there are no
conflicting paths.

## How to use

1. Use the `--input-parameters` or `-i` flag to specify files
   containing input parameters. Multiple input parameter files can be specified and will be
   combined to form a common context. Input parameter keys can not have conflicting
   paths.
2. Use the `--data` or `-d` flag to specify the actual template
   file to be validated.

## Example usage

1. Create an input parameter file (For example, `network.yaml`):

```
NETWORK:
  allowed_security_groups: ["sg-282850", "sg-292040"]
  allowed_prefix_lists: ["pl-63a5400a", "pl-02cd2c6b"]
```

2. Reference these parameters in your guard rule file (For example,
   `security_groups.guard`):

```
let groups = Resources.*[ Type == 'AWS::EC2::SecurityGroup' ]

let permitted_sgs = NETWORK.allowed_security_groups
let permitted_pls = NETWORK.allowed_prefix_lists
rule check_permitted_security_groups_or_prefix_lists(groups) {
    %groups {
        this in %permitted_sgs or
        this in %permitted_pls
    }
}

rule CHECK_PERMITTED_GROUPS when %groups !empty {
    check_permitted_security_groups_or_prefix_lists(
       %groups.Properties.GroupName
    )
}
```

3. Create a failing data template (For example, `security_groups_fail.yaml`):

```
# ---
# AWSTemplateFormatVersion: 2010-09-09
# Description: CloudFormation - EC2 Security Group

Resources:
  mySecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: wrong
```

4. Run the validate command:

```
cfn-guard validate -r security_groups.guard -i network.yaml -d security_groups_fail.yaml
```

In this command:

    * `-r` specifies the rule file.
    * `-i` specifies the input parameter file.
    * `-d` specifies the data file (template) to be validated.

## Multiple input parameters

You can specify multiple input parameter files:

```
cfn-guard validate -r rules.guard -i params1.yaml -i params2.yaml -d template.yaml
```

All files specified with `-i` will be combined to form a single context for
parameter lookup.
