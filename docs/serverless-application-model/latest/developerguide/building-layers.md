# Building Lambda layers in AWS SAM

You can use AWS SAM to build custom Lambda layers. Lambda layers allow you to extract code from a Lambda function
that can then be re-used across several Lambda functions. Building only Lambda layers
(instead of building your entire application) can benefit you in a few ways. It can help you reduce the size of
your deployment packages, separate core function logic from dependencies, and allow you to share dependencies
across multiple functions. For information about layers, see [AWS Lambda
layers](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md") in the _AWS Lambda Developer Guide_.

## How to build a Lambda layer in AWS SAM

###### Note

Before you can build a Lambda layer, you must first write a Lambda layer in your AWS SAM template. For information and examples on doing this, see
[Increase efficiency using Lambda layers with AWS SAM](serverless-sam-cli-layers.md "serverless-sam-cli-layers.md").

To build a custom layer, declare it in your AWS Serverless Application Model (AWS SAM) template file and include a
`Metadata` resource attribute section with a `BuildMethod` entry. Valid
values for `BuildMethod` are identifiers for an [AWS Lambda runtime](../../../lambda/latest/dg/lambda-runtimes.md "../../../lambda/latest/dg/lambda-runtimes.md"), or `makefile`.
Include a `BuildArchitecture` entry to specify the instruction set architectures that
your layer supports. Valid values for `BuildArchitecture` are [Lambda instruction set
architectures](../../../lambda/latest/dg/foundation-arch.md "../../../lambda/latest/dg/foundation-arch.md").

If you specify `makefile`, provide the custom makefile, where you declare a build
target of the form `build-`layer-logical-id``that contains
 the build commands for your layer. Your makefile is responsible for compiling the layer if
 necessary, and copying the build artifacts into the proper location required for subsequent
 steps in your workflow. The location of the makefile is specified by the`ContentUri` property of the layer resource, and must be named`Makefile`.

###### Note

When you create a custom layer, AWS Lambda depends on environment variables to find your
layer code. Lambda runtimes include paths in the `/opt` directory where your layer
code is copied into. Your project's build artifact folder structure must match the runtime's
expected folder structure so your custom layer code can be found.

For example, for Python you can place your code in the `python/` subdirectory.
For NodeJS, you can place your code in the `nodejs/node_modules/`
subdirectory.

For more information, see [Including library
dependencies in a layer](../../../lambda/latest/dg/configuration-layers.md#configuration-layers-path "../../../lambda/latest/dg/configuration-layers.md#configuration-layers-path") in the _AWS Lambda Developer Guide_.

The following is an example `Metadata` resource attribute section.

```
    Metadata:
      BuildMethod: python3.12
      BuildArchitecture: arm64
```

###### Note

If you don't include the `Metadata` resource attribute section, AWS SAM doesn't
build the layer. Instead, it copies the build artifacts from the location specified in the
`CodeUri` property of the layer resource. For more information, see the [ContentUri](sam-resource-layerversion.md#sam-layerversion-contenturi "sam-resource-layerversion.md#sam-layerversion-contenturi") property of the
`AWS::Serverless::LayerVersion` resource type.

When you include the `Metadata` resource attribute section, you can use the
`sam build` command to build the layer,
both as an independent object, or as a dependency of an AWS Lambda function.

- \***\*As an independent
  object.\*\*** You might want to build just the layer object, for example
  when you're locally testing a code change to the layer and don't need to build your entire
  application. To build the layer independently, specify the layer resource with the `sam
build `layer-logical-id`` command.
- **As a dependency of a Lambda function.** When you include a
  layer's logical ID in the `Layers` property of a Lambda function in the same AWS SAM
  template file, the layer is a dependency of that Lambda function. When that layer also
  includes a `Metadata` resource attribute section with a `BuildMethod`
  entry, you build the layer either by building the entire application with the `sam
build` command or by specifying the function resource with the `sam build
`function-logical-id`` command.

## Examples

### Template example 1: Build a layer

against the Python 3.12 runtime environment

The following example AWS SAM template builds a layer against the Python 3.12 runtime
environment.

```
Resources:
  MyLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      ContentUri: my_layer
      CompatibleRuntimes:
        - python3.12
    Metadata:
      BuildMethod: python3.12   # Required to have AWS SAM build this layer
```

### Template example 2: Build a layer

using a custom makefile

The following example AWS SAM template uses a custom `makefile` to build the
layer.

```
Resources:
  MyLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      ContentUri: my_layer
      CompatibleRuntimes:
        - python3.12
    Metadata:
      BuildMethod: makefile
```

The following `makefile` contains the build target and commands that will be
executed. Note that the `ContentUri` property is set to `my_layer`, so
the makefile must be located in the root of the `my_layer` subdirectory, and the
filename must be `Makefile`. Note also that the build artifacts are copied into
the `python/` subdirectory so that AWS Lambda will be able to find the layer
code.

```
build-MyLayer:
  mkdir -p "$(ARTIFACTS_DIR)/python"
  cp *.py "$(ARTIFACTS_DIR)/python"
  python -m pip install -r requirements.txt -t "$(ARTIFACTS_DIR)/python"
```

###### Note

When the `makefile` is called, the appropriate target is triggered and artifacts should be copied to the exposed environmental variable `$ARTIFACTS_DIR`. For more information, refer to
[aws-lambda-builders in GitHub](https://github.com/aws/aws-lambda-builders/blob/develop/aws_lambda_builders/workflows/custom_make/DESIGN.md "https://github.com/aws/aws-lambda-builders/blob/develop/aws_lambda_builders/workflows/custom_make/DESIGN.md").

### Example sam build commands

The following `sam build` commands build layers that include the
`Metadata` resource attribute sections.

```
# Build the 'layer-logical-id' resource independently
`$` `sam build `layer-logical-id``

# Build the 'function-logical-id' resource and layers that this function depends on
`$` `sam build `function-logical-id``

# Build the entire application, including the layers that any function depends on
`$` `sam build`
```
