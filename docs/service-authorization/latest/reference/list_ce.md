

# Actions, resources, and condition keys for AWS Cost Explorer Service
<a name="list_ce"></a>

AWS Cost Explorer Service (service prefix: `ce`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Cost_Explorer_Service.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ce/ce.json) for this service.

**Topics**
+ [API operations defined by AWS Cost Explorer Service](#list_ce-operations)
+ [Actions defined by AWS Cost Explorer Service](#list_ce-actions-as-permissions)
+ [Permission-only actions for AWS Cost Explorer Service](#list_ce-permission-only-actions)
+ [Resource types defined by AWS Cost Explorer Service](#list_ce-resources-for-iam-policies)
+ [Condition keys for AWS Cost Explorer Service](#list_ce-policy-keys)

## API operations defined by AWS Cost Explorer Service
<a name="list_ce-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ce-actions-as-permissions).




- **   CreateAnomalyMonitor  **
  - **IAM action:**  [ce:CreateAnomalyMonitor](#list_ce-action-CreateAnomalyMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ce:TagResource](#list_ce-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAnomalySubscription  **
  - **IAM action:**  [ce:CreateAnomalySubscription](#list_ce-action-CreateAnomalySubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ce:TagResource](#list_ce-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCostCategoryDefinition  **
  - **IAM action:**  [ce:CreateCostCategoryDefinition](#list_ce-action-CreateCostCategoryDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ce:TagResource](#list_ce-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAnomalyMonitor  **
  - **IAM action:**  [ce:DeleteAnomalyMonitor](#list_ce-action-DeleteAnomalyMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnomalySubscription  **
  - **IAM action:**  [ce:DeleteAnomalySubscription](#list_ce-action-DeleteAnomalySubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCostCategoryDefinition  **
  - **IAM action:**  [ce:DeleteCostCategoryDefinition](#list_ce-action-DeleteCostCategoryDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCostCategoryDefinition  **
  - **IAM action:**  [ce:DescribeCostCategoryDefinition](#list_ce-action-DescribeCostCategoryDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnomalies  **
  - **IAM action:**  [ce:GetAnomalies](#list_ce-action-GetAnomalies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnomalyMonitors  **
  - **IAM action:**  [ce:GetAnomalyMonitors](#list_ce-action-GetAnomalyMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnomalySubscriptions  **
  - **IAM action:**  [ce:GetAnomalySubscriptions](#list_ce-action-GetAnomalySubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApproximateUsageRecords  **
  - **IAM action:**  [ce:GetApproximateUsageRecords](#list_ce-action-GetApproximateUsageRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommitmentPurchaseAnalysis  **
  - **IAM action:**  [ce:GetCommitmentPurchaseAnalysis](#list_ce-action-GetCommitmentPurchaseAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCostAndUsage  **
  - **IAM action:**  [ce:GetCostAndUsage](#list_ce-action-GetCostAndUsage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetCostAndUsageComparisons  **
  - **IAM action:**  [ce:GetCostAndUsageComparisons](#list_ce-action-GetCostAndUsageComparisons) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCostAndUsageWithResources  **
  - **IAM action:**  [ce:GetCostAndUsageWithResources](#list_ce-action-GetCostAndUsageWithResources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetCostCategories  **
  - **IAM action:**  [ce:GetCostCategories](#list_ce-action-GetCostCategories)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetCostComparisonDrivers  **
  - **IAM action:**  [ce:GetCostComparisonDrivers](#list_ce-action-GetCostComparisonDrivers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCostForecast  **
  - **IAM action:**  [ce:GetCostForecast](#list_ce-action-GetCostForecast)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetDimensionValues  **
  - **IAM action:**  [ce:GetDimensionValues](#list_ce-action-GetDimensionValues)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetReservationCoverage  **
  - **IAM action:**  [ce:GetReservationCoverage](#list_ce-action-GetReservationCoverage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetReservationPurchaseRecommendation  **
  - **IAM action:**  [ce:GetReservationPurchaseRecommendation](#list_ce-action-GetReservationPurchaseRecommendation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetReservationUtilization  **
  - **IAM action:**  [ce:GetReservationUtilization](#list_ce-action-GetReservationUtilization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRightsizingRecommendation  **
  - **IAM action:**  [ce:GetRightsizingRecommendation](#list_ce-action-GetRightsizingRecommendation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSavingsPlanPurchaseRecommendationDetails  **
  - **IAM action:**  [ce:GetSavingsPlanPurchaseRecommendationDetails](#list_ce-action-GetSavingsPlanPurchaseRecommendationDetails)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSavingsPlansCoverage  **
  - **IAM action:**  [ce:GetSavingsPlansCoverage](#list_ce-action-GetSavingsPlansCoverage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSavingsPlansPurchaseRecommendation  **
  - **IAM action:**  [ce:GetSavingsPlansPurchaseRecommendation](#list_ce-action-GetSavingsPlansPurchaseRecommendation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSavingsPlansUtilization  **
  - **IAM action:**  [ce:GetSavingsPlansUtilization](#list_ce-action-GetSavingsPlansUtilization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetSavingsPlansUtilizationDetails  **
  - **IAM action:**  [ce:GetSavingsPlansUtilizationDetails](#list_ce-action-GetSavingsPlansUtilizationDetails)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetTags  **
  - **IAM action:**  [ce:GetTags](#list_ce-action-GetTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetUsageForecast  **
  - **IAM action:**  [ce:GetUsageForecast](#list_ce-action-GetUsageForecast)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListCommitmentPurchaseAnalyses  **
  - **IAM action:**  [ce:ListCommitmentPurchaseAnalyses](#list_ce-action-ListCommitmentPurchaseAnalyses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCostAllocationTagBackfillHistory  **
  - **IAM action:**  [ce:ListCostAllocationTagBackfillHistory](#list_ce-action-ListCostAllocationTagBackfillHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCostAllocationTags  **
  - **IAM action:**  [ce:ListCostAllocationTags](#list_ce-action-ListCostAllocationTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListCostCategoryDefinitions  **
  - **IAM action:**  [ce:ListCostCategoryDefinitions](#list_ce-action-ListCostCategoryDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCostCategoryResourceAssociations  **
  - **IAM action:**  [ce:ListCostCategoryResourceAssociations](#list_ce-action-ListCostCategoryResourceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSavingsPlansPurchaseRecommendationGeneration  **
  - **IAM action:**  [ce:ListSavingsPlansPurchaseRecommendationGeneration](#list_ce-action-ListSavingsPlansPurchaseRecommendationGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ce:ListTagsForResource](#list_ce-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ProvideAnomalyFeedback  **
  - **IAM action:**  [ce:ProvideAnomalyFeedback](#list_ce-action-ProvideAnomalyFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCommitmentPurchaseAnalysis  **
  - **IAM action:**  [ce:StartCommitmentPurchaseAnalysis](#list_ce-action-StartCommitmentPurchaseAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCostAllocationTagBackfill  **
  - **IAM action:**  [ce:StartCostAllocationTagBackfill](#list_ce-action-StartCostAllocationTagBackfill) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSavingsPlansPurchaseRecommendationGeneration  **
  - **IAM action:**  [ce:StartSavingsPlansPurchaseRecommendationGeneration](#list_ce-action-StartSavingsPlansPurchaseRecommendationGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ce:TagResource](#list_ce-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ce:UntagResource](#list_ce-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAnomalyMonitor  **
  - **IAM action:**  [ce:UpdateAnomalyMonitor](#list_ce-action-UpdateAnomalyMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAnomalySubscription  **
  - **IAM action:**  [ce:UpdateAnomalySubscription](#list_ce-action-UpdateAnomalySubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCostAllocationTagsStatus  **
  - **IAM action:**  [ce:UpdateCostAllocationTagsStatus](#list_ce-action-UpdateCostAllocationTagsStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateCostCategoryDefinition  **
  - **IAM action:**  [ce:UpdateCostCategoryDefinition](#list_ce-action-UpdateCostCategoryDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Cost Explorer Service
<a name="list_ce-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateAnomalyMonitor.html)  **
  - **Description:** Grants permission to create a new Anomaly Monitor
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ce-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateAnomalySubscription.html)  **
  - **Description:** Grants permission to create a new Anomaly Subscription
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ce-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateCostCategoryDefinition.html)  **
  - **Description:** Grants permission to create a new Cost Category with the requested name and rules
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ce-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalyMonitor.html)  **
  - **Description:** Grants permission to delete an Anomaly Monitor
  - **Resource types (\*required):** [anomalymonitor\*](#list_ce-resource-anomalymonitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalySubscription.html)  **
  - **Description:** Grants permission to delete an Anomaly Subscription
  - **Resource types (\*required):** [anomalysubscription\*](#list_ce-resource-anomalysubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteCostCategoryDefinition.html)  **
  - **Description:** Grants permission to delete a Cost Category
  - **Resource types (\*required):** [costcategory\*](#list_ce-resource-costcategory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DescribeCostCategoryDefinition.html)  **
  - **Description:** Grants permission to retrieve descriptions such as the name, ARN, rules, definition, and effective dates of a Cost Category
  - **Resource types (\*required):** [costcategory\*](#list_ce-resource-costcategory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnomalies](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalies.html)  **
  - **Description:** Grants permission to retrieve anomalies
  - **Resource types (\*required):** [anomalymonitor\*](#list_ce-resource-anomalymonitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnomalyMonitors](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalyMonitors.html)  **
  - **Description:** Grants permission to query Anomaly Monitors
  - **Resource types (\*required):** [anomalymonitor\*](#list_ce-resource-anomalymonitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalySubscriptions.html)  **
  - **Description:** Grants permission to query Anomaly Subscriptions
  - **Resource types (\*required):** [anomalysubscription\*](#list_ce-resource-anomalysubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApproximateUsageRecords](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to retrieve approximate usage record count for the chosen resource, level, and hourly granularity preferences, derived from the past month's usage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCommitmentPurchaseAnalysis](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCommitmentPurchaseAnalysis.html)  **
  - **Description:** Grants permission to retrieve the commitment purchase analysis for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html)  **
  - **Description:** Grants permission to retrieve the cost and usage metrics for your account
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCostAndUsageComparisons](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsageComparisons.html)  **
  - **Description:** Grants permission to retrieve the cost and usage comparisons for your account
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCostAndUsageWithResources](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsageWithResources.html)  **
  - **Description:** Grants permission to retrieve the cost and usage metrics with resources for your account
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCostCategories](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostCategories.html)  **
  - **Description:** Grants permission to query Cost Catagory names and values for a specified time period
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCostComparisonDrivers](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostComparisonDrivers.html)  **
  - **Description:** Grants permission to retrieve the cost drivers for your account
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCostForecast](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostForecast.html)  **
  - **Description:** Grants permission to retrieve a cost forecast for a forecast time period
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html)  **
  - **Description:** Grants permission to retrieve all available filter values for a filter for a period of time
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReservationCoverage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationCoverage.html)  **
  - **Description:** Grants permission to retrieve the reservation coverage for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetReservationPurchaseRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationPurchaseRecommendation.html)  **
  - **Description:** Grants permission to retrieve the reservation recommendations for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetReservationUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationUtilization.html)  **
  - **Description:** Grants permission to retrieve the reservation utilization for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRightsizingRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetRightsizingRecommendation.html)  **
  - **Description:** Grants permission to retrieve the rightsizing recommendations for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSavingsPlanPurchaseRecommendationDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlanPurchaseRecommendationDetails.html)  **
  - **Description:** Grants permission to retrieve the Savings Plan recommendation details for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSavingsPlansCoverage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansCoverage.html)  **
  - **Description:** Grants permission to retrieve the Savings Plans coverage for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSavingsPlansPurchaseRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html)  **
  - **Description:** Grants permission to retrieve the Savings Plans recommendations for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSavingsPlansUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html)  **
  - **Description:** Grants permission to retrieve the Savings Plans utilization for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSavingsPlansUtilizationDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilizationDetails.html)  **
  - **Description:** Grants permission to retrieve the Savings Plans utilization details for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTags](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetTags.html)  **
  - **Description:** Grants permission to query tags for a specified time period
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUsageForecast](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetUsageForecast.html)  **
  - **Description:** Grants permission to retrieve a usage forecast for a forecast time period
  - **Resource types (\*required):** [billingview](#list_ce-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCommitmentPurchaseAnalyses](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCommitmentPurchaseAnalyses.html)  **
  - **Description:** Grants permission to retrieve a list of your historical commitment purchase analyses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCostAllocationTagBackfillHistory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostAllocationTagBackfillHistory.html)  **
  - **Description:** Grants permission to list Cost Allocation Tag backfill history
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCostAllocationTags](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostAllocationTags.html)  **
  - **Description:** Grants permission to list Cost Allocation Tags
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCostCategoryDefinitions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostCategoryDefinitions.html)  **
  - **Description:** Grants permission to retrieve names, ARN, and effective dates for all Cost Categories
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCostCategoryResourceAssociations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostCategoryResourceAssociations.html)  **
  - **Description:** Grants permission to retrieve resource associations of all Cost Categories defined in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSavingsPlansPurchaseRecommendationGeneration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListSavingsPlansPurchaseRecommendationGeneration.html)  **
  - **Description:** Grants permission to retrieve a list of your historical recommendation generations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Cost Explorer resource
  - **Resource types (\*required):** [anomalymonitor](#list_ce-resource-anomalymonitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [anomalysubscription](#list_ce-resource-anomalysubscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [costcategory](#list_ce-resource-costcategory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ProvideAnomalyFeedback](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProvideAnomalyFeedback.html)  **
  - **Description:** Grants permission to provide feedback on detected anomalies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCommitmentPurchaseAnalysis](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartCommitmentPurchaseAnalysis.html)  **
  - **Description:** Grants permission to request a commitment purchase analysis
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCostAllocationTagBackfill](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartCostAllocationTagBackfill.html)  **
  - **Description:** Grants permission to request a Cost Allocation Tag backfill
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSavingsPlansPurchaseRecommendationGeneration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartSavingsPlansPurchaseRecommendationGeneration.html)  **
  - **Description:** Grants permission to request a Savings Plans recommendation generation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a Cost Explorer resource
  - **Resource types (\*required):** [anomalymonitor](#list_ce-resource-anomalymonitor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ce-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Resource types (\*required):** [anomalysubscription](#list_ce-resource-anomalysubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ce-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Resource types (\*required):** [costcategory](#list_ce-resource-costcategory) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ce-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a Cost Explorer resource
  - **Resource types (\*required):** [anomalymonitor](#list_ce-resource-anomalymonitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Resource types (\*required):** [anomalysubscription](#list_ce-resource-anomalysubscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Resource types (\*required):** [costcategory](#list_ce-resource-costcategory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ce-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalyMonitor.html)  **
  - **Description:** Grants permission to update an existing Anomaly Monitor
  - **Resource types (\*required):** [anomalymonitor\*](#list_ce-resource-anomalymonitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalySubscription.html)  **
  - **Description:** Grants permission to update an existing Anomaly Subscription
  - **Resource types (\*required):** [anomalysubscription\*](#list_ce-resource-anomalysubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCostAllocationTagsStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.html)  **
  - **Description:** Grants permission to update existing Cost Allocation Tags status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostCategoryDefinition.html)  **
  - **Description:** Grants permission to update an existing Cost Category
  - **Resource types (\*required):** [costcategory\*](#list_ce-resource-costcategory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Cost Explorer Service
<a name="list_ce-permission-only-actions"></a>

The following actions are defined by AWS Cost Explorer Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateNotificationSubscription](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to create Reservation expiration alerts |  |   | Write | 
|   [CreateReport](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to create Cost Explorer Reports |  |   | Write | 
|   [DeleteNotificationSubscription](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to delete Reservation expiration alerts |  |   | Write | 
|   [DeleteReport](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to delete Cost Explorer Reports |  |   | Write | 
|   [DescribeNotificationSubscription](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view Reservation expiration alerts |  |   | Read | 
|   [DescribeReport](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view Cost Explorer Reports page |  |   | Read | 
|   [GetConsoleActionSetEnforced](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view whether existing or fine-grained IAM actions are being used to control authorization to Billing, Cost Management, and Account consoles |  |   | Read | 
|   [GetPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view Cost Explorer Preferences page |  |   | Read | 
|   [UpdateConsoleActionSetEnforced](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to change whether existing or fine-grained IAM actions will be used to control authorization to Billing, Cost Management, and Account consoles |  |   | Write | 
|   [UpdateNotificationSubscription](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to update Reservation expiration alerts |  |   | Write | 
|   [UpdatePreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to edit Cost Explorer Preferences page |  |   | Write | 
|   [UpdateReport](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to update Cost Explorer Reports |  |   | Write | 

## Resource types defined by AWS Cost Explorer Service
<a name="list_ce-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [anomalymonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html)  | arn:${Partition}:ce::${Account}:anomalymonitor/${Identifier} | [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_) | 
|  [anomalysubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html)  | arn:${Partition}:ce::${Account}:anomalysubscription/${Identifier} | [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_) | 
|  [billingview](https://docs.aws.amazon.com/cost-management/latest/userguide/)  | arn:${Partition}:billing::${Account}:billingview/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_) | 
|  [costcategory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html)  | arn:${Partition}:ce::${Account}:costcategory/${Identifier} | [aws:ResourceTag/${TagKey}](#list_ce-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Cost Explorer Service
<a name="list_ce-policy-keys"></a>

AWS Cost Explorer Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 