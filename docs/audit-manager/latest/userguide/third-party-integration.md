

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Integrations with third-party GRC products
<a name="third-party-integration"></a>



AWS Audit Manager supports integrations with the third-party partner GRC products that are listed on this page.

If your company uses a hybrid cloud model or multicloud model, it’s likely that you use a GRC product to manage evidence from those environments. When that product is integrated with Audit Manager, you can pull evidence about your AWS usage directly into your GRC environment. This simplifies how you manage compliance by providing you with a centralized place to review and remediate evidence as you prepare for audits.

Read this page for an overview of the third-party GRC products that can ingest evidence from Audit Manager. You can also see a reference of which Audit Manager API actions you can take directly within those products.

**Topics**
+ [Understanding how third-party integrations work with Audit Manager](#understanding-grc-integrations)
+ [Third-party GRC partner products that integrate with Audit Manager](#supported-grc-integrations)

## Understanding how third-party integrations work with Audit Manager
<a name="understanding-grc-integrations"></a>

GRC partners can use the Audit Manager public APIs to integrate their products with Audit Manager. With this integration in place, you can map the enterprise controls in your GRC environment to the common controls that Audit Manager provides. 

**Tip**  
You can map your enterprise controls to any type of [ Audit Manager control](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#control). However, we recommend that you use common controls. When you map to a common control that represents your goal, Audit Manager collects evidence from a predefined group of data sources that's managed by AWS. This means that you don’t have to be an AWS expert to know which data sources collect the relevant evidence for your goal.

After you complete this one-time control mapping exercise, you can create Audit Manager assessments directly in the GRC product. This action starts the collection of evidence about your AWS usage. You can then see this AWS evidence along with the other evidence that’s collected from your hybrid environment, all within the same context of your enterprise controls.

When you use an Audit Manager integration with a third-party GRC product, keep in mind the following points:
+ Integrations are available for all [AWS Regions where Audit Manager is supported](https://docs.aws.amazon.com/general/latest/gr/audit-manager.html).
+ Any Audit Manager resources that you create in the GRC partner product are also reflected in Audit Manager.
+ You’re subject to [AWS Audit Manager pricing](https://aws.amazon.com/audit-manager/pricing/) in addition to the pricing of the third-party GRC product.
+ The evidence that Audit Manager collects is immutable. Evidence is presented in exactly the same way in third-party GRC products as it is in the Audit Manager console. However, if you use a third-party integration, you might be able to enhance this evidence by providing additional context in your reporting.
+ The same [quotas that apply to Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html) also apply within the third-party GRC product. For example, each AWS account can have up to 100 active Audit Manager assessments. This account-level quota applies whether you create the assessments in the Audit Manager console or in the third-party GRC product. Most Audit Manager quotas, but not all, are listed under the AWS Audit Manager namespace in the Service Quotas console. To learn how to request a quota increase, see [Managing your Audit Manager quotas](service-quotas.md#managing-your-service-quotas).

If you have a compliance solution and you’re interested in integrating with Audit Manager, email `auditmanager-partners@amazon.com`.

## Third-party GRC partner products that integrate with Audit Manager
<a name="supported-grc-integrations"></a>

The following third party GRC products can ingest evidence from Audit Manager.

### MetricStream
<a name="metricstream"></a>

To use this integration, reach out to [MetricStream](https://aws.amazon.com/marketplace/pp/prodview-5ph5amfrrmyx4?qid=1616170904192&sr=0-1&ref_=srh_res_product_title) for the access and purchase of MetricStream GRC software.

Built on the MetricStream Platform, the MetricStream Enterprise GRC solution allows for a comprehensive and collaborative approach to enterprise-wide GRC activities and processes. By ingesting evidence from Audit Manager into MetricStream, you can proactively identify non-compliant evidence from your AWS environment and review it alongside evidence from your on-premises data sources or other cloud partners. This provides you with a convenient and centralized way to review and improve your cloud security and compliance posture as you prepare for audits.

With the MetricStream and Audit Manager integration, you can perform the following API operations.


| Task | API operation | 
| --- | --- | 
| Setting up the Audit Manager integration |  +  [GetAccountStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAccountStatus.html) <br />+  [GetOrganizationAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetOrganizationAdminAccount.html) <br />+  [GetSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetSettings.html)   | 
| Reviewing Audit Manager resources |  +  [GetAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html) <br />+  [GetAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html) <br />+  [GetControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html) <br />+  [ListAssessmentFrameworks](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html) <br />+  [ListControls](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html)   | 
| Creating Audit Manager resources |  +  [CreateAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessment.html) <br />+  [CreateAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessmentFramework.html)   | 
| Updating Audit Manager resources |  +  [UpdateAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessment.html) <br />+  [UpdateAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControl.html) <br />+  [UpdateAssessmentStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentStatus.html)   | 
| Managing evidence |  +  [StartQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartQuery.html) (AWS CloudTrail API)  <br />+  [GetQueryResults](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetQueryResults.html) (AWS CloudTrail API)    | 
| Deleting Audit Manager resources |  +  [DeleteAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html)   | 

**Related MetricStream links**
+ [AWS Marketplace link](https://aws.amazon.com/marketplace/pp/prodview-5ph5amfrrmyx4?qid=1616170904192&sr=0-1&ref_=srh_res_product_title)
+ [Product link](https://www.metricstream.com/products/cyber-grc.htm)
+ [Product pricing](https://info.metricstream.com/ms-pricing.html?Channel=ms-side-widget)