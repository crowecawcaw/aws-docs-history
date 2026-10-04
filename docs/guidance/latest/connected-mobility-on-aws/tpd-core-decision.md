

# Deliver by subscription, not by copy
<a name="tpd-core-decision"></a>

The default instinct — produce data on AWS and then ship it to wherever each consumer lives — is the expensive and fragile option. It incurs egress on every byte, duplicates data into destinations the producer no longer controls, and couples platform availability to a network path the producer neither provisions nor contracts for. This pattern inverts that: the data stays on AWS in Kafka, and consumers subscribe to it. Where a consumer lives in another cloud or network, the connection is made private and contracted rather than best-effort. Egress becomes an exception that must be justified, not the default behavior of the platform.