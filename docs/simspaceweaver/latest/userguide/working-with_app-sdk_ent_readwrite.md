End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Write and read entity field data

All entity data fields are blob types. You can write up to 1,024 bytes of data to
an entity. We recommend that you keep blobs as small as possible because larger
sizes will reduce performance. When you write to a blob, you pass SimSpace Weaver a
pointer to the data and its length. When you read from a blob, SimSpace Weaver
provides you with a pointer and a length to read. All reads must be complete before
the app calls `Commit()`. Pointers returned from a read call are invalidated when the
app calls `Commit()`.

###### Important

- Reading from a cached blob pointer after a `Commit()` is unsupported and can cause the
  simulation to fail.
- Writing to a blob pointer returned from a read call is unsupported and can cause the
  simulation to fail.

###### Topics

- [Store the field data of an entity](working-with_app-sdk_ent_readwrite_store.md "working-with_app-sdk_ent_readwrite_store.md")
- [Load the field data of an entity](working-with_app-sdk_ent_readwrite_load.md "working-with_app-sdk_ent_readwrite_load.md")
- [Loading the field data of removed entities](working-with_app-sdk_ent_readwrite_load-removed.md "working-with_app-sdk_ent_readwrite_load-removed.md")
