

# Replaying investigations

After an investigation completes, you can replay it. Replaying an investigation allows you to see how the agent handles a past incident after you change its skills, instructions, or integrations. Then you can compare the replay with the original by automated grader score, duration, and investigation timeline.

Replays do not change the original and take no mutative actions. A completed replay and its original are both reviewed automatically, so you can compare their results. For more information about reviews, see [Reviewing investigations](working-with-devops-agent-reviewing-investigations.md).

## When to use a Replay
<a name="when-to-use-a-replay"></a>

Replays are best used after an incident has been resolved and you make a change to your agent configuration. Compare the replay to the original and verify if the new investigation is more helpful, improves investigation speed, or differs from the original in its investigation path.

## Start a replay
<a name="start-a-replay"></a>

To start a replay from your DevOps Agent Space web app:

1. Open a **completed** investigation from the Incident Response tab.

1. Go to the **Review & replay** tab.

1. On the **Replay** card, choose **Run replay**.

1. (Optional) Enter a note under **What did you change?** describing what you updated in your configuration.

1. Choose **Start replay**.

## Replay results
<a name="replay-results"></a>

The **Replays** card on the **Review & replay** tab lists all replays of the investigation. The card shows each replay's name, status, creation time, and duration. Choose **View** to open a replay's investigation, or **Compare** to compare it with the original.

The comparison shows the two runs side by side:
+ **Root cause** – the root cause that each run found.
+ **Grader score** – the review grade and the number of criteria that each run passed, with the verdict for each criterion.
+ **Time to root cause** – how long each run took to reach its root cause.
+ **Tools used** – the tools that each run called.
+ **Skills used** – the skills that each run read.
+ **Investigation timeline** – the steps of each run. Choose **Show timelines** to see them.

If you replay an investigation more than once, you can pick any two runs of the same investigation to compare.

## Limitations
<a name="limitations"></a>

Keep the following in mind when you use replays:
+ **Replay limit** – You can run only one replay of an investigation at a time. Wait for it to finish before starting another.
+ **Incident data** – Replays query your live environment, so the data available at the original investigation time may not be available to the replay depending on your environment. Keep this in consideration when comparing.