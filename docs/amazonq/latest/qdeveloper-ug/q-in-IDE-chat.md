# Chatting with Amazon Q Developer about code

Chat with Amazon Q Developer in your integrated development environment (IDE) to ask questions about
building at AWS and for assistance with software development. Amazon Q can explain coding concepts
and code snippets, generate code and unit tests, and improve code, including debugging or
refactoring.

###### Topics

- [Working with Amazon Q in your IDE](#working-with-q-in-IDE "#working-with-q-in-IDE")
- [Example tasks](#example-tasks "#example-tasks")
- [Example questions](#example-topics-questions "#example-topics-questions")
- [Reporting issues with responses from Amazon Q](#report-issues "#report-issues")
- [Reviewing code with Amazon Q Developer](code-reviews.md "code-reviews.md")
- [Transforming code in the IDE with Amazon Q Developer](transform-in-IDE.md "transform-in-IDE.md")
- [Explaining and updating code with Amazon Q Developer](explain-update-code.md "explain-update-code.md")
- [Chatting inline with Amazon Q Developer](q-in-IDE-inline-chat.md "q-in-IDE-inline-chat.md")
- [Adding context to Amazon Q Developer chat in the IDE](ide-chat-context.md "ide-chat-context.md")
- [Chat history compaction in Amazon Q Developer](ide-chat-history-compaction.md "ide-chat-history-compaction.md")
- [Viewing, deleting, and exporting the Amazon Q Developer conversation
  history](ide-chat-conversation.md "ide-chat-conversation.md")
- [Using shortcut keys in chat with Amazon Q Developer](q-in-ides-chat-shortcuts.md "q-in-ides-chat-shortcuts.md")
- [Selecting a model for Amazon Q chat in IDEs](q-in-ides-chat-models.md "q-in-ides-chat-models.md")

## Working with Amazon Q in your IDE

### Using chat

To start chatting with Amazon Q, choose the Amazon Q icon from the navigation bar in your IDE
and enter your question in the text bar. To start chatting with Amazon Q in Visual Studio, choose
**View** from the main menu and then choose **Amazon Q
chat**.

When you ask Amazon Q a question, it uses the current file that is open in your IDE as
context, including the programming language and the file path. You can add more context in your
prompt or specify files, folders, or your whole workspace as context throughout a chat session.
For more information, see [Adding context to the chat](ide-chat-context.md "ide-chat-context.md").

If Amazon Q includes code in its response, you can copy the code or insert it directly into
your file by choosing **Insert at cursor**. Amazon Q might include inline
references to its sources in its response.

Amazon Q maintains the context of your conversation within a given session inform future
responses. You can ask follow up questions or refer to previous questions and responses
throughout the duration of your session. To start a new conversation with Amazon Q, open a new tab
in the panel. You can open up to 10 tabs at a time. Amazon Q doesn't retain context across
different conversations.

#### Chat commands

The following commands help you manage your chats with Amazon Q.

- **/clear** - Use this command to clear a current conversation. This
  removes all previous conversation from the chat panel and clears the context that Amazon Q has
  about your previous conversation.
- **/compact** - Use this command to compact your chat history when the
  context window approaches its capacity limit. This creates a concise summary of your
  conversation while preserving essential information.
- **/help** - Use this command to see an overview of what Amazon Q can and
  can't do, example questions, and available features.

### Agentic coding

With agentic coding, Amazon Q acts as your coding partner, chatting with you as you develop.
Agentic coding is on by default in the IDE. You can toggle agentic coding on or off with the
`</>` icon at the bottom of the chat panel.

When you ask Amazon Q to improve your code, it updates your files directly. You can view the
changes in a diff and have the option to undo them.

While Amazon Q is thinking or working on a task, you can continue to add instructions in the
chat panel, and it will incorporate them into its work.

As you discuss your project with Amazon Q, it will offer suggestions for shell commands.
Sometimes, when it deems those commands to be low-risk, it will run them on its own.

### Chatting in natural languages

Amazon Q Developer provides multi-language support when you chat in the IDE. Supported natural
languages include Mandarin, French, German, Italian, Japanese, Spanish, Korean, Hindi, and
Portuguese, with more languages available. To utilize this functionality, you can start a
conversation with Amazon Q in the IDE using your preferred natural language. Amazon Q automatically
detects the language and provides responses in the appropriate language.

## Example tasks

### Developing code features

###### Note

This capability used to be referred to as /dev in this documentation and in the IDE.

Amazon Q can help you develop code features, make code changes to projects, and
answer questions about software development tasks in your integrated development environment
(IDE). You explain the task you want to accomplish, and Amazon Q uses the context of your
current project or workspace to generate code that you can apply to your codebase. Amazon Q can
help you build AWS projects or your own applications.

### Unit test generation

###### Note

This capability used to be referred to as /test in this documentation and in the IDE.

Amazon Q can generate unit tests so you can automate testing throughout the
software development lifecycle. This feature helps developers focus on accelerating feature
development while ensuring code quality.

### Documentation generation

###### Note

This capability used to be referred to as /doc in this documentation and in the IDE.

Amazon Q helps you understand your code and keep documentation up to date by
generating READMEs and other documentation for your code. It can produce new documentation and
update existing documentation in your codebase.

### Code reviews

###### Note

This capability used to be referred to as /review in this documentation and in the IDE.

Amazon Q can review your codebase for security vulnerabilities and code quality issues to
improve the posture of your applications throughout the development cycle. For more information
on how to use this feature, see [Reviewing code with Amazon Q Developer](code-reviews.md "code-reviews.md").

### Transforming code

Amazon Q can transform your code in integrated development environments (IDEs) by
performing automated language and operating system (OS)-level upgrades and conversions. You
provide the code to be transformed, and Amazon Q generates changes that you can review and apply
to your files. For more information, see [Transforming code](transform-in-IDE.md "transform-in-IDE.md").

## Example questions

Within IDEs, Amazon Q can answer questions about AWS services and software development, in
addition to generating code. Amazon Q is particularly useful for answering questions related to the
following subject areas.

- Building on AWS, including AWS service selection, limits, and best practices
- General software development concepts, including programming language syntax and
  application development
- Writing code, including explaining code, debugging code, and writing unit tests

Following are some example questions that you can ask to get the most out of Amazon Q in your
IDE:

- How do I debug issues with my Lambda functions locally before deploying to AWS?
- How do I choose between AWS Lambda and Amazon EC2 for a scalable web application backend?
- What is the syntax of declaring a variable in TypeScript?
- How do I write an app in React?
- Provide me a description of what this [*selected code or application*]
  does and how it works.
- Generate test cases for [*selected code or function*].

## Reporting issues with responses from Amazon Q

You can optionally leave feedback for every response Amazon Q generates by using the thumbs-up
and thumbs-down icons. To report an issue with a response, choose the thumbs-down icon, and enter
information in the feedback window that appears.
