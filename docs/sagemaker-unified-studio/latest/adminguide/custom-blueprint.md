# Custom blueprints

Custom blueprints in Amazon SageMaker Unified Studio enable organizations to standardize and accelerate how
data projects get set up. They are administrator-defined templates, powered by AWS
CloudFormation, that give teams a ready-made starting point for analytics and machine
learning environments.

In addition to the [built-in blueprints](supported-blueprints.md "supported-blueprints.md")
supported in Amazon SageMaker Unified Studio, you can also design your own. With custom blueprints,
organizations can include their specific dependencies, security controls, and best
practices to allow for new projects to align with internal standards. Since they're
defined through infrastructure-as-code, custom blueprints are easy to version control,
share across teams, and evolve over time. This not only speeds up onboarding but also
keeps projects consistent and governed, no matter how big or distributed your data
science organization becomes.

You can complete the following procedure to create custom blueprints in the Amazon
SageMaker management console:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Blueprints**
   tab.
4. In the **Blueprints** tab, in the
   **Blueprints** section, choose **Create**.
   This brings up the **Create custom blueprint** page.
5. In the **Create custom blueprint** page, specify the
   following and then choose **Next**:
   - **Name** - the name for your custom blueprint. This
     blueprint name cannot be changed after the blueprint is created.
   - **Description** - optional - the description for your
     custom blueprint.
   - In the **Upload CloudFormation template** section,
     specify the Amazon S3 file path where the custom AWS CloudFormation
     template for your blueprint is stored. You can choose to either specify
     the Amazon S3 URL for your template or you can choose to upload your own
     template file.

###### Note

You can choose the **View templates** button on the
**Blueprints** page to view the following sample
template that you can modify to fit your needs. This sample template creates
an AWS Glue database in your SageMaker Lakehouse environment. It also
configures the necessary LakeFormation permissions necessary for the newly
created project to be able to access the database. In addition, it also adds
a custom IAM policy to the project's role.

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

6. In the **Configure editable parameters** page, you can choose
   the parameters for your custom blueprint. Editable parameters are values that
   are visible and editable when this blueprint is used in project profiles. On
   this page, you can remove parameters that you don’t want to be editable in
   project profiles, or edit their default values. Then choose
   **Next**.
7. In the **Enable blueprint - optional** page, you can enable
   your custom blueprint so that it can be used in project profiles and
   projects.

If you choose to enable your custom bluerpint at this point, in the
**Provisioning role**, you must specify that role that
Amazon SageMaker Unified Studio can use to provision and manage resources defined in this blueprint in
your account.

Also, in the **Authorized domain units** section, you must
specify the domain units where projects can access resources defined by this
custom blueprint.

Then choose **Next**. 8. Review your selections in the **Review and create** page, and
then choose **Create blueprint**.
Now that your custom blueprint is created, you can use it when creating custom project
profiles. For more information, see [Custom project profile](custom.md "custom.md").
