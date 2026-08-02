# Connect a Lightsail container service to a Lightsail database

An Amazon Lightsail container service is a highly scalable compute and networking resource on
which you can deploy, run, and manage containers. For more information, see [Deploy and manage containers on
Amazon Lightsail](amazon-lightsail-container-services.md "amazon-lightsail-container-services.md").

An Lightsail database is a fully managed relational database that runs MySQL or
PostgreSQL. For more information, see [Create and
manage relational databases in Amazon Lightsail](amazon-lightsail-databases.md "amazon-lightsail-databases.md").

In this tutorial, you learn how to configure a Lightsail container service to connect to a
Lightsail database. You configure the container to connect to a Lightsail MySQL database.
When you finish, you have a Lightsail container that stores its data in a Lightsail
database.

This tutorial takes approximately 20–30 minutes to complete.

###### Note

The resources you create in this tutorial might result in charges to your AWS account.
Delete the resources after you finish to avoid ongoing charges. For more information, see
[Step 5:
Clean up resources](#amazon-lightsail-connecting-container-service-to-database-cleanup "#amazon-lightsail-connecting-container-service-to-database-cleanup").

###### Note

This tutorial uses Uptime Kuma, a third-party open-source monitoring tool, as an
example.

## Step 1: Complete the prerequisites

Complete the following prerequisites before you begin:

1. Create a Lightsail container service, for example
   `ls-container-service`. For more information, see [Creating Amazon Lightsail
   container services](amazon-lightsail-creating-container-services.md "amazon-lightsail-creating-container-services.md").
2. Create a Lightsail MySQL database, for example `ls-database`. The
   database must be in the same AWS Region as your container service. For more
   information, see [Creating a database
   in Amazon Lightsail](amazon-lightsail-creating-a-database.md "amazon-lightsail-creating-a-database.md").

## Step 2: Choose a container image

This tutorial uses the Uptime Kuma public image as an example. Uptime Kuma is a
lightweight open-source monitoring tool that tracks the uptime of websites, servers, and
services. By default, Uptime Kuma uses a SQLite file stored inside the container. By
configuring your container service to use a Lightsail database, you preserve your
monitoring configuration, availability history, and incident logs data.

Uptime Kuma is a third-party open-source project maintained on GitHub. To review the
project's license and documentation, see the [Uptime Kuma repository on GitHub](https://github.com/louislam/uptime-kuma "https://github.com/louislam/uptime-kuma").

If you want to use your own image, you can create your application on your local machine,
and then push your image to your Lightsail container service. For more information, see
[Pushing and managing container
images on your Amazon Lightsail container services](amazon-lightsail-pushing-container-images.md "amazon-lightsail-pushing-container-images.md").

## Step 3: Create a deployment with database configuration

Complete the following procedure to create a deployment on your container service that
uses the Uptime Kuma image and connects to your Lightsail database.

1. Sign in to the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Containers** to go to the
   container services home page and view your container services.
3. Choose the container service that you created in the prerequisites step, for example
   `ls-container-service`.

![Container services home page in the Lightsail console.](images/container-db-containers-home-page.png) 4. On the container service management page, choose the **Deployments**
tab, and then choose **Create your first deployment**. For more
information, see [Creating
and managing deployments for your Amazon Lightsail container services](amazon-lightsail-container-services-deployments.md "amazon-lightsail-container-services-deployments.md").

![Deployments tab of a container service with no current deployment.](images/container-db-deployments-tab.png) 5. Fill out the deployment configuration as follows:

    1. **Container name** – Enter a name for your container, for
     example `tutorialapp`. The container name doesn't have to match the
     container service name.


    ###### Note

    All containers within a deployment must have unique names and must contain only
     alphanumeric characters and hyphens. A hyphen can separate words but cannot be at
     the start or end of the name.
    2. **Source image** – Specify
     `louislam/uptime-kuma:1`.


    ###### Note

    If you want to use an image from your local machine, choose **Choose
     stored image**, and then select the image that you uploaded to your
     container service.
    3. **Launch command** – Skip this step. The Uptime Kuma image
     does not require an additional launch command for this tutorial.
    4. **Environment variables** – Choose **Add
     environment variables**, and then specify the variables that the container
     reads at runtime. Uptime Kuma requires the following environment variables to
     connect to a MySQL database. To find the database values, choose
     **Databases** in the left navigation pane of the Lightsail
     console, and then choose the database name (for example `ls-database`) to
     open the database management page.




    | Variable | Value | Location in the Lightsail console |
    | --- | --- | --- |
    | `PORT` | `3001` | Not applicable |
    | `UPTIME_KUMA_HOST` | `0.0.0.0` | Not applicable |
    | `DB_TYPE` | `mysql` | Not applicable |
    | `DB_PORT` | Your database port | The **Port*<br>• value in the **Connection<br>details*<br>• section |
    | `DB_USER` | Your database user name | The **User name*<br>• value in the **Database<br>details*<br>• section |
    | `DB_NAME` | Your database name | The database name in the **Database details**<br>section |
    | `DB_HOST` | Your database endpoint | The **Endpoint*<br>• value in the **Connection<br>details*<br>• section |
    | `DB_PASSWORD` | Your database password | Choose **Show*<br>• next to the master password to reveal<br>it |


    The following screenshot shows the location of these values on the database
     management page.



    ![Database management page showing where to find the DB_NAME, DB_HOST, DB_USER, DB_PASSWORD, and DB_PORT values.](images/container-db-database-variable-values.png)

    Using the values from your database management page, enter the environment
     variables as shown in the following screenshot.



    ![Environment variables entered in the deployment configuration.](images/container-db-environment-variables.png)
    5. **Open ports** – Choose **Add open
     ports**, and then open port `3001` with the **HTTP**
     protocol.



    ![Open ports section with port 3001 configured for HTTP.](images/container-db-open-ports.png)
    6. **Public endpoint** – Select the name of your container
     from the dropdown menu. The container in this tutorial is
     `tutorialapp`.



    ![Public endpoint section with the tutorialapp container selected.](images/container-db-public-endpoint.png)

6. Choose **Save and deploy**. Wait a few minutes for the deployment to
finish. You can monitor the deployment status under **Deployment
versions**. When the deployment is complete, the status changes to
**Active**.

![Deployment versions section showing an Active deployment.](images/container-db-deployment-active.png)

## Step 4: Test your application with your Lightsail database

Your Uptime Kuma application now runs on your Lightsail container service and connects to
your Lightsail database. To connect to your application, choose the **Public
domain** link on your container service detail page. The link opens the Uptime Kuma
setup page, where you create an account.

![Uptime Kuma dashboard showing a running monitor.](images/container-db-kuma-dashboard.png)

After you sign up, Uptime Kuma redirects you to the dashboard. On the dashboard, you can
create a new monitor. Uptime Kuma stores the monitor's data in your Lightsail
database.

Now that Uptime Kuma is running, you can use it to monitor your applications.
For example, you can [launch a Lightsail
WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md "amazon-lightsail-launch-and-configure-wordpress.md"), and then [create and
attach a static IP address](lightsail-create-static-ip.md "lightsail-create-static-ip.md") to that instance. You can then use Uptime Kuma to track
the uptime of your WordPress site.

###### Note

The default public IP address for your instance changes if you stop and start the
instance. When you attach a static IP address, it stays the same even if you stop and start
the instance, so your monitor continues to track the correct address. For more information,
see [Create a static IP and attach it to an
instance](lightsail-create-static-ip.md "lightsail-create-static-ip.md").

![Uptime Kuma add monitor page showing a static IP address configured to monitor a Lightsail WordPress instance.](images/container-db-kuma-monitor.png)

To add a monitor for your WordPress instance, complete the following steps in the Uptime
Kuma dashboard:

1. Choose **Add New Monitor**.
2. In the **URL** field, enter the static IP address of your WordPress
   instance using the format `http://`ip-address``, for
   example `http://192.0.2.0`.
3. In the **Friendly Name** field, enter a name for the monitor, for
   example `TestMonitor`.
4. Choose **Save**. Uptime Kuma begins monitoring the uptime of your
   Lightsail WordPress instance.

## Step 5: Clean up resources

To avoid ongoing charges, delete the following resources you created in this tutorial when
you no longer need them: the container service and the Lightsail database. If you also
created a WordPress instance and a static IP address in Step 4, delete those as well.

1. Delete the container service. For more information, see [Deleting Amazon Lightsail container
   services](amazon-lightsail-deleting-container-services.md "amazon-lightsail-deleting-container-services.md").
2. Delete the Lightsail database. For more information, see [Delete a Lightsail database and
   create a final snapshot](amazon-lightsail-deleting-your-database.md "amazon-lightsail-deleting-your-database.md").
3. (Optional) If you created a WordPress instance in Step 4, delete it. For more
   information, see [Deleting an
   Amazon Lightsail instance](delete-an-amazon-lightsail-instance.md "delete-an-amazon-lightsail-instance.md").
4. (Optional) If you created a static IP address in Step 4, delete it. For more
   information, see [Delete a static IP
   address in Amazon Lightsail](how-to-delete-static-ip.md "how-to-delete-static-ip.md").
