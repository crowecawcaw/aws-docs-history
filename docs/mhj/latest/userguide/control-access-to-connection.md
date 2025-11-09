AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Controlling member access to account

connections in AWS Migration Hub Journeys

###### Note

The account-connection feature is in preview release. It is available in
US East (N. Virginia).

This is pre-release documentation. Both the account-connection feature and this
documentation are subject to change.

Journey administrators have access to all of the journey's AWS account connections
and can use all of the IAM roles in all of those connections. However, when you add a
member as a JourneyContributor to a journey, that member doesn't get access to the
journey's connections by default. To grant the member access, perform the following
steps.

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration
   journeys**.
3. In the list of migration journeys, choose the name of the journey.
4. Choose the **Individuals and teams** tab.
5. Choose the radio button to the left of the member's name.
6. Choose **Edit role**.
7. Select **Grant this member access to the journey's account
   connections**.

###### Warning

When you grant a member access to a journey's connections, they get access
to all of the connections within that journey, and they can use all of the
IAM roles in all of the journey's connections. 8. Choose **Update**.
