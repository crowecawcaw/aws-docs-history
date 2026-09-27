

# Migration considerations
<a name="service-managed-pk-configure-migration-considerations"></a>
+ **Immediate effect** — The strategy change reaches all service infrastructure within about one second. The service does not roll out the change gradually or use a canary mechanism. Active consumers processing a batch of records may observe the behavior change mid-batch.
+ **No consumer notification** — The service does not send notifications to active consumers when the strategy changes. Consumers are not drained or quiesced. Design your consumer applications to handle `null` partition keys gracefully regardless of the current stream mode.
+ **Console warning** — The Kinesis Data Streams console displays a warning banner when you switch between modes, reminding you that service-managed mode eliminates ordering guarantees and that user-managed mode requires producers to provide partition keys.
+ **Reversible** — You can switch back at any time. If you observe issues after a migration, switch the stream back to the previous mode immediately.
+ **Test in non-production first** — Always test the migration in a non-production environment with representative traffic patterns before applying to production streams.