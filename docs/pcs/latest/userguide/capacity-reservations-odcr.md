# Using ODCRs with AWS PCS

You can choose how AWS PCS consumes your reserved instances. If you create an
**open** ODCR, any matching instances launched by
AWS PCS or other processes in your account count against the reservation.
With a **targeted** ODCR, only instances launched
with the specific reservation ID count against the reservation. For time-sensitive
workloads, targeted ODCRs are more common.

You can configure an AWS PCS compute node group to use a targeted ODCR by adding
it to a launch template. Here are the steps to do so:

1. Create a targeted On-Demand Capacity Reservation (ODCR) using the
   [Amazon EC2 Create a Capacity Reservation User Guide](../../../AWSEC2/latest/UserGuide/capacity-reservations-create.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-create.md") .
2. Associate the ODCR with a launch template. There are two ways to do that:
   1. **Direct ODCR association:**
      Reference the ODCR ID directly in the launch template.
      This approach provides strict capacity control and does not support instance backfilling
      (If the compute node group requests more instances than available in the ODCR, no additional
      instances will be launched).
   2. **Capacity Reservation group association:**
      Add the ODCR to a Capacity Reservation group and reference the group in
      the launch template. This approach supports instance backfilling, allowing
      AWS PCS to launch additional On-Demand instances if the reservation
      capacity is exceeded.

3. Create or update an AWS PCS compute node group to use the launch template.
   For more information, see [AWS PCS Compute Node Groups User Guide](working-with_cng.md "working-with_cng.md").
   1. Set the `purchaseOption` of the compute node group
      to `ONDEMAND`.

## Example:

Reserve and use hpc6a.48xlarge instances with a targeted ODCR

This example command creates a targeted ODCR for 32 hpc6a.48xlarge instances.
To launch the reserved instances in a placement group, add
`--placement-group-arn` to the command.
You can define a stop date with `--end-date` and
`--end-date-type`, otherwise the reservation will continue until
it is manually terminated.

```
aws ec2 create-capacity-reservation \
    --instance-type hpc6a.48xlarge \
    --instance-platform Linux/UNIX \
    --availability-zone us-east-2a \
    --instance-count 32 \
    --instance-match-criteria targeted
```

The result from this command will be an ARN for the new ODCR. The ODCR ID can be retrieved from the ARN
`"arn:aws:ec2:us-east-2:123456789012:capacity-reservation/ODCR-ID"`
or by using the [Amazon EC2 DescribeCapacityReservations](../../../AWSEC2/latest/APIReference/API_DescribeCapacityReservations.md "../../../AWSEC2/latest/APIReference/API_DescribeCapacityReservations.md").

**Direct ODCR association:** Add the ODCR ID to the launch template.
Here is an example launch template that references the ODCR ID.

```
{
  "CapacityReservationSpecification": {
    "CapacityReservationTarget": {
      "CapacityReservationId": "cr-1234567890abcdef1"
    }
  }
}
```

**Capacity Reservation group association:**
Create a Capacity Reservation group and add the group to the launch template.
The following command creates a Capacity Reservation group named
`EXAMPLE-CR-GROUP`.

```
aws resource-groups create-group \
    --name EXAMPLE-CR-GROUP \
    --configuration \
        '{"Type": "AWS::EC2::CapacityReservationPool"}' \
        '{"Type": "AWS::ResourceGroups::Generic", "Parameters": [{"Name": "allowed-resource-types", "Values": ["AWS::EC2::CapacityReservation"]}]}'
```

The following command adds the ODCR to the Capacity Reservation group.

```
aws resource-groups group-resources --group EXAMPLE-CR-GROUP \
    --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity-reservation/cr-1234567890abcdef1
```

With the ODCR created and added to a Capacity Reservation group,
it can now be connected to an AWS PCS compute node group by adding
it to a launch template. Here is an example launch template that
references the Capacity Reservation group.

```
{
  "CapacityReservationSpecification": {
    "CapacityReservationResourceGroupArn": "arn:aws:resource-groups:us-east-2:123456789012:group/EXAMPLE-CR-GROUP"
  }
}
```

Finally, create or update an AWS PCS compute node group to use hpc6a.48xlarge instances
and use the launch template that references the ODCR.
For a static node group, set minimum and maximum instances to the size of the reservation
(32). For a dynamic node group, set the minimum instances to 0 and the maximum to your desired
instance size.

This example is a simple implementation of a single ODCR that is provisioned for one compute
node group. But, AWS PCS supports many other designs. For example, you can subdivide
a large ODCR or Capacity Reservation group among multiple compute node groups. Or, you
can use ODCRs that another AWS account has created and shared with yours.

For more information, see [On-Demand
Capacity Reservations and Capacity Blocks for ML](../../../AWSEC2/latest/UserGuide/capacity-reservation-overview.md "../../../AWSEC2/latest/UserGuide/capacity-reservation-overview.md") in
the _Amazon Elastic Compute Cloud User Guide_.
