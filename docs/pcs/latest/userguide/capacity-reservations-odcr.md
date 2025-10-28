# Using ODCRs with AWS PCS

You can choose how AWS PCS consumes your reserved instances. If you create an
**open** ODCR, any matching instances launched by
AWS PCS or other processes in your account count against the reservation.
With a **targeted** ODCR, only instances launched
with the specific reservation ID count against the reservation. For time-sensitive
workloads, targeted ODCRs are more common.

You can configure an AWS PCS compute node group to use a targeted ODCR by adding
it to a launch template. Here are the steps to do so:

1. Create a targeted on-demand Capacity Reservation (ODCR).
2. Add the ODCR to a Capacity Reservation group.
3. Associate the Capacity Reservation group with a launch template.
4. Create or update an AWS PCS compute node group to use the launch template.
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

The result from this command will be an ARN for the new ODCR.
To use the ODCR with AWS PCS, it must be added to a Capacity Reservation group.
This is because AWS PCS does not support individual ODCRs. For more information,
see [Capacity
Reservation groups](../../../AWSEC2/latest/UserGuide/create-cr-group.md#create-group "../../../AWSEC2/latest/UserGuide/create-cr-group.md#create-group") in the _Amazon Elastic Compute Cloud User Guide_.

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
    --resource-arns arn:aws:ec2:sa-east-1:123456789012:capacity-reservation/cr-1234567890abcdef1
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
and use the launch template that references the ODCR in its Capacity Reservation group.
For a static node group, set minimum and maximum instances to the size of the reservation
(32). For a dynamic node group, set the minimum instances to 0 and the maximum up to the
reservation size.

This example is a simple implementation of a single ODCR that provisioned for one compute
node group. But, AWS PCS supports many other designs. For example, you can subdivide
a large ODCR or Capacity Reservation group among multiple compute node groups. Or, you
can use ODCRs that another AWS account has created and shared with yours. The key
constraint is that ODCRs always must be contained in a Capacity Reservation group.

For more information, see [On-Demand
Capacity Reservations and Capacity Blocks for ML](../../../AWSEC2/latest/UserGuide/capacity-reservation-overview.md "../../../AWSEC2/latest/UserGuide/capacity-reservation-overview.md") in
the _Amazon Elastic Compute Cloud User Guide_.
