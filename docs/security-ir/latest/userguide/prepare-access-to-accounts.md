# Prepare access to AWS accounts

During an incident, your incident response teams must have access to the environments and
resources involved in the incident. Ensure that your teams have appropriate access to
perform their duties before an event occurs. To do that, you should know what level of
access your team members require (for example, what kinds of actions they are likely to
take) and should provision least privilege access in advance.

To implement and provision this access, you should identify and discuss the AWS
account strategy and cloud identity strategy with your organization's cloud
architects to understand what authentication and authorization methods are configured.
Due to the privileged nature of these credentials, you should consider using approval
flows or retrieving credentials from a vault or safe as part of your implementation.
After implementation, you should document and test the team members’ access well before
an event occurs to make sure they can respond without delays.

Lastly, users that are created specifically to respond to a security incident
are often privileged in order to provide sufficient access. Therefore, use of these
credentials should be restricted, monitored, and not used for daily activities.
