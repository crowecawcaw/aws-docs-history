

# Integrated AWS Config controls available in AWS Control Tower
<a name="config-controls"></a>

AWS Control Tower is integrated with AWS Config to provide over 500 selected additional detective controls that help you monitor and manage your AWS environment. These AWS Config controls are available in the AWS Control Tower console and the Control Catalog APIs. The **Control owner** or **Implementation** field for these controls is displayed as AWS Config or `AWS::Config::ConfigRule`.

You can use AWS Control Tower to search and discover the AWS Config rules that you need to govern your multi-account environment; and you can enable and manage these controls directly from the AWS Control Tower console. To search from the console, go to the Control Catalog and search for controls with the **Implementation** filter AWS Config. (Example: `Implementation = AWS Config`) 

The AWS Control Tower console and AWS Config console each display the same metadata for these controls.

You can enable and disable the AWS Config controls through the AWS Control Tower console or the [`EnableControl`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html) and [`DisableControl`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableControl.html) APIs. Control details are viewable programmatically by calling the Control Catalog [`GetControl`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html) and [`ListControls`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html) APIs.

**Differences**
+ In AWS Config, these integrated controls are listed by identifier.
+ In the AWS Control Tower console and APIs, the integrated controls are shown with names that summarize their function.

**Note**  
AWS Control Tower documentation does not provide a comprehensive list of integrated AWS Config controls. For more information about these controls, see [List of AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) in the *AWS Config Developer Guide*, or view them in the AWS Control Tower console.

**Important**  
AWS Control Tower doesn't support parameter configuration for detective controls. If a control relies on optional parameters, it deploys without them. This can result in more restrictive evaluation behavior. For example, the `CONFIG.EC2.DT.17` control evaluates all internet gateway attachments as `NON_COMPLIANT` when you deploy it without the `AuthorizedVpcIds` parameter. To deploy these types of controls with parameters, create the corresponding AWS Config rule directly in AWS Config.

## Change in drift behavior with service-linked AWS Config rules
<a name="change-in-drift-behavior"></a>

 Before the introduction of service-linked Config rules in AWS Control Tower, you could modify AWS Config rule configurations or add remediations outside of AWS Control Tower. With the release of service-linked Config rules, this behavior has changed: 
+ Modifications made to Config rule settings outside of AWS Control Tower are treated as drift.
+ External remediation configurations added to these Config rules are treated as drift.
+ AWS Control Tower automatically removes these external modifications with the adoption of service-linked Config rules.
+ To maintain consistent governance, all updates that AWS Control Tower supports for your service-linked Config rules must be managed through AWS Control Tower.

**Important**  
Before you adopt service-linked Config rules, review the existing customizations, such as remediations, that you have made to Config rules outside of AWS Control Tower, because these customizations will be removed during the transition. The AWS Config APIs do not support adding remediation configurations for service-linked AWS Config rules. See [`PutRemediationConfigurations`](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationConfigurations.html).