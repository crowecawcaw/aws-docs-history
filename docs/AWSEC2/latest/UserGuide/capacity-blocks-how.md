# How Amazon EC2 Capacity Blocks work

You can reserve a Capacity Block with the following specifications:

- Reserve a start time up to 8 weeks in advance
- Set a reservation duration of one to 14 days or a multiple of 7 days, up to 182
  days (Examples: 21 days, 28 days)
- Configure up to 64 instances per Capacity Block
- Configure up to 256 instances across multiple Capacity Blocks
  For Amazon EC2 UltraServers, each UltraServer corresponds to one Capacity Block. You can request multiple
  UltraServers through a single request.

You can use Capacity Blocks to reserve `p6-b200`, `p5`, `p5e`,
`p5en`, `p4d`, `p4de`, `trn1`, and
`trn2` instances. You can purchase the following UltraServer types through
Capacity Blocks: `P6e-GB200` and `Trn2` (in preview).

To reserve a Capacity Block, you start by specifying your capacity needs, including the instance
type or UltraServer type, the number of instances or UltraServers, amount of time, earliest start date,
and latest end date that you need. Then, you can see an available Capacity Block offering that meets
your specifications. The Capacity Block offering includes details such as start time, Availability
Zone, and reservation price. The price of a Capacity Block offering depends on available supply and
demand at the time the offering was delivered. After you reserve a Capacity Block, the price doesn't
change. For more information, see [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md "capacity-blocks-pricing-billing.md").

When you purchase a Capacity Block offering, your reservation is created for the date and number
of instances that you selected. When your Capacity Block reservation begins, you can target
instance launches by specifying the reservation ID in your launch requests.

You can use all the instances you reserved until 30 minutes (for instance types) or 60
minutes (for UltraServer type) before the end time of the Capacity Block. With 30 minutes (for instance
types) or 60 minutes (for UltraServer types) left in your Capacity Block reservation, we begin
terminating any instances that are running in the Capacity Block. We use this time to clean up
your instances before delivering the Capacity Block to the next customer. We emit an event through
EventBridge 10 minutes before the termination process begins. For more information, see [Monitor Capacity Blocks using EventBridge](capacity-blocks-monitor.md "capacity-blocks-monitor.md").
