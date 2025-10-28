# Maintaining your Amazon Neptune DB Cluster

Neptune performs maintenance periodically on all the resources it uses, including:

- **Replacing the underlying hardware as necessary.**
  This happens in the background, without your having to take any action, and
  generally has no affect on your operations.
- **Updating the underlying operating system.**
  Operating system upgrades of the instances in your DB cluster are undertaken to
  improve performance and security, so you should generally complete them as soon
  as possible. Typically, the updates take about 10 minutes. Operating system updates
  don't change the DB engine version or DB instance class of a DB instance.

It's generally best to update the reader instances in a DB cluster first,
and then the writer instance. Updating the readers and the writer at the same time
can cause downtime in the event of a failover. Note that DB instances are not
automatically backed up before an operating-system update, so be sure to make
manual backups before you apply an operating-system update.

- **Updating the Neptune database engine.**
  Neptune regularly releases a variety of engine updates to introduce new
  features and improvements and to fix bugs.

## Engine version numbers

### Version numbering before engine release 1.3.0.0

Before November 2019, Neptune only supported one engine version at a time,
and engine version numbers all took the form,
`1.0.1.0.200`<xxx>``, where `xxx` was
the patch number. All new engine versions were released as patches to earlier versions.

In November 2019, Neptune started supporting multiple versions, allowing customers
better control over their upgrade paths. As a result, engine release numbering
changed.

From November 2019 up until [engine release
1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md"), engine version numbers have 5 parts. Take version number `1.0.2.0.R2`
as an example:

- The first part was always 1.
- The second part, `0` in `1.0.2.0.R2`), was
  the database major version number.
- The third and fourth parts, `2.0` in `1.0.2.0.R2`)
  were both minor version numbers.
- The fifth part (`R2` in `1.0.2.0.R2`)
  was the patch number.

Most updates were patch updates, and the distinction between patches and minor
version updates was not always clear.

### Version numbering from engine release 1.3.0.0 on

Starting with [engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md"),
Neptune changed the way engine updates are numbered and managed.

Engine version numbers now have four parts, each of which corresponds to a
type of release, as follows:

    `product-version`**.**`major-version`**.**`minor-version`**.**`patch-version`

Non-breaking changes of the sort that were previously released as patches are
now released as minor versions that you can manage using the [AutoMinorVersionUpgrade](engine-maintenance-management.md#using-amvu "engine-maintenance-management.md#using-amvu") instance setting.

This means that if you want you can receive a notification every time a new minor
version is released, by subscribing to the [RDS-EVENT-0156](event-lists.md#RDS-EVENT-0156 "event-lists.md#RDS-EVENT-0156") event (see [Subscribing to Neptune event notification](events-subscribing.md "events-subscribing.md")).

Patch releases are now reserved for urgent targeted fixes, and are numbered
using the last part of the version number (`*.*.*.1`, `*.*.*.2`,
and so forth).
