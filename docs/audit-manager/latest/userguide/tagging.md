

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Tagging AWS Audit Manager resources
<a name="tagging"></a>

 

A *tag* is a metadata label that you assign or that AWS assigns to an AWS resource. Each tag consists of a *key* and a *value*. For tags that you assign, you define the key and value. For example, you might define the key as `stage` and the value for one resource as `test`.

Tags help you do the following:
+ Easily locate your Audit Manager resources. You can use tags as search criteria when browsing the framework library and the control library. 
+ Associate your resource with a compliance type. You can tag multiple resources with a compliance-specific tag to associate those resources with a specific framework. 
+ Identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. 
+  Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly cost allocation report to you. For more information, see [Use cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing and Cost Management User Guide*.

The following sections provide more information about tags for AWS Audit Manager.

**Contents**
+ [Supported resources in Audit Manager](#supported-resources)
+ [Tag restrictions](#tag-restrictions)
+ [Additional resources](#managing-tags)

## Supported resources in Audit Manager
<a name="supported-resources"></a>

 The following Audit Manager resources support tagging: 
+ Assessments
+ Controls
+ Frameworks

## Tag restrictions
<a name="tag-restrictions"></a>

 The following basic restrictions apply to tags on Audit Manager resources: 
+ Maximum number of tags that you can assign to a resource — 50
+ Maximum key length — 128 Unicode characters
+ Maximum value length — 256 Unicode characters
+ Valid characters for key and value — a-z, A-Z, 0-9, space, and the following characters: \_ . : / = \+ - and @
+ Keys and values are case sensitive
+ Don't use `aws:` as a prefix for keys; it's reserved for AWS use

## Additional resources
<a name="managing-tags"></a>

You can set tags as properties when you create an assessment, framework, or control. You can add, edit, and delete tags through the Audit Manager console, the AWS Command Line Interface (AWS CLI), and the Audit Manager API. For more information, see the following links.
+ For tagging assessments:
  + [Creating an assessment in AWS Audit Manager](create-assessments.md) and [Editing an assessment in AWS Audit Manager](edit-assessment.md) in the *Assessments* section of this guide
  + [Tags tab](review-assessments.md#review-assessment-tags) in the *Review an assessment* page of this guide
  + [CreateAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessment.html) and [UpdateAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessment.html) in the *AWS Audit Manager API Reference*
  + [TagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UntagResource.html) in the *AWS Audit Manager API Reference*
+ For tagging frameworks:
  + [Creating a custom framework in AWS Audit Manager](custom-frameworks.md) and [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md) in the *Framework library* section of this guide
  + The [](review-frameworks.md#framework-tags-tab) on the *View framework details* page of this guide
  + [CreateAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessmentFramework.html) and [UpdateAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentFramework.html) in the *AWS Audit Manager API Reference*
  + [TagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UntagResource.html) in the *AWS Audit Manager API Reference*
+ For tagging controls:
  + [Creating a custom control in AWS Audit Manager](create-controls.md) and [Editing a custom control in AWS Audit Manager](edit-controls.md) in the *Control library* section of this guide
  + The [](control-library-review-custom-controls.md#custom-control-tags-tab) section on the *Reviewing a custom control* page of this guide
  + The [](control-library-review-standard-controls.md#standard-control-tags-tab) section on the *Reviewing a standard control* page of this guide
  + [CreateControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateControl.html) and [UpdateControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateControl.html) in the *AWS Audit Manager API Reference*
  + [TagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UntagResource.html) in the *AWS Audit Manager API Reference*