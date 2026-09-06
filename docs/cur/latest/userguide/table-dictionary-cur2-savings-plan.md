

# Savings plan columns
<a name="table-dictionary-cur2-savings-plan"></a>

Saving Plan columns contain data about savings plans that apply to the line item.



| Column name | Description | Data type | 
| --- | --- | --- | 
| savings\_plan\_amortized\_upfront\_commitment\_for\_billing\_period | The amount of upfront fee a Savings Plan subscription is costing you for the billing period. The initial upfront payment for **All Upfront Savings Plan** and **Partial Upfront Savings Plan** amortized over the current month. For **No Upfront Savings Plan**, the value is `0`. | double | 
| savings\_plan\_end\_time | The expiration date for the Savings Plan agreement. | string | 
| savings\_plan\_instance\_type\_family | The instance family that is associated with the specified usage. | string | 
| savings\_plan\_net\_amortized\_upfront\_commitment\_for\_billing\_period | The cost of a Savings Plan subscription upfront fee for the billing period. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| savings\_plan\_net\_recurring\_commitment\_for\_billing\_period | The net unblended cost of the Savings Plan fee. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| savings\_plan\_net\_savings\_plan\_effective\_cost | The effective cost for Savings Plans, which is your usage divided by the fees. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| savings\_plan\_offering\_type | Describes the type of Savings Plan purchased. | string | 
| savings\_plan\_payment\_option | The payment options available for your Savings Plan. | string | 
| savings\_plan\_purchase\_term | Describes the duration, or term, of the Savings Plan. | string | 
| savings\_plan\_recurring\_commitment\_for\_billing\_period | The monthly recurring fee for your Savings Plan subscriptions. For example, the recurring monthly fee for a **Partial Upfront Savings Plan** or **No Upfront Savings Plan**. | double | 
| savings\_plan\_region | The AWS Region (geographic area) that hosts your AWS services. You can use this field to analyze spend across a particular AWS Region. | string | 
| savings\_plan\_savings\_plan\_a\_r\_n | The unique Savings Plan identifier. | string | 
| savings\_plan\_savings\_plan\_effective\_cost | The proportion of the Savings Plan monthly commitment amount (upfront and recurring) that is allocated to each usage line. | double | 
| savings\_plan\_savings\_plan\_rate | The Savings Plan rate for the usage. | double | 
| savings\_plan\_start\_time | The start date of the Savings Plan agreement. | string | 
| savings\_plan\_total\_commitment\_to\_date | The total amortized upfront commitment and recurring commitment to date, for that hour. | double | 
| savings\_plan\_used\_commitment | The total dollar amount of the Savings Plan commitment used. (SavingsPlanRate multiplied by usage) | double | 