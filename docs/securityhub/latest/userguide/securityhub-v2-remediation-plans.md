

# Remediation plans in Security Hub
<a name="securityhub-v2-remediation-plans"></a>

 A remediation plan in AWS Security Hub groups related exposure findings that share a root cause. Each plan targets a single resource in your AWS environment. When you fix that resource, you can resolve or reduce the severity of several exposures at once. 

 Related exposures often come from the same underlying problem, such as a misconfiguration or an overly permissive setting on one resource. Instead of listing a separate action for each exposure, a remediation plan groups these exposures by their shared cause. You address the source once, and you reduce the most risk with the fewest actions. 

 For more information about exposure findings, see [Exposure findings in Security Hub](exposure-findings.md). 

## How Security Hub creates remediation plans
<a name="securityhub-v2-remediation-plans-how"></a>

 Security Hub creates remediation plans from the exposure findings in your account. It generates a plan for each combination of target resource and exposure trait that it can address. 

 Security Hub prioritizes your plans so that the ones that reduce the most risk appear first. The priority helps you decide what to work on first. 

 When Security Hub detects a new exposure, a plan for it might not appear immediately. 

## Remediation plan details
<a name="securityhub-v2-remediation-plans-details"></a>

 Each remediation plan includes the following details. 
+ **Priority** – How urgently you should act on the plan. The value is **Critical**, **High**, **Medium**, or **Low**.
+ **Status** – The current state of the plan. The value is **New**, **Updated**, or **Resolved**.
+ **Impact** – How the plan changes your exposures. A plan can fully resolve some exposures, reduce the severity of others, and address others without changing their severity. The value names the count in each case.
+ **Rollout** – Whether the fix applies immediately or requires a deployment. The value is **Immediate** or **Requires deployment**.
+ **Action** – The change that the plan recommends.
+ **Trait** – The exposure trait that the plan addresses.
+ **Target resource** – The resource that the plan fixes, and its resource type.
+ **Account** and **Region** – The AWS account that owns the target resource, and its AWS Region.

 A plan also shows an affected scope, a risk level, reversibility, automation level, and whether human review is required, when its guidance provides them. 

## Remediation guidance
<a name="securityhub-v2-remediation-plans-guidance"></a>

 Each remediation plan includes guidance that describes how to fix the problem. You open a plan to read its guidance in the **Guidance** section of the **Overview** tab. 

**Note**  
 Security Hub describes the steps, and you apply them yourself. Security Hub doesn't change your resources for you. 

 Guidance groups the steps into phases, such as **Prerequisite**, **Snapshot**, **Fix**, **Verify**, and **Done**. The phases, and what each one contains, come from the guidance for the target resource. 

 A step can also include a rollback, which describes how to undo that step. 

 Guidance can include example commands in more than one format, such as AWS CLI, Azure CLI, Python, Terraform, CDK, CloudFormation, Bicep, and ARM template. The formats available come from the guidance for the target resource. If no guidance is available for the target resource, the section reports that instead. 

## Viewing remediation plans
<a name="securityhub-v2-remediation-plans-viewing"></a>

 You view your remediation plans on the **Remediation plans** page in the Security Hub console. 

**To view remediation plans**

1. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. In the navigation pane, under **Response**, choose **Remediations**.

 The **Remediation plans** page lists your remediation plans in a table. Each row shows the recommended action, the plan's priority, the target resource with its AWS Region and AWS account, and the plan's impact, status, and rollout. For what these mean, see [Remediation plan details](#securityhub-v2-remediation-plans-details). 

 You can't sort the list by column. 

## Filtering remediation plans
<a name="securityhub-v2-remediation-plans-filtering"></a>

 To narrow the list, use the **Filter remediation plans** bar. You can filter by the following properties: 
+ **Priority**
+ **Status**
+ **Resource type**
+ **Cloud provider**
+ **Target resource ID**
+ **Account**

These filters have the following limits:
+ Each filter matches values by equality only. You can't use partial matches or ranges.
+ You can apply up to two filters at a time. Security Hub combines them with `AND`, so a plan must match both filters to appear.

## Viewing the exposures a plan affects
<a name="securityhub-v2-remediation-plans-affected-exposures"></a>

 When you open a remediation plan, the detail panel includes an **Affected exposures** tab. This tab lists the exposure findings that the plan addresses. For each exposure, it shows the exposure title, how the plan changes it, and the resulting severity change. 

 An exposure that the plan addresses without lowering its severity shows a single severity value instead of a change. 

 If a plan affects more exposures than the tab shows, the tab reports how many it is showing. 

## Viewing remediation plans for an exposure
<a name="securityhub-v2-remediation-plans-for-exposure"></a>

 When you view an exposure finding, the detail panel includes a **Remediations** tab. This tab lists the remediation plans that address the exposure. An exposure can have more than one plan. 

 Each plan shows the recommended action, its priority, and the target resource with its resource type. Expand a plan to read its guidance. 

## Tracking remediation impact on the dashboard
<a name="securityhub-v2-remediation-plans-dashboard"></a>

 The summary dashboard includes a **Remediation plans** widget. The widget lists up to five plans with a status of **New** or **Updated**, ordered by priority, so that you can act on the most urgent work without opening the full list. 

 For each plan, the widget shows the recommended action, the plan's priority, its impact, the target resource, and the AWS account that owns the resource. To see the exposures behind a plan, choose its impact. 

 The widget reports each plan's own impact. It doesn't combine impact across plans, so an exposure that more than one plan addresses is counted in each of those plans. 

 You can't apply filters to this widget. 