# Test run fails to start

**Symptom:** Starting a test run returns a
`ConflictException`.

**Cause:** Next generation Resilience Hub runs a single test run at a time
for a target. The previous run for the service is still in progress.

**Solution:** Wait for the current run to complete, or stop it
with `StopTestRun`, and then start the new run.
