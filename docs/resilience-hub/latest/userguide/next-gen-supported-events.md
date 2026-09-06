

# Supported Next generation Resilience Hub events
<a name="next-gen-supported-events"></a>

All Next generation Resilience Hub API actions are logged in CloudTrail, including the following.


| Category | Example events | 
| --- | --- | 
| Systems | CreateSystem, DeleteSystem, GetSystem, ListSystems | 
| Services | CreateService, UpdateService, DeleteService, ListServices | 
| Policies | CreateResiliencePolicy, UpdateResiliencePolicy, DeleteResiliencePolicy | 
| Assessments | StartFailureModeAssessment, GetFailureModeAssessment, ListFailureModeFindings | 
| Discovery | StartServiceTopologyDiscovery, ListDependencies, ClassifyDependency | 
| Resilience testing | CreateTest, GetTest, ListTests, UpdateTest, DeleteTest, StartTestRun, StopTestRun, GetTestRun, ListTestRuns, ListTestTemplates, GetTestTemplate, PutTestSources, DeleteTestSources, ListTestSources, ListTestRunSources, ListTestRunEvents, ListResolvedTestRunTargetResources | 