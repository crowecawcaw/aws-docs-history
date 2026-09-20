

# How to test Amazon Connect Talent
<a name="getting-started-test"></a>

After you set up your instance, test Amazon Connect Talent end-to-end by creating an evaluation and sending it to yourself or your team.

## Optional prerequisites
<a name="getting-started-test-prerequisites"></a>

Before you test Amazon Connect Talent, you can complete the following optional tasks:
+ **Upload your knowledge base** – Amazon Connect Talent uses your knowledge base to understand your company values and the key competencies you want to assess. This informs how evaluations are tailored to your organization. For more information, see [Manage knowledge bases](https://docs.aws.amazon.com/talent/latest/adminguide/manage-knowledge-bases.html).
+ **Connect your applicant tracking system (ATS)** – Amazon Connect Talent imports all the jobs you're currently hiring for. If your ATS isn't connected yet, you can upload or describe your job directly during evaluation creation. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html).

## Build and test an evaluation
<a name="getting-started-test-build"></a>

This end-to-end walkthrough covers creating, publishing, sending, and reviewing a test evaluation:

1. **Create an evaluation** – Choose a role and generate a tailored evaluation. For more information, see [Create an evaluation](managing-evaluations.md#create-candidate-evaluation).

1. Publish the evaluation – finalize and publish it.

1. **Send to candidates** – Navigate to the published evaluation and choose **Send to candidates**. Enter the email addresses of yourself or your team members to send test evaluations.
**Tip**  
Sending a test evaluation to the same email address will overwrite your previous results. Some email clients support plus addressing, which lets you create variations of your email to generate separate candidate records. Add `+` followed by any number or text before the `@` symbol — for example, `yourname+1@yourcompany.com`, `yourname+2@yourcompany.com`. Each variation creates a separate candidate record in Amazon Connect Talent, but all emails deliver to the same inbox. Check whether your email client supports plus addressing before relying on this approach.

1. Review results – after your testers complete their evaluations, review their results to understand how Amazon Connect Talent evaluates and scores candidates. For more information, see [How scoring works](how-scoring-works.md).