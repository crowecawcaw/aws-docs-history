# Overview of CloudFormation macros

There are two major steps to processing templates using macros: creating the macro
itself, and then using the macro to perform processing on your templates.

To create a macro definition, you must create the following:

- A Lambda function to perform the template processing. This Lambda function
  accepts either a snippet or an entire template, and any additional parameters
  that you define. It returns the processed template snippet or the entire
  template as a response.
- A resource of type [AWS::CloudFormation::Macro](../TemplateReference/aws-resource-cloudformation-macro.md "../TemplateReference/aws-resource-cloudformation-macro.md"), which enables users
  to call the Lambda function from within CloudFormation templates. This resource
  specifies the ARN of the Lambda function to invoke for this macro, and additional
  optional properties to assist with debugging. To create this resource within an
  account, author a template that includes the
  `AWS::CloudFormation::Macro` resource, and then create either a
  stack or stack set with self-managed permissions from the template. CloudFormation StackSets
  doesn't currently support creating or updating stack sets with service-managed
  permissions from templates that reference macros.
  To use a macro, reference the macro in your template:

- To process a section, or part, of a template, reference the macro in an
  `Fn::Transform` function located relative to the template content
  you want to transform. When using `Fn::Transform`, you can also pass
  any specified parameters it requires.
- To process an entire template, reference the macro in the [Transform](transform-section-structure.md "transform-section-structure.md") section of the
  template.
  Next, you typically create a change set and then execute it. (Processing macros can
  add multiple resources that you might not be aware of. To ensure that you're aware of
  all of the changes introduced by macros, we strongly advise that you use change sets.)
  CloudFormation passes the specified template content, along with any additional specified
  parameters, to the Lambda function specified in the macro resource. The Lambda function
  returns the processed template content, be it a snippet or an entire template.

After all macros in the template have been called, CloudFormation generates a change set
that includes the processed template content. After you review the change set, execute
it to apply the changes.

![Use the Fn::Transform intrinsic function or the Transform section of the template, to pass the template contents and associated parameters to the macro's underlying Lambda function, which returns the processed template contents.](images/template-macro-use.png)

## How to create stacks directly

To create or update a stack using a template that references macros, you typically
create a change set and then execute it. A change set describes the actions
CloudFormation will take based on the processed template. Processing macros can add
multiple resources that you might not be aware of. To ensure that you're aware of
all the changes introduced by macros, we strongly suggest you use change sets. After
you review the change set, you can execute it to actually apply the changes.

A macro can add IAM resources to your template. For these resources, CloudFormation
requires you to [acknowledge their
capabilities](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities"). Because CloudFormation can't know which resources are added
before processing your template, you might need to acknowledge IAM capabilities
when you create the change set, depending on whether the referenced macros contain
IAM resources. That way, when you run the change set, CloudFormation has the necessary
capabilities to create IAM resources.

To create or update a stack directly from a processed template without first
reviewing the proposed changes in a change set, specify the
`CAPABILITY_AUTO_EXPAND` capability during a `CreateStack`
or `UpdateStack` request. You should only create stacks directly from a
stack template that contains macros if you know what processing the macro performs.
You can't use change sets with stack set macros; you must update your stack set
directly.

For more information, see [CreateStack](../APIReference/API_CreateStack.md "../APIReference/API_CreateStack.md") or [UpdateStack](../APIReference/API_UpdateStack.md "../APIReference/API_UpdateStack.md") in the
_AWS CloudFormation API Reference_.

###### Important

If your stack set template references one or more macros, you must create the
stack set directly from the processed template, without first reviewing the
resulting changes in a change set. Processing macros can add multiple resources
that you might not be aware of. Before you create or update a stack set from a
template that references macros directly, be sure that you know what processing
the macros performs.

To reduce the number of steps for launching stacks from templates that reference
macros, you can use the `package` and `deploy` AWS CLI commands.
For more information, see [Upload local artifacts to an S3 bucket with the
AWS CLI](using-cfn-cli-package.md "using-cfn-cli-package.md") and [Create a stack that includes transforms](service_code_examples.md#deploy-sdk "service_code_examples.md#deploy-sdk").

## Considerations

When working with macros, keep in mind the following notes and limitations:

- Macros are supported only in AWS Regions where Lambda is available. For a
  list of Regions where Lambda is available, see [AWS Lambda endpoints and
  quotas](../../../general/latest/gr/lambda-service.md "../../../general/latest/gr/lambda-service.md").
- Any processed template snippets must be valid JSON.
- Any processed template snippets must pass validation checks for a create
  stack, update stack, create stack set, or update stack set operation.
- CloudFormation resolves macros first, and then processes the template. The
  resulting template must be valid JSON and must not exceed the
  template size limit.
- Because of the order in which CloudFormation processes elements in a template,
  a macro can't include modules in the processed template content it returns
  to CloudFormation. For more information, see [Macro evaluation order](template-macros-author.md#template-macros-order "template-macros-author.md#template-macros-order").
- When using the update rollback feature, CloudFormation uses a copy of the
  original template. It rolls back to the original template even if the
  included snippet was changed.
- Including macros within macros doesn't work because we don't process
  macros recursively.
- The `Fn::ImportValue` intrinsic function isn't currently
  supported in macros.
- Intrinsic functions included in the template are evaluated after any
  macros. Therefore, the processed template content your macro returns can
  include calls to intrinsic functions, and they're evaluated as usual.
- StackSets doesn't currently support creating or updating stack sets
  with service-managed permissions from templates that reference CloudFormation
  macros.

## Macro account scope and

permissions

You can use macros only in the account in which they were created as a resource.
The name of the macro must be unique within a given account. However, you can make
the same functionality available in multiple accounts by enabling cross-account
access on the underlying Lambda function, and then creating macro definitions
referencing that function in multiple accounts. In the example below, three accounts
contain macro definitions that each point to the same Lambda function.

![By allowing cross-account access on the Lambda function, AWS enables you to create macros in multiple accounts that reference that function.](images/template-macro-accounts.png)

To create a macro definition, the user must have permissions to create a stack or
stack set within the specified account.

For CloudFormation to successfully run a macro included in a template, the user must
have `Invoke` permissions for the underlying Lambda function. To prevent
potential escalation of permissions, CloudFormation impersonates the user while running
the macro.

For more information, see [Managing permissions in
AWS Lambda](../../../lambda/latest/dg/lambda-permissions.md "../../../lambda/latest/dg/lambda-permissions.md") in the _AWS Lambda Developer Guide_ and [Actions,
resources, and condition keys for AWS Lambda](../../../service-authorization/latest/reference/list_awslambda.md "../../../service-authorization/latest/reference/list_awslambda.md") in the
_Service Authorization Reference_.
