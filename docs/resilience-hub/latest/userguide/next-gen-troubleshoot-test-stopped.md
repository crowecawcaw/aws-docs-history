# Test run stops before completing

**Symptom:** A test run stops on its own before it finishes.

**Cause:** A CloudWatch alarm that you configured as a stop
condition breached its threshold, and resilience testing stopped the run to limit impact.

**Solution:** Review the alarm that triggered the stop
condition to determine the impact on your service. After you address the underlying issue, start
a new test run.
