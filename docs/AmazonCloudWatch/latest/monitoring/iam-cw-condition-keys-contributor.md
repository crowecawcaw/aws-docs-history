

# Condition keys for Contributor Insights log group access
<a name="iam-cw-condition-keys-contributor"></a>

To create a rule in Contributor Insights and see its results, a user must have the `cloudwatch:PutInsightRule` permission. By default, a user with this permission can create a rule that evaluates any log group in CloudWatch Logs and then view the results. Results can include contributor data from those log groups, which might contain sensitive information.

You can create IAM policies with condition keys to grant users permission to write Contributor Insights rules for specific log groups, while preventing access to data from other log groups.

 For more information about the `Condition` element in IAM policies, see [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html).

## Understanding the Contributor Insights permissions model
<a name="contributor-insights-permissions-model"></a>

Contributor Insights operations use the `cloudwatch:` IAM namespace. Log group operations use the `logs:` namespace. Contributor Insights does not require or evaluate `logs:` permissions when it processes log group data.

A principal with `cloudwatch:PutInsightRule` and `cloudwatch:GetInsightRuleReport` permissions can create rules that evaluate any log group and retrieve the results – even without any `logs:` permissions on those log groups.

**Important**  
Aggregated results can contain sensitive information, such as log fields used as contributor keys. Grant `cloudwatch:PutInsightRule` and `cloudwatch:GetInsightRuleReport` permissions only to principals who need access to data across all referenced log groups.

For cross-account access, if a source account configured an [AWS Organizations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) link that shares log group access, a principal in the monitoring account needs only `cloudwatch:PutInsightRule` to create rules that target source account log groups.

## Restricting Contributor Insights access to specific log groups
<a name="contributor-insights-restrict-log-groups"></a>

Use the following condition keys to restrict which log groups a principal can specify when creating Contributor Insights rules:
+ `cloudwatch:requestInsightRuleLogGroups` – Matches log group names specified in a rule
+ `cloudwatch:requestInsightRuleLogGroupARNs` – Matches log group ARNs specified in a rule

**Important**  
After a rule is created, any principal with `cloudwatch:GetInsightRuleReport` permission can retrieve its results, regardless of log group restrictions.

The following policy grants permission to create Contributor Insights rules for the log group named `AllowedLogGroup` and log groups with names that start with `AllowedWildCard`. It does not grant permission to create rules for any other log groups.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCertainLogGroups",
            "Effect": "Allow",
            "Action": "cloudwatch:PutInsightRule",
            "Resource": "arn:aws:cloudwatch:*:*:insight-rule/*",
            "Condition": {
                "ForAllValues:StringLike": {
                    "cloudwatch:requestInsightRuleLogGroups": [
                        "AllowedLogGroup",
                        "AllowedWildcard*"
                    ]
                }
            }
        }
    ]
}
```

------

The following policy allows creating rules for any log group by default, but explicitly denies creating rules for the log group named `ExplicitlyDeniedLogGroup`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowInsightRulesOnLogGroupsByDefault",
            "Effect": "Allow",
            "Action": "cloudwatch:PutInsightRule",
            "Resource": "arn:aws:cloudwatch:*:*:insight-rule/*"
          
        },
        {
            "Sid": "ExplicitDenySomeLogGroups",
            "Effect": "Deny",
            "Action": "cloudwatch:PutInsightRule",
            "Resource": "arn:aws:cloudwatch:*:*:insight-rule/*",
            "Condition": {
                "ForAllValues:StringEqualsIgnoreCase": {
                    "cloudwatch:requestInsightRuleLogGroups": [
                        "/test/alpine/ExplicitlyDeniedLogGroup"
                    ]
                }
            }
        }
    ]
}
```

------

The following policy denies creation of rules that target log groups with `/production/` in the ARN path.

```
{
    "Version": "		 	 	 ",
    "Statement": [
        {
            "Sid": "DenyProductionLogGroupsByARN",
            "Effect": "Deny",
            "Action": "cloudwatch:PutInsightRule",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringLike": {
                    "cloudwatch:requestInsightRuleLogGroupARNs": [
                        "arn:aws:logs:*:*:log-group:*/production/*"
                    ]
                }
            }
        }
    ]
}
```

**Note**  
Condition keys match against the pattern strings as written in the rule definition, not against the resolved log groups.
If rules specify log groups as full ARNs, a condition value such as `/production/*` does not match because the full ARN string does not start with that prefix. Use `*/production/*` as the wildcard prefix to match ARN-based log group references.

## Security best practices for Contributor Insights
<a name="contributor-insights-security-best-practices"></a>

Follow these best practices to secure your Contributor Insights configuration.
+ **Apply least privilege** – Grant `cloudwatch:PutInsightRule` and `cloudwatch:GetInsightRuleReport` only to principals who must analyze log group data
+ **Use condition keys to restrict log groups** – Limit which log groups a principal can reference in Contributor Insights rules
+ **Protect sensitive fields** – Use CloudWatch Logs data protection to mask sensitive log data before Contributor Insights processes it. For more information, see [Protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).
+ **Consider contributor key sensitivity** – Contributor keys might expose values such as IP addresses or user identifiers in rule results
+ **Review cross-account access** – Audit AWS Organizations link configurations to confirm that only intended monitoring accounts can create rules against source account log groups