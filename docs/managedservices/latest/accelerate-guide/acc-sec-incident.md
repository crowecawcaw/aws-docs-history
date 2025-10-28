# Incident response in Accelerate

Upon receiving an alert, the AMS team uses automated and manual remediations to bring the
resources back to a healthy state. If remediation fails, AMS starts the incident management process to
collaborate with your team. You can change the baselines by updating the default configuration in a configuration file.

## Incident response and onboarding in AMS Accelerate

During onboarding, AMS Accelerate suppresses automatic incident creation for your existing
noncompliant resources; instead, your Cloud Service Deliver Manager (CSDM) provides you with a report that
contains all the noncompliance rules and resources for your review. After you have identified the rules that
you want AMS to remediate, create a service request in the Support Center console indicating
those rule and resources. The following Service Request template is an example of a customer request to
AMS to manually remediate noncompliant resources. If AMS has additional questions, we work
with you in the Service Request to gather the information required.

```
Hello,
Please remediate the following resources for the Config Rule "ENCRYPTED_VOLUMES".
Resource List:
    "Vol-12345678"
    "Vol-87654312"
Thank you
```

After the onboarding process is completed, AMS Accelerate automatically creates an incident for each
noncompliant resource for the rules marked as Automatic Incident.
