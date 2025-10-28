# Create a task in

Contact Lens when a contact is categorized in real-time or after
a call or chat

An especially powerful use of Contact Lens rules is to build rules that
generate tasks. This helps you identify issues in your contact center for you to
follow up, and creates traceable actions with owners. Following are some
examples:

- Create a task to review a contact when the customer is fraudulent. For
  example, you can create a follow-up task when a customer utters words or
  phrases that makes them appear potentially fraudulent.
- Follow up when the customer mentions specific topics that you want to
  later on upsell or provide additional support by reaching out.
- Follow up when there is a serious quality issue. In addition to
  contacts being categorized and getting alerts, you can route a task so
  you have owners. You also have contact records for these tasks, so you
  can search for and trace them.

###### To create a rule that creates a task

1. When you create your rule, choose **Create Task** for
   the action.

![The new rule page, the add action dropdown menu, the create task option.](images/contact-lens-rules-add-task-example1.png) 2. Complete the task fields as follows:

![The new rule page, the assign contact category section, the Create task section.](images/contact-lens-rules-add-tasks-example2.png)

    1. **Category name**: The category name appears
     in the contact record. Max length: 200 characters.
    2. **Name**: The name appears in the agent's
     Contact Control Panel (CCP). Max length: 512 characters.
    3. **Description**: The description appears in
     the agent's Contact Control Panel (CCP). Max length: 4096
     characters.


    ###### Tip

    In **Name** and
     **Description**, use [ ] to choose from
     a menu of dynamic values: **ContactId**,
     **AgentId**,
     **QueueId**, and
     **RuleName**.


    ![The Create task section, the Description field, a list of dynamic values.](images/contact-lens-rules-add-tasks-brackets.png)
    4. **Task reference name**: This is a default
     reference that automatically appears in the agent's CCP.




    	* For real-time rules, the task reference links to the
    	 Real-time details page.
    	* For post-call/chat rules, the task reference links to
    	 the **Contact details** page.
    5. **Additional Reference name**: Max length:
     4096 characters. You can add up to 25 references.
    6. **Select a flow**: Choose the flow that is
     designed to route the task to the appropriate owner of the task.
     The flow must be saved and published for it to appear in your
     list of options in the dropdown.

3. The following image shows an example of how this information appears
   in the agent's CCP.

![A task in the agent's Contact Control Panel.](images/contact-lens-rules-add-tasks-ccp.png)

In this example, the agent sees the following values for
**Name**, **Description**, and
**Task reference name**:

    1. **Name** =
     **Action-Required-Contact Lens-
     ba2cf8fe....**
    2. **Description** =
     **Test**
    3. **Task reference name** = taskRef and the URL
     to the Real-time details page

4. Choose **Next**. Review and then choose
   **Save** the task.
5. After you add rules, they are applied to new contacts that occur after the rule was added. Rules are applied when Contact Lens analyzes conversations.

You cannot apply rules to past, stored conversations.

## Voice and task contact records are

linked

When a rule creates a task, a contact record is automatically generated
for the task. It's linked to the contact record of the voice call or chat
that met the criteria for the rule to create the task.

For example, a call comes into your contact center and generates
CTR1:

![Information on the initial contact record when a call comes in.](images/contact-lens-rules-attributes-example1.png)

The Rules engine generates a task. In the contact record for the task, the
voice contact record appears as the **Previous contact
ID**. In addition, the task contact record inherits contact
attributes from the voice contact record, as illustrated in the following
image:

![Contact record 2 for the task.](images/contact-lens-rules-attributes-example2.png)

## About dynamic values for ContactId,

AgentId, QueueId, RuleName

The dynamic values in brackets [ ] are called [contact attributes](what-is-a-contact-attribute.md "what-is-a-contact-attribute.md"). Contact
attributes enable you to store temporary information about the contact so
you can use it in a flow.

When you add contact attributes in brackets [ ] — such as ContactId,
AgentId, QueueId, or RuleName — the value is passed from one contact
record to another. You can use contact attributes in your flow to branch and
route the contact accordingly.

For more information, see [Use contact attributes](connect-contact-attributes.md "connect-contact-attributes.md").
