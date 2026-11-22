

# RuntimeConfig

`RuntimeConfig` is a property of `AWS::Serverless::Function` that configures an AWS Lambda (Lambda) Event Function to use a customer-managed runtime. You specify the runtime and the runtime alias that the function uses. The runtime publisher controls which runtime version the alias points to.

AWS SAM supports functions that use an existing customer-managed runtime. It doesn't provide a resource type for creating or publishing runtimes. To create a runtime, see [Creating a runtime](https://docs.aws.amazon.com/lambda/latest/dg/cmr-create.html) in the *AWS Lambda Developer Guide*.

To use `RuntimeConfig`, set the function's [Runtime](sam-resource-function.md#sam-function-runtime) property to `custom`. To learn more about customer-managed runtimes, see [Customer-managed runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-customer-managed.html) and [Using a customer-managed runtime](https://docs.aws.amazon.com/lambda/latest/dg/cmr-using.html) in the *AWS Lambda Developer Guide*.

## Syntax
<a name="sam-property-function-runtimeconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-runtimeconfig-syntax.yaml"></a>

```yaml
[RuntimeAlias](#sam-function-runtimeconfig-runtimealias): {{String}}
[RuntimeArn](#sam-function-runtimeconfig-runtimearn): {{String}}
```

## Properties
<a name="sam-property-function-runtimeconfig-properties"></a>

`RuntimeConfig` has the following properties. You must specify both.

 `RuntimeAlias`   <a name="sam-function-runtimeconfig-runtimealias"></a>
The name of the runtime alias that the function uses, such as `prod`. The alias points to a runtime version. By default, when the runtime publisher points the alias to a new runtime version, the function uses the new version at its next cold start. To control when your function picks up runtime updates, use [RuntimeManagementConfig](sam-resource-function.md#sam-function-runtimemanagementconfig).  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the [RuntimeAlias](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-runtimeconfig.html#cfn-lambda-function-runtimeconfig-runtimealias) property of the `AWS::Lambda::Function` `RuntimeConfig` data type.

 `RuntimeArn`   <a name="sam-function-runtimeconfig-runtimearn"></a>
The Amazon Resource Name (ARN) of the customer-managed runtime, such as `arn:aws:lambda:us-east-1:111122223333:runtime/companyphp8`. Specify the ARN of the runtime, not the ARN of a runtime alias. The runtime must be in the same AWS Region as the function.  
To create a function that uses the runtime, or to change its `RuntimeConfig`, you need the `lambda:AssociateRuntimeAlias` permission on the runtime alias. To use a runtime that another AWS account owns, the runtime's resource-based policy must also allow your account to use it. For more information, see [Before you begin](https://docs.aws.amazon.com/lambda/latest/dg/cmr-using.html#cmr-using-before) in the *AWS Lambda Developer Guide*.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the [RuntimeArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-runtimeconfig.html#cfn-lambda-function-runtimeconfig-runtimearn) property of the `AWS::Lambda::Function` `RuntimeConfig` data type.

## Examples
<a name="sam-property-function-runtimeconfig--examples"></a>

### RuntimeConfig
<a name="sam-property-function-runtimeconfig--examples--runtimeconfig"></a>

The following example configures a function to use the `prod` alias of a customer-managed runtime. The function must also set `Runtime` to `custom`.

#### YAML
<a name="sam-property-function-runtimeconfig--examples--runtimeconfig--yaml"></a>

```yaml
RuntimeConfig:
  RuntimeArn: {{arn:aws:lambda:us-east-1:111122223333:runtime/companyphp8}}
  RuntimeAlias: {{prod}}
```