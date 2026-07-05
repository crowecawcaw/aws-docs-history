# Evaluate agent performance in Connect Customer using generative AI

###### Note

**Powered by Amazon Bedrock**: AWS implements automated abuse
detections. Because generative AI features in Contact Lens are built on Amazon Bedrock,
users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety,
security, and the responsible use of artificial intelligence (AI).

Managers can specify their evaluation criteria in natural language, and use
generative AI for automating evaluations of up to 100% of customer interactions.
Generative AI can enable you to automate evaluations of additional agent behaviors (for
example, was the agent able to resolve the customer's issue?), enabling managers to
comprehensively monitor and improve regulatory compliance, agent adherence to quality
standards and sensitive data collection, while reducing the time spent on evaluating
agent performance. Along with answers, you are also provided with context and
justification, and references to specific points in the transcript that you can use to
provide agent coaching.

You can use generative AI to assist managers with filling evaluations or use it to
automatically fill and submitting evaluations. For more information about setting up
automated evaluations, see [Step 6: Enable automated evaluations](create-evaluation-forms.md#step-automate "create-evaluation-forms.md#step-automate").

Evaluations questions are answered using generative AI by interpreting the question
title and evaluation criteria specified within the instructions to evaluators associated
with each question, and using these to analyze the conversation transcript. For more
information, see [Step 2: Add sections and questions](create-evaluation-forms.md#step-sections "create-evaluation-forms.md#step-sections").

## Process to automate evaluations using generative AI

The following is the overview of the automation process:

1. Get a high-level understanding of which of the evaluation questions should
   be answered with generative AI by reading [Guidelines to improve generative AI accuracy](#guidelines-to-improve-generative-ai-accuracy "#guidelines-to-improve-generative-ai-accuracy").
2. Assign permissions to select users within your quality management team to
   use Ask AI assistant. These users will start seeing the Ask AI button next
   to each question, while performing evaluations and can use that to get
   answer recommendations. These users can provide feedback on which questions
   are receiving accurate answers using generative AI. For more information,
   see [Assign security profile permissions for performance evaluations and coaching](evaluation-and-coaching-permissions.md "evaluation-and-coaching-permissions.md").
3. To improve accuracy, you can provide additional evaluation criteria within
   [instructions to evaluators](create-evaluation-forms.md#step-sections "create-evaluation-forms.md#step-sections"). For
   more information, see [Guidelines to improve generative AI accuracy](#guidelines-to-improve-generative-ai-accuracy "#guidelines-to-improve-generative-ai-accuracy").
4. Once you have a good understanding of which questions can be accurately
   answered with generative AI, you can do a broader rollout by pre-configuring
   on the evaluation form, whether a question will receive an automated answer
   using generative AI.
5. Once you have setup automation, any user performing evaluations using the
   evaluation form will get automated generative AI answers to the
   pre-configured questions (without requiring additional permissions). For
   more information, see [Step 6: Enable automated evaluations](create-evaluation-forms.md#step-automate "create-evaluation-forms.md#step-automate").
6. You can setup automation such that an evaluator first reviews the
   generative AI answers before submission or you can automatically fill and
   submit evaluations.

## Use Ask AI to get generative AI answer recommendations

1. Log into Connect Customer with a user account that has [permissions to perform
   evaluations](evaluation-and-coaching-permissions.md "evaluation-and-coaching-permissions.md") and [ask
   AI assistant](evaluation-and-coaching-permissions.md "evaluation-and-coaching-permissions.md").
2. Choose the **Ask AI** button below a question to receive
   a generative AI-powered recommendation for the answer, along with context
   and justification (reference points from the transcript that were used to
   provide answers).

   1. The answer will get automatically selected based on the
      generative AI recommendation, but can be changed by the user.
   2. You can get generative AI-powered recommendations by choosing
      **Ask AI** for up to 10 questions per contact.
      For more information, see [Contact Lens service quotas](amazon-connect-service-limits.md#contactlens-quotas "amazon-connect-service-limits.md#contactlens-quotas").

3. You can choose the time associated with a transcript reference to be
   directed to the point in the conversation

![Generative AI-powered recommendations while evaluating agent performance.](images/get-generative-ai-powered-recommendations-performance.png)

## Provide additional criteria for answering evaluation form questions using generative AI

While configuring an evaluation form, you can provide criteria for answering
questions within the **instructions to evaluators**
associated with each evaluation form question. Apart from driving consistency in
evaluations by evaluators, these instructions are also used to provide generative
AI-powered evaluations.

![New account opening scorecard.](images/provide-criteria-for-answering-evaluation-form-questions.png)

## Set up automated evaluations using generative AI on the evaluation form

You can pre-configure on an evaluation form whether a question will be
automatically answered using generative AI. Then, if you start an evaluation using
the evaluation form on the Connect Customer UI, answers to these questions will get
automatically filled using generative AI (without requiring you to choose Ask AI).
You can also use generative AI to automatically fill and submit evaluations. For
automatically submitted evaluations, you can use generative AI to answer up to 10
questions per contact (see [Contact Lens service quotas](amazon-connect-service-limits.md#contactlens-quotas "amazon-connect-service-limits.md#contactlens-quotas")). Note that this limit does not apply to
automation using contact categories or metrics (for example, longest
hold duration, etc.).

To learn more about setting up automated evaluations using generative AI, see
[Guidelines to improve generative AI accuracy](#guidelines-to-improve-generative-ai-accuracy "#guidelines-to-improve-generative-ai-accuracy").

## Set up generative AI-powered evaluations in non-English languages

By default, if you do not set the language of an evaluation form, the generative
AI model automatically detects the language of your evaluation form questions and
tries to provide answers in the same language, if the AI model understands that
language. By default, generative AI answer justifications are typically provided
in English.

To consistently receive both AI-generated answers and answer justifications in
your preferred language, you can set the language of an evaluation form, choosing from
**English**, **Spanish**,
**Portuguese**, **French**,
**German**, **Italian**,
**Chinese**, **Japanese**,
and **Korean**.
By explicitly setting the language of an evaluation, you can also perform cross-language
evaluations, where generative AI fills a evaluation form in English, even when the
conversation transcript is in another language, say Spanish. This enables multilingual
contact centers to use a standardized evaluation framework across languages.

To set the language of the evaluation form:

1. Select the **Additional settings**
   tab while creating or updating an evaluation form.
2. Choose **Form language** from the dropdown.
3. Ensure your form's questions, instructions and answer choices are in the same
   language as the selected **Form language**, for optimal
   AI performance.

![The evaluation form page, the Additional settings tab.](images/evaluationforms-languageexample1.png)

## Guidelines to improve generative AI accuracy

###### Selecting questions for getting generative AI recommendations

1. Use generative AI to respond to questions that can be answered using
   information from the conversation transcript, without the need to validate
   information through third-party applications such as CRM systems.
2. Using generative AI to answer questions requiring numeric responses, such
   as "How long did the agent interact with the customer?" is not recommended.
   Instead, consider [setting up automation](create-evaluation-forms.md#step-automate "create-evaluation-forms.md#step-automate")
   for such evaluation form questions using Contact Lens or contact
   metrics.
3. Avoid using generative AI to answer highly subjective questions, for
   example, "Was the agent attentive during the call?"
4. Don't ask questions that require information that cannot be known from the
   conversation transcript alone. For example, generative AI cannot analyze the
   agent's screen recording, access external systems such as a CRM, or evaluate
   across multiple contacts. Generative AI also cannot determine the agent's or
   customer's tone of voice.
5. If a question measures more than one thing, split it into multiple simpler
   questions. For example, instead of "Did the agent exhibit active listening?",
   ask separate questions such as "Did the agent understand the customer's
   problem the first time without the need for the customer to repeat
   themselves?" and "Did the agent summarize the issue after the customer
   explained it?". You can also use [conditionally enabled questions](create-evaluation-forms.md#step-conditionally-enable-questions "create-evaluation-forms.md#step-conditionally-enable-questions") so that a follow-up question is
   only evaluated when a triggering question has a particular answer.

###### Improving phrasing of questions and associated instructions

1. Use complete sentences to word questions, for example, replacing
   _ID validation_ with "Did the agent attempt to
   validate the customer's identity?" enables the generative AI to better
   understand the question.
2. It is recommended that you provide detailed criteria for answering the
   question within the **instructions to
   evaluators,** especially if its not possible to answer the
   question based on the question text alone. For example, for the question
   "Did the agent try to validate the customer identity?" you may want to
   provide additional instructions such as, _The agent is required to
   always ask a customer their membership ID and postal code before
   addressing the customer's questions_.
3. If answering a question requires knowledge of some business specific
   terms, then specify those terms in the instruction. For example, if the
   agent needs to specify the name of the department in the greeting, then list
   the required department name(s) that the agent needs to state as part of the
   **instructions to evaluators** associated
   with the question.
4. If possible, use the term 'agent' instead of terms like 'colleague',
   'employee', 'representative', 'advocate', or 'associate'. Similarly use the
   term 'customer', instead of terms like 'member', 'caller', 'guest', or
   'subscriber'.
5. Only use double quotes in your instruction if you want to check for exact
   words being spoken by the agent or the customer. For example, If the
   instruction is to check for the agent saying `"Have a nice day"`,
   then the generative AI will not detect _Have a nice
   afternoon_. Instead the instruction should say: `The
 agent wished the customer a nice day`.
6. Avoid using acronyms in questions and instructions. For example, instead of
   "Did the agent follow CFPB guidelines?", spell out the full term so the
   generative AI can interpret it correctly.
7. Avoid using proper nouns that are likely to be misspelled in the
   conversation transcript. For example, a product name such as
   _O2 Pay_ might be transcribed differently, which can
   prevent the generative AI from matching it.
8. Avoid vaguely phrased questions, such as "Did the agent use appropriate
   language?". Be specific, for example, "Did the agent use profanity?".
9. Phrase questions so that it is clear who is being evaluated. For example,
   "Did the agent avoid the usage of profanity?" can be interpreted as asking
   whether profanity occurred anywhere in the conversation, so the answer becomes
   "No" even when only the customer used profanity. To evaluate the agent's own
   conduct, phrase the question as "Did the agent use profanity?".
10. Avoid negatively phrased questions, such as "Did the agent miss the
    greeting?". Negative phrasing can cause the generative AI to hallucinate
    evidence when providing references. Instead, phrase the question positively,
    for example, "Did the agent greet the customer?".
11. In your instructions, explain when the answer is **Not Applicable** (N/A). For example, _The answer is
    N/A if the call resulted in a transfer_.
12. Avoid long verbatim scripts in your instructions, such as checking that the
    agent said `"Thank you for calling ABC Bank. How may I assist
 you?"`. Minor transcription differences mean the generative AI is
    unlikely to match the full script.
13. Provide examples that cover the different scenarios your agents handle, not
    only the standard call flow. If your agents handle situations such as
    callbacks, escalations, or transfers, include examples in the
    **instructions to evaluators** that reflect
    those situations. For example, a question that asks whether the agent provided
    a timeline might accept "It typically takes 3 to 5 business days" on a standard
    call, but should also include an example of acceptable phrasing for a callback,
    such as "I'll call you back within 30 minutes with an update". Questions that
    include only standard-flow examples are more likely to be answered
    inconsistently on non-standard contacts.
14. Give extra attention to the instructions for questions that automatically
    fail an evaluation, because a single failing answer affects the entire
    evaluation score. Provide the most detailed criteria for these questions,
    including edge cases and non-standard scenarios. For more information about
    scoring, see [Step 5: Assign scores and ranges to answers](create-evaluation-forms.md#step-assignscores "create-evaluation-forms.md#step-assignscores").

###### Improving answer options

1. Use simple and short answer options, such as **Yes**, **No**, and
   **Partial**.
2. Enable the **Optional question** setting when
   there are situations where the question is not applicable. This lets
   evaluators skip the question or mark it as **Not
   Applicable**.
3. Avoid spelling errors and special characters in answer options, because they
   can reduce the accuracy of generative AI answers.
4. Avoid using too many answer options. For example, for the question "How was
   the customer experience?", a long list of options such as Great, Good, OK,
   Poor, Very Poor, and Horrible reduces accuracy. Use a smaller set of
   distinct options instead.
5. Avoid long text in answer options, because it might be incorrectly
   reproduced by the generative AI model.

The following example shows a generative AI-answered question that follows these
guidelines. The question title is a complete sentence, the instructions to evaluators
define each answer option and explain the Not Applicable scenario, and the answer
options are short.

![An evaluation form question configured with a full-sentence title, detailed instructions to evaluators, and short Yes and No answer options with the Not Applicable option enabled.](images/evaluationforms-genai-question-example.png)
