# Replace or restore the target for a local route

You can change the target of the default local route. If you replace the
target of a local route, you can later restore it to the default `local`
target. If your VPC has [multiple CIDR blocks](vpc-cidr-blocks.md#vpc-resize "vpc-cidr-blocks.md#vpc-resize"), your
route tables have multiple local routes—one per CIDR block. You can replace
or restore the target of each of the local routes as needed.

###### To replace the local route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route tables**, and then
   select the route table.
3. From the **Routes** tab, choose **Edit
   routes**.
4. For the local route, clear **Target** and then choose a
   new target.
5. Choose **Save changes**.

###### To restore the target for a local route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route tables**, and then
   select the route table.
3. Choose **Actions**, **Edit
   routes**.
4. For the route, clear **Target**, and then choose
   **local**.
5. Choose **Save changes**.

###### To replace the target for a local route using the AWS CLI

Use the [replace-route](../../../cli/latest/reference/ec2/replace-route.md "../../../cli/latest/reference/ec2/replace-route.md")
command. The following example replaces the target of the local route with
the specified network interface.

```
aws ec2 replace-route \
    --route-table-id `rtb-01234567890123456` \
    --destination-cidr-block `10.0.0.0/16` \
    --network-interface-id `eni-11223344556677889`
```

###### To restore the target for a local route using the AWS CLI

The following example restores the local target for the
specified route table.

```
aws ec2 replace-route \
    --route-table-id `rtb-01234567890123456` \
    --destination-cidr-block `10.0.0.0/16` \
    --local-target
```
