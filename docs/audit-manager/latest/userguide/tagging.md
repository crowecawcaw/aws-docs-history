# Tagging AWS Audit Manager resources

A _tag_ is a metadata label that you assign or that AWS
assigns to an AWS resource. Each tag consists of a _key_ and
a _value_. For tags that you assign, you define the key and
value. For example, you might define the key as `stage` and the value for one
resource as `test`.

Tags help you do the following:

- Easily locate your Audit Manager resources. You can use tags as search criteria when browsing the
  framework library and the control library.
- Associate your resource with a compliance type. You can tag multiple resources with a
  compliance-specific tag to associate those resources with a specific framework.
- Identify and organize your AWS resources. Many AWS services support tagging, so you
  can assign the same tag to resources from different services to indicate that the resources
  are related.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the
  tags to categorize your costs and deliver a monthly cost allocation report to you. For more
  information, see [Use cost allocation
  tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing and Cost Management User Guide_.
  The following sections provide more information about tags for AWS Audit Manager.

###### Contents

- [Supported resources in Audit Manager](tagging.md#supported-resources "tagging.md#supported-resources")
- [Tag restrictions](tagging.md#tag-restrictions "tagging.md#tag-restrictions")
- [Additional resources](tagging.md#managing-tags "tagging.md#managing-tags")

## Supported resources in Audit Manager

The following Audit Manager resources support tagging:

- Assessments
- Controls
- Frameworks

## Tag restrictions

The following basic restrictions apply to tags on Audit Manager resources:

- Maximum number of tags that you can assign to a resource — 50
- Maximum key length — 128 Unicode characters
- Maximum value length — 256 Unicode characters
- Valid characters for key and value — a-z, A-Z, 0-9, space, and the following
  characters: \_ . : / = + - and @
- Keys and values are case sensitive
- Don't use `aws:` as a prefix for keys; it's reserved for AWS use

## Additional resources

You can set tags as properties when you create an assessment, framework, or control. You
can add, edit, and delete tags through the Audit Manager console, the AWS Command Line Interface (AWS CLI), and the Audit Manager
API. For more information, see the following links.

- For tagging assessments:
  - [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md") and [Editing an assessment in AWS Audit Manager](edit-assessment.md "edit-assessment.md") in the
    _Assessments_ section of this guide
  - [Tags tab](review-assessments.md#review-assessment-tags "review-assessments.md#review-assessment-tags") in
    the _Review an assessment_ page of this guide
  - [CreateAssessment](../APIReference/API_CreateAssessment.md "../APIReference/API_CreateAssessment.md") and [UpdateAssessment](../APIReference/API_UpdateAssessment.md "../APIReference/API_UpdateAssessment.md") in the _AWS Audit Manager API
    Reference_
  - [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") in the _AWS Audit Manager API
    Reference_

- For tagging frameworks:
  - [Creating a custom framework in AWS Audit Manager](custom-frameworks.md "custom-frameworks.md") and [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md "edit-custom-frameworks.md") in the
    _Framework library_ section of this guide
  - The [Tags tab](review-frameworks.md#framework-tags-tab "review-frameworks.md#framework-tags-tab") on the
    _View framework details_ page of this guide
  - [CreateAssessmentFramework](../APIReference/API_CreateAssessmentFramework.md "../APIReference/API_CreateAssessmentFramework.md") and [UpdateAssessmentFramework](../APIReference/API_UpdateAssessmentFramework.md "../APIReference/API_UpdateAssessmentFramework.md") in the _AWS Audit Manager API
    Reference_
  - [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") in the _AWS Audit Manager API
    Reference_

- For tagging controls:
  - [Creating a custom control in AWS Audit Manager](create-controls.md "create-controls.md") and [Editing a custom control in AWS Audit Manager](edit-controls.md "edit-controls.md") in the _Control
    library_ section of this guide
  - The [Tags](control-library-review-custom-controls.md#custom-control-tags-tab "control-library-review-custom-controls.md#custom-control-tags-tab") section on the _Reviewing a
    custom control_ page of this guide
  - The [Tags](control-library-review-standard-controls.md#standard-control-tags-tab "control-library-review-standard-controls.md#standard-control-tags-tab") section on the _Reviewing a
    standard control_ page of this guide
  - [CreateControl](../APIReference/API_CreateControl.md "../APIReference/API_CreateControl.md") and [UpdateControl](../APIReference/API_UpdateControl.md "../APIReference/API_UpdateControl.md") in the _AWS Audit Manager API
    Reference_
  - [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") in the _AWS Audit Manager API
    Reference_
