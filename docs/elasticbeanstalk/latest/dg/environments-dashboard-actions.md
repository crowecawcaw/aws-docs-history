# Environment actions

This topic describes the common operations that you can select to perform on your environment from the **Actions** drop-down menu on
the environment management console.

The following image illustrates the environment management console. The **Actions** drop-down menu is on the right side of the header
that displays the environment name, next to the **Refresh** button.

![Image of the environment management console showing the Actions drop-down menu.](images/environment-overview-v2-margin.png)

###### Note

Some actions are only available under certain conditions, remaining disabled until the right conditions are met.

## Load configuration

Load a previously saved configuration. Configurations are saved to your application and can be loaded by any associated environment. If you've made
changes to your environment's configuration, you can load a saved configuration to undo those changes. You can also load a configuration that you saved
from a different environment running the same application to propagate configuration changes between them.

## Save configuration

Save the current configuration of your environment to your application. Before you make changes to your environment's configuration, save the
current configuration so that you can roll back later, if needed. You can also apply a saved configuration when you launch a new environment.

## Swap environment Domains (URLs)

Swap the CNAME of the current environment with a new environment. After a CNAME swap, all traffic to the application using the environment URL goes
to the new environment. When you are ready to deploy a new version of your application, you can launch a separate environment under the new version.
When the new environment is ready to start taking requests, perform a CNAME swap to start routing traffic to the new environment. Doing this doesn't
interrupt your services. For more information, see [Blue/Green deployments with Elastic Beanstalk](using-features.md "using-features.md").

## Clone environment

Launch a new environment with the same configuration as your currently running environment.

## Clone with latest platform

Clone your current environment with the latest version of the in-use Elastic Beanstalk platform. This option is available only when a newer version of the
current environment's platform is available for use.

## Abort current operation

Stop an in-progress environment update. Stopping an operation can cause some of the instances in your environment to be in a different state than
others, depending on how far the operation progressed. This option is available only when your environment is being updated.

## Restart app servers

Restart the web server that is running on your environment's instances. This option doesn't terminate or restart any AWS resources. If your
environment is acting strangely in response to some bad requests, restarting the application server can restore functionality temporarily while you
troubleshoot the root cause.

## Rebuild environment

Terminate all resources in the running environment and build a new environment with the same settings. This operation takes several minutes, similar
to the amount of time needed for deploying a new environment from scratch. Any Amazon RDS instances that are running in your environment's data tier are
deleted during a rebuild. If you need the data, create a snapshot. You can create a snapshot manually [in the RDS console](../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md") or configure your data tier's Deletion Policy to create a snapshot
automatically before deleting the instance. This is the default setting when you create a data tier.

## Terminate environment

Terminate all resources in the running environment and remove the environment from the application. If you have an RDS instance that is running in a
data tier and you need to retain its data, make sure the _database deletion policy_ is set to either `Snapshot` or
`Retain`. For more information, see [Database lifecycle](using-features.managing.md#environments-cfg-rds-lifecycle "using-features.managing.md#environments-cfg-rds-lifecycle") in the
_Configuring environments_ chapter of this guide.
