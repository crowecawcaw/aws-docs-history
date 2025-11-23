# CodeCommit

permissions reference

The following tables list each CodeCommit API operation, the corresponding actions
for which you can grant permissions, and the format of the resource ARN to use for
granting permissions. The CodeCommit APIs are grouped into tables based on the scope of the
actions allowed by that API. Refer to it when setting up [Access control](auth-and-access-control.md#access-control "auth-and-access-control.md#access-control") and writing permissions policies that you can
attach to an IAM identity (identity-based policies).

When you create a permissions policy, you specify the actions in the policy's
`Action` field. You specify the resource value in the policy's
`Resource` field as an ARN, with or without a wildcard character (\*).

To express conditions in your CodeCommit policies, use AWS-wide condition keys.
For a complete list of AWS-wide keys, see [Available
Keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the
_IAM User Guide_.
For complete information about actions, resources, and condition keys for CodeCommit in IAM
policies, see [Actions,
resources, and condition keys for AWS CodeCommit](../../../service-authorization/latest/reference/list_awscodecommit.md "../../../service-authorization/latest/reference/list_awscodecommit.md").

###### Note

To specify an action, use the `codecommit:` prefix followed by the API
operation name (for example, `codecommit:GetRepository` or
`codecommit:CreateRepository`.

**Using Wildcards**

To specify multiple actions or resources, use a wildcard character (\*) in your ARN.
For example, `codecommit:*` specifies all CodeCommit actions and
`codecommit:Get*` specifies all CodeCommit actions that begin with the word
`Get`. The following example grants access to all repositories with names
that begin with `MyDemo`.

```
arn:aws:codecommit:us-west-2:111111111111:MyDemo*
```

You can use wildcards only with the `repository-name`
resources listed in the following table. You can't use wildcards with
`region` or `account-id`
resources. For more information about wildcards, see [IAM Identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md "../../../IAM/latest/UserGuide/reference_identifiers.md") in
_IAM User Guide_.

###### Topics

- [Required permissions for Git client commands](#aa-git "#aa-git")
- [Permissions for actions on branches](#aa-branches "#aa-branches")
- [Permissions for actions on merges](#aa-merges "#aa-merges")
- [Permissions for actions on pull requests](#aa-pr "#aa-pr")
- [Permissions for actions on approval rule templates](#aa-art "#aa-art")
- [Permissions for actions on individual files](#aa-files "#aa-files")
- [Permissions for actions on comments](#aa-comments "#aa-comments")
- [Permissions for actions on committed code](#aa-code "#aa-code")
- [Permissions for actions on repositories](#aa-repositories "#aa-repositories")
- [Permissions for actions on tags](#aa-tags "#aa-tags")
- [Permissions for actions on triggers](#aa-triggers "#aa-triggers")
- [Permissions for actions on CodePipeline integration](#aa-acp "#aa-acp")

## Required permissions for Git client commands

In CodeCommit, the `GitPull` IAM policy permissions apply to any Git
client command where data is retrieved from CodeCommit, including **git
fetch**, **git clone**, and so on. Similarly, the
`GitPush` IAM policy permissions apply to any Git client command
where data is sent to CodeCommit. For example, if the `GitPush` IAM policy
permission is set to `Allow`, a user can push the deletion of a branch
using the Git protocol. That push is unaffected by any permissions applied to the
`DeleteBranch` operation for that IAM user. The
`DeleteBranch` permission applies to actions performed with the
console, the AWS CLI, the SDKs, and the API, but not the Git protocol.

`GitPull` and `GitPush` are IAM policy permissions. They
are not API actions.

Use the scroll bars to see the rest of the table.

CodeCommit Required
Permissions for Actions for Git Client Commands| CodeCommit Permissions for Git | Required Permissions | Resources |
| --- | --- | --- |
| GitPull | `codecommit:GitPull`<br>Required to pull information from a CodeCommit repository to a<br>local repo. This is an IAM policy permission only, not an API<br>action. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GitPush | `codecommit:GitPush`<br>Required to push information from a local repo to a CodeCommit<br>repository. This is an IAM policy permission only, not an API<br>action.<br>NoteIf you create a policy that includes a context key and a<br>`Deny` statement that includes this<br>permission, you must also include a `Null`<br>context. For more information, see [Limit pushes and merges to branches in AWS CodeCommit](how-to-conditional-branch.md "how-to-conditional-branch.md"). | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on branches

The following permissions allow or deny actions on branches in CodeCommit repositories.
These permissions pertain only to actions performed in the CodeCommit console and with
the CodeCommit API, and to commands performed using the AWS CLI. They do not pertain to
similar actions that can be performed using the Git protocol. For example, the
**git show-branch -r** command displays a list of
remote branches for a repository and its commits using the Git protocol. It's not
affected by any permissions for the CodeCommit `ListBranches` operation.

For more information about policies for branches, see [Limit pushes and merges to branches in AWS CodeCommit](how-to-conditional-branch.md "how-to-conditional-branch.md") and [Customer managed policy examples](customer-managed-policies.md "customer-managed-policies.md").

Use the scroll bars to see the rest of the table.

CodeCommit API
Operations and Required Permissions for Actions on Branches| CodeCommit API Operations for Branches | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [CreateBranch](../APIReference/API_CreateBranch.md "../APIReference/API_CreateBranch.md") | `codecommit:CreateBranch`<br>Required to create a branch in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [DeleteBranch](../APIReference/API_DeleteBranch.md "../APIReference/API_DeleteBranch.md") | `codecommit:DeleteBranch`<br>Required to delete a branch from a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetBranch](../APIReference/API_GetBranch.md "../APIReference/API_GetBranch.md") | `codecommit:GetBranch`<br>Required to get details about a branch in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [ListBranches](../APIReference/API_ListBranches.md "../APIReference/API_ListBranches.md") | `codecommit:ListBranches`<br>Required to get a list of branches in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [MergeBranchesByFastForward](../APIReference/API_MergeBranchesByFastForward.md "../APIReference/API_MergeBranchesByFastForward.md") | `codecommit:MergeBranchesByFastForward`<br>Required to merge two branches using the fast-forward merge<br>strategy in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [MergeBranchesBySquash](../APIReference/API_MergeBranchesBySquash.md "../APIReference/API_MergeBranchesBySquash.md") | `codecommit:MergeBranchesBySquash`<br>Required to merge two branches using the squash merge strategy<br>in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [MergeBranchesByThreeWay](../APIReference/API_MergeBranchesByThreeWay.md "../APIReference/API_MergeBranchesByThreeWay.md") | `codecommit:MergeBranchesByThreeWay`<br>Required to merge two branches using the three-way merge<br>strategy in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdateDefaultBranch](../APIReference/API_UpdateDefaultBranch.md "../APIReference/API_UpdateDefaultBranch.md") | `codecommit:UpdateDefaultBranch`Required to<br>change the default branch in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on merges

The following permissions allow or deny actions on merges in CodeCommit repositories.
These permissions pertain to actions performed with the CodeCommit console and the CodeCommit
API, and commands performed using the AWS CLI. They do not pertain to similar
actions that can be performed using the Git protocol. For related permissions on
branches, see [Permissions for actions on branches](#aa-branches "#aa-branches"). For related
permissions on pull requests, see [Permissions for actions on pull requests](#aa-pr "#aa-pr").

Use the scroll bars to see the rest of the table.

CodeCommit Required
Permissions for Actions for Merge Commands| CodeCommit Permissions for Merges | Required Permissions | Resources |
| --- | --- | --- |
| [BatchDescribeMergeConflicts](../APIReference/API_BatchDescribeMergeConflicts.md "../APIReference/API_BatchDescribeMergeConflicts.md") | `codecommit:BatchDescribeMergeConflicts`<br>Required to return information about conflicts in a merge<br>between commits in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [CreateUnreferencedMergeCommit](../APIReference/API_CreateUnreferencedMergeCommit.md "../APIReference/API_CreateUnreferencedMergeCommit.md") | `codecommit:CreateUnreferencedMergeCommit`<br>Required to create an unreferenced commit between two branches<br>or commits in a CodeCommit repository for the purpose of comparing<br>them and identifying any potential conflicts. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [DescribeMergeConflicts](../APIReference/API_DescribeMergeConflicts.md "../APIReference/API_DescribeMergeConflicts.md") | `codecommit:DescribeMergeConflicts`<br>Required to return information about merge conflicts between<br>the base, source, and destination versions of a file in a<br>potential merge in an CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetMergeCommit](../APIReference/API_GetMergeCommit.md "../APIReference/API_GetMergeCommit.md") | `codecommit:GetMergeCommit`<br>Required to return information about the merge between a<br>source and destination commit in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetMergeOptions](../APIReference/API_GetMergeOptions.md "../APIReference/API_GetMergeOptions.md") | `codecommit:GetMergeOptions`<br>Required to return information about the available merge<br>options between two branches or commit specifiers in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on pull requests

The following permissions allow or deny actions on pull requests in CodeCommit
repositories. These permissions pertain to actions performed with the CodeCommit console
and the CodeCommit API, and commands performed using the AWS CLI. They do not pertain to
similar actions that can be performed using the Git protocol. For related
permissions on comments, see [Permissions for actions on comments](#aa-comments "#aa-comments").

Use the scroll bars to see the rest of the table.

CodeCommit API Operations
and Required Permissions for Actions on Pull Requests| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| BatchGetPullRequests | `codecommit:BatchGetPullRequests`<br>Required to return information about one or more pull requests<br>in a CodeCommit repository. This is an IAM policy permission only,<br>not an API action that you can call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [CreatePullRequest](../APIReference/API_CreatePullRequest.md "../APIReference/API_CreatePullRequest.md") | `codecommit:CreatePullRequest`<br>Required to create a pull request in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [CreatePullRequestApprovalRule](../APIReference/API_CreatePullRequestApprovalRule.md "../APIReference/API_CreatePullRequestApprovalRule.md") | `codecommit:CreatePullRequestApprovalRule`<br>Required to create an approval rule for a pull request in a<br>CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [DeletePullRequestApprovalRule](../APIReference/API_DeletePullRequestApprovalRule.md "../APIReference/API_DeletePullRequestApprovalRule.md") | `codecommit:DeletePullRequestApprovalRule`<br>Required to delete an approval rule for a pull request in a<br>CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [DescribePullRequestEvents](../APIReference/API_DescribePullRequestEvents.md "../APIReference/API_DescribePullRequestEvents.md") | Required to return information about one or more pull request<br>events in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [EvaluatePullRequestApprovalRules](../APIReference/API_EvaluatePullRequestApprovalRules.md "../APIReference/API_EvaluatePullRequestApprovalRules.md") | `codecommit:EvaluatePullRequestApprovalRules`<br>Required to evaluate whether a pull request has met all the<br>conditions specified in its associated approval rules in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetCommentsForPullRequest](../APIReference/API_GetCommentsForPullRequest.md "../APIReference/API_GetCommentsForPullRequest.md") | `codecommit:GetCommentsForPullRequest`<br>Required to return comments made on a pull request. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GetCommitsFromMergeBase | `codecommit:GetCommitsFromMergeBase`<br>Required to return information about the difference between<br>commits in the context of a potential merge. This is an IAM<br>policy permission only, not an API action that you can<br>call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetMergeConflicts](../APIReference/API_GetMergeConflicts.md "../APIReference/API_GetMergeConflicts.md") | `codecommit:GetMergeConflicts`<br>Required to return information about merge conflicts between<br>the source and destination branch in a pull request. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetPullRequest](../APIReference/API_GetPullRequest.md "../APIReference/API_GetPullRequest.md") | `codecommit:GetPullRequest`<br>Required to return information about a pull request. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetPullRequestApprovalStates](../APIReference/API_GetPullRequestApprovalStates.md "../APIReference/API_GetPullRequestApprovalStates.md") | `codecommit:GetPullRequestApprovalStates`<br>Required to return information about the approval states for a<br>specified pull request. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetPullRequestOverrideState](../APIReference/API_GetPullRequestOverrideState.md "../APIReference/API_GetPullRequestOverrideState.md") | `codecommit:GetPullRequestOverrideState`<br>Required to return information about whether approval rules<br>have been set aside (overridden) for a pull request, and if so,<br>the Amazon Resource Name (ARN) of the user or identity that<br>overrode the rules and their requirements for the pull<br>request. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [ListPullRequests](../APIReference/API_ListPullRequests.md "../APIReference/API_ListPullRequests.md") | `codecommit:ListPullRequests`<br>Required to return information about the pull requests for a<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [MergePullRequestByFastForward](../APIReference/API_MergePullRequestByFastForward.md "../APIReference/API_MergePullRequestByFastForward.md") | `codecommit:MergePullRequestByFastForward`Required<br>to close a pull request and attempt to merge the source branch<br>into the destination branch of a pull request using the<br>fast-forward merge strategy. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [MergePullRequestBySquash](../APIReference/API_MergePullRequestBySquash.md "../APIReference/API_MergePullRequestBySquash.md") | `codecommit:MergePullRequestBySquash`Required to<br>close a pull request and attempt to merge the source branch into<br>the destination branch of a pull request using the squash merge<br>strategy. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [MergePullRequestByThreeWay](../APIReference/API_MergePullRequestByThreeWay.md "../APIReference/API_MergePullRequestByThreeWay.md") | `codecommit:MergePullRequestByThreeWay`Required<br>to close a pull request and attempt to merge the source branch<br>into the destination branch of a pull request using the<br>three-way merge strategy. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [OverridePullRequestApprovalRules](../APIReference/API_OverridePullRequestApprovalRules.md "../APIReference/API_OverridePullRequestApprovalRules.md") | `codecommit:OverridePullRequestApprovalRules`<br>Required to set aside all approval rule requirements for a<br>pull request in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [PostCommentForPullRequest](../APIReference/API_PostCommentForPullRequest.md "../APIReference/API_PostCommentForPullRequest.md") | `codecommit:PostCommentForPullRequest`<br>Required to post a comment on a pull request in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdatePullRequestApprovalRuleContent](../APIReference/API_UpdatePullRequestApprovalRuleContent.md "../APIReference/API_UpdatePullRequestApprovalRuleContent.md") | `codecommit:UpdatePullRequestApprovalRuleContent`<br>Required to change the structure of an approval rule for a<br>pull request in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdatePullRequestApprovalState](../APIReference/API_UpdatePullRequestApprovalState.md "../APIReference/API_UpdatePullRequestApprovalState.md") | `codecommit:UpdatePullRequestApprovalState`<br>Required to change the state of an approval on a pull request<br>in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdatePullRequestDescription](../APIReference/API_UpdatePullRequestDescription.md "../APIReference/API_UpdatePullRequestDescription.md") | `codecommit:UpdatePullRequestDescription`<br>Required to change the description of a pull request in a<br>CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdatePullRequestStatus](../APIReference/API_UpdatePullRequestStatus.md "../APIReference/API_UpdatePullRequestStatus.md") | `codecommit:UpdatePullRequestStatus`<br>Required to change the status of a pull request in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdatePullRequestTitle](../APIReference/API_UpdatePullRequestTitle.md "../APIReference/API_UpdatePullRequestTitle.md") | `codecommit:UpdatePullRequestTitle`<br>Required to change the title of a pull request in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on approval rule templates

The following permissions allow or deny actions on approval rule templates in
CodeCommit repositories. These permissions pertain only to actions performed in the CodeCommit
console, the CodeCommit API, and to commands performed using the AWS CLI. They do not
pertain to similar actions that can be performed using the Git protocol. For related
permissions on pull requests, see [Permissions for actions on pull requests](#aa-pr "#aa-pr").

Use the scroll bars to see the rest of the table.

CodeCommit API Operations
and Required Permissions for Actions on Approval Rule Templates| CodeCommit API Operations for Approval Rule Templates | Required Permissions | Resources |
| --- | --- | --- |
| [AssociateApprovalRuleTemplateWithRepository](../APIReference/API_AssociateApprovalRuleTemplateWithRepository.md "../APIReference/API_AssociateApprovalRuleTemplateWithRepository.md") | `codecommit:AssociateApprovalRuleTemplateWithRepository`<br>Required to associate a template with a specified repository<br>in an Amazon Web Services account. Once associated, this automatically creates<br>approval rules that match the template conditions on every pull<br>request created in the specified repository. | \* |
| [BatchAssociateApprovalRuleTemplateWithRepositories](../APIReference/API_BatchAssociateApprovalRuleTemplateWithRepositories.md "../APIReference/API_BatchAssociateApprovalRuleTemplateWithRepositories.md") | `codecommit:BatchAssociateApprovalRuleTemplateWithRepositories`<br>Required to associate a template with one or more specified<br>repositories in an Amazon Web Services account. | \* |
| [BatchDisassociateApprovalRuleTemplateFromRepositories](../APIReference/API_BatchDisassociateApprovalRuleTemplateFromRepositories.md "../APIReference/API_BatchDisassociateApprovalRuleTemplateFromRepositories.md") | `codecommit:BatchDisassociateApprovalRuleTemplateFromRepositories`<br>Required to disassociate a template from one or more specified<br>repositories in an Amazon Web Services account. | \* |
| [CreateApprovalRuleTemplate](../APIReference/API_CreateApprovalRuleTemplate.md "../APIReference/API_CreateApprovalRuleTemplate.md") | `codecommit:CreateApprovalRuleTemplate`<br>Required to create a template for approval rules that can then<br>be associated with one or more repositories in your AWS<br>account. | \* |
| [DeleteApprovalRuleTemplate](../APIReference/API_DeleteApprovalRuleTemplate.md "../APIReference/API_DeleteApprovalRuleTemplate.md") | `codecommit:DeleteApprovalRuleTemplate`<br>Required to delete the specified template in an Amazon Web Services account.<br>It does not remove approval rules on pull requests already<br>created with the template. | \* |
| [DisassociateApprovalRuleTemplateFromRepository](../APIReference/API_DisassociateApprovalRuleTemplateFromRepository.md "../APIReference/API_DisassociateApprovalRuleTemplateFromRepository.md") | `codecommit:DisassociateApprovalRuleTemplateFromRepository`<br>Required to disassociate the specified template from a<br>repository in an Amazon Web Services account. It does not remove approval<br>rules on pull requests already created with the template. | \* |
| [GetApprovalRuleTemplate](../APIReference/API_GetApprovalRuleTemplate.md "../APIReference/API_GetApprovalRuleTemplate.md") | `codecommit:GetApprovalRuleTemplate`<br>Required to return information about an approval rule template<br>in an Amazon Web Services account. | \* |
| [ListApprovalRuleTemplates](../APIReference/API_ListApprovalRuleTemplates.md "../APIReference/API_ListApprovalRuleTemplates.md") | `codecommit:ListApprovalRuleTemplates`<br>Required to list approval rule templates in an Amazon Web Services account. | \* |
| [ListAssociatedApprovalRuleTemplatesForRepository](../APIReference/API_ListAssociatedApprovalRuleTemplatesForRepository.md "../APIReference/API_ListAssociatedApprovalRuleTemplatesForRepository.md") | `codecommit:ListAssociatedApprovalRuleTemplatesForRepository`<br>Required to list all approval rule templates that are<br>associated with a specified repository in an Amazon Web Services account. | \* |
| [ListRepositoriesForApprovalRuleTemplate](../APIReference/API_ListRepositoriesForApprovalRuleTemplate.md "../APIReference/API_ListRepositoriesForApprovalRuleTemplate.md") | `codecommit:ListRepositoriesForApprovalRuleTemplate`<br>Required to list all repositories that are associated with a<br>specified approval rule template in an Amazon Web Services account. | \* |
| [UpdateApprovalRuleTemplateContent](../APIReference/API_UpdateApprovalRuleTemplateContent.md "../APIReference/API_UpdateApprovalRuleTemplateContent.md") | `codecommit:UpdateApprovalRuleTemplateContent`<br>Required to update the content of an approval rule template in<br>an Amazon Web Services account. | \* |
| [UpdateApprovalRuleTemplateDescription](../APIReference/API_UpdateApprovalRuleTemplateDescription.md "../APIReference/API_UpdateApprovalRuleTemplateDescription.md") | `codecommit:UpdateApprovalRuleTemplateDescription`<br>Required to update the description of an approval rule<br>template in an Amazon Web Services account. | \* |
| [UpdateApprovalRuleTemplateName](../APIReference/API_UpdateApprovalRuleTemplateName.md "../APIReference/API_UpdateApprovalRuleTemplateName.md") | `codecommit:UpdateApprovalRuleTemplateName`<br>Required to update the name of an approval rule template in an<br>Amazon Web Services account. | \* |

## Permissions for actions on individual files

The following permissions allow or deny actions on individual files in CodeCommit
repositories. These permissions pertain only to actions performed in the CodeCommit
console, the CodeCommit API, and to commands performed using the AWS CLI. They do not
pertain to similar actions that can be performed using the Git protocol. For
example, the `git push` command pushes new and changed files to a CodeCommit
repository by using the Git protocol. It's not affected by any permissions for the
CodeCommit `PutFile` operation.

Use the scroll bars to see the rest of the table.

CodeCommit API Operations
and Required Permissions for Actions on Individual Files| CodeCommit API Operations for Individual Files | Required Permissions | Resources |
| --- | --- | --- |
| [DeleteFile](../APIReference/API_DeleteFile.md "../APIReference/API_DeleteFile.md") | `codecommit:DeleteFile`<br>Required to delete a specified file from a specified branch in<br>a CodeCommit repository from the CodeCommit console. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetBlob](../APIReference/API_GetBlob.md "../APIReference/API_GetBlob.md") | `codecommit:GetBlob`<br>Required to view the encoded content of an individual file in<br>a CodeCommit repository from the CodeCommit console. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetFile](../APIReference/API_GetFile.md "../APIReference/API_GetFile.md") | `codecommit:GetFile`<br>Required to view the encoded content of an individual file and<br>its metadata a CodeCommit repository from the CodeCommit console. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetFolder](../APIReference/API_GetFolder.md "../APIReference/API_GetFolder.md") | `codecommit:GetFolder`<br>Required to view the contents of a specified folder in a CodeCommit<br>repository from the CodeCommit console. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [PutFile](../APIReference/API_PutFile.md "../APIReference/API_PutFile.md") | `codecommit:PutFile`<br>Required to add a new or modified file to a CodeCommit repository<br>from the CodeCommit console, CodeCommit API, or the AWS CLI. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on comments

The following permissions allow or deny actions on comments in CodeCommit repositories.
These permissions pertain to actions performed with the CodeCommit console and the CodeCommit
API, and to commands performed using the AWS CLI. For related permissions on
comments in pull requests, see [Permissions for actions on pull requests](#aa-pr "#aa-pr").

Use the scroll bars to see the rest of the table.

CodeCommit API
Operations and Required Permissions for Comments in Repositories| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [DeleteCommentContent](../APIReference/API_DeleteCommentContent.md "../APIReference/API_DeleteCommentContent.md") | `codecommit:DeleteCommentContent`<br>Required to delete the content of a comment made on a change,<br>file, or commit in a repository. Comments cannot be deleted, but<br>the content of a comment can be removed if the user has this<br>permission. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetComment](../APIReference/API_GetComment.md "../APIReference/API_GetComment.md") | `codecommit:GetComment`<br>Required to return information about a comment made on a<br>change, file, or commit in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetCommentReactions](../APIReference/API_GetCommentReactions.md "../APIReference/API_GetCommentReactions.md") | `codecommit:GetCommentReactions`<br>Required to return information about emoji reactions to a<br>comment made on a change, file, or commit in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetCommentsForComparedCommit](../APIReference/API_GetCommentsForComparedCommit.md "../APIReference/API_GetCommentsForComparedCommit.md") | `codecommit:GetCommentsForComparedCommit`<br>Required to return information about comments made on the<br>comparison between two commits in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [PostCommentForComparedCommit](../APIReference/API_PostCommentForComparedCommit.md "../APIReference/API_PostCommentForComparedCommit.md") | `codecommit:PostCommentForComparedCommit`<br>Required to create a comment on the comparison between two<br>commits in a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [PostCommentReply](../APIReference/API_PostCommentReply.md "../APIReference/API_PostCommentReply.md") | `codecommit:PostCommentReply`<br>Required to create a reply to a comment on a comparison<br>between commits or on a pull request. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [PutCommentReaction](../APIReference/API_PutCommentReaction.md "../APIReference/API_PutCommentReaction.md") | `codecommit:PutCommentReaction`<br>Required to create or update an emoji reaction to a<br>comment. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdateComment](../APIReference/API_UpdateComment.md "../APIReference/API_UpdateComment.md") | `codecommit:UpdateComment`<br>Required to edit a comment on a comparison between commits or<br>on a pull request. Comments can only be edited by the comment<br>author. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on committed code

The following permissions allow or deny actions on code committed to CodeCommit
repositories. These permissions pertain to actions performed with the CodeCommit console
and the CodeCommit API, and commands performed using the AWS CLI. They do not pertain to
similar actions that can be performed using the Git protocol. For example, the
**git commit** command creates a commit for a
branch in a repository using the Git protocol. It's not affected by any permissions
for the CodeCommit `CreateCommit` operation.

Explicitly denying some of these permissions might result in unexpected
consequences in the CodeCommit console. For example, setting `GetTree` to
`Deny` prevents users from navigating the contents of a repository in
the console, but does not block users from viewing the contents of a file in the
repository (if they are sent a link to the file in email, for example). Setting
`GetBlob` to `Deny` prevents users from viewing the
contents of files, but does not block users from browsing the structure of a
repository. Setting `GetCommit` to `Deny` prevents users from
retrieving details about commits. Setting `GetObjectIdentifier` to
`Deny` blocks most of the functionality of code browsing. If you set
all three of these actions to `Deny` in a policy, a user with that policy
cannot browse code in the CodeCommit console.

Use the scroll bars to see the rest of the table.

CodeCommit API
Operations and Required Permissions for Actions on Committed Code| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| BatchGetCommits | `codecommit:BatchGetCommits`<br>Required to return information about one or more commits in a<br>CodeCommit repository. This is an IAM policy permission only, not<br>an API action that you can call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [CreateCommit](../APIReference/CreateCommit.md "../APIReference/CreateCommit.md") | `codecommit:CreateCommit`<br>Required to create a commit. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetCommit](../APIReference/GetCommit.md "../APIReference/GetCommit.md") | `codecommit:GetCommit`<br>Required to return information about a commit. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GetCommitHistory | `codecommit:GetCommitHistory`<br>Required to return information about the history of commits in<br>a repository. This is an IAM policy permission only, not an<br>API action that you can call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetDifferences](../APIReference/API_GetDifferences.md "../APIReference/API_GetDifferences.md") | `codecommit:GetDifferences`<br>Required to return information about the differences between<br>commit specifiers (such as a branch, tag, HEAD, commit ID, or<br>other fully qualified reference). | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GetObjectIdentifier | `codecommit:GetObjectIdentifier`Required to<br>resolve blobs, trees, and commits to their identifier. This is<br>an IAM policy permission only, not an API action that you can<br>call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GetReferences | `codecommit:GetReferences`Required to return all<br>references, such as branches and tags. This is an IAM policy<br>permission only, not an API action that you can<br>call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GetTree | `codecommit:GetTree`Required to view the<br>contents of a specified tree in a CodeCommit repository from the<br>CodeCommit console. This is an IAM policy permission only, not an<br>API action that you can call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on repositories

The following permissions allow or deny actions on CodeCommit repositories. These
permissions pertain to actions performed with the CodeCommit console and the CodeCommit API,
and to commands performed using the AWS CLI. They do not pertain to similar actions
that can be performed using the Git protocol.

Use the scroll bars to see the rest of the table.

CodeCommit API
Operations and Required Permissions for Actions on Repositories| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [BatchGetRepositories](../APIReference/API_BatchGetRepositories.md "../APIReference/API_BatchGetRepositories.md") | `codecommit:BatchGetRepositories`<br>Required to get information about multiple CodeCommit repositories<br>in an Amazon Web Services account. In `Resource`, you must specify<br>the names of all of the CodeCommit repositories for which a user is<br>allowed (or denied) information. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [CreateRepository](../APIReference/CreateRepository.md "../APIReference/CreateRepository.md") | `codecommit:CreateRepository`<br>Required to create a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [DeleteRepository](../APIReference/API_DeleteRepository.md "../APIReference/API_DeleteRepository.md") | `codecommit:DeleteRepository`<br>Required to delete a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetRepository](../APIReference/API_GetRepository.md "../APIReference/API_GetRepository.md") | `codecommit:GetRepository`<br>Required to get information about a single CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [ListRepositories](../APIReference/API_ListRepositories.md "../APIReference/API_ListRepositories.md") | `codecommit:ListRepositories`Required to get a<br>list of the names and system IDs of multiple CodeCommit repositories<br>for an Amazon Web Services account. The only allowed value for<br>`Resource` for this action is all repositories<br>(`*`). | \* |
| [UpdateRepositoryDescription](../APIReference/API_UpdateRepositoryDescription.md "../APIReference/API_UpdateRepositoryDescription.md") | `codecommit:UpdateRepositoryDescription`Required<br>to change the description of a CodeCommit repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UpdateRepositoryName](../APIReference/API_UpdateRepositoryName.md "../APIReference/API_UpdateRepositoryName.md") | `codecommit:UpdateRepositoryName`Required to<br>change the name of a CodeCommit repository. In `Resource`,<br>you must specify both the CodeCommit repositories that are allowed to<br>be changed and the new repository names. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on tags

The following permissions allow or deny actions on AWS tags for CodeCommit resources.

Use the scroll bars to see the rest of the table.

CodeCommit API Operations
and Required Permissions for Actions on Tags| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") | `codecommit:ListTagsForResource`<br>Required to return information about AWS tags configured on<br>a resource in CodeCommit. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") | `codecommit:TagResource`<br>Required to add or edit AWS tags for a resource in<br>CodeCommit. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") | `codecommit:UntagResource`<br>Required to remove AWS tags from a resource in CodeCommit. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on triggers

The following permissions allow or deny actions on triggers for CodeCommit
repositories.

Use the scroll bars to see the rest of the table.

CodeCommit API
Operations and Required Permissions for Actions on Triggers| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [GetRepositoryTriggers](../APIReference/API_GetRepositoryTriggers.md "../APIReference/API_GetRepositoryTriggers.md") | `codecommit:GetRepositoryTriggers`<br>Required to return information about triggers configured for a<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [PutRepositoryTriggers](../APIReference/API_PutRepositoryTriggers.md "../APIReference/API_PutRepositoryTriggers.md") | `codecommit:PutRepositoryTriggers`<br>Required to create, edit, or delete triggers for a<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [TestRepositoryTriggers](../APIReference/API_TestRepositoryTriggers.md "../APIReference/API_TestRepositoryTriggers.md") | `codecommit:TestRepositoryTriggers`<br>Required to test the functionality of a repository trigger by<br>sending data to the topic or function configured for the<br>trigger. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |

## Permissions for actions on CodePipeline integration

In order for CodePipeline to use a CodeCommit repository in a source action for a pipeline,
you must grant all of the permissions listed in the following table to the service
role for CodePipeline. If these permissions are not set in the service role or are set to
`Deny`, the pipeline does not run automatically when a
change is made to the repository, and changes cannot be released manually.

Use the scroll bars to see the rest of the table.

CodeCommit API Operations
and Required Permissions for Actions on CodePipeline Integration| CodeCommit API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [GetBranch](../APIReference/API_GetBranch.md "../APIReference/API_GetBranch.md") | `codecommit:GetBranch`<br>Required to get details about a branch in a CodeCommit<br>repository. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| [GetCommit](../APIReference/GetCommit.md "../APIReference/GetCommit.md") | `codecommit:GetCommit`<br>Required to return information about a commit to the service<br>role for CodePipeline. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| UploadArchive | `codecommit:UploadArchive`<br>Required to allow the service role for CodePipeline to upload<br>repository changes into a pipeline. This is an IAM policy<br>permission only, not an API action that you can call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| GetUploadArchiveStatus | `codecommit:GetUploadArchiveStatus`<br>Required to determine the status of an archive upload: whether<br>it is in progress, complete, cancelled, or if an error occurred.<br>This is an IAM policy permission only, not an API action that<br>you can call. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| CancelUploadArchive | `codecommit:CancelUploadArchive`Required to<br>cancel the uploading of an archive to a pipeline. This is an<br>IAM policy permission only, not an API action that can be<br>called. | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
