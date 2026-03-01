# Overview of Amazon RDS Extended Support

After the RDS end of standard support date, if you didn't disable RDS Extended Support during
the [creation](extended-support-creating-db-instance.md "extended-support-creating-db-instance.md") or [restoration](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md") of your DB
instances, then Amazon RDS will automatically enroll them in RDS Extended Support. Amazon RDS
automatically upgrades your DB instance to the last minor version released before the
RDS end
of standard support date, if you aren't already running that version. Amazon RDS won't
upgrade your minor version until _after_ the RDS end of
standard support date for your major engine version.

You can create new databases with major engine versions that have reached the RDS end of
standard support date. RDS automatically enrolls these new databases in RDS Extended Support and charges you
for this offering.

If you upgrade to an engine that's still under RDS standard support _before_ the RDS end of standard support date, Amazon RDS won't
enroll your engine in RDS Extended Support.

If you attempt to restore a snapshot of a database compatible with an engine that's past
the RDS end
of standard support date but isn't enrolled in RDS Extended Support, then Amazon RDS will
attempt to upgrade the snapshot to be compatible with the latest engine version that is
still under RDS standard support. If the restore fails, then Amazon RDS will
automatically enroll your engine in RDS Extended Support with a version that's compatible with the
snapshot.

You can end enrollment in RDS Extended Support at any time. To end enrollment, upgrade each enrolled
engine to a newer engine version that's still under RDS standard support. The end of
RDS Extended Support enrollment will be effective the day that you complete an upgrade to a newer
engine version that's still under RDS standard support.

For more information about the RDS end of standard support dates and
the RDS end of Extended Support dates, see [Supported MySQL major versions on Amazon RDS](MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar "MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar") and [Release calendar for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md#Release.Calendar "../PostgreSQLReleaseNotes/postgresql-release-calendar.md#Release.Calendar").
