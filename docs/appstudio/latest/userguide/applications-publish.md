# Publishing applications

When you've finished creating and configuring your application the next step is to publish it to test data transfers or share it with end users.
To understand publishing applications in App Studio,
it's important to understand the available environments. App Studio provides three separate environments, which are described in the following list:

1. **Development**: Where you build and preview your application. You do not need to publish to the Development environment, as the
   latest version of your application is hosted there automatically. No live data or third-party services or resources are available in this environment.
2. **Testing**: Where you can perform comprehensive testing of your application. In the Testing environment, you can connect to,
   send data to, and receive data from other services.
3. **Production**: The live operational environment for end-user consumption.
   All of your app building takes place in the **Development** environment. Then, publish to the
   **Testing** environment to test data transfer between other services, and user acceptance testing (UAT) by providing an access
   URL to end users. Afterwards, publish your app to the **Production** environment to perform final tests before sharing it
   with users. For more information about the application environments, see [Application environments](#application-environments "#application-environments").

When you publish an application, it is not available for users until it is shared. This
gives you the opportunity to use and test the application in the Testing and Production environments before users can access it.
When you publish an application to Production that has previously been published and shared, the version that is available to users is updated.

## Publishing applications

Use the following procedure to publish an App Studio application to the Testing or Production environment.

###### To publish an application to Testing or Production environment

1. In the navigation pane, choose **My applications** in the **Build** section.
   You will be taken to a page displaying a list of applications that you have access to.
2. Choose **Edit** for the application you want to publish.
3. Choose **Publish** in the top-right corner.
4. In the **Publish your updates** dialog box:
   1. Review the information about publishing an application.
   2. (Optional) In **Version description**, include a description of this version of the application.
   3. Choose the box to acknowledge the information about the environment.
   4. Choose **Start**. It can take up to 15 minutes for the application to be updated in the live environment.

5. For information about viewing applications in the Testing or Production environments, see [Viewing published applications](#application-viewing-published "#application-viewing-published").

###### Note

Using the application in the Testing or Production environment will result in live data transfer, such as creating records in tables of data sources that
have been connected with connectors.

Published applications that have never been shared will not be available to users or other builders. To make an application available to users,
you must share it after publishing. For more information, see [Sharing published applications](application-share.md "application-share.md").

## Viewing published applications

You can view applications published to the Testing and Production environments to test the application before sharing it with end users or other builders.

###### To view published applications in the Testing or Production environment

1. If necessary, navigate to the application studio of the application you want to preview:
   1. In the navigation pane, choose **My applications** in the **Build** section.
   2. Choose **Edit** for the application.

2. Choose the dropdown arrow next to **Publish** in the top-right corner and choose **Publish Center**.
3. From the publishing center, you can view the environments that your application is published to. If your application is published to the Testing
   or Production environments, you can view the app using the **URL** link for each environment.

###### Note

Using the application in the Testing or Production environment will result in live data transfer, such as creating records in tables of data sources that
have been connected with connectors.

## Application environments

AWS App Studio provides application lifecycle management (ALM) capabilities
with three separate environments - Development, Testing, and Production. This helps you more easily
best practices such as maintaining separate environments, version control, sharing, and
monitoring across the entire app lifecycle.

### Development environment

The **Development** environment is an isolated sandbox where you can
build apps without connecting to any live data sources or services using the application studio and sample data.
In the Development environment, you can preview your app to view and test the app without compromising production data.

Although
your app doesn't connect to other services in the Development environment, you can configure different resources in your app to
mimic live data connectors and automations.

There is a collapsible debug panel that includes errors and warnings at the bottom of the application studio
in the Development environment to help you inspect and debug the app as you build. For more information about troubleshooting and debugging
apps, see [Troubleshooting and debugging App Studio](troubleshooting-and-debugging.md "troubleshooting-and-debugging.md").

### Testing environment

Once your initial app development is complete, the next step is to publish to the
**Testing** environment. While in the Testing environment, your app can connect to, send data to, and
receive data from other services. Therefore, you can use this environment to perform comprehensive testing including user acceptance testing (UAT) by providing an access
URL to end users.

###### Note

Your initial publish to the Testing environment may take up to 15 minutes.

The version of your app published to the Testing environment will be removed after 3 hours of end-user
inactivity. However, all versions persist and can be restored from the **Version History** tab.

Key features of the Testing environment are as follows:

- Integration testing with live data sources and APIs
- User acceptance testing (UAT) facilitated through controlled access
- Environment for gathering feedback and addressing issues
- Ability to inspect and debug both client-side and server-side activities using browser consoles and developer tools.

For more information about troubleshooting and debugging apps, see [Troubleshooting and debugging App Studio](troubleshooting-and-debugging.md "troubleshooting-and-debugging.md").

### Production environment

After you have tested and fixed any issues, you can promote the version of your application from the Testing
environment to the Production environment for live operational use. Although the Production environment is the
live operational environment for end-user consumption, you can test the published version before sharing it with users.

Your published version in the Production environment will be removed after 14 days of end-user inactivity.
However, all versions persist and can be restored from the **Version History** tab.

Key features of the Production environment are as follows:

- Live operational environment for end-user consumption
- Granular role-based access control
- Version control and rollback capabilities
- Ability to inspect and debug client-side activities only
- Uses live connectors, data, automations, and APIs

## Versioning and release management

App Studio provides version control and release management capabilities through
its versioning system in the **Publish center**.

Key versioning capabilities:

- Publishing to the Testing environment generates new version numbers (1.0, 2.0, 3.0...).
- The version number does not change when promoting from the Testing to Production environment.
- You can roll back to any previous version from **Version History**.
- Applications published to the Testing environment are paused after 3 hours of inactivity.
  Versions are persisted and can be restored from **Version History**.
- Applications published to the Production environment are removed after 14 days of inactivity.
  Versions are persisted and can be restored from **Version History**.

This versioning model allows for rapid iteration while maintaining
traceability, rollback capabilities, and optimal performance across the app development and testing cycle.

## Maintenance and operations

App Studio may need to automatically republish your application to address certain maintenance tasks, operational activities,
and to incorporate new software libraries. No action is needed from you, the builder, but end users may need to log back into the
application. In certain situations, we may need you to republish your application to incorporate new features and libraries which
we cannot automatically add ourselves. You will need to resolve any errors and review warnings before republishing.
