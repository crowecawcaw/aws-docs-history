# Accessing reservation recommendations

If you enable Cost Explorer, you automatically get Amazon EC2, Amazon RDS, ElastiCache, OpenSearch Service, Amazon Redshift, Amazon
MemoryDB, and Amazon DynamoDB purchase recommendations that could help reduce your costs.
Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand or
provisioned capacity pricing. Cost Explorer generates your reservation recommendations
using the following process:

- Identifies your On-Demand instance or provisioned capacity usage for a service during a
  specific time period
- Collects your usage into categories that are eligible for a reservation
- Simulates every combination of reservation in each category of usage
- Identifies the best number of each type of reservation to purchase to maximize your
  estimated savings
  For example, Cost Explorer automatically aggregates your Amazon EC2 Linux, shared tenancy, and
  c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional RIs
  to apply to the c4 family usage. Cost Explorer recommends the smallest size instance in an
  instance family. This makes it easier to purchase a size-flexible RI. Cost Explorer also
  shows the equal number of normalized units so that you can purchase any instance size that
  you want. For this example, your RI recommendation would be for `c4.large`
  because that is the smallest size instance in the c4 instance family.

Cost Explorer recommendations are based on a single account or organization usage of the
past seven, 30, or 60 days. Cost Explorer uses On-Demand instance usage during the selected
look-back period to generate recommendations. All other usage in the look-back period that
are covered by features such as RI, SPOT, and Savings Plans aren't included. Amazon EC2, ElastiCache, OpenSearch Service,
Amazon Redshift, Amazon MemoryDB, and Amazon DynamoDB recommendations are for reservations scoped to Region,
not Availability Zones, and your estimated savings reflects the application of those
reservations to your usage. Amazon RDS recommendations are scoped to either Single-AZ or Multi-AZ
RIs. Cost Explorer updates your recommendations at least once every 24 hours.

###### Note

Cost Explorer doesn't forecast your usage or take forecasts into account when recommending
reservations. Instead, Cost Explorer assumes that your historical usage reflects your
future usage when determining which reservations to recommend.

Linked accounts can only see recommendations if they have the relevant permissions. Linked
accounts need permissions to view Cost Explorer and permissions to view recommendations.
For more information, see [Viewing reservation recommendations](#viewing-rex "#viewing-rex").

###### Topics

- [RI recommendations for size-flexible RIs](#rex-flex "#rex-flex")
- [Viewing reservation recommendations](#viewing-rex "#viewing-rex")
- [Understanding reservation recommendations](#reading-rex "#reading-rex")
- [Modifying reservation recommendations](#modifying-rex "#modifying-rex")
- [Saving reservation recommendations](#saving-rex "#saving-rex")
- [Using reservation recommendations](#using-rex "#using-rex")

## RI recommendations for size-flexible RIs

Cost Explorer also considers the benefits of size-flexible regional RIs when generating
your RI purchase recommendations. Size-flexible regional RIs help maximize your
estimated savings across eligible instance families in your recommendations. AWS uses
the concept of normalized units to compare the various sizes within an instance family.
Cost Explorer uses the smallest normalization factor to represent the instance type
that it recommends. For more information, see [Instance size flexibility](../../../AWSEC2/latest/UserGuide/apply_ri.md#ri-instance-size-flexibility "../../../AWSEC2/latest/UserGuide/apply_ri.md#ri-instance-size-flexibility") in the _Amazon Elastic Compute Cloud User
Guide_.

For example, let’s say you own an EC2 RI for a `c4.8xlarge`. This RI
applies to any usage of a `Linux/Unix c4` instance with shared tenancy in the
same region as the RI, such as the following instances:

- One `c4.8xlarge` instance
- Two `c4.4xlarge` instances
- Four `c4.2xlarge` instances
- Sixteen `c4.large` instances

It also includes combinations of EC2 usage, such as one `c4.4xlarge` and
eight `c4.large` instances.

If you own an RI that is smaller than the instance that you're running, you are charged the
prorated, On-Demand price for the excess. This means that you could buy an RI for a
`c4.4xlarge`, use a `c4.4xlarge` instance most of the time,
but occasionally scale up to a `c4.8xlarge` instance. Some of your
`c4.8xlarge` usage is covered by the purchased RI, and the rest is
charged at On-Demand prices. For more information, see [How Reserved
Instance discounts are applied](../../../AWSEC2/latest/UserGuide/apply_ri.md "../../../AWSEC2/latest/UserGuide/apply_ri.md") in the _Amazon Elastic Compute Cloud User
Guide_.

## Viewing reservation recommendations

Linked accounts need the following permissions to view recommendations:

- `ViewBilling`
- `ViewAccount`

For more information, see [Using identity-based policies (IAM policies) for AWS Cost Management](billing-permissions-ref.md "billing-permissions-ref.md").

###### To view your reservation recommendations

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Reservations**, choose **Recommendations**.
3. On the **Recommendations** page, under **Recommendation
   parameters**, choose the **Service** that you want
   recommendations for.

## Understanding reservation recommendations

The **Reservations Recommendations** page shows you your estimated
potential savings, your reservation purchase recommendations, and the parameters that
Cost Explorer used to create your recommendations. You can change the parameters to get
recommendations that might match your use case more closely.

The **Recommendations** page shows you the following three numbers:

- **Total purchase recommendations** – The
  number of different reservation purchase options Cost Explorer has found for
  you.
- **Estimated monthly savings** – How much Cost Explorer
  calculates you could save by purchasing the recommended reservations.
- **Estimated savings vs. On-Demand rates** – Your
  estimated savings as a percentage of your current costs.

These numbers provide you with a rough estimate of how much you could potentially save by
buying more reservations. You can recalculate these numbers for a different use case
using the following **Recommendation parameters**:

- **Term** – The duration for which you want
  recommendations.
- **Offering class** – Whether you want recommendations
  for a standard or convertible reservation.
- **Payment option** – Whether you want to pay for
  recommendations upfront.
- **Based on the past** – The number of days of previous
  usage that you want your recommendations to take into account.

At the bottom of the page are tabs with some of your savings estimates. The **All accounts** tab enables you to see the recommendations based on the combined usage across your entire organization, and the **Individual accounts** tab enables you to see recommendations that Cost Explorer generated on a per-linked-account basis. The table on each tab shows the different purchase recommendations and details about the recommendations. If you want to see the usage that Cost Explorer based a recommendation on, choose the **View associated usage** link in the recommendation details. This takes you to a report that shows the exact parameters that Cost Explorer used to generate your recommendation. The report also shows your costs and associated usage grouped by **Purchase option**, so that you can view the On-Demand Instance usage that your recommendation is based on.

###### Note

Recommendations that Cost Explorer bases on an individual linked account consider all usage by that linked account, including any RIs used by that linked account. This includes RIs shared by another linked account. The recommendations don't assume that an RI will be shared with the linked account in the future.

You can sort your recommendations by **Monthly estimated savings**, **Upfront RI cost**, **Purchase recommendation**, or **Instance type**.

## Modifying reservation recommendations

You can change the information that Cost Explorer uses when it creates your
recommendations, and you can also change the types of recommendations that you want.
This allows you to see recommendations for the reservations that work best for you, such
as All upfront reservations with a one-year term, based on your last 30 days of
usage.

###### Note

Instead of forecasting your future usage, Cost Explorer assumes that your future usage is
the same as your previous usage. Cost Explorer also assumes that you are renewing
any expiring reservations.

###### To modify your reservation recommendations

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Reservations**, choose
   **Recommendations**.
3. On the **Recommendations** page, under
   **Recommendation parameters**, choose the
   **Service** that you want recommendations for.
4. Choose the relevant **Term**.
5. Choose the relevant **Offering class**.
6. Choose the relevant **Payment option**.
7. For **Based on the past**, select how many days of usage that
   you want your reservation recommendations to be based on.
8. Choose either **All accounts** or **Individual accounts** to see recommendations based either on your organization-wide usage or on all of your linked accounts based on their individual account usage.

## Saving reservation recommendations

You can save reservation recommendations as a CSV file.

###### To save your reservation recommendations

1. On the **Reservations Recommendations** page, under
   **Recommendation parameters**, choose the
   **Service** that you want recommendations for and update
   any parameters you want to change.
2. Under **Recommended actions**, choose **Download
   CSV**.

The CSV file contains the following columns.

| Reservation recommendations CSV columns                                             | Column name                                                                    | Service                                                                                                                                                                                                                                                                                                                                                                | Column explanation |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Account ID                                                                          | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The account associated with your recommendation.                                                                                                                                                                                                                                                                                                                       |
| Availability zone                                                                   | Amazon RDS                                                                     | The availability zone of the instances used to generate a<br>recommendation.                                                                                                                                                                                                                                                                                           |
| Average hourly normalized unit usage in historical period                           | Amazon EC2, RDS, MemoryDB                                                      | The average number of normalized units used per hour over the period chosen for<br>generating recommendations.                                                                                                                                                                                                                                                         |
| Average hourly usage in historical period                                           | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB           | The average number of instance hours used per hour over the period chosen for<br>generating recommendations.                                                                                                                                                                                                                                                           |
| Average number of capacity units used per hour in the selected<br>historical period | Amazon DynamoDB                                                                | The average number of provisioned capacity units used per hour over<br>the period chosen for generating recommendations.                                                                                                                                                                                                                                               |
| Break even months                                                                   | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The estimated length of time before you recoup your upfront costs for this set of<br>recommended reservations.                                                                                                                                                                                                                                                         |
| Cache engine                                                                        | Amazon ElastiCache                                                             | The kind of engine that the recommended ElastiCache reserved node runs,<br>such as Redis or Memcheched.                                                                                                                                                                                                                                                                |
| Capacity unit type                                                                  | Amazon DynamoDB                                                                | The type of capacity unit for the recommendation. Read capacity units<br>are used for operations that retrieve data from a table. Write capacity<br>units are used for operations that insert, update, or delete data in a<br>table.                                                                                                                                   |
| Database edition                                                                    | Amazon RDS                                                                     | The edition of the database engine that the recommended RDS reserved<br>instance runs.                                                                                                                                                                                                                                                                                 |
| Database engine                                                                     | Amazon RDS                                                                     | The kind of engine that the recommended RDS reserved instance runs, such as Aurora<br>MySQL or MariaDB.                                                                                                                                                                                                                                                                |
| Deployment option                                                                   | Amazon RDS                                                                     | Whether your reserved instance is for an RDS instance in a single Availability Zone or<br>an RDS instance with a backup in another Availability Zone.                                                                                                                                                                                                                  |
| Estimated savings                                                                   | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The estimated savings of the recommended reservations.                                                                                                                                                                                                                                                                                                                 |
| Expected utilization                                                                | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | How much of the recommended reservations Cost Explorer estimates you will use.                                                                                                                                                                                                                                                                                         |
| Instance type                                                                       | Amazon EC2, RDS, OpenSearch Service                                            | The type of instance that the recommendation is generated for (for example,<br>`m4.large` or `t2.nano`). For size-flexible<br>recommendations, Cost Explorer aggregates all usage in a organization<br>(for example, the m4 family) and shows a recommendation for the smallest<br>reserved instance type that is available for purchase (for example,<br>`m4.large`). |
| Max hourly normalized unit usage in historical period                               | Amazon EC2, RDS, MemoryDB                                                      | The maximum number of normalized units used in an hour over the period chosen for<br>generating recommendations.                                                                                                                                                                                                                                                       |
| Max hourly usage in historical period                                               | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB           | The maximum number of instance hours used in an hour over the period chosen for<br>generating recommendations.                                                                                                                                                                                                                                                         |
| Maximum number of capacity units used per hour in the selected<br>historical period | Amazon DynamoDB                                                                | The maximum number of provisioned capacity units used in an hour over<br>the period chosen for generating recommendations.                                                                                                                                                                                                                                             |
| Min hourly normalized unit usage in historical period                               | Amazon EC2, RDS, MemoryDB                                                      | The minimum number of normalized units used in an hour over the period chosen for<br>generating recommendations.                                                                                                                                                                                                                                                       |
| Min hourly usage in historical period                                               | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB           | The minimum number of instance hours used in an hour over the period chosen for<br>generating recommendations.                                                                                                                                                                                                                                                         |
| Minimum number of capacity units used per hour in the selected<br>historical period | Amazon DynamoDB                                                                | The minimum number of provisioned capacity units used in an hour over<br>the period chosen for generating recommendations.                                                                                                                                                                                                                                             |
| Node type                                                                           | Amazon ElastiCache, Redshift, MemoryDB                                         | The type of node that the recommendation is generated for, such as<br>`ds2.xlarge`.                                                                                                                                                                                                                                                                                    |
| Normalized hours to purchase                                                        | Amazon EC2, RDS, MemoryDB                                                      | How many normalized units that Cost Explorer recommends that you buy.                                                                                                                                                                                                                                                                                                  |
| Number of instances to purchase                                                     | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB           | How many reservations Cost Explorer recommends that you buy.                                                                                                                                                                                                                                                                                                           |
| Offering class                                                                      | Amazon EC2                                                                     | The offering class associated with the recommendation.                                                                                                                                                                                                                                                                                                                 |
| Payment option                                                                      | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The recommended payment option for the recommendation.                                                                                                                                                                                                                                                                                                                 |
| Platform                                                                            | Amazon EC2                                                                     | The operating system and license model for the recommended reserved instance<br>type.                                                                                                                                                                                                                                                                                  |
| Recommended number of capacity units to purchase                                    | Amazon DynamoDB                                                                | How many reserved capacity units Cost Explorer recommends that you<br>buy.                                                                                                                                                                                                                                                                                             |
| Recommendation date                                                                 | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The date that Cost Explorer generated your recommendation.                                                                                                                                                                                                                                                                                                             |
| Recurring monthly cost                                                              | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The recurring monthly cost of the recommended reservations.                                                                                                                                                                                                                                                                                                            |
| Region                                                                              | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The Region used to generate a recommendation. You must purchase the recommended<br>reservations in the recommended Region to see potential savings.                                                                                                                                                                                                                    |
| Size flexible                                                                       | Amazon EC2, RDS, MemoryDB                                                      | Whether a recommended reservation is size-flexible.                                                                                                                                                                                                                                                                                                                    |
| Tenancy                                                                             | Amazon EC2                                                                     | The tenancy for the recommendation. Valid values are **shared\*<br>• or<br>**dedicated\*\*.                                                                                                                                                                                                                                                                            |
| Term                                                                                | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The recommended term length for the recommendation.                                                                                                                                                                                                                                                                                                                    |
| Upfront cost                                                                        | Amazon EC2, RDS, Redshift, ElastiCache, OpenSearch Service, MemoryDB, DynamoDB | The upfront cost associated with the recommendation.                                                                                                                                                                                                                                                                                                                   |

## Using reservation recommendations

To purchase the recommended reservations, go to the purchase page in a service console. You
can also save a CSV file of your recommendations and purchase the reservations at a
later date.

###### To use Amazon Elastic Compute Cloud recommendations

1. On the **Reserved Instance Recommendations** page, choose [Amazon EC2 RI Purchase Console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#ReservedInstances:sort=reservedInstancesId "https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#ReservedInstances:sort=reservedInstancesId").
2. Purchase your RIs by following the instructions at [Buy Reserved Instances
   for Amazon EC2](../../../AWSEC2/latest/UserGuide/ri-market-concepts-buying.md "../../../AWSEC2/latest/UserGuide/ri-market-concepts-buying.md") in the _Amazon Elastic Compute Cloud User Guide_.

###### To use Amazon Relational Database Service recommendations

1. On the **Reserved instances** page in the Amazon RDS console, choose
   **Purchase Reserved DB Instance**.
2. Purchase your reservations by following the instructions at [Purchasing reserved DB instances for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.md") in the
   _Amazon RDS User Guide_.

###### To use Amazon Redshift recommendations

1. On the **Reserved nodes** page in the Amazon Redshift console, choose
   **Purchase reserved nodes**.
2. Purchase your reservations by following the instructions at [Purchasing a
   reserved node](../../../redshift/latest/mgmt/purchase-reserved-node-offering-console.md "../../../redshift/latest/mgmt/purchase-reserved-node-offering-console.md") in the _Amazon Redshift Management Guide_.

###### To use Amazon OpenSearch Service recommendations

1. On the **Reserved Instance Leases** page in the OpenSearch Service console, choose
   **Order Reserved Instance**.
2. Purchase your reservations by following the instructions at [Reserved Instances in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ri.md "../../../opensearch-service/latest/developerguide/ri.md") in the
   _Amazon OpenSearch Service Developer Guide_.

###### To use Amazon ElastiCache recommendations

1. On the **Reserved Nodes** page in the ElastiCache console, choose
   **Purchase reserved nodes**.
2. Purchase your reservations by following the instructions at [Purchasing a reserved node](../../../AmazonElastiCache/latest/UserGuide/CacheNodes.md#reserved-nodes-purchasing "../../../AmazonElastiCache/latest/UserGuide/CacheNodes.md#reserved-nodes-purchasing") in the
   _Amazon ElastiCache User Guide_.

###### To use Amazon MemoryDB recommendations

1. On the **Reserved nodes** page in the MemoryDB console, choose
   **Purchase reserved nodes**.
2. Purchase your reservations by following the instructions at [Working with reserved nodes](../../../memorydb/latest/devguide/nodes.md "../../../memorydb/latest/devguide/nodes.md") in the _Amazon MemoryDB Developer
   Guide_.

###### To use Amazon DynamoDB recommendations

1. On the **Reserved capacity** page in the DynamoDB console, choose
   **Purchase reserved capacity**.
2. Purchase your reserved capacity by following the instructions at [Reserved capacity](../../../amazondynamodb/latest/developerguide/reserved-capacity.md "../../../amazondynamodb/latest/developerguide/reserved-capacity.md") in the _Amazon DynamoDB Developer
   Guide_.
