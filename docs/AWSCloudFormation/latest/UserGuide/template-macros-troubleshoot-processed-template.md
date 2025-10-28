# Troubleshoot the

processed template

When using a macro, the processed template can be found in the CloudFormation
console.

The stage of a template indicates its processing status:

- `Original`: The template that the user originally submitted to
  create or update the stack or stack set.
- `Processed`: The template CloudFormation used to create or update the
  stack or stack set after processing any referenced macros. The processed
  template is formatted as JSON, even if the original template was formatted as
  YAML.
  For troubleshooting, use the processed template. If a template doesn't reference
  macros, the original and processed templates are identical.

For more information, see [View stack information from the
CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md").

To use the AWS CLI to get the processed template, use the [get-template](service_code_examples.md#get-template-sdk "service_code_examples.md#get-template-sdk") command.

## Size limitation

The maximum size for a processed stack template is 51,200 bytes when passed
directly into a `CreateStack`, `UpdateStack`, or
`ValidateTemplate` request, or 1 MB when passed as an S3 object using
an Amazon S3 template URL. However, during processing CloudFormation updates the temporary
state of the template as it serially processes the macros contained in the template.
Because of this, the size of the template during processing may temporarily exceed
the allowed size of a fully-processed template. CloudFormation allows some buffer for
these in-process templates. However, you should design your templates and macros
keeping in mind the maximum allowed size for a processed stack template.

If CloudFormation returns a `Transformation data limit exceeded` error
while processing your template, your template has exceeded the maximum template size
CloudFormation allows during processing.

To resolve this issue, consider doing the following:

- Restructure your template into multiple templates to avoid exceeding the
  maximum size for in-process templates. For example:
  - Use nested stack templates to encapsulate parts of the template.
    For more information, see [Split a template into reusable pieces using nested
    stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md").
  - Create multiple stacks and use cross-stack references to exchange
    information between them. For more information, see [Refer to resource outputs in another CloudFormation
    stack](walkthrough-crossstackref.md "walkthrough-crossstackref.md").

- Reduce the size of template fragment returned by a given macro. CloudFormation
  doesn't tamper with the contents of fragments returned by macros.
