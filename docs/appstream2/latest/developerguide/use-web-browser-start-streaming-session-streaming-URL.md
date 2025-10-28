# Streaming URL

To create a streaming URL, use one of the following methods:

- AppStream 2.0 console
- The [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action
- The [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") AWS CLI command
  To create a streaming URL by using the AppStream 2.0 console, complete the steps in the following procedure.

###### To create a streaming URL by using the AppStream 2.0 console

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the navigation pane, choose **Fleets**.
3. In the list of fleets, choose the fleet that is associated with the stack for which you want to create a streaming URL. Verify that the status of the fleet is **Running**.
4. In the navigation pane, choose **Stacks**. Choose
   the stack, and then choose **Actions**,
   **Create streaming URL**.
5. In **User id**, enter the user ID.
6. For **URL Expiration**, choose an expiration time, which determines how long the generated URL is valid. This URL is valid for a maximum of seven days.
7. Choose **Get URL**.
8. Copy the URL, save it to an accessible location, and then provide it to your users.
