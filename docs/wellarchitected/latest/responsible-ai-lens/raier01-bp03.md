# RAIER01-BP03 For each system update, re-run the evaluation and

update the system registry

Record evaluation activities in logs that capture test conditions,
system configurations, data inputs, raw results, and methodological
notes with sufficient detail to make the entire process
reproducible. Establish version control for evaluation artifacts to
assist builders to trace unique system builds and their
corresponding evaluation results.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Log your evaluation runs, including information on which
   datasets you used, what system version you tested, what
   hardware and software configuration you ran on, and raw and
   intermediate outputs. Your logs should be detailed enough that
   someone else could reproduce your exact evaluation months
   later.
2. Set up version control for your evaluation materials,
   including test scripts, configuration files, and result
   outputs.
3. Link your evaluation materials to both your system and your
   dataset registry so that it is clear which data and system
   versions led to the evaluation results. This allows you to
   link each system build and dataset pair to its specific
   evaluation artifacts.

## Resources

**Related documents**

- [ISO/IEC
  42001:2023 A.6.2.4 AI system verification and
  validation](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
- [ISO/IEC
  42001:2023 A.7.2 Data for development and enhancement of AI
  system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
