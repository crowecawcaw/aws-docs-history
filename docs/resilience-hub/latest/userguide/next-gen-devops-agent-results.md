

# Investigate findings and test runs
<a name="next-gen-devops-agent-results"></a>

After a service is connected, you can launch AWS DevOps Agent directly from the the next generation of Resilience Hub console. When you view a specific failure mode assessment finding, you see an option to chat with DevOps Agent about that finding. For resilience tests, a DevOps Agent investigation starts automatically with the test run, and a summary becomes available shortly after the test completes.
+ **Failure mode assessment findings** – Investigate a finding with DevOps Agent by choosing **Chat with DevOps Agent**, which is available on every failure mode assessment finding. The console opens an interactive DevOps Agent session seeded with that finding. If you use the API, each finding returns an `investigationDeepLink` to the same session.
+ **Resilience test runs** – When a test run finishes, open the test run in the console to see the DevOps Agent investigation, including its verdict, confidence, and analysis summary, and choose the link to open the full session. If you use the API, get the test run and inspect the `devOpsAgentInvestigation` block. The DevOps Agent verdict is advisory; your test run's own result remains authoritative.
+ **Test reports** – When a test report is generated for a connected service, it includes a DevOps Agent investigation section with the summary. The test report generation completes when DevOps Agent completes the investigation.