# Step 4: Set up Amazon Cognito

To manage permissions and users for the web application, you need to set up Amazon Cognito.
Amazon Cognito ensures that the web application is secure and has access control. Amazon Cognito uses
identity pools to provide AWS credentials that grant your users access to other AWS
services. For this tutorial, it provides access to Amazon Lex V2.

When creating an identity pool, Amazon Cognito provides you with AWS Identity and Access Management (IAM) roles for
authenticated and unauthenticated users. You modify the IAM roles by adding policies
that grant access to Amazon Lex V2.

###### To set up Amazon Cognito

1. Sign into the AWS Management Console and open the Amazon Cognito console at [https://console.aws.amazon.com/cognito/](https://console.aws.amazon.com/cognito "https://console.aws.amazon.com/cognito").
2. Choose **Manage Identity Pools**.
3. Choose **Create new identity pool**.
4. Configure the identity pool.
   1. **Identity pool name** – Enter a name that
      indicates the pool's purpose, such as
      `BotPool`.
   2. In the **Unauthenticated identities** section, choose
      **Enable access to unauthenticated
      identities**.

5. Choose **Create Pool**.
6. On the **Identify the IAM roles to use with your new identity
   pool** page, choose **View Details**.
7. Record the IAM role names. You will modify them later.
8. Choose **Allow**.
9. On the **Getting Started with Amazon Cognito** page, for
   **Platform**, choose
   **JavaScript**.
10. In the **Get AWS Credentials** section, find and record the
    **Identity pool ID**.
11. To allow access to Amazon Lex V2, modify the authenticated and unauthenticated IAM
    roles.
    1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. In the navigation pane, under **Access Management**,
       choose **Roles**.
    3. In the search box, enter the name of the authenticated IAM role and
       choose the checkbox next to it.
       1. Choose **Attach policies**.
       2. In the search box, enter
          `AmazonLexRunBotsOnly` and choose the
          checkbox next to it.
       3. Choose **Attach policy**.

    4. Enter the name of the unauthenticated IAM role in the search box and
       choose the checkbox next to it.
       1. Choose **Attach policies**.
       2. In the search box, enter
          `AmazonLexRunBotsOnly` and choose the
          checkbox next to it.
       3. Choose **Attach policy**.

## Next step

[Step 5: Deploy Your Bot as a Web Application](agent-step-5.md "agent-step-5.md")
