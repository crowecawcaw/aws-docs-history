# RAIER02-BP01 Add statistical confidence to your release

decision

Move beyond simple averages and point estimates to understand how
confident you can be that your system will meet its release
criteria when deployed. Instead of just asking did we hit our
target threshold, ask how confident are we that we'll consistently
hit this threshold given the uncertainty in our test results? Use
appropriate statistical methods to account for the limited data
you have and the variation you expect to see in real-world
performance. When you have multiple release criteria, adjust your
analysis to account for the fact that meeting the criteria
simultaneously is harder than meeting each one individually. This
approach may provide a clear, data-driven answer to whether you're
ready to release, rather than making that decision based on
potentially misleading averages that don't account for
uncertainty.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Choose appropriate statistical methods to make inferences
   about your target population based on your sample. For
   example, use a t or normal distribution for continuous
   metrics. For ordinal metrics (for example, LLM as a Judge),
   use non-parametric approaches.
2. To calculate the confidence of meeting a minimum threshold,
   you can use a Cumulative Distribution Function (CDF), while
   for a maximum threshold, you would use the Survival Function
   (SF). For ordinal data, non-parametric approaches like
   bootstrapping can be used to empirically derive these values
   by repeatedly resampling from your observed data to create a
   full distribution of a summary statistic, such as the median.
   From this empirical distribution, you can directly calculate
   the proportion of outcomes that fall below or above a specific
   threshold.
3. Adjust confidence thresholds when evaluating multiple criteria
   together. Apply corrections like Bonferroni to address
   compounding uncertainty from multiple criteria. Document
   methodology and provide clear pass/fail decisions.

## Resources

**Related documents**

- [ISO/IEC
  42001:2023 A.6.2.4 AI system verification and
  validation](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Python
  SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html "https://docs.scipy.org/doc/scipy/reference/stats.html")
- [Python
  Numpy](https://numpy.org/doc/stable/ "https://numpy.org/doc/stable/")
