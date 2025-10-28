# StackInstance

An AWS CloudFormation stack, in a specific account and Region, that's part of a stack set operation. A stack instance is a reference to an attempted or actual stack in a given account within a given Region. A stack instance can exist without a stack—for example, if the stack couldn't be created for some reason. A stack instance is associated with only one stack set. Each stack instance contains the ID of its associated stack set, as well as the ID of the actual stack and the stack status.

## Contents

**Account**

The name of the AWS account that the stack instance is associated with.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**Region**

The name of the AWS Region that the stack instance is associated with.

Type: String

Required: No

**StackInstanceStatus**

The status of the stack instance, in terms of its synchronization with its associated stack set.

- `INOPERABLE`: A `DeleteStackInstances` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further `UpdateStackSet` operations. You might need to perform a `DeleteStackInstances` operation, with `RetainStacks` set to true, to delete the stack instance, and then delete the stack manually.
- `OUTDATED`: The stack isn't currently up to date with the stack set because either
  the associated stack failed during a `CreateStackSet` or `UpdateStackSet` operation,
  or the stack was part of a `CreateStackSet` or `UpdateStackSet` operation that failed or was stopped before the stack was created or updated.
- `CURRENT`: The stack is currently up to date with the stack set.

Type: String

Valid Values: `CURRENT | OUTDATED | INOPERABLE`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/StackInstance.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/StackInstance.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/StackInstance.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/StackInstance.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/StackInstance.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/StackInstance.md")
