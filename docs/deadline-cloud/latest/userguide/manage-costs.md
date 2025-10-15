# Track spending and usage for Deadline Cloud farms

The AWS Deadline Cloud budget manager and usage explorer are cost management tools that provide the
 approximate cost of using Deadline Cloud based on available information about cost variables. The
 cost management tools don't guarantee the amount owed for your actual use of Deadline Cloud and other
 AWS services.

To help you manage costs for Deadline Cloud, you can use the following features:


* **Budget manager** – With the Deadline Cloud budget
 manager, you can create and edit budgets to help manage project costs.
* **Usage explorer** – With the Deadline Cloud usage
 explorer, you can view how many AWS resources are used and the estimated costs for
 those resources.
* **AWS cost allocation tags** – With cost
 allocation tags, you can track detailed costs for all of your AWS services. For
 more information, see [Organizing and
 tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html").

## Cost assumptions


The basic calculation used by the Deadline Cloud cost management tools is:



```
Cost per job =
    (CMF run time x CMF compute rate) +
    (SMF run time x SMF compute rate) +
    (License run time x license rate)
```


* *Run time* is the sum of all tasks in a job, from start
 time to end time.
* *Compute rate* is determined by the [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/") for
 service-managed fleets. For customer-managed fleets, the compute rate is
 estimated to be $1 per worker hour.
* *License rate* is determined by the Deadline Cloud base license
 price and is only available for service-managed fleets. Additional tiers are not
 included. For more information about license pricing, see [AWS Deadline Cloud
 pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

The cost estimate from the Deadline Cloud cost management tools may vary from your actual costs
 for a number of reasons. Common reasons include:



* *Customer owned resources and their pricing*. You can
 choose to bring your own resources, either from AWS or externally from
 on-premises or other cloud providers. Actual costs of these resources are not
 calculated.
* *Idle worker costs*. Idle worker costs are not included
 when the worker status is IDLE. This can happen for fleets with a minimum
 instance count greater than zero, or when workers transition between jobs. Idle
 worker cost are not included in calculations.
* *Worker stop and start time*. After workers complete a
 job, the cost for moving from IDLE to STOPPING and from STOPPING to STOPPED is
 not included in Deadline Cloud cost estimates.
* *Promotional credits, discounts, and custom pricing
 agreements*. The cost management tools don't account for
 promotional credits, private pricing agreements, or other discounts. You may be
 eligible for other discounts that are not part of the estimate.
* *Asset storage*. Asset storage is not included in the
 cost and usage estimates.
* *Changes in price*. AWS offers pay-as-you-go pricing
 for most services. Prices may change over time. The cost management tools use
 the most up-to-date prices publicly available, but there may be delays after
 changes.
* *Taxes*. The cost management tools don't include taxes
 applied to our purchase of the service.
* *Rounding*. The cost management tool perform mathematical
 rounding of pricing data.
* *Currency*. Cost estimates are made in U.S. dollars.
 Global exchange rates vary over time. If you translate estimates to a different
 currency base on the current exchange, changes in the exchange rate affect the
 estimate.
* *Outside licensing*. If you choose to use pre-purchased
 licences ([Software licensing for service-managed fleets](smf-licensing.md "smf-licensing.md")), Deadline Cloud
 cost management tools can't account for this cost.
