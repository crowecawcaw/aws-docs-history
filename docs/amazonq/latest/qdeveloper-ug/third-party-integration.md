# Third-party integration with Amazon Q Developer

Amazon Q Developer integrates with popular development platforms to enhance your software development workflows
through specialized artificial intelligence (AI) capabilities. Supported integrations include and GitLab Duo and GitHub,
providing AI-powered assistance throughout the development lifecycle. These integrations help streamline development by
automating routine tasks, improving code quality, and accelerating modernization efforts.

## GitLab Duo with Amazon Q Developer

GitLab Duo with Amazon Q Developer provides a comprehensive suite of AI experiences integrated directly into your GitLab
workflows. Available for GitLab Self-Managed offering and Ultimate tier subscribers, the integration enables quick actions
in GitLab issues and merge requests to trigger AI capabilities. The integration also includes GitLab Duo Chat powered by Amazon Q,
providing contextual assistance throughout your development process.

GitLab Duo with Amazon Q provides:

- Feature development of high-level ideas with a quick action in GitLab issues
- Code reviews for code quality, issues, and security concerns with a quick action in merge requests
- Code modernization to latest supported Java version with a quick action in GitLab issues
- Unit test generation with a quick action in merge requests
- Integrated chat support for development tasks

To get started, see [Set up GitLab Duo with
Amazon Q](https://docs.gitlab.com/user/duo_amazon_q/setup/ "https://docs.gitlab.com/user/duo_amazon_q/setup/").

## Amazon Q Developer for GitHub (Preview)

The Amazon Q Developer integration with GitHub enables automated feature development, code reviews, and Java modernization
through specialized AI agents. When you assign a GitHub issue to Amazon Q Developer, it uses the issue and project code as context
to generate new code and create a pull request. During the development process, you can provide feedback and Amazon Q Developer
iterates on the suggested code, creating a collaborative development workflow.

Amazon Q Developer offers the following key capabilities in GitHub:

- Feature development label that automatically implements new features and bug fixes from idea to pull request
- Automated code reviews of new or reopened pull requests for code quality, issues, and security concerns
- Code transformation label that automatically upgrades codebase to supported Java version
- Slash commands to provide alternative ways to initiate feature development and code transformation from issues,
  and code reviews after initial automatic review
- Iterative development by providing feedback on generated code and implementing
- Browser extensions to quickly assign feature development and code transformation tasks to Amazon Q Developer

To get started, see [Quickstart: Installing, using features in GitHub, and increasing
usage limits](github-quickstart.md "github-quickstart.md").

## Project rules for Amazon Q Developer

Amazon Q Developer enables you to create and maintain project-specific rules in GitLab or GitHub, which define coding standards
and best practices for your team (such as requiring type hints in Python code or Javadoc comments in Java code). These rules,
stored as Markdown files in the ``project-root`/.amazonq/rules` directory,
ensure consistency across all developers regardless of experience level, and are automatically incorporated into context
for Amazon Q Developer when developers interact with Amazon Q Developer within your project, ensuring all generated responses adhere to your
established guidelines. For more information, see [Creating project rules for Amazon Q Developer in third-party
platforms](third-party-context-project-rules.md "third-party-context-project-rules.md").
