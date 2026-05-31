# Assessment fails with topology not found

**Symptom:**
`StartFailureModeAssessment` returns an error about missing topology.

**Solution:** Run
`StartServiceTopologyDiscovery` first and wait for it to complete
successfully. Assessments require a completed topology.
