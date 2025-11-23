# Create a stack from repository source code with

Git sync

This topic explains how to create a CloudFormation stack that syncs to a Git repository with
Git sync.

###### Important

Before you continue, complete all [prerequisites](git-sync-prereq.md "git-sync-prereq.md")
in the previous section.

## Create a stack from

repository source code

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region to
   create the stack in.
3. On the **Stacks** page, choose **Create
   stack**, and then choose **With new resources
   (standard)**.
4. On the **Create stack** page, do the following:
   1. For **Prerequisite - Prepare template**, keep
      **Choose an existing template** selected.
   2. For **Specify template**, choose **Sync from
      Git**, and then choose **Next**.

5. On the **Specify stack details** page, for **Stack
   name**, type a name for your stack. Stack names can include letters
   (A-Z and a-z), numbers (0-9), and dashes (-).
6. For **Stack deployment file**, **Deployment file
   creation**:
   - If you _haven't_ created a stack deployment file
     and added it to your repository, choose **Create the file using
     the following parameters and place it in my
     repository.**
   - If you have a stack deployment file in your repository, choose
     **I am providing my own file in my
     repository.**

7. For **Template definition repository**, choose
   **Choose a linked Git repository** to choose a Git
   repository that's already linked to CloudFormation, or **Link a Git
   repository** to link a new one. If you choose **Link a Git
   repository**, do the following:
   1. For **Select repository provider**, choose one of the
      following:
      - **GitHub**
      - **GitHub Enterprise Server**
      - **GitLab**
      - **Bitbucket**
      - **GitLab self-managed**

   2. For **Connection**, choose a connection from the
      list. If no options appear in the **Connection** list,
      choose **add a new connection** to go to the [Connections
      console](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections") and create a connection to your repository.

8. In the **Repository** list, select the Git repository that
   contains your stack template file.
9. In the **Branch** list, select the branch you'd like
   Git sync to monitor.

###### Note

Git sync only monitors the selected branch for changes to the CloudFormation
template and stack deployment files. Any changes you'd like to apply to your
stack must be committed to this branch. 10. For the **Deployment file path**, specify the full path
including the stack deployment file name from the root of your repository
branch.

If CloudFormation is generating the file for you, this is where the file will be
committed in your repository. If you are providing the file, this is the
location of the file in your repository. 11. Add an **IAM role**. The IAM role includes permissions
that are required for CloudFormation to sync the stack from your Git repository. You
can choose **New IAM role** to generate a new role, or choose
**Existing IAM role** to select an existing role from
your AWS account. If you choose to generate a new role, the required
permissions are included in the role. 12. Enable or turn off comments on pull request:

    * To have CloudFormation post change set information in pull requests for
     stack updates, keep the **Enable comment on pull
     request** toggle switched on.
    * If you switch this toggle off, CloudFormation won't describe the
     differences between the current stack configuration and the proposed
     changes in pull requests when the repo files are updated.

13. For the **Template file path**, specify the full path from
    the root of your repository for the stack template file.
14. (Optional) To specify the stack parameters, choose **Add
    parameter**, provide a key and value for each parameter, and then
    choose **Next**. For more information, see [Stack deployment file](git-sync-concepts-terms.md#git-sync-concepts-terms-depoyment-file "git-sync-concepts-terms.md#git-sync-concepts-terms-depoyment-file").

For example, to specify a `port=8080` parameter in your
stack deployment file, do the following:

    1. Choose **Add parameter**.
    2. For **Key**, enter
     `port`.
    3. For **Value**, enter
     `8080`.

15. (Optional) To specify stack tags, choose **Add new tag**,
    provide a tag key and value for each tag, and then choose
    **Next**. For more information, see [Stack deployment file](git-sync-concepts-terms.md#git-sync-concepts-terms-depoyment-file "git-sync-concepts-terms.md#git-sync-concepts-terms-depoyment-file").
16. Choose **Next** to continue to **Configure stack
    options**. For information about configuring stack options, see
    [Configure stack options](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options").

When you've completed your stack configuration, choose **Next** to
continue. 17. Review your stack settings and confirm the following:

    * The stack template is configured correctly and set to **Sync
     from Git**.
    * The deployment file is configured correctly.
    * The template definition repository is configured correctly, in
     particular, that the correct **Repository** and
     **Branch name** are selected.
    * The preview of the deployment file is correct and contains the
     expected parameters and values.

18. Choose **Submit** to create the stack.

After you choose **Submit**, a pull request is automatically
created in your Git repository. You must merge this pull request into your Git
repository to create your stack. After the stack is created, CloudFormation monitors
your Git repository for changes.

## Update your stack from your

Git repository

To update the stack, make changes directly to your template file or stack deployment
file in your Git repository. After you commit your changes to the monitored branch,
CloudFormation automatically updates the stack. If you use pull requests, a pull request is
automatically created in your Git repository before the stack is updated. You must merge
this pull request into your Git repository to update your stack.

In the CloudFormation console, you can select the stack and choose the
**Git sync** tab to view information about the status of the stack
and sync events. For more information, see [Git sync status dashboard](git-sync-status.md "git-sync-status.md").
