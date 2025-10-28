# Understand which ephemeris is used

Ephemerides have a _priority_, _expiration time_, and
_enabled_ flag. Together, these determine which ephemeris is used for a
satellite. Only one ephemeris can be active for each satellite.

The ephemeris that will be used is the **highest-priority enabled ephemeris**
whose expiration time is in the future. A larger priority value indicates a higher priority.
The available contact times returned by
**ListContacts** are based on this ephemeris. If multiple
`ENABLED` ephemerides have the same priority, the most recently created or
updated ephemeris will be used.

###### Note

AWS Ground Station has a service quota on the number of `ENABLED` customer-provided
ephemerides per satellite (see: [Service Quotas](../../../general/latest/gr/gs.md "../../../general/latest/gr/gs.md")).
To upload ephemeris data after reaching this quota, delete (using `DeleteEphemeris`)
or disable (using `UpdateEphemeris`) the lowest-priority/earliest created
customer-provided ephemerides.

If no ephemeris has been created, or if no ephemerides have `ENABLED` status,
AWS Ground Station will use a default ephemeris for the satellite (from [Space-Track](https://www.space-track.org/ "https://www.space-track.org/")), if available.
This default ephemeris has priority 0.

## Effect of new ephemerides on previously scheduled contacts

Use the [DescribeContact API](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md")
to view the effects of new ephemerides on previously scheduled contacts by returning the
active visibility times.

Contacts scheduled prior to uploading a new ephemeris will retain the originally scheduled
contact time, while the antenna tracking will use the active ephemeris. If the spacecraft's
position, based on the active ephemeris, differs greatly from the prior ephemeris, this may
result in reduced satellite contact time with the antenna due to the spacecraft operating
outside the transmit/receive site mask. Therefore, we recommend that you cancel and reschedule
your future contacts after you upload a new ephemeris that differs greatly from the previous
ephemeris. With the [DescribeContact API](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md"),
you can determine the portion of your future contact that is unusable due to the spacecraft
operating outside the transmit/receive site mask by comparing your scheduled contact `startTime` and `endTime` with the returned `visibilityStartTime` and `visibilityEndTime`. If you choose to cancel and reschedule your
future contact(s), the contact time range must not be outside the visibility time range by
more than 30 seconds. Cancelled contacts may incur costs when cancelled too close to the time
of contact. For more information on cancelled contacts see: [Ground Station FAQs](https://aws.amazon.com/ground-station/faqs/ "https://aws.amazon.com/ground-station/faqs/").
