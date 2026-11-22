

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# LATEST version for the Bot Control managed rule group

This section explains the `LATEST` version of the AWS WAF Bot Control managed rule group.

`LATEST` is a version name that you can choose for the Bot Control managed rule group instead of the default version or a specific static version. It always points to the newest static version of the rule group that AWS has released. When AWS releases a new static version, it updates `LATEST` to point to the new version, and protection packs (web ACLs) that use `LATEST` start using the new version without any action on your part. 

**Note**  
`LATEST` is currently available only for the AWS WAF Bot Control managed rule group. The other versioned AWS Managed Rules rule groups offer the default version and static versions.

The default version and `LATEST` both let AWS manage the version for you, but they behave differently. The following table compares them. 


|  | Default version | `LATEST` | 
| --- | --- | --- | 
| Which static version you use | The static version that AWS recommends. This is often not the newest static version. AWS promotes a static version to the default after it has been available for a while and AWS has evaluated it against customer traffic. | The newest static version that AWS has released. | 
| When the version changes | When AWS decides to recommend a different static version. AWS might release several static versions before it moves the default. | Each time AWS releases a new static version. | 
| Advance notification | Yes. AWS sends an SNS notification at least one week before it moves the default version, and another at the start of the deployment. For more information about default version deployments, see [Default version deployments for AWS Managed Rules](waf-managed-rule-groups-deployments-default-version.md). | No. AWS announces each new static version through the SNS topic, the [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md), and the [Document history](doc-history.md), but it doesn't send a separate advance notification before LATEST moves to the new version. | 
| Release candidate testing | Yes. AWS might temporarily point the default version at a release candidate that runs candidate rules in Count mode. For more information about release candidates, see [Release candidate deployments for AWS Managed Rules](waf-managed-rule-groups-deployments-release-candidate.md). | No. LATEST points only to released static versions. | 
| Best for | Stability, with advance notice of changes. | Getting new detections as soon as AWS releases them, without manual upgrades. The Targeted bot control setting in the console uses LATEST. | 

**Using the LATEST version**  
When you add or edit the Bot Control managed rule group in your protection pack (web ACL), choose `LATEST` in the **Version** list. Through the API, set the `Version` in the `ManagedRuleGroupStatement` to `LATEST`. 

Before you choose `LATEST`, consider the following: 
+ A new static version can add rules, change rule actions, add labels, and increase the rule group's WCU. With `LATEST`, these changes take effect in your protection pack (web ACL) when AWS releases the version, without a testing period on your side. If you override rule actions or use label match rules against the rule group's labels, review the [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md) entry for each new version to check whether your customizations still apply. 
+ If you need to test and approve each version before you use it, choose a static version instead, and subscribe to SNS notifications so that you know when new versions are available. For more information about the notifications, see [Getting notified of new versions and updates](waf-using-managed-rule-groups-sns-topic.md). 
+ Because `LATEST` always resolves to the newest static version, you don't need to track version expiration for it. 
+ The bot confidence levels in the Bot Control managed rule group require version 8.0 or later. `LATEST` always meets this requirement. For more information about the confidence levels, see [Bot confidence levels](aws-managed-rule-groups-bot-confidence.md). 
+ If you turned on **Targeted bot control** in the console and you later change the rule group's version from `LATEST` to another version, the console turns **Targeted bot control** off. The rule group stays in your protection pack (web ACL) and keeps evaluating traffic with the version that you chose. For more information about the setting, see [Turning on Targeted bot control in the console](waf-bot-control-targeted-console.md). 