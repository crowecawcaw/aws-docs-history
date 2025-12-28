# Creating an Elastic Beanstalk environment

The following procedure launches a new environment running the default application. These steps are simplified to get your environment up and running
quickly, using default option values.

###### Note about permissions

Creating an environment requires the permissions in the Elastic Beanstalk full access managed policy. See [Elastic Beanstalk user policy](concepts-roles-user.md "concepts-roles-user.md") for details.

###### To launch an environment with an application (console)

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Applications**. Select an existing application in the list. You can also choose to create one,
   following the instructions in [Managing applications](applications.md "applications.md").
3. On the application overview page, choose **Create environment**.

This launches the **Create environment** wizard. The wizard provides a set of steps for you to create a new environment. 4. For **Environment tier**, choose the **Web server environment** or **Worker environment**
[environment tier](concepts.md#concepts-tier "concepts.md#concepts-tier"). You can't change an environment's tier after creation.

###### Note

The [.NET on Windows Server platform](create_deploy_NET.md "create_deploy_NET.md") doesn't support the worker environment tier.

The **Application information** fields default, based on the application that you previously chose.

In the **Environment information** grouping the **Environment name** defaults, based on the application name. If
you prefer a different environment name you can enter another value in the field. You can optionally enter a **Domain** name; otherwise
Elastic Beanstalk autogenerates a value. You can also optionally enter an **Environment description.** 5. For **Platform**, select the platform and platform branch that match the language your application uses.

###### Note

Elastic Beanstalk supports multiple [versions](concepts.md "concepts.md") for most of the platforms that are listed. By default, the console
selects the recommended version for the platform and platform branch you choose. If your application requires a different version, you can select it
here. For information about supported platform versions, see [Elastic Beanstalk supported platforms](concepts.md "concepts.md"). 6. For **Application code**, you have several choices to proceed.

    * To launch the default sample application without supplying the source code, choose **Sample application**. This action chooses
     the single page application that Elastic Beanstalk provides for the platform you previously selected.
    * If you downloaded a sample application from this guide, or you have your own source
     code for an application, do the following steps.


    	1. Select **Upload your code**.
    	2. Next choose **Local file**, then under **Upload application**, select **Choose
    	 file**.
    	3. Your client machine's operating system will present you with an interface to
    	 select the local file that you downloaded. Select the source bundle file and
    	 continue.

7. Your choice for **Presets** depends on your purpose for the environment.
   - If you're creating a sample environment to learn about Elastic Beanstalk or a development environment,
     choose **Single instance (free tier eligible)**.
   - If you're creating a production environment or an environment to learn more about load
     balancing, choose one of the **High availability** options.

8. Choose **Next**.

###### To configure service access

Next, you need two roles. A _service role_ allows Elastic Beanstalk
to monitor your EC2 instances and upgrade you environment’s platform. An _EC2 instance profile_ role permits tasks such as writing logs and
interacting with other services.

###### To create or select the Service role

1. If you have previously created a **Service role** and would like to
   choose an existing one, select the value from the **Service role**
   drop-down and skip the remainder of these steps to create a Service role.
2. If you don't see any values listed for **Service role**, or you'd like
   to create a new one, continue with the next steps.
3. For **Service role**, choose **Create role**.
4. For **Trusted entity type**, choose **AWS
   service**.
5. For **Use case**, choose **Elastic Beanstalk –
   Environment**.
6. Choose **Next**.
7. Verify that **Permissions policies** include the following, then choose
   **Next**:
   - `AWSElasticBeanstalkEnhancedHealth`
   - `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

8. Choose **Create role**.
9. Return to the **Configure service access** tab, refresh the list, then
   select the newly created service role.

###### To create or select an EC2 instance profile

1. If you have previously created an **EC2 instance profile** and would
   like to choose an existing one, select the value from the **EC2 instance
   profile** drop-down and skip the remainder of these steps to create an EC2
   instance profile.
2. If you don't see any values listed for **EC2 instance profile**, or you'd like
   to create a new one, continue with the next steps.
3. Choose **Create role**.
4. For **Trusted entity type**, choose **AWS
   service**.
5. For **Use case**, choose **Elastic Beanstalk –
   Compute**.
6. Choose **Next**.
7. Verify that **Permissions policies** include the following, then choose
   **Next**:
   - `AWSElasticBeanstalkWebTier`
   - `AWSElasticBeanstalkWorkerTier`
   - `AWSElasticBeanstalkMulticontainerDocker`

8. Choose **Create role**.
9. Return to the **Configure service access** tab, refresh the list, then
   select the newly created EC2 instance profile.

###### To finish configuring and creating your application

1. (Optional) If you previously created an EC2 key pair, you can select it from the **EC2 key pair** field dropdown. You would use it
   to securely log in to the Amazon EC2 instance that Elastic Beanstalk provisions for your application. If you skip this step, you can always create and assign an EC2 key
   pair after the environment is created. For more information, see [EC2 key pair](using-features.managing.md#using-features.managing.security.keypair "using-features.managing.md#using-features.managing.security.keypair").
2. Choose **Skip to Review** on the **Configure service access** page.
3. The **Review** page displays a summary of all your choices.

To further customize your environment, choose **Edit** next to the step that includes any items you want to configure. You can set
the following options only during environment creation:

    * Environment name
    * Domain name
    * Platform version
    * Processor
    * Load balancer type
    * Tier

You can change the following settings after environment creation, but they require new instances or other resources to be provisioned and can take a
long time to apply:

    * Instance type, root volume, key pair, and AWS Identity and Access Management (IAM) role
    * Internal Amazon RDS database
    * VPC

For details on all available settings, see [The create new environment wizard](environments-create-wizard.md "environments-create-wizard.md"). 4. Choose **Submit** at the bottom of the page to initialize the creation of your new environment.
While Elastic Beanstalk creates your environment, you are redirected to the [Elastic Beanstalk console](environments-console.md "environments-console.md"). When the environment
health turns green, choose the URL next to the environment name to view the running
application. This URL is generally accessible from the internet unless you configure your
environment to use a [custom VPC with an
internal load balancer](environments-create-wizard.md#environments-create-wizard-network "environments-create-wizard.md#environments-create-wizard-network").

###### Topics

- [The create new environment wizard](environments-create-wizard.md "environments-create-wizard.md")
- [Clone an Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md")
- [Terminate an Elastic Beanstalk environment](using-features.md "using-features.md")
- [Creating Elastic Beanstalk environments with the AWS
  CLI](environments-create-awscli.md "environments-create-awscli.md")
- [Creating Elastic Beanstalk environments with the API](environments-create-api.md "environments-create-api.md")
- [Constructing a Launch Now URL](launch-now-url.md "launch-now-url.md")
- [Creating and updating groups of Elastic Beanstalk environments](environment-mgmt-compose.md "environment-mgmt-compose.md")
