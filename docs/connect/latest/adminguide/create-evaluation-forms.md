

# Create an evaluation form in Connect Customer
<a name="create-evaluation-forms"></a>

In Connect Customer, you can create [many different evaluation forms](feature-limits.md#evaluationforms-feature-specs). For example, you might need a different evaluation form for each business unit, and for different queues. You can also create different evaluation forms for evaluating the agent interaction and the self-service interaction with a Lex bot or AI agent.

Each form can contain multiple sections and questions. 
+ You can assign [weights](about-scoring-and-weights.md) to each question and section to indicate how much their score impacts the overall score of the evaluation form.
+ You can configure automation on each question so that answers to those questions are automatically filled using insights and metrics from conversational analytics.

This topic explains how to create a form and configure automation using the Connect Customer admin website. To create and manage forms programmatically, see [Evaluation actions](https://docs.aws.amazon.com/connect/latest/APIReference/evaluation-api.html) in the *Connect Customer API Reference*.

**Contents**
+ [Step 1: Create an evaluation form](#step-title)
  + [Create a form from a sample template](#create-sample)
  + [Import an evaluation form from a PDF using AI](#import-form-pdf)
  + [Create a blank form and set a title](#create-blank)
  + [Import an evaluation form from another instance](#import-form-json)
+ [Step 2: Add sections and questions](#step-sections)
+ [Step 3: Add answers](#step-answers)
+ [Step 4: Conditionally enable questions](#step-conditionally-enable-questions)
+ [Step 5: Assign scores and ranges to answers](#step-assignscores)
  + [Step 5.1: Percentage-based scoring](#step-assignscores-percentage)
  + [Step 5.2: Point-based scoring](#step-assignscores-pointbased)
  + [Step 5.3: Assign performance thresholds](#step-assignscores-performance-thresholds)
+ [Step 6: Enable automated evaluations](#step-automate)
  + [Choose a Gen AI version for automated evaluations](#step-automate-genai-version)
+ [Step 7: Preview the evaluation form](#step-preview)
+ [Step 8: Assign weights for final score](#step-weights)
  + [Weight distribution mode](#weight-distribution-mode)
+ [Step 9: Validate the evaluation form](#step-validateform)
+ [Step 10: Activate an evaluation form](#step-activateform)

Before you begin, make sure you have the required security profile permissions. For more information, see [Assign security profile permissions for performance evaluations and coaching](evaluation-and-coaching-permissions.md).

## Step 1: Create an evaluation form
<a name="step-title"></a>

There are several ways to create an evaluation form. Choose the method that best fits how you work — each method opens the form in the editor, where you can refine it to fit your needs, then preview, validate, and activate it:
+ **Sample form** – Start from a pre-built template whose sections, questions, scoring, and automation are already configured, including questions mapped to business outcomes. See [Create a form from a sample template](#create-sample).
+ **Import from a PDF using AI** – Migrate a form from another quality management system by uploading a PDF. See [Import an evaluation form from a PDF using AI](#import-form-pdf).
+ **Blank form** – Build a form from scratch, adding every section, question, and score yourself. See [Create a blank form and set a title](#create-blank).
+ **Import from another instance** – Copy a form between Connect Customer instances (for example, from a test instance to a production instance) using JSON. See [Import an evaluation form from another instance](#import-form-json).

Whichever method you choose, start by navigating to the **Evaluation forms** page:

1. Log in to Connect Customer with a user account that has the following security profile permission: **Analytics and Optimization** - **Evaluation forms - manage form definitions** - **Create**.

1. Choose **Analytics and optimization**, then choose **Evaluation forms**.

### Create a form from a sample template
<a name="create-sample"></a>

Start from a sample form — a pre-built template with sections, questions, answers, scoring, and automation already configured. Sample forms cover both agent-handled and self-service interactions, and include questions that map to standard business outcomes so you can measure them without building the scoring from scratch.

1. On the **Evaluation forms** page, choose **Create new form**.

1. Choose **Use a sample form**, then select a template, such as **Agent Interaction Outcomes**. (Optional) Add tags to control access to the form. Choose **Create**.  
![The create new form page, the Use a sample form option with the list of sample templates.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluation-forms-sample-form.png)

   The form opens fully configured. Its sections, questions, and scoring are already set up, and questions that measure a business outcome are flagged as a **Business outcome metric**.  
![A pre-built sample form question, "Did the conversation result in customer churn?", with the Business outcome metric option selected and mapped to Churn propensity.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluation-forms-sample-form-outcome.png)

1. Review the form and edit it as needed. Because a sample form is already fully configured, you can typically skip ahead to [Step 7: Preview the evaluation form](#step-preview).

A business outcome metric maps an evaluation question to a standard, normalized outcome. Sample forms use five industry-standard outcome metrics: customer satisfaction (CSAT), churn propensity, and successful sale for agent-handled interactions, and full and partial self-service success for self-service interactions. These outcomes roll up into analytics dashboards, where they are summarized across evaluations and broken down by agent.

### Import an evaluation form from a PDF using AI
<a name="import-form-pdf"></a>

You can import an evaluation form from any quality management system by uploading a PDF. Connect Customer uses AI to extract the sections, questions, answer options, and scoring from the PDF and create a draft evaluation form that you can review and edit.

1. On the **Evaluation forms** page, choose **Import form**, then choose **From PDF**.

   The following image shows the **Import form** menu with the **From PDF** option.  
![The Evaluation forms page showing the Import form button with the From PDF menu option highlighted.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluation-forms-import-pdf.png)

1. In the **Import evaluation form with AI** dialog:
   + **Evaluation form PDF** – Choose a PDF file (max 2 MB).
   + **Scoring method** – Choose **Points-based**, **Percentage-based**, or **Not scored**.
   + **Instructions (optional)** – Provide context to guide the extraction, for example: "This form is for outbound sales calls. Focus on upselling questions."  
![The Import evaluation form with AI dialog, showing fields for Evaluation form PDF, Scoring method, and Instructions.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluation-forms-import-pdf-dialog.png)

1. Choose **Import**. The import typically completes within one minute.

1. After the import completes, the form appears as a draft. Open it to review that the sections, questions, and scoring were extracted correctly.

1. Edit the form as needed, then activate it.

### Create a blank form and set a title
<a name="create-blank"></a>

The following steps explain how to create a blank evaluation form (or duplicate an existing form) and set a title, then build it up using the remaining steps in this topic.

1. On the **Evaluation forms** page, choose **Create new form**, choose **Create manually**, and then choose **Create**.

   —or—

   Select an existing form and choose **Duplicate**.

1. Enter a title for the form, such as *Sales evaluation*, or change the existing title. Add any tags to the form for controlling access to the form (see [ Set up tag-based-access controls on performance evaluations](https://docs.aws.amazon.com/connect/latest/adminguide/tag-based-access-control-performance-evaluations.html)) When finished, choose **Ok**.   
![The evaluation forms page, the set form title section.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-title.png)

   The following tabs appear at the top of the evaluation form page:
   + **Sections and questions**. Add sections, questions, and answers to the form.
   + **Scoring**. Enable scoring on the form. You can also apply scoring to sections or questions.

1. Choose **Save** at any time while creating your form. After you save, you can navigate away from the page and return to the form later.

1. Continue to the next step to add sections and questions.

### Import an evaluation form from another instance
<a name="import-form-json"></a>

You can export an evaluation form from one Connect Customer instance (say a test instance) and import it into another instance (say a production instance).

**To import an evaluation form from JSON**

1. While viewing an existing evaluation form, choose **Actions**, **Export as JSON**.  
![The evaluation form page, the export as json action.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluation-forms-export-json.png)

1. Open the instance where you want to import this form.

1. On the **Evaluation forms** page, choose **Import form**. Choose **Choose File** to upload the previously exported JSON, then choose **Import**.  
![The evaluation forms page, the import form action.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluation-forms-import-json.png)

The form is created including questions, instructions, answers, scoring, and automation configuration. Instance-specific settings such as rule categories and tags are not present in the exported file.

## Step 2: Add sections and questions
<a name="step-sections"></a>

1. While on the **Sections and questions** tab, add a title to the section 1, for example, *Greeting*.   
![The evaluation form page, the sections and queues tab.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-greetingtitle.png)

1. Choose **Add question** to add a question. 

1. In the **Question title** box, enter the question that will appear on the evaluation form. For example, *Did the agent state their name and say they are here to assist?*   
![The evaluation form page, the question title box.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-greetingquestion1.png)

1. In the **Instructions to evaluators** box, add information to help the evaluators or generative AI to answer the question.

   For example, for the question *Did the agent try to validate the customer identity?* you might provide additional instructions such as, *The agent is required to always ask a customer their membership ID and postal code before addressing the customer's questions*.

1. In the **Question type** box, choose one of the following options to appear on the form:
   + **Single selection**: The evaluator can choose from a list of options, such as **Yes**, **No**, or **Good**, **Fair**, **Poor**.
   + **Multiple selection**: The evaluator can choose multiple answers from a list of options, such as list of products that the customer was interested in purchasing, or non-compliant agent behaviours. 
   + **Text field**: The evaluator can enter free form text. 
   + **Number**: The evaluator can enter a number from a range that you specify, such as 1-10. 
   + **Date**: The evaluator can choose a date as an answer. 

1. Continue to the next step to add answers.

## Step 3: Add answers
<a name="step-answers"></a>

1. On the **Answers** tab, add answer options that you want to display to evaluators, such as **Yes**, **No**.

1. To add more answers, choose **Add option**. 

   The following image shows example answers for a **Single selection** question.  
![The Answers tab, the "Add option" command.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-greetingquestion1-answer.png)

   The following image shows an answer range for a **Number** question.  
![The Answers tab, the Min value and Max value boxes.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-questionscoring4.png)

1. You can also mark a question as optional. This enables managers to skip the question (or mark it as **Not applicable**) while performing an evaluation.   
![The option to mark a question "not applicable".](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-questionscoring-not-applicable.png)

## Step 4: Conditionally enable questions
<a name="step-conditionally-enable-questions"></a>

Evaluation forms can have questions that are conditionally enabled or disabled, based on answers to other questions. For example, you can configure a follow-up question to appear in the form only if it is needed.

1. Choose a question that needs a follow-up question. The question type must be **Single selection** or **Multiple selection**, and it must not be an optional question (do not select the ** Optional question** checkbox).

   For example, in the following image, question 1.1 is *What was the reason for the call?* and the **Optional question** checkbox is not selected.   
![The Question type is Single selection and the Optional question checkbox is not selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/conditionalquestions1.png)

1. Add a follow-up question and now select the **Optional question** checkbox.

   In the following image, the follow-up question is question 1.2 *Did the agent check if the customer attempted new account registration online?* and the **Optional question** checkbox is selected.   
![A follow up question, and the Optional question checkbox is selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/conditionalquestions2.png)

1. Choose the **Conditionally enable question** tab and then turn on **Conditional question**. The toggle is shown in the following image.   
![The Conditionally enable question tab, the Conditional question toggle.](https://docs.aws.amazon.com/connect/latest/adminguide/images/conditionalquestions3.png)

1. Configure the follow-up question to be enabled only if answer to question 1.1. *What was the reason for the call?* is **New account registration**. These options are shown in the following image.  
![The Conditional question is one of Other.](https://docs.aws.amazon.com/connect/latest/adminguide/images/conditionalquestions4.png)

   With this configuration, the follow-up question *Did the agent check if the customer attempted new account registration online?* is dynamically added to the form only if the answer to *What was the reason for the call?* is **New account registration**. In all other cases this question is not present in the form and does not need to be answered.

1. To verify that this configuration works as expected, use the **Preview** action. 

Following are a few things to keep in mind when creating conditional questions:
+ When a question is conditionally enabled, it is by default disabled.
+ When a question is conditionally disabled, it is by default enabled.
+ You can only use **Single selection** or ** Multiple selection** questions to conditionally enable or disable other questions. The question cannot be optional.
+  You can choose one or more answer options to trigger the condition of a conditional question. 

**Note**  
If generative AI-powered automation is enabled on a question that is conditionally enabled, then the use of generative AI on that question counts towards the usage limit of questions that can be evaluated on a contact using generative AI. It counts even if the question was conditionally disabled.  
For the default limit of the **Number of evaluation questions that can be answered automatically on a contact using generative AI**, see [Conversational analytics service quotas](amazon-connect-service-limits.md#contactlens-quotas). 

## Step 5: Assign scores and ranges to answers
<a name="step-assignscores"></a>

1. Navigate to the top of the form. Choose the **Scoring** tab, and then select the **Enable scoring** checkbox.  
![The evaluation forms page, the scoring tab, the Enable scoring checkbox.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-enablescoring.png)

   This enables scoring for the entire form. You can also use it to add ranges for answers to **Number** question types.

1. For **Scoring mode**, choose one of the following options:
   + **Percentage** – Calculate scores as percentages using weighted sections or questions.
   + **Point-based** – Calculate scores using points assigned to answer options.
**Important**  
We recommend creating a new evaluation form rather than switching the scoring mode on an existing form. Changing the scoring mode resets all previously configured scoring values, and historical evaluations completed with the previous scoring mode cannot be directly compared with evaluations using the new mode.  
![The scoring method section showing Percentage and Point-based options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-scoring-mode.png)

### Step 5.1: Percentage-based scoring
<a name="step-assignscores-percentage"></a>

If you selected **Percentage** scoring mode, follow these steps to configure scoring for your evaluation form.

1. Return to the **Sections and questions** tab. You can assign scores to **Single selection**, **Multiple selection**, and add ranges for **Number** question types.  
![The Sections and questions tab, the scoring tab specific to the question.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-scoring-feature.png)

1. When you create a **Number** type question, on the **Scoring** tab, choose **Add range** to enter a range of values. Indicate the worst to best score for the answer.

   The following image shows an example of ranges and scoring for a **Number** question type.  
![The Scoring tab specific to the question, the answer ranges.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-questionscoring5.png)
   + If the agent interrupted the customer 0 times, they get a score of 10 (best).
   + If the agent interrupted the customer 1-4 times, they get a score of 5.
   + If the agent interrupted the customer 5-10 times, they get a score of 1 (worst).

1. For **Multiple selection** questions, assign a score value (0-10) to each option. When multiple options are selected, the total score is the sum of selected options' scores, capped at 10.

1. (Optional) Configure **Automatic fail** for an answer option. You can choose to apply automatic fail to the section, the subsection, or the entire form. When the evaluator selects this answer during an evaluation, the score for the affected scope is set to zero.  
![The Automatic fail option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automaticfail.png)

1. (Optional) Exclude individual questions or entire sections from scoring. When a question or section is excluded, it is automatically assigned a weight of 0%, similar to a non-scorable question. The remaining weight is redistributed among the other scored items.  
![Percentage scoring mode showing excluded questions with 0% weight.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-percentage-exclude-scoring.png)

1. After you assign scores to all the answers, choose **Save**.

**Updating existing forms with multiple selection questions**  
If you have existing evaluation forms that were created with multiple selection questions before scoring support was added, you will receive a validation error when creating a new version or activating the form. To resolve this, follow these steps:  
Open the evaluation form and navigate to the multiple selection question.
Choose the **Scoring** tab for the question.
Do one of the following:  
Assign score values to each answer option (0-10), or
Select the **Exclude from scoring** checkbox to remove the question from the scoring calculation.
Choose **Save** and then activate the form.

### Step 5.2: Point-based scoring
<a name="step-assignscores-pointbased"></a>

If you selected **Point-based** scoring mode, follow these steps to configure scoring for your evaluation form.

1. Return to the **Sections and questions** tab. For each question, choose the **Scoring** tab and assign point values to each answer option. Point values can range from **0 to 100**.

   The following image shows an example of point values assigned to a **Single selection** question.  
![The Scoring tab for a single selection question with point values (0 to 100).](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-single-select.png)

1. For **Number** type questions, choose **Add range** to define answer ranges and assign a point value to each range.  
![The Scoring tab for a numeric question with point values assigned to ranges.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-numeric-ranges.png)

1. For **Multiple selection** questions, assign point values to each option. When multiple options are selected, their point values are summed. Optionally, select **Set cap** to configure a maximum point value cap for the question.  
![The Scoring tab for a multiple selection question with point values and Set cap option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-multi-select.png)

1. (Optional) Configure bonus options or bonus questions. With bonus points, you can award extra credit without increasing the maximum possible score.
   + **Bonus options** – An individual answer option that awards extra points on top of the question's maximum base score. When a bonus option is selected, the earned points can exceed the question's normal maximum. Bonus options are only supported on single selection and numeric questions.
   + **Bonus questions** – An entire question that does not contribute to the maximum possible score. The earned points from a bonus question are added to the total, but the question's maximum points are not counted in the base total. Bonus questions cannot have automatic fail options.  
![The Scoring tab showing the Bonus checkbox for an answer option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-bonus-option.png)  
![The Scoring tab showing the Bonus question checkbox.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-bonus-question.png)

1. (Optional) Configure automatic fail. When an automatic fail option is selected during an evaluation, the score for the affected scope is set to zero. You can choose to apply automatic fail to the **Section** or **Entire form**. Automatic fail is supported on single selection, numeric, and multiple selection questions. Bonus questions and bonus options cannot have automatic fail.  
![The Automatic fail option with scope selection.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-automatic-fail.png)

1. (Optional) Exclude individual questions or entire sections from scoring. Excluded items do not contribute to the total score or the maximum possible score.  
![The Exclude from scoring checkbox on a question.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-exclude-scoring.png)

1. After you assign scores to all the answers, choose **Save**.

1. When you're finished assigning scores, continue to the next step to automate the answer of certain questions, or continue to [preview the evaluation form](#step-preview).

### Step 5.3: Assign performance thresholds
<a name="step-assignscores-performance-thresholds"></a>

With performance thresholds, you can classify evaluation results into categories such as "Needs Improvement" or "Exceeds Expectations" based on score thresholds. This feature is supported in both percentage-based and point-based scoring modes.

You can configure performance thresholds at the form level, section level, or question level.

Performance thresholds are not inherited. If you set thresholds at the form level, those thresholds apply only to the overall form score. Sections and questions do not automatically inherit the form-level thresholds. You must explicitly configure thresholds at each level where you want them to apply.

![The Performance categories section with threshold settings.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-performance-categories.png)


## Step 6: Enable automated evaluations
<a name="step-automate"></a>

With Connect Customer, you can automatically answer questions within evaluation forms (for example, did the agent adhere to the greeting script?) using insights and metrics from conversational analytics. Automation can be used to:
+ **Assist evaluators with performance evaluations**: Evaluators receive automated answers to questions on evaluation forms while performing evaluations. Evaluators can override automated answers before submission.
+ **Automatically fill and submit evaluations**: Administrators can configure evaluation forms to automate responses to all questions within an evaluation form and automatically submit evaluations for up to 100% of customer interactions. Evaluators can edit and re-submit evaluations (if needed).

The ways of automation vary by whether you are evaluating the agent interaction or automated interaction (for example, self-service while interacting with a Lex bot or AI agent). You can choose between agent and automated interaction by choosing the **Additional settings**, under **Contact interaction type**.

Both for assisting evaluators, and for automated submission of evaluations, you need to first set up automation on individual questions within an evaluation form. Connect Customer provides three ways of automating evaluations:
+ **Contact categories**: *Single selection* questions (for example, did the agent properly greet the customer (Yes/ No)?), and *Multiple selection* questions (for example, what parts of the greeting script did the agent state correctly?) can be automatically answered using contact categories defined with rules. For more information, see [Create conversational analytics rules using the Connect Customer admin website](build-rules-for-contact-lens.md).
+ **Generative AI**: Both *Single selection* and *Text field* questions can be automatically answered using generative AI.

  For information about automating evaluations of self-service (automated) interactions, see [Performance evaluations of self-service interactions in Connect Customer](performance-evaluations-automated-interactions.md).
+ **Metrics**: *Numeric* questions (for example, what was the longest that the customer was put on hold?) can be automatically answered using metrics such as longest hold time, sentiment score.

Following are examples of each type of automation for each type of question.

**Example automation for a Single selection question using conversational analytics categories**
+ The following image shows that the answer to the evaluation question is yes when conversational analytics has categorized the contact with a label **ProperGreeting**. To label contacts as **ProperGreeting**, you must first set up a rule that detects the words or phrases expected as part of a proper greeting, for example, the agent mentioned "Thank you for calling" in the first 30 seconds of the interaction. For more information, see [Automatically categorize contacts](rules.md).  
![A question section, the automation tab with conversational analytics categories.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation1.png)

  For information about setting up contact categories, see [Automatically categorize contacts](rules.md).

**Example automation for an *optional* Single selection question using contact categories**
+ The following image shows example automation of an optional Single selection question. The first check is whether the question is applicable or not. A rule is created to check whether the contact is about opening a new account. If so, the contact is categorized as **CallReasonNewAccountOpening**. If the call is not about opening a new account, the question is marked as **Not Applicable**.

  The subsequent conditions run only if the question is applicable. The answer is marked as **Yes** or **No** based on the contact category **NewAccountDisclosures**. This category checks whether the agent provided the customer with disclosures about opening a new account.  
![A question section, the automation tab.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation1a.png)

  For information about setting up contact categories, see [Automatically categorize contacts](rules.md).

**Example automation for an *optional* Single selection question using Generative AI**
+ The following image show example automation using Generative AI. Generative AI will automatically answer the evaluation question by interpreting the question title and evaluation criteria specified in the instructions of the evaluation question, and using it to analyze the conversation transcript. Using complete sentences to phrase the evaluation question and clearly specifying the evaluation criteria within the instructions improves accuracy of generative AI. For information, see [Evaluate agent performance in Connect Customer using generative AI](generative-ai-performance-evaluations.md).  
![A question section, the generative AI conversational analytics option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation-genai.png)

**Example automation for a Multiple selection question using conversational analytics categories**
+ Multiple selection questions can be used to capture answer reasoning for a single select question. It can also be used to trigger conditional questions, by checking for customer scenarios, such as call reasons. The following example shows how you can use rules that capture customer call reasons to automatically fill answers to a multiple selection question. Unlike single select questions, all of the conditions are executed sequentially to answer a multiple selection question. In the following example, if the categories **StatusCheck** and ** ChangeExistingRequest** are both present on the contact, then the answer would be both "Checking status of existing service request" and "Changing a service request".  
![A question section, the automation tab with conversational analytics categories.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation1b.png)

  For information about setting up contact categories, see [Automatically categorize contacts](rules.md).

**Example automation for a Numeric question**
+ If the agent interaction duration was less than 30 seconds, score the question as a 10.   
![A question section, the scoring tab, a numeric question.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation2.png)
+ On the **Automation** tab, choose the metric that is used to automatically evaluate the question.  
![A question section, the automation tab, a metric to automatically evaluate the question.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation3.png)
+ You can automate responses to numeric questions using conversational analytics metrics (such as sentiment score of the customers, non-talk time percentage, and number of interruptions) and contact metrics (such as longest hold duration, number of holds, and agent interaction duration).

After an evaluation form is activated with automation configured on some of the questions, then you will receive automated responses to those questions when you start an evaluation from within the Connect Customer admin website.

**To automatically fill and submit evaluations**

1. Set up automation on every question within an evaluation form as previously described.

1. Turn on **Enable fully automated submission of evaluations** before activating the evaluation form. This toggle is shown in the following image.  
![The Enable fully automated evaluations toggle set to On.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-automation4.png)

1. Activate the evaluation form.

1. Upon activation you will be asked to create a rule in conversational analytics that submits an automated evaluation. For more information, see [Create a rule in conversational analytics that submits an automated evaluation](contact-lens-rules-submit-automated-evaluation.md). With the rule, you can specify which contacts should be automatically evaluated using the evaluation form.

### Choose a Gen AI version for automated evaluations
<a name="step-automate-genai-version"></a>

When you enable automated evaluations, Connect Customer uses generative AI to suggest answers for the automated questions on the form. The Gen AI configuration behind those suggestions improves over time as Connect Customer ships refined prompts and upgrades the underlying model. By default, a form automatically uses the latest generally available Gen AI version, so your automated evaluations benefit from these improvements without any action on your part.

**Note**  
Gen AI version selection is not available to customers on Amazon Connect Customer Basic.

If you want more control, choose the Gen AI version the form uses. On the evaluation form builder, choose the **Additional settings** tab. In the **Gen AI version** section, choose one of the following options.

![The Gen AI version section on the Additional settings tab, showing the Latest, Preview, and Specific version options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-genai-version-selector.png)


**Latest**  
Automatically upgrade to the latest Gen AI version for automating evaluations. This is the default. When Connect Customer promotes a new version to latest, forms set to **Latest** move to it automatically so you always benefit from the most recent improvements.

**Preview**  
Try automated evaluations with an upcoming Gen AI version so you can make adjustments before the preview version becomes the latest. If no version is currently in preview, the form uses the latest version.

**Specific version**  
Continue using a specific version until it reaches end of life. Choose this option for predictable automation. If your chosen version reaches end of life, the form automatically uses the latest version.

When you choose **Specific version**, choose a version from the dropdown list. Each entry shows the version name and the date it was released, and a badge indicates the version's state. The versions that are available depend on your form type and your account's enrollment in cross-Region inference. The following tables describe the available versions.

![The Specific version dropdown expanded, listing available versions with their release dates and state badges.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-genai-specific-version.png)


Versions that have reached end of life appear dimmed and cannot be selected for a new form version.

**Agent evaluation versions** — available for agent evaluation forms when your account is enrolled in cross-Region inference.


| Version | State | What changed | 
| --- | --- | --- | 
| AGENT\_EVALUATION\_2026-05-05 | Preview | Adjusts how strictly the model scores answers, to make automated suggestions less strict where earlier versions were too harsh. | 
| AGENT\_EVALUATION\_2026-04-16 | Latest | Reduces the rate of automated evaluations that fail to generate a suggested answer, so more questions receive an automated suggestion. | 
| AGENT\_EVALUATION\_2025-12-03 | Active | The first version with the model upgrade. | 

**Automated interaction (self-service) evaluation versions** — available for automated interaction evaluation forms when your account is enrolled in cross-Region inference.


| Version | State | What changed | 
| --- | --- | --- | 
| SELF\_SERVICE\_EVALUATION\_2026-04-24 | Preview | Adjusts how strictly the model scores answers, making automated suggestions less strict than the previous version. | 
| SELF\_SERVICE\_EVALUATION\_2026-03-18 | Latest | The initial Gen AI version for automated interaction evaluations. | 

**Note**  
The Gen AI versions available to you depend on your form type, your AWS Region, and your account's enrollment in cross-Region inference. If no versions are available for your form's context, the version selector does not list any versions, and the form uses the latest version that Connect Customer resolves at evaluation time.

The Gen AI version you choose is saved on the form version when you save the form, and it applies to that form version for its lifetime. You can change the selection while a form version is in **Draft**; after a form version is activated, its Gen AI version selection is fixed. To move a form to a different version, create a new form version and choose the version you want. Forms created before this feature was available do not have a selection, and Connect Customer uses the latest version for them at evaluation time.

Each Gen AI version has a state, shown as a badge in the version selector: **Latest** is the current default; **Preview** is an upcoming version you can try before it becomes the default; **Active** is a stable version that is not the default but is still available to select; and **End of life** means the version is being retired and can no longer be selected for a new form version.

When a version that one of your forms uses is approaching end of life, Connect Customer notifies you in advance through the AWS Health Dashboard and a warning banner on each affected form version's detail page. You do not need to take action to keep your evaluations running: if a form's selected version reaches end of life before you move the form, Connect Customer automatically uses the latest available version for that form's automated evaluations rather than failing them, so there are no gaps in your evaluations. We recommend that you review your form against the newer version to confirm accuracy, because a newer version can behave differently from the version your form was originally set to.

## Step 7: Preview the evaluation form
<a name="step-preview"></a>

The **Preview** button is active only after you have assigned scores to answers for all of the questions.

![The evaluation form page, the preview button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-previewbutton.png)


The following image shows the form preview. Use the arrows to collapse sections and make the form easier to preview. You can edit the form while viewing the preview, as shown in the following image.

![The preview of the evaluation form.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-previewmode.png)


## Step 8: Assign weights for final score
<a name="step-weights"></a>

When percentage-based scoring is enabled for the evaluation form, you can assign *weights* to sections or questions. The weight raises or lowers the impact of a section or question on the final score of the evaluation. This step applies only to the **Percentage** scoring mode. If you selected **Point-based** scoring, weights are not used; instead, the score is calculated from earned points versus maximum possible points.

![The evaluation form page, the scoring tab, the score weights section, the question option.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-scoring.png)


### Weight distribution mode
<a name="weight-distribution-mode"></a>

With **Weight distribution mode**, you choose whether to assign weight by section or question: 
+ **Weight by section**: You can evenly distribute the weight of each question in the section.
+ **Weight by question**: You can lower or raise the weight of specific questions.

When you change a weight of a section or question, the other weights are automatically adjusted so the total is always 100 percent.

For example, in the following image, question 2.1 was manually set to 50 percent. The weights that display in italics were adjusted automatically. In addition, you can turn on **Exclude optional questions from scoring**, which assigns all optional questions a weight of zero and redistributes the weight among the remaining questions.

![Score weights for a question.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-weightdistribution3.png)


## Step 9: Validate the evaluation form
<a name="step-validateform"></a>

Choose **Save and validate** to save the evaluation form and run it through the validation pipeline. Results appear in a side panel. Validation happens in two stages. First, the validation pipeline checks the form against the same structural and configuration rules that govern activation—for example, section and question limits, weight and scoring consistency, and unique identifiers. The pipeline reports any issues found here as **Errors**, because they would prevent the form from being activated and you must resolve them before you can proceed.

If the pipeline finds no structural **Errors** and the form contains Gen AI–automated questions, validation moves to a second stage. This stage evaluates the content of those questions against best practices for Gen AI automation. The pipeline reports anything identified here as a **Warning**. Warnings do not block activation, but we recommend addressing them to improve the quality and reliability of automated answers.

Validation checks each Gen AI–automated question against the following best practices:
+ **Question phrasing** – The question title reads as a complete question (ending in a question mark), not a statement or heading.
+ **Instructions present** – Every Gen AI–answered question includes instructions telling the AI how to evaluate and answer it.
+ **Answer option language** – Answer options use plain, everyday language with no acronyms or abbreviations.
+ **Answer option conciseness** – Answer options are short labels only, with no extra commentary or conditions.
+ **Transcript answerability** – The question can be answered from the transcript and instructions alone, without external data or system lookups.
+ **Positive action framing** – The question asks what the agent did rather than asking the AI to detect the absence of an action.
+ **Plain language** – Instructions avoid abbreviations, acronyms, and company-specific jargon.
+ **Spelling** – Question titles, instructions, and answer options are free of misspelled words.
+ **No external system references** – Instructions don't reference actions or states in external systems the AI can't see in the transcript.
+ **No non-textual cues** – Questions don't require assessing audio-only qualities (volume, pitch, speaking speed, vocal tone). Text-assessable qualities like professionalism or empathy are fine.
+ **No PII references** – Questions and instructions don't contain specific PII values. Evaluating the agent's PII-handling behavior is fine.

**Note**  
Gen AI validation is rate limited per Connect Customer instance: no more than 3 Gen AI validations can run in parallel, and no more than 30 can run per hour. If you exceed either limit, an error message appears in the side panel. Try again later. These limits don't affect structural validation.

**To validate an evaluation form**

1. Choose **Save**, **Save and validate**.  
![The Save and validate option in the Save menu.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-save-and-validate-ingress.png)

1. When validation completes, the results appear at the top of the form:
   + If no recommendations are found, a green banner appears at the top of the form confirming that validation passed.
   + If recommendations are found, they are listed in the side panel, grouped as **Errors** or **Warnings**.  
![The validation results side panel showing errors and warnings.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-validation-side-panel.png)

1. You can close the side panel at any time. To reopen it, either choose the **Findings** button next to a question, or choose **Save and validate** again.  
![The Findings button next to a question.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-findings-button.png)

1. On the side panel, you can mark each finding as resolved after you have addressed it. Choose the **Pending resolve** filter to focus on the findings that still need attention.  
![The side panel with findings and the Pending resolve filter.](https://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-resolve-findings.png)

**Note**  
Marking a finding as resolved only visually hides it on the panel so you can clearly see which findings are left to address. It does not re-run validation or change the form's activation state.

## Step 10: Activate an evaluation form
<a name="step-activateform"></a>

Choose **Activate** to make the form available to evaluators. Evaluators will no longer be able to choose the previous version of the form from the dropdown list when starting new evaluations. For any evaluations that were completed using previous versions, you will still be able to view the version of the form on which the evaluation was based on.

**Important**  
After you activate a new version, evaluators can no longer start new evaluations with the previous version.

If you are still working on setting up the evaluation form and want to save your work at any point you can choose **Save**, **Save draft**.

If you want to check whether the form has been correctly set up, but not activate it, select **Save**, **Save and validate**.