

# Automation rules in Security Hub
<a name="securityhub-v2-automation-rules"></a>

 With Security Hub, you can automate tasks like updating finding details and creating tickets for third-party integrations. 

## Automation rules and AWS Regions
<a name="automation-regions"></a>

 Automation rules can be created in one AWS Region and then applied in all configured AWS Regions. When using Region aggregation, you can only create rules in the home Region. When creating rules in the home Region, any rule you define is applied to all linked Regions, unless your rule criteria excludes a specific linked Region. You must create an automation rule for any Region that is not a linked Region. 

## Rule actions and criteria
<a name="ocsf-fields"></a>

 Automation rules in Security Hub use criteria to reference OCSF attributes in Security Hub findings. For example, the filters supported for the `Criteria` parameter in [CreateAutomationRuleV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateAutomationRuleV2.html) match the filters supported for the `Filters` parameter in [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html). This means filters used in automation rules can be used to get findings. Security Hub supports the following OCSF fields for automation rule criteria. 


| OCSF field | Console filter value | Filter operators | Field type | 
| --- | --- | --- | --- | 
| activity\_id | Activity ID | Eq (equal-to), Gte (greater-than-equal), Lte (less-than-equal) | Number | 
| activity\_name | Provider status | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| class\_name | Finding class name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| cloud.account.name | Finding account name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| cloud.account.uid | Account ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| cloud.provider | Cloud provider | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| cloud.region | Region | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| compliance.assessments.category | Assessment category | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| compliance.assessments.meets\_criteria | Compliance assessment meets criteria | True, False | Boolean | 
| compliance.assessments.name | Assessment name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| compliance.control | Security control ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| compliance.control\_parameters | Control parameter name | EQUALS | Map | 
| compliance.standards | Applicable standards | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| compliance.status | Compliance status | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| compliance.status\_id | Compliance status ID | Eq (equal-to), Gte (greater-than-equal), Lte (less-than-equal) | Number | 
| confidence\_score | Confidence | Eq (equal-to), Gte (greater-than-equal), Lte (less-than-equal) | Number | 
| finding\_info.created\_time\_dt | Created at | Start, End, DateRange | Date (formatted as 2022-12-01T21:47:39.269Z) | 
| finding\_info.desc | Finding description | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.first\_seen\_time\_dt | First observed at | Start, End, DateRange | Date (formatted as 2022-12-01T21:47:39.269Z) | 
| finding\_info.last\_seen\_time\_dt | Last observed at | Start, End, DateRange | Date (formatted as 2022-12-01T21:47:39.269Z) | 
| finding\_info.modified\_time\_dt | Updated at | Start, End, DateRange | Date (formatted as 2022-12-01T21:47:39.269Z) | 
| finding\_info.related\_events.product.uid | Related findings product ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.related\_events.title | Related findings title | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.related\_events.traits.category | Traits category | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.related\_events.uid | Related findings ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.related\_events\_count | Related findings count | Eq (equal-to), Gte (greater-than-equal), Lte (less-than-equal) | Number | 
| finding\_info.src\_url | Source URL | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.tags | Finding info tags | EQUALS | Map | 
| finding\_info.title | Finding title | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.types | Finding type | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| finding\_info.uid | Provider finding ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| metadata.product.feature.uid | Generator ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| metadata.product.name | Product name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| metadata.product.uid | Product ARN | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| metadata.product.vendor\_name | Company name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| remediation.desc | Recommendation text | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| remediation.references | Recommendation URL | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.cloud\_partition | Resource partition | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.modified\_time\_dt | Resource last modified time | Start, End, DateRange | Date (formatted as 2022-12-01T21:47:39.269Z) | 
| resources.name | Resource name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.owner.account.name | Account name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.owner.account.uid | Account | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.owner.org.uid | Organization | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.provider | Cloud provider | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.region | Resource region | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.tags | Resource tags | EQUALS | Map | 
| resources.type | Resource type | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| resources.uid | Resource ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vendor\_attributes.severity | Provider severity | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vendor\_attributes.severity\_id | Provider severity ID | Eq (equal-to), Gte (greater-than-equal), Lte (less-than-equal) | Number | 
| vulnerabilities.affected\_code.file.path | Affected code file path | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vulnerabilities.affected\_packages.name | Affected package name | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vulnerabilities.cve.cvss.base\_score | CVE CVSS base score | Eq (equal-to), Gte (greater-than-equal), Lte (less-than-equal) | Number | 
| vulnerabilities.cve.epss.score | Epss score | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vulnerabilities.cve.uid | Vulnerability ID | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vulnerabilities.fix\_coverage | Software vulnerabilities coverage | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 
| vulnerabilities.is\_exploit\_available | Software vulnerabilities with exploit available | True, False | Boolean | 
| vulnerabilities.is\_fix\_available | Software vulnerabilities with fix available | True, False | Boolean | 
| vulnerabilities.related\_vulnerabilities | Related vulnerabilities | EQUALS, PREFIX, CONTAINS, NOT\_EQUALS, PREFIX\_NOT\_EQUALS | String | 

 For criteria labeled as string fields, using different filter operators on the same field affects the evaluation logic. For more information, see [StringFilter](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StringFilter.html) in the *Security Hub API Reference*. 

 Each criterion supports a maximum number of values that can be used to filter matching findings. For the limits of each criterion, see [OcsfFindingFilters](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_OcsfFindingFilters.html) in the *Security Hub API Reference* 

**OCSF fields that can be updated**  
 The following are the OCSF fields that can be updated using automation rules. 
+  `Comment` 
+  `SeverityId` 
+  `StatusId` 

## How automation rules evaluate findings
<a name="findings-evaluate"></a>

 An automation rule evaluates new and updated findings that Security Hub generates or ingests after you create the rule. 

 Automation rules evaluate original, provider-supplied findings. Providers can supply new findings and update existing findings through their integration with Security Hub. Rules are not triggered when you update finding fields after rule creation through the `BatchUpdateFindingsV2` operation. If you create an automation rule and make a `BatchUpdateFindingsV2` update that both affect the same finding field, the last update sets the value for that field. Take the following example: 

 You use `BatchUpdateFindingsV2` to update the `Status` field of a finding from `New` to `In Process`. If you call `GetFindingsV2`, the `Status` field now has a value of `In Process`. You create an automation rule that changes the `Status` field of the finding from `New` to `Suppressed` (recall that rules ignore updates made with `BatchUpdateFindingsV2`). The finding provider updates the finding and changes the `Status` field to `New`. If you call `GetFindingsV2`, the `Status` field now has a value of `Suppressed` because the automation rule was applied, and the rule was the last action taken on the finding. 

 When you create or edit a rule on the Security Hub console, the console displays a preview of findings that match the rule criteria. Whereas automation rules evaluate original findings sent by the finding provider, the console preview reflects findings in their final state as they would be shown in a response to the `GetFindingsV2` API operation (that is, after rule actions or other updates are applied to the finding). 

## How automation rules are ordered
<a name="automation-rule-order"></a>

 Each automation rule is assigned a rule order. This determines the order in which Security Hub applies your automation rules, and becomes important when multiple rules relate to the same finding or finding field. 

 When multiple rule actions relate to the same finding or finding field, the rule with the highest numerical value for rule order applies last and has the ultimate effect. 

 When you create a rule in the Security Hub console, Security Hub automatically assigns rule order based on the order of rule creation. The first rule you create will have a rule order of 1. When more than one rule exists each subsequently created rule will have the next highest available numerical value for rule order. 

 When you create a rule through [CreateAutomationRuleV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateAutomationRuleV2.html) API or AWS CLI, Security Hub applies the rule with the lowest numerical value for `RuleOrder` first. It then applies subsequent rules in ascending order. If multiple findings have the same `RuleOrder`, Security Hub applies a rule with an earlier value for the `UpdatedAt` field first (that is, the rule that was most recently edited applies last). 

 You can modify rule order at any time. 

 **Example of rule order**: 

 **Rule A (rule order is `1`)**: 
+ Rule A criteria
  + `ProductName` = `Security Hub CSPM`
  + `Resources.Type` is `S3 Bucket`
  + `Compliance.Status` = `FAILED`
  + `RecordState` is `NEW`
  + `Workflow.Status` = `ACTIVE`
+ Rule A actions
  + Update `Confidence` to `95`
  + Update `Severity` to `CRITICAL`
  + Update `Comment` to `This needs attention`

 **Rule B (rule order is `2`)**: 
+ Rule B criteria
  + `AwsAccountId` = `123456789012`
+ Rule B actions
  + Update `Severity` to `INFORMATIONAL`

 First, Rule A actions apply to Security Hub findings that match Rule A criteria. Then, Rule B actions apply to Security Hub findings with the specified account ID. In this example, since Rule B applies last, the end value of `Severity` in findings from the specified account ID is `INFORMATIONAL`. Based on the Rule A action, the end value of `Confidence` in matched findings is `95`. 

## Third-party integrations
<a name="integrations"></a>

 You can use automation rules to create tickets for integrations with Jira Cloud and ServiceNow ITSM. For more information, see [Creating a rule for a third-party integration](https://docs.aws.amazon.com/securityhub/latest/userguide/securithub-v2-automation-rules-create.html#integration). 

## Scenarios where automation rules do not work
<a name="scenarios"></a>

 The following are scenarios where automation rules do not work. 
+  The standalone account becomes a member of an organization with a delegated admin 
+  The organization management account removes the delegated admin and sets a new delegated admin 
+  The aggregator configuration for the delegated admin or standalone account changes when an unlinked Region is made a linked Region 

 During these scenarios, a member of an organization can manage automation rules with list, get, and delete operations in the AWS CLI or APIs. 

 When an unlinked Region is made a linked Region, the delegated admin or standalone account can manage resources in a linked Region with list, get, and delete operations. 