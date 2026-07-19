# Enabling resource matching

Resource matching is available in preview and is enabled per request.

Matching runs asynchronously after a resource is written and is eventually consistent: there is no fixed service level for the time between when a resource is ingested and when its `Linkage` is created or updated. A resource you have just written may not yet appear in a `Linkage` when you query for it.

If you disable and later re-enable resource matching, resources written to the datastore while it was disabled are not matched retroactively. Only resources written while resource matching is enabled are evaluated.

Resource matching is available in all AWS Regions where AWS HealthLake is available. For the current list of Regions, see [AWS HealthLake endpoints and quotas](../../../general/latest/gr/Amazon-HealthLake.md "../../../general/latest/gr/Amazon-HealthLake.md") in the _AWS General Reference_.
