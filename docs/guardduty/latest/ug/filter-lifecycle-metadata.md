# Filter lifecycle metadata

When you retrieve filter details using the [GetFilter](../APIReference/API_GetFilter.md "../APIReference/API_GetFilter.md") API, you can view lifecycle metadata fields.
These fields show when a filter was created and how many times it has been
modified.

The GetFilter response includes the following lifecycle
metadata fields:

**`createdAt`**

The timestamp when the filter was originally created. GuardDuty sets
this value at creation time and never changes it. GuardDuty does not
populate this field for legacy filters (filters you created before
this feature launched).

**`updatedAt`**

The timestamp when the filter was last updated. GuardDuty updates
this value on every successful [UpdateFilter](../APIReference/API_UpdateFilter.md "../APIReference/API_UpdateFilter.md") call. At creation time,
`updatedAt` matches `createdAt`. For legacy
filters, this field appears only after you update the filter at
least once.

**`version`**

An integer that counts how many times you have modified the filter.
It starts at 1 when you create the filter and increases by 1 with
each successful UpdateFilter call, regardless of
whether the filter content changes. GuardDuty does not populate this
field for legacy filters.

###### Note

These lifecycle metadata fields are read-only. The
CreateFilter and UpdateFilter operations do not
accept these fields as input, and their responses do not include these fields.
To view lifecycle metadata, call GetFilter.
