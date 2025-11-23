# Route table

To use VPC peering or Direct Connect to reach an on-premises database instance, update the
route table that's associated with the VPC you're using with Amazon Quick Suite. For more
information on route tables, see [Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon VPC User Guide._

To learn more about VPC peering and view sample scenarios and configurations, see
[What is VPC
peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") in the _Amazon VPC Peering Guide._ For an example
configuration, see [Example:
Services using AWS PrivateLink and VPC peering](../../../vpc/latest/userguide/vpc-peer-region-example.md "../../../vpc/latest/userguide/vpc-peer-region-example.md") in the _Amazon VPC User Guide._

**Using the AWS CLI**

The following example creates a route table.

```
aws ec2 create-route-table --vpc-id `vpc-0daeb67adda59e0cd`
```

Then you can use the `create-route` command to create a route. For more
information and examples, see [create-route](../../../cli/latest/reference/ec2/create-route.md "../../../cli/latest/reference/ec2/create-route.md") in the _AWS CLI Command
Reference._

For the following examples to work, make sure that you have a subnet in the VPC
associated with the route table. The first example describes the route table with the
specified VPC ID. The second one describes the route table with the specified route
table ID.

```

aws ec2 describe-route-tables \
--filters "Name=vpc-id,Values=`vpc-0daeb67adda59e0cd`"

aws ec2 describe-route-tables \
--route-table-ids `rtb-45ac473a`

```

The following example describes the specified associations between a specific VPC and
your local gateway route tables.

```

aws ec2 describe-local-gateway-route-table-vpc-associations
--filters "Name=vpc-id,Values=`vpc-0daeb67adda59e0cd`"

```
