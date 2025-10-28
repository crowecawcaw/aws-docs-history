# Creating and updating health checks

The following procedure describes how to create and update health checks using the
Route 53 console.

###### Note

We're updating the health checks console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#health-checks-creating-new "#health-checks-creating-new")
- [Old console](#health-checks-creating-old "#health-checks-creating-old")

New console

###### To create or update a health

check

1. If you're updating health checks that are already associated with records,
   perform the recommended tasks in [Updating or deleting health
   checks when DNS failover is configured](health-checks-updating-deleting-tasks.md "health-checks-updating-deleting-tasks.md").
2. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Health Checks**.
4. If you want to update an existing health check, choose the linked ID of the health check,
   and then choose **Edit**.

If you want to create a health check, choose **Create health
check**. 5. Enter the applicable values. Note that some values can't be changed after
you create a health check. For more information, see [Values that you specify when you
create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md"). 6. Choose **Create health check**.

###### Note

Route 53 considers a new health check to be healthy until there's enough
data to determine the actual status, healthy or unhealthy. 7. Associate the health check with one or more Route 53 records. For information
about creating and updating records, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").

Old console

###### To create or update a health

check

1. If you're updating health checks that are already associated with records,
   perform the recommended tasks in [Updating or deleting health
   checks when DNS failover is configured](health-checks-updating-deleting-tasks.md "health-checks-updating-deleting-tasks.md").
2. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Health Checks**.
4. If you want to update an existing health check, select the health check,
   and then choose **Edit Health Check**.

If you want to create a health check, choose **Create Health
Check**. For more information about each setting, move the
mouse pointer over a label to see its tooltip. 5. Enter the applicable values. Note that some values can't be changed after
you create a health check. For more information, see [Values that you specify when you
create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md"). 6. Choose **Create Health Check**.

###### Note

Route 53 considers a new health check to be healthy until there's enough
data to determine the actual status, healthy or unhealthy. If you chose
the option to invert the health check status, Route 53 considers a new
health check to be _unhealthy_ until there's enough
data. 7. Associate the health check with one or more Route 53 records. For information
about creating and updating records, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").
