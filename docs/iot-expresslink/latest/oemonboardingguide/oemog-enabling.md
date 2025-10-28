# Enable onboarding-by-claim

In order for a product to take advantage of the onboarding-by-claim process, the OEM must
ensure that the following components are available and properly configured:

- A registration (web) portal or mobile application.
- The claim-script - this sends the new endpoint to the selected device inside
  the staging account.
- The customer/OEM account - this must be properly configured to support just-in-time
  provisioning.
  The following sections explain how these components operates, and describe how to
  properly configure, and provide implementation examples.

## Create a registration application

The registration application is a software product that is (ideally) completely customized
for the specific OEM product and brand. It requests the end-user to input the device's unique
identifier, and then launches the claim-script that provides the device with a new target
endpoint.

Note that the registration portal can be responsible for collecting additional end-user
information, such as the end-user's location, and for including personally identifiable information
that can be used by the application's location to select a target endpoint among several
alterantives (if the OEM controls multiple AWS accounts). This also makes it possible to
optimize the end-user experience and reduce latency (by selecting the most appopriate region,
for example). The logic used, and any additional information optionally collected, are
completely outside the scope of this document and are not essential to the onboarding
process.

For an example implementation of a basic (web) registration portal, refer to the
[claim provisioning reference implementation](samples/el-claim-provisioning-ref-impl.md "samples/el-claim-provisioning-ref-impl.md") (download).
