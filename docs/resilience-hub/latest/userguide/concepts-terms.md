# AWS Resilience Hub concepts

These concepts can help you better understand the AWS Resilience Hub's approach to helping improve
application resiliency and prevent application outages.

## Resiliency

The ability to maintain availability and to recover from software and operational
disruption in a designated time frame.

## Recovery point objective (RPO)

The maximum acceptable amount of time since the last data recovery point. This determines
what is considered an acceptable loss of data between the last recovery point and the
interruption of service.

## Recovery time objective (RTO)

The maximum acceptable delay between the interruption of service and restoration of
service. This determines what is considered an acceptable time window when service is
unavailable.

## Estimated workload recovery time objective

The estimated workload recovery time objective (estimated workload RTO) is the RTO that
your application is estimated to meet based on the imported application definition and then run
an assessment.

## Estimated workload recovery point objective

The estimated workload recovery point objective (estimated workload RPO) is the RPO that
your application is estimated to meet based on the imported application definition and then run
an assessment.

## Application

An AWS Resilience Hub application is a collection of AWS supported resources that are continuously
monitored and assessed to manage its resiliency posture.

## Application Component

A group of related AWS resources that work and fail as a single unit. For example, if you
have a primary and replica database, then both databases belong to the same Application
Component (AppComponent).

AWS Resilience Hub determines which AWS resources can belong to which type of AppComponent. For
example, a `DBInstance` can belong to
`AWS::ResilienceHub::DatabaseAppComponent` but not to
`AWS::ResilienceHub::ComputeAppComponent`.

## Application compliance status

AWS Resilience Hub reports the following compliance status types for your applications.

**Policy met**

The application is estimated to meet its RTO and RPO targets defined in the policy. All its
components meet the defined policy objectives. For example, you selected an RTO and RPO target
of 24 hours for disruptions across AWS Regions. AWS Resilience Hub can see that your backups are copied
to your fallback Region. You are still expected to maintain a recover from a backup standard
operating procedure (SOP), and to test and time it. This is in the operational recommendations
and part of your overall resiliency score.

**Policy breached**

The application could not be estimated to meet the RTO and RPO targets defined in the
policy. One or more of its AppComponents do not satisfy the policy objectives. For example, you
selected an RTO and RPO target of 24 hours for disruptions across AWS Regions, but your
database configuration does not include any cross-Region recovery method, such as a global
replication and backup copies.

**Not assessed**

The application requires an assessment. It's not currently assessed or tracked.

**Changes detected**

There is a new published version of the application that has not yet been assessed.

## Drift detection

AWS Resilience Hub runs drift notification while running an assessment for your application to check
if the changes in AppComponent configurations have affected the compliance status of your
application. In addition, it also checks and detects changes such as addition or deletion of
resources within the application's input sources and notifies about the same. For comparison,
AWS Resilience Hub uses the previous assessment in which the application component met the policy.
AWS Resilience Hub detects the following types of drifts:

- **Application policy drift** – This drift type identifies all the
  AppComponents that complied with the policy in the previous assessment but failed to comply in
  the current assessment.
- **Application resource drift** – This drift type identifies all
  the drifted resources in the current application version.

## Resiliency assessment

AWS Resilience Hub uses a list of gaps and potential remedies to measure the effectiveness of a
selected policy to recover and continue from a disaster. It evaluates each Application Component
or application compliance status with the policy. This report includes cost optimization
recommendations and references to potential issues.

## Resiliency score

AWS Resilience Hub generates a score that indicates how closely your application follows our
recommendations for meeting the application's resiliency policy, alarms, standard operating
procedures (SOPs), and tests.

## Disruption type

AWS Resilience Hub helps you assess resiliency against the following types of outages:

**Application**

The infrastructure is healthy, but the application or software stack doesn't operate as
needed. This may occur after deployment of new code, configuration changes, data corruption, or
malfunction of downstream dependencies.

**Cloud Infrastructure**

The cloud infrastructure is not functioning as expected because of an outage. An outage may
occur because of a local error in one or more components. In most cases, this type of outage is
resolved by rebooting, recycling, or reloading the faulty components.

**Cloud Infrastructure AZ disruption**

One or more Availability Zones are unavailable. This type of outage can be resolved by
switching to a different Availability Zone.

**Cloud Infrastructure Region incident**

One or more Regions are unavailable. This type of incident can be resolved by switching to
a different AWS Region.

## AWS FIS experiments

AWS Resilience Hub recommends experiments using AWS FIS actions to verify application resiliency
against different types of outages. These outages include application, infrastructure,
Availability Zones (AZ), or AWS Region incidents of Application Components.

These experiments let you do the following:

- Inject a failure.
- Verify that alarms can detect an outage.
- Verify that recovery procedures, or standard operating procedures (SOPs), work correctly
  to recover the application from the outage.

Tests for SOPs measure estimated workload RTO and estimated workload RPO. You can test
different application configurations and measure whether the output RTO and RPO meets the
objectives defined in your policy.

## SOP

A standard operating procedure (SOP) is a prescriptive set of steps that are designed to
efficiently recover your application in the event of an outage or an alarm. Based on the
application assessment, AWS Resilience Hub recommends a set of SOPs and it is recommended to prepare,
test, and measure SOPs in advance of a disruption to ensure timely recovery.
