# Providing Feedback on Insights

Amazon Connect Decisions enables you to provide feedback on any insight — including
Root Cause Analysis (RCA) findings and Recommendations generated for insights —
directly through the Natural Language Interface (NLI). Your feedback helps Amazon
Connect Decisions agents learn and improve the accuracy of future analyses and
recommendations. There are two ways to provide feedback:
**Natural Language feedback in the NLI** and
**Thumbs Up/Down ratings** to the agent's response
in the NLI.

Every piece of feedback — whether a quick thumbs up/down or a detailed natural
language correction — is evaluated by Amazon Connect Decisions agents as a potential
learning. Qualifying feedback that is deterministic, non-conflicting, and
generalizable is curated into actionable learnings stored in the Knowledge Store.
Over time, your feedback improves RCA accuracy, recommendation relevance, and
reduces the need for repeated corrections — making Amazon Connect Decisions
progressively smarter with every interaction.

## Natural Language Feedback

You can also provide detailed, context-specific feedback by simply typing your
correction or observation in the Decisions Teammate / NLI. This is ideal when
you want to explain _why_ an output is incorrect or share
operational knowledge that the agent should learn.

**For example,** you review a projected stockout
alert / insight for electronic connectors at your Frankfurt site. The root cause
agent attributes the root cause to a demand forecast error. You respond via NLI:

_"The root cause isn't a forecast error — Supplier TP\_00001 has a
contractual max order quantity of 291 units per PO, and the system generated a
single PO for 1,600 units. The supplier will reject this. Split the PO into
multiple orders of 291 units or fewer."_

Decisions Teammate responds: _"Thank you for the correction. I've
updated the root cause to reflect the supplier's max order quantity constraint.
The recommendation has been regenerated as 6 split POs (5 x 291 + 1 x 145
units). This supplier constraint will be applied to all future recommendations
for TP\_00001."_

## Thumbs Up / Thumbs Down Ratings

Every RCA finding and Recommendation displayed in the NLI includes a thumbs up
and thumbs down option. Use these to quickly signal whether the agent's output
was accurate and helpful. You can add a comment to provide additional context.

**For example,** you receive a projected stockout
alert / insight for running shoes at your Northeast distribution center. The RCA
Agent identifies the root cause: _"Supplier TP\_00012 shipment delayed
by 8 days due to port congestion at Long Beach, combined with a 22% demand spike
driven by the upcoming Boston Marathon."_ The Recommendation Agent
suggests: _"Reallocate 1,200 units from 6 low-demand Southeast stores
to 9 high-demand Northeast stores."_

You give a **thumbs up** and add:
_"Spot on — the port delay and marathon demand spike are exactly what's
driving this. Good recommendation."_

Decisions Teammate / NLI acknowledges: _"Thank you for confirming. Your
feedback strengthens the RCA Agent's confidence in correlating port disruption
signals with regional demand events for future stockout analyses."_
