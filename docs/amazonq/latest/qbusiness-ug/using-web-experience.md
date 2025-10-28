# Using an Amazon Q Business web experience

You can use the Amazon Q Business web experience generative AI assistant to ask
questions and to accomplish your tasks. When you ask a question, the Amazon Q Business
web experience analyzes the latest approved data collected from data sources within your
organization to generate a comprehensive response.

You can ask complex questions in plain language and get a detailed response. You can also
use an Amazon Q Business web experience to perform tasks for you, such as draft an
email message or create a Jira ticket.

###### Note

As of Oct 31, 2024, once you have created a new Amazon Q Business
application environment, the default web experience will allow users to interact directly with the
LLM to get answers from its general knowledge or uploaded file content, even if the Admin has not yet connected any enterprise data sources.

For existing application environments, the _Allow direct access to LLM_
setting will remain as previously configured. For new application environments, the
_Allow direct access to LLM_ setting will be enabled by default,
though Admins can still disable this if desired.

The Amazon Q Business web experience provides you with the following
capabilities:

###### Web experience features

- [Example
  prompts](#example-prompts "#example-prompts")
- [Engage with contextual responses](#contextual-response "#contextual-response")
- [Analysis
  and reasoning](#analyze-content "#analyze-content")
- [Perform actions using plugins](#actions "#actions")
- [Review source citations](#review-source-citation "#review-source-citation")
- [Upload files and chat](#upload-documents "#upload-documents")
- [Advanced search](#advanced-search "#advanced-search")
- [Copy responses](#copy-responses "#copy-responses")
- [Provide feedback](#provide-feedback "#provide-feedback")
- [Conversation management](#conversation-mgmt "#conversation-mgmt")
- [Response sources](#chat-source-scope "#chat-source-scope")
- [Login, Logout and session duration for Web
  Experience](#Web-logout "#Web-logout")

###### Important

An Amazon Q Business web experience establishes a secure WebSockets connection to [supported Amazon Q Business endpoints](quotas-regions.md#regions "quotas-regions.md#regions") over port 8443. For example,
`wss://qbusiness.us-west-2.api.aws:8443/chat`.

To ensure that your browser can successfully establish a WebSockets connection, ensure
that port 8443 is enabled and not blocked by network rules that you have configured at
the router, VPN, VPC, or firewall level.

## Example

prompts

The welcome page optionally provides example prompts to help you understand the types
of questions and tasks that you can ask the Amazon Q Business web experience.
This
feature is provided depending on how the web experience is
configured. You can use these example prompts to formulate your own
questions and tasks.

## Engage with contextual responses

The Amazon Q Business web experience analyzes your questions and returns
responses from the selected data sources within your organization. You can continue with
a conversation in the context of the active session or start a new conversation to
refresh any previous contexts.

## Analysis

and reasoning

You can ask Amazon Q Business to summarize a response, generate text from a
response, do comparative analysis, and perform math and reasoning tasks.

## Perform actions using plugins

If your system is configured with **Use a plugin** mode enabled, you
can use Amazon Q Business to perform actions on your behalf using [plugins](plugins.md "plugins.md").
For example, you can ask Amazon Q to schedule a meeting, create a ticket in
Jira, or draft an email message. You only see an option to
**Use a plugin** in your web experience if your admin has enabled
it.

You perform plugin actions by choosing **Use a plugin** mode in your
web experience chat. Or, if your admin has enabled the chat orchestration feature,
Amazon Q Business automatically orchestrates end user queries across any
plugins and data sources you’ve configured and selects relevant plugin actions. For
information about how to use plugins, see [Using built-in plugins](using-plugins.md "using-plugins.md")
and [Using custom
plugins](using-custom-plugin.md "using-custom-plugin.md").

###### Note

You can't use plugins and file uploads at the same time.

## Review source citations

The Amazon Q Business web experience provides in-text source citations in a
numbered list. To view the source for a response, choose the number at the end of the
sentence. The dialog box shows the title, URL, and a snippet from the source that was
used to generate the response. Choose the URL to view the source document.

To view the full list of sources, choose **Sources** at the end of
the response. You can use the source list to fact-check the response, or for deeper
analysis.

## Upload files and chat

You can upload document in the Amazon Q Business web experience and ask
questions, summarize, or analyze data based on their content. Amazon Q also
supports a recent documents list so you can find and reuse recently attached files in
new conversations without re-uploading. You can upload new files from your computer,
choose from recent files, or drag and drop files directly into a conversation.

A maximum of five files can be uploaded in a single conversation. Documents uploaded
through the chat interface are stored in your conversation history and deleted when the
conversation is deleted, or after 30 days of inactivity. After files are attached to a
conversation, you must delete the conversation to delete the files. You can't delete
them individually.

###### Note

You can't use plugins and file uploads at the same time.

###### Note

If you connect enterprise data to your application, file upload functionality is
only available in the **General Knowledge** section of the web
experience and isn't available in the **Company Knowledge**
section.

## Advanced search

Advanced search is an Amazon Q Business feature that you can toggle on from
within your web experience interface. When enabled, it enhances the standard
retrieval-augmented generation of Amazon Q Business by employing intelligent
agents that analyze queries more thoroughly, maintain conversation context, and
intelligently performs multiple data retrieval operations to gather comprehensive
information. Advanced search is particularly useful for complex, multi-faceted queries
where you need more comprehensive and contextually aware responses, and want to track
real time progress on query processing.

For more information, see [Agentic Retrieval Augmented Generation (RAG)](agentic-rag.md "agentic-rag.md").

## Copy responses

You can copy and save the responses for later review and analysis. To copy a response,
choose the copy icon at the end of the response.

## Provide feedback

You can provide feedback at any time using the feedback button in the left hand
sidebar. You can also provide direct feedback about the response you received from the
Amazon Q web experience by using the thumbs-up or thumbs-down button.
Your feedback is used to help address technical issues in the web experience.

If you select the thumbs-down button, you can choose from the following feedback
options:

- **Response is not helpful (incorrect or not relevant to my
  query)**
- **Response is not based on company documents**
- **Response is not complete**
- **Response is not concise**
- **The sources are inaccurate or missing**
- **Other**

## Conversation management

Amazon Q Business stores conversations for up to 30 days, and you can access
them in the left navigation pane. You can perform the following tasks to manage your
conversations:

- **View conversation history** – Choose a
  conversation to view the conversation history for that session.
- **Start new conversation** – Choose
  **+ New conversation** to start a new conversation.
- **Delete conversation** – Choose a
  conversation that you want to delete, choose **Delete**, and
  then choose **Delete** again.

## Response sources

If you have the appropriate permissions granted by your administrator, you can
configure Amazon Q Business web experience responses from up to three sources;
**General knowledge**, **Company knowledge**, or
from files that you upload.

- **General knowledge** – If you choose this
  mode, Amazon Q Business only responds using Amazon Q's
  underlying knowledge.
- **Company knowledge** – If you choose
  this, Amazon Q Business only responds from your enterprise data.
- **Uploaded files** – If you upload files,
  Amazon Q Business responds using the data in the files. If the
  uploaded files don't contain an answer for the query, Amazon Q
  generates a response from its underlying knowledge.

For more information, see [Using global controls in Amazon Q Business](guardrails-global-controls.md "guardrails-global-controls.md").

## Login, Logout and session duration for Web

Experience

Users log in through their identity provider, which integrates with the Amazon Q Business Web
App. After authentication, a session token is generated and the user is automatically
logged into the Web App through single sign-on. Amazon Q Business Web App sessions expire one
hour after login. To maintain continuous access, users must refresh their session token
before expiration, not after, by refreshing the page.

For security, users should log out of both the Web App and their identity provider
when finished. Leaving a session active allows anyone using the same computer within the
hour to bypass login due to the still-valid session token.

**IDC (Identity Center) Applications**

When a user logs out:

- Browser cookies are deleted
- The session is revoked through IDC
- The user is redirected to the login page

**IDP (Identity Provider) Applications**

When a user logs out:

- Browser cookies are deleted
- The user is redirected to the login page

JWTs (JSON Web Tokens) are used for authentication and authorization and expire after
an hour.

###### Note

If the webpage’s cookies are restored after logout, then the IDP session cookie
information may still validate the web app, preventing a successful logout.
