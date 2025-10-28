# IAM tutorial: Use an AWS CloudFormation template to

create a SAML federated IAM role

When you have an existing SAML Identity Provider (IdP) configured in your AWS account,
you can create federated IAM roles that trust that IdP. This tutorial shows you how to use
an AWS CloudFormation template to create a SAML federated IAM role that can be assumed by users
authenticated through your external IdP.

The template creates a federated IAM role with a trust policy that allows your SAML IdP
to assume the role. Users authenticated by your external IdP can assume this role to access
AWS resources based on the permissions attached to the role.

The deployed resource consists of the following:

- A federated IAM role that trusts your existing SAML IdP.
- Configurable managed policies that can be attached to the role to grant specific
  permissions.
- Optional permissions boundary and session duration settings.

## Prerequisites

This tutorial assumes that you have the following already in place:

- An existing SAML IdP configured in your AWS account. If you don't have one,
  you can create it using the [IAM tutorial: Use an AWS CloudFormation template to create a SAML
  Identity Provider (IdP)](tutorial_saml-idp.md "tutorial_saml-idp.md") tutorial.
- The ARN of your SAML IdP, which you'll need to specify as a parameter when
  creating the stack.
- Python 3.6 or later installed on your local machine to run the Python command
  used in this tutorial for formatting your IdP's SAML metadata XML file.

## Create a SAML federated role using

AWS CloudFormation

To create the SAML federated role, you'll create an CloudFormation template and use it to
create a stack containing the role.

### Create the template

First, create the CloudFormation template.

1. In the [Template](#tutorial_saml-federated-role-template "#tutorial_saml-federated-role-template") section,
   click the copy icon on the **JSON** or
   **YAML** tab to copy the template contents.
2. Paste the template contents into a new file.
3. Save the file locally.

### Create the stack

Next, use the template you've saved to provision a CloudFormation stack.

1.  Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2.  On the **Stacks** page, from the **Create
    stack** menu, choose **with new resources
    (standard)**.
3.  Specify the template:
    1. Under **Prerequisite**, choose **Choose
       an existing template**.
    2. Under **Specify template**, choose
       **Upload a template file**.
    3. Choose **Choose file**, navigate to the template
       file, and choose it.
    4. Choose **Next**.

4.  Specify the following stack details:
    1. Enter a stack name.
    2. For **SAMLProviderARN**, enter the ARN of your
       existing SAML IdP. This should be in the format
       `arn:aws:iam::123456789012:saml-provider/YourProviderName`.

    Example:
    `arn:aws:iam::123456789012:saml-provider/CompanyIdP`

    ###### Note

    If you created your SAML IdP using the [IAM tutorial: Use an AWS CloudFormation template to create a SAML
    Identity Provider (IdP)](tutorial_saml-idp.md "tutorial_saml-idp.md") tutorial, you can find
    the provider ARN in the Outputs tab of that CloudFormation
    stack. 3. For **RoleName**, you can leave this empty to
    auto-generate a name based on the stack name, or enter a custom name
    for the IAM role.

    Example: `SAML-Developer-Access` or
    `SAML-ReadOnly-Role` 4. For other parameters, accept the default values or enter your own
    based on your requirements:

        * **RoleSessionDuration** - Maximum session
         duration in seconds (3600-43200, default 7200)


        Example: `14400` (4 hours)
        * **RolePermissionsBoundary** - Optional
         ARN of a permissions boundary policy


        Example:
         `arn:aws:iam::123456789012:policy/DeveloperBoundary`
        * **RolePath** - Path for the IAM role
         (default is /)


        Example: `/saml-roles/`
        * **ManagedPolicy1-5** - Optional ARNs of
         up to 5 managed policies to attach


        Example for ManagedPolicy1:
         `arn:aws:iam::aws:policy/ReadOnlyAccess`


        Example for ManagedPolicy2:
         `arn:aws:iam::123456789012:policy/CustomPolicy`

    5. Choose **Next**.

5.  Configure the stack options:
    1. Under **Stack failure options**, choose
       **Delete all newly created resources**.

    ###### Note

    Choosing this option prevents you from possibly being billed
    for resources whose deletion policy specifies they be retained
    even if the stack creation fails. 2. Accept all other default values. 3. Under **Capabilities**, check the box to
    acknowledge that CloudFormation might create IAM resources in your
    account. 4. Choose **Next**.

6.  Review the stack details and choose **Submit**.

AWS CloudFormation creates the stack. Once the stack creation is complete, the stack resources
are ready to use. You can use the **Resources** tab on the stack
detail page to view the resources that were provisioned in your account.

The stack will output the following value, which you can view on the
**Outputs** tab:

- **RoleARN**: The ARN of the created IAM role (for
  example, `arn:aws:iam::123456789012:role/SAML-Developer-Access`
  or `arn:aws:iam::123456789012:role/stack-name-a1b2c3d4` if using
  auto-generated name).

You'll need this role ARN when configuring your IdP to send the appropriate SAML
attributes for role assumption.

## Test the SAML federated

role

Once the SAML federated role has been created, you can verify its configuration and
test the federation setup.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Find and choose your newly created federated role.

If you provided a custom role name, look for that name. If you left the
RoleName parameter empty, the role will have an auto-generated name based on the
stack name and a unique identifier. 4. Choose the **Trust relationships** tab to review the trust
policy.

The trust policy should show that your SAML IdP is trusted to assume this role
with the condition that the SAML audience (`SAML:aud`) matches
`https://signin.aws.amazon.com/saml`. 5. Choose the **Permissions** tab to review the attached
policies.

You can see any managed policies that were attached to the role during
creation. 6. Note the **Role ARN** displayed on the role summary
page.

You will need this ARN to configure your external IdP to allow users to assume
this role.

Your SAML federated role is now ready to be used. Configure your external IdP to
include this role's ARN in SAML assertions, and authenticated users will be able to
assume this role to access AWS resources.

## Clean up: delete resources

As a final step, you'll delete the stack and the resources it contains.

1. Open the AWS CloudFormation console.
2. On the **Stacks** page, choose the stack created from the
   template, and choose **Delete**, then confirm
   **Delete**.

CloudFormation initiates deletion of the stack and all resources it
includes.

## CloudFormation template

details

### Resources

The AWS CloudFormation template for this tutorial will create the following resource in your
account:

- [`AWS::IAM::Role`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md"): A federated IAM role that
  can be assumed by users authenticated through your SAML IdP.

### Configuration

The template includes the following configurable parameters:

- **RoleName** - Name of the IAM Role (leave empty for
  auto-generated name)
- **SAMLProviderARN** - ARN of the SAML IdP
  (required)
- **RoleSessionDuration** - Maximum session duration in
  seconds (3600-43200, default 7200)
- **RolePermissionsBoundary** - Optional ARN of permissions
  boundary policy
- **RolePath** - Path for the IAM role (default /)
- **ManagedPolicy1-5** - Optional ARNs of up to 5 managed
  policies to attach

## CloudFormation template

Save the following JSON or YAML code as a separate file to use as the CloudFormation
template for this tutorial.

JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "[AWSDocs] IAM: tutorial_saml-federated-role",
  "Parameters": {
    "RoleName": {
      "Type": "String",
      "Description": "Name of the IAM Role (leave empty for auto-generated name like '{StackName}-{UniqueId}')",
      "Default": "",
      "AllowedPattern": "^$|^[\\w+=,.@-]{1,64}$",
      "ConstraintDescription": "Must be empty or 1-64 characters and can contain alphanumeric characters and +=,.@-"
    },
    "SAMLProviderARN": {
      "Type": "String",
      "Description": "ARN of the SAML Identity Provider",
      "AllowedPattern": "^arn:aws:iam::\\d{12}:saml-provider/[a-zA-Z0-9._-]+$",
      "ConstraintDescription": "Must be a valid SAML provider ARN"
    },
    "RoleSessionDuration": {
      "Type": "Number",
      "Description": "The maximum session duration (in seconds) that you want to set for the specified role (3600-43200)",
      "MinValue": 3600,
      "MaxValue": 43200,
      "Default": 7200
    },
    "RolePermissionsBoundary": {
      "Type": "String",
      "Description": "Optional ARN of the permissions boundary policy (leave empty for none)",
      "Default": ""
    },
    "RolePath": {
      "Type": "String",
      "Description": "Path for the IAM role (must start and end with /)",
      "Default": "/",
      "AllowedPattern": "^\/.*\/$|^\/$",
      "ConstraintDescription": "Role path must start and end with forward slash (/)"
    },
    "RoleManagedPolicy1": {
      "Type": "String",
      "Description": "Optional managed policy ARN 1",
      "Default": ""
    },
    "RoleManagedPolicy2": {
      "Type": "String",
      "Description": "Optional managed policy ARN 2",
      "Default": ""
    },
    "RoleManagedPolicy3": {
      "Type": "String",
      "Description": "Optional managed policy ARN 3",
      "Default": ""
    },
    "RoleManagedPolicy4": {
      "Type": "String",
      "Description": "Optional managed policy ARN 4",
      "Default": ""
    },
    "RoleManagedPolicy5": {
      "Type": "String",
      "Description": "Optional managed policy ARN 5",
      "Default": ""
    }
  },
  "Conditions": {
    "HasCustomRoleName": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleName"}, ""]}]},
    "HasPermissionsBoundary": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RolePermissionsBoundary"}, ""]}]},
    "HasPolicy1": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy1"}, ""]}]},
    "HasPolicy2": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy2"}, ""]}]},
    "HasPolicy3": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy3"}, ""]}]},
    "HasPolicy4": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy4"}, ""]}]},
    "HasPolicy5": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy5"}, ""]}]}
  },
  "Resources": {
    "SAMLFederatedRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "RoleName": {"Fn::If": ["HasCustomRoleName", {"Ref": "RoleName"}, {"Ref": "AWS::NoValue"}]},
        "Description": "IAM role with SAML provider trust",
        "MaxSessionDuration": {"Ref": "RoleSessionDuration"},
        "PermissionsBoundary": {"Fn::If": ["HasPermissionsBoundary", {"Ref": "RolePermissionsBoundary"}, {"Ref": "AWS::NoValue"}]},
        "Path": {"Ref": "RolePath"},
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Federated": {"Ref": "SAMLProviderARN"}
              },
              "Action": "sts:AssumeRoleWithSAML",
              "Condition": {
                "StringEquals": {
                  "SAML:aud": "https://signin.aws.amazon.com/saml"
                }
              }
            }
          ]
        },
        "ManagedPolicyArns": {
          "Fn::Split": [
            ",",
            {
              "Fn::Join": [
                ",",
                [
                  {"Fn::If": ["HasPolicy1", {"Ref": "RoleManagedPolicy1"}, {"Ref": "AWS::NoValue"}]},
                  {"Fn::If": ["HasPolicy2", {"Ref": "RoleManagedPolicy2"}, {"Ref": "AWS::NoValue"}]},
                  {"Fn::If": ["HasPolicy3", {"Ref": "RoleManagedPolicy3"}, {"Ref": "AWS::NoValue"}]},
                  {"Fn::If": ["HasPolicy4", {"Ref": "RoleManagedPolicy4"}, {"Ref": "AWS::NoValue"}]},
                  {"Fn::If": ["HasPolicy5", {"Ref": "RoleManagedPolicy5"}, {"Ref": "AWS::NoValue"}]}
                ]
              ]
            }
          ]
        }
      }
    }
  },
  "Outputs": {
    "RoleARN": {
      "Description": "ARN of the created IAM Role",
      "Value": {"Fn::GetAtt": ["SAMLFederatedRole", "Arn"]},
      "Export": {
        "Name": {"Fn::Sub": "${AWS::StackName}-RoleARN"}
      }
    }
  }
}
```

YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: '[AWSDocs] IAM: tutorial_saml-federated-role'

Parameters:
  RoleName:
    Type: String
    Description: 'Name of the IAM Role (leave empty for auto-generated name like ''{StackName}-{UniqueId}'')'
    Default: ""
    AllowedPattern: '^$|^[\w+=,.@-]{1,64}$'
    ConstraintDescription: 'Must be empty or 1-64 characters and can contain alphanumeric characters and +=,.@-'

  SAMLProviderARN:
    Type: String
    Description: 'ARN of the SAML Identity Provider'
    AllowedPattern: '^arn:aws:iam::\d{12}:saml-provider/[a-zA-Z0-9._-]+$'
    ConstraintDescription: 'Must be a valid SAML provider ARN'

  RoleSessionDuration:
    Type: Number
    Description: 'The maximum session duration (in seconds) that you want to set for the specified role (3600-43200)'
    MinValue: 3600
    MaxValue: 43200
    Default: 7200

  RolePermissionsBoundary:
    Type: String
    Description: Optional ARN of the permissions boundary policy (leave empty for none)
    Default: ""

  RolePath:
    Type: String
    Description: 'Path for the IAM role (must start and end with /)'
    Default: "/"
    AllowedPattern: '^\/.*\/$|^\/$'
    ConstraintDescription: 'Role path must start and end with forward slash (/)'

  RoleManagedPolicy1:
    Type: String
    Description: Optional managed policy ARN 1
    Default: ""
  RoleManagedPolicy2:
    Type: String
    Description: Optional managed policy ARN 2
    Default: ""
  RoleManagedPolicy3:
    Type: String
    Description: Optional managed policy ARN 3
    Default: ""
  RoleManagedPolicy4:
    Type: String
    Description: Optional managed policy ARN 4
    Default: ""
  RoleManagedPolicy5:
    Type: String
    Description: Optional managed policy ARN 5
    Default: ""

Conditions:
  HasCustomRoleName: !Not [!Equals [!Ref RoleName, ""]]
  HasPermissionsBoundary: !Not [!Equals [!Ref RolePermissionsBoundary, ""]]
  HasPolicy1: !Not [!Equals [!Ref RoleManagedPolicy1, ""]]
  HasPolicy2: !Not [!Equals [!Ref RoleManagedPolicy2, ""]]
  HasPolicy3: !Not [!Equals [!Ref RoleManagedPolicy3, ""]]
  HasPolicy4: !Not [!Equals [!Ref RoleManagedPolicy4, ""]]
  HasPolicy5: !Not [!Equals [!Ref RoleManagedPolicy5, ""]]

Resources:
  SAMLFederatedRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: !If
        - HasCustomRoleName
        - !Ref RoleName
        - !Ref AWS::NoValue
      Description: 'IAM role with SAML provider trust'
      MaxSessionDuration: !Ref RoleSessionDuration
      PermissionsBoundary: !If
        - HasPermissionsBoundary
        - !Ref RolePermissionsBoundary
        - !Ref AWS::NoValue
      Path: !Ref RolePath
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Effect: Allow
            Principal:
              Federated: !Ref SAMLProviderARN
            Action: 'sts:AssumeRoleWithSAML'
            Condition:
              StringEquals:
                'SAML:aud': 'https://signin.aws.amazon.com/saml'
      ManagedPolicyArns:
        !Split
          - ','
          - !Join
            - ','
            - - !If [HasPolicy1, !Ref RoleManagedPolicy1, !Ref 'AWS::NoValue']
              - !If [HasPolicy2, !Ref RoleManagedPolicy2, !Ref 'AWS::NoValue']
              - !If [HasPolicy3, !Ref RoleManagedPolicy3, !Ref 'AWS::NoValue']
              - !If [HasPolicy4, !Ref RoleManagedPolicy4, !Ref 'AWS::NoValue']
              - !If [HasPolicy5, !Ref RoleManagedPolicy5, !Ref 'AWS::NoValue']

Outputs:
  RoleARN:
    Description: 'ARN of the created IAM Role'
    Value: !GetAtt SAMLFederatedRole.Arn
    Export:
      Name: !Sub '${AWS::StackName}-RoleARN'
```
