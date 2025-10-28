# About the free trial for behavior graphs

Amazon Detective provides a 30-day free trial for each account in each Region. The free trial for an account starts the first time one of the following actions occurs.

- An account enables Detective manually and becomes the administrator account for a behavior
  graph.
- An account is designated as the Detective administrator account for an organization in
  AWS Organizations, and has Detective enabled for the first time.
- If the Detective administrator account already had Detective enabled before they were
  designated, then the account does not start a new 30-day free trial.
- An account accepts an invitation to be a member account in a behavior graph and is
  enabled as a member account.
- An organization account is enabled as a member account by the Detective administrator
  account.
  The free trial lasts for 30 days from that point. The account is not billed for any data
  processed during that period. When the trial period ends, Detective begins to bill the account for
  the data it contributes to behavior graphs. For more information about how you can track your
  Detective activity, monitor usage and view the projected cost see [Forecasting and monitoring Detective costs](tracking-usage-logging.md "tracking-usage-logging.md"). For more
  information on pricing, see [Detective pricing](https://aws.amazon.com/detective/pricing/ "https://aws.amazon.com/detective/pricing/")

The same 30-day period is used for all behavior graphs in the Region. For example, an
account is enabled as a member account for a behavior graph. This starts the 30-day free trial.
After 10 days, the account is enabled for a second behavior graph in the same Region. For the
second behavior graph, the account receives 20 days of free data.

The free trial provides multiple benefits:

- Administrator accounts can explore Detective features and functionality to verify its
  value.
- Administrator and member accounts can monitor the amount of data and the estimated cost
  before Detective begins to bill them for it. See [Monitoring usage for a Detective administrator account](usage-tracking-admin.md "usage-tracking-admin.md") and
  [Monitoring usage for a Detective member account](member-usage-tracking.md "member-usage-tracking.md").

## Free trial for optional data sources

Detective also provides a free 30-day trial for optional data sources. This free trial is
separate from the free trial provided for the core Detective data sources when Detective is first
enabled.

###### Note

If a customer disables an optional data source package within 7 days of enabling it, Detective does a one-time automatic reset of the free trial for that data source package if it is enabled again.

To enable or disable an optional data source see [Types of optional data sources in Detective](detective-source-data-about.md#source-data-types-optional "detective-source-data-about.md#source-data-types-optional").
