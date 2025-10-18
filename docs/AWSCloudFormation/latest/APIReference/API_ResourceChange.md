# ResourceChange

The `ResourceChange` structure describes the resource and the action that
 CloudFormation will perform on it if you execute this change set.


## Contents





**Action** 


The action that CloudFormation takes on the resource, such as `Add` (adds a new
 resource), `Modify` (changes a resource), `Remove` (deletes a resource),
 `Import` (imports a resource), or `Dynamic` (exact action for the resource
 can't be determined).


Type: String


Valid Values: `Add | Modify | Remove | Import | Dynamic`



Required: No




**AfterContext** 


An encoded JSON string that contains the context of the resource after the change is
 executed.


Type: String


Required: No




**BeforeContext** 


An encoded JSON string that contains the context of the resource before the change is
 executed.


Type: String


Required: No




**ChangeSetId** 


The change set ID of the nested change set.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`



Required: No




**Details.member.N** 


For the `Modify` action, a list of `ResourceChangeDetail` structures
 that describes the changes that CloudFormation will make to the resource.


Type: Array of [ResourceChangeDetail](API_ResourceChangeDetail.md "API_ResourceChangeDetail.md") objects


Required: No




**LogicalResourceId** 


The resource's logical ID, which is defined in the stack's template.


Type: String


Required: No




**ModuleInfo** 


Contains information about the module from which the resource was created, if the resource
 was created from a module included in the stack template.


Type: [ModuleInfo](API_ModuleInfo.md "API_ModuleInfo.md") object


Required: No




**PhysicalResourceId** 


The resource's physical ID (resource name). Resources that you are adding don't have
 physical IDs because they haven't been created.


Type: String


Required: No




**PolicyAction** 


The action that will be taken on the physical resource when the change set is
 executed.



* `Delete` The resource will be deleted.
* `Retain` The resource will be retained.
* `Snapshot` The resource will have a snapshot taken.
* `ReplaceAndDelete` The resource will be replaced and then deleted.
* `ReplaceAndRetain` The resource will be replaced and then retained.
* `ReplaceAndSnapshot` The resource will be replaced and then have a snapshot
 taken.

Type: String


Valid Values: `Delete | Retain | Snapshot | ReplaceAndDelete | ReplaceAndRetain | ReplaceAndSnapshot`



Required: No




**Replacement** 


For the `Modify` action, indicates whether CloudFormation will replace the resource
 by creating a new one and deleting the old one. This value depends on the value of the
 `RequiresRecreation` property in the `ResourceTargetDefinition` structure.
 For example, if the `RequiresRecreation` field is `Always` and the
 `Evaluation` field is `Static`, `Replacement` is
 `True`. If the `RequiresRecreation` field is `Always` and the
 `Evaluation` field is `Dynamic`, `Replacement` is
 `Conditional`.


If you have multiple changes with different `RequiresRecreation` values, the
 `Replacement` value depends on the change with the most impact. A
 `RequiresRecreation` value of `Always` has the most impact, followed by
 `Conditional`, and then `Never`.


Type: String


Valid Values: `True | False | Conditional`



Required: No




**ResourceType** 


The type of CloudFormation resource, such as `AWS::S3::Bucket`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**Scope.member.N** 


For the `Modify` action, indicates which resource attribute is triggering this
 update, such as a change in the resource attribute's `Metadata`,
 `Properties`, or `Tags`.


Type: Array of strings


Valid Values: `Properties | Metadata | CreationPolicy | UpdatePolicy | DeletionPolicy | UpdateReplacePolicy | Tags`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceChange "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceChange")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceChange "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceChange")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceChange "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceChange")
