# Creating project rules for use with Amazon Q Developer chat

You can build a library of project rules that you can use when chatting with Amazon Q in the IDE.
These rules describe coding standards and best practices across your team. For example, you could
have a rule that states that all Python code must use type hints, or that all Java code must use
Javadoc comments. By storing these rules in your project, you can ensure consistency across
developers, regardless of their experience level.

Project rules are defined in Markdown files in the project's
``project-root`/.amazonq/rules` folder.

Once you've created your project rules, Amazon Q will automatically use them as context whenever a
developer chats with Amazon Q within your project, and will make sure to adhere to them when generating
answers. For more information about adding context to the chat, see [Adding context to Amazon Q Developer chat in the IDE](ide-chat-context.md "ide-chat-context.md").

You can create project rules either directly in the file system or through the Amazon Q chat interface.

###### To create a project rule using the Amazon Q chat interface

1. In your IDE, open the Amazon Q chat panel.
2. In the chat input box, click the **Rules** button.
3. Select **Create new rule**.
4. In the dialog that appears, enter a name for your rule.

This will create a Markdown file with that name in your project's ``project-root`/.amazonq/rules` folder. 5. Add your rule content in the editor. 6. Save the file.

###### To create a project rule using the file system

1. In your IDE, open the project's root folder.
2. In the project root folder, create the following folder:

``project-root`/.amazonq/rules`

This folder holds all your project rules. 3. In ``project-root`/.amazonq/rules`, create a
project rule file. It must be a Markdown file. For example:

`cdk-rules.md` 4. Open your project rule Markdown file. 5. Add a detailed prompt to the file. For example:

```
All Amazon S3 buckets must have encryption enabled, enforce SSL, and block public access.
All Amazon DynamoDB Streams tables must have encryption enabled.
All Amazon SNS topics must have encryption enabled and enforce SSL.
All Amazon SNS queues must enforce SSL.
```

6. Save the file.
7. (Optional) Add more project rule Markdown files.

You have now created one or more project rules. Amazon Q will use these rules as context
automatically whenever a developer chats with Amazon Q within your project.

###### To manage rules in the Amazon Q chat interface

1. In your IDE, open the Amazon Q chat panel.
2. In the chat input box, click the **Rules** button to see all available rules.
3. Click on a rule to toggle it on or off for the current chat session:
   - Rules with a check mark are active and will be applied to your conversation.
   - Rules without a check mark are inactive for the current session.
