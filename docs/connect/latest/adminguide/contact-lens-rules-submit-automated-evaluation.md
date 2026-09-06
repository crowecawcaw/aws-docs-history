

# Create a rule in conversational analytics that submits an automated evaluation
<a name="contact-lens-rules-submit-automated-evaluation"></a>

With Conversational analytics, you can automatically fill and submit evaluations by using insights and metrics from conversational analytics. 

## Step 1: Configure automation on the evaluation form
<a name="auto-eval-prereq-1"></a>

Before you can create a rule that submits an automated evaluation, you need to configure automation on the evaluation form. For detailed instructions, see [Step 6: Enable automated evaluations](create-evaluation-forms.md#step-automate) in [Create an evaluation form](create-evaluation-forms.md).

Following is an overview of the steps:

1.  Setup automation on every question in an evaluation form.

1.  Turn on **Enable automated submission of evaluations** before activating the evaluation form.

1.  When you activate the evaluation form with automation configured, a prompt is displayed for you to create a rule, as shown in the following image.   
![A prompt to create a rule.](http://docs.aws.amazon.com/connect/latest/adminguide/images/create-a-rule-to-submit-automated-evaluations-1.png)

1.  Choose **Create a rule**. 

1. On the **Rules** page, define a rule that specifies which contacts are automatically evaluated using the selected evaluation form. The following procedure provides instructions.

## Step 2: Define a rule that specifies which contacts are automatically evaluated
<a name="auto-eval-prereq-2"></a>

You can trigger automated evaluations with two types of rules:
+ A **Conversational analytics** rule that automatically evaluates the contact after conversational analytics completes its analysis.
+ An **Evaluation forms** rule that can be used to trigger a situation-specific evaluation form as an outcome of a generic evaluation form. For example, if the answer to the evaluation question *Was the customer interested in purchasing a product* is *Yes*, then you can trigger another evaluation form measuring *Agent sales performance*.

### Trigger automated evaluations with a conversational analytics rule
<a name="conversational-analytics-rule"></a>

This is the default rule type that is selected when you create a rule to submit an automated evaluation during form activation. You can also create such a rule by selecting **Create a rule**, **Conversational analytics** on the **Rules** page.

1. Choose **A conversational analytics post-call analysis is available** or **A conversational analytics post-chat analysis is available** as the event source. These two options are highlighted in the following image.  
![The post-call analysis and post-chat analysis options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/defined-conditions-evaluations.png)

1. Define conditions to identify contacts to be automatically evaluated, and then choose **Next**.

   Example conditions that you can use to identify the specific set of agents or contacts on which the evaluation form is applicable are: 
   + Agents
   + Agent hierarchy
   + AI agent
   + Queues
   + Initiation method

   In addition, you can exclude contacts that might have ended prematurely due to connectivity or other issues using conditions such as:
   + Interaction duration (for example, over 30 seconds)
   + Talk time (for example, the customer speaks for over 10 seconds)
   + Potential disconnect issue when the issue does not exist or there is no known connectivity or device issue during the conversation

1. On the **Define actions** page provide a category name to identify the rule.

1. Choose **Add action**, select **Submit automated evaluation**, and select the form that you want to use for automatically submitting an evaluation. (This action is already selected on the page if you created the rule when you activate the form.)

1. Choose **Next**. Review and then choose **Save and Publish**.

After you add rules, they are applied to new contacts that occur after the rule was added. Rules are applied when Amazon Connect conversational analytics analyzes conversations.

**Important**  
You cannot apply rules to past, stored conversations.

### Trigger automated evaluations with an evaluation forms rule
<a name="conversational-analytics-rule-2"></a>

1. Navigate to the **Rules** page. Select **Create a rule**, **Evaluation forms**.

1. Under **When**, select the event source as **A conversational analytics evaluation result is available**.

1. Choose **Add condition** to trigger a situation-specific evaluation. For example:
   + A specific answer on another evaluation, shown in the following image.  
![A specific answer on another evaluation.](http://docs.aws.amazon.com/connect/latest/adminguide/images/add-condition-1.png)
   + The score of another evaluation form, shown in the following image.  
![The score of another evaluation form.](http://docs.aws.amazon.com/connect/latest/adminguide/images/add-condition-2.png)

1. Choose **Add action**, select **Submit automated evaluation**, and select the form that you want to use for automatically submitting an evaluation.

1. Choose **Next**. Review and then choose **Save and Publish**.

## Frequently Asked Questions (FAQ)
<a name="auto-eval-faq"></a>

1.  **Can an automated evaluation override an evaluation that has been manually submitted?** 

    No, an automated evaluation cannot override a manually submitted evaluation. If an evaluation already exists, then the automated evaluation will fail for that contact and account administrators can see such failure notifications within CloudWatch.

1.  **How do I identify automated evaluations?** 

    If an evaluation is automatically submitted, it is marked as "submitted by conversational analytics automation" on the **Contact details** page. If an automated evaluation is edited and re-submitted by an evaluator, the "submitted by" contains the name of the evaluator. 

1.  **Can I automatically evaluate a contact using multiple evaluation forms?** 

    Yes, you can automatically submit evaluations on a contact using multiple evaluation forms. You need to create multiple rules to submit automated evaluations using the different evaluation forms.