# ModuleInfo

Contains information about the module from which the resource was created, if the resource
 was created from a module included in the stack template.

For more information about modules, see [Create reusable resource configurations
 that can be included across templates with CloudFormation modules](../UserGuide/modules.md "../UserGuide/modules.md") in the
 *AWS CloudFormation User Guide*.


## Contents





**LogicalIdHierarchy** 


A concatenated list of the logical IDs of the module or modules that contains the resource.
 Modules are listed starting with the inner-most nested module, and separated by
 `/`.


In the following example, the resource was created from a module, `moduleA`,
 that's nested inside a parent module, `moduleB`.



`moduleA/moduleB`



For more information, see [Reference module resources in
 CloudFormation templates](../UserGuide/module-ref-resources.md "../UserGuide/module-ref-resources.md") in the *AWS CloudFormation User Guide*.


Type: String


Required: No




**TypeHierarchy** 


A concatenated list of the module type or types that contains the resource. Module types are
 listed starting with the inner-most nested module, and separated by `/`.


In the following example, the resource was created from a module of type
 `AWS::First::Example::MODULE`, that's nested inside a parent module of type
 `AWS::Second::Example::MODULE`.



`AWS::First::Example::MODULE/AWS::Second::Example::MODULE`



Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ModuleInfo "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ModuleInfo")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ModuleInfo "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ModuleInfo")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ModuleInfo "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ModuleInfo")
