# Plan a video with

the storyboard

To create more a more complex video, you can use the storyboard to plan the video that
you want to create. In the storyboard you connect a sequence of shots, which the model
combines to generate the video. Each shot is a prompt and an optional start frame image.
Each shot the model generates is always 6 seconds in length. You can't set a specific
duration for the video, but you can affect the duration by adding or removing shots in
the story board. The maximum length of video that you can generate is 120 seconds.

###### Note

You can only use the playground with Amazon Nova Reel 1.1.

###### To generate a video with the storyboard

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. At the top of the page, choose the **Discover**.
4. In the **GENERATIVE AI** section, choose **Image and video playground**.
5. If the **Configurations** pane isn't open, choose the configuration button.
6. For **Model** select a model to use.
7. (Optional) In the **Configurations** section, set parameters
   to influence the output of the model. Note that additional configurations can be
   set in **Advanced configurations**. The parameters that are
   available to depend on the model you use. For more information, see [Configure video generation](bedrock-explore-video-playground-configuration.md "bedrock-explore-video-playground-configuration.md").

In the storyboard, you can't set the duration for the video. 8. In the center pane, choose **Storyboard**. 9. Choose **Add shot** and do the following:

    1. Choose **Describe what happens in this shot...** and enter the text
     for the prompt. You can update the prompt later, if neccessary.
    2. (Optional) Choose **Add start frame** to upload a
     starting image for the video.
    3. (Optional) Choose the trash icon to remove shots than you no longer
     need.

10. Repeat the previous step until you have added all the shots for your
    video.
11. Choose the run button to start generating the video. Don't leave the page while
    the model generates the video.
12. When the model finishes generating the video, choose the play button to view
    the video.
13. (Optional) Make further edits and add shots as you need them.
14. (Optional) Download the video by right-clicking on the video and selecting
    **Save video as...**.
