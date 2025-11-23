# IAM tutorial: Use an CloudFormation template to

create a SAML Identity Provider (IdP) and SAML federated IAM role

To get familiar with SAML federation and its capabilities, you'll use an CloudFormation template to
set up a SAML Identity Provider (IdP) and associated federated IAM role. This tutorial shows
you how to create both resources together in a single stack.

The template creates a SAML IdP that can be used for federated access to AWS resources,
along with an IAM role that trusts the SAML provider. Users authenticated by your external IdP
can assume this role to access AWS resources.

The deployed resources consist of the following:

- A SAML IdP configured with your IdP's metadata document.
- A federated IAM role that trusts the SAML IdP and can be assumed by authenticated
  users.
- Configurable managed policies that can be attached to the role to grant specific
  permissions.

## Prerequisites

This tutorial assumes that you have the following already in place:

- Python 3.6 or later installed on your local machine to run the Python command used in
  this tutorial for formatting your IdP's SAML metadata XML file.
- A SAML metadata document from your external IdP saved as an XML file.

## Create a SAML IdP and role using

CloudFormation

To create the SAML IdP and federated role, you'll create an CloudFormation template and use it
to create a stack containing both resources.

### Create the template

First, create the CloudFormation template.

1. In the [Template](#tutorial_saml-idp-and-federated-role-template "#tutorial_saml-idp-and-federated-role-template") section, click
   the copy icon on the **JSON** or **YAML** tab to copy
   the template contents.
2. Paste the template contents into a new file.
3. Save the file locally.

### Create the stack

Next, use the template you've saved to provision a CloudFormation stack.

1.  Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2.  On the **Stacks** page, from the **Create stack**
    menu, choose **with new resources (standard)**.
3.  Specify the template:
    1. Under **Prerequisite**, choose **Choose an existing
       template**.
    2. Under **Specify template**, choose **Upload a template
       file**.
    3. Choose **Choose file**, navigate to the template file, and
       choose it.
    4. Choose **Next**.

4.  Specify the following stack details:
    1. Enter a stack name.
    2. For **IdentityProviderName**, you can leave this empty to
       auto-generate a name based on the stack name, or enter a custom name for your SAML
       IdP.

    Example: `CompanyIdP` or `EnterpriseSSO` 3. For **IdentityProviderSAMLMetadataDocument**, you need to
    format your SAML metadata XML file as a single line before pasting it into this
    field. This is necessary because the CloudFormation console requires XML content to
    be formatted as a single line when passed through console parameters.

    Use the following Python command to reformat your XML file:

    ```
    python3 -c "import sys, re; content=open(sys.argv[1]).read(); print(re.sub(r'>\s+<', '><', content.replace('\n', '').replace('\r', '').strip()))" `saml-metadata.xml`
    ```

    ###### Note

    The IdP's SAML metadata document must be formatted as a single line for
    console parameter input. The Python command removes line breaks and extra
    whitespace to create the required format while maintaining all original content
    and structure.

    Copy the output from the Python command and paste it into the
    **IdentityProviderSAMLMetadataDocument** field.

    Example of formatted SAML metadata document (abbreviated):

    ```
    <?xml version="1.0" encoding="UTF-8"?><md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://portal.sso.example.com/saml/assertion/CompanyIdP"><md:IDPSSODescriptor WantAuthnRequestsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"><md:KeyDescriptor use="signing"><ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIDXTCCAkWgAwIBAgIJAJC1HiIAZAiIMA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV...</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://portal.sso.example.com/saml/logout/CompanyIdP"/><md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</md:NameIDFormat><md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://portal.sso.example.com/saml/assertion/CompanyIdP"/></md:IDPSSODescriptor></md:EntityDescriptor>
    ```

    4. For **RoleName**, you can leave this empty to auto-generate a
       name based on the stack name, or enter a custom name for the federated IAM
       role.

    Example: `SAML-Developer-Access` or
    `SAML-ReadOnly-Role` 5. For other parameters, accept the default values or enter your own based on your
    requirements:

        * **IdentityProviderAddPrivateKey** - Optional private key
         for decrypting SAML assertions
        * **IdentityProviderAssertionEncryptionMode** - Encryption
         mode for SAML assertions


        Example values: `Allowed`, `Required`, or leave empty
         for no encryption
        * **RoleSessionDuration** - Maximum session duration in
         seconds (3600-43200, default 7200)


        Example: `14400` (4 hours)
        * **RolePermissionsBoundary** - Optional ARN of a permissions
         boundary policy


        Example:
         `arn:aws:iam::123456789012:policy/DeveloperBoundary`
        * **RolePath** - Path for the IAM role (default is /)


        Example: `/saml-roles/`
        * **RoleManagedPolicy1-5** - Optional ARNs of up to 5 managed
         policies to attach


        Example for RoleManagedPolicy1:
         `arn:aws:iam::aws:policy/ReadOnlyAccess`


        Example for RoleManagedPolicy2:
         `arn:aws:iam::123456789012:policy/CustomPolicy`

    6. Choose **Next**.

5.  Configure the stack options:
    1. Under **Stack failure options**, choose **Delete all
       newly created resources**.

    ###### Note

    Choosing this option prevents you from possibly being billed for resources
    whose deletion policy specifies they be retained even if the stack creation
    fails. 2. Accept all other default values. 3. Under **Capabilities**, check the box to acknowledge that
    CloudFormation might create IAM resources in your account. 4. Choose **Next**.

6.  Review the stack details and choose **Submit**.

CloudFormation creates the stack. Once the stack creation is complete, the stack resources are
ready to use. You can use the **Resources** tab on the stack detail page to
view the resources that were provisioned in your account.

The stack will output the following values, which you can view on the
**Outputs** tab:

- **RoleARN**: The ARN of the created IAM role (for example,
  `arn:aws:iam::123456789012:role/SAML-Developer-Access` or
  `arn:aws:iam::123456789012:role/stack-name-a1b2c3d4` if using
  auto-generated name).
- **IdentityProviderARN**: The ARN of the created SAML IdP (for
  example, `arn:aws:iam::123456789012:saml-provider/CompanyIdP`).

You'll need both of these ARNs when configuring your IdP to send the appropriate SAML
attributes for role assumption.

## Test the SAML federation

Once the SAML IdP and federated role have been created, you can test the federation
setup.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers**.

You should see your newly created SAML IdP in the list. 3. Choose the IdP name to view its details.

On the IdP detail page, you can see the SAML metadata document and other configuration
details. 4. In the navigation pane, choose **Roles**. 5. Find and choose your newly created federated role.

On the role detail page, you can see the trust policy that allows the SAML IdP to
assume this role. 6. Choose the **Trust relationships** tab to review the trust
policy.

The trust policy should show that the SAML IdP is trusted to assume this role with the
condition that the SAML audience (`SAML:aud`) matches
`https://signin.aws.amazon.com/saml`.

## Clean up: delete

resources

As a final step, you'll delete the stack and the resources it contains.

1. Open the CloudFormation console.
2. On the **Stacks** page, choose the stack created from the template,
   and choose **Delete**, then confirm **Delete**.

CloudFormation initiates deletion of the stack and all resources it includes.

## CloudFormation template

details

### Resources

The CloudFormation template for this tutorial will create the following resources in your
account:

- [`AWS::IAM::SAMLProvider`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.md"): A SAML IdP that establishes trust
  between AWS and your external IdP.
- [`AWS::IAM::Role`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md"): A federated IAM role that can be assumed by
  users authenticated through the SAML IdP.

### Configuration

The template includes the following configurable parameters:

- **IdentityProviderName** - Name of the SAML IdP (leave empty for
  auto-generated name)
- **IdentityProviderSAMLMetadataDocument** - SAML metadata document
  from your IdP (required)
- **IdentityProviderAddPrivateKey** - Optional private key for
  decrypting SAML assertions
- **IdentityProviderAssertionEncryptionMode** - Encryption mode for
  SAML assertions
- **RoleName** - Name of the IAM Role (leave empty for auto-generated
  name)
- **RolePath** - Path for the IAM role (default /)
- **RolePermissionsBoundary** - Optional ARN of permissions boundary
  policy
- **RoleSessionDuration** - Maximum session duration in seconds
  (3600-43200, default 7200)
- **RoleManagedPolicy1-5** - Optional ARNs of up to 5 managed
  policies to attach

## CloudFormation template

Save the following JSON or YAML code as a separate file to use as the CloudFormation template
for this tutorial.

JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "[AWSDocs] IAM: tutorial_saml-idp-and-federated-role",
  "Parameters": {
    "IdentityProviderName": {
      "Type": "String",
      "Description": "Name of the SAML Identity Provider (leave empty for auto-generated name like '{StackName}-{UniqueId}')",
      "Default": "",
      "AllowedPattern": "^$|^[a-zA-Z0-9._-]+$",
      "ConstraintDescription": "Must be empty or contain only alphanumeric characters, periods, underscores, and hyphens"
    },
    "IdentityProviderSAMLMetadataDocument": {
      "Type": "String",
      "Description": "SAML metadata document from identity provider"
    },
    "IdentityProviderAddPrivateKey": {
      "Type": "String",
      "Description": "Optional private key for decrypting SAML assertions. The private key must be a .pem file that uses AES-GCM or AES-CBC encryption algorithm to decrypt SAML assertions.",
      "Default": ""
    },
    "IdentityProviderAssertionEncryptionMode": {
      "Type": "String",
      "Description": "Optional, sets encryption mode for SAML assertions",
      "Default": "",
      "AllowedValues": ["", "Allowed", "Required"]
    },
    "RoleName": {
      "Type": "String",
      "Description": "Name of the IAM Role (leave empty for auto-generated name like '{StackName}-{UniqueId}')",
      "Default": "",
      "AllowedPattern": "^$|^[\\w+=,.@-]{1,64}$",
      "ConstraintDescription": "Must be empty or 1-64 characters and can contain alphanumeric characters and +=,.@-"
    },
    "RolePath": {
      "Type": "String",
      "Description": "Path for the IAM Role",
      "AllowedPattern": "(^\\/$)|(^\\/.*\\/$)",
      "Default": "/"
    },
    "RolePermissionsBoundary": {
      "Type": "String",
      "Description": "Optional ARN of the permissions boundary policy (leave empty for none)",
      "Default": ""
    },
    "RoleSessionDuration": {
      "Description": "The maximum session duration (in seconds) that you want to set for the specified role (3600-43200)",
      "Type": "Number",
      "MinValue": 3600,
      "MaxValue": 43200,
      "Default": 7200
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
    "HasCustomProviderName": {"Fn::Not": [{"Fn::Equals": [{"Ref": "IdentityProviderName"}, ""]}]},
    "HasCustomRoleName": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleName"}, ""]}]},
    "HasPermissionsBoundary": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RolePermissionsBoundary"}, ""]}]},
    "HasPolicy1": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy1"}, ""]}]},
    "HasPolicy2": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy2"}, ""]}]},
    "HasPolicy3": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy3"}, ""]}]},
    "HasPolicy4": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy4"}, ""]}]},
    "HasPolicy5": {"Fn::Not": [{"Fn::Equals": [{"Ref": "RoleManagedPolicy5"}, ""]}]},
    "HasPrivateKey": {"Fn::Not": [{"Fn::Equals": [{"Ref": "IdentityProviderAddPrivateKey"}, ""]}]},
    "HasAssertionEncryptionMode": {"Fn::Not": [{"Fn::Equals": [{"Ref": "IdentityProviderAssertionEncryptionMode"}, ""]}]}
  },
  "Resources": {
    "SAMLProvider": {
      "Type": "AWS::IAM::SAMLProvider",
      "Properties": {
        "Name": {"Fn::If": ["HasCustomProviderName", {"Ref": "IdentityProviderName"}, {"Ref": "AWS::NoValue"}]},
        "SamlMetadataDocument": {"Ref": "IdentityProviderSAMLMetadataDocument"},
        "AddPrivateKey": {"Fn::If": ["HasPrivateKey", {"Ref": "IdentityProviderAddPrivateKey"}, {"Ref": "AWS::NoValue"}]},
        "AssertionEncryptionMode": {"Fn::If": ["HasAssertionEncryptionMode", {"Ref": "IdentityProviderAssertionEncryptionMode"}, {"Ref": "AWS::NoValue"}]}
      }
    },
    "SAMLFederatedRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "RoleName": {"Fn::If": ["HasCustomRoleName", {"Ref": "RoleName"}, {"Ref": "AWS::NoValue"}]},
        "Path": {"Ref": "RolePath"},
        "Description": "SAML federated IAM role for SSO access with specified permissions",
        "MaxSessionDuration": {"Ref": "RoleSessionDuration"},
        "PermissionsBoundary": {"Fn::If": ["HasPermissionsBoundary", {"Ref": "RolePermissionsBoundary"}, {"Ref": "AWS::NoValue"}]},
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Federated": {"Ref": "SAMLProvider"}
              },
              "Action": [
                "sts:AssumeRole",
                "sts:SetSourceIdentity",
                "sts:TagSession"
              ],
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
    },
    "IdentityProviderARN": {
      "Description": "ARN of the created SAML Identity Provider",
      "Value": {"Ref": "SAMLProvider"},
      "Export": {
        "Name": {"Fn::Sub": "${AWS::StackName}-IdentityProviderARN"}
      }
    }
  }
}
```

YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: '[AWSDocs] IAM: tutorial_saml-idp-and-federated-role'

Parameters:
  IdentityProviderName:
    Type: String
    Description: Name of the SAML Identity Provider (leave empty for auto-generated name like '{StackName}-{UniqueId}')
    Default: ""
    AllowedPattern: '^$|^[a-zA-Z0-9._-]+$'
    ConstraintDescription: Must be empty or contain only alphanumeric characters, periods, underscores, and hyphens

  IdentityProviderSAMLMetadataDocument:
    Type: String
    Description: SAML metadata document from identity provider

  IdentityProviderAddPrivateKey:
    Type: String
    Description: Optional private key for decrypting SAML assertions. The private key must be a .pem file that uses AES-GCM or AES-CBC encryption algorithm to decrypt SAML assertions.
    Default: ""

  IdentityProviderAssertionEncryptionMode:
    Type: String
    Description: Optional, sets encryption mode for SAML assertions
    Default: ""
    AllowedValues:
      - ""
      - "Allowed"
      - "Required"

  RoleName:
    Type: String
    Description: Name of the IAM Role (leave empty for auto-generated name like '{StackName}-{UniqueId}')
    Default: ""
    AllowedPattern: '^$|^[\w+=,.@-]{1,64}$'
    ConstraintDescription: "Must be empty or 1-64 characters and can contain alphanumeric characters and +=,.@-"

  RolePath:
    Type: String
    Description: Path for the IAM Role
    AllowedPattern: (^\/$)|(^\/.*\/$)
    Default: "/"

  RolePermissionsBoundary:
    Type: String
    Description: Optional ARN of the permissions boundary policy (leave empty for none)
    Default: ""

  RoleSessionDuration:
    Description: The maximum session duration (in seconds) that you want to set for the specified role (3600-43200)
    Type: Number
    MinValue: 3600
    MaxValue: 43200
    Default: 7200

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
  HasCustomProviderName: !Not [!Equals [!Ref IdentityProviderName, ""]]
  HasCustomRoleName: !Not [!Equals [!Ref RoleName, ""]]
  HasPermissionsBoundary: !Not [!Equals [!Ref RolePermissionsBoundary, ""]]
  HasPolicy1: !Not [!Equals [!Ref RoleManagedPolicy1, ""]]
  HasPolicy2: !Not [!Equals [!Ref RoleManagedPolicy2, ""]]
  HasPolicy3: !Not [!Equals [!Ref RoleManagedPolicy3, ""]]
  HasPolicy4: !Not [!Equals [!Ref RoleManagedPolicy4, ""]]
  HasPolicy5: !Not [!Equals [!Ref RoleManagedPolicy5, ""]]
  HasPrivateKey: !Not [!Equals [!Ref IdentityProviderAddPrivateKey, ""]]
  HasAssertionEncryptionMode: !Not [!Equals [!Ref IdentityProviderAssertionEncryptionMode, ""]]

Resources:
  SAMLProvider:
    Type: AWS::IAM::SAMLProvider
    Properties:
      Name: !If
        - HasCustomProviderName
        - !Ref IdentityProviderName
        - !Ref AWS::NoValue
      SamlMetadataDocument: !Ref IdentityProviderSAMLMetadataDocument
      AddPrivateKey: !If
        - HasPrivateKey
        - !Ref IdentityProviderAddPrivateKey
        - !Ref AWS::NoValue
      AssertionEncryptionMode: !If
        - HasAssertionEncryptionMode
        - !Ref IdentityProviderAssertionEncryptionMode
        - !Ref AWS::NoValue

  SAMLFederatedRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !If
        - HasCustomRoleName
        - !Ref RoleName
        - !Ref AWS::NoValue
      Path: !Ref RolePath
      Description: "SAML federated IAM role for SSO access with specified permissions"
      MaxSessionDuration: !Ref RoleSessionDuration
      PermissionsBoundary: !If
        - HasPermissionsBoundary
        - !Ref RolePermissionsBoundary
        - !Ref AWS::NoValue
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Effect: Allow
            Principal:
              Federated: !Ref SAMLProvider
            Action:
              - 'sts:AssumeRole'
              - 'sts:SetSourceIdentity'
              - 'sts:TagSession'
            Condition:
              StringEquals:
                'SAML:aud': 'https://signin.aws.amazon.com/saml'
      ManagedPolicyArns: !Split
        - ','
        - !Join
          - ','
          - - !If [HasPolicy1, !Ref RoleManagedPolicy1, !Ref "AWS::NoValue"]
            - !If [HasPolicy2, !Ref RoleManagedPolicy2, !Ref "AWS::NoValue"]
            - !If [HasPolicy3, !Ref RoleManagedPolicy3, !Ref "AWS::NoValue"]
            - !If [HasPolicy4, !Ref RoleManagedPolicy4, !Ref "AWS::NoValue"]
            - !If [HasPolicy5, !Ref RoleManagedPolicy5, !Ref "AWS::NoValue"]

Outputs:
  RoleARN:
    Description: ARN of the created IAM Role
    Value: !GetAtt SAMLFederatedRole.Arn
    Export:
      Name: !Sub '${AWS::StackName}-RoleARN'

  IdentityProviderARN:
    Description: ARN of the created SAML Identity Provider
    Value: !Ref SAMLProvider
    Export:
      Name: !Sub '${AWS::StackName}-IdentityProviderARN'
```
