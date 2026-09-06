

# Prerequisites
<a name="producersdk-android-prerequisites"></a>

We recommend [Android Studio](https://developer.android.com/studio/index.html) for examining, editing, and running the application code. We recommend using the latest stable version.

In the sample code, you provide Amazon Cognito credentials.

**Topics**
+ [Set up a user pool](#set-up-user-pool)
+ [Set up an identity pool](#set-up-identity-pool)

## Set up a user pool
<a name="set-up-user-pool"></a>

**To set up a user pool**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home) and verify the region is correct.

1. In the navigation on the left choose **User pools**.

1. In the **User pools** section, choose **Create user pool**.

1. Complete the following sections:

   1. **Step 1: Configure sign-in experience** - In the **Cognito user pool sign-in options** section, select the appropriate options.

      Select **Next**.

   1. **Step 2: Configure security requirements** - Select the appropriate options.

      Select **Next**.

   1. **Step 3: Configure sign-up experience** - Select the appropriate options.

      Select **Next**.

   1. **Step 4: Configure message delivery** - Select the appropriate options.

      In the **IAM role selection** field, select an existing role or create a new role.

      Select **Next**.

   1. **Step 5: Integrate your app** - Select the appropriate options.

      In the **Initial app client** field, choose **Confidential client**.

      Select **Next**.

   1. **Step 6: Review and create** - Review your selections from the previous sections, then choose **Create user pool**.

1. On the **User pools** page, select the pool that you just created.

   Copy the **User pool ID** and make note of this for later. In the `awsconfiguration.json` file, this is `CognitoUserPool.Default.PoolId`.

1. Select the **App integration** tab and go to the bottom of the page.

1. In the **App client list** section, choose the **App client name** you just created.

   Copy the **Client ID** and make note of this for later. In the `awsconfiguration.json` file, this is `CognitoUserPool.Default.AppClientId`.

1. Show the **Client secret** and make note of this for later. In the `awsconfiguration.json` file, this is `CognitoUserPool.Default.AppClientSecret`.

## Set up an identity pool
<a name="set-up-identity-pool"></a>

**To set up an identity pool**

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home) and verify the region is correct.

1. In the navigation on the left choose **Identity pools**.

1. Choose **Create identity pool**.

1. Configure the identity pool.

   1. **Step 1: Configure identity pool trust** - Complete the following sections:
      + **User access** - Select **Authenticated access**
      + **Authenticated identity sources** - Select **Amazon Cognito user pool**

      Select **Next**.

   1. **Step 2: Configure permissions** - In the **Authenticated role** section, complete the following fields:
      + **IAM role** - Select **Create a new IAM role**
      + **IAM role name** - Enter a name and make note of it for a later step.

      Select **Next**.

   1. **Step 3: Connect identity providers** - In the **User pool details** section complete the following fields: 
      + **User pool ID** - Select the user pool you created earlier.
      + **App client ID** - Select the app client ID you created earlier.

      Select **Next**.

   1. **Step 4: Configure properties** - Type a name in the **Identity pool name** field.

      Select **Next**.

   1. **Step 5: Review and create** - Review your selections in each of the sections, then select **Create identity pool**.

1. On the **Identity pools** page, select your new identity pool.

   Copy the **Identity pool ID** and make note of this for later. In the `awsconfiguration.json` file, this is `CredentialsProvider.CognitoIdentity.Default.PoolId`.

1. Update the permissions for the IAM role.

   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

   1. In the navigation on the left, choose **Roles**.

   1. Find and select the role you created above.
**Note**  
Use the search bar, if needed.

   1. Select the attached permissions policy.

      Select **Edit**.

   1. Select the **JSON** tab and replace the policy with the following:

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Action": [
                      "cognito-identity:*",
                      "kinesisvideo:*"
                  ],
                  "Resource": [
                      "*"
                  ]
              }
          ]
      }
      ```

------

      Select **Next**.

   1. Select the box next to **Set this new version as the default** if it isn't already selected.

      Select **Save changes**.