# Savings Plans details

The **SavingsPlan** columns in AWS Cost and Usage Reports provide details
about the Savings Plans. For more information about Savings Plans, see [What are Savings
Plans?](../../../savingsplans/latest/userguide/what-is-savings-plans.md "../../../savingsplans/latest/userguide/what-is-savings-plans.md") in the _Savings Plans User Guide_.

[A](#sp-A "#sp-A") | B | C | D | [E](#sp-E "#sp-E") | F | G | H | [I](#sp-I "#sp-I") | J | K | L | M | [N](#sp-N "#sp-N") | [O](#sp-O "#sp-O") |
[P](#sp-P "#sp-P") | Q | [R](#sp-R "#sp-R") | [S](#sp-S "#sp-S") |
[T](#sp-T "#sp-T") | [U](#sp-U "#sp-U") | VWXYZ

## A

### savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod

- **Description:** The amount of upfront
  fee a Savings Plans subscription is costing you for the billing period.
  The initial upfront payment for **All Upfront
  Savings Plans** and **Partial Upfront
  Savings Plans** amortized over the current month. For
  **No Upfront Savings Plans**, the value is

0.

- **Line items applicable:**
  SavingsPlanRecurringFee
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## E

### savingsPlan/EndTime

- **Description:** The expiration date for
  the Savings Plans agreement.
- **Line items applicable:**
  SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee,
  SavingsPlanRecurringFee
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## I

### savingsPlan/InstanceTypeFamily

- **Description:** The instance family that
  is associated with the specified usage.
- **Line items applicable:**
  SavingsPlanCoveredUsage
- **Sample values:**
  `m4`, `g2`
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## N

### savingsPlan/NetAmortizedUpfrontCommitmentForBillingPeriod

The cost of a Savings Plans subscription upfront fee for the billing period.
This column is included in your report only when your account has a discount in
the applicable billing period.

### savingsPlan/NetRecurringCommitmentForBillingPeriod

The net unblended cost of the Savings Plans fee. This column is included in
your report only when your account has a discount in the applicable billing
period.

### savingsPlan/NetSavingsPlanEffectiveCost

The effective cost for Savings Plans, which is your usage divided by the fees. This
column is included in your report only when your account has a discount in the
applicable billing period.

## O

### savingsPlan/OfferingType

- **Description:** Describes the type of
  Savings Plans purchased.
- **Line items applicable:**
  SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee,
  SavingsPlanRecurringFee
- **Sample values:**
  `ComputeSavingsPlans`, `EC2InstanceSavingsPlans`,
  `SageMakerSavingsPlans`
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## P

### savingsPlan/PaymentOption

- **Description:** The payment options
  available for your Savings Plans.
- **Line items applicable:**
  SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee,
  SavingsPlanRecurringFee
- **Sample values:**
  `Partial Upfront`, `All Upfront`, `No
 Upfront`
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

### savingsPlan/PurchaseTerm

- **Description:** Describes the duration,
  or term, of the Savings Plans.
- **Line items applicable:**
  SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee,
  SavingsPlanRecurringFee
- **Sample values:**
  `1yr`, `3yr`
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## R

### savingsPlan/RecurringCommitmentForBillingPeriod

- **Description:** The monthly recurring
  fee for your Savings Plans subscriptions. For example, the recurring
  monthly fee for a **Partial Upfront Savings Plans** or
  **No Upfront Savings Plans**.
- **Line items applicable:**
  SavingsPlanRecurringFee
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

### savingsPlan/Region

- **Description:** The AWS Region
  (geographic area) that hosts your AWS services. You can use this field
  to analyze spend across a particular AWS Region.
- **Line items applicable:**
  SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee,
  SavingsPlanRecurringFee
- **Sample values:**
  `US East (N. Virginia)`, `US West (N. California)`,
  `US East (Ohio)`, `Asia Pacific (Mumbai)`,
  `Europe (Ireland)`
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## S

### savingsPlan/SavingsPlanArn

- **Description:** The unique Savings Plans
  identifier.
- **Line items applicable:**
  SavingsPlanUpfrontFee
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

### savingsPlan/SavingsPlanEffectiveCost

- **Description:** The proportion of the
  Savings Plans monthly commitment amount (upfront and recurring) that is
  allocated to each usage line.
- **Line items applicable:**
  SavingsPlanCoveredUsage
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

### savingsPlan/SavingsPlanRate

- **Description:** The Savings Plans rate
  for the usage.
- **Line items applicable:**
  SavingsPlanCoveredUsage
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

### savingsPlan/StartTime

- **Description:** The start date of the
  Savings Plans agreement.
- **Line items applicable:**
  SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee,
  SavingsPlanRecurringFee
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## T

### savingsPlan/TotalCommitmentToDate

- **Description:** The total amortized
  upfront commitment and recurring commitment to date, for that
  hour.
- **Line items applicable:**
  SavingsPlanRecurringFee
- **Services:**
  - Amazon EC2
  - Fargate
  - AWS Lambda
  - Amazon SageMaker AI

## U

### savingsPlan/UsedCommitment

- **Description:** The total dollar amount
  of the Savings Plans commitment used. (SavingsPlanRate multiplied by
  usage)
- **Line items applicable:**
  SavingsPlanRecurringFee
- **Services:**
  - Amazon EC2
  - AWS Lambda
  - Fargate
  - Amazon SageMaker AI
