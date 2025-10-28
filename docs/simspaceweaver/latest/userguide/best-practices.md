End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Best practices when working with SimSpace Weaver

We recommend the following best practices when working
with SimSpace Weaver.

###### Topics

- [Set up billing alarms](#best-practices_billing-alarms "#best-practices_billing-alarms")
- [Use SimSpace Weaver Local](#best-practices_use-local "#best-practices_use-local")
- [Stop simulations that you don't need](#best-practices_stop-sims "#best-practices_stop-sims")
- [Delete resources that you don't need](#best-practices_cleanup "#best-practices_cleanup")
- [Have backups](#best-practices_backup "#best-practices_backup")

## Set up billing alarms

It's easy to provision resources in AWS and leave them running
all the time, even when they aren't needed anymore. This can result
in runaway costs that can be a surprise when you get your bill. You
can configure an alarm in Amazon CloudWatch that will trigger and notify you
when your costs exceed a threshold that you set. You can examine your
costs using cost management tools. For more information, see:

- [Create a billing alarm to monitor your estimated AWS charges](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md")
- [What is AWS Cost Management](../../../cost-management/latest/userguide/what-is-costmanagement.md "../../../cost-management/latest/userguide/what-is-costmanagement.md")

## Use SimSpace Weaver Local

We recommend that you use SimSpace Weaver Local to develop and test your simulations before
uploading them to the SimSpace Weaver service in the AWS Cloud. The benefits of developing
with SimSpace Weaver Local include:

- No need to wait for large uploads
- No limit on the number of local simulations you can create
- You aren't charged for the compute time on your local computer
- Direct access to console output from your apps
- Modify, rebuild, and restart your local simulation without having to recreate it in the AWS Cloud

## Stop simulations that you don't need

You get billing charges for a simulation while it is running. You must
stop a simulation to stop getting charges for it. Running simulations
also count towards your quota for the maximum number of simulations. A
running simulation that has logging configured can also generate large
amounts of logs, which you also get billing charges for. You should
stop any simulation that you don't need in order to stop getting
additional charges.

###### Important

Stopping the simulation clock doesn't stop the simulation,
the clock just stops publishing ticks to your apps.
You can't restart a simulation after you stop it.

## Delete resources that you don't need

Each simulation that you create in SimSpace Weaver also creates resources in other AWS
services. You can get billing charges for resources and data in these other services.
Running and failed simulations count towards your quota for the maximum number of
simulations. You should delete unneeded failed simulations so that you can start new
simulations. When you delete a simulation, resources for your simulation that exist in
other AWS services might not be deleted. For example, any simulation log data in
Amazon CloudWatch Logs will remain there until you delete it. You will get billing charges for that
log data. You should cleanup all the associated resources for your simulations if you
don't need them anymore.

## Have backups

It's a good idea to have backups and backup plans for everything. You shouldn’t assume
that just because your data is in AWS that you don't have to back it up. You must
create your own system if you need to back up your simulation state. Consider using
multiple AWS Regions and having a plan in place to be able to quickly switch your
production workload to another AWS Region if you need to. For more information about
AWS Regions that support SimSpace Weaver, see [SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md").
