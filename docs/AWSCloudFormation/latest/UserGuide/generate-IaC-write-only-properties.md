# Resolve write-only properties

With the CloudFormation IaC generator, you can generate a template using resources provisioned in
 your account that are not already managed by CloudFormation. However, certain resource properties are
 designated as *write-only*, meaning they can be written but can't be read by
 CloudFormation, for example, a database password. 

When generating CloudFormation templates from existing resources, write-only properties pose a
 challenge. In most cases, CloudFormation converts these properties into parameters in the generated
 template. This allows you to enter the properties as parameter values during import operations.
 However, there are scenarios where this conversion is not possible, and CloudFormation handles these
 cases differently.


## Mutually exclusive properties


Some resources have multiple sets of mutually exclusive properties, at least some of which
 are write-only. In these cases, the IaC generator can't determine which set of exclusive
 properties was applied to the resource during creation. For example, you can provide the code for
 a [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html") using one of these sets of properties. 



* `Code/S3Bucket`, `Code/S3Key`, and optionally
 `Code/S3ObjectVersion`
* `Code/ImageUri`
* `Code/ZipFile`

All of these properties are write-only. The IaC generator selects one of the exclusive sets
 of properties and adds them to the generated template. Parameters are added for each of the
 write-only properties. The parameter names include `OneOf` and the parameter
 descriptions indicate that the corresponding property can be replaced with other exclusive
 properties. The IaC generator sets a warning type of `MUTUALLY_EXCLUSIVE_PROPERTIES`
 for the included properties.


## Mutually exclusive types


In some cases, a write-only property can be of multiple data types. For example, the
 `Body` property of [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html") can be either an `object` or a
 `string`. When this is the case, the IaC generator includes the property in the
 generated template using the type of `string` and sets a warning type of
 `MUTUALLY_EXCLUSIVE_TYPES`.


## Array properties


If a write-only property has a type of `array`, the IaC generator can't include
 it in the generated template because parameters can only be scalar values. In this case, the
 property is omitted from the template, and a warning type of `UNSUPPORTED_PROPERTIES`
 is set.


## Optional properties


For optional write-only properties, the IaC generator can’t detect if the property was used
 when setting up the resource. In this case, the property is omitted from the generated template,
 and a warning type of `UNSUPPORTED_PROPERTIES` is set.


## Warnings and next steps


To determine which properties are write-only, you must look at the warnings returned by the
 IaC generator console. The [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html") doesn't indicate if a property is
 write-only, or if it supports multiple types.


Alternatively, you can see which properties are write-only from the resource provider
 schemas. To download the resource provider schemas, see the [CloudFormation resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html"). 


###### To resolve issues with write-only properties

1. Open the [IaC generator
 page](https://console.aws.amazon.com/cloudformation/home?#iac-generator "https://console.aws.amazon.com/cloudformation/home?#iac-generator") of the CloudFormation console.
2. On the navigation bar at the top of the screen, choose the AWS Region for your
 template.
3. Choose the **Templates** tab, and then choose the name of the template
 you created.
4. On the **Template definition** tab, when the generated template includes
 resources with write-only properties, the IaC generator console displays a warning with a
 summary of the type of issues. For example:



![IaC generator console warning about write-only properties in generated template](images/IaC-generator-write-only-property-warning.png)
5. Choose **View warning details** for more details. The resources with
 write-only properties are identified by the logical ID used in the generated template and
 resource type.


Use the list of warnings to identify resources with write-only properties and look at each
 resource to determine what changes (if any) need to be made to the generated template.



![IaC generator console detailed warnings about write-only properties in generated template](images/IaC-generator-write-only-property-resource-warning.png)
6. If your template must be updated to resolve issues with write-only properties, do the
 following: 


	1. Choose **Download** to download a copy of the template.
	2. Edit your template.
	3. When the changes are complete, you can choose the **Import edited
	 template** button to continue the import process.
