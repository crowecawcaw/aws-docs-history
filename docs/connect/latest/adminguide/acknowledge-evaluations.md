

# Acknowledge performance evaluations in Connect Customer
<a name="acknowledge-evaluations"></a>

When an agent performance evaluation is submitted, you can automatically notify the agent to review their evaluation. For example, you can set up a [rule to send an email](contact-lens-rules-email.md) to the agent when an evaluation is available. You can also walk an agent through their evaluation during coaching.

After the agent has reviewed the performance evaluation, they can acknowledge their review of the evaluation and write an optional note in the Connect Customer admin website. This acknowledgement enables managers to track whether agents are reviewing the feedback provided on their performance evaluations.

This topic explains the steps for agents to view and acknowledge an evaluation.

**To acknowledge an evaluation**

1. After you have received a performance evaluation for a contact, use your agent account to log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. Access the contact evaluation that you want to acknowledge. There are a few ways you can do this:
   + Someone might have shared the contact URL with you.

   - OR - 
   + You might have been assigned a task or received an email notification containing the URL for the contact that received an evaluation.

   - OR - 
   + You might have the contact ID and evaluation form name. You can use this information to search for the contact that received the evaluations using the following steps.

     1. On the navigation pane, choose **Analytics and optimization**, **Contact search**.

     1. Search for the contact which was evaluated, but is not yet acknowledged. The following image shows the filters to search for **Acknowledged** = **No**.  
![The Filters section of the Contact search page, set to Acknowledged = No.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack1.png)

1. On the **Contact details** page, choose **Evaluations** or expand the evaluation panel by choosing the **<** icon, as shown in the following image.  
![The Evaluations button, and the icon to expand the evaluation pane.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack2.png)

1. The **Evaluations** panel lists any evaluations that are in progress or completed for the contact. To acknowledge an evaluation, choose an evaluation from the list of **Completed evaluations**. The following image shows one evaluation that has been completed: **Customer servicing scorecard**.  
![The Evaluations pane, the completed evaluations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack3.png)

1. Choose the evaluation you want to review. At the bottom of the evaluation, choose **Acknowledge**, as shown in the following image. 
**Note**  
Only the agent who was evaluated can acknowledge the evaluation.  
![The Evaluations pane, the completed evaluations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack4.png)

1. In the **Acknowledge evaluation result** dialog box, provide an optional comment. For example, *Manager walked through the evaluation during coaching on March 5th, 2025*. 

   When you're finished, choose **Confirm**.   
![The Acknowledge evaluation result section, the Confirm button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack5.png)

1. A message is displayed that the evaluation acknowledgement is **Completed**, as shown in the following image.   
![A message that the evaluation is successfully acknowledged.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack6.png)

1. You can only acknowledge an evaluation after it is submitted. If an evaluation is re-submitted, it again becomes eligible for acknowledgement.

1. To view the acknowledgement note, select the acknowledged evaluation, and then choose the **view note** link.  
![The Acknowledgement note.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-ack7.png)