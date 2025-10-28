# ElastiCache and customer

responsibilities with ElastiCache Extended Support

Following are the responsibilities of Amazon ElastiCache, and your responsibilities with ElastiCache Extended Support.

**Amazon ElastiCache responsibilities**

After the ElastiCache end of standard support date, Amazon ElastiCache will supply patches, bug fixes, and upgrades for engines that are enrolled in ElastiCache Extended Support. This will occur for up to 3 years, or until you stop using the engines in Extended Support, whichever happens first.

**Your responsibilities**

You're responsible for applying the patches, bug fixes, and upgrades given for caches in ElastiCache Extended Support. Amazon ElastiCache reserves the right to change, replace, or withdraw such patches, bug fixes, and upgrades at any time. If a patch is necessary to address security or critical stability issues, Amazon ElastiCache reserves the right to update your caches with the patch, or to require that you install the patch.

You're also responsible for upgrading your engine to a newer engine version before the ElastiCache end of Extended Support date. The ElastiCache end of Extended Support date is typically 3 years after the ElastiCache end of standard support date.

If you don't upgrade your engine, then after the ElastiCache end of Extended Support date, Amazon ElastiCache will attempt to upgrade your engine to a newer engine version that's supported under ElastiCache standard support. If the upgrade fails, then Amazon ElastiCache reserves the right to delete the cache that's running the engine past the ElastiCache end of standard support date. However, before doing so, Amazon ElastiCache will preserve your data from that engine.
