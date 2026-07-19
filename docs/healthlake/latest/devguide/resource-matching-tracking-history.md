# Tracking linkage history

Resource matching does not delete a `Linkage` when a grouping changes. When
resources are split into separate groups, or a group drops below two members, the superseded
`Linkage` is retained with its `active` field set to
`false`. Current groupings have `active` set to `true`.
This lets you trace how a resource's linkages have evolved over time – for
example, to audit why two records were once grouped and are no longer, or to reconstruct the
state of a grouping at an earlier point.

Because inactive `Linkage` resources remain in the data store, use the
`active` search parameter to separate current links from historical ones.

Get the current linkages for a resource

Return only the groupings that still hold:

```
GET /Linkage?item=Patient/patient-A&active=true&_include=Linkage:item
```

Get the historical (inactive) linkages for a resource

Return the superseded groupings a resource once belonged to:

```
GET /Linkage?item=Patient/patient-A&active=false&_include=Linkage:item
```

Get the full linkage history for a resource

Omit the `active` filter to return both current and historical
groupings. Sort by `_lastUpdated` to follow the sequence of
changes:

```
GET /Linkage?item=Patient/patient-A&_include=Linkage:item&_sort=_lastUpdated
```

Each inactive `Linkage` retains the
`linkage-match-detail` extensions that recorded which identifiers caused the
grouping, so you can see the specific `system|value` that once connected the
resources.

###### Note

Inactive `Linkage` resources count toward the linkages returned by a broad
search such as `GET /Linkage`. Filter on `active=true` if you want
only the current view.
