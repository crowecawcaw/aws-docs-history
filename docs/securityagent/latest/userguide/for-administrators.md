# For administrators (console)

As an administrator, you set up AWS Security Agent in the AWS Management Console and configure Agent Spaces that users access through the AWS Security Agent web application. Each Agent Space represents a distinct environment with specific permissions and resources.

We recommend creating a unique Agent Space for each application you want to test. For example, if you have two internal projects—a billing application and a task tracking application—you should create two separate Agent Spaces.

## Example configuration

Consider an administrator setting up an Agent Space to assess the security of an internal billing application. The administrator would:

- Verify the domain (such as `beta.billing.example.com`)
- Connect to GitHub and enable code review
- Configure network access by assigning an appropriate VPC, subnet, and security group for penetration testing

When users initiate a penetration test or design review, they can select from these pre-configured resources, working within the guardrails you’ve defined while maintaining flexibility for their specific assessment needs.
