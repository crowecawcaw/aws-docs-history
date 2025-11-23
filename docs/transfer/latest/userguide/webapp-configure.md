# Configure a Transfer Family web app

This section describes the procedures for creating a Transfer Family web app. To assign users and groups that can use it, see [Assign or add users or groups to a Transfer Family
web app](webapp-add-users.md "webapp-add-users.md").

###### Note

Repeat these procedures to add additional web apps. You can reuse the IAM roles
that you created earlier. Make sure to add the access endpoints for the new web apps
to each bucket's Cross-origin resource sharing (CORS) policy.

## Create a Transfer Family web app

###### Note

If you are not using the IAM Identity Center directory for your identity provider, don't
attempt to create a web app until you have already set up IAM Identity Center and configured a
third party identity provider, as described in [Configure your identity provider for Transfer Family web
apps](webapp-identity-center.md "webapp-identity-center.md").

Complete the following steps to create a Transfer Family web app.

###### To create a Transfer Family web app

1. Sign in to the AWS Management Console and open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Web apps**.
3. Choose **Create web app**.

For authentication access, the pane is populated as follows.

    * If you have already created either an organization or account
     instance in AWS IAM Identity Center, then you see this message: **Your
     AWS Transfer Family application connected to an account instance of
     IAM Identity Center**.
    * If you already have an account instance and are a member of an
     organization instance, you have the option to choose which instance
     to connect.
    * If you don't already have an account instance, or are a member in
     an organization instance, you're presented with the options to
     create an account instance.

4. For **Endpoint type**, choose the **Publicly accessible** endpoint type. For a **VPC hosted** endpoint, see [Create a Transfer Family web app in a VPC](create-webapp-in-vpc.md "create-webapp-in-vpc.md").
5. In the **Permission type** pane, you can use a previously
   created role, or have the service create one for you.
   - If you have already created an identity bearer role, choose
     **Use an existing role** and choose your role
     from the **Select an existing role** menu.
   - To have the service create a role for you, choose **Create
     and use a new service role**.

6. In the **Web app units** pane, choose a value. One web
   app unit allows web app activity from up to 250 unique sessions. When
   creating a web app, you provision how many units you need based on your
   expected peak workload volumes. Changing your web app units has an impact on
   your billing. For information about pricing, see [AWS Transfer Family Pricing](https://aws.amazon.com/aws-transfer-family/pricing "https://aws.amazon.com/aws-transfer-family/pricing").
7. If you are using Transfer Family in an AWS GovCloud (US) Region, you can select the
   **FIPS Enabled endpoint** checkbox in the
   **FIPS Enabled** pane. For all other AWS Regions,
   this option is unavailable.
8. (Optional) Add a tag to help you organize your web apps. We suggest that
   you add a tag with **Name** as the key and a descriptive
   name as the value.
9. Choose **Next**. On this screen, you can optionally
   provide a title for your web app. If you don't provide a title, the default
   title of **Transfer Web App** is supplied. You can also
   upload image files for your logo and favicon.
10. Choose **Next**, then choose **Create web
    app**.

![Screen that shows the Web apps dashboard as well as the menu item for selecting it from the left navigation panel.](images/webapp-transfer-dashboard.png)

###### Note

Make sure to set up a Cross-origin resource sharing (CORS) policy for all of
the buckets that are accessed from the web app endpoint.
