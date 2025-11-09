# Build a hybrid hosting solution

A hybrid hosting solution combines multiple sources of game hosting resources to host your
game, including Amazon GameLift Servers managed fleets that run in the AWS Cloud and resources that you
supply and manage on your own. This topic describes some common patterns for building a
hybrid solution, and provides tips on how to successfully combine self-managed game hosting
with cloud-based game hosting managed by Amazon GameLift Servers.

## Common hybrid patterns

- **Cost optimization**: Use the most cost-effective fleet type for each scenario, such as Anywhere fleets for baseline capacity and managed fleets for peak demand.
- **Geographic flexibility**: Deploy managed fleets in high-traffic AWS Regions and Anywhere fleets where you have existing infrastructure or specific compliance requirements.
- **Risk mitigation**: Reduce dependency on any single hosting approach by distributing load across multiple fleet types and providers.
- **Gradual migration**: Transition from on-premises or other hosting solutions to AWS gradually while maintaining service continuity.

###### Development and production split

Use different fleet types for development and production environments:

- **Development**: Anywhere fleets for cost-effective development and testing
- **Production**: Managed Amazon EC2 or container fleets for scalable, reliable production hosting

### Regional optimization

Optimize fleet types based on AWS Regions characteristics:

- **High-traffic AWS Regions**: Managed fleets with auto-scaling for variable demand
- **Specialized AWS Regions**: Anywhere fleets for compliance, data sovereignty, or existing infrastructure

### Capacity tiering

Use different fleet types for different capacity tiers:

- **Baseline capacity**: Anywhere fleets or reserved instances for predictable load
- **Burst capacity**: Managed fleets with auto-scaling for peak demand
- **Overflow capacity**: Spot instances or additional AWS Regions for extreme peaks

## Implementation considerations

When building a hybrid solution, consider these key factors:

Game session queue configuration

Configure your game session queues to include all fleet types and set appropriate priorities and latency preferences to ensure optimal placement across your hybrid infrastructure.

Monitoring and observability

Implement comprehensive monitoring across all fleet types to maintain visibility into performance, capacity, and costs across your hybrid solution.

Operational complexity

Account for the increased operational complexity of managing multiple fleet types, including different deployment processes, monitoring tools, and troubleshooting procedures.

Network connectivity

Ensure reliable network connectivity between your different hosting environments, especially for Anywhere fleets that may be on-premises or in different cloud providers.

## Getting started with hybrid hosting

To implement a hybrid hosting solution:

1. **Start simple**: Begin with a single fleet type and add others gradually as your requirements become clearer.
2. **Plan your architecture**: Design your hybrid architecture based on your specific requirements for cost, performance, compliance, and operational complexity.
3. **Configure queues**: Set up game session queues that span your different fleet types with appropriate priorities and placement strategies.
4. **Test thoroughly**: Test game session placement and failover scenarios across your hybrid infrastructure before going to production.
5. **Monitor and optimize**: Continuously monitor performance and costs across all fleet types and adjust your configuration as needed.

Tips

- Use the same game client and server components with both managed and
  self-managed hosting resources. Provide a unified player experience
  across all hosting resources.
- Use the same FlexMatch matchmakers to place matches across all hosting
  resources.
- Centrally manage your hybrid hosting resources together while you
  deploy them across the globe.
- As player demand fluctuates, manage game session loads seamlessly
  across managed and self-managed resources.
- With the Amazon GameLift Servers Agent, you can use the same tools to manage game server
  life cycles on all types of hosting resources.
- Gather game and player metrics and logs across all hosting resources.
  Take advantage of Amazon GameLift Servers features and other AWS services to combine
  data and develop cohesive observability solutions.
