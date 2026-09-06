

# Step 4: Review Docker artifacts and code changes
<a name="transform-containers-step-review"></a>

In this step, you review the Docker artifacts and code changes that AWS Transform generated during containerization.

## Reviewing changes from Git repositories
<a name="transform-containers-review-git"></a>

If you provided source code from Git repositories, AWS Transform commits the containerization changes to a new branch in each repository. If you have multiple repositories, AWS Transform presents all changes as a batch for consolidated review.

**To review and approve changes**

1. Review the code diff links that AWS Transform provides. Each diff shows all files that were added or modified, including Dockerfiles, configuration files, and any source code changes.

1. When AWS Transform presents the approval dialog, approve or reject the changes. For multiple repositories, you approve all changes in a single batch operation.

1. If you approve, AWS Transform pushes the changes to the new branches in your repositories.

1. Confirm that you are ready to proceed to the next step.

## Reviewing changes from zip uploads
<a name="transform-containers-review-zip"></a>

If you uploaded source code as zip files, AWS Transform provides download links for the containerized artifacts. Download and review the artifacts, which include the generated Dockerfiles and any source code modifications.

## Requesting changes
<a name="transform-containers-review-request-changes"></a>

If the generated artifacts need modifications, you can provide feedback to the AWS Transform restarts the containerization step with your updated instructions and generates new artifacts for your review.