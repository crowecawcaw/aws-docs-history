# What we do, what we do not do

AMS gives you a standardized approach to deploying AWS infrastructure and provides the necessary ongoing
operational management. For a full description of roles, responsibilities, and supported services, see
[Service Description](../userguide/ams-sd.md "../userguide/ams-sd.md").

###### Note

To request that AMS provide an additional AWS service, file a service request. For more information, see
[Making Service Requests](../userguide/mk-service-requests.md "../userguide/mk-service-requests.md").

- **What we do**:

After you complete onboarding, the AMS environment is available
to receive requests for change (RFCs), incidents, and service requests. Your interaction with
the AMS service revolves around the lifecycle of an application stack. New stacks
are ordered from a preconfigured list of templates, launched into specific virtual
private cloud (VPC) subnets, modified during their operational life through requests for change (RFCs),
and monitored for events and incidents 24/7.

Active application stacks are monitored and maintained by AMS, including patching, and require no
further action for the life of the stack unless a change is required or the stack
is decommissioned. Incidents detected by AMS that affect the health and function
of the stack generate a notification and may or may not need your action to resolve or verify.
How-to questions and other inquiries can be made by submitting a service request.

Additionally, AMS allows you to enable compatible AWS services that are not
managed by AMS. For information about AWS-AMS compatible services, see
[Self-service provisioning mode](../userguide/setting-up-compatible.md "../userguide/setting-up-compatible.md").

- **What we DON'T do**:

While AMS simplifies application deployment by providing a number of manual and automated options, you're responsible
for the development, testing, updating, and management of your application. AMS provides troubleshooting assistance for
infrastructure issues that impact applications, but AMS can't access or validate
your application configurations.
