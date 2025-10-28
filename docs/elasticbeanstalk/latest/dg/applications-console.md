# Elastic Beanstalk application management console

This topic explains how you can use the AWS Elastic Beanstalk console to manage applications, application versions, and saved configurations.

###### To access the application management console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Applications**, and then choose your application's name from the list.

The application overview page shows a list with an overview of all environments associated with the application. 3. You have a few ways to continue:

    1. From the **Actions** drop-down menu, you can choose one of the application management actions: **Create
     environment**, **Delete application**, **View application versions**, **View saved
     configurations**, **Restore terminated environment**.


    To launch an environment in this
     application, you can directly choose **Create environment**. For details, see [Creating an Elastic Beanstalk environment](using-features.md "using-features.md").
    2. The page lists the environment name next to applications that are deployed to an environment. Choose an environment name to go to the [environment management console](environments-console.md "environments-console.md") for that environment, where you can configure, monitor, or manage the
     environment.
    3. When you select an application from the list, the left navigation pane lists the application.


    	* Choose **Application versions** following the application name in the navigation pane to view and manage the application
    	 versions for your application.


    	An application version is an uploaded version of your application code. You can upload new versions, deploy an existing version to any of
    	 the application's environments, or delete old versions. For more information, see [Managing application versions](applications-versions.md "applications-versions.md").
    	* Choose **Saved configurations** following the application name in the navigation pane to view and manage configurations
    	 saved from running environments.


    	A saved configuration is a collection of settings that you can use to restore an environment's settings to a previous state, or to create an
    	 environment with the same settings. For more information see [Using Elastic Beanstalk saved configurations](environment-configuration-savedconfig.md "environment-configuration-savedconfig.md").
