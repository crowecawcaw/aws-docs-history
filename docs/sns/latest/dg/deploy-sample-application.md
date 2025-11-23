# Step 1: Deploying the sample Amazon SNS

application

1.  Sign in to the [AWS Lambda
    console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2.  On the navigation panel, choose **Functions** and then choose
    **Create function**.
3.  On the **Create function** page, do the following:
    1. Choose **Browse serverless app repository**,
       **Public applications**, **Show apps that
       create custom IAM roles or resource policies**.
    2. Search for `fork-example-ecommerce-checkout-api` and then
       choose the application.

4.  On the **fork-example-ecommerce-checkout-api** page, do the
    following:
    1. In the **Application settings** section, enter an
       **Application name** (for example,
       `fork-example-ecommerce-my-app`).

    ###### Note

        * To find your resources easily later, keep the prefix
         `fork-example-ecommerce`.
        * For each deployment, the application name must be unique.
         If you reuse an application name, the deployment will update
         only the previously deployed CloudFormation stack (rather than create
         a new one).

    2. (Optional) Enter one of the following **LogLevel**
       settings for the execution of your application's Lambda function:
       - `DEBUG`
       - `ERROR`
       - `INFO` (default)
       - `WARNING`

5.  Choose **I acknowledge that this app creates custom IAM roles,
    resource policies and deploys nested applications.** and then, at
    the bottom of the page, choose **Deploy**.
    On the **Deployment status for
    fork-example-ecommerce-`my-app`** page, Lambda
    displays the **Your application is being deployed** status.

In the **Resources** section, CloudFormation begins to create the stack and
displays the **CREATE_IN_PROGRESS** status for each resource. When the
process is complete, CloudFormation displays the **CREATE_COMPLETE**
status.

###### Note

It might take 20-30 minutes for all resources to be deployed.

When the deployment is complete, Lambda displays the **Your application has
been deployed** status.
