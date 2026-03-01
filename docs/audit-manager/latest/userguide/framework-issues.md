# Troubleshooting framework issues

You can use the information on this page to resolve common framework issues in
Audit Manager.

###### General framework issues

- [On my custom framework details page, I’m prompted to recreate my custom framework](#recreate-framework-post-common-controls "#recreate-framework-post-common-controls")
- [I can’t make a copy of my custom framework](#cannot-use-custom-framework "#cannot-use-custom-framework")

###### Framework sharing issues

- [My sent share request status displays as Failed](#framework-sharing-error "#framework-sharing-error")
- [My share request has a blue dot next to it. What does this mean?](#framework-sharing-blue-dot "#framework-sharing-blue-dot")
- [My shared framework has controls that use custom AWS Config rules as a data source. Can the recipient collect evidence for these controls?](#framework-sharing-custom-config-rules "#framework-sharing-custom-config-rules")
- [I updated a custom rule that's used in a shared framework. Do I need to take any action?](#framework-sharing-what-happens-when-a-rule-is-updated "#framework-sharing-what-happens-when-a-rule-is-updated")

## On my custom framework details page, I’m prompted to recreate my custom framework

![Screenshot of the pop-up message that prompts you to recreate your assessment.](images/troubleshooting-recreate-framework-post-common-controls-console.png)

If you see a message that says **Updated control definitions are
available**, this indicates that Audit Manager now provides newer definitions
for some of the standard controls that are in your custom framework.

Standard controls can now collect evidence from [AWS managed source](concepts.md#aws-managed-source "concepts.md#aws-managed-source"). This means that whenever Audit Manager updates the
underlying data sources for a common or core control, the same update is
automatically applied to the related standard controls. This helps you to ensure
continuous compliance as the cloud compliance environment changes. To make sure that
you benefit from these AWS managed sources, we recommend that you replace the
controls in your custom framework.

In your custom framework, Audit Manager indicates which controls have replacements
available. You’ll need to replace these controls before you can make a copy of your
custom framework. The next time that you edit your custom framework, we’ll prompt
you to replace these controls along with any other edits you’d like to make.

There are two ways to replace the controls in your custom framework:

###### 1. Recreate your custom framework

If a large number of controls have replacements available, we recommend that
you recreate your custom framework. This is likely to be the best option if your
custom framework is based on a standard framework.

- For example, let’s say you created your custom framework using [NIST SP 800-53 Rev 5](NIST800-53r5.md "NIST800-53r5.md") as the starting
  point. This standard framework has 1007 standard controls, and you added 20
  custom controls.
- In this case, the most efficient option is to find `NIST 800-53 (Rev.

5.  Low-Moderate-High` in the framework library and [make an editable copy of that framework](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md"). During this process,
    you can add the same 20 custom controls that you used before. Because you’re
    now using the latest definition of the standard framework as your starting
    point, your custom framework automatically inherits the latest definitions
    for all of the 1007 standard controls.

###### 2. Edit your custom framework

If a small number of controls have replacements available, we recommend that
you edit your custom framework and replace the controls manually.

- For example, let’s say you created your custom framework from scratch. In
  your custom framework, you added 20 custom controls that you created
  yourself, and eight standard controls from the [ACSC Essential Eight](essential-eight.md "essential-eight.md") standard
  framework.
- In this case, because a maximum of eight controls would have updates
  available, the most efficient option is to edit your custom framework and
  replace those controls one by one. For instructions, see the following
  procedure.

###### To manually replace controls in your custom framework

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Framework
   library**, then choose the **Custom
   frameworks** tab.
3. Select the framework that you want to edit, choose
   **Actions**, and then choose
   **Edit**.
4. On the **Edit framework details** page, choose
   **Next**.
5. On the **Edit control sets** page, review the
   name of each control set to see if any of its controls have
   replacements available.
6. Choose an affected control set to expand it and identify which of
   its controls need to be replaced.

###### Tip

To more quickly identify controls, enter
`Replacement available` in the search
box. 7. Remove affected controls by selecting the check box and choosing
**Remove from control set**. 8. Re-add the same controls. This action replaces the controls that
you just removed with the latest control definition.

    1. Under **Add controls**, use the
     **Control type** dropdown list and
     select **Standard controls**.
    2. Find the replacement for the control that you just
     removed.


    ###### Tip

    In some cases, the replacement control name might not
     be exactly the same as the original. In this event, the
     replacement control name is likely to be very similar to
     the original. In rare cases, one control might be
     replaced by two controls (or the other way
     around).

    If you can't find a replacement control, we recommend
     that you do a partial search. To do this, enter part of
     the original control name or a keyword that represents
     what you're looking for. You can also search by
     compliance type to further narrow the list of
     results.
    3. Select the check box next to a control and choose
     **Add to control set**.
    4. In the pop-up window that appears, choose
     **Add** to confirm.

9. Repeat steps 6-8 as needed until you have replaced all
   controls.
10. Choose **Next**.
11. On the **Review and save** page, choose
    **Save changes**.

## I can’t make a copy of my custom framework

If the **Make a copy** button is unavailable on the framework
details page, this means that you need to replace some of the controls in your
custom framework.

For instructions on how to proceed, see [On my custom framework details page, I’m prompted to recreate my custom framework](#recreate-framework-post-common-controls "#recreate-framework-post-common-controls").

## My sent share request status displays as _Failed_

If you try to share a custom framework and the operation fails, we recommend that
you check the following:

1. Make sure that Audit Manager is enabled in the recipient's AWS account and in the
   specified Region. For a list of supported AWS Audit Manager Regions, see [AWS Audit Manager
   endpoints and quotas](../../../general/latest/gr/audit-manager.md "../../../general/latest/gr/audit-manager.md") in the _Amazon Web Services
   General Reference_.
2. Make sure that you entered the correct AWS account ID when you specified
   the recipient account.
3. Make sure that you didn't specify an AWS Organizations management account as the
   recipient. You can share a custom framework with a delegated administrator,
   but if you try to share a custom framework with a management account, the
   operation fails.
4. If you use a customer managed key to encrypt your Audit Manager data, make sure that your
   KMS key is enabled. If your KMS key is disabled and you try to share a
   custom framework, the operation fails. For instructions on how to enable a
   disabled KMS key, see [Enabling and
   disabling keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") in the _AWS Key Management Service
   Developer Guide_.

## My share request has a blue dot next to it. What does this mean?

A blue dot notification indicates that a share request needs your attention.

A blue notification dot appears next to sent share requests with a status
of _Expiring_. Audit Manager displays the blue dot
notification so that you can remind the recipient to take action on the
share request before it expires.

For the blue notification dot to disappear, the recipient must accept or
decline the request. The blue dot also disappears if you revoke the share
request.

You can use the following procedure to check for any expiring share
requests, and send an optional reminder to the recipient to take
action.

**To view notifications for sent
requests**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. If you have a share request notification, Audit Manager displays a red dot
   next to the navigation menu icon.

![Screenshot of the minimized navigation menu icon, with a red dot that indicates a notification.](images/framework_sharing-navigation_minimized_notification-console.png) 3. Expand the navigation pane and look next to **Share
requests**. A notification badge indicates the number
of share requests that need attention.

![Screenshot of the expanded navigation menu, with Shared framework requests highlighted and a notification badge showing 1 notification.](images/framework_sharing-navigation_expanded_notification-console.png) 4. Choose **Share requests**, and then choose the
**Sent requests** tab. 5. Look for the blue dot to identify share requests that expire
within the next 30 days. Alternatively, you can also view expiring
share requests by selecting **Expiring** from the
**All statuses** filter dropdown.

![Screenshot of a received share request with a blue dot next to the framework name.](images/framework_sharing-blue_dot_notification-sent_requests-console.png) 6. (Optional) Remind the recipient that they need to take action on
the share request before it expires. This step is optional, as Audit Manager
sends a notification in the console to inform the recipient when a
share request is active or expiring. However, you can also send your
own reminder to the recipient using your preferred communication
channel.
A blue notification dot appears next to received share requests with a
status of _Active_ or _Expiring_. Audit Manager displays the blue dot
notification to remind you to take action on the share request before it
expires. For the blue notification dot to disappear, you must [accept or decline](responding-to-shared-framework-requests.md#responding-to-shared-framework-requests-step-2 "responding-to-shared-framework-requests.md#responding-to-shared-framework-requests-step-2") the request. The blue dot also disappears if
the sender revokes the share request.

You can use the following procedure to check for active and expiring share
requests.

**To view notifications for received
requests**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. If you have a share request notification, Audit Manager displays a red dot
   next to the navigation menu icon.

![Screenshot of the minimized navigation menu icon, with a red dot that indicates a notification.](images/framework_sharing-navigation_minimized_notification-console.png) 3. Expand the navigation pane and look next to **Share
requests**. A notification badge indicates the number
of share requests that need your attention.

![Screenshot of the expanded navigation menu, with Share requests highlighted and a notification badge showing one notification.](images/framework_sharing-navigation_expanded_notification-console.png) 4. Choose **Share requests**. By default, this page
opens on the **Received requests** tab. 5. Identify the share requests that need your action by looking for
items with a blue dot.

![Screenshot of a received share request with a blue dot next to the framework name.](images/framework_sharing-blue_dot_notification-console.png) 6. (Optional) To view only requests that expire in the next 30 days,
find the **All statuses** dropdown list and select
**Expiring**.

## My shared framework has controls that use custom AWS Config rules as a data source. Can the recipient collect evidence for these controls?

Yes, your recipient can collect evidence for these controls, but a few steps are
needed to achieve this.

For Audit Manager to collect evidence using an AWS Config rule as a data source mapping, the
following must be true. These criteria apply to both managed rules and custom
rules.

- The rule must exist in the recipient’s AWS environment.
- The rule must be enabled in the recipient’s AWS environment.

Remember that the AWS Config rules in your account likely don’t exist already in the
recipient’s AWS environment. Moreover, when the recipient accepts the share
request, Audit Manager doesn’t recreate any of your custom rules in their account. For the
recipient to collect evidence using your custom rules as a data source mapping, they
must create the same custom rules in their instance of AWS Config. After the recipient
[creates](../../../config/latest/developerguide/evaluate-config_develop-rules_nodejs.md "../../../config/latest/developerguide/evaluate-config_develop-rules_nodejs.md") and then [enables](../../../config/latest/developerguide/setting-up-aws-config-rules-with-console.md "../../../config/latest/developerguide/setting-up-aws-config-rules-with-console.md") the rules in AWS Config, Audit Manager can collect evidence from that data
source.

We recommend that you communicate with the recipient to let them know if any
custom AWS Config rules should be created in their instance of AWS Config.

## I updated a custom rule that's used in a shared framework. Do I need to take any action?

###### For rule updates within your AWS environment

When you update a custom rule within your AWS environment, no action is
needed in Audit Manager. Audit Manager detects and handles rule updates in the way that's
described in the following table. Audit Manager doesn't notify you when a rule update is
detected.

| Scenario                                                             | What Audit Manager does                                                                        | What you need to do                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A custom rule is \*_updated_<br>• in<br>your instance of AWS Config. | Audit Manager continues to report findings for that rule using the updated<br>rule definition. | No action is needed.                                                                                                                                                                                                                                                                                                                                 |
| A custom rule is \*_deleted_<br>• in<br>your instance of AWS Config. | Audit Manager stops reporting findings for the deleted rule.                                   | No action is needed.<br>If you want to, you can [edit<br>the custom controls](edit-controls.md "edit-controls.md") that used the deleted rule as a<br>data source mapping. You can then remove the deleted rule to<br>clean up your control's data source settings. Otherwise, the<br>deleted rule name remains as an unused data source<br>mapping. |

###### For rule updates outside your AWS environment

In the recipient’s AWS environment, Audit Manager doesn’t detect the rule update.
This is because senders and recipients each work in separate AWS environments.
The following table provides recommended actions for this scenario.

| Your role | Scenario                                                                                                                                                                                                                | Recommended action                                                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sender    | • You shared a framework that uses custom rules as a<br>data source mapping.<br>• After you shared the framework, you updated or deleted<br>one of those rules in AWS Config.                                           | Contact the recipient to let them know about the update. That<br>way, they can make the same update and stay in sync with the latest<br>rule definition. |
| Recipient | • You accepted a shared framework that uses custom rules<br>as a data source mapping.<br>• After you recreated the custom rules in your instance<br>of AWS Config, the sender updated or deleted one of those<br>rules. | Make the corresponding rule update in your own instance of<br>AWS Config.                                                                                |
