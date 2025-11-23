# Adding context to Amazon Q Developer chat in the IDE

When you chat with Amazon Q in the integrated development environment (IDE), you can provide Amazon Q with
additional _context_, such as files and folders, that Amazon Q can use to tailor and
improve its answers.

There are two ways to provide context to Amazon Q:

- **Explicitly** – To provide context explicitly, you
  enter `@` in the chat window. The `@` launches a
  context picker pop-up from which you select items to include as context. Alternatively, you
  can type `@` and begin typing the name of the file, folder, or other
  context type to have it auto-complete. For more information, see [Explicit context types](#context-explicit "#context-explicit").
- **Automatically** – To provide context automatically,
  you set up the context separately, outside of the chat. Amazon Q automatically references the
  context whenever any developer working on the project types a question into the chat window.
  For more information, see [Automatic context types](#context-automatic "#context-automatic").
  After Amazon Q generates an answer, it shows you the files it used as context in the
  **Context** drop-down list, which appears immediately above the start of the
  answer.

## Explicit context types

When you type `@` in the chat, you can select from the following context
types:

- **@workspace** – Amazon Q uses your project’s workspace as context
  for its answers. The **@workspace** option requires configuration. For
  more information, see [Adding workspace context to Amazon Q Developer chat in the
  IDE](workspace-context.md "workspace-context.md").
- **Folders** – Amazon Q shows you a list of folders in the current
  project, and uses the folder you select as context for its answers.
- **Files** – Amazon Q shows you a list of files in the current
  project, and uses the file you select as context for its answers.
- **Code** – Amazon Q shows you a list of classes, functions, global
  variables in the current project, and uses your selection as
  context for its answers.
- **Images** – Amazon Q allows you to add images as context
  for your prompts, useful for scenarios like generating code from UI mockups or sequence
  diagrams. Images must be in JPEG, PNG, GIF, or WebP format, with a maximum size of 3.75 MB
  and dimensions not exceeding 8,000 x 8,000 pixels. You can include up to 20 images in a
  single message, including any images pinned to context.
- **Prompts** – Amazon Q shows you a list of prompts that you have
  saved, and uses the prompt you select as context for its answers. The
  **Prompts** option requires some configuration. For more information,
  see [Saving prompts to a library for use with Amazon Q Developer
  chat](context-prompt-library.md "context-prompt-library.md").

## Automatic context types

The following types of contexts will be used automatically by Amazon Q, if you've set them up:

- **Project rules** – Amazon Q will automatically use a set of project
  rules that you define as context. For more information, see [Creating project rules for use with Amazon Q Developer
  chat](context-project-rules.md "context-project-rules.md").
- **Customizations** – Amazon Q will automatically use a repository of
  source code as context.
