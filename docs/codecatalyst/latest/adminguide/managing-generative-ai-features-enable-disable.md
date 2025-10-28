Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Enabling or disabling

generative AI features for a space

To allow users to use generative AI features in CodeCatalyst, you must enable them for your
space. You cannot enable these features for specific projects. If you enable them
for the space, all projects in the space will have access to them. For more
information about the available generative AI features, see [Enabling generative AI features in
Amazon CodeCatalyst](managing-generative-ai-features.md "managing-generative-ai-features.md").

**Before you begin**

The generative AI features in CodeCatalyst are useful and powerful tools for users in your
space. Like all powerful tools, they perform best when well understood by users and
administrators. You should be aware of the following considerations before you decide to
enable generative AI features for your space.

- **Generative AI features cannot make arbitrary changes to
  your project**. While Amazon Q can create pull requests with code
  changes, it cannot merge a pull request. A user must approve the pull request
  and merge the changes. However, if you have one or more workflows configured to
  run based on branch events, those workflows will run immediately when the pull
  request is created. Additionally, once code is merged, the changes are part of
  the source repository branch where the pull request was merged. Just like any
  other merged pull request, any workflows configured to build and deploy pushes
  to the destination branch will start a run of the changes changes contained in a
  pull request created by Amazon Q.
- **Generative AI features might not correctly interpret
  user statements and existing code structures**. User intent can be
  misinterpreted by generative AI features, which can result in code generation
  that does not do what the original requestor expected. The approach Amazon Q
  creates is based on the title and description of an issue, as well as its
  analysis of the code in the source repository specified in the issue. If the
  code in the source repository contains errors, Amazon Q might repeat these
  errors if it interprets them as part of the desired structure and patterns in
  the code. As a best practice, encourage users in a space with generative AI
  features enabled to thoroughly review any code in pull requests created by
  Amazon Q to ensure that the code both does what the issue title and
  description suggested, and that the code itself is well-formed and functional.
  Like any other pull request, users can create a Dev Environment and make changes and
  fixes to the code in the branch created by Amazon Q. Similarly review a
  revision created by Amazon Q to help ensure that the changes correctly address
  any issues raised in comments.
- **Workflows created by Amazon Q might deploy code to
  production resources immediately once a pull request is merged**.
  By default, CodeCatalyst does not allow Amazon Q to create or update workflows.
  However, you can choose to have Amazon Q do so, and it will try to create or
  update a workflow according to the information in the issue. If you merge a pull
  request with workflow changes, that workflow will automatically run when its
  conditions are met. Additionally, like any pull request, pull requests created
  by Amazon Q will start a workflow run when the specified conditions are met,
  so if you have a workflow configured to run on branch events, a pull request
  with workflow changes might start a run of those workflows.
  You must have the **Space administrator** role in CodeCatalyst to manage
  generative feature access for a space.

###### Important

Generative AI features are only available in the US West (Oregon) Region.

###### To enable or disable generative AI features for a space

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space. Choose **Settings**, and
   then choose **Generative AI**.

The **Generative AI** page displays. 3. To enable generative AI features for all projects in your space, choose
the **Projects in this space can access generative AI
features** toggle and make sure it is in the on position. Users in
projects will immediately have access to the generative AI features available to
their roles in those projects. 4. To disable generative AI features for all projects in your space, choose
the **Projects in this space can access generative AI
features** toggle and make sure it is in the off position.

###### Warning

Disabling the generative AI features will stop work on all issues and
summaries in all projects. The work cannot be restarted even if you
immediately re-enable the generative AI features.
