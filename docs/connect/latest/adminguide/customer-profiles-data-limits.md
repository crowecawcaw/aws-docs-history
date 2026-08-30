# Connect Customer Customer Profiles data limits

With Connect Customer Customer Profiles, you can customize your data onboarding by setting data ingestion
limits on various types of customer data that you use to create a unified profile.
By setting limits on your data mappings, you can prioritize how much data to
ingest across mappings. The default maximum limit across all mappings per profile is 1000.

A per-object-type limit (also referred to as
`MaxProfileObjectCount`) does more than cap how many objects of a type
are stored. It also determines how Connect Customer chooses which objects to remove when a
profile reaches its total object limit. For more information, see [How data limits control object eviction](#customer-profiles-data-limits-eviction "#customer-profiles-data-limits-eviction").

###### Note

Data limits are estimates and might vary slightly, with a possible deviation of
a few units in either direction during periods of high ingestion on a single
profile.

## How data limits control object eviction

Each profile can store a limited total number of objects across all object
types (1000 by default; you can request a limit increase, see [Connect Customer service quotas](amazon-connect-service-limits.md "amazon-connect-service-limits.md")). When a profile reaches this total
limit, Connect Customer removes (evicts) an existing object to
make room. The per-object-type limits you set determine which
object is evicted:

1. Connect Customer first looks for object types that have exceeded their configured
   limit. It evicts the oldest object of the object type that is furthest
   over its limit (the largest overage). This continues, one object per
   ingestion. Eviction stops when that object type is back within its
   limit, or when another object type becomes the one furthest over its
   limit.
2. If no object type is over its limit, Connect Customer falls back to
   _self-eviction_. The incoming object evicts the oldest
   object of its own object type. The total object count for the profile
   stays the same, and no other object type is reduced.

###### Important

An object type that has no limit set is never considered to be over its
limit. As a result, its objects can only be removed through self-eviction. A
high-volume object type with no limit can therefore occupy a large share of
the profile budget indefinitely. This leaves less room for other object
types to grow. To reclaim that space for your business-critical object
types, set a limit on the high-volume object type, such as clickstream or
web analytics data.

###### Note

Eviction affects only the objects that count toward a profile's object
limit. It does not delete the underlying ingested data from the data store.
If you have enabled the data store (see [Data store](enable-customer-profiles.md#enable-customer-profiles-data-store "enable-customer-profiles.md#enable-customer-profiles-data-store")), the data store still
retains evicted objects. To delete data from the data store, use the
`DeleteProfile` API, or delete the object types or the Customer Profiles
domain.

## Default limits for standard object types

Standard object types (object type templates) provided by Customer Profiles can include a
built-in default limit. This limit helps prevent high-volume data from consuming
the entire profile budget. Connect Customer applies this default limit automatically during
eviction when you have not set your own `MaxProfileObjectCount` for
that object type. You do not need to configure anything.

- **Your own limit takes priority.** If
  you have set a limit for the object type, Connect Customer uses that value
  instead of the default. When you clear your limit, the object type falls
  back to the default limit if it has one. For how to set or clear a
  limit, see [How to configure Customer Profiles data limits](#customer-profiles-data-limits-configure "#customer-profiles-data-limits-configure") and
  [How to clear Customer Profiles data limits](#customer-profiles-data-limits-clear "#customer-profiles-data-limits-clear").
- **Defaults are managed by Connect Customer.** Connect Customer
  applies these default limits automatically — you do not set them.
  To use a different limit for an object type, set your own
  limit for that object type.
- **Effective date for existing domains.**
  A default limit can have an effective date so that domains that already
  accumulated objects before the default existed are not affected. When a
  default limit has an effective date, it applies only to domains created
  after that date. Domains created on or before that date keep their
  existing behavior unless you set your own limit. Connect Customer manages this
  effective date — you do not configure it.

The following object types include a default limit.

| Object type                | Default limit | Applies to                              | Rationale                                                                                                                              |
| -------------------------- | ------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `_webAnalytics`            | 250           | Domains created after September 1, 2026 | Retains roughly the last 10 sessions of activity, which<br>gives predictive insights a baseline of data for prediction<br>performance. |
| `WebAnalytics-Clickstream` | 100           | All domains                             | Retains roughly the last 4 sessions of activity, which<br>supports basic event triggers and calculated<br>attributes.                  |

###### Note

A per-object-type limit (including these defaults) is not an
additional storage budget. It does not add to the total per-profile object
limit. It only controls whether objects of that
type are selected as eviction candidates when a profile reaches its total
limit. When every object type is within its limit, Connect Customer uses
self-eviction. In that case, a per-object-type limit does not, by itself,
increase or reduce the total number of objects a profile can store.
The per-profile object limit, which is a service quota, always controls this
total. For more information, see [Connect Customer service quotas](amazon-connect-service-limits.md "amazon-connect-service-limits.md").

To retain more history for these object types (for example, for
high-interaction applications), set a higher
`MaxProfileObjectCount` on the object type. If necessary, request
an increase to your total per-profile object limit (see [Connect Customer service quotas](amazon-connect-service-limits.md "amazon-connect-service-limits.md")).

## How to configure Customer Profiles data limits

You can set a limit for a data object in the Connect Customer admin website, as described
in the following steps. You can also set it programmatically by using the
`PutProfileObjectType` API. A limit that you set takes priority over
any default that Connect Customer manages for that object type.

1. Open the Connect Customer Customer Profiles console.
2. Choose the **Data limits** tab to configure limits
   for data objects.

![Navigate to Data Limits tab to configure limits for data objects.](images/customer-profiles-data-limits-setup-1.png) 3. Pause on the desired data object's limit and choose the edit
icon.

![Pause on the desired data object limit and choose the edit icon.](images/customer-profiles-data-limits-setup-2.png) 4. Enter the limit and choose the check-mark icon to save or update the
limit.

![Image shows a new limit being entered and highlights the check-mark icon that is used to save or update your limit.](images/customer-profiles-data-limits-setup-3.png)

## How to clear Customer Profiles data limits

1. Select the radio button for the data object whose limit you want to
   clear. You will then be able to choose **Clear
   limit**.

![Highlights the radio button to the left of the data object on the data limits page.](images/customer-profiles-data-limits-clear-1.png) 2. Type _confirm_ to clear the limit value of the data
object that you selected.

![A pop-up box that asks you to confirm that you would like to clear the data object limit value.](images/customer-profiles-data-limits-clear-2.png)
