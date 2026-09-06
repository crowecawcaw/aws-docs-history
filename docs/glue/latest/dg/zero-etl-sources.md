

# Configuring a source for a zero-ETL integration
<a name="zero-etl-sources"></a>

Setting up an integration requires some prerequisites on the source such as configuring IAM roles or policies which AWS Glue uses to access data from the source (in order to write to the target), the use of KMS keys to encrypt the data in intermediate location, etc.

**Topics**
+ [Configuring Amazon DynamoDB source](#zero-etl-config-source-dynamodb)
+ [Configuring connection (SaaS) source](#zero-etl-config-source-saas)
+ [Setting up Oracle Database at AWS as source](#zero-etl-config-source-oracle)

## Configuring Amazon DynamoDB source
<a name="zero-etl-config-source-dynamodb"></a>

To access data from your source Amazon DynamoDB table, AWS Glue requires access to describe the table and export data from it. Amazon DynamoDB recently introduced a feature which allows configuring a Resource Based Access (RBAC) policy.

The following example Resource Based Access (RBAC) Policy uses a wild card (\*) for integration:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "1111",
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Resource": "*",
      "Action": [
        "dynamodb:ExportTableToPointInTime",
        "dynamodb:DescribeTable",
        "dynamodb:DescribeExport"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:glue:us-east-1:111122223333:integration:*"
        }
      }
    }
  ]
}
```
+ For the Amazon DynamoDB table that you want to replicate, paste the above RBAC policy template into **Resource-based policy for table** and fill in the fields.
+ If you want to make the policy restrictive, you must update the policy after creating the integration and specify the full `integrationArn` and use the `StringEquals` condition instead of `StringLike`.
+ Make sure that Point-in-time recovery (PITR) is enabled for the Amazon DynamoDB table.
+ Make sure that you add `Describe Export` to the Resource Based Access (RBAC) policy.

You can also add the RBAC policy to the table using the following command:

```
aws dynamodb put-resource-policy \
--resource-arn arn:aws:dynamodb:{{region}}:{{account-id}}:table/{{ddb-table-name}} \
--policy file://resource-policy-with-condition.json \
--region {{region}}
```

To verify that policy is applied correctly, use the following command to get the resource policy for a table:

```
aws dynamodb get-resource-policy \
--resource-arn arn:aws:dynamodb:{{region}}:{{account-id}}:table/{{ddb-table-name}} \
--region {{region}}
```

## Configuring connection (SaaS) source
<a name="zero-etl-config-source-saas"></a>

### Prerequisites for setting up an integration
<a name="zero-etl-config-source-saas-prerequisites"></a>

Before creating a zero-ETL integration from SaaS sources, you need to complete the following setup tasks:
+ Create a AWS Glue connection with SaaS source.
+ Create the source role to provide access to connection.
+ Associate the role with the connection.

### Configuring Salesforce source
<a name="zero-etl-config-source-salesforce"></a>

To create a connection for a Salesforce source, see [Connecting to Salesforce](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-salesforce.html).

Once you've created the connection, you can specify the source data to replicate.

![The screenshot shows selecting Salesforce source data to replicate in a zero-ETL integration.](http://docs.aws.amazon.com/glue/latest/dg/images/zero-etl-salesforce-source-data.png)


Using your zero-ETL integration you can perform DDL operations for supported entities. For a list of entities which are not supported, see [Unsupported entities and fields for Salesforce](#zero-etl-config-source-salesforce-unsupported).

#### Additional Salesforce Configuration
<a name="zero-etl-config-source-salesforce-additional"></a>

Salesforce Zero-ETL needs Lake Formation permission on AWS Glue database, otherwise it will get `IngestionFailed` from the Log with the following error:

```
"errorMessage": "Insufficient lake formation permissions on Target Glue database."
```

#### Unsupported entities and fields for Salesforce
<a name="zero-etl-config-source-salesforce-unsupported"></a>

The following Salesforce entities or fields are unsupported for use in a zero-ETL integration with a Salesforce source.

```
AccountChangeEvent, AccountContactRoleChangeEvent, AccountHistory, AccountShare, ActiveFeatureLicenseMetric, ActivePermSetLicenseMetric, ActiveProfileMetric, ActivityFieldHistory, amzsec__asi_Telemetry_Data_Store__ChangeEvent, amzsec__asi_Telemetry_Data_Store__History, amzsec__asi_Telemetry_Data_Store__Share, amzsec__asi_Telemetry_Job_Log__ChangeEvent, amzsec__asi_Telemetry_Job_Log__History, amzsec__asi_Telemetry_Job_Log__Share, amzsec__asi_Telemetry_Requirement__ChangeEvent, amzsec__asi_Telemetry_Requirement__History, amzsec__asi_Telemetry_Requirement__Share, ApexClass, ApexComponent, ApexLog, ApexPage, ApexTestQueueItem, ApexTestResult, ApexTrigger, AssetChangeEvent, AssetHistory, AssetRelationshipHistory, AssetShare, AssignmentRule, AssociatedLocationHistory, AsyncApexJob, AuditTrailFileExportShare, AuthorizationFormConsentChangeEvent, AuthorizationFormConsentHistory, AuthorizationFormConsentShare, AuthorizationFormDataUseHistory, AuthorizationFormDataUseShare, AuthorizationFormHistory, AuthorizationFormShare, AuthorizationFormTextHistory, AuthProvider, AuthSession, BatchJobHistory, BatchJobPartFailedRecordHistory, BatchJobPartHistory, BatchJobShare, BrandTemplate, BriefcaseAssignmentChangeEvent, BriefcaseDefinitionChangeEvent, BusinessBrandShare, BusinessHours, BusinessProcess, CalcMatrixColumnRangeHistory, CalcProcStepRelationshipHistory, CalculationMatrixColumnHistory, CalculationMatrixHistory, CalculationMatrixRowHistory, CalculationMatrixShare, CalculationMatrixVersionHistory, CalculationProcedureHistory, CalculationProcedureShare, CalculationProcedureStepHistory, CalculationProcedureVariableHistory, CalculationProcedureVersionHistory, Calendar, CalendarViewShare, CallCenter, CallCoachConfigModifyEvent, CampaignChangeEvent, CampaignHistory, CampaignMemberChangeEvent, CampaignMemberStatusChangeEvent, CampaignShare, CaseChangeEvent, CaseHistory, CaseHistory2 CaseHistory2ChangeEvent, CaseRelatedIssueChangeEvent, CaseRelatedIssueHistory, CaseShare, CaseStatus, CaseTeamMember, CaseTeamRole, CaseTeamTemplate, CaseTeamTemplateMember, CaseTeamTemplateRecord, CategoryNode, ChangeRequestChangeEvent, ChangeRequestHistory, ChangeRequestRelatedIssueChangeEvent, ChangeRequestRelatedIssueHistory, ChangeRequestRelatedItemChangeEvent, ChangeRequestRelatedItemHistory, ChangeRequestShare, ChatRetirementRdyMetrics, ChatterActivity, ClientBrowser, CollaborationGroup, CollaborationGroupMember, CollaborationGroupMemberRequest, CollaborationInvitation, CommSubscriptionChannelTypeHistory, CommSubscriptionChannelTypeShare, CommSubscriptionConsentChangeEvent, CommSubscriptionConsentHistory, CommSubscriptionConsentShare, CommSubscriptionHistory, CommSubscriptionShare, CommSubscriptionTimingHistory, Community, ConnectedApplication, ContactChangeEvent, ContactHistory, ContactPointAddressChangeEvent, ContactPointAddressHistory, ContactPointAddressShare, ContactPointConsentChangeEvent, ContactPointConsentHistory, ContactPointConsentShare, ContactPointEmailChangeEvent, ContactPointEmailHistory, ContactPointEmailShare, ContactPointPhoneChangeEvent, ContactPointPhoneHistory, ContactPointPhoneShare, ContactPointTypeConsentChangeEvent, ContactPointTypeConsentHistory, ContactPointTypeConsentShare, ContactRequestShare, ContactShare, ContentDocumentChangeEvent, ContentDocumentHistory, ContentDocumentLink, ContentDocumentLinkChangeEvent, ContentDocumentSubscription, ContentFolderItem, ContentFolderLink, ContentFolderMember, ContentNote, ContentNotification, ContentTagSubscription, ContentUserSubscription, ContentVersionChangeEvent, ContentVersionComment, ContentVersionHistory, ContentVersionRating, ContentWorkspace, ContentWorkspaceMember, ContentWorkspacePermission, ContentWorkspaceSubscription, ContractChangeEvent, ContractHistory, ContractLineItemChangeEvent, ContractLineItemHistory, ContractStatus, Conversation, ConversationParticipant, CronJobDetail, CronTrigger, CustomBrand, CustomBrandAsset, CustomerShare, CustomHttpHeader, DashboardComponent, DataUseLegalBasisHistory, DataUseLegalBasisShare, DataUsePurposeHistory, DataUsePurposeShare, DecisionTableRecordset, DeleteEvent, DocumentAttachmentMap, Domain, DomainSite, DTRecordsetReplicaShare, EmailBounceEvent, EmailMessageChangeEvent, EmailServicesAddress, EmailServicesFunction, EmailTemplate, EmailTemplateChangeEvent, EngagementAttendeeChangeEvent, EngagementAttendeeHistory, EngagementChannelTypeHistory, EngagementChannelTypeShare, EngagementInteractionChangeEvent, EngagementInteractionHistory, EngagementInteractionShare, EngagementInterface, EngagementTopicChangeEvent, EngagementTopicHistory, EntitlementChangeEvent, EntitlementHistory, EntitlementTemplate, EntityMilestoneHistory, EntitySubscription, EventChangeEvent, EventRelationChangeEvent, EventRelayConfigChangeEvent, ExpressionSetHistory, ExpressionSetShare, ExpressionSetVersionHistory, ExternalEventMappingShare, FeedAttachment, FeedLike, FeedPollChoice, FeedPollVote, FeedSignal, FieldPermissions, FieldSecurityClassification, FiscalYearSettings, FlowInterviewLogShare, FlowInterviewShare, FlowOrchestrationEvent, FlowOrchestrationInstanceShare, FlowOrchestrationStageInstanceShare, FlowOrchestrationStepInstanceShare, FlowOrchestrationWorkItemShare, FlowRecordShare, FlowRecordVersionChangeEvent, FlowTestResultShare, Folder, Group, GroupMember, Holiday, IdeaComment, IdpEventLog, ImageHistory, ImageShare, IncidentChangeEvent, IncidentHistory, IncidentRelatedItemChangeEvent, IncidentRelatedItemHistory, IncidentShare, IndividualChangeEvent, IndividualHistory, IndividualShare, KnowledgeableUser, LeadChangeEvent, LeadHistory, LeadShare, LeadStatus, LightningExitByPageMetrics, LightningToggleMetrics, LightningUsageByAppTypeMetrics, LightningUsageByBrowserMetrics, LightningUsageByFlexiPageMetrics, LightningUsageByPageMetrics, ListEmailChangeEvent, ListEmailShare, ListView, LocationChangeEvent, LocationHistory, LocationShare, LocationTrustMeasureShare, LoginHistory, LoginIp, MacroChangeEvent, MacroHistory, MacroInstructionChangeEvent, MacroShare, MacroUsageShare, ManagedContentVariantChangeEvent, MessagingEndUserHistory, MessagingEndUserShare, MessagingSessionHistory, MessagingSessionShare, MilestoneType, MLEngagementEvent, ObjectPermissions, OpportunityChangeEvent, OpportunityContactRoleChangeEvent, OpportunityFieldHistory, OpportunityLineItemChangeEvent, OpportunityShare, OpportunityStage, OrderChangeEvent, OrderHistory, OrderItemChangeEvent, OrderItemHistory, OrderShare, OrderStatus, Organization, OrgEmailAddressSecurity, OrgWideEmailAddress, OutgoingEmail, OutgoingEmailRelation, PackageLicense, PartnerRole, PartyConsentChangeEvent, PartyConsentHistory, PartyConsentShare, Period, PermissionSet, PermissionSetAssignment, PermissionSetTabSetting, Pricebook2ChangeEvent, Pricebook2History, PricebookEntryChangeEvent, PricebookEntryHistory, PrivacyJobSessionShare, PrivacyObjectSessionShare, PrivacyRTBFRequestHistory, PrivacyRTBFRequestShare, PrivacySessionRecordFailureShare, ProblemChangeEvent, ProblemHistory, ProblemIncidentChangeEvent, ProblemIncidentHistory, ProblemRelatedItemChangeEvent, ProblemRelatedItemHistory, ProblemShare, ProcessDefinition, ProcessExceptionEvent, ProcessExceptionShare, ProcessInstanceChangeEvent, ProcessInstanceStep, ProcessInstanceStepChangeEvent, ProcessNode, Product2ChangeEvent, Product2History, ProductEntitlementTemplate, Profile, ProfileSkillEndorsementHistory, ProfileSkillHistory, ProfileSkillShare, ProfileSkillUserHistory, PromptActionShare, PromptErrorShare, QueueSobject, QuickTextChangeEvent, QuickTextHistory, QuickTextShare, QuickTextUsageShare, RecentlyViewed, RecommendationChangeEvent, RecordActionHistory, RecordAlertHistory, RecordAlertShare, RecordType, ScorecardShare, SellerHistory, SellerShare, ServiceContractChangeEvent, ServiceContractHistory, ServiceContractShare, SetupAuditTrail, SetupEntityAccess, SharingRecordCollectionShare, Site, SiteHistory, SiteRedirectMapping, SocialPersonaHistory, SocialPostChangeEvent, SocialPostHistory, SocialPostShare, SolutionHistory, SolutionStatus, StaticResource, StreamingChannelShare, TableauHostMappingShare, TaskChangeEvent, TaskPriority, TaskStatus, ThreatDetectionFeedback, TimelineObjectDefinitionChangeEvent, TodayGoalShare, Topic, TopicUserEvent, Translation, User, UserAppMenuCustomizationShare, UserChangeEvent, UserDefinedLabelAssignmentShare, UserDefinedLabelShare, UserEmailPreferredPersonShare, UserLicense, UserLogin, UserPackageLicense, UserPreference, UserPrioritizedRecordShare, UserProvisioningRequestShare, UserRole, UserShare, VideoCallChangeEvent, VideoCallParticipantChangeEvent, VideoCallRecordingChangeEvent, VideoCallShare, VisualforceAccessMetrics, VoiceCallChangeEvent, VoiceCallRecordingChangeEvent, VoiceCallShare, Vote, WebLink, WorkAccessShare, WorkBadgeDefinitionHistory, WorkBadgeDefinitionShare, WorkOrderChangeEvent, WorkOrderHistory, WorkOrderLineItemChangeEvent, WorkOrderLineItemHistory, WorkOrderLineItemStatus, WorkOrderShare, WorkOrderStatus, WorkPlanChangeEvent, WorkPlanHistory, WorkPlanShare, WorkPlanTemplateChangeEvent, WorkPlanTemplateEntryChangeEvent, WorkPlanTemplateEntryHistory, WorkPlanTemplateHistory, WorkPlanTemplateShare, WorkStepChangeEvent, WorkStepHistory, WorkStepStatus, WorkStepTemplateChangeEvent, WorkStepTemplateHistory, WorkStepTemplateShare, WorkThanksShare
```

### Configuring a Salesforce Marketing Cloud Account Engagement source
<a name="zero-etl-config-source-smcae"></a>

To create a connection for a Salesforce Marketing Cloud Account Engagement source, see [Connecting to Salesforce Marketing Cloud Account Engagement](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-salesforce-marketing-cloud-account-engagement.html).

Using your zero-ETL integration you can perform DDL operations for the following supported entities:


| Entity label | Entity name | 
| --- | --- | 
| Campaign | campaign | 
| List | list | 
| Dynamic Content | dynamic-content | 
| List Membership | list-membership | 
| Prospect | prospect | 
| User | user | 
| EmailTemplate | email-template | 
| EngagementStudioProgram | engagement-studio-program | 
| Landing Page | landing-page | 
| List Email | list-email | 

### Configuring an SAP OData source
<a name="zero-etl-config-source-sap"></a>

To create a connection for an SAP OData source, see [Connecting to SAP OData](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-sap-odata.html).

Zero-ETL integrations with an SAP OData source now supports entities starting with `EntityOf`. The ability to override the primary key is currently supported only for SAPOData `EntityOf` objects. Once this property has been set, it cannot be modified.

#### Support for special SAP entities
<a name="zero-etl-config-source-sap-entityof"></a>

AWS Glue zero-ETL supports SAP OData entities that use SAP's Operational Data Provisioning (ODP) framework as well as those that do not use the ODP framework (non-ODP entities). The list of supported entities includes: ODP\_SAP (Business Warehouse or BW extractors), ODP\_CDS (Core Data Services or CDS Views) and non-ODP based OData services for SAP APIs. AWS Glue zero-ETL supports full snapshot and incremental change data capture for ODP and non-ODP SAP entities. For ODP entities, incremental changes are captured using delta links. For non-ODP entities, if a queryable field that can be used for timestamp based ingestion is selected, then zero-ETL will use that field for incremental ingestion.

While ingesting data from SAP entities using AWS Glue zero-ETL, the following things should be noted:
+ Zero-ETL can only ingest SAP entities which have been configured for GET\_ENTITYSET method in SAP.
+ For non-ODP SAP entities, if a timestamp field is not selected for incremental updates, AWS Glue zero-ETL supports a full data extraction and replication with upserts only (no deletions).
+ For ODP extractor entities, we determine the valid primary key sets during data processing. Other SAP entities require an extra step of providing the valid primary key set as input, specifically SAP entities that start with `EntityOf`. When an `EntityOf` entity is selected, you will be directed to provide the set of primary keys.

![The screenshot shows configuring EntityOf primary key set for SAP OData source.](http://docs.aws.amazon.com/glue/latest/dg/images/zero-etl-settings-configure-entityof-primary-key-set.png)


### Configuring a ServiceNow source
<a name="zero-etl-config-source-servicenow"></a>

To create a connection for a ServiceNow source, see [Connecting to ServiceNow](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-servicenow.html).

#### Unsupported entities and fields for ServiceNow
<a name="zero-etl-config-source-servicenow-unsupported"></a>

The following ServiceNow entities or fields are unsupported for use in a zero-ETL integration with a ServiceNow source.

```
ais_acl_overrides, ais_async_genius_result, ais_async_request, ais_connection, ais_genius_result_configuration_parameters, ais_partition_health, ais_partition_health_response, ais_publish_history, ais_relevancy_training_execution, ais_relevancy_training_staging, ais_search_profile_relevancy_model, catalog_draft_entities, clone_log, clone_log0000, clone_log0001, clone_log0002, clone_log0003, clone_log0004, clone_log0005, clone_log0006, clone_log0007, cmdb_ie_context, cmdb_ie_log, cmdb_ie_run, cmdb_ire_partial_payloads_index, cmdb_qb_result_base$par1, cmdb$par1, discovery_log, discovery_log0000, discovery_log0001, discovery_log0002, discovery_log0003, discovery_log0004, discovery_log0005, discovery_log0006, discovery_log0007, ecc_agent_log, entitlement_data, entl_subscription_map, gs_entitlement_plugin_mapping, ih_transaction_exclusion, import_log, import_log0000, import_log0001, import_log0002, import_log0003, import_log0004, import_log0005, import_log0006, import_log0007, jrobin_archive, jrobin_database, jrobin_datasource, jrobin_definition, jrobin_graph, jrobin_graph_line, jrobin_graph_set, jrobin_graph_set_member, jrobin_shard, jrobin_shard_location, license_role_discovery_run, logger_configuration_validation, m2m_analytics_event_logger, m2m_user_consent_info, ml_artifact_object_store, np$sys_gen_ai_filter_sample, np$sys_ui_element, np$sys_ui_list_element, one_api_service_plan_feature_invocation, one_api_service_plan_invocation, open_nlu_predict_log, open_nlu_predict_log0000, open_nlu_predict_log0001, open_nlu_predict_log0002, open_nlu_predict_log0003, open_nlu_predict_log0004, open_nlu_predict_log0005, open_nlu_predict_log0006, open_nlu_predict_log0007, pa_diagnostic_log, pa_diagnostic_log0000, pa_diagnostic_log0001, pa_diagnostic_log0002, pa_diagnostic_log0003, pa_diagnostic_log0004, pa_diagnostic_log0005, pa_diagnostic_log0006, pa_diagnostic_log0007, pa_favorites, pa_job_log_rows, pa_job_log_rows0000, pa_job_log_rows0001, pa_job_log_rows0002, pa_job_log_rows0003, pa_job_log_rows0004, pa_job_log_rows0005, pa_job_log_rows0006, pa_job_log_rows0007, pa_migration_ignored_scores, pa_scores_l1, pa_scores_l2, pa_scores_migration_groups, par_dashboard_conversion_backup, promin_log, promin_log0000, promin_log0001, promin_log0002, promin_log0003, promin_log0004, promin_log0005, promin_log0006, promin_log0007, promin_request_object, proposed_change_verification_log, proposed_change_verification_log0000, proposed_change_verification_log0001, proposed_change_verification_log0002, proposed_change_verification_log0003, proposed_change_verification_log0004, proposed_change_verification_log0005, proposed_change_verification_log0006, proposed_change_verification_log0007, protected_table_log, protected_table_log0000, protected_table_log0001, protected_table_log0002, protected_table_log0003, protected_table_log0004, protected_table_log0005, protected_table_log0006, protected_table_log0007, pwd_history, qb_query_results, scan_log, scan_log0000, scan_log0001, scan_log0002, scan_log0003, scan_log0004, scan_log0005, scan_log0006, scan_log0007, schema_validator_error, sla_repair_log_entry, sla_repair_log_entry0000, sla_repair_log_entry0001, sla_repair_log_entry0002, sla_repair_log_entry0003, sla_repair_log_entry0004, sla_repair_log_entry0005, sla_repair_log_entry0006, sla_repair_log_entry0007, sla_repair_log_message, sla_repair_log_message0000, sla_repair_log_message0001, sla_repair_log_message0002, sla_repair_log_message0003, sla_repair_log_message0004, sla_repair_log_message0005, sla_repair_log_message0006, sla_repair_log_message0007, sn_bm_client_activity, sn_ci_analytics_st_actionable_notifs, sn_ci_analytics_st_conv_completion_by_cat, sn_ci_analytics_st_conv_dynamic_property, sn_ci_analytics_st_conversation, sn_ci_analytics_st_count_by_date, sn_ci_analytics_st_event_occurrence, sn_ci_analytics_st_event_property_value_trend, sn_ci_analytics_st_issue_auto_resolution, sn_ci_analytics_st_no_clicks, sn_ci_analytics_st_no_results, sn_ci_analytics_st_property_summary_by_event, sn_ci_analytics_st_session_count_per_locale, sn_ci_analytics_st_session_duration, sn_ci_analytics_st_spokes_usage, sn_ci_analytics_st_topic_execution_stats, sn_ci_analytics_st_topic_occurrence, sn_ci_analytics_st_trending_content, sn_ci_analytics_st_trending_queries, sn_ci_analytics_st_users, sn_cs_plugin_signatures, sn_cs_telemetry_log, sn_dfc_application, sn_dfc_product, sn_employee_position, sn_entitlement_st_subscription_application_family, sn_entitlement_st_subscription_application_users, sn_hr_sp_st_relevant_for_you, sn_instance_clone_log, sn_instance_clone_log0000, sn_instance_clone_log0001, sn_instance_clone_log0002, sn_instance_clone_log0003, sn_instance_clone_log0004, sn_instance_clone_log0005, sn_instance_clone_log0006, sn_instance_clone_log0007, sn_km_mr_st_kb_knowledge, sn_me_st_topic, sn_rf_conditional_definition, sn_rf_evaluation_type, sn_rf_evaluation_type_input, sn_rf_recommendation_action, sn_rf_recommendation_experience, sn_rf_recommendation_history, sn_rf_recommendation_rule, sn_rf_record_display_configuration, sn_rf_trend_definition, sn_sub_man_st_account_level_entitlement, sn_sub_man_st_gen_ai_metadata, sn_sub_man_st_instance_used_assist_count, sn_sub_man_st_now_assist_creator_instances, sn_sub_man_st_now_assists_aggregate, sn_sub_man_st_subscribed_groups, sn_sub_man_st_subscription_insights, sn_sub_man_st_subscription_license_detail_metric, sn_sub_man_st_unallocated_group_recommendation, sn_sub_man_st_unconfirmed_user_group, sn_wn_user_app_activity, sn_wn_user_content_activity, snc_monitorable_item, snpar_sched_export_v_scheduled_export_visualization, spotlight, spotlight_audit, spotlight_copy_log_row, spotlight_copy_log_row0000, spotlight_copy_log_row0001, spotlight_copy_log_row0002, spotlight_copy_log_row0003, spotlight_copy_log_row0004, spotlight_copy_log_row0005, spotlight_copy_log_row0006, spotlight_copy_log_row0007, spotlight_job_log_row, spotlight_job_log_row0000, spotlight_job_log_row0001, spotlight_job_log_row0002, spotlight_job_log_row0003, spotlight_job_log_row0004, spotlight_job_log_row0005, spotlight_job_log_row0006, spotlight_job_log_row0007, st_dfc_performance_metric, st_license_detail_metric, st_on_call_hour, st_sc_wizard_question, st_sys_catalog_items_and_variable_sets, st_sys_design_system_icon, subscription_instance_stats, svc_container_config, svc_environment_config, svc_layer_config, svc_model_assoc_ci, svc_model_checkpoint_attr, svc_model_obj_cluster, svc_model_obj_constraint, svc_model_obj_deployable, svc_model_obj_element, svc_model_obj_impact, svc_model_obj_impactrule, svc_model_obj_package, svc_model_obj_path, svc_model_obj_relation, svc_model_obj_service, sys_administrative_script_transaction, sys_amb_message, sys_amb_processor, sys_analytics_batch_state, sys_analytics_config, sys_analytics_data_points_error, sys_analytics_event, sys_analytics_logger, sys_analytics_logger_field, sys_app_payload_loader_rule, sys_app_payload_unloader_rule, sys_app_scan_payload, sys_app_scan_variable, sys_app_scan_variable_type, sys_archive_destroy_log, sys_archive_destroy_run, sys_archive_log, sys_archive_run, sys_atf_transaction_log, sys_attachment_doc, sys_attachment_doc_v2, sys_attachment_soft_deleted, sys_audit, sys_audit_relation, sys_auth_policy_api_allowed, sys_aw_registered_scripting_modal, sys_cache_flush, sys_data_egress_source, sys_dm_delete_count, sys_export_set_log, sys_export_set_log0000, sys_export_set_log0001, sys_export_set_log0002, sys_export_set_log0003, sys_export_set_log0004, sys_export_set_log0005, sys_export_set_log0006, sys_export_set_log0007, sys_flow_compiled_flow, sys_flow_compiled_flow_chunk, sys_flow_context_chunk, sys_flow_context_chunk_archive, sys_flow_context_inputs_chunk, sys_flow_execution_history, sys_flow_log, sys_flow_log0000, sys_flow_log0001, sys_flow_log0002, sys_flow_log0003, sys_flow_plan_context_binding, sys_flow_report_doc, sys_flow_report_doc_chunk, sys_flow_report_doc_chunk_archive, sys_flow_runtime_state_chunk, sys_flow_runtime_value_chunk, sys_flow_subflow_plan_chunk, sys_flow_trigger_plan_chunk, sys_flow_val_listener, sys_flow_value, sys_flow_value_chunk, sys_gen_ai_config_example, sys_gen_ai_feature_mapping, sys_gen_ai_strategy_mapping, sys_gen_ai_usage_log, sys_generative_ai_capability_definition, sys_generative_ai_log, sys_generative_ai_response_validator, sys_generative_ai_validator, sys_geo_routing, sys_geo_routing_config, sys_hop_token, sys_hub_action_plan_chunk, sys_hub_snapshot_chunk, sys_journal_field, sys_journal_field_edit, sys_json_chunk, sys_kaa_policy, sys_kaa_subidentity_assertion, sys_kaa_user_policy_mapping, sys_mapplication, sys_mass_encryption_job, sys_notification_execution_log, sys_notification_execution_log0000, sys_notification_execution_log0001, sys_notification_execution_log0002, sys_notification_execution_log0003, sys_notification_execution_log0004, sys_notification_execution_log0005, sys_notification_execution_log0006, sys_notification_execution_log0007, sys_nowmq_message, sys_nowmq_provider_param_definition, sys_orchestrator_action, sys_pd_asset_configuration, sys_pd_context_chunk, sys_pd_context_log, sys_pd_snapshot_chunk, sys_pd_trigger_license, sys_processing_framework_job, sys_query_index_hint, sys_query_rewrite, sys_query_string_log, sys_replication_queue, sys_replication_queue0, sys_replication_queue1, sys_replication_queue2, sys_replication_queue3, sys_replication_queue4, sys_replication_queue5, sys_replication_queue6, sys_replication_queue7, sys_request_performance, sys_rollback_conflict, sys_rollback_incremental, sys_rollback_log, sys_rollback_log0000, sys_rollback_log0001, sys_rollback_log0002, sys_rollback_log0003, sys_rollback_log0004, sys_rollback_log0005, sys_rollback_log0006, sys_rollback_log0007, sys_rollback_run, sys_rollback_schema_change, sys_rollback_schema_conflict, sys_rollback_sequence, sys_scheduler_assignment, sys_scheduler_memory_pressure_job_log, sys_script_adapter_rule, sys_script_batch_adapter_rule, sys_search_source_filter, sys_service_authentication, sys_signing_job, sys_suggestion_reader, sys_sync_history_review, sys_trend, sys_unreferenced_preview, sys_unreferenced_record_rule, sys_upgrade_manifest, sys_upgrade_state, sys_ux_asset_cache_buster, sys_ux_lib_component_prop, sys_ux_lib_presource, sys_ux_page_action, sys_ux_page_action_binding, sysevent_queue_runtime, syslog, syslog_app_scope0000, syslog_app_scope0001, syslog_app_scope0002, syslog_app_scope0003, syslog_app_scope0004, syslog_app_scope0005, syslog_app_scope0006, syslog_app_scope0007, syslog_email0000, syslog_email0001, syslog_email0002, syslog_email0003, syslog_email0004, syslog_email0005, syslog_email0006, syslog_email0007, syslog_transaction, syslog_transaction0000, syslog_transaction0001, syslog_transaction0002, syslog_transaction0003, syslog_transaction0004, syslog_transaction0005, syslog_transaction0006, syslog_transaction0007, syslog0000, syslog0001, syslog0002, syslog0003, syslog0004, syslog0005, syslog0006, syslog0007, ts_attachment, ts_chain, ts_deleted_doc, ts_document, ts_field, ts_index_stats, ts_phrase, ts_search_stats, ts_v4_attachment, ts_word, ua_app_metadata, ua_audit_stats, ua_extra_page, ua_monitor_property, ua_monitor_property_audit, ua_shared_service, ua_sn_table_inventory, ua_sp_known_bot, ua_upload_log, spotlight_criteria, pa_snapshots, pa_widget_indicators, pa_widgets, sn_cim_register, global, gsw_change_log, gsw_content, gsw_content_group, gsw_content_information, gsw_status_of_content, multi_factor_browser_fingerprint, multi_factor_criteria, pa_filters, password_policy, plan_execution, plan_mysql, plan_oracle, plan_postgres, sc_rest_api_without_access_policy, sn_actsub_activity, sn_actsub_activity_fanout, sn_actsub_activity_stream, sn_actsub_activity_type, sn_actsub_atype_attributes, sn_actsub_atype_notif_pref, sn_actsub_module, sn_actsub_notif_object, sn_actsub_subobject_stream, sn_actsub_subscribable_object, sn_actsub_subscription_notif_pref, sn_actsub_user_stream, sn_appclient_store_outbound_http_quota, sn_appcreator_app_template, sn_critical_update, sn_docker_spoke_images, sn_employee_app, sn_employee_app_access, sn_employee_app_access_criteria, sn_entitlement_genai_assist_counts, sn_entitlement_genai_creator_user_counts, sn_entitlement_genai_creator_users, sn_mif_instance, sn_mif_sync_data, sn_mif_sync_status, sn_mif_table_registration, sn_mif_trust_config, sn_vsc_best_practice_configurations, sn_vsc_best_practice_goals, sn_vsc_changed_hardening_settings, sn_vsc_changed_scan_findings, sn_vsc_check_security_area, sn_vsc_elevation_event, sn_vsc_event, sn_vsc_export_event, sn_vsc_export_setting, sn_vsc_harc_compliance_status_lookup, sn_vsc_hardening_compliance_scores, sn_vsc_impersonation_event, sn_vsc_instance_hardening_settings, sn_vsc_login_event, sn_vsc_scan_comparisons, sn_vsc_scan_summary, sn_vsc_security_check_categories, sn_vsc_security_check_configurations, sn_vsc_security_configuration_groups, sn_vsc_security_privacy_capabilities, sn_vsc_updated_settings, sn_vsc_user_comparisons, sys_app_hash_inventory, sys_coalesce_strategy_deferred, sys_flow_secure_data, sys_formula_function, sys_geocoding_request, sys_global_file_hash, sys_import_set_row, sys_index, sys_index_explain, sys_installation_schedule, sys_installation_schedule_item, sys_offline_app, sys_package, sys_package_dependency_item, sys_package_dependency_m2m, sys_plugins, sys_querystat, sys_reap_package, sys_scoped_plugin, sys_stage_storage_alias, sys_storage_alias, sys_storage_table_alias, sys_store_app, sys_table_partition, sys_upgrade_history_log, sys_user_public_credential, sys_webauthn_authentication_request, sys_webauthn_registration_request, syslog_app_scope, syslog_email, syslog_page_timing, ua_instance_state_config, v_expression_cache, v_private_cache, v_shared_cache, sys_amb_message0002, sys_amb_message0004, sys_amb_message0005, sys_metadata, v_par_unified_report_viz
```

### Configuring a Zendesk source
<a name="zero-etl-config-source-zendesk"></a>

To create a connection for a Zendesk source, see [Connecting to Zendesk](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-zendesk.html).

Using your zero-ETL integration you can perform the following DDL operations for supported entities:


| Entity label | Entity name | Create supported | Update supported | Delete supported | 
| --- | --- | --- | --- | --- | 
| Tickets | tickets | Y | Y | Y | 
| User | users | Y | Y | Y | 
| Satisfaction Rating | satisfaction-rating | Y | Y | N | 
| Articles | articles | Y | Y | N | 
| Organization | organizations | Y | Y | Y | 
| Calls | calls | Y | Y | N | 
| Call Legs | legs | Y | Y | N | 

### Configuring a Zoho CRM source
<a name="zero-etl-config-source-zoho"></a>

To create a connection for a Zoho CRM source, see [Connecting to Zoho CRM](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-zoho-crm.html).

Using your zero-ETL integration you can perform the following DDL operations for supported entities:


| Entity label | Entity name | DML-Insert | DML-Modify | DML-Delete | DDL-Insert | DDL-Modify | DDL-Delete | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Leads | lead | Y | Y | Y | Y | Y | Y | 
| Accounts | account | Y | Y | Y | Y | Y | Y | 
| Contacts | contact | Y | Y | Y | Y | Y | Y | 
| Campaigns | campaign | Y | Y | Y | Y | Y | Y | 
| Tasks | task | Y | Y | Y | Y | Y | Y | 
| Events | event | Y | Y | Y | Y | Y | Y | 
| Calls | call | Y | Y | Y | Y | Y | Y | 
| Solutions | solution | Y | Y | Y | Y | Y | Y | 
| Products | product | Y | Y | Y | Y | Y | Y | 
| Vendors | vendor | Y | Y | Y | Y | Y | Y | 
| Quotes | quote | Y | Y | Y | Y | Y | Y | 
| Sales Orders | sales-order | Y | Y | Y | Y | Y | Y | 
| Purchase Orders | purchase-order | Y | Y | Y | Y | Y | Y | 
| Invoices | invoice | Y | Y | Y | Y | Y | Y | 
| Cases | case | Y | Y | Y | Y | Y | Y | 
| Price Books | price-book | Y | Y | Y | Y | Y | Y | 

### Configuring a Facebook Ads source
<a name="zero-etl-config-source-facebook"></a>

To create a connection for a Facebook Ads source, see [Connecting to Facebook Ads](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-facebook-ads.html).

Using your zero-ETL integration you can perform the following DDL operations for supported entities:


| Entity label | Entity name | Create supported | Update supported | Delete supported | 
| --- | --- | --- | --- | --- | 
| Adset | \*/adsets | Y | Y | Y | 
| Campaign | \*/campaigns | Y | Y | Y | 
| Ads | \*/ads | Y | Y | Y | 

### Configuring an Instagram Ads source
<a name="zero-etl-config-source-instagram"></a>

To create a connection for an Instagram Ads source, see [Connecting to Instagram Ads](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-instagram-ads.html).

Using your zero-ETL integration you can perform the following DDL operations for supported entities:


| Entity name | Create supported | Update supported | Delete supported | 
| --- | --- | --- | --- | 
| \*/adsets | Y | Y | Y | 
| \*/campaigns | Y | Y | Y | 
| \*/ads | Y | Y | Y | 

### Setting up the source role for integration
<a name="zero-etl-config-source-role"></a>

Create a source role to allow the zero-ETL integration to access your connection. This is applicable only for SaaS sources. This is a prerequisite for creating integrations with SaaS sources.

**Note**  
To restrict access to only a few connections, you can first create the connection to obtain the connection ARN. See [Configuring a source for a zero-ETL integration](#zero-etl-sources).

Create a role which has permissions for the integration to access the connection:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueConnections",
            "Effect": "Allow",
            "Action": [
                "glue:GetConnections",
                "glue:GetConnection"
            ],
            "Resource": [
                "arn:aws:glue:*:111122223333:catalog",
                "arn:aws:glue:us-east-1:111122223333:connection/*"
            ]
        },
        {
            "Sid": "GlueActionBasedPermissions",
            "Effect": "Allow",
            "Action": [
                "glue:ListEntities",
                "glue:RefreshOAuth2Tokens"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "CloudWatchLogging",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "glue.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Associate the role with the connection using the AWS Glue CLI or API:

```
aws glue create-integration-resource-property \
--resource-arn arn:aws:glue:us-east-1:123456789012:connection/{{connectionName}} \
--source-processing-properties "{\"RoleArn\" : \"arn:aws:iam::123456789012:role/{{rolename}}\"}" \
--region us-east-1
```

## Setting up Oracle Database at AWS as source
<a name="zero-etl-config-source-oracle"></a>

Currently AWS Glue supports Oracle Databases at AWS as source and Redshift as target. The details of the setup can be found at [Setting up zero-ETL for Oracle Database at AWS](https://docs.aws.amazon.com/odb/latest/UserGuide/setting-up-zero-etl.html).