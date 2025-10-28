# Viewing, deleting, and exporting the Amazon Q Developer conversation

history

When you chat with Amazon Q in the integrated development environment (IDE), Amazon Q saves each of your
chat tabs as a separate conversation. You can view, search for, and delete these conversations. You
can also export them to Markdown or HTML format files.

Amazon Q stores your conversations on your local computer, in your home directory.

Amazon Q saves conversations for each workspace separately, so if you don't see your conversation history,
it might be because you're in the wrong workspace. Amazon Q only displays the conversation history for the
current workspace.

Use the following instructions to view, search for, delete, and export your conversations.

###### To view and search for past conversations

1. In your IDE, sign in to Amazon Q.
2. Open an Amazon Q chat tab.
3. Open the chat history by doing one of the following:
   - On the top-right of the chat panel, choose the **View chat
     history** button.
   - Press `ctrl+F` (Windows and Linux) or `⌘ F` (Mac).

4. Do one of the following:
   - Choose the conversation you want to view. Conversations are organized by
     date.
   - Use the search bar near the top of the chat history to find a conversation. Amazon Q
     finds conversations that match exactly the text you enter.

###### To delete a single conversation

1.  In your IDE, sign in to Amazon Q.
2.  Do one of the following:
    - In the chat tab of an open chat session, enter `/clear` to
      delete the contents of the chat tab.
    - Open an Amazon Q chat tab, and then open the chat history by doing one of the
      following:

          + On the top-right of the chat panel, choose the **View chat
           history** button.
          + Press `ctrl+F` (Windows and Linux) or `⌘ F`
           (Mac).

      In the conversation that you want to delete, choose the vertical ellipsis (⋮)
      and choose **Delete**.

###### To export a conversation to Markdown or HTML

1.  In your IDE, sign in to Amazon Q.
2.  Do one of the following:

        * With a chat session already started, on the top-right of the chat panel, choose the
         **Export** button to export the conversation displayed in the
         tab.
        * Open an Amazon Q chat tab, and then open the chat history by doing one of the
         following:




        	+ On the top-right of the chat panel, choose the **View chat
        	 history** button.
        	+ Press `ctrl+F` (Windows and Linux) or `⌘ F`
        	 (Mac).
        In the conversation that you want to export, choose the vertical ellipsis (⋮)
         and choose **Export** to export the conversation to a Markdown or
         HTML format file.

    By default, Amazon Q names the file
    `q-dev-chat-`yyyy`-`mm`-`dd`.`md|html``
    and saves it in the root of your project.
