Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Using CodeCatalyst generative AI

features to speed up your development work

If you have a project and a source repository in Amazon CodeCatalyst in a space where
generative AI features are enabled, you can use these features to help speed up software
development. Developers frequently have more tasks to do than time to accomplish them. They
often don't take the time to explain their code changes to their teammates when creating
pull requests for review of those changes, expecting other users to find the changes
self-explanatory. Pull request creators and reviewers also don't have time to find and read
all the comments on a pull request thoroughly, particularly if the pull request has multiple
revisions. CodeCatalyst integrates with the Amazon Q Developer Agent for software development to provide generative AI features that can
both help team members accomplish their tasks more quickly, and increase the time they have
to focus on the most important parts of their work.

Amazon Q Developer is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. To accelerate your building
on AWS, the model that powers Amazon Q is augmented with high-quality AWS content to produce more complete, actionable, and referenced answers. For more information, see [What is Amazon Q Developer?](../../../amazonq/latest/aws-builder-use-ug/what-is.md "../../../amazonq/latest/aws-builder-use-ug/what-is.md") in the _Amazon Q Developer User Guide_.

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

In this tutorial, you'll learn how to use the generative AI features in CodeCatalyst to help you
create projects with blueprints, as well as add blueprints to existing projects.
Additionally, you'll learn how to summarize changes between branches when creating pull
requests and to summarize comments left on a pull request. You'll also learn how to create
issues with your ideas for code changes or improvements and assign them to Amazon Q. As
part of working with issues assigned to Amazon Q, you'll learn how to allow Amazon Q to
suggest tasks and how to assign and work on any tasks it creates as part of working on an
issue.

###### Topics

- [Prerequisites](#getting-started-project-assistance-prerequisites "#getting-started-project-assistance-prerequisites")
- [Using Amazon Q to choose
  a blueprint when creating a project or adding functionality](#getting-started-project-assistance-create-apply-bp "#getting-started-project-assistance-create-apply-bp")
- [Create a
  summary of the code changes between branches when creating a pull request](#getting-started-project-assistance-pull-request-summary "#getting-started-project-assistance-pull-request-summary")
- [Create a summary of
  comments left on code changes in a pull request](#getting-started-project-assistance-comment-summary "#getting-started-project-assistance-comment-summary")
- [Create an issue and
  assign it to Amazon Q](#getting-started-project-assistance-issue-to-code "#getting-started-project-assistance-issue-to-code")
- [Create an issue and
  have tasks recommended for it by Amazon Q](#getting-started-project-assistance-issue-to-tasks "#getting-started-project-assistance-issue-to-tasks")
- [Clean up resources](#getting-started-project-assistance-clean-up "#getting-started-project-assistance-clean-up")

## Prerequisites

To work with the CodeCatalyst features in this tutorial, you must have first completed and have access to the following resources:

- You have an AWS Builder ID or a single sign-on (SSO) identity for signing in to
  CodeCatalyst.
- Your are in a space that has generative AI features enabled. For
  more information, see [Managing generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md").
- You have the Contributor or Project administrator role in a project in
  that space.
- Unless you are creating a project with generative AI, your existing project
  has at least one source repository configured for it. Linked repositories are not
  supported.
- When assigning issues to have an initial solution created by generative AI,
  the project cannot be configured with the **Jira Software**
  extension. The extension is not supported for this feature.

For more information, see [Creating a space](spaces-create.md "spaces-create.md"), [Track and organize work with issues in CodeCatalyst](issues.md "issues.md"), [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md"), and [Granting access with user roles](ipa-roles.md "ipa-roles.md").

This tutorial is based on a project created using the
**Modern three-tier web application** blueprint with Python. If you use a
project created with a different blueprint, you can still follow the steps, but some
specifics will vary, such as sample code and language.

## Using Amazon Q to choose

a blueprint when creating a project or adding functionality

As a project developer, you can collaborate with Amazon Q, a generative AI assistant,
when creating new projects or adding components to existing projects. You can provide Amazon Q
with requirements for your project by interacting with it in a chat-like interface. Based on
your requirements, Amazon Q suggests a blueprint and also outlines requirements that can’t be
met. If your space has custom blueprints, Amazon Q learns and includes those blueprints in
the recommendations as well. You can then proceed with Amazon Q’s suggestion if you’re satisfied,
and it will create the necessary resources such as a source repository with code for your
requirement. Amazon Q also creates issues for requirements that can’t be satisfied with a blueprint.
To learn more about available CodeCatalyst blueprints, see [Creating a comprehensive project with CodeCatalyst blueprints](project-blueprints.md "project-blueprints.md"). To learn more about using Amazon Q with blueprints,
see [Best practices when using Amazon Q to create projects
or add functionality with blueprints](projects-create.md#projects-create-amazon-q "projects-create.md#projects-create-amazon-q").

###### To create a project with Amazon Q

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you
   want to create a blueprint.
3. On the space dashboard, choose **Create with Amazon Q**.
4. In the Amazon Q prompt text input field, provide instructions by writing a brief description
   about the project you want to build. For example, `“I want to create a project in Python that has a 
presentation layer responsible for how the data is presented, an application layer that contains the 
core logic and functionality of the application, and a data layer that manages the storage and 
retrieval of the data.”`

(Optional) Under **Try examples**, you can use a prewritten prompt by choosing
a blueprint. For example, if you choose React app, the following prompt is provided : `“I want to 
 create a project in Python that has a presentation layer responsible for how the data is presented, 
 an application layer that contains the core logic and functionality of the application, and a data 
 layer that manages the storage and retrieval of the data. I also want to add authentication and 
 authorization mechanisms for security and allowable actions.”` 5. Choose **Send** to submit your instructions to Amazon Q. The generative AI
assistant provides a suggestion and outlines requirements that can’t be met by the blueprint. For
example, Amazon Q might suggest the following based on your criteria:

```
I recommend using the Modern three-tier web application blueprint based on
                    your requirements. Blueprints are dynamic and can always be updated and edited later.

**Modern three-tier web application**
By Amazon Web Services

This blueprint creates a Mythical Mysfits 3-tier web application with a modular presentation, application, and data layers.
The application leverages containers, infrastructure as code (IaC), continuous integration and continuous delivery (CI/CD),
and serverless code functions.

**Version:** 0.1.163

View details

**The following requirements could not be met so I will create issues for you.**
• Add authentication and authorization mechanisms for security and allowable actions.

```

6. (Optional) To view the in-depth details of the suggested blueprint, choose **View
   details**.
7. Do one of the following:
   1. Choose **Yes, use this blueprint** if you’re satisfied with the suggestion.
   2. Choose **Edit prompt** if you want to modify the prompt.
   3. Choose **Start over** if you want to clear the prompt completely.

8. Do one of the following:
   1. Choose **Configure** if you want to configure the blueprint that is suggested.
      You can also configure the blueprint at a later time.
   2. Choose **Skip** if you don’t want to modify the blueprint configurations at the
      moment.

9. If you chose to configure the blueprint, choose **Continue** after modifying the project
   resources.
10. When prompted, enter the name that you want to assign to your project and its associated resource names.
    The name must be unique within your space.
11. Choose **Create project** to create a project with the blueprint. Amazon Q creates resources using
    the blueprint. For example, if you create a project with the Single-page application blueprint, a source repository for
    relevant code and workflows for CI/CD are created.
12. (Optional) By default, Amazon Q also creates issues for the requirements that aren’t satisfied by a blueprint. You can choose which items
    you don't want to create issues for. After you choose to let Amazon Q create issues, you can then assign an issue
    to Amazon Q as well. It’ll analyze the issue in the context of the given source repositories, providing a summary of the
    relevant source files and code. For more information, see [Finding and viewing issues](issues-view.md "issues-view.md"),
    [Create an issue and
    assign it to Amazon Q](#getting-started-project-assistance-issue-to-code "#getting-started-project-assistance-issue-to-code"),
    and [Best practices
    when creating and working with issues assigned to Amazon Q](issues-create-issue.md#issues-create-issue-assign-genai-best-practices "issues-create-issue.md#issues-create-issue-assign-genai-best-practices").

After creating a project with Amazon Q, you can also use Amazon Q to add new components as it suggests CodeCatalyst blueprints
based on your requirements.

###### To add a blueprint with Amazon Q

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the project where you
   want to add a blueprint.
3. Choose **Add with Amazon Q**.
4. In the Amazon Q prompt text input field, provide instructions by writing a brief description
   about the project you want to build. For example, `“I want to create a project in Python that has a 
presentation layer responsible for how the data is presented, an application layer that contains the 
core logic and functionality of the application, and a data layer that manages the storage and 
retrieval of the data.”`

(Optional) Under **Try examples**, you can use a prewritten prompt by choosing
a blueprint. For example, if you choose React app, the following prompt is provided : `“I want to 
 create a project in Python that has a presentation layer responsible for how the data is presented, 
 an application layer that contains the core logic and functionality of the application, and a data 
 layer that manages the storage and retrieval of the data. I also want to add authentication and 
 authorization mechanisms for security and allowable actions.”` 5. Choose **Send** to submit your instructions to Amazon Q. The generative AI
assistant provides a suggestion and outlines requirements that can’t be met by the blueprint. For
example, Amazon Q might suggest the following based on your criteria:

```
I recommend using the Single-page application blueprint based on your requirements. Blueprints are dynamic and can always be updated and edited later.

**Single-page application**
By Amazon Web Services

This blueprint creates a SPA (single-page application) using React, Vue, or Angular frameworks and deploys to AWS Amplify Hosting.

**Version:** 0.2.15
View details

**The following requirements could not be met so I will create issues for you.**
• The application should have reusable UI components
• The application should support for client-side routing
• The application may require server-side rendering for improved performance and SEO

```

6. (Optional) To view the in-depth details of the suggested blueprint, choose **View
   details**.
7. Do one of the following:
   1. Choose **Yes, use this blueprint** if you’re satisfied with the suggestion.
   2. Choose **Edit prompt** if you want to modify the prompt.
   3. Choose **Start over** if you want to clear the prompt completely.

8. Do one of the following:
   1. Choose **Configure** if you want to configure the blueprint that is suggested.
      You can also configure the blueprint at a later time.
   2. Choose **Skip** if you don’t want to modify the blueprint configurations at the
      moment.

9. If you chose to configure the blueprint, choose **Continue** after modifying the project
   resources.
10. Choose **Add to project** to add resources to a project with the blueprint. Amazon Q creates resources using
    the blueprint. For example, if you add to a project with the Single-page application blueprint, a source repository for
    relevant code and workflows for CI/CD are created.
11. (Optional) By default, Amazon Q also creates issues for the requirements that aren’t satisfied by a blueprint. You can choose which items
    you don't want to create issues for. After you choose to let Amazon Q create issues, you can then assign an issue
    to Amazon Q as well. It’ll analyze the issue in the context of the given source repositories, providing a summary of the
    relevant source files and code. For more information, see [Create an issue and
    assign it to Amazon Q](#getting-started-project-assistance-issue-to-code "#getting-started-project-assistance-issue-to-code")
    and [Best practices
    when creating and working with issues assigned to Amazon Q](issues-create-issue.md#issues-create-issue-assign-genai-best-practices "issues-create-issue.md#issues-create-issue-assign-genai-best-practices").

## Create a

summary of the code changes between branches when creating a pull request

A pull request is the primary way you and other project members can review, comment
on, and merge code changes from one branch to another. You can use pull requests to
review code changes collaboratively for minor changes or fixes, major feature additions,
or new versions of your released software. Summarizing the code changes and the intent
behind the changes as part of the pull request's description is helpful to others who
will review the code, and also helps with a historical understanding of the changes to
the code over time. However, developers often rely on their code to explain itself or
provide ambiguous details rather than describing their changes with enough details for
reviewers to understand what they are reviewing or what the intent was behind the
changes in the code.

You can use the **Write description for me** feature when creating
pull requests to have Amazon Q create a description of the changes contained in a pull
request. When you choose this option, Amazon Q analyzes the differences between the
source branch that contains the code changes and the destination branch where you want
to merge these changes. It then creates a summary of what those changes are, as well as
its best interpretation of the the intent and effect of those changes.

###### Note

This feature does not work with Git submodules. It will not summarize any changes
in a Git submodule that is part of the pull request.

This feature is not available for pull requests in linked repositories.

You can try this feature with any pull request you create, but in this tutorial, we'll
test it out by making some simple changes to the code contained in a project created in
a Python-based **Modern three-tier web application** blueprint.

###### Tip

If you are using a project created with a different blueprint or your own code, you can
still follow this tutorial, but the examples in this tutorial will not match the
code in your project. Instead of the suggested example below, make simple changes in
your project's code in a branch, and then create a pull request to test the feature
as shown in the following steps.

First, you will create a branch in the source repository. You'll then make a quick
code change to a file in that branch using the text editor in the console. You'll then
create a pull request, and use the **Write description for me** feature
to summarize the changes you made.

###### To create a branch (console)

1. In the CodeCatalyst console, navigate to the project where your source repository resides.
2. Choose the name of the repository from the list of source repositories for the project.
   Alternatively, in the navigation pane, choose **Code**, and then choose
   **Source repositories**.
3. Choose the repository where you want to create a branch.
4. On the overview page of the repository, choose **More**, and then choose
   **Create branch**.
5. Enter a name for the branch.
6. Choose a branch to create the branch from, and then choose **Create**.

Once you have a branch, edit a file in that branch with a simple change. In this example, you'll edit the `test_endpoint.py` file
to change the number of retries for tests from `3` to **5**.

###### Tip

You can also choose to create or use a Dev Environment to make this code change. For
more information, see [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md").

###### To edit the `test_endpoint.py` file in the console

1. On the overview page for the `mysfits` source repository, choose the
   branch drop-down and choose the branch you created in the previous
   procedure.
2. In **Files**, navigate to the file you want to edit. For example, to edit the `test_endpoint.py` file,
   expand **tests**, expand **integ**, and then choose `test_endpoint.py`.
3. Choose **Edit**.
4. On line 7, change the number of times all tests will be retried from:

```
def test_list_all(retry=3):
```

to:

```
def test_list_all(retry=`5`):
```

5. Choose **Commit** and commit your changes to your branch.

Now that you have a branch with a change, you can create a pull request.

###### Create a pull request with a summary of the changes

1. On the overview page of the repository, choose **More**, and then choose **Create pull request**.
2. In **Destination branch**, choose the branch to merge the code into after
   it is reviewed.

###### Tip

Choose the branch that you created your branch from in the previous
procedure for the simplest demonstration of this feature. For example, if
you created your branch from the repository's default branch, choose that
branch as the destination branch for your pull request. 3. In **Source branch**, choose the branch that contains the changes you just committed to the `test_endpoint.py` file. 4. In **Pull request title**, enter a title that helps other users
understand what needs to be reviewed and why. 5. In **Pull request description**, choose **Write
description for me** to have Amazon Q create a description of the
changes contained in the pull request. 6. A summary of the changes appears. Review the suggested text and then
choose **Accept and add to description**. 7. Optionally, modify the summary to better reflect the changes you made to the code. You can also choose to add reviewers or link issues to this pull request.
When you have finished making any additional changes you want, choose **Create**.

## Create a summary of

comments left on code changes in a pull request

When users review a pull request, they often leave multiple comments on the changes in
that pull request. If there are a lot of comments from a lot of reviewers, it can be
difficult to pick out common themes in the feedback, or even be sure that you've
reviewed all the comments in all revisions. You can use the **Create comment
summary** feature to have Amazon Q analyze all the comments left on code
changes in a pull request and create a summary of those comments.

###### Note

Comment summaries are transient. If you refresh a pull request, the summary will
disappear. Content summaries do not include comments on the overall pull request,
just comments left on differences in code in revisions of the pull request.

This feature does not work with any comments left on code changes in Git
submodules.

This feature is not available for pull requests in linked repositories.

###### To create a summary of comments in a pull request

1. Navigate to the pull request you created in the previous procedure.

###### Tip

If you prefer, you can use any open pull request in your project. In the
navigation bar, choose **Code**, choose **Pull
requests**, and choose any open pull request. 2. Add a few comments to the pull request in **Changes** if the pull request
does not already have comments. 3. In **Overview**, choose **Create comment summary**. When
complete, the **Comment summary** section expands. 4. Review the summary of comments left on changes in the code in revisions of the pull request,
and compare it to the comments in the pull request.

## Create an issue and

assign it to Amazon Q

Development teams create issues to track and manage their work, but sometimes an issue
lingers because either it's not clear who should work on it, or the issue requires
research into a particular part of the code base, or other urgent work must be attended
to first. CodeCatalyst includes integration with Amazon Q Developer Agent for software development. You can assign issues to a
generative AI assistant called **Amazon Q** that can analyze an issue
based on its title and its description. If you assign the issue to Amazon Q, it will
attempt to create a draft solution for you to evaluate. This can help you and your team
to focus and optimize your work on issues that require your attention, while Amazon Q
works on a solution for problems you don't have resources to address immediately.

###### Tip

**Amazon Q** performs best on simple issues and straightforward
problems. For best results, use plain language to clearly explain what you want
done.

When you assign an issue to **Amazon Q**, CodeCatalyst will mark the
issue as blocked until you confirm how you want Amazon Q to work on the issue. It
requires you to answer three questions before it can continue:

- Whether you want to confirm every step it takes or whether you want it to
  proceed without feedback. If you choose to confirm each step, you can reply to
  Amazon Q with feedback on the approach it creates so it can iterate on its
  approach if needed. Amazon Q can also review feedback users leave on any pull
  request it creates if you choose this option. If you choose not to confirm each
  step, Amazon Q might complete its work more quickly, but it won't review any
  feedback you give it in the issue or in any pull request it creates.
- Whether you want to allow it to update workflow files as part of its work.
  Your project might have workflows configured to start runs on pull request
  events. If so, any pull request that Amazon Q creates that includes creating
  or updating workflow YAML might start a run of those workflows included in the
  pull request. As a best practice, don't choose to allow Amazon Q to work on
  workflow files unless you are sure there are no workflows in your project that
  will automatically run these workflows before you review and approve the pull
  request it creates.
- Whether you want to allow it to suggest creating tasks to break down the work
  in the issue into smaller increments that can be individually assigned to users,
  including Amazon Q itself. Allowing Amazon Q to suggest and create tasks can
  help accelerate development on complex issues by allowing multiple people to
  work on discrete portions of the issue. It can also help reduce the complexity
  of understanding the entirety of the work as the work needed to complete each
  task is ideally simpler than the issue it belongs to.
- What source repository you want it to work in. Even if your project has
  multiple source repositories, Amazon Q can only work on code in one source
  repository. Linked repositories are not supported.

Once you have made and confirmed your choices, **Amazon Q** will
move the issue into the **In progress** state while it attempts to
determine what the request is based on the issue title and its description, as well as
the code in the specified repository. It will create a pinned comment where it will
provide updates on the status of its work. After reviewing the data, Amazon Q will
formulate a potential approach to a solution. Amazon Q records its actions by updating
its pinned comment and commenting on its progress on the the issue at every stage.
Unlike pinned comments and replies, it does not keep a strictly chronological record of
its work. Rather, it puts the most relevant information about its work at the top-level
of the pinned comment. It will attempt to create code based on its approach and its
analysis of the code already in the repository. If it successfully generates a potential
solution, it will create a branch and commit code to that branch. It then creates a pull
request that will merge that branch with the default branch. When Amazon Q completes
its work, it moves the issue to **In review** so that you and your team
knows there is code ready for you to evaluate.

###### Note

This feature is only available through **Issues** in the US West (Oregon) Region. It is not
available if you have configured your project to use Jira with the **Jira
Software** extension. Additionally, if you have customized the layout
of your board, the issue might not change states. For best results, only use this
feature with projects that have a standard board layout.

This feature does not work with Git submodules. It cannot make changes to any Git
submodules included in the repository.

Once you have assigned an issue to Amazon Q, you cannot change the title or
description of the issue or assign it to anyone else. If you unassign
**Amazon Q** from the issue, it will finish its current step
and then stop work. It cannot resume work or be reassigned to the issue once it is
unassigned.

An issue can be automatically moved into the **In review** column
if assigned to Amazon Q if a user chooses to allow it to create tasks. However,
the issue in **In review** might still have tasks that are in a
different state, such as in the **In progress** state.

In this portion of the tutorial, you will create three issues based on potential
features for the code included in projects created with the
**Modern three-tier web application** blueprint: one to add a to create a new
mysfit creature, one to add a sort feature, and one to update a workflow to include a
branch named `test`.

###### Note

If you are working in a project with different code, create issues with titles and
descriptions that relate to that code base.

###### To create an issue and have a solution generated for you to evaluate

1. In the navigation pane, choose **Issues** and make sure you
   are in the **Board** view.
2. Choose **Create issue**.
3. Give the issue a title that explains what you want to do in plain language. For example, for
   this issue, enter a title of `Create another mysfit named
Quokkapus`. In **Description**, provide the
   following details:

```
Expand the table of mysfits to 13, and give the new mysfit the following characteristics:

Name: Quokkapus

Species: Quokka-Octopus hybrid

Good/Evil: Good

Lawful/Chaotic: Chaotic

Age: 216

Description: Australia is full of amazing marsupials, but there's nothing there quite like the Quokkapus.
She's always got a friendly smile on her face, especially when she's using her eight limbs to wrap you up
in a great big hug. She exists on a diet of code bugs and caffeine. If you've got some gnarly code that needsa
assistance, adopt Quokkapus and put her to work - she'll love it! Just make sure you leave enough room for
her to grow, and keep that coffee coming.
```

4. (Optional) Attach an image to use as the thumbnail and profile picture for the
   mysfit to the issue. If you do this, update the description to include details
   of what images you want to use and why. For example, you might add the following
   to the description: "The mysfit requires image files to be deployed to the
   website. Add these images attached to this issue to the source repository as
   part of the work, and deploy the images to the website."

###### Note

Attached images might or might not be deployed to the website during the
interactions in this tutorial. You can add the images to the website
yourself, and then leave comments for Amazon Q to update its code to point
to the images you want it to use after it has created a pull request.

Review the description and make sure it contains all the details that might be
needed before you proceed to the next step. 5. In **Assignees**, choose **Assign to Amazon Q**. 6. In **Source repository**, choose the source repository that
contains the project code. 7. Slide the **Require Amazon Q to stop after each step and await
review of its work** selector to the active state if
necessary.

###### Note

Choosing the option to have Amazon Q stop after every step allows you to
comment on the issue or any created tasks to have the option to have
Amazon Q change its approach up to three times based on your comments. If
you choose the option to not have Amazon Q stop after every step so that
you can review its work, work might proceed more quickly because Amazon Q
isn't waiting for your feedback, but you won't be able to influence the
direction Amazon Q takes by leaving comments. Amazon Q will also not
respond to comments left in a pull request if you choose that option. 8. Leave the **Allow Amazon Q to modify workflow files**
selector in the inactive state. 9. Slide the **Allow Amazon Q to suggest creating tasks**
selector to the active state. 10. Choose **Create issue**. Your view changes to the Issues board. 11. Choose **Create issue** to create another issue, this time one with the title `Change the get_all_mysfits() API to return 
 mysfits sorted by the Age attribute`. Assign this issue to **Amazon Q** and create the issue. 12. Choose **Create issue** to create another issue, this time one with the title
`Update the OnPullRequest workflow to include a branch named test
 in its triggers`. Optionally link to the workflow in the
description. Assign this issue to **Amazon Q** but this time
make sure that the **Allow Amazon Q to modify workflow
files** selector is set to the active state. Create the issue to
return to the Issues board.

###### Tip

You can search for files, including workflow files, by entering the at
symbol (`@`) and entering the file name.

Once you have created and assigned the issues, the issues will move into **In
progress**. Amazon Q will add comments tracking its progress inside the
issue in a pinned comment. If it is able to define an approach to a solution, it will
update the issue's description with a **Background** section that
contains its analysis of the code base and a **Approach** section that
details its proposed approach to creating a solution. If Amazon Q is successful in
coming up with a solution to the problem described in the issue, it will create a branch
and code changes in that branch that implement its proposed solution. If the proposed
code contains similarities to open source code that Amazon Q is aware of, it will provide
a file that includes links to that code so that you can review it. Once the code is
ready, it creates a pull request so that you can review the suggested code changes, adds
a link to that pull request to the issue, and moves the issue into **In
review**.

###### Important

You should always review any code changes in a pull request before merging it.
Merging code changes made by Amazon Q, like any other code changes, can negatively
impact your code base and infrastructure code if the merged code is not properly
reviewed and contains errors when merged.

###### To review an issue and linked pull request that contains changes made by Amazon Q

1. In **Issues**, choose an issue assigned to Amazon Q that is in **In
   progress**. Review the comments to monitor the progress of
   Amazon Q. If present, review the background and approach it records in the
   description of the issue. If you chose to allow Amazon Q to suggest tasks,
   review any proposed tasks and take any needed action. For example, if Amazon Q
   suggested tasks and you would like to change the order or assign tasks to
   specific users, choose **Change, add, or reorder tasks** and
   perform any updates necessary. When you are done viewing the issue, choose
   **X** to close the issue pane.

###### Tip

To view progress on tasks, choose the task from the list of tasks in the
issue. Tasks don't appear as separate items on the board and can only be
accessed through an issue. If a task is assigned to Amazon Q, you must
open the task to approve any actions it wants to perform. You must also open
a task to see any linked pull requests as they will not appear as links in
the issue, only in the task. To return to an issue from a task, choose the
link to the issue. 2. Now choose an issue assigned to Amazon Q that is in **In
review**. Review the background and approach it records in the
description of the issue. Review the comments to understand the actions it
performed. Review any tasks created for work related to this issue, including
their progress, any actions you might need to take, and any comments. In
**Pull requests**, choose the link to the pull request next
to the **Open** label to review the code.

###### Tip

Pull requests generated for tasks only appear as linked pull requests in
the task view. They don't appear as linked pull requests for the
issue. 3. In the pull request, review the code changes. For more information, see [Reviewing a pull request](pull-requests-review.md "pull-requests-review.md"). Leave
comments on the pull request if you want Amazon Q to change any of its
suggested code. Be specific when leaving comments for Amazon Q for best
results.

For example, when reviewing the pull request created for `Create
 another mysfit named Quokkapus`, you might notice that there's a
typo in the description. You could leave a comment for Amazon Q that states
"Change the description to fix the typo "needsa" by adding a space between
"needs" and "a"." Alternatively, you could leave a comment that tells Amazon Q
to update the description and provide the entire revised description for it to
incorporate.

If you uploaded images for the new mysfit to the website, you can leave a
comment for Amazon Q to update the mysfit with pointers to the image and
thumbnail to use for the new mysfit.

###### Note

Amazon Q will not respond to individual comments. Amazon Q will only
incorporate feedback left in comments in pull requests if you chose the
default option of stopping after every step for approval when you created
the issue. 4. (Optional) After you and other project users have left all the comments you want for changes
to the code, choose **Create revision** to have Amazon Q
create a revision of the pull request that incorporates the changes you
requested in comments. Progress on the revision creation progress will be
reported by Amazon Q in **Overview**, not in
**Changes**. Make sure to refresh your browser to view the
latest updates from Amazon Q on creating the revision.

###### Note

Only the user who created the issue can create a revision of the pull
request. You can only request one revision of a pull request. Make sure that
you have addressed all problems with comments, and that you are satisfied
with the content of the comments, before you choose **Create
revision**. 5. A workflow is run for each pull request in this example project. Make sure
that you see a successful workflow run before you merge the pull request. You
can also choose to create additional workflows and environments to test the code
before you merge it. For more information, see [Getting started with workflows](workflows-getting-started.md "workflows-getting-started.md"). 6. When you are satisfied with the latest revision of the pull request, choose **Merge**.

## Create an issue and

have tasks recommended for it by Amazon Q

An issue can sometimes contain complex or lengthy amounts of work. CodeCatalyst includes integration with Amazon Q Developer Agent for software development.
You can ask **Amazon Q** to analyze an issue
based on its title and its description, and recommend a logical break down of the work into separate tasks.
It will attempt to create a list of recommended tasks that can then review, modify, and choose whether to create.
This can help you and your team to assign individual parts of the work to users in more managable ways that can be
achieved more quickly.

###### To create and review a list of recommended tasks for an issue

1. In the navigation pane, choose **Issues** and make sure you
   are in the **Board** view.
2. Choose **Create issue**.
3. Give the issue a title that explains what you want to do in plain language. For example, for
   this issue, enter a title of `Change the get_all_mysfits() API to return 
mysfits sorted by the Good/Evil attribute`. In **Description**, provide the
   following details:

```
Update the API to allow sorting of mysfits by whether they are Good, Neutral, or Evil. Add a button on the website that allows users to quickly choose this sort and to exclude alignments that they don't want to see.
```

4. Review the description and make sure it contains all the details that might be
   needed before you proceed to the next step.
5. In **Assignees**, choose to assign the issue to yourself.
6. Choose **Create issue**. Your view changes to the Issues board.
7. Choose the issue you just created to open it. Choose **Recommend tasks**.
8. Choose the source repository that contains the code
   for the issuse. Choose **Start recomending tasks**.

The dialog will close and Amazon Q will begin analyzing the issue for complexity. If the issue is complex, it will suggest a break down of the work
into separate, sequential tasks. When the list is ready, choose **View
recommended tasks**. You can add additional tasks, modify the recommended tasks, and reorder the tasks. If you agree with the recommendations,
choosing **Create tasks** will create the tasks. You can then assign those tasks to users to work on them, or even to Amazon Q itself.

## Clean up resources

Once you've completed this tutorial, consider taking the following actions to clean up any resources you created during this tutorial
that you no longer need.

- Unassign Amazon Q from any issues no longer being worked on. If Amazon Q has finished its
  work on an issue or could not find a solution, make sure to unassign Amazon Q
  to avoid reaching the maximum quota for generative AI features. For more
  information, see [Managing generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md") and
  [Pricing](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").
- Move any issues where work is complete to **Done**.
- If the project is no longer needed, delete the project.
