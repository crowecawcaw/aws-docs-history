

# Use variables in formula expressions
<a name="expression-variables"></a>

Variables represent AWS IoT SiteWise asset properties in formula expressions. Use variables to input values from other asset properties in your expressions, so that you can process data from constant properties ([attributes](attributes.md)), raw data streams ([measurements](measurements.md)), and other formula properties.

Variables can represent asset properties from the same asset model or from associated child asset models. Only metric formulas can input variables from child asset models.

You identify variables by different names in the console and the API.
+ **AWS IoT SiteWise console** – Use asset property names as variables in your expressions.
+ **AWS IoT SiteWise API (AWS CLI, AWS SDKs)** – Define variables with the [ExpressionVariable](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExpressionVariable.html) structure, which requires a variable name and a reference to an asset property. The variable name can contain lowercase letters, numbers, and underscores. Then, use variable names to reference asset properties in your expressions.

Variable names are case sensitive.

For more information, see [Defining transforms](transforms.md) and [Defining metrics](metrics.md).

## Use variables to reference properties
<a name="variable-values"></a>

A variable's *value* defines the property that it references. AWS IoT SiteWise provides different ways to do this.
+ **By property ID:** You can specify the property's unique ID (UUID) to identify it.
+ **By name:** If the property is on the same asset model, you can specify its name in the property ID field.
+ **By path:** A variable value can refer to a property by its *path.* For more information, see [Use paths to reference custom composite model properties](custom-composite-models.md#property-paths).

**Note**  
 Variables are not supported by AWS IoT SiteWise console. They are used by AWS IoT SiteWise API, including the AWS Command Line Interface AWS CLI) and AWS SDKs. 

 A variable that you receive in a response from AWS IoT SiteWise includes full information about the value, including both the ID and the path.

 However, when you pass a variable into AWS IoT SiteWise (for example, in a "create" or "update" call), you only need to specify one of these. For example, if you specify the path, you don't need to provide the ID. 