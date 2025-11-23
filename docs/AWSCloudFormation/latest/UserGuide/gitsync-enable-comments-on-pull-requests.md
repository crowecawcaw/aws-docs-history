# Enable CloudFormation to post a

summary of stack changes in pull requests

This topic shows you how to enable CloudFormation to post a summary of stack changes in pull
requests in your Git repository.

By enabling the comments on pull requests feature, you allow CloudFormation to post a comment
that describes the differences between the current stack configuration and the proposed
changes when the repo files are updated. This comment provides a summary of the resources that
will be added, modified, or deleted, allowing you to perform a thorough code review before
merging the pull request.

###### To enable comments on pull requests for a new stack (console)

When you create the stack, on the **Specify stack details** page, under
**Template definition repository**, make sure the **Enable
comment on pull request** toggle is switched on. This is the default setting for
new stacks.

###### To enable comments on pull requests for an existing stack (console)

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region that you
   created your stack in.
3. On the **Stacks** page, choose the running stack that you want to
   update.
4. Choose the **Git sync** tab, and then choose
   **Edit**.
5. On the **Edit Git sync settings** page, under **Template
   definition repository**, switch the **Enable comment on pull
   request** toggle on.
6. Choose **Update configuration**.
