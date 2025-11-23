# Configure security groups for your Classic Load Balancer

When you use the AWS Management Console to create a load balancer, you can
choose an existing security group or create a new one.
If you choose an existing security group, it must allow traffic in both directions
to the listener and health check ports for the load balancer. If you choose to
create a security group, the console automatically adds rules to allow all traffic
on these ports.

[Nondefault VPC] If you use the AWS CLI or API create a load balancer in a nondefault VPC,
but you don't specify a security group, your load balancer is automatically associated
with the default security group for the VPC.

[Default VPC] If you use the AWS CLI or API to create a load balancer in your default VPC,
you can't choose an existing security group for your load balancer. Instead,
ELB provides a security group with rules to allow all traffic on the ports specified
for the load balancer. ELB creates only one such security group per AWS account, with
a name of the form default_elb\_`id` (for example,
`default_elb_fc5fbed3-0405-3b7d-a328-ea290EXAMPLE`).
Subsequent load balancers that you create in the default VPC also use this security group.
Be sure to review the security group rules to ensure that they allow traffic
on the listener and health check ports for the new load balancer. When you delete
your load balancer, this security group is not deleted automatically.

If you add a listener to an existing load balancer, you must review your security groups
to ensure they allow traffic on the new listener port in both directions.

###### Contents

- [Recommended rules for load balancer security groups](#recommended-sg-rules "#recommended-sg-rules")
- [Assign security groups using the console](#assign-sg-console "#assign-sg-console")
- [Assign security groups using the AWS CLI](#assign-sg-cli "#assign-sg-cli")

## Recommended rules for load balancer security groups

The security groups for your load balancers must allow them to communicate with your
instances. The recommended rules depend on the type of load balancer, internet-facing
or internal.

###### Internet-facing load balancer

The following table shows the recommended inbound rules for an internet-facing load balancer.

| Source    | Protocol | Port Range | Comment                                                      |
| --------- | -------- | ---------- | ------------------------------------------------------------ |
| 0.0.0.0/0 | TCP      | `listener` | Allow all inbound traffic on the load balancer listener port |

The following table shows the recommended outbound rules for an internet-facing load balancer.

| Destination               | Protocol | Port Range          | Comment                                                           |
| ------------------------- | -------- | ------------------- | ----------------------------------------------------------------- |
| `instance security group` | TCP      | `instance listener` | Allow outbound traffic to instances on the instance listener port |
| `instance security group` | TCP      | `health check`      | Allow outbound traffic to instances on the health check port      |

###### Internal load balancers

The following table shows the recommended inbound rules for an internal load balancer.

| Source     | Protocol | Port Range | Comment                                                                    |
| ---------- | -------- | ---------- | -------------------------------------------------------------------------- |
| `VPC CIDR` | TCP      | `listener` | Allow inbound traffic from the VPC CIDR on the load balancer listener port |

The following table shows the recommended outbound rules for an internal load balancer.

| Destination               | Protocol | Port Range          | Comment                                                           |
| ------------------------- | -------- | ------------------- | ----------------------------------------------------------------- |
| `instance security group` | TCP      | `instance listener` | Allow outbound traffic to instances on the instance listener port |
| `instance security group` | TCP      | `health check`      | Allow outbound traffic to instances on the health check port      |

## Assign security groups using the console

Use the following procedure to change the security groups associated with
your load balancer.

###### To update a security group assigned to your load balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Security** tab, choose **Edit**.
5. On the **Edit security groups** page, Under
   **Security groups**, add or remove security groups
   as needed.

You can add up to five security groups. 6. When you are finished, choose **Save changes**.

## Assign security groups using the AWS CLI

Use the following [apply-security-groups-to-load-balancer](../../../cli/latest/reference/elb/apply-security-groups-to-load-balancer.md "../../../cli/latest/reference/elb/apply-security-groups-to-load-balancer.md") command to associate a
security group with a load balancer. The specified security groups
override the previously associated security groups.

```
`aws elb apply-security-groups-to-load-balancer --load-balancer-name `my-loadbalancer` --security-groups `sg-53fae93f``
```

The following is an example response:

```
{
  "SecurityGroups": [
     "sg-53fae93f"
  ]
}
```
