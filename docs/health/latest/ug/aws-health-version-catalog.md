

# Version catalog for AWS Health
<a name="aws-health-version-catalog"></a>

Learn about the version catalog for AWS Health, which provides a service-wide view of supported versions and their timelines.

**Topics**
+ [What is the version catalog?](#what-is-the-version-catalog)
+ [What you can do with the version catalog](#what-can-i-use-the-version-catalog-for)
+ [How to access the version catalog](#accessing-the-version-catalog)
+ [Details available in the version catalog](#version-catalog-details)
+ [How to retrieve the version catalog information with the API](#version-catalog-using-the-api)
+ [How to view the version catalog in the Health Dashboard](#version-catalog-using-the-dashboard)

## What is the version catalog?
<a name="what-is-the-version-catalog"></a>

If you run applications on AWS, you must stay current with software versions to maintain a strong security and operational posture. AWS Health already sends account-specific and resource-specific [Planned lifecycle events for AWS Health](aws-health-planned-lifecycle-events.md) well in advance of major version end-of-support milestones. The version catalog adds a service-wide view of supported versions and their timelines. You can use this view to build upgrade schedules and governance controls, and to move to newer supported versions before you receive an account-specific planned lifecycle event.

The version lifecycle API aggregates this information into a single, consistent schema. With one authenticated API call, you can query the support timeline of a specific release of an AWS service component, such as an AWS Lambda language runtime, an Amazon Relational Database Service (Amazon RDS) engine version, or an Amazon Elastic Kubernetes Service (Amazon EKS) Kubernetes version.

Use this data to build upgrade dashboards, alert on versions that approach end of support, and automate compliance checks for the versions that you run. You can also reduce technical debt by moving to newer supported versions before you receive an account-specific planned lifecycle event.

## What you can do with the version catalog
<a name="what-can-i-use-the-version-catalog-for"></a>

The version lifecycle API gives you programmatic access to understand where every AWS service component sits in its support timeline. Common use cases include the following:
+ **Vulnerability and compliance management** – Identify software running past its end of life that no longer receives security patches (for example, Python 3.9 reached end of life in October 2025), and feed end-of-life data into compliance dashboards for PCI DSS, SOC 2, and FedRAMP audits.
+ **Infrastructure and fleet inventory auditing** – Cross-reference your configuration management database (CMDB) or resource inventory to flag unsupported database engines (Amazon RDS PostgreSQL, MySQL) or Lambda runtimes (Node.js, Java, .NET). This is especially useful for AWS-managed services, because the catalog tracks Amazon EKS, Amazon Aurora (Aurora) MySQL and PostgreSQL, Amazon RDS, Amazon OpenSearch Service, Amazon ElastiCache, Lambda runtimes, and more.
+ **Proactive upgrade planning** – Build migration timelines and programs, and generate roadmaps that show when each dependency exits support relative to its active development phases.
+ **CI/CD pipeline automation** – Integrate the API into your pipelines to fail builds or raise warnings when a project depends on a runtime or framework that is at or near end of life. You can also maintain a test matrix automatically (for example, test against all actively supported Python versions) without hardcoding version lists.
+ **Developer tooling and dashboards** – Power internal operational dashboards that show the support status of every component used in a specific workload.
+ **AWS service lifecycle tracking** – Track AWS-managed service versions, such as Amazon EKS and Lambda, and prepare for forced upgrades before they occur.

## How to access the version catalog
<a name="accessing-the-version-catalog"></a>

You can view the version catalog in two ways:
+ **Health Dashboard** – View supported versions and their lifecycle timelines directly in the console.
+ **AWS Health API** – Customers on AWS Support can call the `DescribeServiceLifecycle` API to integrate lifecycle data into their operational workflows.

See the [AWS Health API Reference](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeServiceLifecycle.html) for full details.

## Details available in the version catalog
<a name="version-catalog-details"></a>

Each version in a response provides an overview and a timeline toward the various phases in the lifecycle.

### Top-level version entry
<a name="version-catalog-top-level-entry"></a>


| Field | Description | 
| --- | --- | 
| `service` | The AWS service that the version belongs to, for example, `LAMBDA`, `RDS`, or `EKS`. | 
| `title` | The human-readable name of the version, for example, `Python 3.14 Lambda Runtime`. | 
| `version` | The service-specific version identifier that you pass in queries, for example, `python3.14`. | 
| `lifecycleEvents` | A list of lifecycle events for this version, in chronological order. Each event marks a significant date, such as a release, an end of standard support, or an end of life, and includes impact-risk tags that indicate the consequence of that date passing. Read the events in order to understand the full timeline from release through end of support. | 

### Lifecycle event object
<a name="version-catalog-lifecycle-event-object"></a>


| Field | Description | 
| --- | --- | 
| `lifecycleEventType` | The milestone type, for example, `END_OF_SUPPORT`, `BLOCK_RESOURCE_CREATE`, or `BLOCK_RESOURCE_UPDATE`. | 
| `date` | The date when the milestone takes effect. | 
| `description` | A human-readable explanation of what happens on this date. | 
| `impactRisks` | One or more impact-risk tags, such as `END_OF_SUPPORT`, `BILLING`, or `AVAILABILITY`, that indicate what stops working when the date passes. | 
| `regions` | The Regions that the event applies to. A value of `["all"]` means all Regions. | 

**Note**  
The values shown for `lifecycleEventType` and `impactRisks` are those visible in this example. See the [AWS Health API Reference](https://docs.aws.amazon.com/health/latest/APIReference/API_LifecycleEvent.html) for the complete list of possible values.

### Impact-risk tags
<a name="version-catalog-impact-risk-tags"></a>

Each event lists one or more impact-risk tags so that you can assess severity. `AVAILABILITY` impacts are the most urgent, because the resource becomes unavailable after that date passes.


| Tag | Meaning | 
| --- | --- | 
| `END_OF_SUPPORT` | The version no longer receives security patches or updates. | 
| `BILLING` | Continuing to run this version might incur additional charges, for example, extended-support fees. | 
| `AVAILABILITY` | The resource becomes unavailable after the date passes. This is the most urgent impact. | 

## How to retrieve the version catalog information with the API
<a name="version-catalog-using-the-api"></a>

Query the lifecycle information by using the AWS Command Line Interface (AWS CLI).

```
aws health describe-service-lifecycle
```

The following example shows a version entry from the `DescribeServiceLifecycle` API.

```
{
  "service": "LAMBDA",
  "title": "Python 3.14 Lambda Runtime",
  "version": "python3.14",
  "lifecycleEvents": [
    {
      "lifecycleEventType": "END_OF_SUPPORT",
      "date": 1877472000.0,
      "description": "Runtime no longer receives security patches or updates",
      "impactRisks": ["END_OF_SUPPORT"],
      "regions": ["all"]
    },
    {
      "lifecycleEventType": "BLOCK_RESOURCE_CREATE",
      "date": 1880150400.0,
      "description": "Cannot create new Lambda functions using this runtime",
      "impactRisks": ["AVAILABILITY"],
      "regions": ["all"]
    },
    {
      "lifecycleEventType": "BLOCK_RESOURCE_UPDATE",
      "date": 1882828800.0,
      "description": "Cannot update existing Lambda functions using this runtime",
      "impactRisks": ["AVAILABILITY"],
      "regions": ["all"]
    }
  ]
}
```

## How to view the version catalog in the Health Dashboard
<a name="version-catalog-using-the-dashboard"></a>

The following shows the version catalog feature in the Health Dashboard.

![The version catalog in the Health Dashboard, showing a table with Service, Resource, and Version columns, and a side pane with the selected version's timeline of lifecycle events.](https://docs.aws.amazon.com/health/latest/ug/images/health-version-catalog-console.png)
