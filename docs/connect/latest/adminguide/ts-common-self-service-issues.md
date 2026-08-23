# Common issues

## Bundle the latest AWS SDK with your Lambda functions

If you are calling AI agents APIs directly from Lambda functions,
you must package and bundle the latest version of the AWS SDK along with your
function code. The Lambda runtime environment might include an older version of the
SDK that does not support the latest AI agents API models and
features.

**Symptoms**: You might experience parameter
validation exceptions or request input parameters being silently ignored when
using an outdated SDK version.

To avoid API model drift, include the latest AWS SDK as a dependency in your
deployment package or as a Lambda layer rather than relying on the SDK provided
by the Lambda runtime. The steps to bundle the SDK vary by language. For example,
for Node.js, see [Creating a deployment package with dependencies](../../../lambda/latest/dg/nodejs-package.md#nodejs-package-create-dependencies "../../../lambda/latest/dg/nodejs-package.md#nodejs-package-create-dependencies"). For other
languages, refer to the corresponding Lambda deployment packaging documentation.
For sharing the SDK across multiple functions, see [Lambda layers](../../../lambda/latest/dg/chapter-layers.md "../../../lambda/latest/dg/chapter-layers.md").
