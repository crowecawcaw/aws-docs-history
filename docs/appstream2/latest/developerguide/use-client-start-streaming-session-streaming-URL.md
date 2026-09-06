

# Streaming URL
<a name="use-client-start-streaming-session-streaming-URL"></a>

To create a streaming URL, use one of the following methods:
+ WorkSpaces Applications console
+ The [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) API action 
+ The [create-streaming-url](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-streaming-url.html) AWS CLI command

To create a streaming URL by using the WorkSpaces Applications console, complete the steps in the following procedure.

**To create a streaming URL by using the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the navigation pane, choose **Fleets**.

1. In the list of fleets, choose the fleet that is associated with the stack for which you want to create a streaming URL. Verify that the status of the fleet is **Running**.

1. In the navigation pane, choose **Stacks**. Choose the stack, and then choose **Actions**, **Create streaming URL**.

1. In **User id**, enter the user ID.

1. For **URL Expiration**, choose an expiration time, which determines how long the generated URL is valid. This URL is valid for a maximum of seven days.

1. Choose **Get URL**.

1. Copy the URL, save it to an accessible location, and then provide it to your users.

   In the WorkSpaces Applications client sign-in page, users enter the streaming URL that you created as the web address, and then choose **Connect**. 