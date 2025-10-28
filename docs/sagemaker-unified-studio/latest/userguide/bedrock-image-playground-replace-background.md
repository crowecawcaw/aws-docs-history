# Replace the background for an image

The following procedure shows you how to use a model to replace the background for an image.
For example, you could change the background for an image from a view of a forest
to a view of city buildings. You can set various configurations such as the number of images to
generate and how strongly the prompt affects the generation of the image. For more
information, see [Configuration options](explore-image-playground.md#bedrock-image-configuration "explore-image-playground.md#bedrock-image-configuration").

###### Note

The background replacement action is only available with Titan Image Generator G1 V1 and Titan Image Generator G1 V2 models.

###### To replace the background for an image

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. At the top of the page, choose the **Discover**.
4. In the **GENERATIVE AI** section, choose **Image and video playground**.
5. If the **Configurations** pane isn't open, choose the configuration button.
6. For **Model** select a model to use.
7. For **Action** choose **Replace background**.
8. (Optional) For **Negative prompt** enter text that describes content or concepts that you
   don't want the model to include in the image.
9. In **Reference image** choose **Upload
   image** and upload the image that you want the model to use with
   the action.
10. (Optional) For **Negative prompt** enter text that describes content or concepts that you
    do not want the model to include in the image.
11. (Optional) In **Advanced configurations**, change how the
    model generates images by making advanced configuration changes. For more
    information, see [Advanced configuration options](explore-image-playground.md#bedrock-image-advanced-configurations "explore-image-playground.md#bedrock-image-advanced-configurations").
12. In the center pane, use the masking tool to draw a bounding box around the
    area of the image that you want the action to preserve. The model updates the
    area outside of the bounding box. You can do the following:
    1. Resize the bounding box by selecting a corner of the bounding box with
       your mouse button. Then, drag the mouse to resize the bounding box.
       Release the mouse button to complete resizing the bounding box.
    2. Move the bounding box by selecting the interior of the bounding box
       with your mouse button. Move the bounding box to the new location and
       release the mouse button.

13. In the **Enter prompt** text box, enter a prompt that describes the background
    that you want the image to have.
14. Press Enter on your keyboard to start the action. Amazon Bedrock in SageMaker Unified Studio shows
    the image that the model generates in the playground.
