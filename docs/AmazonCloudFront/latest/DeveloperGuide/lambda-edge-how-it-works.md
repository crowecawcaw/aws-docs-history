# Get started with Lambda@Edge functions (console)

With Lambda@Edge, you can use CloudFront triggers to invoke a Lambda function. When you
associate a CloudFront distribution with a Lambda function, CloudFront [intercepts requests and responses](../../../lambda/latest/dg/lambda-edge.md "../../../lambda/latest/dg/lambda-edge.md") at
CloudFront edge locations and runs the function. Lambda functions can improve security or
customize information close to your viewers to improve performance.

The following list provides a basic overview of how to create and use Lambda functions
with CloudFront.

###### Overview: Creating and using Lambda functions with CloudFront

1. Create a Lambda function in the US East (N. Virginia) Region.
2. Save and publish a numbered version of the function.

If you want to change the function, you must edit the $LATEST version of the
function in the US East (N. Virginia) Region. Then, before you set it up to work with CloudFront,
you publish a new numbered version. 3. Associate the function with a CloudFront distribution and cache behavior. Then
specify one or more CloudFront events (_triggers_) that cause the
function to execute. For example, you can create a trigger for the function to
execute when CloudFront receives a request from a viewer. 4. When you create a trigger, Lambda creates replicas of the function at AWS
locations around the world.

###### Tip

For more information, see [creating and
updating functions](lambda-edge-create-function.md "lambda-edge-create-function.md"), [the event
structure](lambda-event-structure.md "lambda-event-structure.md"), and [adding CloudFront
triggers](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md"). You can also find more ideas and get code samples in [Lambda@Edge example functions](lambda-examples.md "lambda-examples.md").

For a step-by-step tutorial, see the following topic:

###### Topics

- [Tutorial: Create a basic
  Lambda@Edge function (console)](lambda-edge-how-it-works-tutorial.md "lambda-edge-how-it-works-tutorial.md")
