# Key patterns when exporting asset revisions

from AWS Data Exchange

When you export an asset revision from AWS Data Exchange, each asset becomes an object in the S3
bucket. The names of the objects are based on a key pattern that you provide. You can use
dynamic references that represent asset attributes to create a pattern for the names that
are automatically generated during the export. Use the dynamic references shown in the
following table.

| Dynamic references            | Description                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `${Asset.Id}`                 | The Id of the asset.                                                                                                                    |
| `${Asset.Name}`               | The name of the asset.                                                                                                                  |
| `${DataSet.Id}`               | The Id of the data set being exported.                                                                                                  |
| `${DataSet.Name}`             | The name of the data set being exported.                                                                                                |
| `${Revision.CreatedAt}`       | The UTC date and time the revision was created, in the following format:<br>YYYY-MM-DDTHH:MM:SSZ. For example: 2021-10-08T16:33:19.787Z |
| `${Revision.CreatedAt.Day}`   | The day of the month the revision was created.                                                                                          |
| `${Revision.CreatedAt.Month}` | The month the revision was created.                                                                                                     |
| `${Revision.CreatedAt.Year}`  | The year the revision was created.                                                                                                      |
| `${Revision.Id}`              | The Id of the revision being exported.                                                                                                  |

You can use these dynamic references to create the key patterns for your asset names.
You must include at least one of the two `Asset` dynamic references, which are
`${Asset.Name}` and `${Asset.Id}`.

For example, using `${Revision.Id}/${Asset.Name}` as a key pattern
results in Amazon S3 objects that use the revision Id and asset name (separated by a slash) as
the object name.

If you export a revision with the Id `testRevisionId` that has two assets
named `asset1` and `asset2`, the assets are exported to the following
locations in Amazon S3:

- `<bucket>/testRevisionId/asset1`
- `<bucket>/testRevisionId/asset2`

###### Note

Your resulting objects must have unique names. If they have the same names as existing
objects in the S3 bucket, your export will overwrite existing objects. If the revision you
are exporting has non-unique names (for example, two assets with the same name), the
export will fail. The only dynamic reference that is unique is
`${Asset.Id}`.
