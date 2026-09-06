

# Savings Plans details
<a name="savingsplans-columns"></a>

The **SavingsPlan** columns in AWS Cost and Usage Reports provide details about the Savings Plans. For more information about Savings Plans, see [What are Savings Plans?](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) in the *Savings Plans User Guide*.

 [A](#sp-A) \| B \| C \| D \| [E](#sp-E) \| F \| G \| H \| [I](#sp-I) \| J \| K \| L \| M \| [N](#sp-N) \| [O](#sp-O) \| [P](#sp-P) \| Q \| [R](#sp-R) \| [S](#sp-S) \| [T](#sp-T) \| [U](#sp-U) \| VWXYZ 

## A
<a name="savingsplans-details-A"></a>

### savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod
<a name="savingsplans-details-A-AmortizedUpfrontCommitmentForBillingPeriod"></a>
+ **Description:** The amount of upfront fee a Savings Plans subscription is costing you for the billing period. The initial upfront payment for **All Upfront Savings Plans** and **Partial Upfront Savings Plans** amortized over the current month. For **No Upfront Savings Plans**, the value is 0.
+ **Line items applicable:** SavingsPlanRecurringFee
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## E
<a name="savingsplans-details-E"></a>

### savingsPlan/EndTime
<a name="savingsplans-details-E-EndTime"></a>
+ **Description:** The expiration date for the Savings Plans agreement.
+ **Line items applicable:** SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee, SavingsPlanRecurringFee
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## I
<a name="savingsplans-details-I"></a>

### savingsPlan/InstanceTypeFamily
<a name="savingsplans-details-I-InstanceTypeFamily"></a>
+ **Description:** The instance family that is associated with the specified usage.
+ **Line items applicable:** SavingsPlanCoveredUsage
+ **Sample values:** `m4`, `g2`
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## N
<a name="savingsplans-details-N"></a>

### savingsPlan/NetAmortizedUpfrontCommitmentForBillingPeriod
<a name="savingsplans-details-N-NetAmortizedUpfrontCommitmentForBillingPeriod"></a>

The cost of a Savings Plans subscription upfront fee for the billing period. This column is included in your report only when your account has a discount in the applicable billing period.

### savingsPlan/NetRecurringCommitmentForBillingPeriod
<a name="savingsplans-details-N-NetRecurringCommitmentForBillingPeriod"></a>

The net unblended cost of the Savings Plans fee. This column is included in your report only when your account has a discount in the applicable billing period.

### savingsPlan/NetSavingsPlanEffectiveCost
<a name="savingsplans-details-N-NetSavingsPlanEffectiveCost"></a>

The effective cost for Savings Plans, which is your usage divided by the fees. This column is included in your report only when your account has a discount in the applicable billing period.

## O
<a name="savingsplans-details-O"></a>

### savingsPlan/OfferingType
<a name="savingsplans-details-O-OfferingType"></a>
+ **Description:** Describes the type of Savings Plans purchased.
+ **Line items applicable:** SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee, SavingsPlanRecurringFee
+ **Sample values:** `ComputeSavingsPlans`, `EC2InstanceSavingsPlans`, `SageMakerSavingsPlans`
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## P
<a name="savingsplans-details-P"></a>

### savingsPlan/PaymentOption
<a name="savingsplans-details-P-PaymentOption"></a>
+ **Description:** The payment options available for your Savings Plans.
+ **Line items applicable:** SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee, SavingsPlanRecurringFee
+ **Sample values:** `Partial Upfront`, `All Upfront`, `No Upfront`
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

### savingsPlan/PurchaseTerm
<a name="savingsplans-details-P-PurchaseTerm"></a>
+ **Description:** Describes the duration, or term, of the Savings Plans.
+ **Line items applicable:** SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee, SavingsPlanRecurringFee
+ **Sample values:** `1yr`, `3yr`
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## R
<a name="savingsplans-details-R"></a>

### savingsPlan/RecurringCommitmentForBillingPeriod
<a name="savingsplans-details-R-RecurringCommitmentForBillingPeriod"></a>
+ **Description:** The monthly recurring fee for your Savings Plans subscriptions. For example, the recurring monthly fee for a **Partial Upfront Savings Plans** or **No Upfront Savings Plans**.
+ **Line items applicable:** SavingsPlanRecurringFee
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

### savingsPlan/Region
<a name="savingsplans-details-R-Region"></a>
+ **Description:** The AWS Region (geographic area) that hosts your AWS services. You can use this field to analyze spend across a particular AWS Region.
+ **Line items applicable:** SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee, SavingsPlanRecurringFee
+ **Sample values:** `US East (N. Virginia)`, `US West (N. California)`, `US East (Ohio)`, `Asia Pacific (Mumbai)`, `Europe (Ireland)`
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## S
<a name="savingsplans-details-S"></a>

### savingsPlan/SavingsPlanArn
<a name="savingsplans-details-S-SavingsPlanARN"></a>
+ **Description:** The unique Savings Plans identifier.
+ **Line items applicable:** SavingsPlanUpfrontFee
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

### savingsPlan/SavingsPlanEffectiveCost
<a name="reservation-details-S-SavingsPlanEffectiveCost"></a>
+ **Description:** The proportion of the Savings Plans monthly commitment amount (upfront and recurring) that is allocated to each usage line.
+ **Line items applicable:** SavingsPlanCoveredUsage
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

### savingsPlan/SavingsPlanRate
<a name="savingsplans-details-S-SavingsPlanRate"></a>
+ **Description:** The Savings Plans rate for the usage.
+ **Line items applicable:** SavingsPlanCoveredUsage
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

### savingsPlan/StartTime
<a name="savingsplans-details-S-StartTime"></a>
+ **Description:** The start date of the Savings Plans agreement.
+ **Line items applicable:** SavingsPlanCoveredUsage, SavingsPlanNegation, SavingsPlanUpfrontFee, SavingsPlanRecurringFee
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## T
<a name="savingsplans-details-T"></a>

### savingsPlan/TotalCommitmentToDate
<a name="savingsplans-details-T-TotalCommitmenToDate"></a>
+ **Description:** The total amortized upfront commitment and recurring commitment to date, for that hour.
+ **Line items applicable:** SavingsPlanRecurringFee
+ **Services:**
  + Amazon EC2
  + Fargate
  + AWS Lambda
  + Amazon SageMaker AI

## U
<a name="savingsplans-details-U"></a>

### savingsPlan/UsedCommitment
<a name="savingsplans-details-U-UsedCommitment"></a>
+ **Description:** The total dollar amount of the Savings Plans commitment used. (SavingsPlanRate multiplied by usage)
+ **Line items applicable:** SavingsPlanRecurringFee
+ **Services:**
  + Amazon EC2
  + AWS Lambda
  + Fargate
  + Amazon SageMaker AI