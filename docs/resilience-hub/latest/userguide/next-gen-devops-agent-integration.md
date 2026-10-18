

# Working with AWS DevOps Agent in the next generation of Resilience Hub
<a name="next-gen-devops-agent-integration"></a>

The next generation of Resilience Hub integrates with AWS DevOps Agent to add agentic investigation to your failure mode assessment findings and resilience test runs. When you connect a service to an *Agent Space* in AWS DevOps Agent, Resilience Hub can launch investigations on your behalf:
+ From any failure mode assessment finding, you can chat with AWS DevOps Agent to investigate and ask for remediation steps interactively.
+ For a resilience test, a DevOps Agent investigation starts automatically with the test run, and a summary of its analysis becomes available shortly after the test completes – shown on the test run and included in the test report.

Resilience Hub calls AWS DevOps Agent on your behalf by assuming the same *invoker role* that you have already set up at service level.

For more information about AWS DevOps Agent, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

**Topics**
+ [Prerequisites](next-gen-devops-agent-prerequisites.md)
+ [Add DevOps Agent permissions to the invoker role](next-gen-devops-agent-invoker-role.md)
+ [Connect a service to the Agent Space](next-gen-devops-agent-connect.md)
+ [Investigate findings and test runs](next-gen-devops-agent-results.md)