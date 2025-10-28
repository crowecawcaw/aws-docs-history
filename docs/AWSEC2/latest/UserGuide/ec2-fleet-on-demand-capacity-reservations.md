# Use Capacity Reservations to reserve

On-Demand capacity in EC2 Fleet

With On-Demand Capacity Reservations, you can reserve compute capacity for your On-Demand Instances in a
specified Availability Zone for any duration. You can configure an EC2 Fleet to use the Capacity Reservations
first when launching On-Demand Instances.

On-Demand Capacity Reservations are available only for EC2 Fleet with the request type set to
`instant`.

Capacity Reservations are configured as either `open` or
`targeted`. EC2 Fleet can launch On-Demand Instances into either `open` or
`targeted` Capacity Reservations, as follows:

- If a Capacity Reservation is `open`, On-Demand Instances that have matching attributes
  automatically run in the reserved capacity.
- If a Capacity Reservation is `targeted`, On-Demand Instances must specifically target it to run
  in the reserved capacity. This is useful for using up specific Capacity Reservations or for
  controlling when to use specific Capacity Reservations.
  If you use `targeted` Capacity Reservations in your EC2 Fleet, there must be
  enough Capacity Reservations to fulfil the target On-Demand capacity, otherwise the launch fails. To
  avoid a launch fail, rather add the `targeted` Capacity Reservations to a resource group, and
  then target the resource group. The resource group doesn't need to have enough Capacity Reservations; if
  it runs out of Capacity Reservations before the target On-Demand capacity is fulfilled, the fleet can
  launch the remaining target capacity into regular On-Demand capacity.

###### To use Capacity Reservations with EC2 Fleet

1. Configure the fleet as type `instant`. You can't use Capacity Reservations for
   fleets of other types.
2. Configure the usage strategy for Capacity Reservations as
   `use-capacity-reservations-first`.
3. In the launch template, for **Capacity reservation**, choose
   either **Open** or **Target by group**. If you
   choose **Target by group**, specify the Capacity Reservations resource group
   ID.
   When the fleet attempts to fulfil the On-Demand capacity, if it finds
   that multiple instance pools have unused matching Capacity Reservations, it determines the pools in
   which to launch the On-Demand Instances based on the On-Demand allocation strategy
   (`lowest-price` or `prioritized`).

###### Related resources

- For CLI examples of how to configure a fleet to use Capacity Reservations to fulfil On-Demand capacity,
  see [Example CLI configurations for EC2 Fleet](ec2-fleet-examples.md "ec2-fleet-examples.md"),
  specifically Examples 5 through 7.
- For a tutorial that takes you through the steps for creating Capacity Reservations, using them in your
  fleet, and viewing how many Capacity Reservations are remaining, see [Tutorial: Configure EC2 Fleet to launch On-Demand Instances using targeted Capacity Reservations](ec2-fleet-launch-on-demand-instances-using-targeted-capacity-reservations-walkthrough.md "ec2-fleet-launch-on-demand-instances-using-targeted-capacity-reservations-walkthrough.md")
- For information about configuring Capacity Reservations, see [Reserve compute capacity with EC2
  On-Demand Capacity Reservations](ec2-capacity-reservations.md "ec2-capacity-reservations.md") and
  the [On-Demand
  Capacity Reservation FAQs](https://aws.amazon.com/ec2/faqs/#On-Demand_Capacity_Reservation "https://aws.amazon.com/ec2/faqs/#On-Demand_Capacity_Reservation").
