# Configure AWS Security Agent

AWS recommends creating a unique Agent Space for each application you want to test. For example, if you have two internal projects—a billing application and a task tracking application—you should create two separate Agent Spaces.

## Example configuration

Consider an administrator setting up an agent space to assess the security of an internal billing application. The administrator would:

- Verify the domain (such as `beta.billing.example.com`)
- Connect to GitHub and enable Code Review
- Configure network access by assigning an appropriate VPC, Subnet, and Security Group for penetration testing

When users initiate a penetration test or design review, they can select from these pre-configured resources, working within the guardrails you’ve defined while maintaining flexibility for their specific assessment needs.
