# AMI subscriptions in AWS Marketplace

In AWS Marketplace, some Amazon Machine Image (AMI)-based software products offer an annual
subscription pricing model. With this pricing model, you make a one-time upfront payment and pay
no hourly usage fee for the next 12 months. You can apply one annual subscription to an AWS Marketplace
software product to one Amazon Elastic Compute Cloud (Amazon EC2) instance.

###### Note

For AMI hourly with annual pricing, the annual subscription covers only the instance types
that you specify when purchasing. For example, `t3.medium`. Launching any other
instance type will incur the hourly rate for that instance type based on the active
subscription.

You can also continue to launch and run AWS Marketplace software products by using hourly pricing.
Charges for using Amazon EC2 and other services from AWS are separate and in addition to what you
pay to purchase AWS Marketplace software products.

If you change the Amazon EC2 instance type for hourly usage, your Amazon EC2 infrastructure will be
billed according to your signed savings plan. However, the AMI license from AWS Marketplace will
automatically change to hourly pricing.

If an AMI hourly product doesn't support annual pricing, the buyer can't purchase an annual
subscription. If an AMI hourly product does support annual pricing, the buyer can go to the
product's page in AWS Marketplace and purchase annual contracts. Each annual contract allows the buyer to
run one instance without being billed the hourly rate. Contracts vary according to instance
type.

## Annual agreement amendments

With hourly annual (annual) plan amendments, you can amend your plan directly from the
AWS Marketplace Management Portal. You can use amendments when you need to switch the AMI to run on an Amazon Elastic Compute Cloud
(Amazon EC2) instance type with more vCPUs, or move to a more modern generation of CPU
architecture. With amendments, you can make the following changes to your existing annual
plan:

- Switch between Amazon EC2 instance type families
- Switch between Amazon EC2 instance type sizes
- Add a new instance type
- Increase the quantity of an existing instance type in the agreement

Any new Amazon EC2 instance types you add or switch to in the agreement will be co-termed to
the current end-date of the plan, so that all instance types in the agreement are renewed at
the same time.

You can make a change as long as the prorated cost of the change is greater than zero. The
prorated cost of the newly added Amazon EC2 instances is based on the annual cost of the instance
type adjusted for the remaining term of the agreement. When switching instance types, the
prorated cost of the removed Amazon EC2 instance type is deducted from the prorated cost of the
newly added Amazon EC2 instance type.

###### Note

Amendments are supported for all agreements made from public offers and agreements from
private offers without installment plans.

### Annual agreement amendment examples

Consider the follow examples related to annual agreement amendments. In the following
examples, the customer signed a contract on January 1, 2024, for two units of m5.large
instance types ($4,000/year). The seller is paid $8,000, minus the listing fees.

###### Example 1: Switching to an instance type of equal value

Mid-year, the customer wants to switch one unit of the m5.large instance type to one
unit of the r5.large instance type. The prorated cost of the switch is calculated by
deducting the prorated cost of the instance removed (six months of m5.large - $2,000) from
the prorated cost of the instance added (six months of r5.large - $2,000). The net cost is
$0, so the amendment can occur.

###### Example 2: Switching to higher priced instance type

Mid-year, the customer wants to switch one unit of the m5.large instance type to one
unit of the m5.2xlarge instance type. The prorated cost of the switch is calculated by
deducting the prorated cost of the instance removed (six months of m5.large - $2,000) from
the prorated cost of instance added (six months of m5.2xlarge - $3,000). The net cost is
$1,000, so the amendment can occur.

###### Example 3: Switching to a single unit of a lower-priced instance type

Mid-year, the customer wants to switch one unit of the m5.large instance type to one
unit of the c5.large instance type. The prorated cost of the switch is calculated by
deducting the prorated cost of the instance removed (6 months of m5.large - $2,000) from
the prorated cost of instance added (6 months of c5.large - $1,500). The net cost is -$500
(less than $0), so the amendment can't occur.

###### Example 4: Switching to multiple units of a lower-priced instance type

Mid-year, the customer wants to switch one unit of the m5.large instance type to two
units of the c5.large instance type. The prorated cost of the switch is calculated by
deducting the prorated cost of the instance removed (six months of m5.large - $2,000) from
the prorated cost of instances added (six months of two c5.large - $3,000). The net cost
is $1,000, so the amendment can occur.

###### Example 5: Adding a new instance type

Mid-year, the customer wants to add an additional unit of the m5.large instance type
to the agreement. The prorated cost of this change is calculated as the prorated cost of
the instance added (six months of m5.large - $2,000). The net cost is $2,000, so the
amendment can occur.

###### Example 6: Removing an instance type

Mid-year, the customer wants to remove one unit of the m5.large instance type. The
prorated cost of this change is calculated as the prorated cost of instance removed (six
months of m5.large - $2,000). The net cost is -$2,000 (less than $0), so the amendment
can't occur.
