# Reserved Instances in Amazon OpenSearch Service

Reserved Instances (RIs) in Amazon OpenSearch Service offer significant discounts compared to standard
On-Demand Instances. The instances themselves are identical; RIs are just a billing discount
applied to On-Demand Instances in your account. For long-lived applications with predictable
usage, RIs can provide considerable savings over time.

OpenSearch Service RIs require one- or three-year terms and have three payment options that affect the
discount rate:

- **No Upfront** – You pay nothing upfront. You
  pay a discounted hourly rate for every hour within the term.
- **Partial Upfront** – You pay a portion of the
  cost upfront, and you pay a discounted hourly rate for every hour within the
  term.
- **All Upfront** – You pay the entirety of the
  cost upfront. You don't pay an hourly rate for the term.
  Generally speaking, a larger upfront payment means a larger discount. You can't cancel
  Reserved Instances—when you reserve them, you commit to paying for the entire
  term—and upfront payments are nonrefundable.

RIs are not flexible; they only apply to the exact instance type that you reserve. For
example, a reservation for eight `c5.2xlarge.search` instances does not apply to
sixteen `c5.xlarge.search` instances or four `c5.4xlarge.search`
instances. However, linked accounts that are part of an organization in AWS Organizations can benefit
from any unused discount application from the owning account of the RI as long as the
instance types, Region, family, and size match. For more information, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/elasticsearch-service/pricing/ "https://aws.amazon.com/elasticsearch-service/pricing/") and
[FAQ](https://aws.amazon.com/elasticsearch-service/faqs/ "https://aws.amazon.com/elasticsearch-service/faqs/").

## Examining costs

Cost Explorer is a free tool that you can use to view your spending data for the past
13 months. Analyzing this data helps you identify trends and understand if RIs fit your
use case. If you already have RIs, you can [group by](../../../awsaccountbilling/latest/aboutv2/groupdata.md "../../../awsaccountbilling/latest/aboutv2/groupdata.md")
**Purchase Option** and [show
amortized costs](../../../awsaccountbilling/latest/aboutv2/advanced.md "../../../awsaccountbilling/latest/aboutv2/advanced.md") to compare that spending to your spending for On-Demand
Instances. You can also set [usage
budgets](../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md "../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md") to make sure you are taking full advantage of your reservations. For
more information, see [Analyzing
Your Costs with Cost Explorer](../../../awsaccountbilling/latest/aboutv2/cost-explorer-what-is.md "../../../awsaccountbilling/latest/aboutv2/cost-explorer-what-is.md") in the _AWS Billing User Guide_.
