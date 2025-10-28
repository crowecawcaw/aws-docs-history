# Storyboarding videos with Amazon Nova Reel

Amazon Nova Reel includes the ability to create videos in six second increments that are up to two minutes long. From the Amazon Bedrock playground, you can provide a single prompt that will generate a video of a specified length. However, if you want more control over subjects and direction of the video, you can use the storyboard.

The storyboard allows you provide multiple input images and prompts to better guide the generated video towards your desired outcome. For each six second interval, you have the option of providing an input image, a prompt, or both. These inputs are used to generate the video until a different input image or prompt are encountered. This way, if you want your video to cut to a different camera angle or focus on a different subject, you can prompt the model when it's time to do so.

To create a video with the storyboard, complete the following steps:

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. From the left navigation pane, choose **Image / Video** under
   **Playgrounds**.
3. Choose **Select model** and select **Amazon** and **Amazon Nova Reel v1.1** as the provider and model. Choose **Apply**.
4. In the left panel, move the slider so that the value of **Duration (seconds)** is greater than 6.
5. Choose the storyboard icon ![Striped icon representing a list or menu with multiple items.](images/storyboardIcon.png) to enter the Storyboard.
6. In the Storyboard, add or remove shots to reach the desired length of generated video.
7. For each shot, you can add an image, text prompt, or both. You must add at least a text prompt to the first shot of the storyboard.
8. After you have specified all of the shot information, choose **Run**. Video generation will run asynchronously until completion. When finished, you will be notified and the video will be saved in an Amazon S3 bucket.
