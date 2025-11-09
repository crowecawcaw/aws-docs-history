AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Managing

your application compliance

In Application Manager, a component of AWS Systems Manager, the **Configurations**
page displays [AWS Config](../../../config/latest/developerguide.md "../../../config/latest/developerguide.md") resource and configuration
rule compliance information. This page also displays AWS Systems Manager [State Manager](systems-manager-state.md "systems-manager-state.md") association
compliance information. You can choose a resource, a rule, or an association to open
the corresponding console for more information. This page displays compliance
information from the last 90 days.

###### Actions you can perform on this page

You can perform the following actions on this page:

- Choose a resource name to open the AWS Config console where you can view
  compliance information about a selected resource.
- Choose the option button beside a resource name. Then, choose the
  **Resource timeline** button to open the AWS Config console
  where you can view compliance information about a selected resource.
- In the **Config rules compliance** section, you can do
  the following:
  - Choose a rule name to open the AWS Config console where you can view
    information about that rule.
  - Choose **Add rules** to open the AWS Config console
    where you can create a rule.
  - Choose the option button beside a rule name, choose
    **Actions**, and then choose **Manage
    remediation** to change the remediation action for a
    rule.
  - Choose the option button beside a rule name, choose
    **Actions**, and then choose
    **Re-evaluate** to have AWS Config run a compliance
    check on the selected rule.

- In the **Association compliance** section, you can do the
  following:
  - Choose an association name to open the
    **Associations** page where you can view
    information about that association.
  - Choose **Create association** to open Systems Manager
    State Manager where you can create an association.
  - Choose the option button beside an association name and choose
    **Apply association** to immediately start all
    actions specified in the association.

###### To open the **Compliance** tab

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Application Manager**.
3. In the **Applications** section, choose a category. If
   you want to open an application you created manually in Application Manager, choose
   **Custom applications**.
4. Choose the application in the list. Application Manager opens the
   **Overview** tab.
5. Choose the **Compliance** tab.
