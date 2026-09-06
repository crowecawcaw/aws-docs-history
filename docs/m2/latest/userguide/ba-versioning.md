

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe versioning
<a name="ba-versioning"></a>

The AWS Transform for mainframe Transformation and Runtime products are versioned using a semver (semantic versioning) compliant scheme. To deploy your application, you need to use the corresponding runtime version compatible with your modernized code. If you have questions about what version to use, contact your AWS Transform for mainframe delivery manager. 

## Releases
<a name="ba-versioning-releases"></a>

Each *release* is identified with a **`[Major].[Minor].[Patch]`** pattern. For example, with AWS Transform for mainframe Runtime version `4.1.0`, the major version is 4, the minor version is 1, and the patch version is 0.

We intend to release new AWS Transform for mainframe Runtime minor versions monthly, and new major versions when there are impactful changes to the product or its dependencies.

For details on the new features available in each version, see [AWS Transform for mainframe release notes](ba-release-notes.md).

## Alpha pre-releases
<a name="ba-versioning-alpha"></a>

Each *alpha pre-release* is identified with a **`[Major].[Minor].0`** pattern.

Alpha pre-releases are frequent short-lived versions that are intended and available for quick iteration during the modernization projects. There is no fixed release cadence for new Alpha pre-release versions, and are made available as they are developed and tested.

For more information about versioning, upgrades, and support, see [AWS Mainframe Modernization components lifecycle](lifecycle-m2.md).

**Important**  
Alpha pre-releases should be used during the modernization project phase only and not for production or critical workloads.