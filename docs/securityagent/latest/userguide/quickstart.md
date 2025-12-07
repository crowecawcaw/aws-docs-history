# Quickstart: Run a penetration test

This quickstart walks you through running your first penetration test (pentest) with AWS Security Agent. AWS Security Agent tests your deployed application and identifies security vulnerabilities with detailed findings.

###### Note

You need access to AWS Management console to setup a new penetration test

## Step 1: Set up AWS Security Agent in the AWS console

1. Navigate to [AWS Security Agent](https://us-east-1.console.aws.amazon.com/securityagent/ "https://us-east-1.console.aws.amazon.com/securityagent/") in the AWS Management Console.
2. Select **Set up AWS Security Agent**
3. Create an agent space. An agent space can be used by multiple users and should be specific for every application you want to test. Enter a name and description for your first agent space. This name appears to users in the web application. The name of the agent space should be based on the application you want to penetration test.
4. Select **IAM Users** under _User access configuration_
   - This quickstart does not cover enabling single sign-on (SSO) with IAM Identity Center. This allows users to directly access the AWS Security Agent web application, from the AWS Console.
   - If you want to enable users without AWS Management Console Access to perform tasks such as starting a penetration test or design review, you should enable the IAM Identity Center integration.

5. Click **Set up AWS Security Agent**

###### Note

When you choose Set up, AWS Security Agent will create your Agent Space, and establish a web application where your users can carry out design reviews and penetration tests.

## Step 2: Enable and configure penetration testing

###### Note

In the AWS console, you define the scope of what can be tested. Users then run specific penetration tests within that scope from the AWS Security Agent web application.

1. From the left sidebar, select **Agent Spaces** and then select the Agent Space you created in Step 1.
2. From the header, select **Enable penetration test** to enable this capability.
3. Specify the target domains. The target domain should be live, and host the application you want to penetration test. You will need to verify ownership of the target domains once you complete the pentest setup.
   - AWS Security Agent can only test validated domains.
   - Domains registered in Route 53 are validated automatically.
   - For domains outside Route 53, manually validate them using a `TXT` record.

4. Select the default role with the necessary permissions policies. You can also optionally customize the role AWS Security Agent will use to interact with AWS Services. However, AWS Security agent recommends using the default role.

## Step 3: Connect to GitHub (optional)

###### Note

This step is optional, however we recommend connecting to your GitHub account to give AWS Security Agent access to the source code for your application. This helps the Security Agent understand your application context and improve penetration testing coverage.

1. Once you have completed the pentest setup, you will see a banner with an option to connect GitHub for penetration testing, click **Add** in the right side of the banner.
2. Click **Create new registration**
3. Select **GitHub** and then **Next**
4. Click **Install and authorize**. You’ll be redirected to GitHub to complete the installation.
   1. Select the _GitHub User_ or _GitHub Organization_ that owns the repository you want to test.
   2. Select either **All repositories** or **Only select repositories**. AWS suggests installing AWS Security Agent on all repositories, and then creating a unique agent space for each repository you want to test.
   3. Select **Install & Authorize** and complete GitHub authentication.

5. Define the **Registration Name** and confirm the **account type** matches where you installed the GitHub application.
6. Click **Next**
7. Select the repositories you want to be associated for penetration testing. This allows the web application users to associate these repositories to a penetration test, when they create a new pentest.
8. Click **Next**
9. If you want to enable automatic code remediation, enable **Pentest remediation enabled** on the repositories you want to allow AWS Security Agent to create pull requests with ready-to-implement code fix for pentest findings.
10. Click **Connect**

## Step 4: Run a penetration test

###### Note

You can create and run a penetration test only in the AWS Security Agent web application.

1. Select the **Web app** tab and then **Admin access** to launch the AWS Security Agent Web Application with administrator privileges. This will only work if you had setup your agent using **IAM Users** under _User access configuration_. Alternatively, you will need to add users and create a login.
2. In the left sidebar, click **Penetration Test**, then select **Create your first penetration test**.
3. Define the penetration test details:
   1. Select the domain you want to test or specify one or more paths. You can only test verified domains.
   2. If your application needs to access URLs that are outside of your target domain, including for login purposes, then please add all the URLs to the **Additional allowed URLs** field.
      NOTE: **Additional allowed URLs** is outside the scope of pentesting, and is accessed for tasks such as login.
   3. Select the IAM role and log group AWS Security Agent should use to store logs. If you do not select a log group, AWS Security agent will create a log group at the start of the pentest run.
   4. Select **Enable automatic code remediation** to allow AWS Security Agent to automatically create a pull request with ready-to-implement code fix for all the pentest findings.
   5. Click **Next**.

4. (Optional) If your application requires a login, then input the credentials directly into the web application. Define how AWS Security Agent should authenticate to your application. Provide authentication instructions into **Agent Space login prompt**, then click **Next**.
5. (Optional) Provide additional resources to help test your application. You can upload files such as design documents, threat model, API specifications or other documents that are helpful to understand the application context.
6. Click **Create and execute**. You’ll be redirected to the penetration test detail screen.
   - To save the configuration for future use without running it immediately, click **Create penetration test** instead.

## Step 5: Review penetration test findings

1. The penetration test can take up to several hours to complete.
2. Once complete, review the details of the pentest on the Pentest overview, logs and findings screens.
