

# Reviewing your Savings Plan purchase analysis
<a name="sp-review-purchase-analysis"></a>

After setting parameters and running the analysis, Purchase Analyzer applies the resulting Savings Plan to each hour of the historical lookback period. This process takes into account the composition of usage across different services and Regions, as well as the Savings Plans inventory after removing any Savings Plans that were excluded. This allows you to review the impact of a purchase on your unique environment. The data is presented in three charts: cost, coverage, and utilization. You can switch between tabs to view the different metrics and hover over data points for detailed hourly information.

The **Analysis** section on the **Purchase Analyzer** page shows visual overtime charts and includes the following summary metrics:
+ **Estimated monthly savings** – The monthly net savings amount based on the usage over the selected time period, if you purchased the recommended or custom commitment.
+ **Average hourly coverage increase** – The estimated average hourly coverage increase, if you were to purchase the recommended or custom commitment.
+ **Average hourly utilization** – The estimated average hourly utilization of the recommended or custom commitment.

**Note**  
You can also receive your purchase analyses via the [AWS Cost Explorer API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html).

**To model different scenarios**

1. Adjust the parameters as required.

1. Choose **Run analysis**.

   This generates new results.

1. Compare results across different commitment amounts or terms.