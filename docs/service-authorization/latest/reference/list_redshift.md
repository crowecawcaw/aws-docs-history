

# Actions, resources, and condition keys for Amazon Redshift
<a name="list_redshift"></a>

Amazon Redshift (service prefix: `redshift`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/redshift/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-authentication-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/redshift/redshift.json) for this service.

**Topics**
+ [API operations defined by Amazon Redshift](#list_redshift-operations)
+ [Actions defined by Amazon Redshift](#list_redshift-actions-as-permissions)
+ [Permission-only actions for Amazon Redshift](#list_redshift-permission-only-actions)
+ [Resource types defined by Amazon Redshift](#list_redshift-resources-for-iam-policies)
+ [Condition keys for Amazon Redshift](#list_redshift-policy-keys)

## API operations defined by Amazon Redshift
<a name="list_redshift-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_redshift-actions-as-permissions).




- **   AcceptReservedNodeExchange  **
  - **IAM action:**  [redshift:AcceptReservedNodeExchange](#list_redshift-action-AcceptReservedNodeExchange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddPartner  **
  - **IAM action:**  [redshift:AddPartner](#list_redshift-action-AddPartner)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:DeletePartner](#list_redshift-action-DeletePartner)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AssociateDataShareConsumer  **
  - **IAM action:**  [redshift:AssociateDataShareConsumer](#list_redshift-action-AssociateDataShareConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AuthorizeClusterSecurityGroupIngress  **
  - **IAM action:**  [redshift:AuthorizeClusterSecurityGroupIngress](#list_redshift-action-AuthorizeClusterSecurityGroupIngress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AuthorizeDataShare  **
  - **IAM action:**  [redshift:AuthorizeDataShare](#list_redshift-action-AuthorizeDataShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AuthorizeEndpointAccess  **
  - **IAM action:**  [redshift:AuthorizeEndpointAccess](#list_redshift-action-AuthorizeEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AuthorizeSnapshotAccess  **
  - **IAM action:**  [redshift:AuthorizeSnapshotAccess](#list_redshift-action-AuthorizeSnapshotAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   BatchDeleteClusterSnapshots  **
  - **IAM action:**  [redshift:BatchDeleteClusterSnapshots](#list_redshift-action-BatchDeleteClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchModifyClusterSnapshots  **
  - **IAM action:**  [redshift:BatchModifyClusterSnapshots](#list_redshift-action-BatchModifyClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelResize  **
  - **IAM action:**  [redshift:CancelResize](#list_redshift-action-CancelResize) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyClusterSnapshot  **
  - **IAM action:**  [redshift:CopyClusterSnapshot](#list_redshift-action-CopyClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAuthenticationProfile  **
  - **IAM action:**  [redshift:CreateAuthenticationProfile](#list_redshift-action-CreateAuthenticationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCluster  **
  - **IAM action:**  [redshift:AssociateDataShareConsumer](#list_redshift-action-AssociateDataShareConsumer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateCluster](#list_redshift-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [redshift:RegisterNamespace](#list_redshift-action-RegisterNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift.amazonaws.com / **Access level:** Write

- **   CreateClusterParameterGroup  **
  - **IAM action:**  [redshift:CreateClusterParameterGroup](#list_redshift-action-CreateClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateClusterSecurityGroup  **
  - **IAM action:**  [redshift:CreateClusterSecurityGroup](#list_redshift-action-CreateClusterSecurityGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateClusterSnapshot  **
  - **IAM action:**  [redshift:CreateClusterSnapshot](#list_redshift-action-CreateClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateClusterSubnetGroup  **
  - **IAM action:**  [redshift:CreateClusterSubnetGroup](#list_redshift-action-CreateClusterSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomDomainAssociation  **
  - **IAM action:**  [redshift:CreateCustomDomainAssociation](#list_redshift-action-CreateCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEndpointAccess  **
  - **IAM action:**  [redshift:CreateEndpointAccess](#list_redshift-action-CreateEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEventSubscription  **
  - **IAM action:**  [redshift:CreateEventSubscription](#list_redshift-action-CreateEventSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHsmClientCertificate  **
  - **IAM action:**  [redshift:CreateHsmClientCertificate](#list_redshift-action-CreateHsmClientCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHsmConfiguration  **
  - **IAM action:**  [redshift:CreateHsmConfiguration](#list_redshift-action-CreateHsmConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIntegration  **
  - **IAM action:**  [redshift:CreateIntegration](#list_redshift-action-CreateIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateQev2IdcApplication  **
  - **IAM action:**  [redshift:CreateQev2IdcApplication](#list_redshift-action-CreateQev2IdcApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRedshiftIdcApplication  **
  - **IAM action:**  [redshift:CreateRedshiftIdcApplication](#list_redshift-action-CreateRedshiftIdcApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateScheduledAction  **
  - **IAM action:**  [redshift:CreateScheduledAction](#list_redshift-action-CreateScheduledAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:PauseCluster](#list_redshift-action-PauseCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:ResizeCluster](#list_redshift-action-ResizeCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:ResumeCluster](#list_redshift-action-ResumeCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift.amazonaws.com / **Access level:** Write

- **   CreateSnapshotCopyGrant  **
  - **IAM action:**  [redshift:CreateSnapshotCopyGrant](#list_redshift-action-CreateSnapshotCopyGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSnapshotSchedule  **
  - **IAM action:**  [redshift:CreateSnapshotSchedule](#list_redshift-action-CreateSnapshotSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTags  **
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [redshift:DeleteTags](#list_redshift-action-DeleteTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUsageLimit  **
  - **IAM action:**  [redshift:CreateTags](#list_redshift-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [redshift:CreateUsageLimit](#list_redshift-action-CreateUsageLimit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeauthorizeDataShare  **
  - **IAM action:**  [redshift:DeauthorizeDataShare](#list_redshift-action-DeauthorizeDataShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteAuthenticationProfile  **
  - **IAM action:**  [redshift:DeleteAuthenticationProfile](#list_redshift-action-DeleteAuthenticationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [redshift:CreateClusterSnapshot](#list_redshift-action-CreateClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:DeleteCluster](#list_redshift-action-DeleteCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteClusterParameterGroup  **
  - **IAM action:**  [redshift:DeleteClusterParameterGroup](#list_redshift-action-DeleteClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterSecurityGroup  **
  - **IAM action:**  [redshift:DeleteClusterSecurityGroup](#list_redshift-action-DeleteClusterSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterSnapshot  **
  - **IAM action:**  [redshift:DeleteClusterSnapshot](#list_redshift-action-DeleteClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterSubnetGroup  **
  - **IAM action:**  [redshift:DeleteClusterSubnetGroup](#list_redshift-action-DeleteClusterSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomDomainAssociation  **
  - **IAM action:**  [redshift:DeleteCustomDomainAssociation](#list_redshift-action-DeleteCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpointAccess  **
  - **IAM action:**  [redshift:DeleteEndpointAccess](#list_redshift-action-DeleteEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSubscription  **
  - **IAM action:**  [redshift:DeleteEventSubscription](#list_redshift-action-DeleteEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHsmClientCertificate  **
  - **IAM action:**  [redshift:DeleteHsmClientCertificate](#list_redshift-action-DeleteHsmClientCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHsmConfiguration  **
  - **IAM action:**  [redshift:DeleteHsmConfiguration](#list_redshift-action-DeleteHsmConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **IAM action:**  [redshift:DeleteIntegration](#list_redshift-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartner  **
  - **IAM action:**  [redshift:DeletePartner](#list_redshift-action-DeletePartner) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQev2IdcApplication  **
  - **IAM action:**  [redshift:DeleteQev2IdcApplication](#list_redshift-action-DeleteQev2IdcApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRedshiftIdcApplication  **
  - **IAM action:**  [redshift:DeleteRedshiftIdcApplication](#list_redshift-action-DeleteRedshiftIdcApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [redshift:DeleteResourcePolicy](#list_redshift-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteScheduledAction  **
  - **IAM action:**  [redshift:DeleteScheduledAction](#list_redshift-action-DeleteScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshotCopyGrant  **
  - **IAM action:**  [redshift:DeleteSnapshotCopyGrant](#list_redshift-action-DeleteSnapshotCopyGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshotSchedule  **
  - **IAM action:**  [redshift:DeleteSnapshotSchedule](#list_redshift-action-DeleteSnapshotSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [redshift:DeleteTags](#list_redshift-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteUsageLimit  **
  - **IAM action:**  [redshift:DeleteUsageLimit](#list_redshift-action-DeleteUsageLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterNamespace  **
  - **IAM action:**  [redshift:DeregisterNamespace](#list_redshift-action-DeregisterNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountAttributes  **
  - **IAM action:**  [redshift:DescribeAccountAttributes](#list_redshift-action-DescribeAccountAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAuthenticationProfiles  **
  - **IAM action:**  [redshift:DescribeAuthenticationProfiles](#list_redshift-action-DescribeAuthenticationProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterDbRevisions  **
  - **IAM action:**  [redshift:DescribeClusterDbRevisions](#list_redshift-action-DescribeClusterDbRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeClusterParameterGroups  **
  - **IAM action:**  [redshift:DescribeClusterParameterGroups](#list_redshift-action-DescribeClusterParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterParameters  **
  - **IAM action:**  [redshift:DescribeClusterParameters](#list_redshift-action-DescribeClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterSecurityGroups  **
  - **IAM action:**  [redshift:DescribeClusterSecurityGroups](#list_redshift-action-DescribeClusterSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterSnapshots  **
  - **IAM action:**  [redshift:DescribeClusterSnapshots](#list_redshift-action-DescribeClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterSubnetGroups  **
  - **IAM action:**  [redshift:DescribeClusterSubnetGroups](#list_redshift-action-DescribeClusterSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterTracks  **
  - **IAM action:**  [redshift:DescribeClusterTracks](#list_redshift-action-DescribeClusterTracks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeClusterVersions  **
  - **IAM action:**  [redshift:DescribeClusterVersions](#list_redshift-action-DescribeClusterVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusters  **
  - **IAM action:**  [redshift:DescribeClusters](#list_redshift-action-DescribeClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCustomDomainAssociations  **
  - **IAM action:**  [redshift:DescribeCustomDomainAssociations](#list_redshift-action-DescribeCustomDomainAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDataShares  **
  - **IAM action:**  [redshift:DescribeDataShares](#list_redshift-action-DescribeDataShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSharesForConsumer  **
  - **IAM action:**  [redshift:DescribeDataSharesForConsumer](#list_redshift-action-DescribeDataSharesForConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSharesForProducer  **
  - **IAM action:**  [redshift:DescribeDataSharesForProducer](#list_redshift-action-DescribeDataSharesForProducer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDefaultClusterParameters  **
  - **IAM action:**  [redshift:DescribeDefaultClusterParameters](#list_redshift-action-DescribeDefaultClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpointAccess  **
  - **IAM action:**  [redshift:DescribeEndpointAccess](#list_redshift-action-DescribeEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpointAuthorization  **
  - **IAM action:**  [redshift:DescribeEndpointAuthorization](#list_redshift-action-DescribeEndpointAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventCategories  **
  - **IAM action:**  [redshift:DescribeEventCategories](#list_redshift-action-DescribeEventCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventSubscriptions  **
  - **IAM action:**  [redshift:DescribeEventSubscriptions](#list_redshift-action-DescribeEventSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEvents  **
  - **IAM action:**  [redshift:DescribeEvents](#list_redshift-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeHsmClientCertificates  **
  - **IAM action:**  [redshift:DescribeHsmClientCertificates](#list_redshift-action-DescribeHsmClientCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHsmConfigurations  **
  - **IAM action:**  [redshift:DescribeHsmConfigurations](#list_redshift-action-DescribeHsmConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInboundIntegrations  **
  - **IAM action:**  [redshift:DescribeInboundIntegrations](#list_redshift-action-DescribeInboundIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeIntegrations  **
  - **IAM action:**  [redshift:DescribeIntegrations](#list_redshift-action-DescribeIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLoggingStatus  **
  - **IAM action:**  [redshift:DescribeLoggingStatus](#list_redshift-action-DescribeLoggingStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNodeConfigurationOptions  **
  - **IAM action:**  [redshift:DescribeNodeConfigurationOptions](#list_redshift-action-DescribeNodeConfigurationOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOrderableClusterOptions  **
  - **IAM action:**  [redshift:DescribeOrderableClusterOptions](#list_redshift-action-DescribeOrderableClusterOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePartners  **
  - **IAM action:**  [redshift:DescribePartners](#list_redshift-action-DescribePartners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQev2IdcApplications  **
  - **IAM action:**  [redshift:DescribeQev2IdcApplications](#list_redshift-action-DescribeQev2IdcApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRedshiftIdcApplications  **
  - **IAM action:**  [redshift:DescribeRedshiftIdcApplications](#list_redshift-action-DescribeRedshiftIdcApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReservedNodeExchangeStatus  **
  - **IAM action:**  [redshift:DescribeReservedNodeExchangeStatus](#list_redshift-action-DescribeReservedNodeExchangeStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedNodeOfferings  **
  - **IAM action:**  [redshift:DescribeReservedNodeOfferings](#list_redshift-action-DescribeReservedNodeOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedNodes  **
  - **IAM action:**  [redshift:DescribeReservedNodes](#list_redshift-action-DescribeReservedNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResize  **
  - **IAM action:**  [redshift:DescribeResize](#list_redshift-action-DescribeResize) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScheduledActions  **
  - **IAM action:**  [redshift:DescribeScheduledActions](#list_redshift-action-DescribeScheduledActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshotCopyGrants  **
  - **IAM action:**  [redshift:DescribeSnapshotCopyGrants](#list_redshift-action-DescribeSnapshotCopyGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshotSchedules  **
  - **IAM action:**  [redshift:DescribeSnapshotSchedules](#list_redshift-action-DescribeSnapshotSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStorage  **
  - **IAM action:**  [redshift:DescribeStorage](#list_redshift-action-DescribeStorage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTableRestoreStatus  **
  - **IAM action:**  [redshift:DescribeTableRestoreStatus](#list_redshift-action-DescribeTableRestoreStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTags  **
  - **IAM action:**  [redshift:DescribeTags](#list_redshift-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUsageLimits  **
  - **IAM action:**  [redshift:DescribeUsageLimits](#list_redshift-action-DescribeUsageLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableLogging  **
  - **IAM action:**  [redshift:DisableLogging](#list_redshift-action-DisableLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableSnapshotCopy  **
  - **IAM action:**  [redshift:DisableSnapshotCopy](#list_redshift-action-DisableSnapshotCopy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDataShareConsumer  **
  - **IAM action:**  [redshift:DisassociateDataShareConsumer](#list_redshift-action-DisassociateDataShareConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableLogging  **
  - **IAM action:**  [redshift:EnableLogging](#list_redshift-action-EnableLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableSnapshotCopy  **
  - **IAM action:**  [redshift:EnableSnapshotCopy](#list_redshift-action-EnableSnapshotCopy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverPrimaryCompute  **
  - **IAM action:**  [redshift:FailoverPrimaryCompute](#list_redshift-action-FailoverPrimaryCompute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetClusterCredentials  **
  - **IAM action:**  [redshift:CreateClusterUser](#list_redshift-action-CreateClusterUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [redshift:GetClusterCredentials](#list_redshift-action-GetClusterCredentials)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:JoinGroup](#list_redshift-action-JoinGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   GetClusterCredentialsWithIAM  **
  - **IAM action:**  [redshift:GetClusterCredentialsWithIAM](#list_redshift-action-GetClusterCredentialsWithIAM) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetIdentityCenterAuthToken  **
  - **IAM action:**  [redshift:GetIdentityCenterAuthToken](#list_redshift-action-GetIdentityCenterAuthToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReservedNodeExchangeConfigurationOptions  **
  - **IAM action:**  [redshift:GetReservedNodeExchangeConfigurationOptions](#list_redshift-action-GetReservedNodeExchangeConfigurationOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReservedNodeExchangeOfferings  **
  - **IAM action:**  [redshift:GetReservedNodeExchangeOfferings](#list_redshift-action-GetReservedNodeExchangeOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [redshift:GetResourcePolicy](#list_redshift-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecommendations  **
  - **IAM action:**  [redshift:ListRecommendations](#list_redshift-action-ListRecommendations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [redshift:ViewQueriesInConsole](#list_redshift-action-ViewQueriesInConsole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ModifyAquaConfiguration  **
  - **IAM action:**  [redshift:ModifyAquaConfiguration](#list_redshift-action-ModifyAquaConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyAuthenticationProfile  **
  - **IAM action:**  [redshift:ModifyAuthenticationProfile](#list_redshift-action-ModifyAuthenticationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCluster  **
  - **IAM action:**  [redshift:ModifyCluster](#list_redshift-action-ModifyCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClusterDbRevision  **
  - **IAM action:**  [redshift:ModifyClusterDbRevision](#list_redshift-action-ModifyClusterDbRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClusterIamRoles  **
  - **IAM action:**  [redshift:ModifyClusterIamRoles](#list_redshift-action-ModifyClusterIamRoles)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift.amazonaws.com / **Access level:** Write

- **   ModifyClusterMaintenance  **
  - **IAM action:**  [redshift:ModifyClusterMaintenance](#list_redshift-action-ModifyClusterMaintenance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClusterParameterGroup  **
  - **IAM action:**  [redshift:ModifyClusterParameterGroup](#list_redshift-action-ModifyClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClusterSnapshot  **
  - **IAM action:**  [redshift:ModifyClusterSnapshot](#list_redshift-action-ModifyClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClusterSnapshotSchedule  **
  - **IAM action:**  [redshift:ModifyClusterSnapshotSchedule](#list_redshift-action-ModifyClusterSnapshotSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClusterSubnetGroup  **
  - **IAM action:**  [redshift:ModifyClusterSubnetGroup](#list_redshift-action-ModifyClusterSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCustomDomainAssociation  **
  - **IAM action:**  [redshift:ModifyCustomDomainAssociation](#list_redshift-action-ModifyCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyEndpointAccess  **
  - **IAM action:**  [redshift:ModifyEndpointAccess](#list_redshift-action-ModifyEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyEventSubscription  **
  - **IAM action:**  [redshift:ModifyEventSubscription](#list_redshift-action-ModifyEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyIntegration  **
  - **IAM action:**  [redshift:ModifyIntegration](#list_redshift-action-ModifyIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyLakehouseConfiguration  **
  - **IAM action:**  [redshift:AssociateDataShareConsumer](#list_redshift-action-AssociateDataShareConsumer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:DeregisterNamespace](#list_redshift-action-DeregisterNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:RegisterNamespace](#list_redshift-action-RegisterNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift.amazonaws.com / **Access level:** Write

- **   ModifyQev2IdcApplication  **
  - **IAM action:**  [redshift:ModifyQev2IdcApplication](#list_redshift-action-ModifyQev2IdcApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyRedshiftIdcApplication  **
  - **IAM action:**  [redshift:ModifyRedshiftIdcApplication](#list_redshift-action-ModifyRedshiftIdcApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyScheduledAction  **
  - **IAM action:**  [redshift:ModifyScheduledAction](#list_redshift-action-ModifyScheduledAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:PauseCluster](#list_redshift-action-PauseCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:ResizeCluster](#list_redshift-action-ResizeCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:ResumeCluster](#list_redshift-action-ResumeCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift.amazonaws.com / **Access level:** Write

- **   ModifySnapshotCopyRetentionPeriod  **
  - **IAM action:**  [redshift:ModifySnapshotCopyRetentionPeriod](#list_redshift-action-ModifySnapshotCopyRetentionPeriod) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifySnapshotSchedule  **
  - **IAM action:**  [redshift:ModifySnapshotSchedule](#list_redshift-action-ModifySnapshotSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyUsageLimit  **
  - **IAM action:**  [redshift:ModifyUsageLimit](#list_redshift-action-ModifyUsageLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PauseCluster  **
  - **IAM action:**  [redshift:PauseCluster](#list_redshift-action-PauseCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PurchaseReservedNodeOffering  **
  - **IAM action:**  [redshift:PurchaseReservedNodeOffering](#list_redshift-action-PurchaseReservedNodeOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [redshift:PutResourcePolicy](#list_redshift-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RebootCluster  **
  - **IAM action:**  [redshift:RebootCluster](#list_redshift-action-RebootCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterNamespace  **
  - **IAM action:**  [redshift:RegisterNamespace](#list_redshift-action-RegisterNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectDataShare  **
  - **IAM action:**  [redshift:RejectDataShare](#list_redshift-action-RejectDataShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ResetClusterParameterGroup  **
  - **IAM action:**  [redshift:ResetClusterParameterGroup](#list_redshift-action-ResetClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResizeCluster  **
  - **IAM action:**  [redshift:ResizeCluster](#list_redshift-action-ResizeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreFromClusterSnapshot  **
  - **IAM action:**  [redshift:AssociateDataShareConsumer](#list_redshift-action-AssociateDataShareConsumer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:RegisterNamespace](#list_redshift-action-RegisterNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:RestoreFromClusterSnapshot](#list_redshift-action-RestoreFromClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift.amazonaws.com / **Access level:** Write

- **   RestoreTableFromClusterSnapshot  **
  - **IAM action:**  [redshift:RestoreTableFromClusterSnapshot](#list_redshift-action-RestoreTableFromClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeCluster  **
  - **IAM action:**  [redshift:ResumeCluster](#list_redshift-action-ResumeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeClusterSecurityGroupIngress  **
  - **IAM action:**  [redshift:RevokeClusterSecurityGroupIngress](#list_redshift-action-RevokeClusterSecurityGroupIngress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeEndpointAccess  **
  - **IAM action:**  [redshift:RevokeEndpointAccess](#list_redshift-action-RevokeEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RevokeSnapshotAccess  **
  - **IAM action:**  [redshift:RevokeSnapshotAccess](#list_redshift-action-RevokeSnapshotAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RotateEncryptionKey  **
  - **IAM action:**  [redshift:RotateEncryptionKey](#list_redshift-action-RotateEncryptionKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePartnerStatus  **
  - **IAM action:**  [redshift:UpdatePartnerStatus](#list_redshift-action-UpdatePartnerStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Redshift
<a name="list_redshift-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptReservedNodeExchange](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AcceptReservedNodeExchange.html)  **
  - **Description:** Grants permission to exchange a DC1 reserved node for a DC2 reserved node with no changes to the configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddPartner](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AddPartner.html)  **
  - **Description:** Grants permission to add a partner integration to a cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateDataShareConsumer](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AssociateDataShareConsumer.html)  **
  - **Description:** Grants permission to associate a consumer to a datashare
  - **Resource types (\*required):** [datashare\*](#list_redshift-resource-datashare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[redshift:AllowWrites](#list_redshift-redshift_AllowWrites)<br />[redshift:ConsumerArn](#list_redshift-redshift_ConsumerArn)
  - **Access level:** Write

- **   [AuthorizeClusterSecurityGroupIngress](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AuthorizeClusterSecurityGroupIngress.html)  **
  - **Description:** Grants permission to add an inbound (ingress) rule to an Amazon Redshift security group
  - **Resource types (\*required):** [securitygroup\*](#list_redshift-resource-securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securitygroupingress-ec2securitygroup\*](#list_redshift-resource-securitygroupingress-ec2securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AuthorizeDataShare](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AuthorizeDataShare.html)  **
  - **Description:** Grants permission to authorize the specified datashare consumer to consume a datashare
  - **Resource types (\*required):** [datashare\*](#list_redshift-resource-datashare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[redshift:AllowWrites](#list_redshift-redshift_AllowWrites)<br />[redshift:ConsumerIdentifier](#list_redshift-redshift_ConsumerIdentifier)
  - **Access level:** Permissions management, Write

- **   [AuthorizeEndpointAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AuthorizeEndpointAccess.html)  **
  - **Description:** Grants permission to authorize endpoint related activities for redshift-managed vpc endpoint
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AuthorizeSnapshotAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AuthorizeSnapshotAccess.html)  **
  - **Description:** Grants permission to the specified AWS account to restore a snapshot
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [BatchDeleteClusterSnapshots](https://docs.aws.amazon.com/redshift/latest/APIReference/API_BatchDeleteClusterSnapshots.html)  **
  - **Description:** Grants permission to delete snapshots in a batch of size upto 100
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchModifyClusterSnapshots](https://docs.aws.amazon.com/redshift/latest/APIReference/API_BatchModifyClusterSnapshots.html)  **
  - **Description:** Grants permission to modify settings for a list of snapshots
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelResize](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CancelResize.html)  **
  - **Description:** Grants permission to cancel a resize operation
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyClusterSnapshot](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CopyClusterSnapshot.html)  **
  - **Description:** Grants permission to copy a cluster snapshot
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAuthenticationProfile](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateAuthenticationProfile.html)  **
  - **Description:** Grants permission to create an Amazon Redshift authentication profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterParameterGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterParameterGroup.html)  **
  - **Description:** Grants permission to create an Amazon Redshift parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_redshift-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterSecurityGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSecurityGroup.html)  **
  - **Description:** Grants permission to create an Amazon Redshift security group
  - **Resource types (\*required):** [securitygroup\*](#list_redshift-resource-securitygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterSnapshot](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html)  **
  - **Description:** Grants permission to create a manual snapshot of the specified cluster
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterSubnetGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSubnetGroup.html)  **
  - **Description:** Grants permission to create an Amazon Redshift subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_redshift-resource-subnetgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterUser](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-role-permissions.html)  **
  - **Description:** Grants permission to automatically create the specified Amazon Redshift user if it does not exist
  - **Resource types (\*required):** [dbuser\*](#list_redshift-resource-dbuser)
  - **Condition keys:** [redshift:DbUser](#list_redshift-redshift_DbUser)
  - **Access level:** Permissions management, Write

- **   [CreateCustomDomainAssociation](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateCustomDomainAssociation.html)  **
  - **Description:** Grants permission to create a custom domain name for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEndpointAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateEndpointAccess.html)  **
  - **Description:** Grants permission to create a redshift-managed vpc endpoint
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEventSubscription](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateEventSubscription.html)  **
  - **Description:** Grants permission to create an Amazon Redshift event notification subscription
  - **Resource types (\*required):** [eventsubscription\*](#list_redshift-resource-eventsubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHsmClientCertificate](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateHsmClientCertificate.html)  **
  - **Description:** Grants permission to create an HSM client certificate that a cluster uses to connect to an HSM
  - **Resource types (\*required):** [hsmclientcertificate\*](#list_redshift-resource-hsmclientcertificate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHsmConfiguration](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateHsmConfiguration.html)  **
  - **Description:** Grants permission to create an HSM configuration that contains information required by a cluster to store and use database encryption keys in a hardware security module (HSM)
  - **Resource types (\*required):** [hsmconfiguration\*](#list_redshift-resource-hsmconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateIntegration.html)  **
  - **Description:** Grants permission to create an Amazon Redshift zero-ETL integration
  - **Resource types (\*required):** [integration\*](#list_redshift-resource-integration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)<br />[redshift:IntegrationSourceArn](#list_redshift-redshift_IntegrationSourceArn)<br />[redshift:IntegrationTargetArn](#list_redshift-redshift_IntegrationTargetArn)
  - **Access level:** Write

- **   [CreateRedshiftIdcApplication](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateRedshiftIdcApplication.html)  **
  - **Description:** Grants permission to create a redshift idc application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateScheduledAction](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateScheduledAction.html)  **
  - **Description:** Grants permission to create an Amazon Redshift scheduled action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSnapshotCopyGrant](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateSnapshotCopyGrant.html)  **
  - **Description:** Grants permission to create a snapshot copy grant and encrypt copied snapshots in a destination AWS Region
  - **Resource types (\*required):** [snapshotcopygrant\*](#list_redshift-resource-snapshotcopygrant)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [CreateSnapshotSchedule](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateSnapshotSchedule.html)  **
  - **Description:** Grants permission to create a snapshot schedule
  - **Resource types (\*required):** [snapshotschedule\*](#list_redshift-resource-snapshotschedule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTags](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateTags.html)  **
  - **Description:** Grants permission to add one or more tags to a specified resource
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [eventsubscription](#list_redshift-resource-eventsubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [hsmclientcertificate](#list_redshift-resource-hsmclientcertificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [hsmconfiguration](#list_redshift-resource-hsmconfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [integration](#list_redshift-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [parametergroup](#list_redshift-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [securitygroup](#list_redshift-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [securitygroupingress-cidr](#list_redshift-resource-securitygroupingress-cidr) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [securitygroupingress-ec2securitygroup](#list_redshift-resource-securitygroupingress-ec2securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_redshift-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshotcopygrant](#list_redshift-resource-snapshotcopygrant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshotschedule](#list_redshift-resource-snapshotschedule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [subnetgroup](#list_redshift-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [usagelimit](#list_redshift-resource-usagelimit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CreateUsageLimit](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateUsageLimit.html)  **
  - **Description:** Grants permission to create a usage limit
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [usagelimit\*](#list_redshift-resource-usagelimit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [DeauthorizeDataShare](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeauthorizeDataShare.html)  **
  - **Description:** Grants permission to remove permission from the specified datashare consumer to consume a datashare
  - **Resource types (\*required):** [datashare\*](#list_redshift-resource-datashare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[redshift:ConsumerIdentifier](#list_redshift-redshift_ConsumerIdentifier)
  - **Access level:** Permissions management, Write

- **   [DeleteAuthenticationProfile](API_DeleteAuthenticationProfile.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift authentication profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete a previously provisioned cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterParameterGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteClusterParameterGroup.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_redshift-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterSecurityGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteClusterSecurityGroup.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift security group
  - **Resource types (\*required):** [securitygroup\*](#list_redshift-resource-securitygroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterSnapshot](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteClusterSnapshot.html)  **
  - **Description:** Grants permission to delete a manual snapshot
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterSubnetGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteClusterSubnetGroup.html)  **
  - **Description:** Grants permission to delete a cluster subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_redshift-resource-subnetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomDomainAssociation](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteCustomDomainAssociation.html)  **
  - **Description:** Grants permission to delete a custom domain name for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpointAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteEndpointAccess.html)  **
  - **Description:** Grants permission to delete a redshift-managed vpc endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEventSubscription](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteEventSubscription.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift event notification subscription
  - **Resource types (\*required):** [eventsubscription\*](#list_redshift-resource-eventsubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHsmClientCertificate](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteHsmClientCertificate.html)  **
  - **Description:** Grants permission to delete an HSM client certificate
  - **Resource types (\*required):** [hsmclientcertificate\*](#list_redshift-resource-hsmclientcertificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHsmConfiguration](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteHsmConfiguration.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift HSM configuration
  - **Resource types (\*required):** [hsmconfiguration\*](#list_redshift-resource-hsmconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift zero-ETL integration
  - **Resource types (\*required):** [integration\*](#list_redshift-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePartner](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeletePartner.html)  **
  - **Description:** Grants permission to delete a partner integration from a cluster
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRedshiftIdcApplication](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteRedshiftIdcApplication.html)  **
  - **Description:** Grants permission to delete a redshift idc application
  - **Resource types (\*required):** [redshiftidcapplication\*](#list_redshift-resource-redshiftidcapplication)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the resource policy for a specified resource
  - **Resource types (\*required):** [namespace\*](#list_redshift-resource-namespace)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteScheduledAction](API_DeleteScheduledAction.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift scheduled action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSnapshotCopyGrant](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteSnapshotCopyGrant.html)  **
  - **Description:** Grants permission to delete a snapshot copy grant
  - **Resource types (\*required):** [snapshotcopygrant\*](#list_redshift-resource-snapshotcopygrant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshotSchedule](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteSnapshotSchedule.html)  **
  - **Description:** Grants permission to delete a snapshot schedule
  - **Resource types (\*required):** [snapshotschedule\*](#list_redshift-resource-snapshotschedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteTags.html)  **
  - **Description:** Grants permission to delete a tag or tags from a resource
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [eventsubscription](#list_redshift-resource-eventsubscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [hsmclientcertificate](#list_redshift-resource-hsmclientcertificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [hsmconfiguration](#list_redshift-resource-hsmconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [integration](#list_redshift-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [parametergroup](#list_redshift-resource-parametergroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [securitygroup](#list_redshift-resource-securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [securitygroupingress-cidr](#list_redshift-resource-securitygroupingress-cidr) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [securitygroupingress-ec2securitygroup](#list_redshift-resource-securitygroupingress-ec2securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshotcopygrant](#list_redshift-resource-snapshotcopygrant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshotschedule](#list_redshift-resource-snapshotschedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [subnetgroup](#list_redshift-resource-subnetgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [usagelimit](#list_redshift-resource-usagelimit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteUsageLimit](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteUsageLimit.html)  **
  - **Description:** Grants permission to delete a usage limit
  - **Resource types (\*required):** [usagelimit\*](#list_redshift-resource-usagelimit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterNamespace](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeregisterNamespace.html)  **
  - **Description:** Grants permission to deregister the specified namespace from a consumer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAccountAttributes](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeAccountAttributes.html)  **
  - **Description:** Grants permission to describe attributes attached to the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAuthenticationProfiles](API_DescribeAuthenticationProfiles.html)  **
  - **Description:** Grants permission to describe created Amazon Redshift authentication profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusterDbRevisions](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterDbRevisions.html)  **
  - **Description:** Grants permission to describe database revisions for a cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeClusterParameterGroups](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterParameterGroups.html)  **
  - **Description:** Grants permission to describe Amazon Redshift parameter groups, including parameter groups you created and the default parameter group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusterParameters](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterParameters.html)  **
  - **Description:** Grants permission to describe parameters contained within an Amazon Redshift parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_redshift-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterSecurityGroups](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterSecurityGroups.html)  **
  - **Description:** Grants permission to describe Amazon Redshift security groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusterSnapshots](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterSnapshots.html)  **
  - **Description:** Grants permission to describe one or more snapshot objects, which contain metadata about your cluster snapshots
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterSubnetGroups](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterSubnetGroups.html)  **
  - **Description:** Grants permission to describe one or more cluster subnet group objects, which contain metadata about your cluster subnet groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusterTracks](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterTracks.html)  **
  - **Description:** Grants permission to describe available maintenance tracks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeClusterVersions](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusterVersions.html)  **
  - **Description:** Grants permission to describe available Amazon Redshift cluster versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClusters](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusters.html)  **
  - **Description:** Grants permission to describe properties of provisioned clusters
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeCustomDomainAssociations](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeCustomDomainAssociations.html)  **
  - **Description:** Grants permission to describe custom domain names for a cluster
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDataShares](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeDataShares.html)  **
  - **Description:** Grants permission to describe datashares created and consumed by your clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataSharesForConsumer](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeDataSharesForConsumer.html)  **
  - **Description:** Grants permission to describe only datashares consumed by your clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataSharesForProducer](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeDataSharesForProducer.html)  **
  - **Description:** Grants permission to describe only datashares created by your clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDefaultClusterParameters](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeDefaultClusterParameters.html)  **
  - **Description:** Grants permission to describe parameter settings for a parameter group family
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpointAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeEndpointAccess.html)  **
  - **Description:** Grants permission to describe redshift-managed vpc endpoints
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpointAuthorization](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeEndpointAuthorization.html)  **
  - **Description:** Grants permission to authorize describe activity for redshift-managed vpc endpoint
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeEventCategories](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeEventCategories.html)  **
  - **Description:** Grants permission to describe event categories for all event source types, or for a specified source type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventSubscriptions](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeEventSubscriptions.html)  **
  - **Description:** Grants permission to describe Amazon Redshift event notification subscriptions for the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEvents](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permission to describe events related to clusters, security groups, snapshots, and parameter groups for the past 14 days
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeHsmClientCertificates](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeHsmClientCertificates.html)  **
  - **Description:** Grants permission to describe HSM client certificates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeHsmConfigurations](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeHsmConfigurations.html)  **
  - **Description:** Grants permission to describe Amazon Redshift HSM configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInboundIntegrations](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeInboundIntegrations.html)  **
  - **Description:** Grants permission to list the inbound integrations
  - **Resource types (\*required):** 
  - **Condition keys:** [redshift:InboundIntegrationArn](#list_redshift-redshift_InboundIntegrationArn)
  - **Access level:** List

- **   [DescribeIntegrations](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeIntegrations.html)  **
  - **Description:** Grants permission to describe an Amazon Redshift zero-ETL integration
  - **Resource types (\*required):** [integration\*](#list_redshift-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeLoggingStatus](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeLoggingStatus.html)  **
  - **Description:** Grants permission to describe whether information, such as queries and connection attempts, is being logged for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNodeConfigurationOptions](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeNodeConfigurationOptions.html)  **
  - **Description:** Grants permission to describe properties of possible node configurations such as node type, number of nodes, and disk usage for the specified action type
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeOrderableClusterOptions](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeOrderableClusterOptions.html)  **
  - **Description:** Grants permission to describe orderable cluster options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePartners](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribePartners.html)  **
  - **Description:** Grants permission to retrieve information about the partner integrations defined for a cluster
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRedshiftIdcApplications](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeRedshiftIdcApplications.html)  **
  - **Description:** Grants permission to describe redshift idc applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeReservedNodeExchangeStatus](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeReservedNodeExchangeStatus.html)  **
  - **Description:** Grants permission to describe exchange status details and associated metadata for a reserved-node exchange. Statuses include such values as in progress and requested
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReservedNodeOfferings](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeReservedNodeOfferings.html)  **
  - **Description:** Grants permission to describe available reserved node offerings by Amazon Redshift
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReservedNodes](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeReservedNodes.html)  **
  - **Description:** Grants permission to describe the reserved nodes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeResize](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeResize.html)  **
  - **Description:** Grants permission to describe the last resize operation for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeScheduledActions](API_DescribeScheduledActions.html)  **
  - **Description:** Grants permission to describe created Amazon Redshift scheduled actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSnapshotCopyGrants](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeSnapshotCopyGrants.html)  **
  - **Description:** Grants permission to describe snapshot copy grants owned by the specified AWS account in the destination AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSnapshotSchedules](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeSnapshotSchedules.html)  **
  - **Description:** Grants permission to describe snapshot schedules
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshotschedule\*](#list_redshift-resource-snapshotschedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStorage](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeStorage.html)  **
  - **Description:** Grants permission to describe account level backups storage size and provisional storage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTableRestoreStatus](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeTableRestoreStatus.html)  **
  - **Description:** Grants permission to describe status of one or more table restore requests made using the RestoreTableFromClusterSnapshot API action
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTags](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeTags.html)  **
  - **Description:** Grants permission to describe tags
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventsubscription](#list_redshift-resource-eventsubscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hsmclientcertificate](#list_redshift-resource-hsmclientcertificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hsmconfiguration](#list_redshift-resource-hsmconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration](#list_redshift-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [parametergroup](#list_redshift-resource-parametergroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securitygroup](#list_redshift-resource-securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securitygroupingress-cidr](#list_redshift-resource-securitygroupingress-cidr) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securitygroupingress-ec2securitygroup](#list_redshift-resource-securitygroupingress-ec2securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshotcopygrant](#list_redshift-resource-snapshotcopygrant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshotschedule](#list_redshift-resource-snapshotschedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subnetgroup](#list_redshift-resource-subnetgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [usagelimit](#list_redshift-resource-usagelimit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUsageLimits](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeUsageLimits.html)  **
  - **Description:** Grants permission to describe usage limits
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [usagelimit\*](#list_redshift-resource-usagelimit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableLogging](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DisableLogging.html)  **
  - **Description:** Grants permission to disable logging information, such as queries and connection attempts, for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableSnapshotCopy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DisableSnapshotCopy.html)  **
  - **Description:** Grants permission to disable the automatic copy of snapshots for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateDataShareConsumer](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DisassociateDataShareConsumer.html)  **
  - **Description:** Grants permission to disassociate a consumer from a datashare
  - **Resource types (\*required):** [datashare\*](#list_redshift-resource-datashare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[redshift:ConsumerArn](#list_redshift-redshift_ConsumerArn)
  - **Access level:** Write

- **   [EnableLogging](https://docs.aws.amazon.com/redshift/latest/APIReference/API_EnableLogging.html)  **
  - **Description:** Grants permission to enable logging information, such as queries and connection attempts, for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableSnapshotCopy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_EnableSnapshotCopy.html)  **
  - **Description:** Grants permission to enable the automatic copy of snapshots for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [FailoverPrimaryCompute](https://docs.aws.amazon.com/redshift/latest/APIReference/API_FailoverPrimaryCompute.html)  **
  - **Description:** Grants permission to failover the primary compute of an Multi-AZ cluster to another AZ
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetClusterCredentials](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html)  **
  - **Description:** Grants permission to get temporary credentials to access an Amazon Redshift database by the specified AWS account
  - **Resource types (\*required):** [dbname](#list_redshift-resource-dbname) / **Condition keys:** [redshift:DbName](#list_redshift-redshift_DbName)<br />[redshift:DbUser](#list_redshift-redshift_DbUser)<br />[redshift:DurationSeconds](#list_redshift-redshift_DurationSeconds)
  - **Resource types (\*required):** [dbuser\*](#list_redshift-resource-dbuser) / **Condition keys:** [redshift:DbName](#list_redshift-redshift_DbName)<br />[redshift:DbUser](#list_redshift-redshift_DbUser)<br />[redshift:DurationSeconds](#list_redshift-redshift_DurationSeconds)
  - **Access level:** Write

- **   [GetClusterCredentialsWithIAM](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentialsWithIAM.html)  **
  - **Description:** Grants permission to get enhanced temporary credentials to access an Amazon Redshift database by the specified AWS account
  - **Resource types (\*required):** [dbname](#list_redshift-resource-dbname)
  - **Condition keys:** [redshift:DbName](#list_redshift-redshift_DbName)<br />[redshift:DurationSeconds](#list_redshift-redshift_DurationSeconds)
  - **Access level:** Write

- **   [GetIdentityCenterAuthToken](https://docs.aws.amazon.com/redshift/latest/mgmt/identity-center-authentication.html)  **
  - **Description:** Grants permission to get an authorized token for Identity Center users to access Redshift clusters
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReservedNodeExchangeConfigurationOptions](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetReservedNodeExchangeConfigurationOptions.html)  **
  - **Description:** Grants permission to get the configuration options for the reserved-node exchange
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReservedNodeExchangeOfferings](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetReservedNodeExchangeOfferings.html)  **
  - **Description:** Grants permission to get an array of DC2 ReservedNodeOfferings that matches the payment type, term, and usage price of the given DC1 reserved node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the resource policy for a specified resource
  - **Resource types (\*required):** [namespace\*](#list_redshift-resource-namespace)
  - **Condition keys:**  
  - **Access level:** Read

- **   [JoinGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html)  **
  - **Description:** Grants permission to join the specified Amazon Redshift group
  - **Resource types (\*required):** [dbgroup\*](#list_redshift-resource-dbgroup)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ListRecommendations](API_ListRecommendations.html)  **
  - **Description:** Grants permission to list Advisor recommendations
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ModifyAquaConfiguration](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyAquaConfiguration.html)  **
  - **Description:** Grants permission to modify the AQUA configuration of a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyAuthenticationProfile](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyAuthenticationProfile.html)  **
  - **Description:** Grants permission to modify an existing Amazon Redshift authentication profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyCluster.html)  **
  - **Description:** Grants permission to modify the settings of a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClusterDbRevision](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterDbRevision.html)  **
  - **Description:** Grants permission to modify the database revision of a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClusterIamRoles](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterIamRoles.html)  **
  - **Description:** Grants permission to modify the list of AWS Identity and Access Management (IAM) roles that can be used by a cluster to access other AWS services
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ModifyClusterMaintenance](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterMaintenance.html)  **
  - **Description:** Grants permission to modify the maintenance settings of a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClusterParameterGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterParameterGroup.html)  **
  - **Description:** Grants permission to modify the parameters of a parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_redshift-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClusterSnapshot](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterSnapshot.html)  **
  - **Description:** Grants permission to modify the settings of a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClusterSnapshotSchedule](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterSnapshotSchedule.html)  **
  - **Description:** Grants permission to modify a snapshot schedule for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClusterSubnetGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyClusterSubnetGroup.html)  **
  - **Description:** Grants permission to modify a cluster subnet group to include the specified list of VPC subnets
  - **Resource types (\*required):** [subnetgroup\*](#list_redshift-resource-subnetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyCustomDomainAssociation](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyCustomDomainAssociation.html)  **
  - **Description:** Grants permission to modify a custom domain name for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyEndpointAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyEndpointAccess.html)  **
  - **Description:** Grants permission to modify a redshift-managed vpc endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyEventSubscription](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyEventSubscription.html)  **
  - **Description:** Grants permission to modify an existing Amazon Redshift event notification subscription
  - **Resource types (\*required):** [eventsubscription\*](#list_redshift-resource-eventsubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyIntegration](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyIntegration.html)  **
  - **Description:** Grants permission to modify an Amazon Redshift zero-ETL integration
  - **Resource types (\*required):** [integration\*](#list_redshift-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyRedshiftIdcApplication](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyRedshiftIdcApplication.html)  **
  - **Description:** Grants permission to modify a redshift idc application
  - **Resource types (\*required):** [redshiftidcapplication\*](#list_redshift-resource-redshiftidcapplication)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyScheduledAction](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyScheduledAction.html)  **
  - **Description:** Grants permission to modify an existing Amazon Redshift scheduled action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifySnapshotCopyRetentionPeriod](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifySnapshotCopyRetentionPeriod.html)  **
  - **Description:** Grants permission to modify the number of days to retain snapshots in the destination AWS Region after they are copied from the source AWS Region
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifySnapshotSchedule](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifySnapshotSchedule.html)  **
  - **Description:** Grants permission to modify a snapshot schedule
  - **Resource types (\*required):** [snapshotschedule\*](#list_redshift-resource-snapshotschedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyUsageLimit](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ModifyUsageLimit.html)  **
  - **Description:** Grants permission to modify a usage limit
  - **Resource types (\*required):** [usagelimit\*](#list_redshift-resource-usagelimit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PauseCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_PauseCluster.html)  **
  - **Description:** Grants permission to pause a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PurchaseReservedNodeOffering](https://docs.aws.amazon.com/redshift/latest/APIReference/API_PurchaseReservedNodeOffering.html)  **
  - **Description:** Grants permission to purchase a reserved node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to update the resource policy for a specified resource
  - **Resource types (\*required):** [namespace\*](#list_redshift-resource-namespace)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RebootCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RebootCluster.html)  **
  - **Description:** Grants permission to reboot a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterNamespace](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RegisterNamespace.html)  **
  - **Description:** Grants permission to register the specified namespace to a consumer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectDataShare](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RejectDataShare.html)  **
  - **Description:** Grants permission to decline a datashare shared from another account
  - **Resource types (\*required):** [datashare\*](#list_redshift-resource-datashare)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ResetClusterParameterGroup](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ResetClusterParameterGroup.html)  **
  - **Description:** Grants permission to set one or more parameters of a parameter group to their default values and set the source values of the parameters to "engine-default"
  - **Resource types (\*required):** [parametergroup\*](#list_redshift-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResizeCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ResizeCluster.html)  **
  - **Description:** Grants permission to change the size of a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreFromClusterSnapshot](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RestoreFromClusterSnapshot.html)  **
  - **Description:** Grants permission to create a cluster from a snapshot
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-aws_TagKeys)
  - **Access level:** Write

- **   [RestoreTableFromClusterSnapshot](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RestoreTableFromClusterSnapshot.html)  **
  - **Description:** Grants permission to create a table from a table in an Amazon Redshift cluster snapshot
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResumeCluster](https://docs.aws.amazon.com/redshift/latest/APIReference/API_ResumeCluster.html)  **
  - **Description:** Grants permission to resume a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeClusterSecurityGroupIngress](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RevokeClusterSecurityGroupIngress.html)  **
  - **Description:** Grants permission to revoke an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group
  - **Resource types (\*required):** [securitygroup\*](#list_redshift-resource-securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securitygroupingress-ec2securitygroup\*](#list_redshift-resource-securitygroupingress-ec2securitygroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeEndpointAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RevokeEndpointAccess.html)  **
  - **Description:** Grants permission to revoke access for endpoint related activities for redshift-managed vpc endpoint
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RevokeSnapshotAccess](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RevokeSnapshotAccess.html)  **
  - **Description:** Grants permission to revoke access from the specified AWS account to restore a snapshot
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RotateEncryptionKey](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RotateEncryptionKey.html)  **
  - **Description:** Grants permission to rotate an encryption key for a cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePartnerStatus](https://docs.aws.amazon.com/redshift/latest/APIReference/API_UpdatePartnerStatus.html)  **
  - **Description:** Grants permission to update the status of a partner integration
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Redshift
<a name="list_redshift-permission-only-actions"></a>

The following actions are defined by Amazon Redshift but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AuthorizeInboundIntegration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html)  **
  - **Description:** Grants permission to Amazon Redshift to continuously validate that the target namespace can receive data replicated from the source ARN
  - **Resource types (\*required):** [namespace\*](#list_redshift-resource-namespace)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to cancel a query through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelQuerySession](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to see queries in the Amazon Redshift console
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInboundIntegration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html)  **
  - **Description:** Grants permission to the source principal to create an integration into the namespace of target data warehouse
  - **Resource types (\*required):** [namespace\*](#list_redshift-resource-namespace)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateQev2IdcApplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)  **
  - **Description:** Grants permission to create a qev2 idc application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSavedQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to create saved SQL queries through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteQev2IdcApplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)  **
  - **Description:** Grants permission to delete a qev2 idc application
  - **Resource types (\*required):** [qev2idcapplication\*](#list_redshift-resource-qev2idcapplication)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSavedQueries](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to delete saved SQL queries through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAutonomicsDenylist](https://docs.aws.amazon.com/redshift/latest/dg/t_Manage_workload_exclusion.html)  **
  - **Description:** Grants permission to describe the list of resources that are denylisted from global autonomics decisions for a specified cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeQev2IdcApplications](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)  **
  - **Description:** Grants permission to describe qev2 idc applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to describe a query through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSavedQueries](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to describe saved queries through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTable](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to describe a table through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ExecuteQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to execute a query through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [FetchResults](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to fetch query results through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDatabases](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list databases through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSavedQueries](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list saved queries through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchemas](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list schemas through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTables](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to list tables through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ModifyAutonomicsDenylist](https://docs.aws.amazon.com/redshift/latest/dg/t_Manage_workload_exclusion.html)  **
  - **Description:** Grants permission to add or remove resources from the global autonomics denylist for a specified cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyQev2IdcApplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)  **
  - **Description:** Grants permission to modify a qev2 idc application
  - **Resource types (\*required):** [qev2idcapplication\*](#list_redshift-resource-qev2idcapplication)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifySavedQuery](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to modify an existing saved query through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ViewQueriesFromConsole](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to view query results through the Amazon Redshift console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ViewQueriesInConsole](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  **
  - **Description:** Grants permission to terminate running queries and loads through the Amazon Redshift console
  - **Resource types (\*required):** [cluster](#list_redshift-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_)
  - **Access level:** List



## Resource types defined by Amazon Redshift
<a name="list_redshift-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)  | arn:${Partition}:redshift:${Region}:${Account}:cluster:${ClusterName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [datashare](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html)  | arn:${Partition}:redshift:${Region}:${Account}:datashare:${ProducerClusterNamespace}/${DataShareName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [dbgroup](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_GROUP.html)  | arn:${Partition}:redshift:${Region}:${Account}:dbgroup:${ClusterName}/${DbGroup} |   | 
|  [dbname](https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html)  | arn:${Partition}:redshift:${Region}:${Account}:dbname:${ClusterName}/${DbName} |   | 
|  [dbuser](https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html)  | arn:${Partition}:redshift:${Region}:${Account}:dbuser:${ClusterName}/${DbUser} |   | 
|  [eventsubscription](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-events.html)  | arn:${Partition}:redshift:${Region}:${Account}:eventsubscription:${EventSubscriptionName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [hsmclientcertificate](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM)  | arn:${Partition}:redshift:${Region}:${Account}:hsmclientcertificate:${HSMClientCertificateId} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [hsmconfiguration](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM)  | arn:${Partition}:redshift:${Region}:${Account}:hsmconfiguration:${HSMConfigurationId} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [integration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html)  | arn:${Partition}:redshift:${Region}:${Account}:integration:${IntegrationIdentifier} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [namespace](https://docs.aws.amazon.com/redshift/latest/dg/concepts.html)  | arn:${Partition}:redshift:${Region}:${Account}:namespace:${ClusterNamespace} |   | 
|  [parametergroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html)  | arn:${Partition}:redshift:${Region}:${Account}:parametergroup:${ParameterGroupName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [qev2idcapplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)  | arn:${Partition}:redshift:${Region}:${Account}:qev2idcapplication:${Qev2IdcApplicationId} |   | 
|  [redshiftidcapplication](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html)  | arn:${Partition}:redshift:${Region}:${Account}:redshiftidcapplication:${RedshiftIdcApplicationId} |   | 
|  [securitygroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html)  | arn:${Partition}:redshift:${Region}:${Account}:securitygroup:${SecurityGroupName}/ec2securitygroup/${Owner}/${Ec2SecurityGroupId} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [securitygroupingress-cidr](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html)  | arn:${Partition}:redshift:${Region}:${Account}:securitygroupingress:${SecurityGroupName}/cidrip/${IpRange} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [securitygroupingress-ec2securitygroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html)  | arn:${Partition}:redshift:${Region}:${Account}:securitygroupingress:${SecurityGroupName}/ec2securitygroup/${Owner}/${Ece2SecuritygroupId} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)  | arn:${Partition}:redshift:${Region}:${Account}:snapshot:${ClusterName}/${SnapshotName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [snapshotcopygrant](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#configure-snapshot-copy-grant)  | arn:${Partition}:redshift:${Region}:${Account}:snapshotcopygrant:${SnapshotCopyGrantName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [snapshotschedule](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)  | arn:${Partition}:redshift:${Region}:${Account}:snapshotschedule:${ScheduleIdentifier} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [subnetgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html)  | arn:${Partition}:redshift:${Region}:${Account}:subnetgroup:${SubnetGroupName} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 
|  [usagelimit](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-usage-limits.html)  | arn:${Partition}:redshift:${Region}:${Account}:usagelimit:${UsageLimitId} | [aws:ResourceTag/${TagKey}](#list_redshift-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Redshift
<a name="list_redshift-policy-keys"></a>

Amazon Redshift defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by actions based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by actions based on tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by actions based on the presence of mandatory tags in the request | ArrayOfString | 
|   [redshift:AllowWrites](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the allowWrites input parameter | Bool | 
|   [redshift:ConsumerArn](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the datashare consumer arn | ARN | 
|   [redshift:ConsumerIdentifier](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the datashare consumer | String | 
|   [redshift:DbName](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the database name | String | 
|   [redshift:DbUser](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the database user name | String | 
|   [redshift:DurationSeconds](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the number of seconds until a temporary credential set expires | String | 
|   [redshift:InboundIntegrationArn](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the ARN of an inbound zero-ETL Integration resource | ARN | 
|   [redshift:IntegrationSourceArn](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the ARN of a zero-ETL Integration source | ARN | 
|   [redshift:IntegrationTargetArn](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by the ARN of a zero-ETL Integration target | ARN | 