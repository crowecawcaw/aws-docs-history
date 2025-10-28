# Configuring application version lifecycle settings

This topic explains the policies and quotas that Elastic Beanstalk applies to the versions of your application in a given environment, including how long an
application version remains in an environment.

Each time you upload a new version of your application with the Elastic Beanstalk console or the EB CLI,
Elastic Beanstalk creates an [application version](applications-versions.md "applications-versions.md"). If you don't
delete versions that you no longer use, you will eventually reach the [application version quota](../../../general/latest/gr/elasticbeanstalk.md#limits_elastic_beanstalk "../../../general/latest/gr/elasticbeanstalk.md#limits_elastic_beanstalk") and be unable to create new versions of that
application.

You can avoid hitting the quota by applying an _application version lifecycle
policy_ to your applications. A lifecycle policy tells Elastic Beanstalk to delete application
versions that are old, or to delete application versions when the total number of versions for
an application exceeds a specified number.

Elastic Beanstalk applies an application's lifecycle policy each time you create a new application
version, and deletes up to 100 versions each time the lifecycle policy is applied. Elastic Beanstalk deletes
old versions after creating the new version, and does not count the new version towards the
maximum number of versions defined in the policy.

Elastic Beanstalk does not delete application versions that are currently being used by an environment,
or application versions deployed to environments that were terminated less than ten weeks before
the policy was triggered.

The application version quota applies across all applications in a region. If you have several applications, configure each application with a lifecycle
policy appropriate to avoid reaching the quota. For example, if you have 10 applications in a region and the quota is 1,000 application versions, consider
setting a lifecycle policy with a quota of 99 application versions for all applications, or set other values in each application as long as the total is
less than 1,000 application versions. Elastic Beanstalk only applies the policy if the application version creation succeeds, so if you have already reached the quota,
you must delete some versions manually prior to creating a new version.

By default, Elastic Beanstalk leaves the application version's [source bundle](applications-sourcebundle.md "applications-sourcebundle.md") in Amazon S3 to prevent loss of data. You can delete the source bundle to
save space.

You can set the lifecycle settings through the Elastic Beanstalk CLI and APIs. See
[eb appversion](eb3-appversion.md "eb3-appversion.md"),
[CreateApplication](../api/API_CreateApplication.md "../api/API_CreateApplication.md") (using the `ResourceLifecycleConfig` parameter), and
[UpdateApplicationResourceLifecycle](../api/API_UpdateApplicationResourceLifecycle.md "../api/API_UpdateApplicationResourceLifecycle.md")
for details.

## Setting the application lifecycle settings in the console

You can specify the lifecycle settings in the Elastic Beanstalk console.

###### To specify your application lifecycle settings

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Applications**, and then choose your application's name from the list.
3. In the navigation pane, find your application's name and choose **Application versions**.
4. Choose **Settings**.
5. Use the on-screen form to configure application lifecycle settings.
6. Choose **Save**.

On the settings page, you can do the following.

- Configure lifecycle settings based on the total count of application versions or the age of application versions.
- Specify whether to delete the source bundle from S3 when the application version is deleted.
- Specify the service role under which the application version is deleted. To include all permissions required for version deletion, choose the
  default Elastic Beanstalk service role, named `aws-elasticbeanstalk-service-role`, or another service role using the Elastic Beanstalk managed service policies.
  For more information, see [Managing Elastic Beanstalk service roles](iam-servicerole.md "iam-servicerole.md").
