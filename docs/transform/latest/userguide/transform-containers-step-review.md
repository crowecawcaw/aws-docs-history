# Step 4: Review Docker artifacts and code changes

In this step, you review the Docker artifacts and code changes that AWS Transform
generated during containerization.

## Reviewing changes from Git repositories

If you provided source code from Git repositories, AWS Transform commits the
containerization changes to a new branch in each repository. If you have multiple
repositories, the agent presents all changes as a batch for consolidated
review.

###### To review and approve changes

1. Review the code diff links that the agent provides. Each diff shows all
   files that were added or modified, including Dockerfiles, configuration
   files, and any source code changes.
2. When the agent presents the approval dialog, approve or reject the
   changes. For multiple repositories, you approve all changes in a single
   batch operation.
3. If you approve, the agent pushes the changes to the new branches in your
   repositories.
4. Confirm that you are ready to proceed to the next step.

## Reviewing changes from zip uploads

If you uploaded source code as zip files, the agent provides download links for
the containerized artifacts. Download and review the artifacts, which include the
generated Dockerfiles and any source code modifications.

## Requesting changes

If the generated artifacts need modifications, you can provide feedback to the
agent. The agent restarts the containerization step with your updated instructions
and generates new artifacts for your review.
