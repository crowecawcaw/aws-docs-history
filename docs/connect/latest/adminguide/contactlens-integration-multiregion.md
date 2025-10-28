# Set up multi-region redundancy

for Contact Lens integration

Multi-region redundancy enables you to scale your external voice system for
highest reliability, performance, and efficiency. You can support multi-region
redundancy using Amazon Connect replica instance.

## Active/Passive redundancy

configuration

You can create one Amazon Connect instance in one Region (for example,
US East (N. Virginia)) and a replica instance in another Region (for example,
US West (Oregon)). You can then configure your external voice system to send
SIPREC SIP INVITE to the primary Region. When the Amazon Connect instance in the primary
Region fails, you can update your external voice system to failover to the
replica Amazon Connect instance in the passive Region.

## Active/Active redundancy

configuration

You can implement the active-active strategy by concurrently streaming audio
to both Amazon Connect instances. To implement this strategy, configure your external
voice system to concurrently stream audio to the two separate Regions. In each
Region, Contact Lens integration will do the following:

1. Create its own Amazon Connect contact.
2. Captures the audio stream to create call recordings
3. Perform Contact Lens analysis

This approach requires you to replicate all the Amazon Connect contact center
configurations manually. However, you can use Amazon Connect Global Resiliency and it
will replicate all the Amazon Connect instance settings across the Regions automatically.
For more information, see [Set up Amazon Connect Global Resiliency](setup-connect-global-resiliency.md "setup-connect-global-resiliency.md").
