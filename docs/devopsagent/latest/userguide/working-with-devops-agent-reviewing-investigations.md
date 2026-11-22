

# Reviewing investigations

After an investigation completes, you can launch a Review, an on-demand quality assessment of that investigation. It reports back with an overall verdict and a per-criterion breakdown. Reviews also run automatically on a sample of completed investigations.

## What a Review is
<a name="what-a-review-is"></a>

A Review reads the investigation's record to gauge how well the investigation performed. That record includes the problem it was given, the evidence it collected, and the conclusion it reached.

A Review does not re-run or alter the investigation. It leaves the investigation as it is and produces its own result alongside it. Each Review returns two things:
+ An **overall quality verdict** – whether the investigation was helpful or not helpful.
+ A **per-criterion breakdown** – a pass, fail, or not applicable verdict on each quality dimension.

## When to use a Review
<a name="when-to-use-a-review"></a>

Use a Review when you want a structured assessment of an investigation's quality. Run one when you are deciding whether to act on a root cause or when you are comparing investigations. You can also use it to quickly check whether you can trust the findings before you rely on them.

For more information about running an investigation again and comparing the two runs, see [Replaying investigations](working-with-devops-agent-replaying-investigations.md).

## Launch a Review
<a name="launch-a-review"></a>

You can review only a completed investigation. To launch a Review from your DevOps Agent Space web app:

1. Open a **completed** investigation from the Incident Response tab of your DevOps Agent Space web app.

1. Choose **Review** on the completed investigation to open the **Review & replay** tab.

1. Choose **Run review**.

1. DevOps Agent runs the Review and displays the results on the **Review & replay** tab.

## Automatic Reviews
<a name="automatic-reviews"></a>

AWS DevOps Agent can automatically review a sample of your completed investigations. An automatic Review is the same Review that you launch yourself. The Grader agent runs every Review, including automatic Reviews. You see the same overall verdict and per-criterion breakdown. You get ongoing visibility into investigation quality without launching each Review yourself.

The following table describes how automatic Reviews work.


| Setting | Behavior | 
| --- | --- | 
| When ticket closes | An automatic Review runs when the linked ServiceNow or PagerDuty ticket is resolved. Only investigations that started from that ticket and are complete when it's resolved are eligible. | 
| After investigation completes | An automatic Review runs 7 days after an investigation completes. This trigger covers all investigations. You can't change this delay. | 
| Sampling rate | The percentage of eligible investigations that get an automatic Review. One rate applies across both triggers. The default is 10 percent. A higher sampling rate reviews more of your investigations, which gives you more feedback on investigation quality. You can set a whole number from 1 to 100. For example, at 10 percent, about 1 in 10 eligible investigations gets an automatic Review. | 
| Default state | Automatic Reviews are on by default, with both triggers selected. | 
| Limit | Each investigation gets at most one automatic Review, even if you select both triggers. | 

**When ticket closes** is available only after you connect your [Agent Space](about-aws-devops-agent-what-are-devops-agent-spaces.md) to [ServiceNow](connecting-to-ticketing-and-chat-connecting-servicenow.md) or [PagerDuty](connecting-to-ticketing-and-chat-connecting-pagerduty.md).

## Turn automatic Reviews on or off
<a name="turn-automatic-reviews-on-or-off"></a>

Turn off automatic Reviews if you only want Reviews that you launch yourself. Choose which triggers run automatic Reviews. Raise the sampling rate for broader coverage, or lower it to review fewer investigations.

You change these settings on the Grader agent's page in your Operator Web App.

To turn automatic Reviews on or off:

1. In your Operator Web App, open the **Agents** page.

1. In the **Managed agents** section, choose **Grader**.

1. Choose **Configuration**.

1. In **Automated reviews**, turn **Enable automatic reviews** on or off.

1. (Optional) For **Sampling rate**, enter a whole number from 1 to 100.

1. Under **When to review**, select one or more triggers: **When ticket closes**, **After investigation completes**, or both.

1. Choose **Save**.

You can also open these settings on the **Review & replay** tab of an investigation. Choose **Configure the Grader agent**.

## View automatic Review results
<a name="view-automatic-review-results"></a>

To view an automatic Review:

1. Open the investigation.

1. Choose the **Review & replay** tab.

## How automatic Reviews work with Reviews that you launch
<a name="how-automatic-reviews-work-with-reviews-that-you-launch"></a>

Automatic Reviews don't replace the Reviews that you launch yourself. You can still launch or re-run a Review on any completed investigation at any time. An automatic Review skips an investigation that already has a Review, unless that Review failed or timed out.

## Review results
<a name="review-results"></a>

When a Review finishes, it reports back on the investigation with:
+ An **overall quality verdict** of **helpful** or **not helpful**, summarizing how well the investigation did its job.
+ A **per-criterion breakdown** across five quality dimensions. Each dimension gets its own verdict: **pass**, **fail**, or **not applicable**, with the reasoning behind it. The dimensions are:
  + **Scope alignment** – whether the investigation stayed focused on the problem that was reported.
  + **Evidence grounding** – whether the investigation's conclusions are backed by the evidence it collected.
  + **Completeness** – whether the investigation covered the relevant areas and reached a conclusion.
  + **Environment impact** – whether the investigation accounted for its effect on your environment.
  + **Accuracy** – whether the investigation's root cause matches the root cause on the linked ticket or incident.

A dimension returns **not applicable** when the Review cannot assess it. For example, Accuracy is not applicable when there is no linked ticket or incident, or when the ticket records no root cause.

## Custom Reviews
<a name="custom-reviews"></a>

The five quality dimensions in Review results are the defaults. You can tailor what a Review checks for by setting agent instructions for the Grader agent. With this, you can shape the Review around what quality means for your team, rather than relying on the defaults alone. You set these instructions on the **Grader** agent in the **Knowledge** page of your Operator Web App. For more information about setting agent instructions, see [Agent instructions](about-aws-devops-agent-agent-instructions.md).

There is no fixed schema or special syntax to learn. You describe, in your own words, what you want the Review to check, and it reads those instructions before it assesses an investigation. With these instructions, you can:
+ **Adjust a default criterion** – change what an existing dimension looks for, so it matches how your team judges that quality, while the rest stay on their defaults.
+ **Add a criterion** – introduce a new dimension on top of the five defaults, so the Review also checks for something specific to your environment.
+ **Drop a criterion** – leave out a default dimension that does not apply to your investigations, so the Review no longer evaluates or reports it.

By default, your instructions build on the defaults instead of replacing them. Criteria you don't mention stay as they are. To start from a clean slate instead, say so explicitly in your instructions, and the Review uses only the criteria you define.

Whatever you define applies to Reviews you launch and to automatic Reviews from that point on. The Review reports your custom criteria the same way it reports the defaults. Each criterion gets its own line in the per-criterion breakdown, alongside the overall verdict of helpful or not helpful. This way, a Review stays a consistent, structured read on quality, measured against the criteria that matter to you.