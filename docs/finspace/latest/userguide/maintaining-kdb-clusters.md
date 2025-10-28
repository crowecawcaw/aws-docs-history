After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Maintaining a Managed kdb Insights cluster

Maintaining a kdb cluster involves updates to the cluster's underlying operating
system or to the container hosting the Managed kdb Insights software. FinSpace manages and
applies all such updates.

Some maintenance may require FinSpace to take your Managed kdb cluster offline for a
short time. This includes, installing or upgrading required operating system or database
patches. This maintenance is automatically scheduled for patches that are related to
security and instance reliability.

The maintenance window determines when pending operations start, but it
doesn't limit the total execution time of these operations. Maintenance
operations that don't finish before the maintenance window ends can continue
beyond the specified end time.

## Managed kdb Insights maintenance window

Every Manged kdb environment has a weekly maintenance window during which system
changes are applied. You can control when modifications and software patches occurs
during a maintenance window. If a maintenance event is scheduled for a given week, it
is initiated during the maintenance window.

| AWS Region name          | Time block      |
| ------------------------ | --------------- |
| Canada (Central)         | 15:00–16:30 UTC |
| US West (N. California)  | 18:00–19:30 UTC |
| US West (Oregon)         | 18:00–19:30 UTC |
| US East (N. Virginia)    | 15:00–16:30 UTC |
| US East (Ohio)           | 15:00–16:30 UTC |
| Europe (Ireland)         | 10:00–11:30 UTC |
| Europe (London)          | 09:00–10:30 UTC |
| Europe (Frankfurt)       | 08:00–09:30 UTC |
| Asia Pacific (Singapore) | 02:00–03:30 UTC |
| Asia Pacific (Sydney)    | 23:00–12:30 UTC |
| Asia Pacific (Tokyo)     | 01:00–02:30 UTC |
