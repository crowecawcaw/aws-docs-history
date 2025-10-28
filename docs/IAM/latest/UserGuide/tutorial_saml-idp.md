# IAM tutorial: Use an AWS CloudFormation template to create a SAML

Identity Provider (IdP)

To set up SAML federation for your AWS account, you need to create a SAML Identity
Provider (IdP). This tutorial shows you how to use an AWS CloudFormation template to create a SAML IdP
that establishes trust between AWS and your external IdP.

The template creates a SAML IdP configured with your IdP's metadata document. Federated
IAM roles can then reference this IdP to allow authenticated users from your external IdP
to access AWS resources.

The deployed resource consists of a SAML IdP configured with your IdP's metadata document
and optional encryption settings.

## Prerequisites

This tutorial assumes that you have the following already in place:

- Python 3.6 or later installed on your local machine to run the Python command
  used in this tutorial for formatting your IdP's SAML metadata XML file.
- A SAML metadata document from your external IdP saved as an XML file.

## Create a SAML IdP using AWS CloudFormation

To create the SAML IdP, you'll create an CloudFormation template and use it to create a
stack containing the IdP resource.

### Create the template

First, create the CloudFormation template.

1. In the [Template](#tutorial_saml-idp-template "#tutorial_saml-idp-template") section, click the
   copy icon on the **JSON** or **YAML** tab
   to copy the template contents.
2. Paste the template contents into a new file.
3. Save the file locally.

### Create the stack

Next, use the template you've saved to provision a CloudFormation stack.

1. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, from the **Create
   stack** menu, choose **with new resources
   (standard)**.
3. Specify the template:
   1. Under **Prerequisite**, choose **Choose
      an existing template**.
   2. Under **Specify template**, choose
      **Upload a template file**.
   3. Choose **Choose file**, navigate to the template
      file, and choose it.
   4. Choose **Next**.

4. Specify the following stack details:
   1. Enter a stack name.
   2. For **IdentityProviderName**, you can leave this
      empty to auto-generate a name based on the stack name, or enter a
      custom name for your SAML IdP. Custom names must contain only
      alphanumeric characters, periods, underscores, and hyphens.
   3. For **IdentityProviderSAMLMetadataDocument**, you
      need to format your SAML metadata XML file as a single line before
      pasting it into this field. This is necessary because the
      CloudFormation console requires XML content to be formatted as a
      single line when passed through console parameters.

   Use the following Python command to reformat your XML file:

   ```
   python3 -c "import sys, re; content=open(sys.argv[1]).read(); print(re.sub(r'>\s+<', '><', content.replace('\n', '').replace('\r', '').strip()))" `saml-metadata.xml`
   ```

   ###### Note

   The IdP's SAML metadata document must be formatted as a single
   line for console parameter input. The Python command removes
   line breaks and extra whitespace to create the required format
   while maintaining all original content and structure.

   Copy the output from the Python command and paste it into the
   **IdentityProviderSAMLMetadataDocument**
   field.

   Example of formatted SAML metadata document (abbreviated):

   ```
   <?xml version="1.0" encoding="UTF-8"?><md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://portal.sso.example.com/saml/assertion/CompanyIdP"><md:IDPSSODescriptor WantAuthnRequestsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"><md:KeyDescriptor use="signing"><ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIDXTCCAkWgAwIBAgIJAJC1HiIAZAiIMA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV...</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://portal.sso.example.com/saml/logout/CompanyIdP"/><md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</md:NameIDFormat><md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://portal.sso.example.com/saml/assertion/CompanyIdP"/></md:IDPSSODescriptor></md:EntityDescriptor>
   ```

   4. For other parameters, accept the default values or enter your own
      based on your requirements:
      - **IdentityProviderAddPrivateKey** -
        Optional private key for decrypting SAML assertions
      - **IdentityProviderAssertionEncryptionMode**
      * Optional, sets encryption mode for SAML assertions
        (Allowed, Required, or empty)

   5. Choose **Next**.

5. Configure the stack options:
   1. Under **Stack failure options**, choose
      **Delete all newly created resources**.

   ###### Note

   Choosing this option prevents you from possibly being billed
   for resources whose deletion policy specifies they be retained
   even if the stack creation fails. 2. Accept all other default values. 3. Under **Capabilities**, check the box to
   acknowledge that CloudFormation might create IAM resources in your
   account. 4. Choose **Next**.

6. Review the stack details and choose **Submit**.

AWS CloudFormation creates the stack. Once the stack creation is complete, the stack resources
are ready to use. You can use the **Resources** tab on the stack
detail page to view the resources that were provisioned in your account.

The stack will output the following values, which you can view on the
**Outputs** tab:

- **ProviderARN**: The ARN of the created SAML IdP (for
  example, `arn:aws:iam::123456789012:saml-provider/CompanyIdP`).
  You'll need this ARN when creating roles that trust this provider.
- **ProviderName**: The name of the created SAML IdP (for
  example, `CompanyIdP` if you specified a custom name, or
  `my-saml-stack-saml-provider` if you used the default
  naming).

These outputs are also exported, allowing them to be imported by other AWS CloudFormation
stacks using the `Fn::ImportValue` function.

## Verify the SAML IdP

Once the SAML IdP has been created, you can verify its configuration and note its ARN
for use with federated roles.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers**.

You should see your newly created SAML IdP in the list. 3. Choose the IdP name to view its details.

On the IdP detail page, you can see the SAML metadata document and other
configuration details. 4. Note the **Provider ARN** displayed on the details
page.

You will need this ARN when creating federated IAM roles that trust this
IdP. 5. Review the metadata document to ensure it matches what you provided from your
external IdP.

Your SAML IdP is now ready to be used by federated IAM roles. You can create roles
that trust this IdP to allow authenticated users from your external IdP to assume those
roles and access AWS resources.

## Clean up: delete resources

As a final step, you'll delete the stack and the resources it contains.

1. Open the AWS CloudFormation console.
2. On the **Stacks** page, choose the stack created from the
   template, and choose **Delete**, then confirm
   **Delete**.

CloudFormation initiates deletion of the stack and all resources it
includes.

## CloudFormation template details

### Resources

The AWS CloudFormation template for this tutorial will create the following resource in your
account:

[`AWS::IAM::SAMLProvider`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.md"): A SAML IdP that establishes
trust between AWS and your external IdP.

### Configuration

The template includes the following configurable parameters:

- **IdentityProviderName** - The name for your SAML IdP
  (leave empty for auto-generated name)

Example: `CompanyIdP` or `EnterpriseSSO`

- **IdentityProviderSAMLMetadataDocument** - The SAML
  metadata document from your external IdP (formatted as a single line)
- **IdentityProviderAddPrivateKey** - Optional private key
  for decrypting SAML assertions
- **IdentityProviderAssertionEncryptionMode** - Optional,
  sets encryption mode for SAML assertions

## CloudFormation template

Save the following JSON or YAML code as a separate file to use as the CloudFormation
template for this tutorial.

JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "[AWSDocs] IAM: tutorial_saml-idp",
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
    }
  },
  "Conditions": {
    "HasPrivateKey": {"Fn::Not": [{"Fn::Equals": [{"Ref": "IdentityProviderAddPrivateKey"}, ""]}]},
    "HasEncryptionMode": {"Fn::Not": [{"Fn::Equals": [{"Ref": "IdentityProviderAssertionEncryptionMode"}, ""]}]},
    "HasCustomName": {"Fn::Not": [{"Fn::Equals": [{"Ref": "IdentityProviderName"}, ""]}]}
  },
  "Resources": {
    "SAMLProvider": {
      "Type": "AWS::IAM::SAMLProvider",
      "Properties": {
        "Name": {"Fn::If": ["HasCustomName", {"Ref": "IdentityProviderName"}, {"Ref": "AWS::NoValue"}]},
        "SamlMetadataDocument": {"Ref": "IdentityProviderSAMLMetadataDocument"},
        "Tags": [
          {
            "Key": "Name",
            "Value": {"Fn::If": ["HasCustomName", {"Ref": "IdentityProviderName"}, {"Fn::Sub": "${AWS::StackName}-saml-provider"}]}
          }
        ],
        "AddPrivateKey": {"Fn::If": ["HasPrivateKey", {"Ref": "IdentityProviderAddPrivateKey"}, {"Ref": "AWS::NoValue"}]},
        "AssertionEncryptionMode": {"Fn::If": ["HasEncryptionMode", {"Ref": "IdentityProviderAssertionEncryptionMode"}, {"Ref": "AWS::NoValue"}]}
      }
    }
  },
  "Outputs": {
    "ProviderARN": {
      "Description": "ARN of the created SAML Identity Provider",
      "Value": {"Ref": "SAMLProvider"},
      "Export": {
        "Name": {"Fn::Sub": "${AWS::StackName}-ProviderARN"}
      }
    },
    "ProviderName": {
      "Description": "Name of the SAML Identity Provider",
      "Value": {"Fn::If": ["HasCustomName", {"Ref": "IdentityProviderName"}, {"Fn::Sub": "${AWS::StackName}-saml-provider"}]},
      "Export": {
        "Name": {"Fn::Sub": "${AWS::StackName}-ProviderName"}
      }
    }
  }
}
```

YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: '[AWSDocs] IAM: tutorial_saml-idp'

Parameters:
  IdentityProviderName:
    Type: String
    Description: Name of the SAML Identity Provider (leave empty for auto-generated name like '{StackName}-{UniqueId}')
    Default: ""
    AllowedPattern: '^$|^[a-zA-Z0-9._-]+$'
    ConstraintDescription: 'Must be empty or contain only alphanumeric characters, periods, underscores, and hyphens'

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

Conditions:
  HasPrivateKey: !Not [!Equals [!Ref IdentityProviderAddPrivateKey, ""]]
  HasEncryptionMode: !Not [!Equals [!Ref IdentityProviderAssertionEncryptionMode, ""]]
  HasCustomName: !Not [!Equals [!Ref IdentityProviderName, ""]]

Resources:
  SAMLProvider:
    Type: 'AWS::IAM::SAMLProvider'
    Properties:
      Name: !If
        - HasCustomName
        - !Ref IdentityProviderName
        - !Ref AWS::NoValue
      SamlMetadataDocument: !Ref IdentityProviderSAMLMetadataDocument
      Tags:
        - Key: Name
          Value: !If
            - HasCustomName
            - !Ref IdentityProviderName
            - !Sub '${AWS::StackName}-saml-provider'
      AddPrivateKey: !If
        - HasPrivateKey
        - !Ref IdentityProviderAddPrivateKey
        - !Ref AWS::NoValue
      AssertionEncryptionMode: !If
        - HasEncryptionMode
        - !Ref IdentityProviderAssertionEncryptionMode
        - !Ref AWS::NoValue

Outputs:
  ProviderARN:
    Description: 'ARN of the created SAML Identity Provider'
    Value: !Ref SAMLProvider
    Export:
      Name: !Sub '${AWS::StackName}-ProviderARN'

  ProviderName:
    Description: 'Name of the SAML Identity Provider'
    Value: !If
      - HasCustomName
      - !Ref IdentityProviderName
      - !Sub '${AWS::StackName}-saml-provider'
    Export:
      Name: !Sub '${AWS::StackName}-ProviderName'
```
