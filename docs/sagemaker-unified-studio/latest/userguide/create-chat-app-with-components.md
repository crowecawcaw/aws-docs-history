# Create a chat agent app with Amazon Bedrock

In this section, you learn how create a simple Amazon Bedrock in SageMaker Unified Studio chat agent app that
creates playlists for a radio station.

The app can
generate playlists and get the dates and locations of upcoming shows. Later, you add the following Amazon Bedrock
features.

- A guardrail to prevent songs with inappropriate song titles.
- A knowledge base that lets the app create playlists using your unique song information.
- A function that gets today's top 10 songs.

###### Topics

- [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app")
- [Step 2: Add a guardrail to your chat agent app](#chat-app-add-guardrail "#chat-app-add-guardrail")
- [Step 3: Add a knowledge base to your chat agent app](#chat-app-add-data-source "#chat-app-add-data-source")
- [Step 4: Add a function call to your chat agent app](#chat-app-add-function-call "#chat-app-add-function-call")

## Step 1: Create the initial chat agent app

In this step you create a chat agent app that generates
playlists for a radio station.

To create the app, you first need to create an Amazon SageMaker Unified Studio
[project](projects.md "projects.md"). A project can contain multiple apps and is also
where you can add the Amazon Bedrock components that you want your apps to use. Later you will
add guardail, knowledge base, and function components to your app. You can share a project with
other users and groups of users. For more information, see [Share an Amazon Bedrock chat agent app](app-share.md "app-share.md").

To help guide users of the app, you can set user interface (UI) text, such as hint
text for the beginning of a chat.

In the app, you can experiment with the randomness and diversity of the response
that the model returns by changing the [inference parameters](explore-prompts.md#inference-parameters "explore-prompts.md#inference-parameters").

While you develop your app, you work on the current draft. You can save the current draft to
the app history. Later you might want to restart work from a previous draft. For more
information, see [Use app history to view and restore versions of an Amazon Bedrock app](app-history.md "app-history.md").

###### Warning

Generative AI may give inaccurate responses. Avoid sharing sensitive information.
Chats may be visible to others in your organization.

###### To create an Amazon Bedrock chat agent app

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. On the Amazon SageMaker Unified Studio home page, in the **Amazon Bedrock in SageMaker Unified Studio**
   tile, choose **Build chat agent app** to create a new
   chat agent app. The **Select or create a new project to
   continue** dialog box opens.
4. In the **Select or create a new project to continue** dialog box, do one of the following:
   - If you want to use a new project, follow the instructions at
     [Create a new project](create-new-project.md "create-new-project.md"). For the **Project profile** in step 1, choose
     **Generative AI application development**.
   - If you want to use an existing project, select the project that you
     want to use and then choose **Continue**.

5. In **Untitled App - nnnn**, enter `Radio
show` as the name for your app.
6. In the **Configs** pane, do the following:
   1. For **Model**, select a model that supports
      Guardrails, Data, and Function components. The description of the
      model tells you the components that a model supports. For full
      information about the model, choose **View full model
      details** in the information panel. For more information,
      see [Find serverless models with the Amazon Bedrock model
      catalog](model-catalog.md "model-catalog.md").
      If you don't have
      access to an appropriate model, contact your administrator.
      Different models might not support all features.
   2. For **Enter a system instruction** in **Instructions for chat agent
      & examples**, enter `You are a
chat agent app that creates 2 hour long playlists for a radio
station that plays rock and pop music.`.
   3. In the **UI** section, update the user interface for the app by doing the following:
      1. In **Hint text for empty chat** enter `Hi!
I'm your radio show playlist creator.`.
      2. In **Hint text for user input** enter
         `Enter a prompt that describes the playlist that you want.`.
      3. In **Quick start prompts** choose
         **Edit**.
      4. Choose **Reset** to clear the list of quick start
         prompts
      5. For **Quick-start prompt 1**, enter `Create a
playlist of pop music songs.`.
      6. (Optional). Enter quick start prompts of your choice in the remaining quick start prompt text boxes.
      7. Choose **Back to configs**.

7. Choose **Save** to save the current working draft of your app.
8. In the **Quick start prompts** section of the
   **Preview** pane, run the quick start prompt that you just
   created by choosing the prompt.

The app shows the prompt and the response from the model in the
**Preview** pane. 9. In the prompt text box (the text should read **Enter a prompt that describes the playlist that you
want**), enter
`Create a playlist of songs where each song on the list is related to
 the next song, by musician, bands, or other connections. Be sure to explain
 the connection from one song to the next.` . 10. Choose the run button (or press Enter on your keyboard) to send the prompt to the model. 11. (Optional) In the **Inference parameters** section change
the inference parameters. For example, include less familiar songs
in the playlist by increasing the **Temperature**
inference parameter.

The inference parameters you can change are
_Temperature_, _Top P_,
and _Top K_. Not all models support each of these
inference parameters. For more information, see [Inference parameters](explore-prompts.md#inference-parameters "explore-prompts.md#inference-parameters"). 12. (Optional) In **Stop sequences**, add one or more stop
sequences for the model. A stop sequence ensures that the model stops
generating text immediately after it generates text that matches the stop
sequence. Stop sequences are useful for getting precise answers without unnecessary additional text.
Not all models support stop sequences. 13. (Optional) In **Reasoning** select **Model
reasoning** to enable model reasoning. Model reasoning is when
a model uses chain of thought reasoning to take a large, complex task and
break it down into smaller, simpler steps. You can only enable or disable
model reasoning at the start of a new chat. You can specify the number of
tokens to use, which includes both output and reasoning tokens. Not all
models support model reasoning. For more information, see [Enhance model responses with model
reasoning](../../../bedrock/latest/userguide/inference-reasoning.md "../../../bedrock/latest/userguide/inference-reasoning.md") in the _Amazon Bedrock user guide_. 14. (Optional) Share your app with others by following the
instructions at [Share an Amazon Bedrock chat agent app](app-share.md "app-share.md"). 15. (Optional) Deploy your app for use in a flow app by following the
instructions at [Deploy an Amazon Bedrock chat agent app](app-deploy.md "app-deploy.md"). 16. (Optional) Export your snapshot from Amazon SageMaker Unified Studio by following the
instructions at [Use your app outside of Amazon SageMaker Unified Studio](app-export.md "app-export.md"). 17. Next step: Add a guardrail to your app by following the instructions at
[Step 2: Add a guardrail to your chat agent app](#chat-app-add-guardrail "#chat-app-add-guardrail").

## Step 2: Add a guardrail to your chat agent app

Guardrails for Amazon Bedrock lets you implement safeguards for your Amazon Bedrock in SageMaker Unified Studio app
based on your use cases and responsible AI policies. You can create multiple guardrails
tailored to different use cases and apply them across multiple foundation models,
providing a consistent user experience and standardizing safety controls across
generative AI apps. You can configure denied topics to disallow undesirable topics and
content filters to block harmful content in the prompts you send to a model and to the
responses you get from a model. You can use guardrails with text-only foundation models.
For more information, see [Safeguard your Amazon Bedrock app with a guardrail](guardrails.md "guardrails.md").

### Add a guardrail

This procedure shows you how to use a guardrail to safeguard the app you created
in [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app"). The guardrail prevents
inappropriate language in song titles and filters out unwanted music genres.

###### To add a guardrail to an Amazon Bedrock app

1. Open the app that you created in
   [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app").
2. In the **Configs** pane, choose
   **Guardrails** and then **Create new
   guardrail**.
3. For **Guardrail name**, enter
   `prevent_unwanted_songs`.
4. For **Guardrail description**, enter `Prevents inappropriate or undesirable songs.`.
5. In **Content filters** make sure **Enable content
   filters** is selected. For more information, see [Content filters](guardrails.md#guardrails-studio-content-filters "guardrails.md#guardrails-studio-content-filters").
6. In **Filter for prompts** make sure the filter for each
   category is set to **High**.
7. Make sure **Apply the same filters for responses** is
   selected.
8. In **Blocked messsaging** do the following.
   1. For **Blocked messaging for
      prompts**, enter `Sorry, your prompt contained inappropriate
text.`.
   2. Clear **Apply the same message for blocked responses**.
   3. For **Blocked
      messaging for responses**, enter `Sorry, but I can't respond with information that
contains inappropriate text.`.

9. Choose **Create** to create the guardrail.
10. In the **Configs** pane, in the **Guardrails** section,
    select the guardrail that you just created (**prevent_unwanted_songs**). It might take a minute for
    the guardrail to appear in the list.
11. Test the guardrail by entering `Create a list of 10 songs where each song has a swear word in the title.`
    In the prompt edit box.
12. Choose the run button to send the prompt to the model. The model should
    respond with the message **Sorry, but I can't respond with
    information that contains inappropriate text.**
13. Use a denied topic filter to prevent requests for music from a specific
    music genere. For information about denied topics, see [Denied topics](guardrails.md#guardrails-topic-policies "guardrails.md#guardrails-topic-policies").

To add the filter, do the following.

    1. In the **Guardrails** section of the **Configs** pane,
     select the guardrail and choose **Preview**.
    2. Choose **Edit** to edit the guardrail.
    3. In **Denied topics**, choose **Add
     topic**.
    4. For **Name**, enter `heavy
     metal`.
    5. For **Definition for topic**, enter `Avoid mentioning songs that are from the
     heavy metal genre of music.`.
    6. In **Sample phrases
     - optional**, enter `Create a playlist of heavy metal
     songs`.
    7. (Optional) Choose **Add phrase** to add other phrases.
    8. Choose **Save**.
    9. Om the **Edit guardrail** page, choose **Update** to update the
     guardrail.
    10. Test the guardrail by entering `Create a list of heavy
     metal songs.` in the prompt edit box.
    11. Choose the run button to send the prompt to the model. The model should
     respond with the message **Sorry, your prompt contained inappropriate
     text**.

14. Next step: Add a data source to your app by following the instructions at
    [Step 3: Add a knowledge base to your chat agent app](#chat-app-add-data-source "#chat-app-add-data-source").

## Step 3: Add a knowledge base to your chat agent app

You can use your own data into your application by adding a knowledge base to your app.
Doing this allows your app to access to information that is only available to you. When
your app passes a query, Amazon Bedrock in SageMaker Unified Studio generates a response that
includes the query results from the knowledge base. For more information, see [Add a Knowledge Base to your Amazon Bedrock app](data-sources.md "data-sources.md").

In this topic, you update the app you created in [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app") to use a CSV
file as a document (local file) data source for a knowledge base. The CSV file includes
information about bands that don't have public metadata such as song length, or
music genre. The user can use the app to create a playlist based on criteria such as
song length or music genre.

###### To add your own data to an Amazon Bedrock app

1. Create a CSV file name _songs.csv_ and fill with the
   following ficticious CSV data.

```
song,artist,genre,length-seconds
"Celestial Odyssey","Starry Renegades","Cosmic Rock",240
"Neon Rapture","Synthwave Siren","Synthwave Pop",300
"Wordsmith Warriors","Lyrical Legions","Lyrical Flow",180
"Nebula Shredders","Galactic Axemen","Cosmic Rock",270
"Electro Euphoria","Neon Nomads","Synthwave Pop",210
"Rhythm Renegades","Percussive Pioneers","Lyrical Flow",240
"Stardust Rift","Cosmic Crusaders","Cosmic Rock",180
"Synthwave Serenade","Electro Enchanters","Synthwave Pop",300
"Lyrical Legends","Rhyme Royale","Lyrical Flow",240
"Supernova Shredders","Amplified Ascension","Cosmic Rock",300
"Celestial Chords","Ethereal Echoes","Cosmic Rock",240
"Neon Nirvana","Synthwave Sirens","Synthwave Pop",270
"Verbal Virtuoso","Lyrical Maestros","Lyrical Flow",210
"Cosmic Collision","Stellar Insurgents","Cosmic Rock",180
"Pop Paradox","Melodic Mavericks","Synthwave Pop",240
"Flow Fusion","Verbal Virtuosos","Lyrical Flow",300
"Shredding Shadows","Crimson Crusaders","Cosmic Rock",270
"Synth Serenade","Electro Enchanters","Synthwave Pop",180
"Wordsmith Warlords","Lyrical Legionnaires","Lyrical Flow",240
"Sonic Supernova","Amplified Ascension","Cosmic Rock",210
"Celestial Symphony","Ethereal Ensemble","Cosmic Rock",300
"Electro Euphoria","Neon Nomads","Synthwave Pop",180
"Lyrical Legends","Rhyme Royale","Lyrical Flow",270
"Crimson Crescendo","Scarlet Serenaders","Cosmic Rock",240
"Euphoric Tides","Melodic Mystics","Synthwave Pop",210
"Rhythm Renegades","Percussive Pioneers","Lyrical Flow",180
"Cosmic Collision","Stellar Insurgents","Cosmic Rock",300
"Stardust Serenade","Celestial Crooners","Synthwave Pop",240
"Wordsmith Warriors","Lyrical Legions","Lyrical Flow",270
"Sonic Supernova III","Amplified Ascension","Cosmic Rock",180
```

2. Open the app that you created in [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app").
3. In **Data** choose **Use Knowledge
   Base** and then **Create Knowledge Base**. The
   **Create Knowledge Base** pane is shown. If you've
   previously created the knowledge base, go to step _10_
   and select the knowledge base.
4. For **Name**, enter a name for the Knowledge Base.
5. For **Description**, enter a description for the
   Knowledge Base.
6. In **Add data sources**, choose **Local
   file**.
7. Choose **Click to upload** and upload the CSV file that
   you created in step 1. Alternatively, add the CSV by dragging and dropping
   the document from your computer.

For more information, see [Use a Local file as a data source](data-source-document.md "data-source-document.md"). 8. For **Embeddings model**, choose a model for converting
your data into vector embeddings. 9. Choose **Create**. It might take Amazon Bedrock in SageMaker Unified Studio a few
minutes to create the knowledge base. 10. For **Select Knowledge Base**, select the Knowledge Base
that you just created. 11. Test the data source by entering `Create a playlist of songs in
 the Lyrical Flow genre` in the prompt text box. 12. Choose the run button to send the prompt to the model. The model should
respond with a playlist of songs from the Lyrical Flow genre that the CSV
file contains. 13. Choose **Save** to save the app.

## Step 4: Add a function call to your chat agent app

Amazon Bedrock in SageMaker Unified Studio functions let a model include information that it has no previous
knowledge of in its response. For example, you can use a function to include dynamic
information in a model's response such as a weather forecast, sports results, or traffic
conditions. To use a function in Amazon Bedrock in SageMaker Unified Studio you add a function component to your app.
For more information, see [Call functions from your Amazon Bedrock chat agent app](functions.md "functions.md").

In Amazon Bedrock in SageMaker Unified Studio, a function calls an API hosted outside of Amazon Bedrock in SageMaker Unified Studio. You either
create the API yourself, or use an existing API. To create an API, you can use [Amazon API Gateway](../../../apigateway.md "../../../apigateway.md").

In this procedure, you add a function
to the app that you created in [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app") so that users can get a list of the
top 10 songs played on the radio station that day.

###### To add a function to an Amazon Bedrock app

1. Create a HTTPS server that implements a `TopSongsToday` function. Make sure
   the function adheres to the following schema.

```
openapi: 3.0.0
info:
  title: Top Songs API
  description: API to retrieve the top 10 songs played today
  version: 1.0.0

paths:
  /top-songs:
    get:
      operationId: TopSongsToday
      summary: Get the top 10 songs played today
      description: >
        This endpoint returns an array of the top 10 songs played today,
        ordered by popularity. The first element in the array (index 0)
        represents the most popular song, and the last element (index 9)
        represents the 10th most popular song.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TopSongs'

components:
  schemas:
    TopSongs:
      type: array
      items:
        $ref: '#/components/schemas/Song'
      description: >
        An array containing the top 10 songs played today. The first element
        (index 0) is the most popular song, and the last element (index 9)
        is the 10th most popular song.
      example:
        - title: 'Song Title 1'
          artist: 'Artist Name 1'
          album: 'Album Name 1'
        - title: 'Song Title 2'
          artist: 'Artist Name 2'
          album: 'Album Name 2'
        # ... up to 10 songs

    Song:
      type: object
      properties:
        title:
          type: string
          description: The title of the song
        artist:
          type: string
          description: The name of the artist or band
        album:
          type: string
          description: The name of the album the song is from
      required:
        - title
        - artist
        - album

```

2. Open the app that you created in [Step 1: Create the initial chat agent app](#chat-app-create-app "#chat-app-create-app").
3. In **Models**, choose a model that supports functions. If
   you don't have access to an appropriate model, contact your
   administrator.
4. In **Functions**, choose **Create new function**.
5. In the **Create function** pane, do the following.
   1. For in **Function
      name**, enter `Top_ten_songs_today`.
   2. For **Function
      description (optional)**, enter `Today's top 10 songs.`.
   3. For **Function
      schema**, enter the OpenAPI schema from step one.
   4. Choose **Validate schema** to validate the schema.
   5. In **Authentication method** choose the
      authentication method for your HTTP server. For more information, see
      [Authentication methods](functions.md#functions-authentication "functions.md#functions-authentication").
   6. In **API servers**, enter the URL for your server in
      **Server URL**. This value is autopopulated if the
      server URL is in the schema.
   7. Choose **Create** to create your function. It might take a few minutes
      to create the function.

6. For **Enter a system instruction**, update the system instruction
   so that it describes the function. Use the following text: `You are an
app that creates 2 hour long playlists for a radio station that plays rock
and pop music. The function Top_ten_songs_today gets the most popular song
played on the radio station.`.
7. Test the function by doing the following.
   1. Enter `What are today's top 10 songs?` in the
      prompt edit box.
   2. Choose the run button to send the prompt to the model. The model should
      respond with the list of today's top 10 songs.
