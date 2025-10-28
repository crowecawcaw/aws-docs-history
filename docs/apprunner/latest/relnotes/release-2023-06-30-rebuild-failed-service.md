# Release: App Runner adds support to update and rebuild failed services on June 30, 2023

AWS App Runner now supports updating and rebuilding failed services.

**Release date:** June 30, 2023

## Changes

AWS App Runner now supports updating and rebuilding a failed App Runner service. Prior to this release, if your service creation failed for any reason you had to delete the
service and create a new one. This led to longer wait times to get a successful service creation.

With this release, you no longer need to delete the service.
You can rebuild the failed service with or without any changes to the source code or configuration.

For more information, see
[Rebuilding a failed App Runner service](../dg/manage-rebuild.md "../dg/manage-rebuild.md") in the _AWS App Runner Developer Guide_.
