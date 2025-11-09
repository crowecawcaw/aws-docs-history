Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Invoking a Lambda function using a workflow

This section describes how to invoke a AWS Lambda function using a CodeCatalyst workflow. To
accomplish this, you must add the **AWS Lambda invoke** action to your workflow.
The **AWS Lambda invoke** action invokes the Lambda function that you
specify.

In addition to invoking your function, the **AWS Lambda invoke** action also
converts each top-level key in the response payload received from the Lambda function into a
[workflow output variable](workflows-working-with-variables.md "workflows-working-with-variables.md"). These
variables can then be referenced in subsequent workflow actions. If you don't want all top-level
keys to be converted to variables, you can use filters to specify the exact ones. For more
information, see [ResponseFilters](lam-invoke-action-ref.md#lam.invoke.response.filters "lam-invoke-action-ref.md#lam.invoke.response.filters") property description in the ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md "lam-invoke-action-ref.md").

###### Topics

- [When to use this action](#lam-invoke-action-when-to-use "#lam-invoke-action-when-to-use")
- [Runtime image used by the 'AWS Lambda invoke'
  action](#lam-invoke-action-runtime "#lam-invoke-action-runtime")
- [Example: Invoke a Lambda
  function](lam-invoke-action-example-workflow.md "lam-invoke-action-example-workflow.md")
- [Adding the 'AWS Lambda invoke' action](lam-invoke-action-add.md "lam-invoke-action-add.md")
- ['AWS Lambda invoke' variables](lam-invoke-action-variables.md "lam-invoke-action-variables.md")
- ['AWS Lambda invoke' action YAML](lam-invoke-action-ref.md "lam-invoke-action-ref.md")

## When to use this action

Use this action if you want to add functionality to your workflow that is encapsulated in,
and performed by, a Lambda function.

For example, you might want your workflow to send a `Build started`
notification to a Slack channel before starting a build of your application. In this case,
your workflow would include an **AWS Lambda invoke** action to invoke a Lambda
to send out the Slack notification, and a [build action](build-add-action.md "build-add-action.md")
to build your application.

As another example, you might want your workflow to conduct a vulnerability scan on your
application before it is deployed. In this case, you would use a build action to build your
application, an **AWS Lambda invoke** action to invoke a Lambda to scan for
vulnerabilities, and a deploy action to deploy the scanned application.

## Runtime image used by the 'AWS Lambda invoke'

action

The **AWS Lambda invoke** action runs on a [November 2022 image](build-images.md#build.previous-image "build-images.md#build.previous-image"). For more information, see [Active images](build-images.md#build-curated-images "build-images.md#build-curated-images").
