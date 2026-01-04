# TELCOREL04-BP03 Implement default configuration to bypass

billing and charging services in case the system is down

Implementing a default configuration to bypass billing and charging services in a telecom
network maintains service continuity for customers in the event of a failure or outage in the
billing or charging system. The network is configured with a failover mechanism that continues
providing critical communication services while bypassing the charging/billing component if they
become unavailable or unresponsive. This bypass mode allows customers to continue accessing and
using the telecom services without interruption, even when the billing or charging systems are
down.

**Desired outcome:**

- Verify customer experience and service availability take precedence over billing and
  charging functions.
- Allow customers to continue using services while their usage and session data is
  temporarily stored or cached within the network.
- Process cached usage data once the billing and charging systems are restored, verifying
  revenue is not lost.

## Implementation guidance

Implement a default configuration on the control plane functions that allows the network
to bypass the billing and charging systems in the event of a failure or outage. Configure the
network functions to continue call setup or session establishment even when the charging
system is unresponsive. When the billing or charging systems are restored, they process the
cached usage data to verify revenue is not lost despite the temporary bypass of these systems.

### Implementation steps

- Define bypass triggers and thresholds:
  - Use monitoring tools to detect failures or unresponsiveness in the billing
    and charging systems
  - Establish clear criteria and thresholds for triggering the bypass mode, such as
    connection timeouts, error rates, or system availability metrics

- Implement bypass configuration:
  - Configure network functions with a default method to continue call setup or
    session setup in case the charging system is unresponsive.

- Use data records and call records for offline charging/billing:
  - Once the billing or charging systems are back online, the cached usage data can
    be processed and the end user is billed accordingly, verifying that revenue is not
    lost despite the temporary bypass of these systems.

## Resources

**Key AWS services:**

- [Amazon CloudWatch for monitoring and alerting](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Lambda for implementing custom bypass logic and
  data processing](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
