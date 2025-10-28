# Managing Terraform Open Source product status errors

Terraform Open Source `ProvisionProduct` failures are routed to the `TAINTED`
state, allowing each provisioned product to proceed to `UpdateProvisionedProduct`. When this
occurs:

- `UpdateProvisionedProduct` does **not** make an attempt to update or
  correct tags, or to
  create or modify a resource group.
- `UpdateProvisionedProduct` does **not** consider failures
  from previous provisioning operations when deciding if the provisioned product
  should be set to `AVAILABLE` or `TAINTED`.
  AWS Service Catalog only applies Tags during `ProvisionProduct`. Any failed tagging that results from a failure
  of the `ProvisionProduct` operation are **not** automatically resolved.

## Status error examples

**Example 1: AWS Service Catalog does not create a resource group during** `ProvisionProduct`

In the scenario below, you have a provisioned product in the `AVAILABLE` state even if
there is not a supporting resource group, and without any tags applied to the resources.

1. Your action initiates `ProvisionProduct`.
2. The Terraform provisioning engine responds to `ProvisionProduct` with a
   workflow failure and does not provide a `ResourceIdentifier`.
3. The `ProvisionProduct` workflow does not create a resource group, and then sets
   the provisioned product state to `ERROR`.
4. You then initiate the `UpdateProvisionedproduct` operation.
5. The Terraform provisioning engine responds indicating "success."
6. As a result, the `UpdateprovisionedProduct` workflow sets the provisioned product
   state to `AVAILABLE`, but does **not** create a resource group,
   or attempt to apply any Tags.

**Example 2: AWS Service Catalog creates new resources during** `UpdateProvisionedProduct`

In the scenario below, you have a provisioned product in the `AVAILABLE` state even if new
resources do **not** have any tags applied.

1. Your action initiates `ProvisionProduct`.
2. The Terraform provisioning engine responds indicating "success" and provides a
   `ResourceIdentifier`.
3. The `ProvisionProduct` workflow creates a resource group and applies tags to all
   of the identified resources.
4. You initiate `UpdateProvisionedProduct` on a new artifact that creates new resources.
5. The Terraform provisioning engine responds indicating "success."
6. The `UpdateProvisionedProduct` workflow sets the provisioned product state to
   `AVAILABLE` but does **not** attempt to apply any additional
   tags to the new resources.

### Status error solution

AWS Service Catalog ensures that a resource group is created for all provisioned products set to `TAINTED`
from `ProvisionProduct`. If the Terraform provisioning engine does not return a
`ResourceIdentifier`, or if AWS Service Catalog fails to create a resource group, then the provisioned
product is set to the `ERROR` state, forcing you to terminate.
