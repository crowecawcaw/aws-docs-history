# Moving to

production with AWS CloudFormation

API-linked policy stores are a way to quickly build an authorization model for an API Gateway API.
They are designed to serve as a testing environment for the authorization component of
your application. After you create your test policy store, spend time refining the policies,
schema, and Lambda authorizer.

You might adjust the architecture of your API, requiring equivalent adjustments to
your policy store schema and policies. API-linked policy stores don't automatically update their schema
from API architecture–Verified Permissions only polls the API at the time you create a policy store. If
your API changes sufficiently, you might have to repeat the process with a new
policy store.

When your application and authorization model are ready for deployment to production,
integrate the API-linked policy store that you developed with your automation processes. As a
best practice, we recommend that you export the policy store schema and policies into a
AWS CloudFormation template that you can deploy to other AWS accounts and AWS Regions.

The results of the API-linked policy store process are an initial policy store and a Lambda authorizer.
The Lambda authorizer has several dependent resources. Verified Permissions deploys these resources in
an automatically-generated CloudFormation stack. To deploy to production, you must collect
the policy store and the Lambda authorizer resources into a template. An API-linked policy store
is made of the following resources:

1. [AWS::VerifiedPermissions::PolicyStore](../../../AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.md"): Copy
   your schema to the `SchemaDefinition` object. Escape `"`
   characters as `\"`.
2. [AWS::VerifiedPermissions::IdentitySource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.md"): Copy
   values from the output of [GetIdentitySource](../apireference/API_GetIdentitySource.md "../apireference/API_GetIdentitySource.md") from your test policy store
   and modify as needed.
3. One or more of [AWS::VerifiedPermissions::Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.md"): Copy your
   policy statement to the `Definition` object. Escape `"`
   characters as `\"`.
4. [AWS::Lambda::Function](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md"), [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md"), [AWS::IAM::Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), [AWS::ApiGateway::Authorizer](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.md"), [AWS::Lambda::Permission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md")
   The following template is an example policy store. You can append the Lambda authorizer
   resources from your existing stack to this template.

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MyExamplePolicyStore": {
            "Type": "AWS::VerifiedPermissions::PolicyStore",
            "Properties": {
                "ValidationSettings": {
                    "Mode": "STRICT"
                },
                "Description": "ApiGateway: PetStore/test",
                "Schema": {
                    "CedarJson": "{\"PetStore\":{\"actions\":{\"get /pets\":{\"appliesTo\":{\"principalTypes\":[\"User\"],\"resourceTypes\":[\"Application\"],\"context\":{\"type\":\"Record\",\"attributes\":{}}}},\"get /\":{\"appliesTo\":{\"principalTypes\":[\"User\"],\"resourceTypes\":[\"Application\"],\"context\":{\"type\":\"Record\",\"attributes\":{}}}},\"get /pets/{petId}\":{\"appliesTo\":{\"context\":{\"type\":\"Record\",\"attributes\":{}},\"resourceTypes\":[\"Application\"],\"principalTypes\":[\"User\"]}},\"post /pets\":{\"appliesTo\":{\"principalTypes\":[\"User\"],\"resourceTypes\":[\"Application\"],\"context\":{\"type\":\"Record\",\"attributes\":{}}}}},\"entityTypes\":{\"Application\":{\"shape\":{\"type\":\"Record\",\"attributes\":{}}},\"User\":{\"memberOfTypes\":[\"UserGroup\"],\"shape\":{\"attributes\":{},\"type\":\"Record\"}},\"UserGroup\":{\"shape\":{\"type\":\"Record\",\"attributes\":{}}}}}}"
                }
            }
        },
        "MyExamplePolicy": {
            "Type": "AWS::VerifiedPermissions::Policy",
            "Properties": {
                "Definition": {
                    "Static": {
                        "Description": "Policy defining permissions for testgroup cognito group",
                        "Statement": "permit(\nprincipal in PetStore::UserGroup::\"us-east-1_EXAMPLE|testgroup\",\naction in [\n  PetStore::Action::\"get /\",\n  PetStore::Action::\"post /pets\",\n  PetStore::Action::\"get /pets\",\n  PetStore::Action::\"get /pets/{petId}\"\n],\nresource);"
                    }
                },
                "PolicyStoreId": {
                    "Ref": "MyExamplePolicyStore"
                }
            },
            "DependsOn": [
                "MyExamplePolicyStore"
            ]
        },
        "MyExampleIdentitySource": {
            "Type": "AWS::VerifiedPermissions::IdentitySource",
            "Properties": {
                "Configuration": {
                    "CognitoUserPoolConfiguration": {
                        "ClientIds": [
                            "1example23456789"
                        ],
                        "GroupConfiguration": {
                            "GroupEntityType": "PetStore::UserGroup"
                        },
                        "UserPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_EXAMPLE"
                    }
                },
                "PolicyStoreId": {
                    "Ref": "MyExamplePolicyStore"
                },
                "PrincipalEntityType": "PetStore::User"
            },
            "DependsOn": [
                "MyExamplePolicyStore"
            ]
        }
    }
}
```
