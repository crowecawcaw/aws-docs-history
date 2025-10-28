# Create an environment using a custom AWS

service blueprint

Complete the following procedure to create an environment using a custom AWS service
blueprint.

1. Sign in to the AWS Management Console and open the Amazon DataZone management
   console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose **View domains** and choose the domain in which your
   custom AWS service blueprint is enabled.
3. Choose the **Blueprints** tab, then choose the enabled
   **AWS service** bluepint, and then choose
   **Create environment**.
4. On the **Create environment** page, specify the following and
   then choose **Create environment**:
   - **Name** - specify the name for the
     environment.
   - **Description** - specify the description for the
     environment.
   - **Project** - specify a new or existing owning
     project for the environment. Projects enable groups of users to
     discover, publish, subscribe to, and consume assets in Amazon DataZone. This
     environment will be available to all the members of the specified
     project. All environments are owned by projects whose users have access
     to the environment.
   - **Environment role** - specify an existing IAM role
     that will grant Amazon DataZone access to your existing AWS services and
     resources, such as Amazon S3 and AWS Glue, in this environment.

   ###### Note

   Amazon DataZone does not provision this role for you. You must have an
   existing IAM role with permissions to your existing AWS services
   and resources that you want to enable in this environment.

   Make sure that this IAM role has the minimum required permissions,
   in other words, is scoped down to provide access only to the AWS
   services and resources that you want to enable in this
   environment.

   You can use the AWS Policy Generator to build a policy that fits
   your requirements and attach it to the custom IAM role you want to
   use.

   Make sure the role begins with `AmazonDataZone` to
   follow conventions. This is not mandatory, but recommended. If the
   IAM administrator is using the `AmazonDataZoneFullAccess`
   policy, you must follow this convention because there is a pass role
   check validation.

   When you create your custom role, make sure that it trusts
   `datazone.amazonaws.com` in its trust policy:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": [
    "datazone.amazonaws.com"
    ]
    },
    "Action": [
    "sts:AssumeRole",
    "sts:TagSession"
    ]
    }
    ]
   }`

   ```

   - **AWS region** - specify an AWS region in which
     you want to create this environment.
