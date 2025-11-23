# RAIRC02-BP03 Design a custom metric if no suitable metric

exists

When creating custom metrics for benefits or potential harmful
events, define what you need to measure and its key characteristics.
Break complex concepts into quantifiable components that directly
relate to stakeholder impacts. Design metrics with definitions and
examples of positive and negative results, including edge cases.
Validate your custom metric against known examples, choose
appropriate measurement scales (like binary, categorical, or
continuous), and document the methodology. Plan for refinement based
on testing, being cautious of metrics that may not generalize well
beyond initial testing.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Clearly define what you're trying to measure and write down
   its key characteristics, focusing on how it directly impacts
   your stakeholders. For example, if you need to measure how
   natural a conversation is, define what makes a conversation
   feel natural or robotic to your specific users. This
   foundation assists to build an accurate metric.
2. Break complex concepts down into smaller pieces that you can
   count or score. For example, split user satisfaction into task
   completion rate, time to complete, and user survey scores, as
   you can measure each of these objectively. This makes abstract
   concepts concrete and measurable.
3. Identify what good and bad results look like, including edge
   cases that might confuse your metric. Define that a helpful
   response should be accurate, relevant, and actionable. Clear
   examples reduce confusion during measurement.
4. Test your custom metric on examples where you already know
   what the right answer should be. Run your metric on obviously
   good and obviously bad examples to see if it gives the results
   you expect. This catches major problems with your metric
   design before you use it on real data.
5. Choose the types of scores your measurement needs. Continuous
   scores give you more nuanced information and let you track
   gradual improvements, while categorical ratings are simpler
   for humans and LLM judge models to assign consistently and
   binary scores simplify the metric but can hide performance
   nuance.
6. Document exactly how to calculate your metric, including
   step-by-step instructions that someone else could follow to
   get the same results. This blocks inconsistency when different
   team members apply your metric and assists you to spot
   problems in your methodology
7. Plan to refine your metric based on real testing since custom
   metrics often need adjustment after you see how they perform.
   Start with small tests and be ready to modify the metric if it
   doesn't work well in practice or gives misleading results on
   new types of data.

## Resources

**Related documents:**

[Use
custom metrics to evaluate your generative AI application with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/use-custom-metrics-to-evaluate-your-generative-ai-application-with-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/use-custom-metrics-to-evaluate-your-generative-ai-application-with-amazon-bedrock/")

[ISO/IEC
42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and validation

**Related tools:**

[scikit
learn : make_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html "https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html")
