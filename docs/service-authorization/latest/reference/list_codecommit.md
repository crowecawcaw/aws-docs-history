

# Actions, resources, and condition keys for AWS CodeCommit
<a name="list_codecommit"></a>

AWS CodeCommit (service prefix: `codecommit`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codecommit/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codecommit/codecommit.json) for this service.

**Topics**
+ [API operations defined by AWS CodeCommit](#list_codecommit-operations)
+ [Actions defined by AWS CodeCommit](#list_codecommit-actions-as-permissions)
+ [Permission-only actions for AWS CodeCommit](#list_codecommit-permission-only-actions)
+ [Resource types defined by AWS CodeCommit](#list_codecommit-resources-for-iam-policies)
+ [Condition keys for AWS CodeCommit](#list_codecommit-policy-keys)

## API operations defined by AWS CodeCommit
<a name="list_codecommit-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codecommit-actions-as-permissions).




- **   AssociateApprovalRuleTemplateWithRepository  **
  - **IAM action:**  [codecommit:AssociateApprovalRuleTemplateWithRepository](#list_codecommit-action-AssociateApprovalRuleTemplateWithRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateApprovalRuleTemplateWithRepositories  **
  - **IAM action:**  [codecommit:BatchAssociateApprovalRuleTemplateWithRepositories](#list_codecommit-action-BatchAssociateApprovalRuleTemplateWithRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDescribeMergeConflicts  **
  - **IAM action:**  [codecommit:BatchDescribeMergeConflicts](#list_codecommit-action-BatchDescribeMergeConflicts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDisassociateApprovalRuleTemplateFromRepositories  **
  - **IAM action:**  [codecommit:BatchDisassociateApprovalRuleTemplateFromRepositories](#list_codecommit-action-BatchDisassociateApprovalRuleTemplateFromRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetCommits  **
  - **IAM action:**  [codecommit:BatchGetCommits](#list_codecommit-action-BatchGetCommits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetRepositories  **
  - **IAM action:**  [codecommit:BatchGetRepositories](#list_codecommit-action-BatchGetRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateApprovalRuleTemplate  **
  - **IAM action:**  [codecommit:CreateApprovalRuleTemplate](#list_codecommit-action-CreateApprovalRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBranch  **
  - **IAM action:**  [codecommit:CreateBranch](#list_codecommit-action-CreateBranch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCommit  **
  - **IAM action:**  [codecommit:CreateCommit](#list_codecommit-action-CreateCommit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePullRequest  **
  - **IAM action:**  [codecommit:CreatePullRequest](#list_codecommit-action-CreatePullRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePullRequestApprovalRule  **
  - **IAM action:**  [codecommit:CreatePullRequestApprovalRule](#list_codecommit-action-CreatePullRequestApprovalRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRepository  **
  - **IAM action:**  [codecommit:CreateRepository](#list_codecommit-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codecommit:TagResource](#list_codecommit-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUnreferencedMergeCommit  **
  - **IAM action:**  [codecommit:CreateUnreferencedMergeCommit](#list_codecommit-action-CreateUnreferencedMergeCommit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApprovalRuleTemplate  **
  - **IAM action:**  [codecommit:DeleteApprovalRuleTemplate](#list_codecommit-action-DeleteApprovalRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBranch  **
  - **IAM action:**  [codecommit:DeleteBranch](#list_codecommit-action-DeleteBranch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCommentContent  **
  - **IAM action:**  [codecommit:DeleteCommentContent](#list_codecommit-action-DeleteCommentContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFile  **
  - **IAM action:**  [codecommit:DeleteFile](#list_codecommit-action-DeleteFile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePullRequestApprovalRule  **
  - **IAM action:**  [codecommit:DeletePullRequestApprovalRule](#list_codecommit-action-DeletePullRequestApprovalRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRepository  **
  - **IAM action:**  [codecommit:DeleteRepository](#list_codecommit-action-DeleteRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeMergeConflicts  **
  - **IAM action:**  [codecommit:DescribeMergeConflicts](#list_codecommit-action-DescribeMergeConflicts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePullRequestEvents  **
  - **IAM action:**  [codecommit:DescribePullRequestEvents](#list_codecommit-action-DescribePullRequestEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateApprovalRuleTemplateFromRepository  **
  - **IAM action:**  [codecommit:DisassociateApprovalRuleTemplateFromRepository](#list_codecommit-action-DisassociateApprovalRuleTemplateFromRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EvaluatePullRequestApprovalRules  **
  - **IAM action:**  [codecommit:EvaluatePullRequestApprovalRules](#list_codecommit-action-EvaluatePullRequestApprovalRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApprovalRuleTemplate  **
  - **IAM action:**  [codecommit:GetApprovalRuleTemplate](#list_codecommit-action-GetApprovalRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlob  **
  - **IAM action:**  [codecommit:GetBlob](#list_codecommit-action-GetBlob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlobDifferences  **
  - **IAM action:**  [codecommit:GetBlobDifferences](#list_codecommit-action-GetBlobDifferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBranch  **
  - **IAM action:**  [codecommit:GetBranch](#list_codecommit-action-GetBranch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComment  **
  - **IAM action:**  [codecommit:GetComment](#list_codecommit-action-GetComment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommentReactions  **
  - **IAM action:**  [codecommit:GetCommentReactions](#list_codecommit-action-GetCommentReactions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommentsForComparedCommit  **
  - **IAM action:**  [codecommit:GetCommentsForComparedCommit](#list_codecommit-action-GetCommentsForComparedCommit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommentsForPullRequest  **
  - **IAM action:**  [codecommit:GetCommentsForPullRequest](#list_codecommit-action-GetCommentsForPullRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommit  **
  - **IAM action:**  [codecommit:GetCommit](#list_codecommit-action-GetCommit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDifferences  **
  - **IAM action:**  [codecommit:GetDifferences](#list_codecommit-action-GetDifferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFile  **
  - **IAM action:**  [codecommit:GetFile](#list_codecommit-action-GetFile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFolder  **
  - **IAM action:**  [codecommit:GetFolder](#list_codecommit-action-GetFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMergeCommit  **
  - **IAM action:**  [codecommit:GetMergeCommit](#list_codecommit-action-GetMergeCommit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMergeConflicts  **
  - **IAM action:**  [codecommit:GetMergeConflicts](#list_codecommit-action-GetMergeConflicts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMergeOptions  **
  - **IAM action:**  [codecommit:GetMergeOptions](#list_codecommit-action-GetMergeOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPullRequest  **
  - **IAM action:**  [codecommit:GetPullRequest](#list_codecommit-action-GetPullRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPullRequestApprovalStates  **
  - **IAM action:**  [codecommit:GetPullRequestApprovalStates](#list_codecommit-action-GetPullRequestApprovalStates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPullRequestOverrideState  **
  - **IAM action:**  [codecommit:GetPullRequestOverrideState](#list_codecommit-action-GetPullRequestOverrideState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepository  **
  - **IAM action:**  [codecommit:GetRepository](#list_codecommit-action-GetRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepositoryTriggers  **
  - **IAM action:**  [codecommit:GetRepositoryTriggers](#list_codecommit-action-GetRepositoryTriggers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApprovalRuleTemplates  **
  - **IAM action:**  [codecommit:ListApprovalRuleTemplates](#list_codecommit-action-ListApprovalRuleTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociatedApprovalRuleTemplatesForRepository  **
  - **IAM action:**  [codecommit:ListAssociatedApprovalRuleTemplatesForRepository](#list_codecommit-action-ListAssociatedApprovalRuleTemplatesForRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBranches  **
  - **IAM action:**  [codecommit:ListBranches](#list_codecommit-action-ListBranches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFileCommitHistory  **
  - **IAM action:**  [codecommit:ListFileCommitHistory](#list_codecommit-action-ListFileCommitHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPullRequests  **
  - **IAM action:**  [codecommit:ListPullRequests](#list_codecommit-action-ListPullRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRepositories  **
  - **IAM action:**  [codecommit:ListRepositories](#list_codecommit-action-ListRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRepositoriesForApprovalRuleTemplate  **
  - **IAM action:**  [codecommit:ListRepositoriesForApprovalRuleTemplate](#list_codecommit-action-ListRepositoriesForApprovalRuleTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codecommit:ListTagsForResource](#list_codecommit-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   MergeBranchesByFastForward  **
  - **IAM action:**  [codecommit:MergeBranchesByFastForward](#list_codecommit-action-MergeBranchesByFastForward) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MergeBranchesBySquash  **
  - **IAM action:**  [codecommit:MergeBranchesBySquash](#list_codecommit-action-MergeBranchesBySquash) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MergeBranchesByThreeWay  **
  - **IAM action:**  [codecommit:MergeBranchesByThreeWay](#list_codecommit-action-MergeBranchesByThreeWay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MergePullRequestByFastForward  **
  - **IAM action:**  [codecommit:MergePullRequestByFastForward](#list_codecommit-action-MergePullRequestByFastForward) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MergePullRequestBySquash  **
  - **IAM action:**  [codecommit:MergePullRequestBySquash](#list_codecommit-action-MergePullRequestBySquash) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MergePullRequestByThreeWay  **
  - **IAM action:**  [codecommit:MergePullRequestByThreeWay](#list_codecommit-action-MergePullRequestByThreeWay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   OverridePullRequestApprovalRules  **
  - **IAM action:**  [codecommit:OverridePullRequestApprovalRules](#list_codecommit-action-OverridePullRequestApprovalRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PostCommentForComparedCommit  **
  - **IAM action:**  [codecommit:PostCommentForComparedCommit](#list_codecommit-action-PostCommentForComparedCommit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PostCommentForPullRequest  **
  - **IAM action:**  [codecommit:PostCommentForPullRequest](#list_codecommit-action-PostCommentForPullRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PostCommentReply  **
  - **IAM action:**  [codecommit:PostCommentReply](#list_codecommit-action-PostCommentReply) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutCommentReaction  **
  - **IAM action:**  [codecommit:PutCommentReaction](#list_codecommit-action-PutCommentReaction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFile  **
  - **IAM action:**  [codecommit:PutFile](#list_codecommit-action-PutFile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRepositoryTriggers  **
  - **IAM action:**  [codecommit:PutRepositoryTriggers](#list_codecommit-action-PutRepositoryTriggers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [codecommit:TagResource](#list_codecommit-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestRepositoryTriggers  **
  - **IAM action:**  [codecommit:TestRepositoryTriggers](#list_codecommit-action-TestRepositoryTriggers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [codecommit:UntagResource](#list_codecommit-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApprovalRuleTemplateContent  **
  - **IAM action:**  [codecommit:UpdateApprovalRuleTemplateContent](#list_codecommit-action-UpdateApprovalRuleTemplateContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApprovalRuleTemplateDescription  **
  - **IAM action:**  [codecommit:UpdateApprovalRuleTemplateDescription](#list_codecommit-action-UpdateApprovalRuleTemplateDescription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApprovalRuleTemplateName  **
  - **IAM action:**  [codecommit:UpdateApprovalRuleTemplateName](#list_codecommit-action-UpdateApprovalRuleTemplateName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateComment  **
  - **IAM action:**  [codecommit:UpdateComment](#list_codecommit-action-UpdateComment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDefaultBranch  **
  - **IAM action:**  [codecommit:UpdateDefaultBranch](#list_codecommit-action-UpdateDefaultBranch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePullRequestApprovalRuleContent  **
  - **IAM action:**  [codecommit:UpdatePullRequestApprovalRuleContent](#list_codecommit-action-UpdatePullRequestApprovalRuleContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePullRequestApprovalState  **
  - **IAM action:**  [codecommit:UpdatePullRequestApprovalState](#list_codecommit-action-UpdatePullRequestApprovalState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePullRequestDescription  **
  - **IAM action:**  [codecommit:UpdatePullRequestDescription](#list_codecommit-action-UpdatePullRequestDescription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePullRequestStatus  **
  - **IAM action:**  [codecommit:UpdatePullRequestStatus](#list_codecommit-action-UpdatePullRequestStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePullRequestTitle  **
  - **IAM action:**  [codecommit:UpdatePullRequestTitle](#list_codecommit-action-UpdatePullRequestTitle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRepositoryDescription  **
  - **IAM action:**  [codecommit:UpdateRepositoryDescription](#list_codecommit-action-UpdateRepositoryDescription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRepositoryEncryptionKey  **
  - **IAM action:**  [codecommit:UpdateRepositoryEncryptionKey](#list_codecommit-action-UpdateRepositoryEncryptionKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRepositoryName  **
  - **IAM action:**  [codecommit:TagResource](#list_codecommit-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codecommit:UpdateRepositoryName](#list_codecommit-action-UpdateRepositoryName)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS CodeCommit
<a name="list_codecommit-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateApprovalRuleTemplateWithRepository](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_AssociateApprovalRuleTemplateWithRepository.html)  **
  - **Description:** Grants permission to associate an approval rule template with a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateApprovalRuleTemplateWithRepositories](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchAssociateApprovalRuleTemplateWithRepositories.html)  **
  - **Description:** Grants permission to associate an approval rule template with multiple repositories in a single operation
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDescribeMergeConflicts](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchDescribeMergeConflicts.html)  **
  - **Description:** Grants permission to get information about multiple merge conflicts when attempting to merge two commits using either the three-way merge or the squash merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchDisassociateApprovalRuleTemplateFromRepositories](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchDisassociateApprovalRuleTemplateFromRepositories.html)  **
  - **Description:** Grants permission to remove the association between an approval rule template and multiple repositories in a single operation
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetCommits](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchGetCommits.html)  **
  - **Description:** Grants permission to return information about one or more commits in an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetRepositories](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchGetRepositories.html)  **
  - **Description:** Grants permission to get information about multiple repositories
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateApprovalRuleTemplate](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateApprovalRuleTemplate.html)  **
  - **Description:** Grants permission to create an approval rule template that will automatically create approval rules in pull requests that match the conditions defined in the template; does not grant permission to create approval rules for individual pull requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateBranch](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateBranch.html)  **
  - **Description:** Grants permission to create a branch in an AWS CodeCommit repository with this API; does not control Git create branch actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [CreateCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateCommit.html)  **
  - **Description:** Grants permission to add, copy, move or update single or multiple files in a branch in an AWS CodeCommit repository, and generate a commit for the changes in the specified branch
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [CreatePullRequest](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreatePullRequest.html)  **
  - **Description:** Grants permission to create a pull request in the specified repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePullRequestApprovalRule](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreatePullRequestApprovalRule.html)  **
  - **Description:** Grants permission to create an approval rule specific to an individual pull request; does not grant permission to create approval rule templates
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateRepository.html)  **
  - **Description:** Grants permission to create an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecommit-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecommit-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUnreferencedMergeCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateUnreferencedMergeCommit.html)  **
  - **Description:** Grants permission to create an unreferenced commit that contains the result of merging two commits using either the three-way or the squash merge option; does not control Git merge actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [DeleteApprovalRuleTemplate](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteApprovalRuleTemplate.html)  **
  - **Description:** Grants permission to delete an approval rule template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBranch](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteBranch.html)  **
  - **Description:** Grants permission to delete a branch in an AWS CodeCommit repository with this API; does not control Git delete branch actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [DeleteCommentContent](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteCommentContent.html)  **
  - **Description:** Grants permission to delete the content of a comment made on a change, file, or commit in a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFile](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteFile.html)  **
  - **Description:** Grants permission to delete a specified file from a specified branch
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [DeletePullRequestApprovalRule](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeletePullRequestApprovalRule.html)  **
  - **Description:** Grants permission to delete approval rule created for a pull request if the rule was not created by an approval rule template
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepository](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteRepository.html)  **
  - **Description:** Grants permission to delete an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeMergeConflicts](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DescribeMergeConflicts.html)  **
  - **Description:** Grants permission to get information about specific merge conflicts when attempting to merge two commits using either the three-way or the squash merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePullRequestEvents](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DescribePullRequestEvents.html)  **
  - **Description:** Grants permission to return information about one or more pull request events
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateApprovalRuleTemplateFromRepository](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DisassociateApprovalRuleTemplateFromRepository.html)  **
  - **Description:** Grants permission to remove the association between an approval rule template and a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EvaluatePullRequestApprovalRules](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_EvaluatePullRequestApprovalRules.html)  **
  - **Description:** Grants permission to evaluate whether a pull request is mergable based on its current approval state and approval rule requirements
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApprovalRuleTemplate](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetApprovalRuleTemplate.html)  **
  - **Description:** Grants permission to return information about an approval rule template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBlob](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetBlob.html)  **
  - **Description:** Grants permission to view the encoded content of an individual file in an AWS CodeCommit repository from the AWS CodeCommit console
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBranch](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetBranch.html)  **
  - **Description:** Grants permission to get details about a branch in an AWS CodeCommit repository with this API; does not control Git branch actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComment](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetComment.html)  **
  - **Description:** Grants permission to get the content of a comment made on a change, file, or commit in a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommentReactions](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommentReactions.html)  **
  - **Description:** Grants permission to get the reactions on a comment
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommentsForComparedCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommentsForComparedCommit.html)  **
  - **Description:** Grants permission to get information about comments made on the comparison between two commits
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommentsForPullRequest](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommentsForPullRequest.html)  **
  - **Description:** Grants permission to get comments made on a pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommit.html)  **
  - **Description:** Grants permission to return information about a commit, including commit message and committer information, with this API; does not control Git log actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDifferences](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetDifferences.html)  **
  - **Description:** Grants permission to view information about the differences between valid commit specifiers such as a branch, tag, HEAD, commit ID, or other fully qualified reference
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFile](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetFile.html)  **
  - **Description:** Grants permission to return the base-64 encoded contents of a specified file and its metadata
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFolder](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetFolder.html)  **
  - **Description:** Grants permission to return the contents of a specified folder in a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMergeCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetMergeCommit.html)  **
  - **Description:** Grants permission to get information about a merge commit created by one of the merge options for pull requests that creates merge commits. Not all merge options create merge commits. This permission does not control Git merge actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Read

- **   [GetMergeConflicts](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetMergeConflicts.html)  **
  - **Description:** Grants permission to get information about merge conflicts between the before and after commit IDs for a pull request in a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMergeOptions](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetMergeOptions.html)  **
  - **Description:** Grants permission to get information about merge options for pull requests that can be used to merge two commits; does not control Git merge actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPullRequest](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetPullRequest.html)  **
  - **Description:** Grants permission to get information about a pull request in a specified repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPullRequestApprovalStates](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetPullRequestApprovalStates.html)  **
  - **Description:** Grants permission to retrieve the current approvals on an inputted pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPullRequestOverrideState](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetPullRequestOverrideState.html)  **
  - **Description:** Grants permission to retrieve the current override state of a given pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepository](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetRepository.html)  **
  - **Description:** Grants permission to get information about an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositoryTriggers](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetRepositoryTriggers.html)  **
  - **Description:** Grants permission to get information about triggers configured for a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApprovalRuleTemplates](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListApprovalRuleTemplates.html)  **
  - **Description:** Grants permission to list all approval rule templates in an AWS Region for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssociatedApprovalRuleTemplatesForRepository](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListAssociatedApprovalRuleTemplatesForRepository.html)  **
  - **Description:** Grants permission to list approval rule templates that are associated with a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBranches](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListBranches.html)  **
  - **Description:** Grants permission to list branches for an AWS CodeCommit repository with this API; does not control Git branch actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFileCommitHistory](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListFileCommitHistory.html)  **
  - **Description:** Grants permission to list commits and changes to a specified file
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPullRequests](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListPullRequests.html)  **
  - **Description:** Grants permission to list pull requests for a specified repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRepositories](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListRepositories.html)  **
  - **Description:** Grants permission to list information about AWS CodeCommit repositories in the current Region for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositoriesForApprovalRuleTemplate](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListRepositoriesForApprovalRuleTemplate.html)  **
  - **Description:** Grants permission to list repositories that are associated with an approval rule template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the resource attached to a CodeCommit resource ARN
  - **Resource types (\*required):** [repository](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [MergeBranchesByFastForward](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeBranchesByFastForward.html)  **
  - **Description:** Grants permission to merge two commits into the specified destination branch using the fast-forward merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [MergeBranchesBySquash](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeBranchesBySquash.html)  **
  - **Description:** Grants permission to merge two commits into the specified destination branch using the squash merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [MergeBranchesByThreeWay](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeBranchesByThreeWay.html)  **
  - **Description:** Grants permission to merge two commits into the specified destination branch using the three-way merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [MergePullRequestByFastForward](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergePullRequestByFastForward.html)  **
  - **Description:** Grants permission to close a pull request and attempt to merge it into the specified destination branch for that pull request at the specified commit using the fast-forward merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [MergePullRequestBySquash](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergePullRequestBySquash.html)  **
  - **Description:** Grants permission to close a pull request and attempt to merge it into the specified destination branch for that pull request at the specified commit using the squash merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [MergePullRequestByThreeWay](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergePullRequestByThreeWay.html)  **
  - **Description:** Grants permission to close a pull request and attempt to merge it into the specified destination branch for that pull request at the specified commit using the three-way merge option
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [OverridePullRequestApprovalRules](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_OverridePullRequestApprovalRules.html)  **
  - **Description:** Grants permission to override all approval rules for a pull request, including approval rules created by a template
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PostCommentForComparedCommit](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PostCommentForComparedCommit.html)  **
  - **Description:** Grants permission to post a comment on the comparison between two commits
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PostCommentForPullRequest](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PostCommentForPullRequest.html)  **
  - **Description:** Grants permission to post a comment on a pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PostCommentReply](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PostCommentReply.html)  **
  - **Description:** Grants permission to post a comment in reply to a comment on a comparison between commits or a pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutCommentReaction](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PutCommentReaction.html)  **
  - **Description:** Grants permission to post a reaction on a comment
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFile](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PutFile.html)  **
  - **Description:** Grants permission to add or update a file in a branch in an AWS CodeCommit repository, and generate a commit for the addition in the specified branch
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [PutRepositoryTriggers](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PutRepositoryTriggers.html)  **
  - **Description:** Grants permission to create, update, or delete triggers for a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to attach resource tags to a CodeCommit resource ARN
  - **Resource types (\*required):** [repository](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codecommit-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecommit-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestRepositoryTriggers](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_TestRepositoryTriggers.html)  **
  - **Description:** Grants permission to test the functionality of repository triggers by sending information to the trigger target
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate resource tags from a CodeCommit resource ARN
  - **Resource types (\*required):** [repository](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codecommit-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApprovalRuleTemplateContent](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateApprovalRuleTemplateContent.html)  **
  - **Description:** Grants permission to update the content of approval rule templates; does not grant permission to update content of approval rules created specifically for pull requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApprovalRuleTemplateDescription](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateApprovalRuleTemplateDescription.html)  **
  - **Description:** Grants permission to update the description of approval rule templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApprovalRuleTemplateName](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateApprovalRuleTemplateName.html)  **
  - **Description:** Grants permission to update the name of approval rule templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateComment](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateComment.html)  **
  - **Description:** Grants permission to update the contents of a comment if the identity matches the identity used to create the comment
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDefaultBranch](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateDefaultBranch.html)  **
  - **Description:** Grants permission to change the default branch in an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePullRequestApprovalRuleContent](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestApprovalRuleContent.html)  **
  - **Description:** Grants permission to update the content for approval rules created for a specific pull requests; does not grant permission to update approval rule content for rules created with an approval rule template
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePullRequestApprovalState](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestApprovalState.html)  **
  - **Description:** Grants permission to update the approval state for pull requests
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePullRequestDescription](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestDescription.html)  **
  - **Description:** Grants permission to update the description of a pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePullRequestStatus](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestStatus.html)  **
  - **Description:** Grants permission to update the status of a pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePullRequestTitle](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestTitle.html)  **
  - **Description:** Grants permission to update the title of a pull request
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRepositoryDescription](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateRepositoryDescription.html)  **
  - **Description:** Grants permission to change the description of an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRepositoryEncryptionKey](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateRepositoryEncryptionKey.html)  **
  - **Description:** Grants permission to change the AWS KMS encryption key used to encrypt and decrypt an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRepositoryName](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateRepositoryName.html)  **
  - **Description:** Grants permission to change the name of an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS CodeCommit
<a name="list_codecommit-permission-only-actions"></a>

The following actions are defined by AWS CodeCommit but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [BatchGetPullRequests](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-pr)  **
  - **Description:** Grants permission to return information about one or more pull requests in an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CancelUploadArchive](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-acp)  **
  - **Description:** Grants permission to cancel the uploading of an archive to a pipeline in AWS CodePipeline
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBlobDifferences](API_GetBlobDifferences.html)  **
  - **Description:** Grants permission to compute a structured, line-level diff between two blob versions in an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommitHistory](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-code)  **
  - **Description:** Grants permission to get information about the history of commits in a repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommitsFromMergeBase](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-pr)  **
  - **Description:** Grants permission to get information about the difference between commits in the context of a potential merge
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetObjectIdentifier](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-code)  **
  - **Description:** Grants permission to resolve blobs, trees, and commits to their identifier
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReferences](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-code)  **
  - **Description:** Grants permission to get details about references in an AWS CodeCommit repository; does not control Git reference actions
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTree](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-code)  **
  - **Description:** Grants permission to view the contents of a specified tree in an AWS CodeCommit repository from the AWS CodeCommit console
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUploadArchiveStatus](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-acp)  **
  - **Description:** Grants permission to get status information about an archive upload to a pipeline in AWS CodePipeline
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GitPull](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-git)  **
  - **Description:** Grants permission to pull information from an AWS CodeCommit repository to a local repo
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GitPush](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-git)  **
  - **Description:** Grants permission to push information from a local repo to an AWS CodeCommit repository
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)<br />[codecommit:References](#list_codecommit-codecommit_References)
  - **Access level:** Write

- **   [UploadArchive](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html#aa-acp)  **
  - **Description:** Grants permission to the service role for AWS CodePipeline to upload repository changes into a pipeline
  - **Resource types (\*required):** [repository\*](#list_codecommit-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CodeCommit
<a name="list_codecommit-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [repository](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control.html#arn-formats)  | arn:${Partition}:codecommit:${Region}:${Account}:${RepositoryName} | [aws:ResourceTag/${TagKey}](#list_codecommit-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CodeCommit
<a name="list_codecommit-policy-keys"></a>

AWS CodeCommit defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [codecommit:References](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-conditional-branch.html)  | Filters access by Git reference to specified AWS CodeCommit actions | String | 