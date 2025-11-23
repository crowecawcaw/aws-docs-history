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

|                                                     |                                                                                   |
| --------------------------------------------------- | --------------------------------------------------------------------------------- |
| Number of free budgets with actions per account     | 2                                                                                 |
| Number of actions per budget                        | 10                                                                                |
| Number of budget actions per account                | 100                                                                               |
| Total number of budgets per management account      | 20,000                                                                            |
| Total number of budgets using a custom billing view | 150                                                                               |
| Characters allowed in a budget name                 | • `0-9`<br>• `A-Z` and `a-z`<br>• `Space`<br>• The following symbols: `_.:/=+-%@` |

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

**AWS Managed Monitor Quotas**

|                                                                                                                   |       |
| ----------------------------------------------------------------------------------------------------------------- | ----- |
| AWS managed monitor for AWS services per account (management and<br>member)                                       | 1     |
| Additional AWS managed monitors (linked account, cost allocation<br>tag, or cost category) per management account | 1     |
| Total AWS managed monitors per management account                                                                 | 2     |
| Total AWS managed monitors per member account                                                                     | 1     |
| Values tracked per AWS managed monitor                                                                            | 5,000 |

**Customer Managed Monitor Quotas**

|                                                                     |     |
| ------------------------------------------------------------------- | --- |
| Total customer managed monitors per management account              | 500 |
| Values per customer managed monitor (linked accounts or tag values) | 10  |
| Values per customer managed monitor (cost category values)          | 1   |

**General Quotas (Apply to Both)**

|                                        |                                                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alert subscriptions per account        | 100                                                                                                                                                                                                            |
| Email recipients per subscription      | 10                                                                                                                                                                                                             |
| Amazon SNS topics per subscription     | 1                                                                                                                                                                                                              |
| Monitors per alert subscription        | 502 maximum (all monitors can be attached)                                                                                                                                                                     |
| Time to detect anomaly after usage     | Up to 24 hours                                                                                                                                                                                                 |
| Historical data required for detection | 10 days minimum                                                                                                                                                                                                |
| Unsupported services                   | • AWS Marketplace<br>• AWS Support<br>• WorkSpaces<br>• Cost Explorer<br>• Budgets<br>• AWS Shield<br>• Amazon Route 53<br>• AWS Certificate Manager<br>• Only analyzes Usage charge type and NetUnblendedCost |

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
