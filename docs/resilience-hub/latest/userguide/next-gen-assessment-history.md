

# Assessment history and trends
<a name="next-gen-assessment-history"></a>

Next generation Resilience Hub retains assessment history for 2 years, enabling you to:
+ Track how your resilience posture improves over time.
+ See which findings have been resolved versus remain open.
+ Identify recurring issues across assessments.
+ Generate compliance reports showing improvement trends.

**To view assessment history (CLI)**

```
aws resiliencehubv2 list-failure-mode-assessments \
  --service-arn "arn:aws:resiliencehub:..."
```