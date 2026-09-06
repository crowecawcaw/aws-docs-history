

# Assessment fails with topology not found
<a name="next-gen-troubleshoot-topology-not-found"></a>

**Symptom:** `StartFailureModeAssessment` returns an error about missing topology.

**Solution:** Run `StartServiceTopologyDiscovery` first and wait for it to complete successfully. Assessments require a completed topology.