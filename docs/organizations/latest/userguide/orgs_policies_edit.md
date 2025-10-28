# Editing tags attached to organization policies with

AWS Organizations

This topic describes how to edit tags attached policies with AWS Organizations. A
_policy_ defines the controls that you want to apply to a group of
AWS accounts.

###### Topics

- [Edit tags attached to a service control policy
  (SCP)](#tag_policy_scp "#tag_policy_scp")
- [Edit tags attached to a resource control policy
  (RCP)](#tag_policy_rcp "#tag_policy_rcp")
- [Edit tags attached to an declarative
  policy](#tag-declarative-policy-procedure "#tag-declarative-policy-procedure")
- [Edit tags attached to a backup
  policy](#tag-backup-policy-procedure "#tag-backup-policy-procedure")
- [Edit tags attached to a tag policy](#tag_tag-policies "#tag_tag-policies")
- [Edit tags attached to a chat applications
  policy](#tag_chatbot-policies "#tag_chatbot-policies")
- [Edit tags attached to an AI services
  opt-out policy](#tag-ai-opt-out-policy-procedure "#tag-ai-opt-out-policy-procedure")
- [Edit tags attached to a Security Hub
  policy](#tag-security-hub-policy-procedure "#tag-security-hub-policy-procedure")

## Edit tags attached to a service control policy

(SCP)

When you sign in to your organization's management account, you can add or remove the
tags attached to an SCP. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Minimum permissions

To edit the tags attached to an SCP in your organization, you must have the
following permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:DescribePolicy` – required only when using the Organizations console
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to an SCP

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy")** page choose the name of the policy with the
   tags that you want to edit.
3. On the policy details page, choose the **Tags**
   tab, and then choose**Manage tags**.
4. Make any or all of the following changes:
   - Change the value of a tag by entering a new value over the
     old one. You can't directly modify the tag key. To change a
     key, you must delete the tag with the old key and then add a
     tag with the new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. When you're finished, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To edit the tags attached to an SCP

You can use one of the following commands to edit the tags attached to
an SCP:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to a resource control policy

(RCP)

When you sign in to your organization's management account, you can add or remove the
tags attached to an RCP. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Minimum permissions

To edit the tags attached to an RCP in your AWS organization, you must have the
following permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:DescribePolicy` – required only when using the Organizations console
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to an RCP

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **Resource control policy** page, choose
   the name of the policy with the tags that you want to edit.
3. On the policy details page, choose the **Tags**
   tab, and then choose **Manage tags**.
4. Make any or all of the following changes:
   - Change the value of a tag by entering a new value over the
     old one. You can't directly modify the tag key. To change a
     key, you must delete the tag with the old key and then add a
     tag with the new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. When you're finished, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To edit the tags attached to an RCP

You can use one of the following commands to edit the tags attached to
an RCP:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to an declarative

policy

When you sign in to your organization's management account, you can add or remove the
tags attached to a declarative policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Minimum permissions

To edit the tags attached to a declarative policy in your AWS organization, you
must have the following permissions:

- `organizations:DescribeOrganization`– required only when using the Organizations console
- `organizations:DescribePolicy`– required only when using the Organizations console
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to a declarative policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2 "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2")** page, choose the
   name of the policy with the tags that you want to edit.
3. On the chosen policy's detail page, choose the
   **Tags** tab, and then choose **Manage
   tags**.
4. You can perform any of these actions on this page:
   - Edit the value for any tag by entering a new value over
     the old one. You can't modify the key. To change a key, you
     must delete the tag with the old key and add a tag with the
     new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to a declarative policy

You can use one of the following commands to edit the tags attached to
a declarative policy:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to a backup

policy

When you sign in to your organization's management account, you can add or remove the
tags attached to a backup policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Minimum permissions

To edit the tags attached to a backup policy in your organization, you must have
the following permissions:

- `organizations:DescribeOrganization` (console only – to
  navigate to the policy)
- `organizations:DescribePolicy` (console only – to
  navigate to the policy)
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to an backup policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy "https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy")** page
3. Choose the name of the policy with the tags that you want to
   edit.

The policy detail page appears. 4. On the **Tags** tab, choose **Manage
tags**. 5. You can perform any of these actions on this page:

    * Edit the value for any tag by entering a new value over
     the old one. You can't modify the key. To change a key, you
     must delete the tag with the old key and add a tag with the
     new key.
    * Remove an existing tag by choosing
     **Remove**.
    * Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

6. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to a backup policy

You can use one of the following commands to edit the tags attached to
a backup policy:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to a tag policy

When you sign in to your organization's management account, you can add or remove the
tags attached to a tag policy. To do this, complete the following steps.

###### Minimum permissions

To edit the tags attached to a tag policy in your organization, you must have the
following permissions:

- `organizations:DescribeOrganization` (console only – to
  navigate to the policy)
- `organizations:DescribePolicy` (console only – to
  navigate to the policy)
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to a tag policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the \***\*[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy "https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy")** page\*\* page, choose the
   name of the policy with the tags that you want to edit.
3. On the chosen policy's detail page, choose the
   **Tags** tab, and then choose **Manage
   tags**.
4. You can perform any of these actions on this page:
   - Edit the value for any tag by entering a new value over
     the old one. You can't modify the key. To change a key, you
     must delete the tag with the old key and add a tag with the
     new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to a tag policy

You can use one of the following commands to edit the tags attached to
a tag policy:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to a chat applications

policy

When you sign in to your organization's management account, you can add or remove the
tags attached to a chat applications policy. To do this, complete the following
steps.

###### Minimum permissions

To edit the tags attached to a chat applications policy in your organization, you
must have the following permissions:

- `organizations:DescribeOrganization` (console only – to
  navigate to the policy)
- `organizations:DescribePolicy` (console only – to
  navigate to the policy)
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to an chat applications policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the \***\*[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy")** page\*\* page, choose
   the name of the policy with the tags that you want to edit.
3. On the chosen policy's detail page, choose the
   **Tags** tab, and then choose **Manage
   tags**.
4. You can perform any of these actions on this page:
   - Edit the value for any tag by entering a new value over
     the old one. You can't modify the key. To change a key, you
     must delete the tag with the old key and add a tag with the
     new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to a chat applications policy

You can use one of the following commands to edit the tags attached to
a chat applications policy:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to an AI services

opt-out policy

When you sign in to your organization's management account, you can add or remove the
tags attached to an AI services opt-out policy. For more information about tagging, see
[Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Minimum permissions

To edit the tags attached to an AI services opt-out policy in your organization,
you must have the following permissions:

- `organizations:DescribeOrganization`– required only when using the Organizations console
- `organizations:DescribePolicy`– required only when using the Organizations console
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to an AI services opt-out policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose the name of the policy
   with the tags that you want to edit.
3. On the chosen policy's detail page, choose the
   **Tags** tab, and then choose **Manage
   tags**.
4. You can perform any of these actions on this page:
   - Edit the value for any tag by entering a new value over
     the old one. You can't modify the key. To change a key, you
     must delete the tag with the old key and add a tag with the
     new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to a AI services opt-out policy

You can use one of the following commands to edit the tags attached to
a AI services opt-out policy:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

## Edit tags attached to a Security Hub

policy

When you sign in to your organization's management account, you can add or remove the
tags attached to a Security Hub policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Minimum permissions

To edit the tags attached to a Security Hub policy in your organization, you must have
the following permissions:

- `organizations:DescribeOrganization`– required only when using the Organizations console
- `organizations:DescribePolicy`– required only when using the Organizations console
- `organizations:TagResource`
- `organizations:UntagResource`

AWS Management Console

###### To edit the tags attached to a Security Hub policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy")** page, choose the name of the policy
   with the tags that you want to edit.
3. On the chosen policy's detail page, choose the
   **Tags** tab, and then choose **Manage
   tags**.
4. You can perform any of these actions on this page:
   - Edit the value for any tag by entering a new value over
     the old one. You can't modify the key. To change a key, you
     must delete the tag with the old key and add a tag with the
     new key.
   - Remove an existing tag by choosing
     **Remove**.
   - Add a new tag key and value pair. Choose **Add
     tag**, then enter the new key name and optional
     value in the provided boxes. If you leave the
     **Value** box empty, the value is an
     empty string; it isn't `null`.

5. Choose **Save changes** after you've made all the
   additions, removals, and edits you want to make.

AWS CLI & AWS SDKs

###### To edit the tags attached to a Security Hub policy

You can use one of the following commands to edit the tags attached to
a Security Hub policy:

- AWS CLI: [tag-resource](../../../cli/latest/reference/organizations/tag-resource.md "../../../cli/latest/reference/organizations/tag-resource.md") and [untag-resource](../../../cli/latest/reference/organizations/untag-resource.md "../../../cli/latest/reference/organizations/untag-resource.md")
- AWS SDKs: [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
