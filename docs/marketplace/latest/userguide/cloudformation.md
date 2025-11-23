# Add CloudFormation templates to your product

AWS Marketplace sellers can list AMI-based products that are delivered to AWS Marketplace buyers by using
AWS CloudFormation templates. Adding a CloudFormation template to your AMI-based product allows your buyers
to deploy your solution without having to manually configure the resources and dependencies. You
can use the templates to define a cluster or distributed architecture for the products or to
select different AMI combinations or product configurations. Single AMI solutions can contain a
maximum of three CloudFormation templates.

The CloudFormation templates can be configured to deliver a single Amazon Machine Image (AMI)
with associated configuration files and Lambda functions. Additionally, you must include an
architectural diagram for each template.

###### Topics

- [Preparing your CloudFormation
  template](#aws-cloudformation-template-preparation "#aws-cloudformation-template-preparation")
- [Architectural diagram](#topology-diagram "#topology-diagram")
- [Convert CloudFormation templates of
  existing products](#convert-cloudformation-templates "#convert-cloudformation-templates")
- [Adding serverless application
  components](cloudformation-serverless-application.md "cloudformation-serverless-application.md")

## Preparing your CloudFormation

template

To build your CloudFormation templates, you must meet the template prerequisites and provide
the required input and security parameters. When submitting your CloudFormation template, use the
guidelines in the following sections.

### Template prerequisites

- Verify that the template is launched successfully through the CloudFormation console
  **in all AWS Regions enabled for your product**. You
  can use the [TaskCat tool](https://github.com/aws-quickstart/taskcat "https://github.com/aws-quickstart/taskcat")
  to test your templates.
- AMIs included in your CloudFormation template must either be the AMI of the product
  you are publishing or an AWS-managed AMI such as the latest Amazon Linux 2. Don't
  include any community AMI or AMI owned and shared by you or any other third-party. To
  use an AWS-managed AMI, use [public parameters in AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/parameter-store-public-parameters.md "../../../systems-manager/latest/userguide/parameter-store-public-parameters.md")
  instead of hardcoding AMI IDs. For example, within your CloudFormation template where
  you specify the AMI ID, you use a dynamic reference `ImageId:
'{{resolve:ssm:/aws/service/ecs/optimized-ami/amazon-linux-2/recommended/image_id}}'`.
- Build templates so that they do not depend on the use in a particular Availability
  Zone (AZ). Not all customers have access to all AZs, and AZs are mapped differently for
  different accounts.
- If you're building a clustered solution using an Amazon EC2 Auto Scaling group, we recommend that you
  account for a scaling event. The new node should join the running cluster
  automatically.
- Even for single-node products, we recommend using an [Amazon EC2 Auto Scaling
  group](../../../autoscaling/latest/userguide/create-asg-from-instance.md "../../../autoscaling/latest/userguide/create-asg-from-instance.md").
- If your solution involves a cluster of multiple instances, consider using placement
  groups if you want low network latency, high network throughput, or both among the
  instances.
- For ease of review by the AWS Marketplace team and transparency to the customer, we
  recommend that you add comments in your **UserData** section.

### Requirements for AMI details

###### Note

If you create an **Amazon Machine Image (AMI) or AMI with
CloudFormation** on the [server products](https://aws.amazon.com//marketplace/management/products/server "https://aws.amazon.com//marketplace/management/products/server") page of the seller portal and are prompted to
download the [product load form](product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product "product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product"), see [Requirements for AMI details using the
product load form](#ami-requirements-product-load-form "#ami-requirements-product-load-form") instead.

When specifying the `ImageId` property of resources that deploy your AMI to
EC2 instances such as [AWS::EC2::Instance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.md"), [AWS::AutoScaling::LaunchConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.md"), and [AWS::EC2::LaunchTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.md") resources, you must reference a
[template parameter.](../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md") The parameter type must be either a
`AWS::EC2::Image::Id`,
`AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>`, or
`String`.

You can name this template parameter any valid parameter name. AWS Marketplace copies your
template to its own Amazon S3 buckets and replaces the specified parameter with an [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") parameter. AWS Marketplace also updates the
description and constraint text to make the correct value clear to buyers who are deploying
the template. When buyers deploy your template, that parameter resolves to the
AWS Region-specific AMI ID of your published product.

The following template examples illustrate the `ImageId` property referencing
template parameters using the intrinsic function [Ref](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md").

YAML example:

```
Parameters:
  ImageId:
    Type: AWS::EC2::Image::Id
    Default: ami-example1234567890
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref ImageId
```

JSON example:

```
{
  "Parameters": {
    "ImageId": {
      "Type": "AWS::EC2::Image::Id",
      "Default": "ami-example1234567890"
    }
  },
  "Resources": {
    "MyInstance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": {
          "Ref": "ImageId"
        }
      }
    }
  }
}
```

If you are deploying EC2 instances inside a [nested stack](../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md") instead of the root stack, the AMI ID must
dynamically inherit its value from the root stack. Edit your root and nested stacks so that
in the root stack, setting the value of your template parameter overrides the AMI ID used in
this nested stack.

### Requirements for AMI details using the

product load form

###### Note

When you create an **Amazon Machine Image (AMI) or AMI with
CloudFormation** on the [server products](https://aws.amazon.com//marketplace/management/products/server "https://aws.amazon.com//marketplace/management/products/server") page of the seller portal and are not
immediately prompted to download the [product load form](product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product "product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product"), see [Requirements for AMI details](#ami-requirements-sse "#ami-requirements-sse") instead.

AMIs must be in a mapping table for each Region. The AWS Marketplace team updates the AMI IDs
after they're cloned. Your source AMI must be in the `us-east-1` Region. The
other Regions can use placeholders.

YAML example:

```
Mappings:
  RegionMap:
      us-east-1:
          ImageId: ami-0123456789abcdef0
      us-west-1:
          ImageId: ami-xxxxxxxxxxxxxxxxx
      eu-west-1:
          ImageId: ami-xxxxxxxxxxxxxxxxx
      ap-southeast-1:
          ImageId: ami-xxxxxxxxxxxxxxxxx
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !FindInMap
        - RegionMap
        - !Ref AWS::Region
        - ImageId
```

### Requirements for nested stack

templates

###### Note

This section only applies to pricing models that do not use the [product load form](product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product "product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product"). For pricing models that _do use_ the product load form, only a fixed string is allowed
for the nested stack `TemplateURL` property.

If your template includes [nested stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md"), the `TemplateURL` property of
nested stack resources must reference the template parameters for the Amazon S3 bucket name,
bucket Region, and Amazon S3 object key prefix. The parameter names for the bucket name must be
`MPS3BucketName`, the bucket Region must be `MPS3BucketRegion`, and
for the object key prefix must be `MPS3KeyPrefix`.

Set the default values for these parameters to correspond to your Amazon S3 bucket where your
nested templates are stored. All nested templates must be publicly accessible. When you
submit your template for publishing, AWS Marketplace copies your templates to its own Amazon S3 buckets and
modifies the properties of those three parameters to have the default value and allowed
value set to correspond with where the copies are stored. AWS Marketplace also updates the description
and constraint text to make the correct values clear to buyers who are deploying the
template.

If you have multiple levels of nested stacks, all nested stacks that create additional
nested stacks must be configured so that the `TemplateURL` property dynamically
inherits the values of the Amazon S3 bucket name, Amazon S3 bucket Region, and Amazon S3 object key from the root
stack. Edit your root and nested stacks so that in the root stack, setting the value of the
template parameter `MPS3BucketName`, `MPS3BucketRegion`, and
`MPS3KeyPrefix` overrides their respective values in the URL used in this
nested stack to create additional nested stacks.

The following template examples illustrate the `TemplateURL` property
referencing template parameters using the intrinsic function [Fn::Sub](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-sub.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-sub.md").

YAML example:

```
AWSTemplateFormatVersion: '2010-09-09'
Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: AWS Marketplace Parameters
        Parameters:
          - ImageId
          - MPS3BucketName
          - MPS3BucketRegion
          - MPS3KeyPrefix
Parameters:
  ImageId:
    Type: AWS::EC2::Image::Id
    Default: ami-example1234567890
    Description: The AMI that will be used to launch EC2 resources.
  MPS3BucketName:
    Type: String
    Default: sellerbucket
    Description: Name of the S3 bucket for your copy of the nested templates.
  MPS3BucketRegion:
    Type: String
    Default: us-east-1
    Description: AWS Region where the S3 bucket for your copy of the nested templates is hosted.
  MPS3KeyPrefix:
    Type: String
    Default: sellerproductfolder/
    Description: S3 key prefix that is used to simulate a folder for your copy of the nested templates.
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref ImageId
  NestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Sub https://${MPS3BucketName}.s3.${MPS3BucketRegion}.${AWS::URLSuffix}/${MPS3KeyPrefix}nested-template.yaml
```

JSON example:

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Metadata": {
        "AWS::CloudFormation::Interface": {
            "ParameterGroups": [
                {
                    "Label": {
                        "default": "AWS Marketplace Parameters"
                    },
                    "Parameters": [
                        "ImageId",
                        "MPS3BucketName",
                        "MPS3BucketRegion",
                        "MPS3KeyPrefix"
                    ]
                }
            ]
        }
    },
    "Parameters": {
        "ImageId": {
            "Type": "AWS::EC2::Image::Id",
            "Default": "ami-example1234567890",
            "Description": "The AMI that will be used to launch EC2 resources."
        },
        "MPS3BucketName": {
            "Type": "String",
            "Default": "sellerbucket",
            "Description": "Name of the S3 bucket for your copy of the nested templates."
        },
        "MPS3BucketRegion": {
            "Type": "String",
            "Default": "us-east-1",
            "Description": "AWS Region where the S3 bucket for your copy of the nested templates is hosted."
        },
        "MPS3KeyPrefix": {
            "Type": "String",
            "Default": "sellerproductfolder/",
            "Description": "S3 key prefix that is used to simulate a folder for your copy of the nested templates."
        }
    },
    "Resources": {
        "EC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": {
                    "Ref": "ImageId"
                }
            }
        },
        "NestedStack": {
            "Type": "AWS::CloudFormation::Stack",
            "Properties": {
                "TemplateURL": {
                    "Fn::Sub": "https://${MPS3BucketName}.s3.${MPS3BucketRegion}.${AWS::URLSuffix}/${MPS3KeyPrefix}nested-template.yaml"
                }
            }
        }
    }
}
```

###### Note

[AWS::CloudFormation::Interface](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-interface.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-interface.md") is used to define how
parameters are grouped and sorted in the AWS CloudFormation console when buyers deploy your
template.

### Template input parameters

- Input parameters to the template must not include the AWS Marketplace customer's AWS
  credentials (such as passwords, public keys, private keys, or certificates).
- For sensitive input parameters such as passwords, choose the `NoEcho`
  property and enable stronger regular expression. For other input parameters, set the
  most common inputs along with appropriate helper text.
- Use CloudFormation parameter types for inputs where available.
- Use `AWS::CloudFormation::Interface` to group and sort input
  parameters.
- Don't set any default values for the following input parameters:

###### Note

Customers must provide these as input parameters.

    + Default CIDR ranges that allow ingress into remote access ports from the public
     internet
    + Default CIDR ranges that allow ingress into database connection ports from the
     public internet
    + Default passwords for users or databases

### Network and security parameters

- Ensure that the default SSH port (22) or RDP port (3389) isn't open to
  0.0.0.0.
- Instead of using the default virtual private cloud (VPC), we recommend that you
  build a VPC with appropriate access control lists (ACLs) and security groups.
- Your template can't request long-term access keys from users or create them to
  access AWS resources. If your AMI application requires access to the AWS services in
  the buyer’s account, it must use [IAM roles for Amazon
  EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md").
- Set IAM roles and policies to [grant the least
  privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") and enable write access only when absolutely necessary. For example,
  if your application needs only `S3:GET`, `PUT`, and
  `DELETE` operations, specify those actions only. We don't recommend the use
  of `S3:*` in this case.

After your template is received, AWS Marketplace validates the product configuration and
information and provides feedback for any required revisions.

## Architectural diagram

You must provide an architectural diagram for each template. To learn more about
diagramming, see [What is
architecture diagramming?](https://aws.amazon.com/what-is/architecture-diagramming/ "https://aws.amazon.com/what-is/architecture-diagramming/")

The diagram must meet the following criteria:

- Illustrate a standard deployment on AWS.
- Depict logically where resources are deployed. For example, resources like Amazon EC2
  instances are in the correct subnet.
- Use the most current AWS product icons for each AWS service deployed through the
  CloudFormation template. To download the current set of architecture icons, see [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons/ "https://aws.amazon.com/architecture/icons/").
- Include metadata for all the services deployed by the CloudFormation template.
- Include all networks, VPCs, and subnets deployed by the CloudFormation template.
- Show integration points, including third party assets, APIs and on-premises, hybrid
  assets.
- Diagrams must be 1100 x 700 pixels in size. Maintain original diagram proportions
  without stretching or cropping.

## Convert CloudFormation templates of

existing products

###### Note

This section is for sellers with an existing AMI with CloudFormation product that used
the [product load form](product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product "product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product") to publish their templates and now want to update that template
without using the product load form. If you are publishing a new product, see [Preparing your CloudFormation templates](cloudformation.md#aws-cloudformation-template-preparation "cloudformation.md#aws-cloudformation-template-preparation").

If you create an **Amazon Machine Image (AMI) or AMI with
CloudFormation** on the [server products](https://aws.amazon.com//marketplace/management/products/server "https://aws.amazon.com//marketplace/management/products/server") page of the seller portal and are prompted to
download the [product load form](product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product "product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product"), see [Requirements for AMI details using the
product load form](#ami-requirements-product-load-form "#ami-requirements-product-load-form").

If you want to use the self-service experience to update an existing product that
previously used the [product load form](product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product "product-submission.md#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product") to publish, you must make changes to your existing CloudFormation
template.

The following table describes the difference between using the product load form and the
self-service experience:

|                                                          | Product load form                                                                                                                                                                                                           | Self-service experience                                                                                                                                                                                                                         |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Value of `ImageId` property for EC2<br>resources**     | References a \*_mapping table_<br>• for your AMI ID. For<br>more information, see [Requirements for AMI details using the<br>product load form](#ami-requirements-product-load-form "#ami-requirements-product-load-form"). | References a \*_template parameter_<br>• for your AMI ID.<br>For more information, see [Requirements for AMI details](#ami-requirements-sse "#ami-requirements-sse").                                                                           |
| **Value of `TemplateURL` property for nested<br>stacks** | Must be a fixed string and can't use intrinsic functions.                                                                                                                                                                   | Can be dynamic by using intrinsic functions. Must reference a set of **template parameters**. For more information, see [Requirements for nested stack<br>templates](#nested-stack-template-requirements "#nested-stack-template-requirements") |

The following example templates illustrate an example of an existing product that used the
product load form to publish the template. In this example, the AMI ID is
`ami-example123456` and a nested template is in a seller’s S3 bucket at the
location
`https://sellerbucket.s3.us-east-1.amazonaws.com/sellerproductfolder/nested-template.yaml`.

YAML example published with the product load form:

```
AWSTemplateFormatVersion: '2010-09-09'
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-example123456
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !FindInMap
        - RegionMap
        - !Ref AWS::Region
        - AMI
  NestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://sellerbucket.s3.us-east-1.amazonaws.com/sellerproductfolder/nested-template.yaml

```

JSON example published with the product load form:

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Mappings": {
        "RegionMap": {
            "us-east-1": {
                "AMI": "ami-example123456"
            }
        }
    },
    "Resources": {
        "EC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": {
                    "Fn::FindInMap": [
                        "RegionMap",
                        {
                            "Ref": "AWS::Region"
                        },
                        "AMI"
                    ]
                }
            }
        },
        "NestedStack": {
            "Type": "AWS::CloudFormation::Stack",
            "Properties": {
                "TemplateURL": "https://sellerbucket.s3.us-east-1.amazonaws.com/sellerproductfolder/nested-template.yaml"
            }
        }
    }
}
```

The following template examples illustrate the changes required to use the self-service
experience to update the product.

YAML example published with the self-service experience:

```
AWSTemplateFormatVersion: '2010-09-09'
Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: AWS Marketplace Parameters
        Parameters:
          - ImageId
          - MPS3BucketName
          - MPS3BucketRegion
          - MPS3KeyPrefix
Parameters:
  ImageId:
    Type: AWS::EC2::Image::Id
    Default: ami-example123456
    Description: The AMI that will be used to launch EC2 resources.
  MPS3BucketName:
    Type: String
    Default: sellerbucket
    Description: Name of the S3 bucket for your copy of the nested templates.
  MPS3BucketRegion:
    Type: String
    Default: us-east-1
    Description: AWS Region where the S3 bucket for your copy of the nested templates is hosted.
  MPS3KeyPrefix:
    Type: String
    Default: sellerproductfolder/
    Description: S3 key prefix that is used to simulate a folder for your copy of the nested templates.
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref ImageId
  NestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Sub https://${MPS3BucketName}.s3.${MPS3BucketRegion}.${AWS::URLSuffix}/${MPS3KeyPrefix}nested-template.yaml
```

JSON Example published with the self-service experience:

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Metadata": {
        "AWS::CloudFormation::Interface": {
            "ParameterGroups": [
                {
                    "Label": {
                        "default": "AWS Marketplace Parameters"
                    },
                    "Parameters": [
                        "ImageId",
                        "MPS3BucketName",
                        "MPS3BucketRegion",
                        "MPS3KeyPrefix"
                    ]
                }
            ]
        }
    },
    "Parameters": {
        "ImageId": {
            "Type": "AWS::EC2::Image::Id",
            "Default": "ami-example123456",
            "Description": "The AMI that will be used to launch EC2 resources."
        },
        "MPS3BucketName": {
            "Type": "String",
            "Default": "sellerbucket",
            "Description": "Name of the S3 bucket for your copy of the nested templates."
        },
        "MPS3BucketRegion": {
            "Type": "String",
            "Default": "us-east-1",
            "Description": "AWS Region where the S3 bucket for your copy of the nested templates is hosted."
        },
        "MPS3KeyPrefix": {
            "Type": "String",
            "Default": "sellerproductfolder/",
            "Description": "S3 key prefix that is used to simulate a folder for your copy of the nested templates."
        }
    },
    "Resources": {
        "EC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": {
                    "Ref": "ImageId"
                }
            }
        },
        "NestedStack": {
            "Type": "AWS::CloudFormation::Stack",
            "Properties": {
                "TemplateURL": {
                    "Fn::Sub": "https://${MPS3BucketName}.s3.${MPS3BucketRegion}.${AWS::URLSuffix}/${MPS3KeyPrefix}nested-template.yaml"
                }
            }
        }
    }
}
```
