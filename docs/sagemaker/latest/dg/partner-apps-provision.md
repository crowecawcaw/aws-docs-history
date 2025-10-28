# Partner AI App provisioning

After admins have set up the required permissions, they can explore and provision Amazon SageMaker Partner AI Apps
for users in the domain.

Admins can view all of the available Partner AI Apps, as well as the Partner AI Apps that they have
provisioned from the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/"). From
the **Partner AI Apps** page, admins can view details about the pricing model
for each Partner AI App and make them available to users. Admins can make them available by navigating
to the AWS Marketplace to subscribe to that Partner AI App.

Admins can provision new apps from the Partner AI Apps page. They can also view the Partner AI Apps that they
have already provisioned from the **My Apps** tab.

###### Note

Applications that admins provision can be accessed by all users that admins give proper
permissions to in an AWS account. Partner AI Apps are not restricted to a specific domain or
user.

## Status

When admins view a Partner AI App that they have provisioned, they can also see the status of their
application with one of the following values.

- **Deployed** – The application is ready for use.
  Admins can update the application configuration and delete the application.
- **Error** – There was an issue with the application
  deployment. Admins can troubleshoot and configure the application again to deploy
  it.
- **Not deployed** – The application has been subscribed
  to, but not deployed. Admins can configure the application to deploy it.

## Options

When admins configure an application, they can decide the following options:

- **App name** – A unique name for the application.
- **App maintenance schedule** – Partner AI Apps undergo
  maintenance on a weekly basis. With this option, admins choose both the day of the week
  and the time that this maintenance happens.
- **STS identity propagation** – Use this option to pass
  the AWS Security Token Service (AWS STS) launcher IAM session name as the Partner AI App user identity. For more
  information, see [Set up Partner AI Apps](partner-app-onboard.md "partner-app-onboard.md").
- **Admin management** – Some Partner AI Apps support adding up
  to five admins that have full rights to manage the Partner AI App functionality. This only applies
  to Comet and Fiddler. For more information, see [Set up Partner AI Apps](partner-app-onboard.md "partner-app-onboard.md").
- **Execution role** – The role that the Partner AI App uses to
  access resources and perform actions. For more information, see [Set up Partner AI Apps](partner-app-onboard.md "partner-app-onboard.md").
- **App version** – The version of the Partner AI App that
  admins want to use.
- **Tier selection** – The infrastructure deployment
  tier for the Partner AI App. The tier size impacts the speed and capabilities of the application.
  For more information, see [Set up Partner AI Apps](partner-app-onboard.md "partner-app-onboard.md").
- **Lakera S3 bucket policy** – This is only required by
  the Lakera-guard app to access an Amazon S3 bucket.
