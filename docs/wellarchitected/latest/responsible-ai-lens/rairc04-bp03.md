# RAIRC04-BP03 Set confidence requirements for your quantitative

release criteria

Decide how certain you need to be that your system meets each
performance threshold before each release criterion question can be
answered. For example, if you were to divide use cases into higher,
moderate, and lower risk, you might set corresponding confidence
requirements to 99%, 95%, and 90% respectively. Consider what level
of confidence your stakeholders might expect.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Group your release criteria by risk level to understand which
   performance decisions need higher confidence as opposed to
   those where you can accept more uncertainty. Create simple
   risk categories like high, medium, and low based on how much
   harm could result if you're wrong about whether your system
   meets each performance limit. This grouping assists you to
   focus your most rigorous testing on the decisions that matter
   most while avoiding over-testing low-risk areas.
2. Check what confidence levels your key stakeholders expect by
   talking with users, business leaders, and other groups who
   depend on your system working correctly. Compare their
   expectations with your planned confidence levels and adjust
   where there are mismatches between what you're planning and
   what they need. Stakeholder alignment assists you to avoid
   surprise rejection of your system because your confidence
   levels don't match their risk tolerance.
3. Set specific confidence levels for each risk category by
   deciding how certain you need to be before you can confidently
   say your system meets each performance limit. Assign
   confidence percentages like 99% for high-risk decisions, 95%
   for medium-risk, and 90% for lower-risk areas based on what
   level of uncertainty and risk tolerance your organization and
   stakeholders can accept.
4. For each release criteria, transform your question from
   "Does our system produce accurate outputs?" into
   confidence, threshold, and metric-based questions like
   "Are we at least 95% confident that our system achieves
   at least 85% accuracy on our LLM-as-a-judge metric for
   correctness?" This allows for clear, objective and
   measurable criteria that leads to binary yes or no responses
   that account for measurement uncertainty.

## Resources

**Related documents:**

- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.9.3 Objectives for responsible use of AI
  system
