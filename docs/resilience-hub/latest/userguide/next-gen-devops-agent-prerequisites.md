

# Prerequisites
<a name="next-gen-devops-agent-prerequisites"></a>

Before you connect a service, make sure that you have the following:
+ A DevOps Agent *Agent Space*. You create and configure the Agent Space in the DevOps Agent console. Note its Amazon Resource Name (ARN), which has the form `arn:aws:aidevops:{{region}}:{{account-id}}:agentspace/{{agent-space-id}}`.
+ An existing Next generation Resilience Hub service, with resource discovery already configured. The cross-account invoker role that discovery uses must exist. You add DevOps Agent permissions to this same role in [Add DevOps Agent permissions to the invoker role](next-gen-devops-agent-invoker-role.md).
+ An Agent Space in a DevOps Agent supported AWS Region. DevOps Agent can investigate resources in any Region regardless of where the Agent Space is created.