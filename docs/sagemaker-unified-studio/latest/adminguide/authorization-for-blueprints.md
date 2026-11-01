

# Manage blueprint authorization
<a name="authorization-for-blueprints"></a>

You can perform the following procedure to manage the authorization configuration of a blueprint. 

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and choose the domain’s name from the list. The name is a hyperlink.

1. On the domain's details page, navigate to the **Blueprints** tab. 

1. In the **Blueprints** tab, choose the blueprint the authorization configuration of which you'd like to change. The name of the blueprint is a hyperlink. 

1. On the bluprint's details page, navigate to the **Authorization** tab. 

1. In the Authorization tab, you can use the **Add** and **Remove** buttons to add or remove domain units and designations for the grant. By adding a domain unit, you're allowing projects that belong to this domain unit to use this blueprint. By adding a designation, you're allowing project members with that designation to use this blueprint. By removing a domain unit or designation, you're removing the ability to use this blueprint from the corresponding projects or members.

   You can use the **Cascade to all child domain units** toggle to apply the authorization setting that you're configuring to all the child domain units of the domain unit that you're adding or removing.

**Important**  
To use a blueprint, a designation must include the **Manage Environments** permission. If you add a designation that doesn't have this permission, project members with that designation can't use the blueprint. For example, the Data Steward designation doesn't have Manage Environments permissions and can't use this blueprint. To resolve this, either update the designation from the domain management portal to include the Manage Environments permission, or remove the designation from the authorization.

![Blueprint authorization in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Blueprint.png)
