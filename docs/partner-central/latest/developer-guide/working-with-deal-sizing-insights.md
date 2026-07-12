The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with deal sizing insights

## What is Deal Sizing?

Deal Sizing is a capability within the APN Customer Engagements (ACE) Opportunities in AWS Partner Central that uses AI to provide automated deal size estimates and AWS service recommendations when Partners create or update opportunities.

### AI forecasted MRR estimates

Deal sizing insights provide the median of the forecasted monthly recurring revenue (MRR) ranges based on Partners' historical AWS opportunities, use cases, and business descriptions. Partners should review and update the total MRR as Partners gather more information about the deal and progress through the sales cycle.

### AI-Recommended AWS Products

AI-recommended products are identified based on customer business problem descriptions and opportunity details. The AI recommends relevant AWS products aligned with technical requirements and use cases. Partners should review these suggestions and customize the product selection to match the customer's specific needs.

### Enhanced Insights with Pricing Calculator URLs

Partners can also import AWS Pricing Calculator URLs to automatically populate service selections and receive enhanced insights including Migration Acceleration Program (MAP) eligibility indicators, optimization recommendations, and potential cost savings analysis.

## Understanding Source-Separated Data

Deal Sizing provides insights from two separate sources to give you comprehensive visibility into opportunity value:

- **AWS Source:** AI-recommended products based on patterns from similar historical opportunities
- **Partner Source:** Your own estimates imported from AWS Pricing Calculator

### Handling Variance Between Sources

When partner-provided estimates differ significantly from AWS recommendations, Partners should:

1. Review opportunity details to ensure all relevant information is captured
2. Verify Pricing Calculator URL configurations match actual requirements
3. Consider AWS recommendations as data points informed by similar historical opportunities
4. Make informed decisions based on specific customer context and requirements

## Accessing Deal Sizing Insights

Partners access Deal Sizing data through the `GetAwsOpportunitySummary` API action, which returns an extended `AwsOpportunitySummary` object containing deal sizing forecasts, product recommendations, and optimization insights.

### When Deal Sizing Data Becomes Available

Deal Sizing insights become available after an opportunity is created with sufficient customer and project details. The system analyzes the opportunity attributes and generates:

1. **AI forecasted MRR:** Automatically calculated based on opportunity characteristics
2. **AWS product recommendations:** Services relevant to the customer's business problem and technical requirements
3. **Enhanced insights (when Pricing Calculator URL provided):** MAP eligibility, optimization recommendations, and cost savings analysis

###### Note

Deal Sizing insights are not available for all opportunities. Eligibility depends on factors such as partner history and the completeness of opportunity details provided.

## Providing Deal Sizing Inputs

Partners provide inputs for Deal Sizing through the `CreateOpportunity` and `UpdateOpportunity` API actions. The system uses opportunity attributes to generate recommendations.

### Providing Total Contract Value (TCV)

Partners who estimate in Total Contract Value rather than Monthly Recurring Revenue can provide their deal value directly. AWS automatically converts TCV to AWS MRR using AI-powered conversion models.

For deal sizing in TCV, provide `ExpectedContractDuration` as `Months` (valid values range from 1 to 144 months) and `TargetCompany` as `Self` and `Frequency` as `None`.

```
{
  "Project": {
    "ExpectedContractDuration": { "Term": "Months", "Value": "36" },
    "ExpectedCustomerSpend": [
      {
        "Amount": "1200000.00",
        "CurrencyCode": "USD",
        "Frequency": "None",
        "TargetCompany": "Self"
      }
    ]
  }
}
```

AWS derives the AWS MRR estimate and returns both entries on `GetOpportunity`:

```
{
  "Project": {
    "ExpectedContractDuration": { "Term": "Months", "Value": "36" },
    "ExpectedCustomerSpend": [
      {
        "Amount": "5600.00",
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      },
      {
        "Amount": "1200000.00",
        "CurrencyCode": "USD",
        "Frequency": "None",
        "TargetCompany": "Self"
      }
    ]
  }
}
```

In above example the `ExpectedCustomerSpend` first array contains the AWS MRR estimate (`TargetCompany: "AWS"`, `Frequency: "Monthly"`) and second array is the partner’s Total Contract Value (`TargetCompany: "Self"`, `Frequency: "None"`).

#### TCV Validation Rules

All TCV validation errors return error code `INVALID_VALUE` with `Reason: "BUSINESS_VALIDATION_FAILED"`. The distinguishing factor is the `FieldName` and `Message`:

| Condition                                                   | Field                                         | Message                                                           |
| ----------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------- |
| Self entry without `ExpectedContractDuration`               | `project.expectedContractDuration`            | ExpectedContractDuration is required when a Self entry is present |
| `ExpectedContractDuration` without Self entry (Create only) | `project.expectedCustomerSpend`               | A Self entry is required when ExpectedContractDuration is present |
| Multiple Self entries                                       | `project.expectedCustomerSpend`               | Only one Self entry is allowed                                    |
| Invalid TargetCompany when duration present                 | `project.expectedCustomerSpend.targetCompany` | TargetCompany must be 'AWS' or 'Self'                             |
| Currency mismatch between AWS and Self                      | `project.expectedCustomerSpend.currencyCode`  | CurrencyCode must match between entries                           |
| Self entry + EstimationUrl together                         | `project.expectedCustomerSpend.estimationUrl` | Self entry and EstimationUrl cannot coexist                       |

###### Note

On `UpdateOpportunity`, if `ExpectedContractDuration` is present without a Self entry but partner deal value exists in storage, the system reconstructs the Self entry automatically — no error is thrown.

#### Switching Between TCV and Manual MRR

To switch from TCV mode back to manual MRR, explicitly set `ExpectedContractDuration` to `null` and provide only an `AWS` entry:

```
{
  "Project": {
    "ExpectedContractDuration": null,
    "ExpectedCustomerSpend": [
      {
        "Amount": "8000.00",
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      }
    ]
  }
}
```

###### Note

Omitting `ExpectedContractDuration` from the payload (not sending the field) means “no change” — the existing TCV data is preserved. Explicitly sending `null` means “clear TCV mode.”

#### TCV and Pricing Calculator URLs

If a partner provides both a `Self` entry (TCV mode) and an `EstimationUrl`, the API returns a validation error. Self entry and EstimationUrl cannot coexist in the same request.

### Providing Manual MRR Estimates

Partners can manually enter MRR estimates using the `Project.ExpectedCustomerSpend[].Amount` field:

###### Note

The `CurrencyCode` field accepts `USD` and `EUR`. If the AWS Partition is `aws-eusc` (AWS European Sovereign Cloud), the currency code must be `EUR`.

```
{
  "Project": {
    "ExpectedCustomerSpend": [
      {
        "Amount": "25000.00",
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      }
    ]
  }
}
```

This field is available to all Partners and can be used to accept AI forecasts by setting the same value or to override with Partner-provided values.

### Providing Pricing Calculator URLs

Partners can optionally provide AWS Pricing Calculator URLs via the `Project.ExpectedCustomerSpend[].EstimationUrl` field to automatically import service configurations and receive enhanced insights including MAP eligibility indicators, optimization recommendations, and cost savings analysis.

```
{
  "Project": {
    "ExpectedCustomerSpend": [
      {
        "Amount": null,
        "CurrencyCode": "USD",
        "EstimationUrl": "https://calculator.aws/#/estimate?id=abc123",
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      }
    ]
  }
}
```

When a valid Pricing Calculator URL is provided, the system automatically calculates the MRR amount from the calculator configuration and populates both the Amount field and detailed product-level spend data in the Partner source of `AwsProductsSpendInsightsBySource`. Partners should set Amount to null when supplying an EstimationUrl - the system will calculate it automatically.

URLs in invalid formats and URLs that cannot be resolved will be rejected with a `ValidationException`.

### How Amount and EstimationUrl Work Together

You have flexibility in how you provide monthly recurring revenue (MRR) estimates for opportunities. The API intelligently handles various combinations of manual amounts and AWS Pricing Calculator URLs to ensure that your opportunities can always be created successfully.

#### Using only a manual amount

When you provide only the Amount field, the API saves your manual estimate and sets EstimationUrl to null. This approach is useful when you have a specific MRR estimate from customer conversations or your own calculations.

Example request:

```
{
    "Project": {
        "ExpectedCustomerSpend": [{
            "Amount": "25000.00",
            "CurrencyCode": "USD",
            "Frequency": "Monthly",
            "TargetCompany": "AWS"
        }]
    }
}
```

#### Using only an AWS Pricing Calculator URL

When you provide only the EstimationUrl field:

- **Valid URL** – The API calculates the MRR amount from your calculator configuration and saves both the URL and calculated amount.
- **Invalid URL** – The API returns a ValidationException with details about why the URL is invalid.

Example request:

```
{
    "Project": {
        "ExpectedCustomerSpend": [{
            "EstimationUrl": "https://calculator.aws/#/estimate?id=abc123",
            "CurrencyCode": "USD",
            "Frequency": "Monthly",
            "TargetCompany": "AWS"
        }]
    }
}
```

Example error response (invalid URL):

```
{
    "ErrorList": [{
        "Code": "INVALID_VALUE",
        "FieldName": "project.expectedCustomerSpend.estimationUrl",
        "Message": "Invalid Estimation URL: https://calculator.aws/#/estimate?id=invalid"
    }],
    "Message": "The provided Estimation URL is invalid",
    "Reason": "INVALID_VALUE"
}
```

#### Providing both Amount and EstimationUrl

When you provide both fields, the API prioritizes ensuring that your opportunity is created successfully:

1. If both values are unchanged – no update is performed on these fields
2. URL is invalid – The API saves your provided Amount and sets EstimationUrl to null, allowing your opportunity creation to proceed.
3. URL is valid and calculated amount matches your provided Amount – Both values are saved.
4. URL is valid but calculated amount doesn't match your provided Amount – The API saves your provided Amount and sets EstimationUrl to null without returning an error.

###### Note

When both values don't match existing ones, the API first attempts to calculate the amount from the URL. Your manually provided Amount always takes precedence when there's a mismatch or validation issue.

**Key benefit: Invalid URLs never block opportunity creation**

This approach ensures that invalid or inaccessible AWS Pricing Calculator URLs never prevent you from creating or updating opportunities. Your manually provided Amount always takes precedence when there's a conflict or validation issue, giving you full control over your opportunity data.

## Understanding the Extended AwsOpportunitySummary Data Model

This section describes the response structure returned by the `GetAwsOpportunitySummary` API action.

###### Note

AI-forecasted MRR is returned in `Project.ExpectedCustomerSpend[].Amount`

The `GetAwsOpportunitySummary` API action returns deal sizing insights through the new `Insights.AwsProductsSpendInsightsBySource` structure that provides comprehensive spend analysis with source attribution.

### Source Separation: AWS vs Partner Data

Deal Sizing separates insights by source to provide transparency and prevent double-counting:

- **AWS Source:** AI product recommendations from AWS
- **Partner Source:** Spend data and product details imported from partner-provided Pricing Calculator URLs

This separation enables Partners to:

1. Compare their estimates against AWS recommendations
2. Validate their sizing assumptions
3. Avoid inflating totals by accidentally combining both sources
4. Maintain visibility into data provenance

### Structure Overview

```
{
  "Insights": {
    "AwsProductsSpendInsightsBySource": {
      "<AWS | Partner>": {
        "CurrencyCode": "string",
        "Frequency": "string",
        "TotalAmount": "string",
        "TotalOptimizedAmount": "string",
        "TotalPotentialSavingsAmount": "string",
        "TotalAmountByCategory": { },
        "AwsProducts": [ ]
      }
    }
  },
  "Project": {
    "ExpectedCustomerSpend": [ ]
  },
  "RelatedEntityIds": {
    "AwsProducts": [ ]
  }
}
```

### Field Reference

#### AwsProductsSpendInsightsBySource Map

Source-separated spend insights that provide independent analysis for AWS recommendations and partner estimates.

The `Insights.AwsProductsSpendInsightsBySource` field is a map containing up to two keys:

| Key     | Type                     | Description                                                                                                      |
| ------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| AWS     | AwsProductsSpendInsights | AI-generated insights including recommended products from AWS                                                    |
| Partner | AwsProductsSpendInsights | Partner-sourced insights derived from Pricing Calculator URLs including detailed service costs and optimizations |

###### Note

Only sources with available data are included in the response. New opportunities typically start with only the AWS source populated.

#### AwsProductInsights Object

Comprehensive spend analysis for a single source (AWS or Partner) including total amounts, optimization savings, program category breakdowns, and detailed product-level insights.

Each source object contains the following fields:

| Field                       | Type   | Description                                                                                                                                                                       |
| --------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CurrencyCode                | string | ISO 4217 currency code. Supported values are "USD" and "EUR".                                                                                                                     |
| Frequency                   | string | Indicates how frequently the customer is expected to spend the projected amount. Only the value Monthly is allowed for the Frequency field, representing recurring monthly spend. |
| TotalAmount                 | string | Total estimated spend for this source before optimizations                                                                                                                        |
| TotalOptimizedAmount        | string | Total estimated spend after applying recommended optimizations                                                                                                                    |
| TotalPotentialSavingsAmount | string | Quantified savings achievable through implementing optimizations                                                                                                                  |
| TotalAmountByCategory       | object | Spend amounts mapped to AWS programs and modernization pathways                                                                                                                   |
| AwsProducts                 | array  | Product-level details including costs and optimization recommendations                                                                                                            |

**Current State Limitation:** For the AWS source, TotalAmount, TotalOptimizedAmount, and TotalPotentialSavingsAmount may be omitted when per-product spend recommendations are not available. Partners should reference `Project.ExpectedCustomerSpend[].Amount` for the total AWS MRR estimate in these cases.

#### TotalAmountByCategory Object

Maps spend amounts to AWS programs and strategic initiatives:

| Category Key                          | Description                                                           |
| ------------------------------------- | --------------------------------------------------------------------- |
| MAP Eligible                          | Spend on services eligible for Migration Acceleration Program funding |
| CAT Eligible                          | Services supporting cost allocation and tracking                      |
| Pathway<br>• Move to Cloud Native     | Services aligned with cloud-native modernization                      |
| Pathway<br>• Move to Managed Services | Services supporting managed service adoption                          |
| Pathway<br>• Move to Open Source      | Open source service alternatives                                      |
| Pathway<br>• Move to Containers       | Container-based service options                                       |
| Pathway<br>• Move to Serverless       | Serverless computing services                                         |
| Pathway<br>• Move to Databases        | Database modernization services                                       |
| Pathway<br>• Move to Analytics        | Analytics and data processing services                                |

###### Note

Total category amounts may exceed TotalAmount because individual products can belong to multiple categories.

#### AwsProducts Array

List of AWS services with program eligibility indicators (MAP, modernization pathways), cost estimates, and optimization recommendations.

Each product object contains:

| Field                  | Type   | Required | Description                                                                                         |
| ---------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------- |
| ProductCode            | string | Yes      | AWS Partner Central product identifier used for opportunity association                             |
| ServiceCode            | string | No       | Pricing Calculator service code (links to original calculator URL)                                  |
| Categories             | array  | Yes      | List of program and pathway categories this product is eligible for                                 |
| Amount                 | string | No       | Baseline service cost before optimizations (may be null for AWS-sourced recommendations)            |
| OptimizedAmount        | string | No       | Service cost after applying optimizations (may be null for AWS-sourced recommendations)             |
| PotentialSavingsAmount | string | No       | Service-specific cost reduction through optimizations (may be null for AWS-sourced recommendations) |
| Optimizations          | array  | No       | List of specific optimization recommendations for this product                                      |

**Null Handling:** For AWS-sourced products, Amount, OptimizedAmount, and PotentialSavingsAmount fields may be null when per-product spend recommendations are not available. The system provides total MRR via `Project.ExpectedCustomerSpend[0].Amount` instead.

#### Optimization Object

Each optimization recommendation contains:

| Field         | Type   | Description                                                          |
| ------------- | ------ | -------------------------------------------------------------------- |
| Description   | string | Human-readable explanation of the optimization strategy              |
| SavingsAmount | string | Quantified cost savings achievable by implementing this optimization |

### Examples

#### Example 1: AWS recommendations Only (Current State)

This example shows the typical response when only AI recommendations are available and per-product spend amounts cannot yet be recommended.

```
{
  "Catalog": "AWS",
  "Insights": {
    "AwsProductsSpendInsightsBySource": {
      "AWS": {
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "AwsProducts": [
          {
            "ProductCode": "AmazonEC2",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          },
          {
            "ProductCode": "AWSLambda",
            "Categories": ["Cost Allocation Tagging", "Pathway - Move to Cloud Native"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          },
          {
            "ProductCode": "AmazonRDS",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging", "Pathway - Move to Managed Services"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          }
        ]
      }
    }
  },
  "Project": {
    "ExpectedCustomerSpend": [
      {
        "Amount": "28000.00",
        "CurrencyCode": "USD",
        "EstimationUrl": null,
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      }
    ]
  },
  "RelatedEntityIds": {
    "AwsProducts": [
      "AmazonEC2",
      "AWSLambda",
      "AmazonRDS"
    ]
  }
}
```

**Key Points:** AWS source shows recommended products with categories but no per-product amounts. Total MRR estimate available via `Project.ExpectedCustomerSpend[].Amount`.

#### Example 2: Partner Pricing Calculator Import

This example shows enhanced insights when a partner has provided a valid Pricing Calculator URL.

```
{
  "Catalog": "AWS",
  "Insights": {
    "AwsProductsSpendInsightsBySource": {
      "Partner": {
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "TotalAmount": "32500.00",
        "TotalOptimizedAmount": "30000.00",
        "TotalPotentialSavingsAmount": "2500.00",
        "TotalAmountByCategory": {
          "MAP Eligible": "22500.00",
          "Cost Allocation Tagging": "32500.00",
          "Pathway - Move to Cloud Native": "5000.00",
          "Pathway - Move to Managed Services": "7500.00"
        },
        "AwsProducts": [
          {
            "ServiceCode": "ec2",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": "15000.00",
            "OptimizedAmount": "13500.00",
            "PotentialSavingsAmount": "1500.00",
            "Optimizations": [
              {
                "Description": "Convert to 3-year reserved instances",
                "SavingsAmount": "1000.00"
              },
              {
                "Description": "Migrate to Graviton-based instances",
                "SavingsAmount": "500.00"
              }
            ]
          },
          {
            "ServiceCode": "lambda",
            "Categories": ["Cost Allocation Tagging", "Pathway - Move to Cloud Native"],
            "Amount": "5000.00",
            "OptimizedAmount": "5000.00",
            "PotentialSavingsAmount": "0.00",
            "Optimizations": []
          },
          {
            "ServiceCode": "AmazonRDS",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging", "Pathway - Move to Managed Services"],
            "Amount": "7500.00",
            "OptimizedAmount": "6500.00",
            "PotentialSavingsAmount": "1000.00",
            "Optimizations": [
              {
                "Description": "Optimize Multi-AZ for dev/test environments",
                "SavingsAmount": "1000.00"
              }
            ]
          },
          {
            "ServiceCode": "AmazonS3",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": "5000.00",
            "OptimizedAmount": "5000.00",
            "PotentialSavingsAmount": "0.00",
            "Optimizations": []
          }
        ]
      }
    }
  },
  "Project": {
    "ExpectedCustomerSpend": [
      {
        "Amount": "32500.00",
        "CurrencyCode": "USD",
        "EstimationUrl": "https://calculator.aws/#/estimate?id=abc123",
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      }
    ]
  },
  "RelatedEntityIds": {
    "AwsProducts": []
  }
}
```

**Key Points:** Partner source contains complete spend details with per-product amounts. Optimization recommendations provide actionable cost reduction strategies. Category breakdowns show MAP eligibility ($22,500 of $32,500 total). Products include ServiceCode linking back to Pricing Calculator configuration.

#### Example 3: Both Sources Present (Comparison Scenario)

This example demonstrates how both AWS recommendations and partner estimates appear together, enabling comparison.

```
{
  "Catalog": "AWS",
  "Insights": {
    "AwsProductsSpendInsightsBySource": {
      "AWS": {
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "AwsProducts": [
          {
            "ProductCode": "AmazonEC2",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          },
          {
            "ProductCode": "AWSLambda",
            "Categories": ["Cost Allocation Tagging", "Pathway - Move to Cloud Native"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          },
          {
            "ProductCode": "EBS",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          },
          {
            "ProductCode": "RDS",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging", "Pathway - Move to Managed Services"],
            "Amount": null,
            "OptimizedAmount": null,
            "PotentialSavingsAmount": null,
            "Optimizations": []
          }
        ]
      },
      "Partner": {
        "CurrencyCode": "USD",
        "Frequency": "Monthly",
        "TotalAmount": "32500.00",
        "TotalOptimizedAmount": "30000.00",
        "TotalPotentialSavingsAmount": "2500.00",
        "TotalAmountByCategory": {
          "MAP Eligible": "22500.00",
          "Cost Allocation Tagging": "32500.00",
          "Pathway - Move to Cloud Native": "5000.00",
          "Pathway - Move to Managed Services": "7500.00"
        },
        "AwsProducts": [
          {
            "ServiceCode": "ec2",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": "15000.00",
            "OptimizedAmount": "13500.00",
            "PotentialSavingsAmount": "1500.00",
            "Optimizations": [
              {
                "Description": "Convert to 3-year reserved instances",
                "SavingsAmount": "1000.00"
              }
            ]
          },
          {
            "ServiceCode": "lambda",
            "Categories": ["Cost Allocation Tagging", "Pathway - Move to Cloud Native"],
            "Amount": "5000.00",
            "OptimizedAmount": "5000.00",
            "PotentialSavingsAmount": "0.00",
            "Optimizations": []
          },
          {
            "ServiceCode": "amazonRDS",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging", "Pathway - Move to Managed Services"],
            "Amount": "7500.00",
            "OptimizedAmount": "6500.00",
            "PotentialSavingsAmount": "1000.00",
            "Optimizations": [
              {
                "Description": "Optimize Multi-AZ for dev/test environments",
                "SavingsAmount": "1000.00"
              }
            ]
          },
          {
            "ServiceCode": "amazonS3",
            "Categories": ["MAP Eligible", "Cost Allocation Tagging"],
            "Amount": "5000.00",
            "OptimizedAmount": "5000.00",
            "PotentialSavingsAmount": "0.00",
            "Optimizations": []
          }
        ]
      }
    }
  },
  "Project": {
    "ExpectedCustomerSpend": [
      {
        "Amount": "28000.00",
        "CurrencyCode": "USD",
        "EstimationUrl": "https://calculator.aws/#/estimate?id=abc123",
        "Frequency": "Monthly",
        "TargetCompany": "AWS"
      }
    ]
  },
  "RelatedEntityIds": {
    "AwsProducts": [
      "AmazonEC2",
      "AWSLambda",
      "EBS",
      "RDS"
    ]
  }
}
```

**Key Points:** Both sources present: AWS recommendations ($28K total) and Partner calculator ($32.5K total). AWS recommendations show 4 products; Partner calculator shows 4 products (3 overlapping). Partners can compare AWS recommendations against their detailed estimates. AWS total available via `Project.ExpectedCustomerSpend[].Amount`.

### Best Practices

#### Handling Null Values

1. **EstimationUrl Field:** Expect EstimationUrl to be null for most Partners. This is standard behavior and should not be treated as an error. Display manual MRR entry options as the primary path.
2. **Missing Categories:** If TotalAmountByCategory is not present for the AWS source, this indicates per-product recommendations are not available. Category breakdowns are available for Partner-sourced data when Pricing Calculator URLs are provided.

#### Optimization Recommendations

1. **Display Actionable Insights:** Show optimization descriptions and savings amounts prominently to help Partners understand cost reduction opportunities.
2. **Aggregate Savings:** Sum PotentialSavingsAmount across products to show total optimization potential.
3. **Prioritize by Impact:** Sort optimizations by SavingsAmount to help Partners focus on highest-impact recommendations.

#### Monitoring for Updates

1. **Poll Periodically:** Poll `GetAwsOpportunitySummary` periodically (recommended: every 5 minutes) during opportunity creation workflows.
2. **Handle Async Generation:** Deal Sizing insights may not be immediately available after opportunity creation. Implement appropriate loading states and retry logic.

#### API Integration Patterns

1. **Leverage Existing Integrations:** Partners already calling `GetAwsOpportunitySummary` only need to consume additional fields in the response—no new API calls required.
2. **Graceful Degradation:** Design UIs to handle scenarios where Deal Sizing data is not yet available or incomplete.

#### Data Quality and Accuracy

1. **Validate Pricing Calculator URLs:** Ensure URLs are valid before submission to avoid null EstimationUrl responses.
2. **Provide Rich Opportunity Details:** More complete opportunity information (customer details, project description, technical requirements) yields more accurate AI recommendations.
3. **Review Variance:** When partner estimates differ significantly from AWS recommendations, review opportunity details to ensure all relevant context is captured.
