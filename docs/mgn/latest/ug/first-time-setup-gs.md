

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# First time setup
<a name="first-time-setup-gs"></a>

The first setup step for AWS Transform MGN is creating the replication template. 

Choose **Get started** on the AWS Transform MGN landing page.

 You will automatically be prompted to initialize the service the first time you log into AWS Transform MGN. 

 Initializing the service will create a replication template. This template will determine how data replication will work for each newly added source server.

The configured replication settings can be changed at any time for any individual source server or group of source servers. [Learn more about replication settings.](replication-settings-template.md)

[Learn more about changing individual server and multiple server replication settings.](replication-settings-template.md#template-vs-server) 

**Important**  
Before configuring your replication template, ensure that you meet the [Network requirements for running AWS Transform MGN](preparing-environments.md).

Once AWS Transform MGN is initialized you'll be redirected into the MGN console **Source servers** page.

To edit your replication template, choose **Replication template**. You will be able to edit individual server replication settings after adding your source servers to AWS Transform MGN.

The next step of the setup process is adding your source servers to AWS Transform MGN.