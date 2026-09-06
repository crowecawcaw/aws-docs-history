

# Setting up Organizations integration
<a name="next-gen-delegated-admin-setup"></a>

To use the next generation of Resilience Hub with AWS Organizations, you must designate a delegated administrator account that manages organization-wide policies and visibility.

**Prerequisites**
+ AWS Organizations must be configured with all features enabled.
+ You must have access to the management account to enable trusted access.
+ Identify which member account will serve as the delegated administrator.
+ The management account must create the Service-Linked Role (SLR) for the Organizations integration to function. Without the SLR, the delegated administrator cannot access member account data.

**Important**  
The management account must create the Service-Linked Role (SLR) during setup. The Organizations integration does not function without the SLR, and the delegated administrator cannot access member account data until the SLR is created.

**Quick setup steps**

1. From the **management account**, open the the next generation of Resilience Hub console and choose **AWS Organizations settings**.

1. Select the checkboxes to enable trusted access and create the Service-Linked Role (SLR).

1. Choose **Create integration**.

1. (Optional) Register a delegated administrator by choosing **Register** on the same page.

1. From the **delegated administrator account**, select the home region in the the next generation of Resilience Hub console.

1. Individual service owners in member accounts create their own invoker roles for their services. For invoker role setup, see [Setting up Next generation Resilience Hub](next-gen-setting-up.md).

After setup completes, Next generation Resilience Hub performs the following actions:

1. Service-Linked Roles are created in all member accounts. This may take additional time for large organizations due to API throttling.

1. Next generation Resilience Hub fetches the initial organization structure.

1. The DA account gains cross-account visibility through the SLRs.

1. Organization structure sync begins (event-driven plus a 12-hour reconciliation job).