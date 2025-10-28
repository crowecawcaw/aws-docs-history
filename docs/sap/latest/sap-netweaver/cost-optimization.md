# Cost Optimization

Resources (CPU, Memory, additional application servers, system copies for different tests/validations, and so on) require SAP landscape changes over time. AWS recommends that you monitor system utilization and the need for existing systems on a regular basis and take actions to reduce cost. In case of a database like SQL Server, the only opportunity to right-size the database server is by scaling up/down or shutting it down, if not required. Here are few suggestions that you can consider for cost optimization:

- Consider Reserved instances over On-Demand instances if the requirement is to run your instances 24x7 365 days per year. Reserved instances provide up to a 75% discount over On-Demand instances. See [EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") for details.
- Consider running occasionally required systems like training, sandbox, and so on, on-demand for the duration required.
- Monitor CPU and memory utilization over time for other non-production systems like Dev/QA and right-size them when possible.
