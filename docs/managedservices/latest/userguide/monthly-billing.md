

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Billing report (monthly)
<a name="monthly-billing"></a>

## Billing charges details
<a name="billing-charges-details"></a>

This report provides details about AMS billing charges with linked accounts and respective AWS services.

**This report provides:**
+ Data on AMS service-level charges, uplift percentages, account-level AMS service tiers and AMS fees.
+ Data on linked accounts and AWS usage charges.

**Important**  
The Monthly Billing report is only available in your Management Payer Account (MPA) or your defined Charge Account. These are the accounts where your AMS monthly bill is sent. If you're unable to locate these accounts, then contact your Cloud Service Delivery Manager (CSDM) for assistance.


| **Field Name** | **Dataset Field Name** | **Definition** | 
| --- | --- | --- | 
| Billing Date | date | The month and year of the service billed | 
| Payer Account Id | payer\_account\_id | The 12 digit ID identifying the account responsible for paying the AMS charges | 
| Linked Account Id | linked\_account\_id | The 12 digit ID identifying the AMS account that consumes services that generates expanses  | 
| AWS Service Name | product\_name | The AWS service that was used | 
| AWS Charges | aws\_charges | The AWS charges for the AWS service name in AWS Service Name | 
| Pricing Plan | pricing\_plan | The pricing plan associated with the linked account | 
| AMS Service Group  | tier\_uplifting\_groups  | AMS service group code that determines uplift percentage  | 
| Uplift Proportion | uplift\_percent | The uplift percentage (as a decimal V.WXYZ) based on pricing\_plan, SLA, and AWS service | 
| Adjusted AWS Charges | adjusted\_aws\_usage | AWS usage adjusted for AMS | 
| Uplifted AWS Charges | uplifted\_aws\_charges | The percentage of AWS charges to be charged for AMS; adjusted\_aws\_charges \* uplift\_percent | 
| Instances EC2 RDS Spend | instances\_ec2\_rds\_spend | Spend on EC2 and RDS instances | 
| Reserved Instance Charges | ris\_charges | Reserved instance charges | 
| Uplifted Reserved Instance Charges | uplifted\_ris | The percentage of reserved instance charges to becharged for AMS; ris\_charges \* uplift\_percent | 
| Savings Plan Charges | sp\_charges | SavingsPlan usage charges | 
| Uplifted Savings Plan Charges | uplifted\_sp | The percentage of savings plans charges to be chargedfor AMS; sp\_charges \* uplift\_percent | 
| AMS Charges | ams\_charges | Total ams charges for the product; uplifted\_aws\_charges \+ instance\_ec2\_rds\_spend \+ uplifted\_ris \+ uplifted\_sp | 
| Prorated Minimum Fee | prorated\_minimum | The amount we charge to meet the contractual minimum | 
| Linked Account Total AMS Charges | linked\_account\_total<br />ams\_charges | Sum of all charges for the linked\_account | 
| Payer Account Total AMS Charges | payer\_account\_total<br />ams\_charges | Sum of all charges for payer account | 
| Minimum Fee | minimum\_fees | AMS Minimum Fees (if applicable) | 
| Reserved Instance and Savings Plan discount | adj\_ri\_sp\_charges | RI/SP discount to be applied against RI/SP charges (applicable under certain circumstances) | 