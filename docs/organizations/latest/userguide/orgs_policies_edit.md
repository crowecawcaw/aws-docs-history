

# Editing tags attached to organization policies with AWS Organizations
<a name="orgs_policies_edit"></a>

This topic describes how to edit tags attached policies with AWS Organizations. A *policy* defines the controls that you want to apply to a group of AWS accounts.

**Topics**
+ [Edit tags attached to a service control policy (SCP)](#tag_policy_scp)
+ [Edit tags attached to a resource control policy (RCP)](#tag_policy_rcp)
+ [Edit tags attached to an declarative policy](#tag-declarative-policy-procedure)
+ [Edit tags attached to a backup policy](#tag-backup-policy-procedure)
+ [Edit tags attached to a tag policy](#tag_tag-policies)
+ [Edit tags attached to a chat applications policy](#tag_chatbot-policies)
+ [Edit tags attached to an AI services opt-out policy](#tag-ai-opt-out-policy-procedure)
+ [Edit tags attached to a Security Hub policy](#tag-security-hub-policy-procedure)

## Edit tags attached to a service control policy (SCP)
<a name="tag_policy_scp"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to an SCP. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md). 

**Minimum permissions**  
To edit the tags attached to an SCP in your organization, you must have the following permissions:  
`organizations:DescribeOrganization` – required only when using the Organizations console
`organizations:DescribePolicy` – required only when using the Organizations console
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to an SCP**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy)** page choose the name of the policy with the tags that you want to edit.

1. On the policy details page, choose the **Tags** tab, and then choose**Manage tags**.

1. Make any or all of the following changes:
   + Change the value of a tag by entering a new value over the old one. You can't directly modify the tag key. To change a key, you must delete the tag with the old key and then add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. When you're finished, choose **Save changes**.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to an SCP**  
You can use one of the following commands to edit the tags attached to an SCP:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to a resource control policy (RCP)
<a name="tag_policy_rcp"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to an RCP. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md). 

**Minimum permissions**  
To edit the tags attached to an RCP in your AWS organization, you must have the following permissions:  
`organizations:DescribeOrganization` – required only when using the Organizations console
`organizations:DescribePolicy` – required only when using the Organizations console
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to an RCP**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **Resource control policy** page, choose the name of the policy with the tags that you want to edit.

1. On the policy details page, choose the **Tags** tab, and then choose **Manage tags**.

1. Make any or all of the following changes:
   + Change the value of a tag by entering a new value over the old one. You can't directly modify the tag key. To change a key, you must delete the tag with the old key and then add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. When you're finished, choose **Save changes**.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to an RCP**  
You can use one of the following commands to edit the tags attached to an RCP:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to an declarative policy
<a name="tag-declarative-policy-procedure"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to a declarative policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md).

**Minimum permissions**  
To edit the tags attached to a declarative policy in your AWS organization, you must have the following permissions:  
`organizations:DescribeOrganization`– required only when using the Organizations console
`organizations:DescribePolicy`– required only when using the Organizations console
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to a declarative policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the ** [Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2)** page, choose the name of the policy with the tags that you want to edit.

1. On the chosen policy's detail page, choose the **Tags** tab, and then choose **Manage tags**.

1. You can perform any of these actions on this page:
   + Edit the value for any tag by entering a new value over the old one. You can't modify the key. To change a key, you must delete the tag with the old key and add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. Choose **Save changes** after you've made all the additions, removals, and edits you want to make.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to a declarative policy**  
You can use one of the following commands to edit the tags attached to a declarative policy:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to a backup policy
<a name="tag-backup-policy-procedure"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to a backup policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md).

**Minimum permissions**  
To edit the tags attached to a backup policy in your organization, you must have the following permissions:  
`organizations:DescribeOrganization` (console only – to navigate to the policy)
`organizations:DescribePolicy` (console only – to navigate to the policy)
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to an backup policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy)** page

1. Choose the name of the policy with the tags that you want to edit.

   The policy detail page appears.

1. On the **Tags** tab, choose **Manage tags**.

1. You can perform any of these actions on this page:
   + Edit the value for any tag by entering a new value over the old one. You can't modify the key. To change a key, you must delete the tag with the old key and add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. Choose **Save changes** after you've made all the additions, removals, and edits you want to make.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to a backup policy**  
You can use one of the following commands to edit the tags attached to a backup policy:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to a tag policy
<a name="tag_tag-policies"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to a tag policy. To do this, complete the following steps.

**Minimum permissions**  
To edit the tags attached to a tag policy in your organization, you must have the following permissions:  
`organizations:DescribeOrganization` (console only – to navigate to the policy)
`organizations:DescribePolicy` (console only – to navigate to the policy)
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to a tag policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the ****[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy)** page** page, choose the name of the policy with the tags that you want to edit.

1. On the chosen policy's detail page, choose the **Tags** tab, and then choose **Manage tags**.

1. You can perform any of these actions on this page:
   + Edit the value for any tag by entering a new value over the old one. You can't modify the key. To change a key, you must delete the tag with the old key and add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. Choose **Save changes** after you've made all the additions, removals, and edits you want to make.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to a tag policy**  
You can use one of the following commands to edit the tags attached to a tag policy:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to a chat applications policy
<a name="tag_chatbot-policies"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to a chat applications policy. To do this, complete the following steps.

**Minimum permissions**  
To edit the tags attached to a chat applications policy in your organization, you must have the following permissions:  
`organizations:DescribeOrganization` (console only – to navigate to the policy)
`organizations:DescribePolicy` (console only – to navigate to the policy)
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to an chat applications policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the ****[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy)** page** page, choose the name of the policy with the tags that you want to edit.

1. On the chosen policy's detail page, choose the **Tags** tab, and then choose **Manage tags**.

1. You can perform any of these actions on this page:
   + Edit the value for any tag by entering a new value over the old one. You can't modify the key. To change a key, you must delete the tag with the old key and add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. Choose **Save changes** after you've made all the additions, removals, and edits you want to make.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to a chat applications policy**  
You can use one of the following commands to edit the tags attached to a chat applications policy:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to an AI services opt-out policy
<a name="tag-ai-opt-out-policy-procedure"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to an AI services opt-out policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md).

**Minimum permissions**  
To edit the tags attached to an AI services opt-out policy in your organization, you must have the following permissions:  
`organizations:DescribeOrganization`– required only when using the Organizations console
`organizations:DescribePolicy`– required only when using the Organizations console
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to an AI services opt-out policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy)** page, choose the name of the policy with the tags that you want to edit.

1. On the chosen policy's detail page, choose the **Tags** tab, and then choose **Manage tags**.

1. You can perform any of these actions on this page:
   + Edit the value for any tag by entering a new value over the old one. You can't modify the key. To change a key, you must delete the tag with the old key and add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. Choose **Save changes** after you've made all the additions, removals, and edits you want to make.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to a AI services opt-out policy**  
You can use one of the following commands to edit the tags attached to a AI services opt-out policy:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------

## Edit tags attached to a Security Hub policy
<a name="tag-security-hub-policy-procedure"></a>

When you sign in to your organization's management account, you can add or remove the tags attached to a Security Hub policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md).

**Minimum permissions**  
To edit the tags attached to a Security Hub policy in your organization, you must have the following permissions:  
`organizations:DescribeOrganization`– required only when using the Organizations console
`organizations:DescribePolicy`– required only when using the Organizations console
`organizations:TagResource`
`organizations:UntagResource`

------
#### [ AWS Management Console ]

**To edit the tags attached to a Security Hub policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy)** page, choose the name of the policy with the tags that you want to edit.

1. On the chosen policy's detail page, choose the **Tags** tab, and then choose **Manage tags**.

1. You can perform any of these actions on this page:
   + Edit the value for any tag by entering a new value over the old one. You can't modify the key. To change a key, you must delete the tag with the old key and add a tag with the new key. 
   + Remove an existing tag by choosing **Remove**.
   + Add a new tag key and value pair. Choose **Add tag**, then enter the new key name and optional value in the provided boxes. If you leave the **Value** box empty, the value is an empty string; it isn't `null`.

1. Choose **Save changes** after you've made all the additions, removals, and edits you want to make.

------
#### [ AWS CLI & AWS SDKs ]

**To edit the tags attached to a Security Hub policy**  
You can use one of the following commands to edit the tags attached to a Security Hub policy:
+ AWS CLI: [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/organizations/untag-resource.html)
+ AWS SDKs: [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)

------