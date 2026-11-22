

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# LATEST version updates for AWS Managed Rules

The AWS WAF Bot Control managed rule group offers a `LATEST` version that always points to the newest static version of the rule group. When AWS deploys a new static version of the rule group, it also updates `LATEST` to point to the new version. Protection packs (Web ACLs) that use `LATEST` start using the new static version at that time, without any action on your part. 

This isn't a separate deployment type. It's part of the static version deployment. Unlike a default version deployment, AWS doesn't test release candidates on `LATEST` and doesn't send advance notification before `LATEST` moves to the new version. For a comparison of `LATEST` with the default version, see [LATEST version for the Bot Control managed rule group](waf-managed-rule-groups-versioning-latest.md). 

**Timing and notifications**  
AWS updates `LATEST` whenever it deploys a new static version of the Bot Control managed rule group. 
+ **SNS** – AWS doesn't send a separate notification for the `LATEST` update. The SNS notification for the static version deployment tells you that a new version is available. If you use `LATEST`, your protection pack (web ACL) is using the new version. 
+ **Change log** – The change log entry for the new static version describes the changes that you receive if you use `LATEST`. 