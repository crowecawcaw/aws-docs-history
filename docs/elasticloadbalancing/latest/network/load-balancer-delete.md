# Delete a Network Load Balancer

As soon as your Network Load Balancer becomes available, you are billed for each hour or
partial hour that you keep it running. When you no longer need the Network Load Balancer, you
can delete it. As soon as the Network Load Balancer is deleted, you stop incurring charges for
it.

You can't delete a Network Load Balancer if deletion protection is enabled. For more
information, see [Deletion protection](edit-load-balancer-attributes.md#deletion-protection "edit-load-balancer-attributes.md#deletion-protection").

You can't delete a Network Load Balancer if it is in use by another service. For example, if
the Network Load Balancer is associated with a VPC endpoint service, you must delete the
endpoint service configuration before you can delete the associated Network Load Balancer.

Deleting a Network Load Balancer also deletes its listeners. Deleting a Network Load Balancer does not
affect its registered targets. For example, your EC2 instances continue to run and are
still registered to their target groups. To delete your target groups, see [Delete a target group for your Network Load Balancer](delete-target-group.md "delete-target-group.md").

Console

###### To delete a Network Load Balancer

1. If you have a DNS record for your domain that points to your Network Load Balancer,
   point it to a new location and wait for the DNS change to take effect before
   deleting your Network Load Balancer. For example:
   - If the record is a CNAME record with a Time To Live (TTL) of 300
     seconds, wait at least 300 seconds before continuing to the next step.
   - If the record is a Route 53 Alias(A) record, wait at least 60 seconds.
   - If using Route 53, the record change takes 60 seconds to propagate to
     all global Route 53 name servers. Add this time to the TTL value of the
     record that is being updated.

2. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
3. In the navigation pane, choose **Load Balancers**.
4. Select the check box for the Network Load Balancer.
5. Choose **Actions**, **Delete load
   balancer**.
6. When prompted for confirmation, enter `confirm` and
   choose **Delete**.

AWS CLI

###### To delete a Network Load Balancer

Use the [delete-load-balancer](../../../cli/latest/reference/elbv2/delete-load-balancer.md "../../../cli/latest/reference/elbv2/delete-load-balancer.md") command.

```
aws elbv2 delete-load-balancer \
    --load-balancer-arn `load-balancer-arn`
```
