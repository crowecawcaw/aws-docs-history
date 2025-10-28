# Subnet CIDR reservations

A _subnet CIDR reservation_ is a range of IPv4 or IPv6 addresses that you
set aside so that AWS won't assign them to your network interfaces. This enables you to
reserve IPv4 or IPv6 CIDR blocks (also called "prefixes") for use with your network
interfaces.

When you create a subnet CIDR reservation, you specify how you will use the reserved IP
addresses. The following options are available:

- **Prefix** — Allows you to assign a prefix to a single
  network interface. For more information, see [Assign prefixes to Amazon EC2
  network interfaces](../../../AWSEC2/latest/UserGuide/ec2-prefix-eni.md "../../../AWSEC2/latest/UserGuide/ec2-prefix-eni.md") in the _Amazon EC2 User Guide_.
- **Explicit** — Allows you to manually assign an
  individual IP address to a single network interface.
  The following rules apply to subnet CIDR reservations:

- When you create a subnet CIDR reservation, the IP address range can include addresses
  that are already in use. Creating a subnet reservation does not unassign any IP addresses
  that are already in use.
- You can reserve multiple CIDR ranges per subnet. When you reserve multiple CIDR ranges
  within the same VPC, the CIDR ranges can't overlap.
- When you reserve more than one range in a subnet for Prefix Delegation, and Prefix
  Delegation is configured for automatic assignment, we choose the IP addresses to assign
  to network interfaces at random.
- When you delete a subnet reservation, the unused IP addresses are available for AWS
  to assign to your network interfaces. Deleting a subnet reservation does not unassign
  any IP addresses that are in use.
- The reservation type affects the count of available IP addresses for the subnet. If
  you create a prefix reservation, the count decreases immediately. If you create an
  explicit prefix reservation, the count decreases when the IP addresses are assigned.
  For more information about Classless Inter-Domain Routing (CIDR) notation, see [IP addressing for your VPCs and subnets](vpc-ip-addressing.md "vpc-ip-addressing.md").

###### Contents

- [Work with subnet CIDR reservations using the console](#edit-subnet-cidr-reservations "#edit-subnet-cidr-reservations")
- [Work with subnet CIDR reservations using the AWS CLI](#work-with-subnet-cidr-reservations "#work-with-subnet-cidr-reservations")

## Work with subnet CIDR reservations using the console

You can create and manage subnet CIDR reservations as follows.

###### To edit subnet CIDR reservations

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. Select the subnet.
4. Choose the **CIDR reservations** tab to get information about
   any existing subnet CIDR reservations.
5. To add or remove subnet CIDR reservations, choose **Actions**,
   **Edit CIDR reservations** and then do the following:
   - To add an IPv4 CIDR reservation, choose **IPv4**, **Add IPv4 CIDR reservation**.
     Choose the reservation type, enter the CIDR range, and choose **Add**.
   - To add an IPv6 CIDR reservation, choose **IPv6**, **Add IPv6 CIDR reservation**.
     Choose the reservation type, enter the CIDR range, and choose **Add**.
   - To remove a CIDR reservation, choose **Remove** for the subnet
     CIDR reservation.

## Work with subnet CIDR reservations using the AWS CLI

You can use the AWS CLI to create and manage subnet CIDR reservations.

###### Tasks

- [Create a subnet CIDR reservation](#Create-subnet-cidr-reservations "#Create-subnet-cidr-reservations")
- [View subnet CIDR reservations](#view-subnet-cidr-reservations "#view-subnet-cidr-reservations")
- [Delete a subnet CIDR reservation](#delete-subnet-cidr-reservations "#delete-subnet-cidr-reservations")

### Create a subnet CIDR reservation

You can use [create-subnet-cidr-reservation](../../../cli/latest/reference/ec2/create-subnet-cidr-reservation.md "../../../cli/latest/reference/ec2/create-subnet-cidr-reservation.md")
to create a subnet CIDR reservation.

```
aws ec2 create-subnet-cidr-reservation --subnet-id `subnet-03c51e2eEXAMPLE` --reservation-type prefix --cidr `2600:1f13:925:d240:3a1b::/80`
```

The following is example output.

```
{
    "SubnetCidrReservation": {
        "SubnetCidrReservationId": "scr-044f977c4eEXAMPLE",
        "SubnetId": "subnet-03c51e2ef5EXAMPLE",
        "Cidr": "2600:1f13:925:d240:3a1b::/80",
        "ReservationType": "prefix",
        "OwnerId": "123456789012"
    }
}
```

### View subnet CIDR reservations

You can use [get-subnet-cidr-reservations](../../../cli/latest/reference/ec2/get-subnet-cidr-reservations.md "../../../cli/latest/reference/ec2/get-subnet-cidr-reservations.md")
to view the details of a subnet CIDR reservation.

```
aws ec2 get-subnet-cidr-reservations --subnet-id `subnet-05eef9fb78EXAMPLE`
```

### Delete a subnet CIDR reservation

You can use [delete-subnet-cidr-reservation](../../../cli/latest/reference/ec2/delete-subnet-cidr-reservation.md "../../../cli/latest/reference/ec2/delete-subnet-cidr-reservation.md")
to delete a subnet CIDR reservation.

```
aws ec2 delete-subnet-cidr-reservation --subnet-cidr-reservation-id `scr-044f977c4eEXAMPLE`
```
