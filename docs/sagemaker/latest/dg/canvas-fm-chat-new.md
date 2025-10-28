# Start a new conversation to generate, extract, or

summarize content

To get started with generative AI foundation models in Canvas, you can initiate a
new chat session with one of the models. For JumpStart models, you are charged while
the model is active, so you must start up models when you want to use them and shut them
down when you are done interacting. If you do not shut down a JumpStart model,
Canvas shuts it down after 2 hours of inactivity. For Amazon Bedrock models (such as
Amazon Titan), you are charged by prompt; the models are already active and don’t need to
be started up or shut down. You are charged directly for use of these models by
Amazon Bedrock.

To open a chat with a model, do the following:

1. Open the SageMaker Canvas application.
2. In the left navigation pane, choose **Ready-to-use
   models**.
3. Choose **Generate, extract and summarize content**.
4. On the welcome page, you’ll receive a recommendation to start up the default
   model. You can start the recommended model, or you can choose **Select
   another model** from the dropdown to choose a different one.
5. If you selected a JumpStart foundation model, you have to start it up
   before it is available for use. Choose **Start up the model**,
   and then the model is deployed to a SageMaker AI instance. It might take several minutes
   for this to complete. When the model is ready, you can enter prompts and ask the
   model questions.

If you selected a foundation model from Amazon Bedrock, you can start using it
instantly by entering a prompt and asking questions.
Depending on the model, you can perform various tasks. For example, you can enter a
passage of text and ask the model to summarize it. Or, you can ask the model to come up
with a short summary of the market trends in your domain.

The model’s responses in a chat are based on the context of your previous prompts. If
you want to ask a new question in the chat that is unrelated to the previous
conversation topic, we recommend that you start a new chat with the model.
