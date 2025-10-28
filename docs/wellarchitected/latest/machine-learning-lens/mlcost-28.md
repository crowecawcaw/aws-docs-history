# MLCOST-28: Monitor Return on Investment for ML models

Once a model is deployed into production, establish a
reporting capability to track the value which is being
delivered. For example:

- If a model is used to support customer acquisition: How
  many new customers are acquired and what is their spend
  when the model’s advice is used compared with a baseline.
- If a model is used to predict when maintenance is needed:
  What savings are being made by optimizing the maintenance
  cycle.

Effective reporting enables you to compare the value delivered
by an ML model against the ongoing runtime cost and to take
appropriate action. If the ROI is substantially positive, are
there ways in which this might be scaled to similar
challenges, for example. If the ROI is negative, could this be
addressed by remedial action, such as reducing the model
latency by using server less inference, or reducing the run
time cost by changing the compromise between model accuracy
and model complexity, or layering in an additional simpler
model to triage or filter the cases that are submitted to the
full model.

## Implementation plan

- **Use dashboard
  reporting** - Using a reporting tool such as
  Quick Suite to develop business focused reports
  showing the value delivered by using the model in terms
  of business KPIs.

## Documents

- [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
