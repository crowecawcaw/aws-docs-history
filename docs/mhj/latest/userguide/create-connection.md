AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Creating an AWS account connection in

AWS Migration Hub Journeys

###### Note

The account-connection feature is in preview release. It is available in
US East (N. Virginia).

This is pre-release documentation. Both the account-connection feature and this
documentation are subject to change.

To create an AWS account connection, you first initiate a connection request in the
Migration Hub Journeys console. The next step is for an administrator of the AWS account to accept
the connection request.

###### To initiate an account connection request

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration
   journeys**.
3. In the list of migration journeys, choose the name of the journey for which
   you want to create the account connection.
4. Choose the **Account connections** tab.
5. Choose **Connect account**.
6. For **Connection name** enter a name that can help you and
   other journey members identify this connection.
7. For **AWS account ID** enter the ID of the AWS account to
   which you want to connect the journey. An AWS account ID is a 12-digit
   number.
8. (Optional) Enter a description for this new connection.
9. Choose **Initiate account connection**.
10. Copy the connection ARN. You need this ARN to complete the account
    connection.

###### To accept a connection request

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, choose **Journey
   connections**.
3. Choose **Verify new connection**.
4. Enter the connection ARN that Migration Hub Journeys generated when the connection request
   was initiated.
5. Choose **Accept connection**.
