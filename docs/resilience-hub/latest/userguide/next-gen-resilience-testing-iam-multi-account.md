

# Multi-account execution roles
<a name="next-gen-resilience-testing-iam-multi-account"></a>

For a multi-account test, AWS FIS uses a role chain. AWS FIS assumes the *orchestrator role* in the account that runs the experiment. The orchestrator role then assumes a *target role* in each account that contains targeted resources. Create the orchestrator role once, and create a target role in every target account.