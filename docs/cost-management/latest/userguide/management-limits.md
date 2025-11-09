# Quotas and restrictions

The following table describes the current quotas, restrictions, and naming constraints
within AWS Cost Management features.

For a list of quotas and restrictions for features in the AWS Billing console, see [Quotas and restrictions](../../../awsaccountbilling/latest/aboutv2/billing-limits.md "../../../awsaccountbilling/latest/aboutv2/billing-limits.md") in the _AWS Billing User Guide_.

###### Topics

- [Budgets](#limits-budgets "#limits-budgets")
- [Budget reports](#limits-reports "#limits-reports")
- [Cost Explorer](#limits-ce "#limits-ce")
- [AWS Cost Anomaly Detection](#limits-ad "#limits-ad")
- [AWS Pricing Calculator](#limits-pc "#limits-pc")
- [Billing View](#limits-billing-view "#limits-billing-view")
- [AWS Billing and Cost Management Dashboards](#limits-dashboards "#limits-dashboards")

## Budgets

|                                                 |                                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------- |
| Number of free budgets with actions per account | 2                                                                                 |
| Number of actions per budget                    | 10                                                                                |
| Number of budget actions per account            | 100                                                                               |
| Total number of budgets per management account  | 20,000                                                                            |
| Characters allowed in a budget name             | • `0-9`<br>• `A-Z` and `a-z`<br>• `Space`<br>• The following symbols: `_.:/=+-%@` |

## Budget reports

|                                             |     |
| ------------------------------------------- | --- |
| Maximum number of budget reports            | 50  |
| Maximum number of budgets per budget report | 50  |
| Maximum email recipients in a budget report | 50  |

## Cost Explorer

|                                                                       |     |
| --------------------------------------------------------------------- | --- |
| Maximum number of reports that you can save per account               | 300 |
| Maximum number of filters in the `GetCostAndUsage`<br>operation (API) | 100 |

## AWS Cost Anomaly Detection

|                                                                                                                                   |                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum number of anomaly monitors you can create for an<br>AWS services monitor type                                             | 1 monitor per account                                                                                                                                                                                                 |
| Maximum number of anomaly monitors you can create for other monitor<br>types (linked account, cost category, cost allocation tag) | 500 total monitors per management account                                                                                                                                                                             |
| Maximum number of anomaly alert subscriptions you can create                                                                      | 100 subscriptions per account                                                                                                                                                                                         |
| Unsupported services                                                                                                              | • AWS Marketplace<br>• AWS Support<br>• WorkSpaces<br>• Cost Explorer<br>• Budgets<br>• AWS Shield<br>• Amazon Route 53<br>• AWS Certificate Manager<br>• Upfront and recurring reserved fee and Savings Plan<br>fees |

## AWS Pricing Calculator

|                                                                                   |      |
| --------------------------------------------------------------------------------- | ---- |
| Maximum number of workload estimates an account can create in a<br>month          | 50   |
| Maximum number of modifications that can be made in a single<br>workload estimate | 350  |
| Maximum number of usage lines that can be added to a single<br>workload estimate  | 2000 |
| Maximum number of usage lines that can be added to a single bill<br>estimate      | 2000 |

## Billing View

|                                                                    |      |
| ------------------------------------------------------------------ | ---- |
| Maximum number of billing views that you can create per<br>account | 3000 |

## AWS Billing and Cost Management Dashboards

|                                          |     |
| ---------------------------------------- | --- |
| Maximum number of widgets per dashboard  | 20  |
| Maximum number of dashboards per account | 50  |
