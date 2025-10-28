# Creating project rules for Amazon Q Developer in third-party

platforms

You can build a library of project rules that you can use with Amazon Q Developer in GitLab
or GitHub. These rules describe coding standards and best practices across your team. For example,
you could have a rule that states that all Python code must use type hints, or that all Java code
must use Javadoc comments. By storing these rules in your project, you can ensure consistency
across developers, regardless of their experience level.

Project rules are defined in Markdown files in the project's
``project-root`/.amazonq/rules` folder.

Once you've created your project rules, Amazon Q Developer will automatically use them as context
within your project, and will make sure to adhere to them when generating code for feature
development.

###### To create a project rule using the file system

1. In your third-party repository, open your project's root folder.
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

6. Commit, review, and merge your changes.
7. (Optional) Add more project rule Markdown files.

You have now created one or more project rules. Amazon Q will use these rules as context
automatically within your project.
