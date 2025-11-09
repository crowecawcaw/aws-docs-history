# More Elastic Beanstalk example applications and tutorials for Java

This section provides additional applications and tutorials. The [QuickStart for Java](java-quickstart.md "java-quickstart.md") and [QuickStart for Java on Tomcat](tomcat-quickstart.md "tomcat-quickstart.md") topics located earlier in this topic walk you through launching a sample
Java application with the EB CLI.

To get started with Java applications on AWS Elastic Beanstalk, all you need is an application [source
bundle](applications-sourcebundle.md "applications-sourcebundle.md") to upload as your first application version and to deploy to an environment. When you create an environment, Elastic Beanstalk allocates all of the
AWS resources needed to run a scalable web application.

## Launching an environment with a sample Java application

Elastic Beanstalk provides single page sample applications for each platform as well as more complex examples that show the use of additional AWS resources such
as Amazon RDS and language or platform-specific features and APIs.

The single page samples are the same code that you get when you create an environment without supplying your own source code. The more complex
examples are hosted on GitHub and may need to be compiled or built prior to deploying to an Elastic Beanstalk environment.

| Samples                | Name                                              | Supported versions   | Environment type                                                                                                              | Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------------------- | ------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Tomcat (single page)   | All \*Tomcat with Corretto<br>• platform branches | Web Server<br>Worker | [tomcat.zip](samples/tomcat.md "samples/tomcat.md")                                                                           | Tomcat web application with a single page (`index.jsp`) configured to be displayed at the website root.<br>For [worker environments](using-features-managing-env-tiers.md "using-features-managing-env-tiers.md"), this sample includes a `cron.yaml` file<br>that configures a scheduled task that calls `scheduled.jsp` once per minute. When `scheduled.jsp` is<br>called, it writes to a log file at `/tmp/sample-app.log`. Finally, a configuration file is included in<br>`.ebextensions` that copies the logs from `/tmp/` to the locations read by Elastic Beanstalk when you request<br>environment logs.<br>If you [enable X-Ray integration](environment-configuration-debugging.md "environment-configuration-debugging.md") on an environment running this sample, the<br>application shows additional content regarding X-Ray and provides an option to generate debug information that you can view in the X-Ray<br>console.                                                                                                                                                                                                                                                                                                 |
| Corretto (single page) | Corretto 11<br>Corretto 8                         | Web Server           | [corretto.zip](samples/corretto.md "samples/corretto.md")                                                                     | Corretto application with `Buildfile` and `Procfile` configuration files.<br>If you [enable X-Ray integration](environment-configuration-debugging.md "environment-configuration-debugging.md") on an environment running this sample, the<br>application shows additional content regarding X-Ray and provides an option to generate debug information that you can view in the X-Ray<br>console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Scorekeep              | Java 8                                            | Web Server           | [Clone the repo at GitHub.com](https://github.com/awslabs/eb-java-scorekeep "https://github.com/awslabs/eb-java-scorekeep")   | \*Scorekeep<br>• is a RESTful web API that uses the Spring framework to provide an interface for creating and managing users,<br>sessions, and games. The API is bundles with an Angular 1.5 web app that consumes the API over HTTP.<br>The application uses features of the Java SE platform to download dependencies and build on-instance, minimizing the size of the souce<br>bundle. The application also includes nginx configuration files that override the default configuration to serve the frontend web app statically<br>on port 80 through the proxy, and route requests to paths under `/api` to the API running on `localhost:5000`.<br>Scorekeep also includes an `xray` branch that shows how to instrument a Java application for use with AWS X-Ray. It shows<br>instrumentation of incoming HTTP requests with a servlet filter, automatic and manual AWS SDK client instrumentation, recorder configuration,<br>and instrumentation of outgoing HTTP requests and SQL clients.<br>See the readme for instructions or use the [AWS X-Ray getting started tutorial](../../../xray/latest/devguide/xray-gettingstarted.md "../../../xray/latest/devguide/xray-gettingstarted.md")<br>to try the application with X-Ray. |
| Does it Have Snakes?   | Tomcat 8 with Java 8                              | Web Server           | [Clone the repo at GitHub.com](https://github.com/awslabs/eb-tomcat-snakes "https://github.com/awslabs/eb-tomcat-snakes")     | \*Does it Have Snakes?<br>• is a Tomcat web application that shows the use of Elastic Beanstalk configuration files, Amazon RDS,<br>JDBC, PostgreSQL, Servlets, JSPs, Simple Tag Support, Tag Files, Log4J, Bootstrap, and Jackson.<br>The source code for this project includes a minimal build script that compiles the servlets and models into class files and packages the<br>required files into a Web Archive that you can deploy to an Elastic Beanstalk environment. See the readme file in the project repository for<br>full instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Locust Load Generator  | Java 8                                            | Web Server           | [Clone the repo at GitHub.com](https://github.com/awslabs/eb-locustio-sample "https://github.com/awslabs/eb-locustio-sample") | Web application that you can use to load test another web application running in a different Elastic Beanstalk environment. Shows the use of<br>`Buildfile` and `Procfile` files, DynamoDB, and [Locust](http://locust.io/ "http://locust.io/"), an open<br>source load testing tool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

Download any of the sample applications and deploy it to Elastic Beanstalk by following these steps:

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

## Next steps

After you have an environment running an application, you can [deploy a new version](using-features.md "using-features.md") of
the application or a completely different application at any time. Deploying a new application version is very quick because it doesn't require
provisioning or restarting EC2 instances.

After you've deployed a sample application or two and are ready to start developing and running Java applications locally, see [the next section](java-development-environment.md "java-development-environment.md") to set up a Java development environment with all of the tools and libraries that you
will need.
