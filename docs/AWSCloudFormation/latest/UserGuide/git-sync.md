# Syncing stacks with source code stored in a Git repository with

Git sync

With Git sync, you can manage your CloudFormation stacks with source control. You do this by
configuring CloudFormation to monitor a Git repository. The repository is monitored for changes to
two files:

- A CloudFormation template file that defines a stack
- A stack deployment file that contains parameters that configure the stack
  With Git sync, you can use pull requests and version tracking to configure, deploy, and
  update your CloudFormation stacks from a centralized location. When you commit changes to the
  template or the deployment file, CloudFormation automatically updates the stack. If you use pull
  requests, CloudFormation can leave a comment on the pull request explaining what changes will be
  made to your stack before actually updating it. However, you need to enable this feature first.

Git sync provides a console interface that you can use to link to a repository, generate a
stack deployment file, update a CloudFormation template, and submit a pull request to your
repository. Git sync also provides a status dashboard that you can use to monitor, edit, and
troubleshoot active Git sync stack deployments. Git sync is accessed through the [CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/") when you [create a stack](cfn-console-create-stack.md "cfn-console-create-stack.md"). You can also access Git sync using
CodeConnections. For more information, see [Working with sync configurations for
linked repositories](../../../dtconsole/latest/userguide/configurations.md "../../../dtconsole/latest/userguide/configurations.md") in the _Developer Tools Console User
Guide_.

Git sync supports [GitHub](https://github.com/ "https://github.com/"), [GitHub Enterprise](https://github.com/enterprise "https://github.com/enterprise"), [GitLab](https://about.gitlab.com/ "https://about.gitlab.com/"), [Bitbucket](https://bitbucket.org "https://bitbucket.org"), and [GitLab self-managed](https://docs.gitlab.com/subscriptions/self_managed/ "https://docs.gitlab.com/subscriptions/self_managed/") repositories.

###### Note

Git sync is available in the following regions: US East (N. Virginia), US East (Ohio),
US West (N. California), US West (Oregon), Canada (Central), Asia Pacific (Mumbai),
Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore),
Asia Pacific (Sydney), Europe (Ireland), Europe (London), Europe (Paris),
Europe (Stockholm), Europe (Frankfurt), Europe (Milan), and
South America (São Paulo).

For information about using Git sync with a multi-account strategy, see
the following blog post [Use
CloudFormation Git sync to configure resources in customer accounts](https://aws.amazon.com/blogs/devops/use-aws-cloudformation-git-sync-to-configure-resources-in-customer-accounts/ "https://aws.amazon.com/blogs/devops/use-aws-cloudformation-git-sync-to-configure-resources-in-customer-accounts/").

###### Topics

- [How Git sync works](git-sync-concepts-terms.md "git-sync-concepts-terms.md")
- [Prerequisites](git-sync-prereq.md "git-sync-prereq.md")
- [Create a stack from repository source
  code](git-sync-create-stack-from-repository-source-code.md "git-sync-create-stack-from-repository-source-code.md")
- [Enable comments on pull
  requests](gitsync-enable-comments-on-pull-requests.md "gitsync-enable-comments-on-pull-requests.md")
- [Status dashboard](git-sync-status.md "git-sync-status.md")
