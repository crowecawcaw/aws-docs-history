# AMS Resource Scheduler cost estimator

In order to track cost savings, AMS Resource Scheduler features a component that
hourly calculates the estimated cost savings for Amazon EC2 and RDS resources that are managed
by scheduler. This cost savings data is then published as a CloudWatch metric
(`AMS/ResourceScheduler`) to help you track it. The cost savings estimator only
estimates savings on instance running hours. It does not account any other cost, such as data
transfer costs associated with a resource.

The cost savings estimator is enabled with Resource Scheduler. It runs hourly and retrieves
cost and usage data from AWS Cost Explorer. From that data it calculates the average cost per hour for
each instance type and then projects the cost for a full day if it was running without being
scheduled. The cost savings is the difference between the projected cost and the actual reported
cost from Cost Explorer for a given day.

For example, if instance A is configured with Resource Scheduler to run from 9 a.m. to 5
p.m., that is eight hours on a given day. Cost Explorer reports the cost as $1 and usage as 8. The average
cost per hour is therefore $0.125. If the instance was not scheduled with Resource Scheduler,
then the instance would run 24 hours on that day. In that case, the cost would have been
24x0.125 = $3. Resource Scheduler helped you achieve a cost savings of $2.

In order for the cost savings estimator to retrieve cost and usage only for resources
managed by Resource Scheduler from Cost Explorer, the tag key that Resource Scheduler uses to target
resources needs to be activated as the **Cost allocation** tag in the Billing Dashboard.
If the account belongs to an organization, the tag key needs to be activated in the Management account of the organization. For
information on doing this, see
[Activating User-Defined Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") and
[User-Defined Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md")

After the tag key is activated as Cost Allocation Tag, AWS billing starts tracking cost and
usage for resources managed by Resource Scheduler, and after that data is available, the cost
savings estimator starts to calculate the cost savings and publish the data under the
`AMS/ResourceScheduler` metric namespace in CloudWatch.
