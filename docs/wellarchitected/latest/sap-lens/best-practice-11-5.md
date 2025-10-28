# Best Practice 11.5 – Automate reaction

to failure

You can minimize the impact to service by automating the response to failure. Design
automation to respond to failure, impaired capacity, or loss of connectivity. Ensure clear
arbitration criteria are defined to avoid false positives.

**Suggestion 11.5.1 – Evaluate your automation for application
awareness**

For automation solutions that protect an application, evaluate the impact on state – for
example, connected user sessions, logon targets, data replication consistency, and data
corruption risk.

**Suggestion 11.5.2 – Evaluate the health check mechanisms that
initiate automation**

Health checks should be designed with controls to help ensure that automations are not
started because of false positives.

Where possible, rely on the data plane over the control plane for resilience. The
control plane is used to configure resources, and the data plane delivers services. Data
planes typically have higher availability design goals than control planes and are usually
less complex.

- AWS Documentation: [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/")
