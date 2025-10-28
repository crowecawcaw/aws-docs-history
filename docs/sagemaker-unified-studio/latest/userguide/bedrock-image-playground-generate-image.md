# Generate an image

The following procedure shows you how to use a model to generate an image. You can set
various configurations such as the number of images to generate and how strongly the prompt
affects the generation of the image. For more information, see [Configuration options](explore-image-playground.md#bedrock-image-configuration "explore-image-playground.md#bedrock-image-configuration").

###### To generate an image in the image playground

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. At the top of the page, choose the **Discover**.
4. In the **GENERATIVE AI** section, choose **Image and video playground**.
5. If the **Configurations** pane isn't open, choose the configuration button.
6. For **Model** select a model to use.
7. For **Action** choose the action **Generate image**.
8. In **Response image** do the following:
   1. For **Number of images** select the number of images that you want the
      model to generate. Not all models support changing this value.
   2. For **Orientation**, choose the orientation (landscape or portrait)
      for the images that the model generates.
   3. For **Size**, select the size, in pixels, of the images that the model
      generates.

9. (Optional) In **Advanced configurations**, change how the
   model generates images by making advanced configuration changes. For more
   information, see [Advanced configuration options](explore-image-playground.md#bedrock-image-advanced-configurations "explore-image-playground.md#bedrock-image-advanced-configurations").
10. In the **Enter prompt** text box, enter `Create a photo of a
local classic rock band playing on an outdoor stage.`. Alternatively, enter a prompt
    of your choosing.
11. Press Enter on your keyboard to start the action. Amazon Bedrock in SageMaker Unified Studio shows
    the image that the model generates in the playground.
12. (Optional) See how different configuration parameters affect image generation by
    repeating steps 9 - 11 with different values.
