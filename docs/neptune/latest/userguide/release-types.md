# Different types of engine release in Amazon Neptune

The four types of engine release that correspond to the four parts of an engine
version number are as follows:

- **Product version**   –  
  This only changes if the product undergoes sweeping, fundamental changes in
  functionality or interface. The current Neptune product version is 1.
- [Major version](#major-versions "#major-versions")   –  
  Major versions introduce important new features and breaking changes, and
  generally have a useful lifespan of at least two years.
- [Minor version](#minor-versions "#minor-versions")   –  
  Minor versions can contain new features, improvements, and bug fixes
  but do not contain any breaking changes. You can choose whether or not to have
  them applied them automatically during the next maintenance window, and
  you can also choose to be notified whenever one is released.
- [Patch version](#patch-version-updates "#patch-version-updates")   –  
  Patch versions are released only to address urgent bug fixes or critical
  security updates. They seldom contain breaking changes, and they are automatically
  applied during the next maintenance window following their release.

## Amazon Neptune major version updates

A major version update generally introduces one or more important new features
and often contains breaking changes. It usually has a support lifetime of around
two years. Neptune major versions are listed in [Engine
releases](engine-releases.md "engine-releases.md"), along with the date they were released and their estimated end of
life.

Major version updates are entirely optional until the major version that
you're using reaches its end of life. If you do choose to upgrade to a new major
version, you must install the new version yourself using the AWS CLI or the
Neptune console as described in [Major version upgrades](engine-updates-manually.md "engine-updates-manually.md").

If the major version that you're using reaches its end of life, however,
you'll be notified that you are required to upgrade to a more recent major version.
Then, if you don't upgrade within a grace period after the notification, an upgrade
to the most recent major version is automatically scheduled to occur during the next
maintenance window. See [Engine version life-spans](engine-updates-eol-planning.md "engine-updates-eol-planning.md") for more information.

## Amazon Neptune minor version updates

Most Neptune engine updates are minor version updates. They happen quite
frequently and do not contain breaking changes.

If you have the [AutoMinorVersionUpgrade](engine-maintenance-management.md#using-amvu "engine-maintenance-management.md#using-amvu")
field set to `true` in the writer (primary) instance of your DB cluster,
minor version updates are applied automatically to all instances in your DB cluster
during the next maintenance window after they are released.

If you have the [AutoMinorVersionUpgrade](engine-maintenance-management.md#using-amvu "engine-maintenance-management.md#using-amvu")
field set to `false` in the writer instance of your DB cluster, they are
applied only if you [explicitly install them](engine-updates-manually.md "engine-updates-manually.md").

###### Note

Minor version updates are self-contained (they don't depend on previous minor
version updates to the same major version), and cumulative (they contain all the features
and fixes introduced in previous minor version updates). This means that you can install
any given minor version update whether or not you have installed previous ones.

It's easy to keep track of minor-version releases by subscribing to the
[RDS-EVENT-0156](event-lists.md#RDS-EVENT-0156 "event-lists.md#RDS-EVENT-0156") event (see [Subscribing to Neptune event notification](events-subscribing.md "events-subscribing.md")).
You will then be notified every time a new minor version is released.

Also, whether or not you subscribe to notifications, you can always [check to see what updates are pending](engine-maintenance-management.md#check-pending-updates "engine-maintenance-management.md#check-pending-updates").

## Amazon Neptune patch version updates

In the case of security issues or other serious defects that affect instance
reliability, Neptune deploys mandatory patches. They are applied to all instances
in your DB cluster during your next maintenance window without any intervention on
your part.

A patch release is only deployed when the risks of not deploying it outweigh any
risks and downtime associated with deploying it. Patch releases happen infrequently
(typically once every few months) and seldom require more than a fraction of your
maintenance window to apply.
