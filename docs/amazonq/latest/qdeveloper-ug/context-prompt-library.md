# Saving prompts to a library for use with Amazon Q Developer chat

You can build a library of common prompts that you can use when chatting with Amazon Q in the IDE. By
storing these prompts in your library, you can easily insert them into the chat without having to
retype the prompt each time. You can use saved prompts across multiple conversations and
projects.

Prompts are saved in the `~/.aws/amazonq/prompts` folder.

###### To save a prompt to a prompt library

1. In your IDE, open an Amazon Q chat window.
2. Type `@`, and select **Prompts**.
3. Choose **Create a new prompt**. (You might have to scroll down to find it.)
4. In **Prompt name**, enter a prompt name such as `Create_sequence_diagram` and press Enter. Note that prompt names cannot include spaces.

Amazon Q creates a prompt file called `Create_sequence_diagram.md` in the
`~/.aws/amazonq/prompts` folder, and opens the file in your
IDE. 5. In the prompt file, add a detailed prompt. For example:

`Create a sequence diagram using Mermaid that shows the sequence of calls between
 resources. Ignore supporting resources like IAM policies and security group
 rules.` 6. Save the prompt file.

###### To use a saved prompt

1. In your IDE, open an Amazon Q chat window.
2. Type `@`, and select **Prompts**.
3. Choose your saved prompt, for example, **Create_sequence_diagram**.
4. (Optional) In the chat input window, add details, as required. You can type more text
   and add more context types. An example prompt might look like this...

`**@Create\_sequence\_diagram** using the files in the
 **@lib** folder` 5. Submit the prompt and wait for Amazon Q to generate an answer.
