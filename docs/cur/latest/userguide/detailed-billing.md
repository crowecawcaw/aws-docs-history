# Using Detailed Billing Reports

###### Important

The Detailed Billing Reports feature is unavailable for new customers as of July
8, 2019.

Detailed Billing Reports (DBR) contain similar information to AWS Cost and Usage Reports (AWS CUR)
regarding your charges, but calculates the individual line items differently. If you've
signed up for both the DBR and AWS CUR, the line items don't match. However, when the
reports are finalized at the end of the month, the total cost will align.

AWS stores DBR in Amazon S3 as CSV files using the following naming convention:

```
`AWS account number`-aws-billing-detailed-line-items-`yyyy`-`mm`.csv.zip
```

AWS recreates Detailed Billing Reports (DBR) multiple times a day, overwriting the
reports. When AWS overwrites reports, line items might be in a different order than
they were in previous reports. A final report is created at the end of the month. For
the next month, AWS creates a new report file instead of overwriting the final report
from the previous month. Reports for previous months remain in your S3 bucket until you
delete them.

For information on how to migrate your DBR to AWS CUR, see [Migrating from Detailed Billing Reports to
Cost and Usage Reports](detailed-billing-migrate.md "detailed-billing-migrate.md").
