

# On-demand Investigations
<a name="on-demand-investigations"></a>

Amazon Connect Decisions automatically runs root cause analysis and recommendations for the insights it generates. Because this automatic processing is subject to a quota, an on-demand investigation lets you prioritize exceptions that matter most to you — generating their root cause analysis and recommendations even if you’ve already reached your automatic processing quota.

## When to use an On-demand investigation
<a name="on-demand-investigations-when-to-use"></a>

Use an on-demand investigation when you want root cause analysis and recommendations for a specific insight that has not been automatically processed — for example, a high-priority exception you want to act on right away.

## In this Section
<a name="on-demand-investigations-in-this-section"></a>

### Identifying eligible Insights
<a name="on-demand-investigations-identifying-eligible-insights"></a>

On the Insights page, the Root Cause Analysis status of each insight tells you whether it has been processed and whether it is eligible for an on-demand investigation. Look for insights whose status indicates they have not yet been processed.

### Running an on-demand investigation
<a name="on-demand-investigations-running"></a>
+ On the Insights page, locate an insight that has not been automatically processed.
+ Open the Insight and click the Investigate button near the top right.
  + You can also select multiple Insights and start investigations for all of them at once.
+ Once you click the button, Amazon Connect Decisions will investigate and determine the root cause for the Insight and then provide recommendations. Depending on complexity, this should take between 3-15 minutes.
+ When the investigation is complete, you’ll see email and in-app notifications.
  + The in-app notifications can be accessed on the notifications screen by clicking the bell icon in the top-right.
  + These notifications can be disabled in settings.
+ Review the generated root cause analysis and recommendations, and act on them as you would for any other insight (see [Acting on Recommendations](acting-on-recommendations.html)).