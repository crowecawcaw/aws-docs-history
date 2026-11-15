

# Create a rule in conversational analytics that ends associated email contacts from a case
<a name="contact-lens-rules-ends-email-contacts"></a>

**To create a rule that ends associated email contacts**

1. When you create your rule, choose **A case is updated** as the event source.  
![The new Cases rule page, the When dropdown menu, the A case is updated option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-ends-email-contacts-1.png)

1. When you create your rule, choose **End email contacts** for the action.  
![The new Cases rule page, the Add action dropdown menu, the End email contacts option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-ends-email-contacts-2.png)  
![The End email contacts action added to the rule.](https://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-ends-email-contacts-3.png)

1. Choose **Next**. Name your rule, review it, and then choose **Save**.

1. After you add rules, they are applied to new contacts that occur after the rule was added. Rules are applied when Connect Customer conversational analytics analyzes conversations.

   You cannot apply rules to past, stored conversations. 