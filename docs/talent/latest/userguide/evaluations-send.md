

# Sending evaluations to candidates
<a name="evaluations-send"></a>

This page covers how to send evaluation invitations to candidates in Amazon Connect Talent.

An evaluation invitation is an email that Amazon Connect Talent sends to a candidate with a link to complete their evaluation. The email contains instructions and a unique link that takes the candidate directly to their evaluation. For more information about what the candidate sees, see [Candidate experience](candidate-experience.md).

**Important**  
Before Amazon Connect Talent can send evaluation invitation emails to candidates, your Amazon Simple Email Service (Amazon SES) account must be moved out of sandbox mode. Evaluations are not sent to candidates until this step is complete. For more information, see [Move Amazon SES out of sandbox mode](https://docs.aws.amazon.com/talent/latest/adminguide/getting-started.html#getting-started-ses).

## Manually send or resend evaluations
<a name="send-eval-manual"></a>

You can send an evaluation to any candidate by email directly from Amazon Connect Talent. Before ATS integrations are available, this is how you deliver evaluations to candidates.

To send an evaluation:

1. In the sidebar, choose **Evaluations**.

1. Choose the published evaluation you want to send.

1. Choose **Send to candidates**.

1. Enter the candidate's email address and send.

Amazon Connect Talent checks whether a candidate record already exists for that email address and role. If one exists, the evaluation is sent to the existing candidate. If one doesn't exist, Amazon Connect Talent creates a new candidate record. Amazon Connect Talent also checks for an existing active attempt and warns you before it resends, so you don't send a duplicate invitation.

### When to resend
<a name="send-eval-when-resend"></a>

You may need to resend an evaluation in the following situations:
+ **Expired invitations** – Evaluation invitations expire after 7 days. If a candidate contacts you because their invitation has expired, resend the evaluation using the preceding steps.
+ **Technical difficulties** – If a candidate experiences a technical difficulty during their evaluation, Amazon Connect Talent instructs them to contact their recruiter for help. Resend the evaluation using the preceding steps. If the candidate already completed their assessments and then experiences a technical difficulty during the AI-led interview, their assessment progress and scores are saved. The candidate must restart the AI-led interview. For more information, see [Assist candidates with technical difficulties](candidate-experience.md#candidate-experience-technical-difficulties).
+ **Rescheduling** – If a candidate needs to reschedule and ends the interview early, resend the evaluation using the preceding steps. If the candidate already completed their assessments, their assessment progress and scores are saved. The candidate must restart the AI-led interview.

## Automated evaluation invitations with ATS integration
<a name="send-eval-automated"></a>

**Note**  
ATS integrations are not available at launch. Support for ATS integrations is coming soon. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html) in the *Amazon Connect Talent Administrator Guide*.

With an ATS integration, you can link evaluations to application stages from your ATS. When a candidate reaches the linked application stage, Amazon Connect Talent automatically sends them an evaluation invitation.