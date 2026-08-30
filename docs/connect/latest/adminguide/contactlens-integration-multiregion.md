# Set up multi-region redundancy for conversational analytics integration

With multi-region redundancy, you can scale your external voice system for
highest reliability, performance, and efficiency. You can support multi-region
redundancy using Connect Customer replica instance.

## Active/Passive redundancy configuration

You can create one Connect Customer instance in one Region (for example,
US East (N. Virginia)) and a replica instance in another Region (for example,
US West (Oregon)). You can then configure your external voice system to send
SIPREC SIP INVITE to the primary Region. When the Connect Customer instance in the primary
Region fails, you can update your external voice system to failover to the
replica Connect Customer instance in the passive Region.

## Active/Active redundancy configuration

You can implement the active-active strategy by concurrently streaming audio
to both Connect Customer instances. To implement this strategy, configure your external
voice system to concurrently stream audio to the two separate Regions. In each
Region, conversational analytics integration will do the following:

1. Create its own Connect Customer contact.
2. Captures the audio stream to create call recordings
3. Perform conversational analytics analysis

This approach requires you to replicate all the Connect Customer contact center
configurations manually. However, you can use Connect Customer Global Resiliency and it
will replicate all the Connect Customer instance settings across the Regions automatically.
For more information, see [Set up Connect Customer Global Resiliency](setup-connect-global-resiliency.md "setup-connect-global-resiliency.md").
