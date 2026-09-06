

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Specifying a default parameter tier for your AWS account and AWS Region
<a name="ps-default-tier"></a>

If you create or update a parameter but don't specify a parameter tier in the command, the default tier setting determines the tier. By default, Parameter Store sets the default setting to the standard parameter tier.

## Default parameter tier options
<a name="parameter-store-advanced-parameters-default-tier"></a>

Standard parameters are available at no cost, but they have size and feature restrictions, as described in [Standard and advanced parameter tiers](parameter-store-advanced-parameters.md#parameter-store-advanced-parameters-table). If your use case requires features or limits that standard parameters don't support, consider setting the advanced tier as the default. The advanced tier offers higher limits and extra features, at a cost. For more information, see [AWS Systems Manager Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store).

You can change Parameter Store default tier settings at any time using the [UpdateServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateServiceSetting.html) API. Set the parameter tier default value to `Standard`, `Advanced`, or `Intelligent-Tiering`.

To maximize efficiency and reduce costs, consider setting `Intelligent-Tiering` as the default value. This setting determines whether to use the standard or advanced tier based on the request content. For example, if you create a parameter that meets the criteria for a standard parameter, intelligent tiering creates the parameter in the standard tier. If you create a parameter where one or more criteria don't meet the standard-tier requirements, intelligent tiering creates the parameter in the advanced tier.

Intelligent tiering offers the following benefits:

**Cost control**  
Intelligent tiering helps control your parameter-related costs by always creating standard parameters unless the request requires the advanced tier.

**Automatic upgrade to the advanced tier**  
When you make a change to your code that requires upgrading a standard parameter to an advanced parameter, intelligent tiering handles the conversion for you. You don't need to change your code to handle the upgrade. Sample use cases include the following:  
+ Your AWS CloudFormation templates provision numerous parameters when they're run. When this process causes you to reach the 10,000 parameter quota in the standard-parameter tier, Intelligent-Tiering automatically upgrades you to the advanced-parameter tier, and your CloudFormation processes aren't interrupted.
+ You store a certificate value in a parameter, rotate the certificate value regularly, and the content is less than the 4 KB quota of the standard-parameter tier. If a replacement certificate value exceeds 4 KB, Intelligent-Tiering automatically upgrades the parameter to the advanced-parameter tier.
+ You want to associate numerous existing standard parameters to a parameter policy, which requires the advanced-parameter tier. Instead of including the `--tier Advanced` option in calls to update parameters, Intelligent-Tiering automatically upgrades parameters to the advanced tier.