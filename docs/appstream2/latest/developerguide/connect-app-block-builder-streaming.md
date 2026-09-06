

# Streaming URL (Amazon WorkSpaces Applications Client or Browser Connection)
<a name="connect-app-block-builder-streaming"></a>

You can create a streaming URL to connect to an app block builder through a browser or the WorkSpaces Applications client. Unlike a streaming URL that you create to enable user access to a fleet instance, which is valid for a maximum of seven days, by default, a streaming URL that you create to access an image builder expires after one hour. To set a different expiration time, you must generate the streaming URL by using the [CreateAppBlockBuilderStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlockBuilderStreamingURL.html) API action.

**Note**  
Streaming a URL to connect to an app block builder is not supported on the macOS client. 

You can create a streaming URL in any of the following ways:
+ WorkSpaces Applications console
+ The [CreateAppBlockBuilderStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlockBuilderStreamingURL.html) API action 
+ The [create-app-block-builder-streaming-url](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-app-block-builder-streaming-url.html) AWS CLI command

To create a streaming URL and connect to the app block builder by using the WorkSpaces Applications console, complete the steps in the following procedure.

**To create a streaming URL and connect to the app block builder by using the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the navigation pane, choose **Application Manager**, **App block builders**.

1. In the list of app block builders, choose the app block builder to which you want to connect. Verify that the status of the app block builder is **Running**.

1. Choose **Actions**, **Create streaming URL**.

1. Do one of the following:
   + To save the streaming URL to connect to the app block builder later, choose **Copy Link** to copy the URL, then save it to an accessible location.
   + To connect to the app block builder through the WorkSpaces Applications client, choose **Launch in Client**. When you choose this option, the WorkSpaces Applications client sign-in page is prepopulated with the streaming URL.
   + To connect to the app block builder through a browser, choose **Launch in Browser**. When you choose this option, a browser opens with the address bar prepopulated with the streaming URL.

1. After you create the streaming URL and connect to the app block builder, start streaming the app block builder.