# How the cost management capabilities in Amazon Q Developer work

## Agentic architecture

Amazon Q Developer uses an agentic architecture to analyze your AWS costs. When you ask a question, Q creates a plan for how to answer it, gathers data from multiple sources, performs calculations, and dynamically updates its plan based on what it learns at each step. This approach allows Q to handle complex, open-ended questions that do not have predefined workflows.

To answer your question, Amazon Q Developer can perform the following steps.

1. **Forms a plan**: When you ask a question, Q analyzes your request and creates an initial plan for how to gather the necessary information.
2. **Gathers data**: Q retrieves data from the appropriate Billing and Cost Management APIs based on your question. For complex questions, Q may call multiple APIs in series or in parallel.
3. **Performs calculations**: Q can perform calculations ranging from simple period-over-period changes to complex unit economic metrics like cost per vCPU-hour or cost per GB-month of storage.
4. **Updates the plan**: As Q reviews the results from each API call or calculation, it updates its plan based on what it learns. For example, if Q discovers that EC2 costs increased significantly, it might decide to investigate whether any Savings Plans expired.
5. **Continues until complete**: Q continues gathering data and refining its analysis until it has enough information to provide a comprehensive answer to your question.

Throughout this process, Q displays the details of each API call it makes and each calculation it performs, so you can see exactly how it arrived at its answer.

## Data sources and API integrations

Amazon Q Developer retrieves cost data from 38 APIs across seven Billing and Cost Management services. This broad integration allows Q to answer questions that span multiple data sources without requiring you to switch between different tools or console pages.

### Cost Explorer

Amazon Q Developer uses Cost Explorer APIs to retrieve your historical and forecasted cost and usage data:

- **GetCostAndUsage**: Retrieves cost and usage data aggregated by time period and dimension
- **GetCostAndUsageWithResources**: Retrieves resource-level cost data with hourly granularity
- **GetCostForecast**: Retrieves forecasted costs for a specified time period
- **GetUsageForecast**: Retrieves forecasted usage for a specified time period
- **GetDimensionValues**: Retrieves available values for cost dimensions (such as service names or account IDs)
- **GetTags**: Retrieves available cost allocation tag keys and values
- **GetCostCategories**: Retrieves available cost category keys and values
- **GetAnomalies**: Retrieves detected cost anomalies
- **GetReservationCoverage**: Retrieves the percentage eligible spend covered by reservations
- **GetReservationUtilization**: Retrieves the utilization of purchased reservations
- **GetReservationPurchaseRecommendation**: Retrieves recommendations for purchasing reservations
- **GetSavingsPlansCoverage**: Retrieves the percentage of eligible spend covered by Savings Plans
- **GetSavingsPlansUtilization**: Retrieves the utilization of purchased Savings Plans
- **GetSavingsPlansUtilizationDetails**: Retrieves detailed utilization data for Savings Plans
- **GetSavingsPlansPurchaseRecommendation**: Retrieves recommendations for purchasing Savings Plans
- **GetRightsizingRecommendation**: Retrieves rightsizing recommendations for EC2 instances
- **GetCostAndUsageComparisons**: Retrieves cost comparisons between time periods
- **GetCostComparisonDrivers**: Retrieves the drivers of cost changes between time periods

### Cost Optimization Hub

Amazon Q Developer uses Cost Optimization Hub APIs to retrieve personalized cost optimization recommendations:

- **GetRecommendation**: Retrieves details for a specific recommendation
- **ListRecommendations**: Retrieves a list of recommendations with filtering options
- **ListRecommendationSummaries**: Retrieves summary information about recommendations

### AWS Compute Optimizer

Amazon Q Developer uses Compute Optimizer APIs to retrieve resource optimization recommendations:

- **GetAutoScalingGroupRecommendations**: Retrieves rightsizing recommendations for Auto Scaling groups
- **GetEBSVolumeRecommendations**: Retrieves recommendations for EBS volumes
- **GetEC2InstanceRecommendations**: Retrieves rightsizing recommendations for EC2 instances
- **GetECSServiceRecommendations**: Retrieves recommendations for ECS services
- **GetRDSDatabaseRecommendations**: Retrieves recommendations for RDS databases
- **GetLambdaFunctionRecommendations**: Retrieves recommendations for Lambda functions
- **GetIdleRecommendations**: Retrieves recommendations for idle resources
- **GetLicenseRecommendations**: Retrieves recommendations for license optimization
- **GetEffectiveRecommendationPreferences**: Retrieves the effective recommendation preferences

### AWS Budgets

Amazon Q Developer uses the Budgets API to retrieve information about your budget configurations and status:

- **DescribeBudgets**: Retrieves budget details including thresholds and actual spending

### Free Tier

Amazon Q Developer uses Free Tier APIs to retrieve information about your free tier usage:

- **GetFreeTierUsage**: Retrieves your current free tier usage
- **GetAccountPlanState**: Retrieves information about your current account type and free tier eligibility
- **ListAccountActivities**: Retrieves a list of account activities you can take to earn additional free tier credits
- **GetAccountActivity**: Retrieves details of a specific account activity you can take to earn additional free tier credits

### AWS Price List

Amazon Q Developer uses Price List APIs to retrieve public pricing information for AWS services:

- **DescribeServices**: Retrieves a list of available AWS services
- **GetAttributeValues**: Retrieves valid values for product attributes
- **GetProducts**: Retrieves pricing information for specific products

## Calculation engine

Amazon Q Developer includes a flexible calculation engine that allows it to perform a wide range of calculations on your cost data. This capability enables it to provide deeper insights than simple data retrieval alone.

### Types of calculations

Q can perform calculations including:

- **Period-over-period changes**: Calculate the difference in costs between two time periods, both in absolute terms and as a percentage change.
- **Unit economics**: Calculate metrics like cost per vCPU-hour, cost per GB-month of storage, or cost per API request.
- **Effective rates**: Calculate the effective cost per unit after applying discounts from Savings Plans or Reserved Instances.
- **Aggregations**: Sum, average, or find the minimum or maximum values across multiple dimensions.
- **Custom metrics**: Combine multiple data points to create custom metrics tailored to your question.

## API transparency

With each response, Amazon Q Developer provides full transparency into how it retrieved and processed your data. This transparency helps you understand exactly what Q did to answer your question and allows you to verify the results or provide more specific instructions in follow-up questions.

### What Amazon Q Developer displays

For each response, Q shows you:

- **API calls made**: Q displays the name of each API it called to retrieve data.
- **Parameters used**: Q shows the exact parameters it used for each API call, including time ranges, filters, grouping dimensions, and any other relevant parameters.
- **Console deep-links**: Where applicable, Q provides links to matching views in the AWS Management Console. These links allow you to verify the data Q retrieved or explore the data further using the console's visualization and filtering capabilities.

### Using transparency to refine your questions

The transparency that Q provides allows you to guide its behavior more effectively. For example:

- If Q retrieved data for the wrong time period, you can specify the exact dates you want in a follow-up question.
- If Q grouped costs by one tag key but you wanted them grouped by another, you can ask Q to regroup the data.

## Limitations

Amazon Q Developer has the following limitations:

- **Pricing data**: The pricing and cost estimation capabilities only provide public pricing data from the AWS Price List APIs. Customer-specific discounts are not reflected in pricing estimates. Amazon Q Developer does not integrate with the AWS Pricing Calculator, so it cannot create or save workload estimates that reflect customer-specific discounts or pricing.
- **Savings Plans analysis**: Amazon Q Developer can provide Savings Plans recommendations and analyze your historical Savings Plans coverage and utilization. Q does not integrate with Savings Plans Purchase Analyzer, so it cannot model the impact of a specific Savings Plans purchase on savings, coverage, or utilization.
- **Mutating actions**: Amazon Q Developer can retrieve and analyze cost data, but cannot take mutating actions on your behalf, such as creating or modifying budgets, purchasing Savings Plans or Reserved Instances, or modifying Cost Management preferences.
