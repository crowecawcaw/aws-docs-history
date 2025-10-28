# Chatting inline with Amazon Q Developer

The _inline chat_ feature lets you chat with Amazon Q from your IDE's main coding window.
To use the inline chat feature, you highlight code that you want suggestions for, and provide instructions
in the small input screen. Amazon Q proceeds to generate code for you, which it presents in a diff within the
main coding window. You can then choose to accept or reject the changes.

The advantage of inline chat is that it eliminates the context switching that occurs when moving
between a chat window and the main coding window.

You would typically use the inline chat feature when you're reviewing code, writing unit tests, or
performing other tasks that require code-based answers. For situations where you want text-based answers
(for example, an answer to "Explain this code") then using the chat
window is a better option.

Amazon Q considers the code in the current file when generating a code recommendation through the inline
chat. It won’t look at code in other files or projects.

## Amazon Q inline chat in action

An inline chat session unfolds as follows.

1.  You highlight the code that you want suggestions for, and then choose from the following options
    based on your IDE:

        * In Visual Studio Code and JetBrains, press `⌘+I` (Mac) or `Ctrl+I` (Windows)
        * In Eclipse, press `⌘+Shift+I` (Mac) or `Ctrl+Shift+I` (Windows)
        * Alternatively, you can right-click the selection and choose **Amazon Q** and then
         **Inline chat**

    This launches a small input screen at the top of the main coding window where you can enter a
    prompt, such as `Fix this code`.

![The inline chat input screen.](images/inline-chat-input-screen.png) 2. Amazon Q generates code and presents it in a diff.

![The inline chat diff.](images/inline-chat-diff.png) 3. You accept or reject the change by choosing **Accept** or
**Reject**, or by pressing the keyboard equivalents (`Enter` or
`Esc`).

![The inline chat accept and reject buttons.](images/inline-chat-accept.png)

## Example topics and questions

The inline chat always returns code as the answer, so you can enter prompts like:

- Document this code
- Refactor this code
- Write unit tests for this function

## Diff format

The inline chat displays the diff in multiple blocks, with the existing code on the top, and the
suggested code on the bottom. A side-by-side diff is not supported.
