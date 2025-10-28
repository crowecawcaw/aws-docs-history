# Generate a variation of an image

The following procedure shows you how to generate a variation of a
reference image that you supply. You can set various configurations such as the number
of images to generate and how strongly the prompt affects the generation of the image.
For more information, see [Configuration options](explore-image-playground.md#bedrock-image-configuration "explore-image-playground.md#bedrock-image-configuration").

###### To generate a variation of an image

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. At the top of the page, choose the **Discover**.
4. In the **GENERATIVE AI** section, choose **Image and video playground**.
5. If the **Configurations** pane isn't open, choose the configuration button.
6. For **Model** select a model to use.
7. For **Action** choose **Generate variations**.
8. (Optional) For **Negative prompt** enter text that describes content or concepts that you
   do not want the model to include in the image.
9. In **Reference image** choose **Upload
   image** and upload the image that you want the model to use with
   the action.
10. In **Response image** do the following:
    1. For **Number of images** select the number of images that you want the
       model to generate. Not all models support changing this value.
    2. For **Orientation**, choose the orientation (landscape or portrait)
       for the images that the model generates.
    3. For **Size**, select the size, in pixels, of the images that the model
       generates.

11. (Optional) In **Advanced configurations**, change how the
    model generates images by making advanced configuration changes. For more
    information, see [Advanced configuration options](explore-image-playground.md#bedrock-image-advanced-configurations "explore-image-playground.md#bedrock-image-advanced-configurations").
12. In the **Enter prompt** text box, enter the prompt that describes the image
    that you want the model to generate.
13. Press Enter on your keyboard to start the action. Amazon Bedrock in SageMaker Unified Studio shows
    the image that the model generates in the playground.
