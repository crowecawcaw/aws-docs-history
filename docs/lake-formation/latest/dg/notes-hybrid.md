# Hybrid access mode considerations and limitations

Hybrid access mode provides the flexibility to selectively enable Lake Formation permissions for
databases and tables in your AWS Glue Data Catalog.  With the Hybrid access mode, you now have an
incremental path that allows you to set Lake Formation permissions for a specific set of users without
interrupting the permission policies of other existing users or workloads.

The following considerations and limitations apply to hybrid access mode.

###### Limitations

- Update Amazon S3 location registration – You
  can't edit parameters of a location that is registered with Lake Formation using a service linked
  role.
- Opt in option when using LF-Tags – When
  you can grant Lake Formation permissions using LF-Tags, you can opt in principals to enforce Lake Formation
  permissions as a consecutive step by choosing databases and tables that has LF-Tags
  attached.
- Hybrid access mode access –
  Access to hybrid access mode in Lake Formation is limited to users with data lake administrator or read-only administrator permissions.
- Opt in principals – Currently, only
  a data lake administrator role can opt in principals to resources.
- Opt in all tables in a database – In
  cross-account grants, when you grant permissions, and opt in all tables in a database, you
  need to opt in the database also for the permissions to work.

###### Considerations

- Updating Amazon S3 location registered with Lake Formation to hybrid access
  mode – We do not recommend converting a Amazon S3 data location that is already
  registered with Lake Formation to hybrid access mode though it can be done.
- API behaviors when a data location is registered in hybrid access mode
  - CreateTable – The location is considered as registered with Lake Formation
    regardless of the hybrid access mode flag and opt in status. Thus, the user requires
    the data location permission to create a table.
  - CreatePartition/BatchCreatePartitions/UpdatePartitions (when partition location is
    updated to point to the location registered with hybrid) – The Amazon S3 location is
    considered as registered with Lake Formation regardless of the hybrid access mode flag and opt
    in status. Thus, the user requires the data location permission to create or update a
    database.
  - CreateDatabase/UpdateDatabase (when database location is updated to point to the
    location registered in hybrid access mode) – The location is considered as registered
    with Lake Formation regardless of the hybrid access mode flag and opt in status. Thus, the user
    requires the data location permission to create or update a database.
  - UpdateTable (when a table location is updated to point to the location registered
    in hybrid access mode) – The location is considered as registered with Lake Formation
    regardless of the hybrid access mode flag and opt in status. Thus, the user requires
    data location permission to update the table. If the table location is not updated or
    it is pointing to a location that is not registered with Lake Formation, the user doesn't
    require data location permission to update the table.
