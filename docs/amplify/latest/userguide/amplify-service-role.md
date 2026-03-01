# Adding a service role with permissions to deploy backend resources

Amplify requires permissions to deploy backend resources with your front end. You use
a service role to accomplish this. A service role is the AWS Identity and Access Management (IAM) role that
provides Amplify Hosting with permissions to deploy, create, and manage backends on your
behalf.

When you are creating a new app that requires an IAM service role, you can either
allow Amplify Hosting to automatically create a service role for you or you can select an
IAM role that you have already created. In this section, you will learn how to create an
Amplify service role that has account administrative permissions and explicity allows
direct access to resources that Amplify applications require to deploy, create, and
manage backends.

## Creating an Amplify service role in the IAM console

###### To create a service role

1. [Open the IAM console](https://console.aws.amazon.com/iam/home?#/roles "https://console.aws.amazon.com/iam/home?#/roles")
   and choose **Roles** from the left navigation bar,
   then choose **Create role**.
2. On the **Select trusted entity** page, choose **AWS
   service**. For **Use case**, select \*\*Amplify

- Backend Deployment**, then choose **Next\*\*.

3. On the **Add permissions** page, choose
   **Next**.
4. On the **Name, view, and create** page, for **Role
   name** enter a meaningful name, such as
   `AmplifyConsoleServiceRole-AmplifyRole`.
5. Accept all the defaults and choose **Create role**.
6. Return to the Amplify console to attach the role to your app.
   - If you are in the process of deploying a new app, do the
     following:
     1. Refresh the list of service roles.
     2. Select the role you just created. For this example, it should look
        like
        **AmplifyConsoleServiceRole-AmplifyRole**.
     3. Choose **Next** and follow the steps to complete
        your app deployment.

   - If you have an existing app, do the following:
     1. In the navigation pane, choose **App settings**,
        then choose **IAM roles**.
     2. On the **IAM roles** page, in the
        **Service role** section, choose
        **Edit**.
     3. On the **Service role** page, select the role you
        just created from the **Service role** list.
     4. Choose **Save**.

7. Amplify now has permissions to deploy backend resources for your app.

## Editing a service role's trust policy to prevent confused deputy

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the
action. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

Currently, the default trust policy for the `Amplify-Backend Deployment`
service role enforces the `aws:SourceArn` and `aws:SourceAccount`
global context condition keys to prevent against confused deputy. However, if you
previously created an `Amplify-Backend Deployment` role in your account, you
can update the role's trust policy to add these conditions to protect against confused
deputy.

Use the following example to restrict access to apps in your account. Replace the
Region and application ID in the example with your own information.

```
"Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:amplify:`us-east-1`:`123456789012`:apps/*"
      },
      "StringEquals": {
        "aws:SourceAccount": "`123456789012`"
      }
    }

```

For instructions on editing the trust policy for a role using the AWS Management Console, see
[Modifying a role
(console)](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md") in the _IAM User Guide_.
