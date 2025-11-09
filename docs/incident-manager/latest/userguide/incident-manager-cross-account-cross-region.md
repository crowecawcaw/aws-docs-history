AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Managing incidents across

AWS accounts and Regions in Incident Manager

You can configure Incident Manager, a tool in AWS Systems Manager, to work with multiple AWS Regions
and accounts. This section describes cross-Region and cross-account best practices, set up
steps, and known limitations.

###### Topics

- [Cross-Region incident management](#incident-manager-cross-region "#incident-manager-cross-region")
- [Cross-account incident
  management](#incident-manager-cross-account "#incident-manager-cross-account")

## Cross-Region incident management

Incident Manager supports automated and manual incident creation in [several
AWS Regions](../../../general/latest/gr/incident-manager.md "../../../general/latest/gr/incident-manager.md"). When you initially onboard with Incident Manager by using the
**Get prepared** wizard, you can specify up to three AWS Regions
for your _replication set_. For incidents automatically created by
Amazon CloudWatch alarms or Amazon EventBridge events, Incident Manager attempts to create an incident in the
same AWS Region as the event rule or alarm. If Incident Manager is experiencing an outage
in that Region, then CloudWatch or EventBridge automatically creates the incident in another Region
that your data is being replicated to.

###### Important

Note the following important details.

- We recommend that you specify at least two AWS Regions in your
  replication set. If you don't specify at least two Regions, the system will
  fail to create incidents during the period when Incident Manager is
  unavailable.
- Incidents created by a cross-Region failover don't invoke runbooks specified in response plans.

For more information about on-boarding with Incident Manager and specifying additional
Regions, see [Getting started with Incident Manager](getting-started.md "getting-started.md").

## Cross-account incident

management

Incident Manager uses AWS Resource Access Manager (AWS RAM) to share Incident Manager resources across management
and application accounts. This section describes cross-account best practices, how to
set up cross-account functionality for Incident Manager, and known limitations of
cross-account functionality in Incident Manager.

A management account is the account that you perform operations management from. In an
organization setup, the management account owns the response plans, contacts, escalation
plans, runbooks, and other AWS Systems Manager resources.

A application account is the account that owns the resources that make up your
applications. These resources can be Amazon EC2 instances, Amazon DynamoDB tables, or any of the
other resources that you use to build applications in the AWS Cloud. Application
accounts also own the Amazon CloudWatch alarms and Amazon EventBridge events that create incidents in
Incident Manager.

AWS RAM uses resource shares to share resources between accounts. You can share the
response plan and contact resources between accounts in AWS RAM. By sharing these
resources, application accounts and management accounts can interact with engagements
and incidents. Sharing a response plan shares all past and future incidents created
using that response plan. Sharing a contact shares all past and future engagements of
the contact or response plan.

### Best practices

Follow these best practices when sharing your Incident Manager resources across
accounts:

- Regularly update the resource share with response plans and
  contacts.
- Regularly review resource share principals.
- Set up Incident Manager, runbooks, and chat channels in your management
  account.

### Set up and configure

cross-account incident management

The following steps describe how to set up and configure Incident Manager resources and
use them for cross-account functionality. You may have configured some services and
resources for cross-account functionality in the past. Use these steps as a
checklist of requirements before starting your first incident using cross-account
resources.

1. (Optional) Create organizations and organizational units using AWS Organizations.
   Follow the steps in the [Tutorial:
   Creating and configuring an organization](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md") in the _AWS Organizations User Guide_.
2. (Optional) Use Quick Setup, a tools in AWS Systems Manager, to set up the correct
   AWS Identity and Access Management roles for you to use when configuring your cross-account runbooks.
   For more information, see [Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") in the
   _AWS Systems Manager User Guide_.
3. Follow the steps listed in [Running automations in multiple AWS Regions and accounts](../../../systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.md "../../../systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.md") in
   the _AWS Systems Manager User Guide_ to create runbooks in your Systems Manager
   automation documents. A runbook can be run by either a management account,
   or by one of your application accounts. Depending on your use case, you will
   need to install the appropriate AWS CloudFormation template for the roles necessary
   to create and view runbooks during an incident.
   - _Running a runbook in the management account._
     The management account must download and install the [AWS-SystemsManager-AutomationReadOnlyRole](https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemsManager-AutomationReadOnlyRole.zip "https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemsManager-AutomationReadOnlyRole.zip")
     CloudFormation template. When installing
     AWS-SystemsManager-AutomationReadOnlyRole,
     specify the account IDs of all application accounts. This role will
     let your application accounts read the status of the runbook from
     the incident details page. The application account must install the
     [AWS-SystemsManager-AutomationAdministrationReadOnlyRole](https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemManager-AutomationAdministrationReadOnlyRole.zip "https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemManager-AutomationAdministrationReadOnlyRole.zip")
     CloudFormation template. The incident details page uses this role to get
     the automation status from the management account.
   - _Running a runbook in a application account._
     The management account must download and install the [AWS-SystemsManager-AutomationAdministrationReadOnlyRole](https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemManager-AutomationAdministrationReadOnlyRole.zip "https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemManager-AutomationAdministrationReadOnlyRole.zip")
     CloudFormation template. This role allows the management account to read
     the status of the runbook in the application account. The
     application account must download and install the [AWS-SystemsManager-AutomationReadOnlyRole](https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemsManager-AutomationReadOnlyRole.zip "https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemsManager-AutomationReadOnlyRole.zip")
     CloudFormation template. When installing
     `AWS-SystemsManager-AutomationReadOnlyRole`, specify
     the account ID of the management account and other application
     accounts. The management account and other application accounts
     assume this role to read the status of the runbook.

4. (Optional) In each application account in the organization, download and
   install the [AWS-SystemsManager-IncidentManagerIncidentAccessServiceRole](https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemsManager-IncidentManagerIncidentAccessServiceRole.zip "https://s3.amazonaws.com/aws-incident-manager-assets.us-east-1/cross-account-setup/AWS-SystemsManager-IncidentManagerIncidentAccessServiceRole.zip")
   CloudFormation template. When installing
   AWS-SystemsManager-IncidentManagerIncidentAccessServiceRole,
   specify the account ID of the management account. This role provides the
   permissions that Incident Manager needs to access information about AWS CodeDeploy
   deployments and AWS CloudFormation stack updates. This information is reported as
   _findings_ for an incident if the
   Findings feature is enabled. For more information, see [Identifying potential causes of incidents from other services as
   "findings" in Incident Manager](findings.md "findings.md").
5. To set up and create contacts, escalation plans, chat channels, and
   response plans, follow the steps detailed in [Preparing for incidents in Incident Manager](incident-response.md "incident-response.md").
6. Add your contacts and response plan resources to either your existing
   resource share or a new resource share in AWS RAM. For more information, see
   [Getting started with
   AWS RAM](../../../ram/latest/userguide/getting-started.md "../../../ram/latest/userguide/getting-started.md") in the _AWS RAM User Guide_. Adding
   response plans to AWS RAM enables application accounts to access incidents and
   incident dashboards created using the response plans. Application accounts
   also gain the ability to associate CloudWatch alarms and EventBridge events to a response
   plan. Adding the contacts and escalation plans to AWS RAM enables application
   accounts to view engagements and engage contacts from the incident
   dashboard.
7. Add cross-account cross-Region functionality to your CloudWatch console. For
   steps and information, see [Cross-account cross-Region CloudWatch console](../../../AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.md "../../../AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.md") in the _Amazon CloudWatch User Guide_. Adding this functionality
   ensures that the application accounts and management account you've created
   can view and edit metrics from the incident and analysis dashboards.
8. Create a cross-account Amazon EventBridge event bus. For steps and information, see
   [Sending and
   receiving Amazon EventBridge events between AWS accounts](../../../eventbridge/latest/userguide/eb-cross-account.md "../../../eventbridge/latest/userguide/eb-cross-account.md"). You can then
   use this event bus to create event rules that detect incidents in
   application accounts and create incidents in the management account.

### Limitations

The following are known limitations of Incident Manager's cross-account
functionality:

- The account that creates a post-incident analysis is the only account that
  can view and change it. If you use a application account to create a
  post-incident analysis, only members of that account can view and change it.
  The same is true if you use a management account to create a post-incident
  analysis.
- Timeline events aren't populated for automation documents run in
  application accounts. Updates of automation documents run in application
  accounts are visible in the **Runbook** tab of the
  incident.

- Amazon Simple Notification Service topics can't be used cross-account. Amazon SNS topics must be created
  in the same Region and account as the response plan it's used in. We
  recommend using the management account to create all SNS topics and response
  plans.
- Escalation plans can only be created using contacts in the same account. A
  contact that has been shared with you can't be added to an escalation plan
  in your account.
- Tags applied to response plans, incident records, and contacts can only be
  viewed and modified from the resource owner account.
