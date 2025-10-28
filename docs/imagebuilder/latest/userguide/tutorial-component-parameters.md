# Tutorial: Create a custom component with input parameters

You can manage Image Builder components, including creating and setting component parameters,
directly from the EC2 Image Builder console, from the AWS CLI, or from the Image Builder API or SDKs. In
this section, we'll cover creating and using parameters in your component, and setting
component parameters through the Image Builder console and AWS CLI commands at runtime.

###### Important

Component parameters are plain text values, and are logged
in AWS CloudTrail. We recommend that you use AWS Secrets Manager or the AWS Systems Manager Parameter Store to store
your secrets. For more information about Secrets Manager, see [What
is Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_. For more information about
AWS Systems Manager Parameter Store, see [AWS Systems Manager
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.

## Use parameters in your YAML component document

To build a component, you must provide a YAML or JSON application component document. The
document contains the code that runs during the phases and steps that you define to provide customization
for your image. The recipe that references
the component can set the parameters to customize the values at runtime, with default
values that take effect if the parameter is not set to a specific value.

###### Create a component document with input parameters

This section shows you how to define and use input parameters in your YAML
component document.

To create a YAML application component document that uses parameters and runs
commands in your Image Builder build or test instances, follow the steps that match your image
operating system:

Linux

###### Create a YAML component document

Use a file editing tool to create a component document file.
Documentation examples use a file named
`hello-world-test.yaml` that
includes the following content:

```
# Document Start
#
name: "HelloWorldTestingDocument-Linux"
description: "Hello world document to demonstrate parameters."
schemaVersion: 1.0
parameters:
  - MyInputParameter:
      type: string
      default: "It's me!"
      description: This is an input parameter.
phases:
  - name: build
    steps:
      - name: HelloWorldStep
        action: ExecuteBash
        inputs:
          commands:
            - echo "Hello World! Build phase. My input parameter value is {{ MyInputParameter }}"

  - name: validate
    steps:
      - name: HelloWorldStep
        action: ExecuteBash
        inputs:
          commands:
            - echo "Hello World! Validate phase. My input parameter value is {{ MyInputParameter }}"

  - name: test
    steps:
      - name: HelloWorldStep
        action: ExecuteBash
        inputs:
          commands:
            - echo "Hello World! Test phase. My input parameter value is {{ MyInputParameter }}"
# Document End
```

###### Tip

Use a tool like this online [YAML
Validator](https://jsonformatter.org/yaml-validator "https://jsonformatter.org/yaml-validator"), or a YAML lint extension in your code environment to verify
that your YAML is well-formed.

Windows

###### Create a YAML component document

Use a file editing tool to create a component document file.
Documentation examples use a file named
`hello-world-test.yaml` that
includes the following content:

```
# Document Start
#
name: "HelloWorldTestingDocument-Windows"
description: "Hello world document to demonstrate parameters."
schemaVersion: 1.0
parameters:
  - MyInputParameter:
      type: string
      default: "It's me!"
      description: This is an input parameter.
phases:
  - name: build
    steps:
      - name: HelloWorldStep
        action: ExecutePowerShell
        inputs:
          commands:
            - Write-Host "Hello World! Build phase. My input parameter value is {{ MyInputParameter }}"

  - name: validate
    steps:
      - name: HelloWorldStep
        action: ExecutePowerShell
        inputs:
          commands:
            - Write-Host "Hello World! Validate phase. My input parameter value is {{ MyInputParameter }}"

  - name: test
    steps:
      - name: HelloWorldStep
        action: ExecutePowerShell
        inputs:
          commands:
            - Write-Host "Hello World! Test phase. My input parameter value is {{ MyInputParameter }}"
# Document End
```

###### Tip

Use a tool like this online [YAML
Validator](https://jsonformatter.org/yaml-validator "https://jsonformatter.org/yaml-validator"), or a YAML lint extension in your code environment to verify
that your YAML is well-formed.

macOS

###### Create a YAML component document

Use a file editing tool to create a component document file.
Documentation examples use a file named
`hello-world-test.yaml` that
includes the following content:

```
# Document Start
#
name: "HelloWorldTestingDocument-macOS"
description: "Hello world document to demonstrate parameters."
schemaVersion: 1.0
parameters:
  - MyInputParameter:
      type: string
      default: "It's me!"
      description: This is an input parameter.
phases:
  - name: build
    steps:
      - name: HelloWorldStep
        action: ExecuteBash
        inputs:
          commands:
            - echo "Hello World! Build phase. My input parameter value is {{ MyInputParameter }}"

  - name: validate
    steps:
      - name: HelloWorldStep
        action: ExecuteBash
        inputs:
          commands:
            - echo "Hello World! Validate phase. My input parameter value is {{ MyInputParameter }}"

  - name: test
    steps:
      - name: HelloWorldStep
        action: ExecuteBash
        inputs:
          commands:
            - echo "Hello World! Test phase. My input parameter value is {{ MyInputParameter }}"
# Document End
```

###### Tip

Use a tool like this online [YAML
Validator](https://jsonformatter.org/yaml-validator "https://jsonformatter.org/yaml-validator"), or a YAML lint extension in your code environment to verify
that your YAML is well-formed.

For more information about the phases, steps, and syntax for AWSTOE
application component documents, see
[Use documents in AWSTOE](toe-use-documents.md "toe-use-documents.md"). For more information about parameters and their
requirements, see the [Parameters](toe-user-defined-variables.md#user-defined-vars-parameters "toe-user-defined-variables.md#user-defined-vars-parameters")
section of the **Define and reference variables in AWSTOE** page.

###### Create a component from the YAML component document

Whatever method you use to create an AWSTOE component, the YAML application
component document is always required as a baseline.

- To create a component directly from your YAML document with the Image Builder console,
  see [Create a custom component from the console](create-component.md#create-component-ib-console "create-component.md#create-component-ib-console").
- To create a component from the command line with the Image Builder **create-component**
  command, see [Create a custom component from the AWS CLI](create-component.md#create-component-ib-cli "create-component.md#create-component-ib-cli").
  Replace the YAML document name in those examples with the name of your Hello World YAML
  document (`hello-world-test.yaml`).

## Set component parameters in an Image Builder recipe from the console

Setting component parameters works the same for image recipes and container recipes.
When you create a new recipe, or a new version of a recipe, you choose which components to
include from the **Build components** and **Test components**
lists. The component lists include components that are applicable for the base operating
system you chose for your image.

After you select a component, it is displayed in the **Selected
components** section, directly under the component lists. Configuration
options are shown for each component that is selected. If your component has input
parameters defined, they are displayed as an expandable section called **Input
parameters**.

The following parameter settings are shown for each parameter that's defined for your component:

- **Parameter name** (_not editable_) –
  The name of the parameter.
- **Description** (_not editable_) –
  The parameter description
- **Type** (_not editable_) –
  The data type for the parameter value.
- **Value** – The value for the parameter. If you are using this component for the first time in this recipe, and
  a default value was defined for the input parameter, the default value appears in the
  **Value** box with greyed-out text. If no other value is entered, Image Builder
  uses the default value.
