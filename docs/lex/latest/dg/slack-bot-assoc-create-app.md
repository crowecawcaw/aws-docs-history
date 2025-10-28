End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 3: Create a Slack

Application

In this section, you do the following:

1. Create a Slack application on the Slack API Console
2. Configure the application to add interactive messaging to
   your bot:
   At the end of this section, you get application credentials
   (Client Id, Client Secret, and Verification Token). In the next
   section, you use this information to configure bot channel
   association in the Amazon Lex console.

3. Sign in to the Slack API Console at [http://api.slack.com](http://api.slack.com "http://api.slack.com") .
4. Create an application.

After you have successfully created the application, Slack
displays the **Basic Information** page for
the application. 3. Configure the application features as follows:

    1. In the left menu, choose **Interactivity
     & Shortcuts**.




    	* Choose the toggle to turn interactive
    	 components on.
    	* In the **Request URL**
    	 box, specify any valid URL. For example, you
    	 can use
    	 `https://slack.com`.


    	###### Note

    	For now, enter any valid URL to get
    	 the verification token that you need in
    	 the next step. You will update this URL
    	 after you add the bot channel
    	 association in the Amazon Lex console.
    	* Choose **Save
    	 Changes**.

4. In the left menu, in **Settings**, choose
   **Basic Information**. Record the
   following application credentials:
   - Client ID
   - Client Secret
   - Verification Token

###### Next Step

[Step 4: Integrate the
Slack Application with the Amazon Lex Bot](slack-bot-assoc-create-assoc.md "slack-bot-assoc-create-assoc.md")
