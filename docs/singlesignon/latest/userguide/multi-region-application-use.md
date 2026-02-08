# Deploying and managing applications across multiple AWS

Regions

The topic of application access through IAM Identity Center is covered extensively in [Configure access to applications](manage-your-applications.md "manage-your-applications.md"). This section provides additional details relevant to
the deployment and management of applications across multiple AWS Regions.

## Deploying and managing AWS managed applications across multiple AWS Regions

With a single-Region IAM Identity Center instance, you can deploy AWS managed applications in the same
Region as your instance. Some applications such as Amazon Q Business support a cross-Region
connection to IAM Identity Center, which enables their deployment outside the IAM Identity Center's Region if the
application of interest is available there. However, cross-Region calls can cause slower
application performance, and most AWS managed applications don't support this type of
connection.

A multi-Region IAM Identity Center instance lets you deploy AWS managed applications in any enabled
Region with a connection to IAM Identity Center in the same Region ("Region-local connection"). This
requires that the AWS managed application is available in the Region and supports
deployment in additional Regions. With a Region-local connection to IAM Identity Center, AWS managed
applications access workforce identities in the same Region for optimal performance and
reliability. We recommend choosing a Region-local connection when deploying an AWS managed
application whenever the [prerequisites](multi-region-iam-identity-center.md#multi-region-prerequisites "multi-region-iam-identity-center.md#multi-region-prerequisites") are
met.

To deploy an AWS managed application in an additional Region of IAM Identity Center, start the
deployment in that Region through the application console or API in the same way that you
deploy in the primary Region.

**Considerations:**

- If you haven't replicated your IAM Identity Center to that Region yet, we recommend that you do this
  first so that the application deployment can complete right away.
- AWS managed applications will, in many cases, automatically establish a Region-local
  connection if you've already replicated IAM Identity Center to the Region.
- If an AWS managed application offers a cross-Region connection to IAM Identity Center, we
  recommend that you choose a Region-local connection provided that the [prerequisites](multi-region-iam-identity-center.md#multi-region-prerequisites "multi-region-iam-identity-center.md#multi-region-prerequisites") are met.
- If the application doesn't support deployment in additional Regions, you can deploy
  it in the primary Region
  provided that the application is available there.

###### Important

If your IAM Identity Center instance is multi-regional, all AWS managed applications in use by
your organization must support IAM Identity Center configured with a customer-managed KMS key regardless
of the application deployment Region. Confirm this in the [AWS managed applications
that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md") before deploying an application and
before configuring a customer-managed KMS key in your IAM Identity Center.

### An application's management Region

After you deploy an AWS managed application in an additional Region of IAM Identity Center using a
Region-local connection, you manage the application and its assignments to users and
groups in the same Region. IAM Identity Center replicates the application metadata including assignments
to users and groups to other enabled Regions so that your workforce can launch
applications from any enabled Region.

If your AWS managed application is using a cross-Region connection to IAM Identity Center, you can manage
the application details such as name and description, and application assignments to users and
groups through IAM Identity Center console and API in the connected Region. Regardless of the connection type,
you can manage the application through its console in its deployment Region.

### Trusted identity propagation

You can use trusted identity propagation with AWS managed applications that support it
in any enabled Region of your IAM Identity Center instance.

All applications that propagate identity context to each other must be in the same Region.

### An application’s dependency on its connected IAM Identity Center Region

Each AWS managed application connects to a specific IAM Identity Center Region
during deployment. The application then depends on that Region for user sign-in, even if
your IAM Identity Center is enabled in multiple Regions. If your IAM Identity Center is
experiencing a disruption in that Region, users might not be able to access AWS managed
applications connected to the Region.

## Deploying and managing customer managed applications across multiple AWS Regions

IAM Identity Center supports SAML and OAuth2 [Customer managed applications](customermanagedapps.md "customermanagedapps.md"). You can choose
to create them in any enabled Region of your IAM Identity Center instance. After you create one, you
manage the application and its assignments to users and groups in the same Region.
