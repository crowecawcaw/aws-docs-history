NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# First time setup

The first setup step for AWS Application Migration Service is creating the replication template.

Choose **Get started** on the AWS Application Migration Service landing page.

You will automatically be prompted to initialize the service the first time you log into
AWS Application Migration Service.

Initializing the service will create a replication template. This template will determine
how data replication will work for each newly added source server.

The configured replication settings can be changed at any time for any individual source
server or group of source servers. [Learn more
about replication settings.](replication-settings-template.md "replication-settings-template.md")

[Learn more about changing individual server and multiple
server replication settings.](replication-settings-template.md#template-vs-server "replication-settings-template.md#template-vs-server")

###### Important

Prior to configuring your replication template, ensure that you meet the [Network requirements for running AWS Application Migration Service](preparing-environments.md "preparing-environments.md").

Once AWS Application Migration Service is initialized you'll be redirected into the MGN console **Source servers** page.

To edit your replication template, click **Replication
template** on the left-hand navigation menu. You will be able to edit individual
server replication settings after adding your source servers to AWS Application Migration Service.

The next step of the setup process is adding your source servers to AWS Application Migration Service.
