# Best Practice 4.1 – Understand and

plan for lifecycle events of your SAP workload

SAP workloads are highly reliant on SAP to provide new software and vulnerability
patching, operating system and database kernels, and escalation for support. SAP regularly
publishes information about SAP software releases: Release types, maintenance durations,
planned availability, and upgrade paths in their [Product Availability
Matrix (PAM)](https://support.sap.com/en/release-upgrade-maintenance.html "https://support.sap.com/en/release-upgrade-maintenance.html") and SAP Notes. You should obtain specific details each of your SAP
applications and track these locally to understand if your SAP software is current,
supported and when it will be end of life from a maintenance perspective.

The PAM also offers information about platform availability and compatibility:
including database platform and operating systems supported which should guide you in
patching and upgrading these underlying components of your SAP workload. Operating System
vendors also have their own patching and support lifecycle which should be taken into
account when planning SAP maintenance and lifecycle events such as upgrades.

**Suggestion 4.1.1 - Create an operational roadmap for your SAP
applications taking into account key support and lifecycle dates**

List all of your SAP software applications, kernel versions. operating systems, and
database versions in a central register and consolidate with PAM information on supported
versions and maintenance windows. Use this list as a consolidated view to plan patching,
upgrades and platform changes in all components required to keep SAP current and within
support.

- SAP Documentation: [SAP Release &
  Maintenance Strategy: Product Availability Matrix](https://support.sap.com/en/release-upgrade-maintenance.html "https://support.sap.com/en/release-upgrade-maintenance.html") [Requires SAP Portal
  Access]

**Suggestion 4.1.2 - Maintain a calendar for expiring of credentials,
certificates and licenses**

Alongside the major SAP lifecycle events and patching mentioned previously, ensure
you have an operational calendar which plans minor system events. Examples of these
maintenance events could be expiry of system credentials, expiry of certificates (for
example, for STRUST integration between systems) and any license renewal work or updates
required (for example, temporary SAP or database licenses for migration, development or
POC purposes).

- AWS Documentation: [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")

**Suggestion 4.1.3 - Plan for upgrades or alternatives before SAP
software becomes end of life**

Create an SAP landscape roadmap visualizing your key SAP lifecycle events and
operational upkeep - patching, software upgrades, migrations and re-platforming if
required. Communicate this lifecycle calendar to business and technical stakeholders. Plan
investment to fund these SAP lifecycle activities/projects. Plan in advance with your
business stakeholders where maintenance windows can occur and downtime or restarts will be
required.

- SAP Documentation: [SAP
  Roadmap Explorer](https://www.sap.com/products/roadmaps.html "https://www.sap.com/products/roadmaps.html")

**Suggestion 4.1.4 - Stay up to date and subscribe to key SAP notes
for support advice**

Subscribe to key SAP notes and Knowledge Base Articles (KBAs) for your SAP workload
such that you will be notified upon any changes or updates to supportability and advice.
Use “Favorite” SAP notes functionality to keep a list of frequently accessed and important
notes for your SAP workload to make them easily accessible and comparable.

- [SAP Support
  Portal - Favorite SAP Notes](https://launchpad.support.sap.com/#/mynotes?tab=Favorites "https://launchpad.support.sap.com/#/mynotes?tab=Favorites") [Requires SAP Portal Access]
