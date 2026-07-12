# Actions, resources, and condition keys for AWS services

Each AWS service can define API operations, actions, resources, and condition context
keys for use in IAM policies. This topic describes how the elements provided for each
service are documented.

Each topic consists of tables that provide the list of available operations, actions,
resources, and condition keys.

## The operations table

The **Operations** table lists the API operations defined by the
service and maps each one to the IAM actions that authorize it. A single operation can
authorize more than one IAM action. Some services do not yet have an operations table.
This does not mean there are no operations for that service. This table does not yet
include actions that downstream services authorize through [forward access sessions](access_forward_access_sessions.md "access_forward_access_sessions.md").

- The **Operation** column lists the name of the
  API operation. When an operation authorizes multiple actions, the operation
  name spans the rows for all of its authorized actions.
- The **IAM action** column lists each IAM
  action authorized by the operation, in the form
  `service:ActionName`. When the action belongs to the same service as
  the operation, the entry links to that action's row in the
  **Actions** table on the same page. When the action belongs to
  a different service, the entry links to that service's authorization reference
  page.
- The **Condition key** and **Possible value(s)** columns list only the condition keys that
  this operation sets to a fixed, known value when it authorizes this action,
  along with the value it sets. This is not the full set of condition keys that may
  be available during authorization. The keys
  shown are the ones with values determined statically by the API itself. For the full set of condition keys supported by the
  action, see the [Actions table](#actions_table "#actions_table") and the
  [Condition keys table](#context_keys_table "#context_keys_table") on the same page.
- The **Access level** column shows the access
  level classification of the authorized action. For more information about access levels, see [Understanding access level summaries within policy
  summaries](access_policies_understand-policy-summary-access-level-summaries.md "access_policies_understand-policy-summary-access-level-summaries.md").

## The actions table

The **Actions** table lists all the actions that you can use in an
IAM policy statement's `Action` element. Some services include
permission-only actions that don't directly correspond to an API operation. These
actions are listed in a separate **Permission-only actions** table on
the same page. Use these tables to determine which actions you can use in an IAM policy.
For more information about the `Action`, `Resource`, or
`Condition` elements, see [IAM
JSON policy elements reference](reference_policies_elements.md "reference_policies_elements.md"). The **Actions** and
**Description** table columns are self-descriptive.

- The **Access level** column describes how the
  action is classified (List, Read, Write, Permissions management, or Tagging).
  This classification can help you understand the level of access that an action
  grants when you use it in a policy. For more information about access levels,
  see [Understanding access level summaries within policy
  summaries](access_policies_understand-policy-summary-access-level-summaries.md "access_policies_understand-policy-summary-access-level-summaries.md").
- The **Resource types** column indicates whether
  the action supports resource-level permissions. If the column is empty, then the
  action does not support resource-level permissions and you must specify all
  resources ("\*") in your policy. If the column includes a resource type, then you
  can specify the resource ARN in the `Resource` element of your
  policy. For more information about that resource, refer to that row in the
  **Resource types** table. All actions and resources that
  are included in one statement must be compatible with each other. If you specify
  a resource that is not valid for the action, any request to use that action
  fails, and the statement's `Effect` does not apply.

Required resources are indicated in the table with an asterisk (\*). If you
specify a resource-level permission ARN in a statement using this action, then
it must be of this type. Some actions support multiple resource types. If the
resource type is optional (not indicated as required), then you can choose to
use one but not the other.

- The **Condition keys** column includes keys that
  you can specify in a policy statement's `Condition` element.
  Condition keys might be supported with an action, or with an action and a
  specific resource. Pay close attention to whether the key is in the same row as
  a specific resource type. This table does not include global condition keys that
  are available for any action or under unrelated circumstances. For more
  information about global condition keys, see [AWS global condition keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").

## The resource types table

The **Resource types** table lists all the resource types that you
can specify as an ARN in the `Resource` policy element. Not every resource
type can be specified with every action. Some resource types work with only certain
actions. For more
information about the `Resource` element, see [IAM JSON policy elements: Resource](reference_policies_elements_resource.md "reference_policies_elements_resource.md").

- The **ARN** column specifies the Amazon Resource Name (ARN)
  format that you must use to reference resources of this type. The portions that
  are preceded by a $ must be replaced by the actual values for your scenario. For
 example, if you see `$user-name` in an ARN, you must replace that
  string with either the actual user's name or a [policy variable](reference_policies_variables.md "reference_policies_variables.md") that contains a user's name. For more information
  about ARNs, see [IAM ARNs](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns").
- The **Condition keys** column specifies condition context
  keys that you can include in an IAM policy statement only when both this
  resource and a supporting action from the table above are included in the
  statement.

## The condition keys table

The **condition keys** table lists all of the condition keys
that you can use in an IAM policy statement's `Condition` element. Not
every key can be specified with every action or resource. Certain keys only work with
certain types of actions and resources. For more information about the
`Condition` element, see [IAM JSON policy elements: Condition](reference_policies_elements_condition.md "reference_policies_elements_condition.md").

- The **Type** column specifies the data type of the condition
  key. This data type determines which [condition operators](reference_policies_elements_condition_operators.md "reference_policies_elements_condition_operators.md") you can use to compare values in the request
  with the values in the policy statement. You must use an operator that is
  appropriate for the data type. If you use an incorrect operator, then the match
  always fails and the policy statement never applies.

If the **Type** column specifies "ArrayOf.." one of the
simple types, then you must use [multivalued set operators](reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys "reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys") in your policies. Use the `ForAllValues` prefix to
specify that **all** values in the request must
match a value in the policy statement. Use the `ForAnyValue` prefix
to specify that **at least one** value in the
request matches one of the values in the policy statement.

###### Topics

- [AWS Billing Conductor (billingconductor)](list_billingconductor.md "list_billingconductor.md")
- [AWS Cloud Control API (cloudformation)](list_cloudcontrol.md "list_cloudcontrol.md")
- [AWS Cloud Map (servicediscovery)](list_servicediscovery.md "list_servicediscovery.md")
- [AWS Account Management (account)](list_account.md "list_account.md")
- [AWS Action Recommendations (action-recommendations)](list_action-recommendations.md "list_action-recommendations.md")
- [AWS Activate (activate)](list_activate.md "list_activate.md")
- [AWS Amplify (amplify)](list_amplify.md "list_amplify.md")
- [AWS Amplify Admin (amplifybackend)](list_amplifybackend.md "list_amplifybackend.md")
- [AWS Amplify UI Builder (amplifyuibuilder)](list_amplifyuibuilder.md "list_amplifyuibuilder.md")
- [AWS App Mesh (appmesh)](list_appmesh.md "list_appmesh.md")
- [AWS App Mesh Preview (appmesh-preview)](list_appmesh-preview.md "list_appmesh-preview.md")
- [AWS App Runner (apprunner)](list_apprunner.md "list_apprunner.md")
- [AWS App Studio (appstudio)](list_appstudio.md "list_appstudio.md")
- [AWS App2Container (a2c)](list_a2c.md "list_a2c.md")
- [AWS AppConfig (appconfig)](list_appconfig.md "list_appconfig.md")
- [AWS AppFabric (appfabric)](list_appfabric.md "list_appfabric.md")
- [AWS Application Auto Scaling (application-autoscaling)](list_application-autoscaling.md "list_application-autoscaling.md")
- [AWS Application Discovery Service (discovery)](list_discovery.md "list_discovery.md")
- [AWS Application Migration Service (mgn)](list_mgn.md "list_mgn.md")
- [AWS Application Transformation Service (application-transformation)](list_application-transformation.md "list_application-transformation.md")
- [AWS AppSync (appsync)](list_appsync.md "list_appsync.md")
- [AWS Artifact (artifact)](list_artifact.md "list_artifact.md")
- [AWS Audit Manager (auditmanager)](list_auditmanager.md "list_auditmanager.md")
- [AWS Auto Scaling (autoscaling-plans)](list_autoscaling-plans.md "list_autoscaling-plans.md")
- [AWS B2B Data Interchange (b2bi)](list_b2bi.md "list_b2bi.md")
- [AWS Backup (backup)](list_backup.md "list_backup.md")
- [AWS Backup Gateway (backup-gateway)](list_backup-gateway.md "list_backup-gateway.md")
- [AWS Backup Search (backup-search)](list_backupsearch.md "list_backupsearch.md")
- [AWS Backup storage (backup-storage)](list_backup-storage.md "list_backup-storage.md")
- [AWS Batch (batch)](list_batch.md "list_batch.md")
- [AWS Budget Service (budgets)](list_budgets.md "list_budgets.md")
- [AWS BugBust (bugbust)](list_bugbust.md "list_bugbust.md")
- [AWS Certificate Manager (acm)](list_acm.md "list_acm.md")
- [AWS Chatbot (chatbot)](list_chatbot.md "list_chatbot.md")
- [AWS Clean Rooms (cleanrooms)](list_cleanrooms.md "list_cleanrooms.md")
- [AWS Clean Rooms ML (cleanrooms-ml)](list_cleanroomsml.md "list_cleanroomsml.md")
- [AWS Cloud9 (cloud9)](list_cloud9.md "list_cloud9.md")
- [AWS CloudFormation (cloudformation)](list_cloudformation.md "list_cloudformation.md")
- [AWS CloudHSM (cloudhsm)](list_cloudhsm.md "list_cloudhsm.md")
- [AWS CloudShell (cloudshell)](list_cloudshell.md "list_cloudshell.md")
- [AWS CloudTrail (cloudtrail)](list_cloudtrail.md "list_cloudtrail.md")
- [AWS CloudTrail Data (cloudtrail-data)](list_cloudtrail-data.md "list_cloudtrail-data.md")
- [AWS CloudWatch RUM (rum)](list_rum.md "list_rum.md")
- [AWS CodeArtifact (codeartifact)](list_codeartifact.md "list_codeartifact.md")
- [AWS CodeBuild (codebuild)](list_codebuild.md "list_codebuild.md")
- [AWS CodeCommit (codecommit)](list_codecommit.md "list_codecommit.md")
- [AWS CodeConnections (codeconnections)](list_codeconnections.md "list_codeconnections.md")
- [AWS CodeDeploy (codedeploy)](list_codedeploy.md "list_codedeploy.md")
- [AWS CodeDeploy secure host commands service (codedeploy-commands-secure)](list_codedeploy-commands-secure.md "list_codedeploy-commands-secure.md")
- [AWS CodePipeline (codepipeline)](list_codepipeline.md "list_codepipeline.md")
- [AWS CodeStar (codestar)](list_codestar.md "list_codestar.md")
- [AWS CodeStar Connections (codestar-connections)](list_codestar-connections.md "list_codestar-connections.md")
- [AWS CodeStar Notifications (codestar-notifications)](list_codestar-notifications.md "list_codestar-notifications.md")
- [AWS Compute Optimizer (compute-optimizer)](list_compute-optimizer.md "list_compute-optimizer.md")
- [AWS Compute Optimizer Automation (aco-automation)](list_compute-optimizer-automation.md "list_compute-optimizer-automation.md")
- [AWS Config (config)](list_config.md "list_config.md")
- [AWS Connector Service (awsconnector)](list_awsconnector.md "list_awsconnector.md")
- [AWS Consolidated Billing (consolidatedbilling)](list_consolidatedbilling.md "list_consolidatedbilling.md")
- [AWS Control Catalog (controlcatalog)](list_controlcatalog.md "list_controlcatalog.md")
- [AWS Control Tower (controltower)](list_controltower.md "list_controltower.md")
- [AWS Cost and Usage Report (cur)](list_cur.md "list_cur.md")
- [AWS Cost Explorer Service (ce)](list_ce.md "list_ce.md")
- [AWS Cost Optimization Hub (cost-optimization-hub)](list_cost-optimization-hub.md "list_cost-optimization-hub.md")
- [AWS Customer Verification Service (customer-verification)](list_customer-verification.md "list_customer-verification.md")
- [AWS Data Exchange (dataexchange)](list_dataexchange.md "list_dataexchange.md")
- [AWS Data Pipeline (datapipeline)](list_datapipeline.md "list_datapipeline.md")
- [AWS Database Migration Service (dms)](list_dms.md "list_dms.md")
- [AWS DataSync (datasync)](list_datasync.md "list_datasync.md")
- [AWS Deadline Cloud (deadline)](list_deadline.md "list_deadline.md")
- [AWS Device Farm (devicefarm)](list_devicefarm.md "list_devicefarm.md")
- [AWS DevOps Agent Service (aidevops)](list_devops-agent.md "list_devops-agent.md")
- [AWS Diagnostic tools (ts)](list_ts.md "list_ts.md")
- [AWS Direct Connect (directconnect)](list_directconnect.md "list_directconnect.md")
- [AWS Directory Service (ds)](list_ds.md "list_ds.md")
- [AWS Directory Service Data (ds-data)](list_ds-data.md "list_ds-data.md")
- [AWS Elastic Beanstalk (elasticbeanstalk)](list_elasticbeanstalk.md "list_elasticbeanstalk.md")
- [AWS Elastic Disaster Recovery (drs)](list_drs.md "list_drs.md")
- [AWS Elastic Load Balancing (elasticloadbalancing)](list_elb.md "list_elb.md")
- [AWS Elastic Load Balancing V2 (elasticloadbalancing)](list_elbv2.md "list_elbv2.md")
- [AWS Elemental Appliances and Software (elemental-appliances-software)](list_elemental-appliances-software.md "list_elemental-appliances-software.md")
- [AWS Elemental Appliances and Software Activation Service (elemental-activations)](list_elemental-activations.md "list_elemental-activations.md")
- [AWS Elemental Inference (elemental-inference)](list_elementalinference.md "list_elementalinference.md")
- [AWS Elemental MediaConnect (mediaconnect)](list_mediaconnect.md "list_mediaconnect.md")
- [AWS Elemental MediaConvert (mediaconvert)](list_mediaconvert.md "list_mediaconvert.md")
- [AWS Elemental MediaLive (medialive)](list_medialive.md "list_medialive.md")
- [AWS Elemental MediaPackage (mediapackage)](list_mediapackage.md "list_mediapackage.md")
- [AWS Elemental MediaPackage V2 (mediapackagev2)](list_mediapackagev2.md "list_mediapackagev2.md")
- [AWS Elemental MediaPackage VOD (mediapackage-vod)](list_mediapackage-vod.md "list_mediapackage-vod.md")
- [AWS Elemental MediaStore (mediastore)](list_mediastore.md "list_mediastore.md")
- [AWS Elemental MediaTailor (mediatailor)](list_mediatailor.md "list_mediatailor.md")
- [AWS Elemental Support Cases (elemental-support-cases)](list_elemental-support-cases.md "list_elemental-support-cases.md")
- [AWS Elemental Support Content (elemental-support-content)](list_elemental-support-content.md "list_elemental-support-content.md")
- [AWS End User Messaging SMS and Voice V2 (sms-voice)](list_pinpoint-sms-voice-v2.md "list_pinpoint-sms-voice-v2.md")
- [AWS End User Messaging Social (social-messaging)](list_socialmessaging.md "list_socialmessaging.md")
- [AWS Entity Resolution (entityresolution)](list_entityresolution.md "list_entityresolution.md")
- [AWS Fault Injection Service (fis)](list_fis.md "list_fis.md")
- [AWS FinOps Agent (finops-agent)](list_finops-agent.md "list_finops-agent.md")
- [AWS Firewall Manager (fms)](list_fms.md "list_fms.md")
- [AWS Free Tier (freetier)](list_freetier.md "list_freetier.md")
- [AWS Global Accelerator (globalaccelerator)](list_globalaccelerator.md "list_globalaccelerator.md")
- [AWS Glue (glue)](list_glue.md "list_glue.md")
- [AWS Glue DataBrew (databrew)](list_databrew.md "list_databrew.md")
- [AWS Ground Station (groundstation)](list_groundstation.md "list_groundstation.md")
- [AWS Health APIs and Notifications (health)](list_health.md "list_health.md")
- [AWS HealthImaging (medical-imaging)](list_medical-imaging.md "list_medical-imaging.md")
- [AWS HealthLake (healthlake)](list_healthlake.md "list_healthlake.md")
- [AWS HealthOmics (omics)](list_omics.md "list_omics.md")
- [AWS IAM Access Analyzer (access-analyzer)](list_accessanalyzer.md "list_accessanalyzer.md")
- [AWS IAM Identity Center (sso)](list_iam-identity-center.md "list_iam-identity-center.md")
- [AWS IAM Identity Center directory (sso-directory)](list_sso-directory.md "list_sso-directory.md")
- [AWS IAM Identity Center OIDC service (sso-oauth)](list_sso-oidc.md "list_sso-oidc.md")
- [AWS Identity and Access Management (IAM) (iam)](list_iam.md "list_iam.md")
- [AWS Identity and Access Management Roles Anywhere (rolesanywhere)](list_rolesanywhere.md "list_rolesanywhere.md")
- [AWS Identity Store (identitystore)](list_identitystore.md "list_identitystore.md")
- [AWS Identity Store Auth (identitystore-auth)](list_identitystore-auth.md "list_identitystore-auth.md")
- [AWS Identity Sync (identity-sync)](list_identity-sync.md "list_identity-sync.md")
- [AWS Import Export Disk Service (importexport)](list_importexport.md "list_importexport.md")
- [AWS Interconnect (interconnect)](list_interconnect.md "list_interconnect.md")
- [AWS Invoicing Service (invoicing)](list_invoicing.md "list_invoicing.md")
- [AWS IoT (iot)](list_iot.md "list_iot.md")
- [AWS IoT Analytics (iotanalytics)](list_iotanalytics.md "list_iotanalytics.md")
- [AWS IoT Core Device Advisor (iotdeviceadvisor)](list_iotdeviceadvisor.md "list_iotdeviceadvisor.md")
- [AWS IoT Device Tester (iot-device-tester)](list_iot-device-tester.md "list_iot-device-tester.md")
- [AWS IoT Events (iotevents)](list_iotevents.md "list_iotevents.md")
- [AWS IoT Fleet Hub for Device Management (iotfleethub)](list_iotfleethub.md "list_iotfleethub.md")
- [AWS IoT FleetWise (iotfleetwise)](list_iotfleetwise.md "list_iotfleetwise.md")
- [AWS IoT Greengrass (greengrass)](list_greengrass.md "list_greengrass.md")
- [AWS IoT Greengrass V2 (greengrass)](list_greengrassv2.md "list_greengrassv2.md")
- [AWS IoT Jobs DataPlane (iotjobsdata)](list_iot-jobs-data.md "list_iot-jobs-data.md")
- [AWS IoT Managed Integrations (iotmanagedintegrations)](list_iot-managed-integrations.md "list_iot-managed-integrations.md")
- [AWS IoT SiteWise (iotsitewise)](list_iotsitewise.md "list_iotsitewise.md")
- [AWS IoT TwinMaker (iottwinmaker)](list_iottwinmaker.md "list_iottwinmaker.md")
- [AWS IoT Wireless (iotwireless)](list_iotwireless.md "list_iotwireless.md")
- [AWS IQ (iq)](list_iq.md "list_iq.md")
- [AWS IQ Permissions (iq-permission)](list_iq-permission.md "list_iq-permission.md")
- [AWS Key Management Service (kms)](list_kms.md "list_kms.md")
- [AWS Lake Formation (lakeformation)](list_lakeformation.md "list_lakeformation.md")
- [AWS Lambda (lambda)](list_lambda.md "list_lambda.md")
- [AWS Launch Wizard (launchwizard)](list_launch-wizard.md "list_launch-wizard.md")
- [AWS License Manager (license-manager)](list_license-manager.md "list_license-manager.md")
- [AWS License Manager Linux Subscriptions Manager (license-manager-linux-subscriptions)](list_license-manager-linux-subscriptions.md "list_license-manager-linux-subscriptions.md")
- [AWS License Manager User Subscriptions (license-manager-user-subscriptions)](list_license-manager-user-subscriptions.md "list_license-manager-user-subscriptions.md")
- [AWS Mainframe Modernization Application Testing (apptest)](list_apptest.md "list_apptest.md")
- [AWS Mainframe Modernization Service (m2)](list_m2.md "list_m2.md")
- [AWS Microservice Extractor for .NET (serviceextract)](list_serviceextract.md "list_serviceextract.md")
- [AWS Migration Acceleration Program Credits (mapcredits)](list_mapcredits.md "list_mapcredits.md")
- [AWS Migration Hub (mgh)](list_migration-hub.md "list_migration-hub.md")
- [AWS Migration Hub Orchestrator (migrationhub-orchestrator)](list_migrationhuborchestrator.md "list_migrationhuborchestrator.md")
- [AWS Migration Hub Refactor Spaces (refactor-spaces)](list_migration-hub-refactor-spaces.md "list_migration-hub-refactor-spaces.md")
- [AWS Migration Hub Strategy Recommendations (migrationhub-strategy)](list_migrationhubstrategy.md "list_migrationhubstrategy.md")
- [AWS MWAA Serverless (airflow-serverless)](list_mwaa-serverless.md "list_mwaa-serverless.md")
- [AWS Network Firewall (network-firewall)](list_network-firewall.md "list_network-firewall.md")
- [AWS Network Manager (networkmanager)](list_networkmanager.md "list_networkmanager.md")
- [AWS Network Manager Chat (networkmanager-chat)](list_networkmanager-chat.md "list_networkmanager-chat.md")
- [AWS OpsWorks (opsworks)](list_opsworks.md "list_opsworks.md")
- [AWS OpsWorks Configuration Management (opsworks-cm)](list_opsworks-cm.md "list_opsworks-cm.md")
- [AWS Organizations (organizations)](list_organizations.md "list_organizations.md")
- [AWS Outposts (outposts)](list_outposts.md "list_outposts.md")
- [AWS Panorama (panorama)](list_panorama.md "list_panorama.md")
- [AWS Parallel Computing Service (pcs)](list_pcs.md "list_pcs.md")
- [AWS Partner Central (partnercentral)](list_partner-central.md "list_partner-central.md")
- [AWS Partner central account management (partnercentral-account-management)](list_partnercentral-account-management.md "list_partnercentral-account-management.md")
- [AWS Payment Cryptography (payment-cryptography)](list_payment-cryptography.md "list_payment-cryptography.md")
- [AWS Payments (payments)](list_payments.md "list_payments.md")
- [AWS Performance Insights (pi)](list_pi.md "list_pi.md")
- [AWS Price List (pricing)](list_pricing.md "list_pricing.md")
- [AWS PricingPlanManager Service (pricingplanmanager)](list_pricingplanmanager.md "list_pricingplanmanager.md")
- [AWS Private CA Connector for Active Directory (pca-connector-ad)](list_pca-connector-ad.md "list_pca-connector-ad.md")
- [AWS Private CA Connector for SCEP (pca-connector-scep)](list_pca-connector-scep.md "list_pca-connector-scep.md")
- [AWS Private Certificate Authority (acm-pca)](list_acm-pca.md "list_acm-pca.md")
- [AWS PrivateLink (vpce)](list_vpce.md "list_vpce.md")
- [AWS Proton (proton)](list_proton.md "list_proton.md")
- [AWS Purchase Orders Console (purchase-orders)](list_purchase-orders.md "list_purchase-orders.md")
- [AWS Recycle Bin (rbin)](list_rbin.md "list_rbin.md")
- [AWS reInvent event pass amount charge to customer AWS account (eventsbilltoaws)](list_eventsbilltoaws.md "list_eventsbilltoaws.md")
- [AWS rePost Private (repostspace)](list_repostspace.md "list_repostspace.md")
- [AWS Resilience Hub (resiliencehub)](list_resilience-hub.md "list_resilience-hub.md")
- [AWS Resource Access Manager (RAM) (ram)](list_ram.md "list_ram.md")
- [AWS Resource Explorer (resource-explorer-2)](list_resource-explorer-2.md "list_resource-explorer-2.md")
- [AWS Resource Groups (resource-groups)](list_resource-groups.md "list_resource-groups.md")
- [AWS RoboMaker (robomaker)](list_robomaker.md "list_robomaker.md")
- [AWS Route53 Global Resolver (route53globalresolver)](list_route53globalresolver.md "list_route53globalresolver.md")
- [AWS RTB Fabric (rtbfabric)](list_rtbfabric.md "list_rtbfabric.md")
- [AWS Savings Plans (savingsplans)](list_savingsplans.md "list_savingsplans.md")
- [AWS Secrets Manager (secretsmanager)](list_secretsmanager.md "list_secretsmanager.md")
- [AWS Security Agent (securityagent)](list_securityagent.md "list_securityagent.md")
- [AWS Security Hub (securityhub)](list_securityhub.md "list_securityhub.md")
- [AWS Security Incident Response (security-ir)](list_security-ir.md "list_security-ir.md")
- [AWS Security Token Service (sts)](list_sts.md "list_sts.md")
- [AWS Server Migration Service (sms)](list_sms.md "list_sms.md")
- [AWS Serverless Application Repository (serverlessrepo)](list_serverlessrepo.md "list_serverlessrepo.md")
- [AWS Service - Oracle Database@AWS (odb)](list_odb.md "list_odb.md")
- [AWS Service Catalog (servicecatalog)](list_service-catalog.md "list_service-catalog.md")
- [AWS service providing managed private networks (private-networks)](list_private-networks.md "list_private-networks.md")
- [AWS Shield (shield)](list_shield.md "list_shield.md")
- [AWS Shield network security director (network-security-director)](list_network-security-director.md "list_network-security-director.md")
- [AWS Signer (signer)](list_signer.md "list_signer.md")
- [AWS Signin (signin)](list_signin.md "list_signin.md")
- [AWS SimSpace Weaver (simspaceweaver)](list_simspaceweaver.md "list_simspaceweaver.md")
- [AWS Snow Device Management (snow-device-management)](list_snow-device-management.md "list_snow-device-management.md")
- [AWS Snowball (snowball)](list_snowball.md "list_snowball.md")
- [AWS SQL Workbench (sqlworkbench)](list_sqlworkbench.md "list_sqlworkbench.md")
- [AWS Step Functions (states)](list_stepfunctions.md "list_stepfunctions.md")
- [AWS Storage Gateway (storagegateway)](list_storagegateway.md "list_storagegateway.md")
- [AWS Supply Chain (scn)](list_supplychain.md "list_supplychain.md")
- [AWS Sustainability (sustainability)](list_sustainability.md "list_sustainability.md")
- [AWS Systems Manager (ssm)](list_ssm.md "list_ssm.md")
- [AWS Systems Manager for SAP (ssm-sap)](list_ssm-sap.md "list_ssm-sap.md")
- [AWS Systems Manager GUI Connect (ssm-guiconnect)](list_ssm-guiconnect.md "list_ssm-guiconnect.md")
- [AWS Systems Manager Incident Manager (ssm-incidents)](list_ssm-incidents.md "list_ssm-incidents.md")
- [AWS Systems Manager Incident Manager Contacts (ssm-contacts)](list_ssm-contacts.md "list_ssm-contacts.md")
- [AWS Systems Manager Quick Setup (ssm-quicksetup)](list_ssm-quicksetup.md "list_ssm-quicksetup.md")
- [AWS Tax Settings (tax)](list_taxsettings.md "list_taxsettings.md")
- [AWS Telco Network Builder (tnb)](list_tnb.md "list_tnb.md")
- [AWS Tiros (tiros)](list_tiros.md "list_tiros.md")
- [AWS Transfer Family (transfer)](list_transfer.md "list_transfer.md")
- [AWS Transform (transform)](list_transform.md "list_transform.md")
- [AWS Transform custom (transform-custom)](list_transform-custom.md "list_transform-custom.md")
- [AWS Trusted Advisor (trustedadvisor)](list_trustedadvisor.md "list_trustedadvisor.md")
- [AWS User Experience Customization (uxc)](list_uxc.md "list_uxc.md")
- [AWS User Notifications (notifications)](list_notifications.md "list_notifications.md")
- [AWS User Notifications Contacts (notifications-contacts)](list_notificationscontacts.md "list_notificationscontacts.md")
- [AWS User Subscriptions (user-subscriptions)](list_user-subscriptions.md "list_user-subscriptions.md")
- [AWS Verified Access (verified-access)](list_verified-access.md "list_verified-access.md")
- [AWS WAF (waf)](list_waf.md "list_waf.md")
- [AWS WAF Regional (waf-regional)](list_waf-regional.md "list_waf-regional.md")
- [AWS WAF V2 (wafv2)](list_wafv2.md "list_wafv2.md")
- [AWS Well-Architected Tool (wellarchitected)](list_wellarchitected.md "list_wellarchitected.md")
- [AWS Wickr (wickr)](list_wickr.md "list_wickr.md")
- [AWS WorkSpaces Managed Instances (workspaces-instances)](list_workspaces-instances.md "list_workspaces-instances.md")
- [AWS X-Ray (xray)](list_xray.md "list_xray.md")
- [AWS Billing (billing)](list_billing.md "list_billing.md")
- [AWS Billing and Cost Management Dashboards (bcm-dashboards)](list_bcm-dashboards.md "list_bcm-dashboards.md")
- [AWS Billing And Cost Management Data Exports (bcm-data-exports)](list_bcm-data-exports.md "list_bcm-data-exports.md")
- [AWS Billing And Cost Management Pricing Calculator (bcm-pricing-calculator)](list_bcm-pricing-calculator.md "list_bcm-pricing-calculator.md")
- [AWS Billing And Cost Management Recommended Actions (bcm-recommended-actions)](list_bcm-recommended-actions.md "list_bcm-recommended-actions.md")
- [AWS Billing Console (aws-portal)](list_aws-portal.md "list_aws-portal.md")
- [AWS Management Console Mobile App (consoleapp)](list_consoleapp.md "list_consoleapp.md")
- [AWS Marketplace (aws-marketplace)](list_marketplace-agreement.md "list_marketplace-agreement.md")
- [AWS Marketplace Catalog (aws-marketplace)](list_marketplace-catalog.md "list_marketplace-catalog.md")
- [AWS Marketplace Commerce Analytics Service (marketplacecommerceanalytics)](list_marketplacecommerceanalytics.md "list_marketplacecommerceanalytics.md")
- [AWS Marketplace Deployment Service (aws-marketplace)](list_marketplace-deployment.md "list_marketplace-deployment.md")
- [AWS Marketplace Discovery (aws-marketplace)](list_marketplace-discovery.md "list_marketplace-discovery.md")
- [AWS Marketplace Entitlement Service (aws-marketplace)](list_marketplace-entitlement.md "list_marketplace-entitlement.md")
- [AWS Marketplace Image Building Service (aws-marketplace)](list_marketplace-image-build.md "list_marketplace-image-build.md")
- [AWS Marketplace Management Portal (aws-marketplace-management)](list_aws-marketplace-management.md "list_aws-marketplace-management.md")
- [AWS Marketplace Metering Service (aws-marketplace)](list_meteringmarketplace.md "list_meteringmarketplace.md")
- [AWS Marketplace Private Marketplace (aws-marketplace)](list_private-marketplace.md "list_private-marketplace.md")
- [AWS Marketplace Procurement Systems Integration (aws-marketplace)](list_marketplace-procurement-integration.md "list_marketplace-procurement-integration.md")
- [AWS Marketplace Reporting (aws-marketplace)](list_marketplace-reporting.md "list_marketplace-reporting.md")
- [AWS Marketplace Seller Reporting (aws-marketplace)](list_marketplace-seller-reporting.md "list_marketplace-seller-reporting.md")
- [AWS Marketplace Vendor Insights (vendor-insights)](list_vendor-insights.md "list_vendor-insights.md")
- [AWS Support (support)](list_support.md "list_support.md")
- [AWS Support App in Slack (supportapp)](list_support-app.md "list_support-app.md")
- [AWS Support Authorization (supportauthz)](list_supportauthz.md "list_supportauthz.md")
- [AWS Support Console (support-console)](list_support-console.md "list_support-console.md")
- [AWS Support Plans (supportplans)](list_supportplans.md "list_supportplans.md")
- [Alexa for Business (a4b)](list_a4b.md "list_a4b.md")
- [Amazon AI Operations (aiops)](list_aiops.md "list_aiops.md")
- [Amazon API Gateway (execute-api)](list_apigatewaymanagementapi.md "list_apigatewaymanagementapi.md")
- [Amazon API Gateway Management (apigateway)](list_apigateway.md "list_apigateway.md")
- [Amazon API Gateway Management V2 (apigateway)](list_apigatewayv2.md "list_apigatewayv2.md")
- [Amazon AppFlow (appflow)](list_appflow.md "list_appflow.md")
- [Amazon AppIntegrations (app-integrations)](list_appintegrations.md "list_appintegrations.md")
- [Amazon Application Recovery Controller - Zonal Shift (arc-zonal-shift)](list_arc-zonal-shift.md "list_arc-zonal-shift.md")
- [Amazon AppStream 2.0 (appstream)](list_appstream.md "list_appstream.md")
- [Amazon ARC Region switch (arc-region-switch)](list_arc-region-switch.md "list_arc-region-switch.md")
- [Amazon Athena (athena)](list_athena.md "list_athena.md")
- [Amazon Aurora DSQL (dsql)](list_dsql.md "list_dsql.md")
- [Amazon Bedrock (bedrock)](list_bedrock.md "list_bedrock.md")
- [Amazon Bedrock Agentcore (bedrock-agentcore)](list_bedrock-agentcore.md "list_bedrock-agentcore.md")
- [Amazon Bedrock Powered by AWS Mantle (bedrock-mantle)](list_bedrock-mantle.md "list_bedrock-mantle.md")
- [Amazon Bio Discovery (researchstudio)](list_researchstudio.md "list_researchstudio.md")
- [Amazon Braket (braket)](list_braket.md "list_braket.md")
- [Amazon Chime (chime)](list_chime.md "list_chime.md")
- [Amazon Cloud Directory (clouddirectory)](list_clouddirectory.md "list_clouddirectory.md")
- [Amazon CloudFront (cloudfront)](list_cloudfront.md "list_cloudfront.md")
- [Amazon CloudFront KeyValueStore (cloudfront-keyvaluestore)](list_cloudfront-keyvaluestore.md "list_cloudfront-keyvaluestore.md")
- [Amazon CloudSearch (cloudsearch)](list_cloudsearch.md "list_cloudsearch.md")
- [Amazon CloudWatch (cloudwatch)](list_cloudwatch.md "list_cloudwatch.md")
- [Amazon CloudWatch Application Insights (applicationinsights)](list_application-insights.md "list_application-insights.md")
- [Amazon CloudWatch Application Signals (application-signals)](list_application-signals.md "list_application-signals.md")
- [Amazon CloudWatch Application Signals MCP Server (application-signals-mcp)](list_application-signals-mcp.md "list_application-signals-mcp.md")
- [Amazon CloudWatch Evidently (evidently)](list_evidently.md "list_evidently.md")
- [Amazon CloudWatch Internet Monitor (internetmonitor)](list_internetmonitor.md "list_internetmonitor.md")
- [Amazon CloudWatch Logs (logs)](list_logs.md "list_logs.md")
- [Amazon CloudWatch Network Synthetic Monitor (networkmonitor)](list_networkmonitor.md "list_networkmonitor.md")
- [Amazon CloudWatch Observability Access Manager (oam)](list_oam.md "list_oam.md")
- [Amazon CloudWatch Observability Admin Service (observabilityadmin)](list_observabilityadmin.md "list_observabilityadmin.md")
- [Amazon CloudWatch Synthetics (synthetics)](list_synthetics.md "list_synthetics.md")
- [Amazon CodeCatalyst (codecatalyst)](list_codecatalyst.md "list_codecatalyst.md")
- [Amazon CodeGuru (codeguru)](list_codeguru.md "list_codeguru.md")
- [Amazon CodeGuru Profiler (codeguru-profiler)](list_codeguruprofiler.md "list_codeguruprofiler.md")
- [Amazon CodeGuru Reviewer (codeguru-reviewer)](list_codeguru-reviewer.md "list_codeguru-reviewer.md")
- [Amazon CodeGuru Security (codeguru-security)](list_codeguru-security.md "list_codeguru-security.md")
- [Amazon CodeWhisperer (codewhisperer)](list_codewhisperer.md "list_codewhisperer.md")
- [Amazon Cognito Identity (cognito-identity)](list_cognito-identity.md "list_cognito-identity.md")
- [Amazon Cognito Sync (cognito-sync)](list_cognito-sync.md "list_cognito-sync.md")
- [Amazon Cognito User Pools (cognito-idp)](list_cognito-idp.md "list_cognito-idp.md")
- [Amazon Comprehend (comprehend)](list_comprehend.md "list_comprehend.md")
- [Amazon Comprehend Medical (comprehendmedical)](list_comprehendmedical.md "list_comprehendmedical.md")
- [Amazon Connect (connect)](list_connect.md "list_connect.md")
- [Amazon Connect Cases (cases)](list_connectcases.md "list_connectcases.md")
- [Amazon Connect Customer Profiles (profile)](list_customer-profiles.md "list_customer-profiles.md")
- [Amazon Connect Health (health-agent)](list_connecthealth.md "list_connecthealth.md")
- [Amazon Connect Outbound Campaigns (connect-campaigns)](list_connect-outbound-campaigns.md "list_connect-outbound-campaigns.md")
- [Amazon Connect Voice ID (voiceid)](list_voice-id.md "list_voice-id.md")
- [Amazon Data Lifecycle Manager (dlm)](list_dlm.md "list_dlm.md")
- [Amazon DataZone (datazone)](list_datazone.md "list_datazone.md")
- [Amazon Detective (detective)](list_detective.md "list_detective.md")
- [Amazon DevOps Guru (devops-guru)](list_devops-guru.md "list_devops-guru.md")
- [Amazon DocumentDB Elastic Clusters (docdb-elastic)](list_docdb-elastic.md "list_docdb-elastic.md")
- [Amazon DynamoDB (dynamodb)](list_dynamodb.md "list_dynamodb.md")
- [Amazon DynamoDB Accelerator (DAX) (dax)](list_dax.md "list_dax.md")
- [Amazon EC2 (ec2)](list_ec2.md "list_ec2.md")
- [Amazon EC2 Auto Scaling (autoscaling)](list_autoscaling.md "list_autoscaling.md")
- [Amazon EC2 Image Builder (imagebuilder)](list_imagebuilder.md "list_imagebuilder.md")
- [Amazon EC2 Instance Connect (ec2-instance-connect)](list_ec2-instance-connect.md "list_ec2-instance-connect.md")
- [Amazon ECS MCP Service (ecs-mcp)](list_ecs-mcp.md "list_ecs-mcp.md")
- [Amazon EKS Auth (eks-auth)](list_eks-auth.md "list_eks-auth.md")
- [Amazon EKS MCP Server (eks-mcp)](list_eks-mcp.md "list_eks-mcp.md")
- [Amazon Elastic Block Store (ebs)](list_ebs.md "list_ebs.md")
- [Amazon Elastic Container Registry (ecr)](list_ecr.md "list_ecr.md")
- [Amazon Elastic Container Registry Public (ecr-public)](list_ecr-public.md "list_ecr-public.md")
- [Amazon Elastic Container Service (ecs)](list_ecs.md "list_ecs.md")
- [Amazon Elastic File System (elasticfilesystem)](list_efs.md "list_efs.md")
- [Amazon Elastic Kubernetes Service (eks)](list_eks.md "list_eks.md")
- [Amazon Elastic MapReduce (elasticmapreduce)](list_emr.md "list_emr.md")
- [Amazon Elastic Transcoder (elastictranscoder)](list_elastictranscoder.md "list_elastictranscoder.md")
- [Amazon Elastic VMware Service (evs)](list_evs.md "list_evs.md")
- [Amazon ElastiCache (elasticache)](list_elasticache.md "list_elasticache.md")
- [Amazon EMR on EKS (EMR Containers) (emr-containers)](list_emr-containers.md "list_emr-containers.md")
- [Amazon EMR Serverless (emr-serverless)](list_emr-serverless.md "list_emr-serverless.md")
- [Amazon EventBridge (events)](list_events.md "list_events.md")
- [Amazon EventBridge Pipes (pipes)](list_pipes.md "list_pipes.md")
- [Amazon EventBridge Scheduler (scheduler)](list_scheduler.md "list_scheduler.md")
- [Amazon EventBridge Schemas (schemas)](list_schemas.md "list_schemas.md")
- [Amazon FinSpace (finspace)](list_finspace.md "list_finspace.md")
- [Amazon FinSpace API (finspace-api)](list_finspace-data.md "list_finspace-data.md")
- [Amazon Forecast (forecast)](list_forecast.md "list_forecast.md")
- [Amazon Fraud Detector (frauddetector)](list_frauddetector.md "list_frauddetector.md")
- [Amazon FreeRTOS (freertos)](list_freertos.md "list_freertos.md")
- [Amazon FSx (fsx)](list_fsx.md "list_fsx.md")
- [Amazon GameLift Servers (gamelift)](list_gamelift.md "list_gamelift.md")
- [Amazon GameLift Streams (gameliftstreams)](list_gameliftstreams.md "list_gameliftstreams.md")
- [Amazon GroundTruth Labeling (groundtruthlabeling)](list_groundtruthlabeling.md "list_groundtruthlabeling.md")
- [Amazon GuardDuty (guardduty)](list_guardduty.md "list_guardduty.md")
- [Amazon Honeycode (honeycode)](list_honeycode.md "list_honeycode.md")
- [Amazon Inspector (inspector)](list_inspector.md "list_inspector.md")
- [Amazon Inspector2 (inspector2)](list_inspector2.md "list_inspector2.md")
- [Amazon Inspector2 Telemetry Channel (inspector2-telemetry)](list_inspector2-telemetry.md "list_inspector2-telemetry.md")
- [Amazon InspectorScan (inspector-scan)](list_inspector-scan.md "list_inspector-scan.md")
- [Amazon Interactive Video Service (ivs)](list_interactive-video-service.md "list_interactive-video-service.md")
- [Amazon Interactive Video Service Chat (ivschat)](list_ivschat.md "list_ivschat.md")
- [Amazon Kendra (kendra)](list_kendra.md "list_kendra.md")
- [Amazon Kendra Intelligent Ranking (kendra-ranking)](list_kendra-ranking.md "list_kendra-ranking.md")
- [Amazon Keyspaces (for Apache Cassandra) (cassandra)](list_keyspaces.md "list_keyspaces.md")
- [Amazon Kinesis Analytics (kinesisanalytics)](list_kinesisanalytics.md "list_kinesisanalytics.md")
- [Amazon Kinesis Analytics V2 (kinesisanalytics)](list_kinesisanalyticsv2.md "list_kinesisanalyticsv2.md")
- [Amazon Kinesis Data Streams (kinesis)](list_kinesis.md "list_kinesis.md")
- [Amazon Kinesis Firehose (firehose)](list_firehose.md "list_firehose.md")
- [Amazon Kinesis Video Streams (kinesisvideo)](list_kinesis-video-streams.md "list_kinesis-video-streams.md")
- [Amazon Lex (lex)](list_lex.md "list_lex.md")
- [Amazon Lex V2 (lex)](list_lex-v2.md "list_lex-v2.md")
- [Amazon Lightsail (lightsail)](list_lightsail.md "list_lightsail.md")
- [Amazon Location (geo)](list_location.md "list_location.md")
- [Amazon Location Service Maps (geo-maps)](list_geo-maps.md "list_geo-maps.md")
- [Amazon Location Service Places (geo-places)](list_geo-places.md "list_geo-places.md")
- [Amazon Location Service Routes (geo-routes)](list_geo-routes.md "list_geo-routes.md")
- [Amazon Lookout for Equipment (lookoutequipment)](list_lookoutequipment.md "list_lookoutequipment.md")
- [Amazon Lookout for Metrics (lookoutmetrics)](list_lookoutmetrics.md "list_lookoutmetrics.md")
- [Amazon Lookout for Vision (lookoutvision)](list_lookoutvision.md "list_lookoutvision.md")
- [Amazon Machine Learning (machinelearning)](list_machinelearning.md "list_machinelearning.md")
- [Amazon Macie (macie2)](list_macie2.md "list_macie2.md")
- [Amazon Managed Blockchain (managedblockchain)](list_managedblockchain.md "list_managedblockchain.md")
- [Amazon Managed Blockchain Query (managedblockchain-query)](list_managedblockchain-query.md "list_managedblockchain-query.md")
- [Amazon Managed Grafana (grafana)](list_grafana.md "list_grafana.md")
- [Amazon Managed Service for Prometheus (aps)](list_amp.md "list_amp.md")
- [Amazon Managed Streaming for Apache Kafka (kafka)](list_kafka.md "list_kafka.md")
- [Amazon Managed Streaming for Kafka Connect (kafkaconnect)](list_kafkaconnect.md "list_kafkaconnect.md")
- [Amazon Managed Workflows for Apache Airflow (airflow)](list_mwaa.md "list_mwaa.md")
- [Amazon Mechanical Turk (mechanicalturk)](list_mturk.md "list_mturk.md")
- [Amazon MemoryDB (memorydb)](list_memorydb.md "list_memorydb.md")
- [Amazon Message Delivery Service (ec2messages)](list_ec2messages.md "list_ec2messages.md")
- [Amazon Message Gateway Service (ssmmessages)](list_ssmmessages.md "list_ssmmessages.md")
- [Amazon Mobile Analytics (mobileanalytics)](list_mobileanalytics.md "list_mobileanalytics.md")
- [Amazon Monitron (monitron)](list_monitron.md "list_monitron.md")
- [Amazon MQ (mq)](list_mq.md "list_mq.md")
- [Amazon Neptune (neptune-db)](list_neptunedata.md "list_neptunedata.md")
- [Amazon Neptune Analytics (neptune-graph)](list_neptune-graph.md "list_neptune-graph.md")
- [Amazon Nimble Studio (nimble)](list_nimble.md "list_nimble.md")
- [Amazon Nova Act (nova-act)](list_nova-act.md "list_nova-act.md")
- [Amazon One Enterprise (one)](list_one.md "list_one.md")
- [Amazon OpenSearch (opensearch)](list_opensearch.md "list_opensearch.md")
- [Amazon OpenSearch Ingestion (osis)](list_osis.md "list_osis.md")
- [Amazon OpenSearch Serverless (aoss)](list_opensearchserverless.md "list_opensearchserverless.md")
- [Amazon OpenSearch Service (es)](list_es.md "list_es.md")
- [Amazon Personalize (personalize)](list_personalize.md "list_personalize.md")
- [Amazon Pinpoint (mobiletargeting)](list_pinpoint.md "list_pinpoint.md")
- [Amazon Pinpoint Email Service (ses)](list_pinpoint-email.md "list_pinpoint-email.md")
- [Amazon Pinpoint SMS and Voice Service (sms-voice)](list_pinpoint-sms-voice.md "list_pinpoint-sms-voice.md")
- [Amazon Polly (polly)](list_polly.md "list_polly.md")
- [Amazon Q (q)](list_q.md "list_q.md")
- [Amazon Q Business (qbusiness)](list_qbusiness.md "list_qbusiness.md")
- [Amazon Q Business Q Apps (qapps)](list_qapps.md "list_qapps.md")
- [Amazon Q Developer (qdeveloper)](list_qdeveloper.md "list_qdeveloper.md")
- [Amazon Q in Connect (wisdom)](list_q-in-connect.md "list_q-in-connect.md")
- [Amazon QLDB (qldb)](list_qldb.md "list_qldb.md")
- [Amazon QuickSight (quicksight)](list_quicksight.md "list_quicksight.md")
- [Amazon RDS (rds)](list_rds.md "list_rds.md")
- [Amazon RDS Data API (rds-data)](list_rds-data.md "list_rds-data.md")
- [Amazon RDS IAM Authentication (rds-db)](list_rds-db.md "list_rds-db.md")
- [Amazon Redshift (redshift)](list_redshift.md "list_redshift.md")
- [Amazon Redshift Data API (redshift-data)](list_redshift-data.md "list_redshift-data.md")
- [Amazon Redshift Serverless (redshift-serverless)](list_redshift-serverless.md "list_redshift-serverless.md")
- [Amazon Rekognition (rekognition)](list_rekognition.md "list_rekognition.md")
- [Amazon Resource Group Tagging API (tag)](list_resourcegroupstaggingapi.md "list_resourcegroupstaggingapi.md")
- [Amazon RHEL Knowledgebase Portal (rhelkb)](list_rhelkb.md "list_rhelkb.md")
- [Amazon Route 53 (route53)](list_route53.md "list_route53.md")
- [Amazon Route 53 Domains (route53domains)](list_route53domains.md "list_route53domains.md")
- [Amazon Route 53 Profiles (route53profiles)](list_route53profiles.md "list_route53profiles.md")
- [Amazon Route 53 Recovery Cluster (route53-recovery-cluster)](list_route53-recovery-cluster.md "list_route53-recovery-cluster.md")
- [Amazon Route 53 Recovery Controls (route53-recovery-control-config)](list_route53-recovery-control-config.md "list_route53-recovery-control-config.md")
- [Amazon Route 53 Recovery Readiness (route53-recovery-readiness)](list_route53-recovery-readiness.md "list_route53-recovery-readiness.md")
- [Amazon Route 53 Resolver (route53resolver)](list_route53resolver.md "list_route53resolver.md")
- [Amazon S3 (s3)](list_s3.md "list_s3.md")
- [Amazon S3 Express (s3express)](list_s3express.md "list_s3express.md")
- [Amazon S3 Files (s3files)](list_s3files.md "list_s3files.md")
- [Amazon S3 Glacier (glacier)](list_glacier.md "list_glacier.md")
- [Amazon S3 Object Lambda (s3-object-lambda)](list_s3-object-lambda.md "list_s3-object-lambda.md")
- [Amazon S3 on Outposts (s3-outposts)](list_s3outposts.md "list_s3outposts.md")
- [Amazon S3 Tables (s3tables)](list_s3tables.md "list_s3tables.md")
- [Amazon S3 Vectors (s3vectors)](list_s3vectors.md "list_s3vectors.md")
- [Amazon SageMaker (sagemaker)](list_sagemaker.md "list_sagemaker.md")
- [Amazon SageMaker data science assistant (sagemaker-data-science-assistant)](list_sagemaker-data-science-assistant.md "list_sagemaker-data-science-assistant.md")
- [Amazon SageMaker geospatial capabilities (sagemaker-geospatial)](list_sagemaker-geospatial.md "list_sagemaker-geospatial.md")
- [Amazon SageMaker Unified Studio MCP (sagemaker-unified-studio-mcp)](list_sagemaker-unified-studio-mcp.md "list_sagemaker-unified-studio-mcp.md")
- [Amazon SageMaker with MLflow (sagemaker-mlflow)](list_sagemaker-mlflow.md "list_sagemaker-mlflow.md")
- [Amazon Security Lake (securitylake)](list_securitylake.md "list_securitylake.md")
- [Amazon SES (ses)](list_ses.md "list_ses.md")
- [Amazon Simple Email Service - Mail Manager (ses)](list_mailmanager.md "list_mailmanager.md")
- [Amazon Simple Email Service v2 (ses)](list_sesv2.md "list_sesv2.md")
- [Amazon Simple Workflow Service (swf)](list_swf.md "list_swf.md")
- [Amazon SimpleDB (sdb)](list_simpledb.md "list_simpledb.md")
- [Amazon SNS (sns)](list_sns.md "list_sns.md")
- [Amazon SQS (sqs)](list_sqs.md "list_sqs.md")
- [Amazon Textract (textract)](list_textract.md "list_textract.md")
- [Amazon Timestream (timestream)](list_timestream.md "list_timestream.md")
- [Amazon Timestream InfluxDB (timestream-influxdb)](list_timestream-influxdb.md "list_timestream-influxdb.md")
- [Amazon Transcribe (transcribe)](list_transcribe.md "list_transcribe.md")
- [Amazon Translate (translate)](list_translate.md "list_translate.md")
- [Amazon Verified Permissions (verifiedpermissions)](list_verifiedpermissions.md "list_verifiedpermissions.md")
- [Amazon VPC Lattice (vpc-lattice)](list_vpc-lattice.md "list_vpc-lattice.md")
- [Amazon VPC Lattice Services (vpc-lattice-svcs)](list_vpc-lattice-svcs.md "list_vpc-lattice-svcs.md")
- [Amazon WorkDocs (workdocs)](list_workdocs.md "list_workdocs.md")
- [Amazon WorkLink (worklink)](list_worklink.md "list_worklink.md")
- [Amazon WorkMail (workmail)](list_workmail.md "list_workmail.md")
- [Amazon WorkMail Message Flow (workmailmessageflow)](list_workmailmessageflow.md "list_workmailmessageflow.md")
- [Amazon WorkSpaces (workspaces)](list_workspaces.md "list_workspaces.md")
- [Amazon WorkSpaces AgentAccess MCP Server (agentaccess-mcp)](list_agentaccess-mcp.md "list_agentaccess-mcp.md")
- [Amazon WorkSpaces Application Manager (wam)](list_wam.md "list_wam.md")
- [Amazon WorkSpaces Secure Browser (workspaces-web)](list_workspaces-web.md "list_workspaces-web.md")
- [Amazon WorkSpaces Thin Client (thinclient)](list_workspaces-thin-client.md "list_workspaces-thin-client.md")
- [AmazonMediaImport (mediaimport)](list_mediaimport.md "list_mediaimport.md")
- [Apache Kafka APIs for Amazon MSK clusters (kafka-cluster)](list_kafka-cluster.md "list_kafka-cluster.md")
- [Application Discovery Arsenal (arsenal)](list_arsenal.md "list_arsenal.md")
- [Claude Platform on AWS (aws-external-anthropic)](list_aws-external-anthropic.md "list_aws-external-anthropic.md")
- [Database Query Metadata Service (dbqms)](list_dbqms.md "list_dbqms.md")
- [Multi-party approval (mpa)](list_mpa.md "list_mpa.md")
- [Network Flow Monitor (networkflowmonitor)](list_networkflowmonitor.md "list_networkflowmonitor.md")
- [Service Quotas (servicequotas)](list_service-quotas.md "list_service-quotas.md")
- [Tag Editor (resource-explorer)](list_resource-explorer.md "list_resource-explorer.md")
