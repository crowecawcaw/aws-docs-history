

# Custom blueprints
<a name="custom-blueprint"></a>

Custom blueprints in Amazon SageMaker Unified Studio enable organizations to standardize and accelerate how data projects get set up. They are administrator-defined templates, powered by AWS CloudFormation, that give teams a ready-made starting point for analytics and machine learning environments.

In addition to the blueprints that Amazon SageMaker Unified Studio provides, you can also design your own. For more information, see [Supported blueprints](supported-blueprints.md). With custom blueprints, organizations can include their specific dependencies, security controls, and best practices to allow for new projects to align with internal standards. Since they're defined through infrastructure-as-code, custom blueprints are easy to version control, share across teams, and evolve over time. This not only speeds up onboarding but also keeps projects consistent and governed, no matter how big or distributed your data science organization becomes.

**Topics**
+ [Register a custom blueprint in the console](#custom-blueprint-register-console)
+ [Register a custom blueprint with the API](#custom-blueprint-register-api)
+ [Reserved parameters](#custom-blueprint-reserved-parameters)
+ [Trust policy for the provisioning role](#custom-blueprint-trust-policy)
+ [Sample custom blueprint template](#custom-blueprint-sample-template)

## Register a custom blueprint in the console
<a name="custom-blueprint-register-console"></a>

Have your AWS CloudFormation template ready before you start. The Amazon SageMaker Unified Studio console accepts either an Amazon S3 URL or a file that you upload.

1. Open the [Amazon SageMaker Unified Studio console](https://console.aws.amazon.com/datazone/), and then use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains**, and then choose the domain's name (shown as a hyperlink) from the list.

1. On the domain's details page, navigate to the **Blueprints** tab. 

1. In the **Blueprints** tab, in the **Blueprints** section, choose **Create**. This brings up the **Create custom blueprint** page.

1. In the **Create custom blueprint** page, specify the following and then choose **Next**:
   + **Name** - the name for your custom blueprint. This blueprint name cannot be changed after the blueprint is created.
   + **Description** - optional - the description for your custom blueprint.
   + In the **Upload CloudFormation template** section, specify the Amazon S3 file path where the custom AWS CloudFormation template for your blueprint is stored. You can choose to either specify the Amazon S3 URL for your template or you can choose to upload your own template file.
**Note**  
Choose **View templates** on the **Blueprints** page to open the sample template in the console, where you can modify it. For the same template with an explanation of what it creates, see [Sample custom blueprint template](#custom-blueprint-sample-template).

1. In the **Configure editable parameters** page, you can choose the parameters for your custom blueprint. Editable parameters are values that are visible and editable when this blueprint is used in project profiles. On this page, you can remove parameters that you don't want to be editable in project profiles, or edit their default values. Then choose **Next**.

1. In the **Enable blueprint - optional** page, you can enable your custom blueprint so that it can be used in project profiles and projects.

   If you choose to enable your custom blueprint at this point, in the **Provisioning role**, you must specify the role that Amazon SageMaker Unified Studio can use to provision and manage resources defined in this blueprint in your account.

   Also, in the **Authorized domain units** section, you must specify the domain units where projects can access resources defined by this custom blueprint. 

   Then choose **Next**.

1. Review your selections in the **Review and create** page, and then choose **Create blueprint**.

Now that your custom blueprint is created, you can use it when creating custom project profiles. For more information, see [Custom project profile](custom.md).

## Register a custom blueprint with the API
<a name="custom-blueprint-register-api"></a>

The `CreateEnvironmentBlueprint` API requires an Amazon S3 URL for the AWS CloudFormation template. The blueprint's provisioning role must have access to that Amazon S3 object. The `SageMakerStudioProjectProvisioningRolePolicy` managed policy grants `s3:GetObject` on buckets whose names begin with `amazon-sagemaker-cf-templates`. The console creates such a bucket when you upload a template there.

```
aws datazone create-environment-blueprint \
  --domain-identifier {{domain-id}} \
  --name {{blueprint-name}} \
  --provisioning-properties '{
    "cloudFormation": {
      "templateUrl": "https://amazon-sagemaker-cf-templates-{{region}}-{{suffix}}.s3.{{region}}.amazonaws.com/my-template.yaml"
    }
  }'
```

**Note**  
You can categorize a custom blueprint as Tooling by setting `blueprintCategory` to `TOOLING`, so it serves as a project's Tooling environment in place of the one Amazon SageMaker Unified Studio provides. For more information about what a Tooling template must declare and how to register one, see [Custom blueprints as Tooling](tooling-custom-blueprints.md).

After you create the blueprint, Amazon SageMaker Unified Studio disables it by default. To enable a blueprint in an AWS Region, you must supply a provisioning role with permissions for all resources in the template.

```
aws datazone put-environment-blueprint-configuration \
  --domain-identifier {{domain-id}} \
  --environment-blueprint-identifier {{blueprint-id}} \
  --enabled-regions {{region}} \
  --provisioning-role-arn {{provisioning-role-arn}}
```

## Reserved parameters
<a name="custom-blueprint-reserved-parameters"></a>

Reserved parameters are AWS CloudFormation parameters whose values Amazon SageMaker Unified Studio supplies when it deploys your template. The names are case-sensitive. When Amazon SageMaker Unified Studio cannot find a value for an optional parameter, an empty string is injected, which overrides any `Default` you declared. The one exception is `sagemakerUnifiedStudioNetworkGlueConnectionNames`, which Amazon SageMaker Unified Studio omits instead, leaving your `Default` in place.

The prefixes `amazon`, `aws`, `datazone`, and `sagemaker` are reserved. When you register a blueprint, Amazon SageMaker Unified Studio rejects any name in `userParameters` that begins with one of them, whether or not it appears in the table.


| Parameter name | Optional | Description | 
| --- | --- | --- | 
| awsDefaultGlueCatalogKmsKeyArn | Yes | The ARN of the AWS KMS key for the default AWS Glue Data Catalog. | 
| datazoneEnvironmentDomainArn | No | The ARN of the Amazon SageMaker Unified Studio domain. | 
| datazoneEnvironmentDomainId | No | The ID of the Amazon SageMaker Unified Studio domain. | 
| datazoneEnvironmentDomainKmsKeyArn | Yes | The ARN of the AWS KMS key for the Amazon SageMaker Unified Studio domain. | 
| datazoneEnvironmentEnvironmentId | No | The ID of the environment. | 
| datazoneEnvironmentIdentityCenterInstanceArn | Yes | The ARN of the AWS IAM Identity Center instance for the Amazon SageMaker Unified Studio domain. | 
| datazoneEnvironmentProjectExecutionRoleArn | Yes | The ARN of the project execution role that you supply when you create the project. IAM-based domains only. | 
| datazoneEnvironmentProjectId | No | The ID of the project. | 
| datazoneEnvironmentProjectName | No | The name of the project. | 
| datazoneEnvironmentProvisioningRoleArn | No | The ARN of the provisioning role for the blueprint. | 
| sagemakerUnifiedStudioKmsKeyArn | Yes | The ARN of the AWS KMS key that you set on the blueprint configuration for the AWS Region. | 
| sagemakerUnifiedStudioNetworkGlueConnectionNames | Yes | The names of the AWS Glue connections for the VPC, as a comma-separated list. We omit this parameter entirely rather than sending an empty value, which leaves your Default in place. | 
| sagemakerUnifiedStudioNetworkSecurityGroupId | Yes | The ID of the security group for the VPC. | 
| sagemakerUnifiedStudioNetworkSubnets | Yes | The IDs of the subnets in the VPC, as a comma-separated list. | 
| sagemakerUnifiedStudioNetworkVpcId | Yes | The ID of the VPC for the Amazon SageMaker Unified Studio domain. | 
| sagemakerUnifiedStudioToolingEnvironmentId | Yes | The ID of the project's Tooling environment. | 
| sagemakerUnifiedStudioToolingIamConnectionId | Yes | The ID of the IAM connection for the project. | 
| sagemakerUnifiedStudioToolingKmsKeyArn | Yes | The ARN of the AWS KMS key for the project. | 
| sagemakerUnifiedStudioToolingS3BucketArn | Yes | The ARN of the Amazon S3 bucket for the project. | 
| sagemakerUnifiedStudioToolingUserRoleArn | Yes | The ARN of the project user role. Use it as the principal when your template grants project members access to a resource. | 

**Important**  
Reserved parameter names are case-sensitive. If your template declares a parameter that begins with a reserved prefix (`amazon`, `aws`, `datazone`, or `sagemaker`) but doesn't match a reserved name exactly, Amazon SageMaker Unified Studio doesn't supply a value for it. Deployment then fails, because CloudFormation rejects a parameter it received no value for:  

```
Parameters: [{{parameterName}}] must have values
```
Review the parameters that your template declares and confirm that each name matches the preceding table exactly, including case.

## Trust policy for the provisioning role
<a name="custom-blueprint-trust-policy"></a>

Amazon SageMaker Unified Studio assumes the blueprint's provisioning role with `sts:AssumeRole` to deploy your AWS CloudFormation template. It also attaches your user context to that session as tags with `sts:TagSession`. Amazon SageMaker Unified Studio resources such as connections and data sources require this user context to provision. Therefore, the trust policy of the provisioning role must allow both actions for the `datazone.amazonaws.com` service principal, as shown in the following example. The `aws:SourceAccount` condition restricts the role to your own AWS account, which guards against the cross-service confused deputy problem.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "datazone.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

## Sample custom blueprint template
<a name="custom-blueprint-sample-template"></a>

The following template creates an AWS Glue database in your SageMaker Lakehouse catalog, grants the project's users access to it through AWS Lake Formation, and attaches a managed policy to the project's role. It is the same template that the **View templates** button on the **Blueprints** page shows.

```
{
  "Parameters": {
    "datazoneEnvironmentEnvironmentId": {
      "Type": "String",
      "Description": "EnvironmentId for which the resource will be created for."
    },
    "datazoneEnvironmentProjectId": {
      "Type": "String",
      "Description": "DZ projectId for which project the resource will be created for."
    },
    "userRoleArn": {
      "Type": "String",
      "Description": "Project Role ARN"
    },
    "glueDbName": {
      "Type": "String",
      "Default": "gluedb",
      "Description": "Glue DB name"
    }
  },
  "Resources": {
    "GlueDatabase": {
      "Type": "AWS::Glue::Database",
      "Properties": {
        "CatalogId": {
          "Ref": "AWS::AccountId"
        },
        "DatabaseInput": {
          "CreateTableDefaultPermissions": [],
          "Description": {
            "Fn::Join": [
              "",
              [
                "Created by DataZone for project ",
                {
                  "Ref": "datazoneEnvironmentProjectId"
                }
              ]
            ]
          },
          "LocationUri": {
            "Fn::Join": [
              "",
              [
                {
                  "Fn::ImportValue": {
                    "Fn::Join": [
                      "",
                      [
                        "s3BucketPath-",
                        {
                          "Ref": "datazoneEnvironmentProjectId"
                        },
                        "-dev"
                      ]
                    ]
                  }
                },
                "/data/catalogs/"
              ]
            ]
          },
          "Name": {
            "Fn::Sub": "${glueDbName}-${datazoneEnvironmentEnvironmentId}"
          }
        }
      }
    },
    "GlueAccessManagedPolicy": {
      "Type": "AWS::IAM::ManagedPolicy",
      "Properties": {
        "ManagedPolicyName": {
          "Fn::Sub": "GlueAccess-${glueDbName}-${datazoneEnvironmentEnvironmentId}-Policy"
        },
        "PolicyDocument": {
          "Version": "2012-10-17",		 	 	 
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "glue:GetDatabase",
                "glue:GetTables",
                "glue:GetTable",
                "glue:CreateTable",
                "glue:UpdateTable",
                "glue:DeleteTable",
                "glue:BatchDeleteTable",
                "glue:GetPartitions",
                "glue:GetPartition",
                "glue:BatchCreatePartition",
                "glue:BatchDeletePartition"
              ],
              "Resource": [
                {
                  "Fn::Sub": "arn:aws:glue:${AWS::Region}:${AWS::AccountId}:catalog"
                },
                {
                  "Fn::Sub": "arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/${glueDbName}-${datazoneEnvironmentEnvironmentId}"
                },
                {
                  "Fn::Sub": "arn:aws:glue:${AWS::Region}:${AWS::AccountId}:table/${glueDbName}-${datazoneEnvironmentEnvironmentId}/*"
                }
              ]
            }
          ]
        }
      }
    },
    "LakeFormationDbPermissions": {
      "Type": "AWS::LakeFormation::Permissions",
      "Properties": {
        "DataLakePrincipal": {
          "DataLakePrincipalIdentifier": {
            "Ref": "userRoleArn"
          }
        },
        "Resource": {
          "DatabaseResource": {
            "CatalogId": {
              "Ref": "AWS::AccountId"
            },
            "Name": {
              "Fn::Sub": "${glueDbName}-${datazoneEnvironmentEnvironmentId}"
            }
          }
        },
        "Permissions": [
          "DESCRIBE",
          "CREATE_TABLE"
        ]
      },
      "DependsOn": [
        "GlueDatabase"
      ]
    },
    "LakeFormationTablePermissions": {
      "Type": "AWS::LakeFormation::Permissions",
      "Properties": {
        "DataLakePrincipal": {
          "DataLakePrincipalIdentifier": {
            "Ref": "userRoleArn"
          }
        },
        "Resource": {
          "TableResource": {
            "CatalogId": {
              "Ref": "AWS::AccountId"
            },
            "DatabaseName": {
              "Fn::Sub": "${glueDbName}-${datazoneEnvironmentEnvironmentId}"
            },
            "TableWildcard": {}
          }
        },
        "Permissions": [
          "ALL"
        ]
      },
      "DependsOn": [
        "GlueDatabase"
      ]
    }
  },
  "Outputs": {
    "GlueDatabaseName": {
      "Value": {
        "Fn::Sub": "${glueDbName}-${datazoneEnvironmentEnvironmentId}"
      },
      "Export": {
        "Name": {
          "Fn::Sub": "${glueDbName}-${datazoneEnvironmentEnvironmentId}"
        }
      }
    },
    "GlueAccessManagedPolicy": {
      "Description": "ARN of the created managed policy",
      "Value": {
        "Ref": "GlueAccessManagedPolicy"
      },
      "Export": {
        "Name": {
          "Fn::Sub": "datazone-managed-policy-glue-${glueDbName}-${datazoneEnvironmentEnvironmentId}"
        }
      }
    }
  }
}
```