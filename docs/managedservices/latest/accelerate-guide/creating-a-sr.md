# Creating a service request in Accelerate

To create a service request, follow these steps:

1. From the AMS Accelerate console, browse to [Dashboard](https://console.aws.amazon.com/managedservices/dashboard "https://console.aws.amazon.com/managedservices/dashboard").
2. Choose **Open a service request**, the **AMS – Service Request** is pre-selected.
3. Choose a **Category**.
4. Choose **Severity** (Plus or Premium tiers only).
5. Enter information for:
   - **Subject**: A descriptive title for the service request.
   - **Description**: A comprehensive description of the service request,
     the systems impacted, and the expected outcome of a resolution.

6. To add an attachment, choose **Attach files**, browse to the attachment you
   want, and choose **Open**. To delete the attachment, choose the delete icon
   ![Blue circular icon with a white X symbol in the center.](images/icon-delete-attachment.png)
7. **Contact us**: The default contact AMS through the web. To select other options:
   - **Preferred contact language**: English is the supported
     language for AMS Accelerate service requests.
   - **Web**: Your service request is submitted through the web
     and handled by the AMS operations team.
   - **Chat**: Chat online with an AMS Accelerate operations
     representative. This option adds you to the chat queue.
   - **Phone**: An AMS operations representative calls you back.
     Enter your AWS Region, phone number, and extension if applicable.
   - **Additional contacts**: Enter any additional email addresses
     you want copied on your service request.

8. Choose **Submit**.

A case details page opens with information on the service request, such as
**Type**, **Subject**, **Created**,
**ID**, and **Status**. Plus,
a **Correspondence** area that includes the description of the
request you create.

To open a correspondence area and provide additional details or updates in status, choose **Reply**.

After the service request has been resolved, choose **Resolve Case**.

If there are so many correspondences that they don't all appear on the page,
choose **Load More**.

Be sure to rate the service through the 1-5 star rating to let AMS know how
we're doing.

###### Note

If you're going to test service request functionality, we recommend you add a no-action flag
to your service request's subject, such as `AMSTestNoOpsActionRequired`. Then
you can test without starting the service request resolution process.

The AMS Accelerate team receives service requests created by you programmatically using the
[AWS Support API](../../../awssupport/latest/user/Welcome.md "../../../awssupport/latest/user/Welcome.md")
with service code `service-ams-operations-service-request`.
