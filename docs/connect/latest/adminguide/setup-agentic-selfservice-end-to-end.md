# AI Message Streaming

###### Note

Orchestration AI Agents require chat streaming to be enabled for chat contacts. Without chat streaming enabled, some messages will fail to render. See [Enable message streaming for AI-powered
chat](message-streaming-ai-chat.md "message-streaming-ai-chat.md").

## What is AI Messaging Streaming?

AI Message Streaming is an Amazon Connect feature that enables **progressive display of AI agent responses** during chat interactions. Instead of waiting for the AI to generate a complete response before showing anything to the customer, streaming displays text as it's being generated, creating a more natural, conversational experience.

### How It Works

With standard chat responses, customers wait while the AI generates its entire response, then the complete message appears all at once. With AI Message Streaming, customers see a **growing text bubble** where words appear progressively as the AI generates them, similar to watching someone type in real-time.

###### Note

**Official Documentation**: For the complete technical reference, see [Enable message streaming for AI-powered
chat](message-streaming-ai-chat.md "message-streaming-ai-chat.md").

### Benefits of Progressive Text Display

AI Message Streaming provides several key benefits for customer experience:

- **Reduced perceived wait time** - Customers see immediate activity rather than staring at a loading spinner
- **More natural conversation flow** - Progressive text mimics human typing, creating a more engaging interaction
- **Better engagement** - Customers can start reading the response while it's still being generated
- **Fulfillment messages** - AI agents can provide interim messages like "One moment while I review your account" during processing

### Standard Chat vs Streaming Chat

The following table compares the customer experience between standard chat and streaming chat:

| Aspect                   | Standard Chat                                 | Streaming Chat                              |
| ------------------------ | --------------------------------------------- | ------------------------------------------- |
| **Response Display**     | Complete message appears all at once          | Text appears progressively (growing bubble) |
| **Customer Experience**  | Wait for full response with loading indicator | See words appear in real-time               |
| **Perceived Wait Time**  | Longer (waiting for complete response)        | Shorter (immediate visual feedback)         |
| **Conversation Feel**    | Transactional                                 | Natural, like chatting with a person        |
| **Fulfillment Messages** | Not available                                 | AI can send interim status updates          |
| **Lex Timeout Handling** | Subject to Lex timeout limits                 | Eliminates Lex timeout limitations          |

## Enablement Status

AI Message Streaming availability depends on when your Amazon Connect instance was created and how it's configured.

### Automatic Enablement for New Instances

Amazon Connect instances created **after December 2025** have AI Message Streaming enabled by default. The `MESSAGE_STREAMING` instance attribute is automatically set to `true` for these instances, so no additional configuration is required.

###### Important

If you're using an AWS account with an Amazon Connect instance created **before December 2025**, you may need to manually enable AI Message Streaming. Follow the instructions in the [Enable message streaming for AI-powered chat](message-streaming-ai-chat.md "message-streaming-ai-chat.md") documentation to check your instance's `MESSAGE_STREAMING` attribute and enable it if needed.

### Amazon Lex Bot Permissions

AI Message Streaming requires the `lex:RecognizeMessageAsync` permission to function correctly. This permission allows Amazon Connect to invoke the asynchronous message recognition API that enables streaming responses.

**For new Lex bot associations**: When you associate a new Amazon Lex bot with your Amazon Connect instance, the required `lex:RecognizeMessageAsync` permission is **automatically included** in the bot's resource-based policy. No additional configuration is needed.

###### Important

If you have an Amazon Lex bot that was associated with your Amazon Connect instance **before** AI Message Streaming was enabled, you may need to update the bot's resource-based policy to include the `lex:RecognizeMessageAsync` permission.

To update your existing Lex bot policy:

1. Navigate to the Amazon Lex console
2. Select your bot and go to **Resource-based policy**
3. Add the `lex:RecognizeMessageAsync` action to the policy statement that grants Amazon Connect access
4. Save the updated policy
   For detailed instructions, see the [Lex bot permissions](message-streaming-ai-chat.md#lex-bot-permissions "message-streaming-ai-chat.md#lex-bot-permissions") section in the AWS documentation.

## Create Communications Widget

The Amazon Connect Communications Widget is an embeddable chat interface that you can add to any website. In this section, you'll create and configure a widget to test AI Message Streaming. You can skip this section if you plan to use your own customer chat widget.

### Step 1: Navigate to Communications Widget

1. In the Amazon Connect console, navigate to your instance
2. Click **Channels** in the left navigation menu
3. Click **Communications widget**
4. You'll see the Communications Widget management page

###### Note

**What is the Communications Widget?** The Communications Widget is Amazon Connect's out-of-the-box chat solution. It provides a fully functional chat interface that you can embed in websites using a simple JavaScript snippet. The widget handles all the complexity of establishing connections, managing sessions, and displaying messages.

### Step 2: Create a New Widget

1. Click **Add widget** to create a new Communications Widget
2. Enter the following details:
   - **Name**: `AI-Streaming-Demo-Widget`
   - **Description**: `Widget for testing AI Message Streaming`

3. Under **Communication options** ensure **Add chat** is selected
4. Select **Self Service Test Flow** as your Chat contact flow
5. Click **Save and continue** to proceed to the configuration page

###### Contact Flow Selection

Make sure you select a contact flow that:

- Has the Basic Settings configured (creates AI session, logging, etc)
- Routes to your Lex bot with AI Agent integration
- Has proper error handling for disconnects
  If you haven't created a contact flow yet, complete the [Creating the Flow](https://catalog.workshops.aws/amazon-q-in-connect/en-US/03-Self-Service-Track/01-ai-agent-configuration/04-creating-flow/ "https://catalog.workshops.aws/amazon-q-in-connect/en-US/03-Self-Service-Track/01-ai-agent-configuration/04-creating-flow/") section first.

### Step 3: Customize Widget Appearance

Customize the look and feel of your chat widget to match your brand and select **Save and continue**.

### Step 4: Configure Allowed Domains

The Communications Widget only loads on websites that are explicitly allowed. This security feature prevents unauthorized use of your widget.

1. Scroll down to **Allowed domains**
2. Click **Add domain** and add the following domain for localhost testing:
   - `http://localhost`

3. Select **No** under security
4. If you plan to deploy to a production website later, add those domains as well and ensure you configure security (e.g., `https://www.example.com`)

### Step 5: Save and Get Widget Code

1. Click **Save and continue** to save your widget configuration
2. After creation, you'll see the **Widget details** page with your embed code
3. **Important**: Copy and save the following values from the embed code snippet:
   - **Client URI** - The URL to the widget JavaScript file
   - **Widget ID** - A unique identifier for your widget
   - **Snippet ID** - A Base64-encoded configuration string

### Step 6: Set Up Local Testing Environment

To test the widget locally, you'll create a simple HTML file that loads the Communications Widget.

1. Create a new folder on your computer for testing (e.g., `ai-streaming-test`)
2. Download the background image for the demo page and save it as `background.jpg` in your test folder
3. Create a new file called `index.html` in your test folder with the following content:

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <style>
        body {
            background-image: url("background.jpg");
            background-repeat: no-repeat;
            background-size: cover;
        }
    </style>
    <title>AI Message Streaming Demo</title>
</head>
<body>
    <div id="root"></div>
    <script type="text/javascript">
      (function(w, d, x, id){
        s=d.createElement('script');
        s.src='REPLACE_WITH_CLIENT_URI';
        s.async=1;
        s.id=id;
        d.getElementsByTagName('head')[0].appendChild(s);
        w[x] = w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
      })(window, document, 'amazon_connect', 'REPLACE_WITH_WIDGET_ID');
      amazon_connect('styles', {
        iconType: 'CHAT',
        openChat: { color: '#ffffff', backgroundColor: '#ff9200' },
        closeChat: { color: '#ffffff', backgroundColor: '#ff9200'}
      });
      amazon_connect('snippetId', 'REPLACE_WITH_SNIPPET_ID');
      amazon_connect('supportedMessagingContentTypes', [
        'text/plain',
        'text/markdown',
        'application/vnd.amazonaws.connect.message.interactive',
        'application/vnd.amazonaws.connect.message.interactive.response'
      ]);
      amazon_connect('customStyles', {
        global: { frameWidth: '500px', frameHeight: '900px'}
      });
    </script>
</body>
</html>
```

### Step 7: Replace Placeholder Values

Replace the placeholder values in the HTML file with your actual widget values:

| Placeholder               | Replace With                | Example                                                                       |
| ------------------------- | --------------------------- | ----------------------------------------------------------------------------- |
| `REPLACE_WITH_CLIENT_URI` | Your Client URI from Step 5 | `https://d2s9x5slqf05.cloudfront.net/amazon-connect-chat-interface-client.js` |
| `REPLACE_WITH_WIDGET_ID`  | Your Widget ID from Step 5  | `amazon_connect_widget_abc123`                                                |
| `REPLACE_WITH_SNIPPET_ID` | Your Snippet ID from Step 5 | `QVFJREFIaWJYbG...` (long Base64 string)                                      |

### Step 8: Start a Local Web Server

To test the widget, you need to serve the HTML file from a local web server. Here are several options:

###### Option A: Python (if installed)

```
python -m http.server 8001
```

###### Option B: Node.js (if installed)

```
npx http-server -p 8001
```

###### Option C: VS Code Live Server Extension

- Install the "Live Server" extension in VS Code
- Right-click on `index.html` and select "Open with Live Server"

After starting the server, open your browser and navigate to: `http://localhost:8001`

You should see the demo page with an orange chat button in the bottom-right corner.

## Test the Streaming Experience

Now that your widget is loaded, it's time to test AI Message Streaming and observe the progressive text display in action.

### What to Look For: Streaming vs Non-Streaming

Understanding the difference between streaming and non-streaming responses helps you verify that AI Message Streaming is working:

| Behavior            | Non-Streaming (Standard)             | Streaming (AI Message Streaming)                |
| ------------------- | ------------------------------------ | ----------------------------------------------- |
| **Initial display** | Loading indicator or typing dots     | Text starts appearing immediately               |
| **Text appearance** | Complete message appears all at once | Words appear progressively (growing bubble)     |
| **Response timing** | Wait until AI finishes generating    | See response as it's being generated            |
| **Visual effect**   | "Pop" of complete text               | Smooth, flowing text like watching someone type |
