# Standard cards in Infrastructure Composer

All CloudFormation resources are available to use as **standard IaC resource cards** from the **Resources** palette.
After being dragged onto the visual canvas, a **standard IaC resource card** becomes a **standard component card**.
This simply means the card is one or more standard IaC resources. For further examples and details, see the topics in this section.

You can modify your infrastructure code through the **Template** view and through the **Resource properties** window. For example, the following is an example starting template of an
`Alexa::ASK::Skill` standard IaC resource:

```
Resources:
  Skill:
    Type: Alexa::ASK::Skill
    Properties:
      AuthenticationConfiguration:
        RefreshToken: `<String>`
        ClientSecret: `<String>`
        ClientId: `<String>`
      VendorId: `<String>`
      SkillPackage:
        S3Bucket: `<String>`
        S3Key: `<String>`
```

A standard IaC resource card starting template consists of the following:

- The CloudFormation resource type.
- Required or commonly used properties.
- The required type of the value to provide for each property.

###### Note

You can use Amazon Q to generate infrastructure code suggestions for standard resource cards. To learn more, see
[Using AWS Infrastructure Composer with Amazon Q Developer](using-composer-ide-cw.md "using-composer-ide-cw.md").

## Procedure

You can modify the infrastructure code for each resource in a standard component card through the **Resource properties** panel.

###### To modify a standard component card

1. Open the **Resource properties** panel of the standard IaC component card.
2. In the **Editing** field, select the standard IaC resource to edit from the dropdown list.
3. Modify your infrastructure code and **Save**.
