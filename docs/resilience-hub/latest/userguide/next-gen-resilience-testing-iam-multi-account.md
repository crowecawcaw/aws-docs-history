# Multi-account execution roles

For a multi-account test, AWS FIS uses a role chain. AWS FIS assumes the _orchestrator role_ in the account that runs the experiment. The orchestrator role then assumes a _target role_ in each account that contains targeted resources. Create the orchestrator role once, and create a target role in every target account.
