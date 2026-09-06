

# Configure the Region deny control
<a name="region-deny"></a>

AWS Control Tower offers two Region deny controls. One control, `AWS-GR_REGION_DENY`, when activated, applies to the entire landing zone. Another control, `CT.MULTISERVICE.PV.1`, when activated, can apply to specific OUs that you specify. For more information see [Deny access to AWS based on the requested AWS Region](https://docs.aws.amazon.com/controltower/latest/controlreference/primary-region-deny-policy.html) and [Region deny control applied to the OU](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html).

**Considerations about the Region deny control for the landing zone**

The Region deny control, [`AWS-GR_REGION_DENY`](https://docs.aws.amazon.com/controltower/latest/controlreference/primary-region-deny-policy.html) is unique, because it applies to the landing zone as a whole, rather than to any specific OU. To configure the Region deny control, go to the **Landing zone settings** page and select **Modify settings**. 
+ This setting can be changed at a later time.
+ When enabled, this control applies to all OUs with the `AWSControlTowerBaseline` enabled.
+ This control cannot be configured for individual OUs.

**Note**  
Before you enable the Region deny control, be sure that you do not have existing resources in these Regions, because you will not have access to your resources after you apply the control. While the control is enabled, you will not be able to deploy resources in the denied Regions.

When you enable the control, it applies to all top-level OUs with the `AWSControlTowerBaseline` enabled, and it is inherited by OUs lower in the organization hierarchy. When you remove the control, it is removed on all previously applied OUs, all non-governed Regions in AWS Control Tower remain in a **Not governed** status, and you can deploy resources in Regions outside of AWS Control Tower availability.

**Exceptions**  
You cannot deny access to your home Region. Certain global AWS services, such as IAM and AWS Organizations, are exempt from the Region deny control. To learn more, see [Deny access to AWS based on the requested AWS Region](https://docs.aws.amazon.com/controltower/latest/controlreference/lz-region-deny.html).
+ Full control name: **Deny access to AWS based on the requested AWS Region for the landing zone**
+ Control description: Disallows access to unlisted operations in global and regional services outside of the specified Regions for the landing zone.
+ This is an elective control with preventive guidance.

To view the template for the Region deny control SCP, see [Deny access to AWS based on the requested AWS Region](https://docs.aws.amazon.com/controltower/latest/controlreference/lz-region-deny.html) in the *AWS Control Tower Control reference*. The AWS Control Tower SCP is similar to [the SCP for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-deny-region), but not identical.

You can determine Regional service endpoints on the [Regional services page](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services).