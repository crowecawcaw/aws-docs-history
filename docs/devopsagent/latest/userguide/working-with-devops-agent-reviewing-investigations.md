

# Reviewing investigations
<a name="working-with-devops-agent-reviewing-investigations"></a>

After an investigation completes, you can launch a Review, an on-demand quality assessment of that investigation. It reports back with an overall verdict and a per-criterion breakdown.

## What a Review is
<a name="what-a-review-is"></a>

A Review reads the investigation's record to gauge how well the investigation performed. That record includes the problem it was given, the evidence it collected, and the conclusion it reached.

A Review does not re-run or alter the investigation. It leaves the investigation as it is and produces its own result alongside it. Each Review returns two things:
+ An **overall quality verdict** – whether the investigation was helpful or not helpful.
+ A **per-criterion breakdown** – a pass, fail, or not applicable verdict on each quality dimension.

## When to use a Review
<a name="when-to-use-a-review"></a>

Use a Review when you want a structured assessment of an investigation's quality. Run one when you are deciding whether to act on a root cause or when you are comparing investigations. You can also use it to quickly check whether you can trust the findings before you rely on them.

## Launch a Review
<a name="launch-a-review"></a>

You can review only a completed investigation. To launch a Review from your DevOps Agent Space web app:

1. Open a **completed** investigation from the Incident Response tab of your DevOps Agent Space web app.

1. Choose **Review** on the completed investigation.

1. DevOps Agent runs the Review and displays the results on the Review tab.

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

## Custom reviews
<a name="custom-reviews"></a>

The five quality dimensions in Review results are the defaults. You can tailor what a Review checks for by setting agent instructions for the Grader agent. With this, you can shape the Review around what quality means for your team, rather than relying on the defaults alone. You set these instructions on the **Grader** agent in the **Knowledge** page of your Operator Web App. For more information about setting agent instructions, see [Agent instructions](about-aws-devops-agent-agent-instructions.md).

There is no fixed schema or special syntax to learn. You describe, in your own words, what you want the Review to check, and it reads those instructions before it assesses an investigation. With these instructions, you can:
+ **Adjust a default criterion** – change what an existing dimension looks for, so it matches how your team judges that quality, while the rest stay on their defaults.
+ **Add a criterion** – introduce a new dimension on top of the five defaults, so the Review also checks for something specific to your environment.
+ **Drop a criterion** – leave out a default dimension that does not apply to your investigations, so the Review no longer evaluates or reports it.

By default, your instructions build on the defaults instead of replacing them. Criteria you don't mention stay as they are. To start from a clean slate instead, say so explicitly in your instructions, and the Review uses only the criteria you define.

Whatever you define applies to Reviews you launch from that point on. The Review reports your custom criteria the same way it reports the defaults. Each criterion gets its own line in the per-criterion breakdown, alongside the overall helpful or not helpful verdict. This way, a Review stays a consistent, structured read on quality, measured against the criteria that matter to you.