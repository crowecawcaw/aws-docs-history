

# Candidate experience
<a name="candidate-experience"></a>

Candidates experience a mobile-first, employer-customized evaluation process. They can complete their evaluation—all from their mobile device through a seamless web experience. AI agents are available around the clock, so candidates can complete interviews whenever it's convenient for them, not just during business hours.

**Topics**
+ [Receive the invitation email](#candidate-experience-invitation)
+ [The candidate journey](#candidate-experience-journey)
+ [Audio and device setup](#candidate-experience-audio)
+ [Languages and accessibility](#candidate-experience-languages-accessibility)
+ [How a candidate opts out](#candidate-experience-opt-out)
+ [Assist candidates with technical difficulties](#candidate-experience-technical-difficulties)
+ [Supported browsers](#candidate-experience-supported-browsers)

## Receive the invitation email
<a name="candidate-experience-invitation"></a>

A candidate receives an email invitation to complete their evaluation. The email includes a button and a link to start the evaluation.

The invitation comes from a sender address that includes your instance name, in the following form:

`noreply@{{instance-name}}.email.connect.aws`

When the candidate chooses the button or opens the link, Amazon Connect Talent launches the browser-based evaluation experience described in this chapter.

## The candidate journey
<a name="candidate-experience-journey"></a>

A candidate receives an email invitation to complete an evaluation for a specific role. Opening the link launches the branded experience. Amazon Connect Talent guides the candidate through the following steps:

1. **Review the role and job details** – The candidate sees the position details (the job description added by the recruiter) and a role overview (a brief AI-generated summary of the role). The candidate can choose **Start evaluation** to proceed or **Opt out** to decline the entire evaluation.

1. **Review and accept disclosures** – The candidate reviews any disclosures configured by your organization and chooses **Accept and continue** to proceed. For more information about adding disclosures, see [Configure disclosures](https://docs.aws.amazon.com/talent/latest/adminguide/configure-disclosures.html) in the *Amazon Connect Talent Administrator Guide*.

1. **Review the evaluation overview** – The candidate sees a list of all steps in the evaluation, including each assessment and the AI-led interview (if applicable). A progress indicator tracks completion as the candidate moves through the steps.

1. **Complete assessments (if included)** – For each assessment, the candidate reviews an instructions page that explains what the assessment measures and how it works, then completes the assessment. Assessments have no time limit, and the candidate's progress is shown at the top.

1. **Complete the AI-led interview (if included)** – The candidate reviews what the interview is and how it works, and chooses **Start AI-led interview** to proceed or **Opt out** to decline the interview only. Before the interview begins, the candidate sets up and tests their audio and microphone. The AI interviewer then conducts the interview, asking questions and follow-ups.

1. **Finish at a confirmation screen** – The candidate sees a confirmation screen that explains what happens next.

When an evaluation has more than one step, Amazon Connect Talent lists all the steps in order and shows the candidate's progress.

## Audio and device setup
<a name="candidate-experience-audio"></a>

Before an AI-led interview, the candidate sets up audio. The candidate can choose a microphone and speaker, run a speaker test that plays a spoken phrase in their language, and complete a microphone check that confirms Amazon Connect Talent can hear them. On a single-device setup, such as a phone, Amazon Connect Talent hides the advanced device options. Microphone access is required to complete an AI-led interview.

## Languages and accessibility
<a name="candidate-experience-languages-accessibility"></a>

### Languages
<a name="candidate-experience-languages"></a>

The language you set when creating the evaluation determines the language of the entire candidate experience. Assessments are localized in the selected language, and the AI-led interview is conducted in that language. For the languages that Amazon Connect Talent supports, see [Set the evaluation language](managing-evaluations.md#evaluations-language).

### Accessibility
<a name="candidate-experience-accessibility"></a>

Amazon Connect Talent supports screen readers and keyboard navigation across the candidate experience. The AI-led interview, however, is not optimized for screen readers. Candidates who use a screen reader or other assistive technology incompatible with the AI-led interview can opt out and complete the remaining parts of the evaluation. Opting out keeps the candidate's application Active and preserves their place in your pipeline. For more information, see [How a candidate opts out](#candidate-experience-opt-out).

## How a candidate opts out
<a name="candidate-experience-opt-out"></a>

A candidate can choose not to complete the evaluation and instead pursue another path with your recruiting team. Opting out does not penalize the candidate's application. It is also the way a candidate proceeds when the AI-led interview is not usable with their assistive technology.

Amazon Connect Talent offers two ways to opt out. Both come before the AI step begins:
+ **Opt out of the entire evaluation** – At the start of the evaluation, on the role landing page, the candidate can decline the whole evaluation, including all assessments and the AI-led interview.
+ **Opt out of the interview only** – At the start of the AI-led interview, before the audio check, the candidate can decline the interview only. Any assessments the candidate already completed are kept.

There is no per-assessment opt-out. A candidate opts out of either the whole evaluation or the interview only.

To prevent an accidental exit, opting out takes two steps: a first action opens a confirmation message, and a second action confirms the choice. After the candidate confirms, Amazon Connect Talent shows a completion screen and directs the candidate to contact the recruiting team for next steps.

Opting out does not affect the candidate's score. Opting out is final in the product: a candidate cannot reverse it, and returning later shows a completion screen. To learn how opted-out candidates appear to recruiters, see [Candidates who opted out](candidates.md#candidates-opted-out).

## Assist candidates with technical difficulties
<a name="candidate-experience-technical-difficulties"></a>

If a candidate experiences a technical difficulty during their evaluation, Amazon Connect Talent instructs them to contact their recruiter for help. To help the candidate, resend the evaluation. Go to the applicable evaluation, choose **Send to candidates**, and enter the candidate's email address.

If the candidate already completed their assessments and then experiences a technical difficulty during the AI-led interview, their assessment progress and scores are saved. The candidate must restart the AI-led interview.

## Supported browsers
<a name="candidate-experience-supported-browsers"></a>

The candidate evaluation experience requires a supported browser. The following browsers and versions are not supported:
+ **Firefox** versions earlier than 141, including Firefox ESR 140.
+ **iPhone and iPad** running iOS earlier than 26.2. This applies to all browsers on iOS, including Chrome and Safari.

If a candidate reports that their evaluation link will not load, ask them to update their browser or device to a supported version. For more information about assisting candidates with technical issues, see [Assist candidates with technical difficulties](#candidate-experience-technical-difficulties).