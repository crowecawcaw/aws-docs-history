Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Enabling generative AI features in

Amazon CodeCatalyst

Amazon Q Developer in Amazon CodeCatalyst includes generative AI features that can help users in projects
in your space develop software faster. Developers frequently have more tasks to do than
time to accomplish them. CodeCatalyst integrates with Amazon Q Developer to provide features that can help
team members accomplish their tasks more quickly and increase the time they have to focus on
the most important parts of their work. These features are only available to users if you
enable generative AI features for your space. If you choose to allow access to these
features, users can access and use these features to help them accomplish their work more
quickly. When these features are enabled, an individual user's usage of and quotas for using
Amazon Q features depends on the user's subscription to Amazon Q Developer. For more information, see
[Amazon Q Developer Pricing](https://aws.amazon.com/q/developer/pricing "https://aws.amazon.com/q/developer/pricing").

###### Important

Generative AI features are only available in the US West (Oregon) Region.

The generative AI features available for your space provide the following
functionality:

- **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development: Users
  with the Project administrator or Contributor role in a project can assign
  issues to Amazon Q. Once assigned, Amazon Q will analyze an issue based on its title
  and its description, review the code in the specified repository, and attempt to
  create a draft solution for users to evaluate. Users can assign issues to address
  problems or feature requests in code. They can also use this feature to create or
  update workflows for a project. This feature includes interactive commenting between
  users and Amazon Q in not only the issue, but in any tasks or pull requests it
  creates. Users can choose to have Amazon Q create one revision of any pull request
  it creates based on user comments left for Amazon Q.
- **Recommend tasks**: This feature helps users by using Amazon Q to
  analyze an issue and create tasks based on the issue title, description, and its
  analysis of the complexity of the issue and the repository code. This can help you
  and your team to assign individual parts of the work to users in more managable ways
  that can be achieved more quickly.
- **Write description for me**: This feature helps users creating
  pull requests create detailed descriptions of the code changes contained in the pull
  request by comparing the code in the source and destination branches and evaluating
  the impact of the differences on the overall application. This feature is not
  available for pull requests in linked repositories.
- **Create comment summary**: This feature helps users reviewing
  pull requests understand the overall direction of the comments left on the code
  changes by other reviewers by summarizing the requests and sentiments expressed in
  all comments in the overview of the pull request. This feature is not available for
  pull requests in linked repositories.

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

The generative AI features in CodeCatalyst are subject to quotas. For more information, see
[Amazon Q Developer Pricing](https://aws.amazon.com/q/developer/pricing "https://aws.amazon.com/q/developer/pricing"),
[Enabling or disabling
generative AI features for a space](managing-generative-ai-features-enable-disable.md "managing-generative-ai-features-enable-disable.md") , and [Administering billing](managing-billing.md "managing-billing.md").
