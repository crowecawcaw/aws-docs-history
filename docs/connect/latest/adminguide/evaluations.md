# Evaluate contact center agent performance in Amazon Connect

###### Tip

**New user?** Check out the [Amazon Connect
Agent Evaluation Forms Workshop](https://catalog.workshops.aws/amazon-connect-evaluation-forms/en-US "https://catalog.workshops.aws/amazon-connect-evaluation-forms/en-US"). This online course guides you through
creating a working example of an evaluation form.

**IT administrators**: To enable Amazon Connect evaluation
capabilities, go to the Amazon Connect console, choose your instance alias, choose
**Data storage**, **Content evaluations**,
**Edit**. You'll be prompted to create or choose an S3 bucket.
After the bucket is created, you can store evaluations and export them.

Amazon Connect helps you to assess, track, and improve how agents interact with customers and
resolve issues. For example, you can search for a contact, choose the appropriate evaluation
form, review the contact audio, transcript, or both, and then evaluate how the agent
interacted with the customer. You can then use that feedback to help the agent deliver
improved customer experiences.

You can perform manual evaluations for all contact types (such as voice, chat, email, and task).
Automated evaluations only work for voice and chat contacts analyzed by conversational
analytics.

###### To evaluate performance

1. Log in to Amazon Connect with a user account that has [permissions to perform
   evaluations](evaluation-forms-permissions.md "evaluation-forms-permissions.md").
2. Access the contact that you want to evaluate. There are a few ways you can do
   this. For example, someone may have shared the contact URL with you, or assigned you
   a task that has the URL. Or, you may have the contact ID, which lets you search for
   the contact record by doing the following: on the navigation pane, choose
   **Analytics and optimization**, **Contact
   search**, and then search for the contact that you want to
   evaluate.
3. On the **Contact details** page, choose
   **Evaluations** or the **<** icon.

![The Contact details page, the Evaluations button.](images/evaluationforms-evaluatebutton.png) 4. The **Evaluations** panel lists any evaluations that are in
progress or completed for the contact.

![The evaluations pane, the status of two evaluations.](images/evaluationforms-startevaluation.png) 5. To start an evaluation, choose an evaluation from the dropdown menu, and then
choose **Start evaluation**. 6. To navigate an especially long evaluation form, use the arrows next to each
section to collapse or expand it.

![The evaluations pane, the arrow to collapse or expand a section.](images/evaluationforms-exampleevaluation.png) 7. Choose **Save** to save a form in progress. The status of the
form becomes **Draft**. You can return to it any time to continue,
or you can delete it and start over.

![The evaluations pane, the status of an evaluation set to draft.](images/evaluationforms-draft.png) 8. When you're done, choose **Submit**. If you have skipped optional
questions in the form, you will see a warning asking you to confirm that you want to
submit the evaluation. Choose **Yes**. The evaluation is now
**Completed**.

![Skip optional questions and submit the evaluation.](images/evaluationforms-draft-submit.png)
