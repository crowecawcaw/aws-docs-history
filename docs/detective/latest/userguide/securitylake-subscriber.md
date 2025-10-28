# Step 1: Creating a Security Lake subscriber in Detective

This topic explains how to use the Detective console to create a Security Lake subscriber.

To consume logs and events from Amazon Security Lake, you must be a Security Lake subscriber. A Subscriber
can query and access the data that Security Lake collects. A subscriber with query access can
query AWS Lake Formation tables directly in an Amazon Simple Storage Service (Amazon S3) bucket by using services such as
Amazon Athena. To become a subscriber, the Security Lake administrator has to provide you with
subscriber access that lets you query the data lake. For information about how the
administrator does this, see [Creating a subscriber with query access](../../../security-lake/latest/userguide/subscriber-query-access.md#create-query-subscriber-procedures "../../../security-lake/latest/userguide/subscriber-query-access.md#create-query-subscriber-procedures") in the Amazon Security Lake User Guide.

Follow these steps to create a Security Lake subscriber in order to grant query access to a Detective administrator account.

###### To create a Detective subscriber in Security Lake

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Integrations**.
3. In the Security Lake subscriber pane, note the **Account ID** and
   **External ID** values.

Ask the Security Lake administrator to use these IDs to:

    * To create a Detective subscriber for you in Security Lake.
    * To configure the subscriber
     to have query access.
    * To make sure that the Security Lake query subscriber is created with Lake Formation
     permissions, select **Lake Formation** as the **Data
     Access Method** in the Security Lake console.

When the Security Lake administrator creates a subscriber for you, Security Lake generates an Amazon Resource Share ARN for you. Ask the administrator to send this ARN to you. 4. Enter the **Resource Share ARN** that is provided by the Security Lake administrator in the **Security Lake subscriber** pane. 5. After you receive the Resource Share ARN from the Security Lake Administrator, enter the
ARN in the **Resource Share ARN** box in the **Security Lake
subscriber** pane.
