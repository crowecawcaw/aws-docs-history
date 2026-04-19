# Limitations

Cedar policies and the current Amazon Bedrock AgentCore Gateway implementation have certain limitations that affect policy authoring and functionality.

## Cedar language limitations

The following limitations are inherent to the Cedar policy language:

- **No floating-point numbers** - Cedar does not support float types. Use Decimal for fractional values (limited to 4 decimal places)
- **No regular expressions** - Pattern matching is limited to the like operator with \* wildcards

## Current implementation limitations

The following limitations are specific to the current Amazon Bedrock AgentCore Gateway implementation:

- **Custom claims in NL2Cedar** - to use custom claims with NL2Cedar, provide the custom claims in the prompt
- **Limited decimal precision** - Decimal values are limited to 4 decimal places and a specific range
- **Max policy size** - 10 KB per individual policy
- **Max total policy size per resource** - 200 KB combined across all policies per resource within a policy engine
- **Cedar schema size** - supported schemas size under 100 KB
- **Max Policies per Engine** - 1,000
- **Max Policy Engines per account** - 1,000

These implementation limitations may be addressed in future releases.
