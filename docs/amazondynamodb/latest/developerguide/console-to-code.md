

# Generate infrastructure code for Amazon DynamoDB using Console-to-Code
<a name="console-to-code"></a>

Amazon Q Developer's Console-to-Code feature simplifies infrastructure management for Amazon DynamoDB by transforming manual table creation steps into reproducible automation code. This capability helps developers efficiently scale database resource configuration across their environments. For more information, see [Automating AWS services with Amazon Q Developer Console-to-Code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/console-to-code.html).

Console-to-Code captures detailed DynamoDB table configurations, including partition keys, sort keys, provisioned throughput settings, and secondary indexes, and converts these into precise infrastructure-as-code templates. Using generative AI, the tool ensures generated code maintains the parameter compatibility established during your console workflow.

Developers can generate DynamoDB infrastructure code in multiple formats, such as:
+ AWS Cloud Development Kit (AWS CDK) in TypeScript, Python, and Java
+ CloudFormation in YAML or JSON

This approach allows teams to:
+ Standardize database resource management
+ Implement version-controlled infrastructure
+ Reduce manual configuration errors

Console-to-Code for Amazon DynamoDB is available in all commercial AWS Regions, providing a powerful solution for transforming manual configurations into automated, reproducible infrastructure code.

## How it works
<a name="how-it-works"></a>

When using Console-to-Code with DynamoDB, the process typically involves:

1. **Prototyping in the console** – Use the DynamoDB console to create and configure resources like tables. See [Connect to Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html) for more information.

1. **Recording actions** – Console-to-Code records these actions as you perform them.

1. **Code generation** – The feature uses Amazon Q Developer's generative AI capabilities to transform your console actions into reusable code in your preferred format.

1. **Code customization** – You can then copy or download this code and further customize it for your production workloads.

## Benefits of using Console-to-Code with DynamoDB
<a name="benefits"></a>

**Simplified automation**  
Convert manual DynamoDB table creation and configuration into reusable code with a single click.

**Best practices**  
Generated code follows AWS guided best practices for reliable deployments.

**Bridge between console and code**  
You don't have to choose between using the AWS Management Console or Infrastructure-as-Code (IaC). You can use both approaches together.

**Accelerated development**  
Get started quickly with automation code that can be further customized for production use.

## Example use cases
<a name="example-use-cases"></a>
+ Creating DynamoDB tables with specific attributes, keys, and capacity settings
+ Setting up Global Secondary Indexes and Local Secondary Indexes
+ Configuring auto-scaling policies for DynamoDB tables
+ Establishing backup and restore configurations
+ Creating and managing DynamoDB Streams

## Getting started
<a name="getting-started"></a>

To start using Console-to-Code with DynamoDB:

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodbv2/](https://console.aws.amazon.com/dynamodbv2/).

1. Begin creating or modifying DynamoDB resources through the console interface.

1. Use the Console-to-Code feature to generate code for your actions in your preferred format.

1. Copy or download the generated code and customize it as needed for your specific requirements.

For more information and detailed instructions on how to use Console-to-Code, see [Automating AWS services with Amazon Q Developer Console-to-Code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/console-to-code.html) in the *Amazon Q Developer User Guide*.