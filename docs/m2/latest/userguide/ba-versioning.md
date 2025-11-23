AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age versioning

The AWS Blu Age Transformation and Runtime products are versioned using a semver (semantic
versioning) compliant scheme. To deploy your application, you need to use the corresponding
runtime version compatible with your modernized code. If you have questions about what
version to use, contact your AWS Blu Age delivery manager.

## Releases

Each _release_ is identified with a **`[Major].[Minor].[Patch]`** pattern. For example,
with AWS Blu Age Runtime version `4.1.0`, the major version is 4, the minor version is 1,
and the patch version is 0.

We intend to release new AWS Blu Age Runtime minor versions monthly, and new major versions when
there are impactful changes to the product or its dependencies.

For details on the new features available in each version, see [AWS Blu Age release notes](ba-release-notes.md "ba-release-notes.md").

## Alpha pre-releases

Each _alpha pre-release_ is identified with a
**`[Major].[Minor].0`** pattern.

Alpha pre-releases are frequent short-lived versions that are intended and available
for quick iteration during the modernization projects. There is no fixed release cadence
for new Alpha pre-release versions, and are made available as they are developed and
tested.

For more information about versioning, upgrades, and support, see [AWS Mainframe Modernization components lifecycle](lifecycle-m2.md "lifecycle-m2.md").

###### Important

Alpha pre-releases should be used during the modernization project phase only and
not for production or critical workloads.
