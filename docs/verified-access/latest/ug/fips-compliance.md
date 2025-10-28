# FIPS compliance for Verified Access

Federal Information Processing Standard (FIPS) is a US and Canadian government standard that specifies security requirements for cryptographic modules that protect sensitive information. AWS Verified Access provides the option to configure your environment to adhere to FIPS Publication 140-2. FIPS compliance for Verified Access is available in the following AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Canada (Central)
- AWS GovCloud (US) West
- AWS GovCloud (US) East
  This page shows you how to configure a new, or an existing Verified Access environment, to be FIPS compliant.

###### Contents

- [Existing environment](#migrate-configuration "#migrate-configuration")
- [New environment](#new-configuration "#new-configuration")

## Configure an existing Verified Access environment for FIPS compliance

If you have an existing Verified Access environment and you want to configure it to be FIPS compliant, some of the resources will need to be deleted and re-created in order to turn on FIPS compliance.

To re-configure an existing AWS Verified Access environment to be FIPS compliant, follow the steps below.

1. Delete your original Verified Access endpoint(s), group(s), and instance. Your configured trust providers can be re-used.
2. Create a Verified Access instance, making sure to enable **Federal Information Process Standards (FIPS)** during creation. Also during creation, attach the **Verified Access trust provider** you want to use, by selecting it from the drop down list.
3. Create a Verified Access [group](verified-access-groups.md "verified-access-groups.md"). During creation of the group, you associate it with the Verified Access instance just created.
4. Create one or more [Verified Access endpoints](verified-access-endpoints.md "verified-access-endpoints.md"). During the creation of your endpoint(s), you associate them with the group created in the previous step.

## Configure a new Verified Access environment for FIPS compliance

To configure a new AWS Verified Access environment that is FIPS compliant, follow the steps below.

1. Configure a [trust provider](trust-providers.md "trust-providers.md"). You will need to create a [user identity](user-trust.md "user-trust.md") trust provider and (optionally) a [device-based](device-trust.md "device-trust.md") trust provider, depending on your needs.
2. Create a Verified Access [instance](verified-access-instances.md "verified-access-instances.md"), making sure to enable **Federal Information Process Standards (FIPS)** during the process. Also during creation, attach the **Verified Access trust provider** you created in the previous step, by selecting it from the drop down list.
3. Create a Verified Access [group](verified-access-groups.md "verified-access-groups.md"). During creation of the group, you associate it with the Verified Access instance just created.
4. Create one or more [Verified Access endpoints](verified-access-endpoints.md "verified-access-endpoints.md"). During the creation of your endpoint(s), you associate them with the group created in the previous step.
