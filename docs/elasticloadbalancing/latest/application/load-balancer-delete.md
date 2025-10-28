# Delete an Application Load Balancer

As soon as your load balancer becomes available, you are billed for each hour or
partial hour that you keep it running. When you no longer need the load balancer, you
can delete it. As soon as the load balancer is deleted, you stop incurring charges for
it.

You can't delete a load balancer if deletion protection is enabled. For more
information, see [Deletion protection](edit-load-balancer-attributes.md#deletion-protection "edit-load-balancer-attributes.md#deletion-protection").

Note that deleting a load balancer does not affect its registered targets. For
example, your EC2 instances continue to run and are still registered to their target
groups. To delete your target groups, see [Delete an Application Load Balancer target group](delete-target-group.md "delete-target-group.md").

###### DNS records

If you have a DNS record for your domain that points to your load balancer,
point it to a new location and wait for the DNS change to take effect before
deleting your load balancer.

- If the record is a CNAME record with a Time To Live (TTL) of 300
  seconds, wait at least 300 seconds before continuing to the next step.
- If the record is a Route 53 Alias(A) record, wait at least 60 seconds.
- If using Route 53, the record change takes 60 seconds to propagate to
  all global Route 53 name servers. Add this time to the TTL value of the
  record that is being updated.

Console

###### To delete a load balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer, and then choose **Actions**,
   **Delete load balancer**.
4. When prompted for confirmation, enter `confirm` and then
   choose **Delete**.

AWS CLI

###### To delete a load balancer

Use the [delete-load-balancer](../../../cli/latest/reference/elbv2/delete-load-balancer.md "../../../cli/latest/reference/elbv2/delete-load-balancer.md") command.

```
aws elbv2 delete-load-balancer \
    --load-balancer-arn `load-balancer-arn`
```
