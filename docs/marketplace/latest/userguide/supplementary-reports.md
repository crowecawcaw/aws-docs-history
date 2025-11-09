# Supplementary reports

AWS Marketplace delivers supplementary reports through the [Seller delivery data feeds in AWS Marketplace](data-feed-service.md "data-feed-service.md") to seller-owned Amazon S3 accounts that are connected to the
AWS Marketplace Seller Account ID associated with the AWS Marketplace listings for sellers. For more information,
see [Create a destination Amazon Simple Storage Service bucket](data-feed-service.md#data-feed-accessing "data-feed-service.md#data-feed-accessing").

The supplementary reports are published daily at 16:00 UTC if there were new subscribers in
the day prior. These reports cover the previous day from 13:59 UTC through 16:01 UTC of the
following day.

## Agreement details report

The agreement details report helps you support the customers that are on a software as a
service (SaaS) contract free trial. The report includes agreement details such as the
subscriber name, subscriber ID, offer ID, agreement start, and agreement end date.

You only receive this report if relevant information is available. If you don't receive
this report on an occasion when you think that you should, contact the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.

You can access this report through Amazon S3 bucket associated with the AWS Marketplace Seller
Account ID.

The following table lists the column names and descriptions for the agreement details
report.

| SaaS contract free trial report data | Name                                                                                                                            | Description |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `vendor_display_name`                | The name of the vendor that sold the product.                                                                                   |
| `vendor_aws_account_id`              | The identification associated with the vendor that sold the product.                                                            |
| `subscriber_aws_account_id`          | The identification associated with the AWS account that is subscribed to the<br>product.                                        |
| `customer_id`                        | The unique identifier for the software product.                                                                                 |
| `product_title`                      | The title of the product.                                                                                                       |
| `offer_id`                           | The identifier for the offer that the buyer signed.                                                                             |
| `offer_visibility`                   | Indication of whether the offer is a public, private, or enterprise contract<br>offer.                                          |
| `reseller_name`                      | The name of the channel partner reseller.                                                                                       |
| `reseller_aws_account_id`            | The unique identifier for the channel partner reseller.                                                                         |
| `agreement_id`                       | A unique agreement data feed reference for the agreement signed between a proposer<br>and an accepter to start using a product. |
| `agreement_acceptance_date`          | The date the agreement was accepted.                                                                                            |
| `agreement_start_date`               | The start date of the agreement.                                                                                                |
| `agreement_end_date`                 | The end date of the agreement. For metered/pay as go/subscriptions, this is set to<br>1-JAN-9999.                               |
| `is_free_trial_offer`                | A flag that indicates if the offer or agreement is a free trial offer.                                                          |
| `is_upgraded_after_free_trial`       | A flag that indicates if the agreement was upgraded to a paid contract.                                                         |
| `total_contract_value`               | The total value of the contract.                                                                                                |
