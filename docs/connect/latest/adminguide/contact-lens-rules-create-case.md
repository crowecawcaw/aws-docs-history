

# Create a rule in conversational analytics that creates a case
<a name="contact-lens-rules-create-case"></a>

**To create a rule that creates a case**

1. When you create your rule, choose **Post-call analysis is available**, **Post-chat analysis is available**, or **Email analysis is available** as the event source.  
![The define condition page with Post-call, Post-chat, and Email analysis event source options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-create-case-1.png)

1. Choose **Next**

1. On the actions page, choose **Create case** for the action.  
![The new rule page, the add action dropdown menu, the create case option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-create-case-2.png)

1. In the **Create case** card, select a **Case template**.  
![In the Create case card, select a Case template.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-create-case-3.png)

1. Fill out the **required fields** and add **optional case fields** to populate case data.
**Note**  
A customer profile must be associated with a contact for this action to work. For more information, see [Enable Cases](enable-cases.md).  
![Fill out the required fields and add optional case fields to populate case data.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-rules-create-case-4.png)

1. Choose **Next**. Review and then choose **Save**.

1. After you add rules, they are applied to new contacts that occur after the rule was added. Rules are applied when Connect Customer conversational analytics analyzes conversations.

   You cannot apply rules to past, stored conversations. 