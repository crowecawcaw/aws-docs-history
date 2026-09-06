

# Error codes for the Amazon EC2 API
<a name="errors-overview"></a>

Amazon EC2 has two types of error codes:
+ **Client errors**. These errors are usually caused by something the client did. Common causes include specifying an incorrect or invalid parameter in the request, or using an action or resource on behalf of a user that doesn't have permission to use the action or resource. These errors are accompanied by a 400-series HTTP response code.
+ **Server errors**. These errors are usually caused by an AWS server-side issue. These errors are accompanied by a 500-series HTTP response code.

**Topics**
+ [Common client error codes](#CommonErrors)
+ [Client error codes for specific actions](#api-error-codes-table-client)
+ [Server error codes](#api-error-codes-table-server)
+ [Example error response](#api-error-response)
+ [Eventual consistency](#api-eventual-consistency)

## Common client error codes
<a name="CommonErrors"></a>

This section lists the client error codes that all Amazon EC2 API actions can return.


| Error code | Description | 
| --- | --- | 
| AuthFailure | The provided credentials could not be validated. You might not be authorized to carry out the request; for example, trying to associate an Elastic IP address that is not yours, or trying to use an AMI for which you do not have permissions. Ensure that your account is authorized to use Amazon EC2, that your credit card details are correct, and that you are using the correct credentials. | 
| Blocked | Your account is currently blocked. Contact [Support](https://aws.amazon.com/contact-us/) if you have questions. | 
| DryRunOperation | The user has the required permissions, so the request would have succeeded, but the DryRun parameter was used. | 
| IdempotentParameterMismatch | The request uses the same client token as a previous, but non-identical request. Do not reuse a client token with different requests, unless the requests are identical. | 
| IncompleteSignature | The request signature does not conform to AWS standards. | 
| InvalidAction | The action or operation requested is not valid. Verify that the action is typed correctly. | 
| InvalidCharacter | A specified character is invalid. | 
| InvalidClientTokenId | The X.509 certificate or credentials provided do not exist in our records. | 
| InvalidPaginationToken | The specified pagination token is not valid or is expired. | 
| InvalidParameter | A parameter specified in a request is not valid, is unsupported, or cannot be used. The returned message provides an explanation of the error value. For example, if you are launching an instance, you can't specify a security group and subnet that are in different VPCs. | 
| InvalidParameterCombination | Indicates an incorrect combination of parameters, or a missing parameter. For example, trying to terminate an instance without specifying the instance ID. | 
| InvalidParameterDependency | Indicates an incorrect combination of parameters, or a missing parameter. For example, trying to terminate an instance without specifying the instance ID. | 
| InvalidParameterValue | A value specified in a parameter is not valid, is unsupported, or cannot be used. Ensure that you specify a resource by using its full ID. The returned message provides an explanation of the error value. | 
| InvalidQueryParameter | The AWS query string is malformed or does not adhere to AWS standards. | 
| MalformedQueryString | The query string contains a syntax error. | 
| MissingAction | The request is missing an action or a required parameter. | 
| MissingAuthenticationToken | The request must contain valid credentials. | 
| MissingParameter | The request is missing a required parameter. Ensure that you have supplied all the required parameters for the request; for example, the resource ID. | 
| OptInRequired | You are not authorized to use the requested service. Ensure that you have subscribed to the service you are trying to use. If you are new to AWS, your account might take some time to be activated while your credit card details are being verified. | 
| PendingVerification | Your account is pending verification. Until the verification process is complete, you may not be able to carry out requests with this account. If you have questions, contact [Support](https://aws.amazon.com/contact-us/).  | 
| RequestExpired | The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for presigned URLs), or the date stamp on the request is more than 15 minutes in the future. If you're using temporary security credentials, this error can also occur if the credentials have expired. For more information, see [Temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the IAM User Guide. | 
| TagPolicyViolation | You attempted to create or update a resource with tags that are not compliant with the tag policy requirements for this account. For more information, see [Grant permission to tag resources during creation.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.html)  | 
| UnauthorizedOperation | You are not authorized to perform this operation. Check your IAM policies, and ensure that you are using the correct credentials. For more information, see [Identity and access management for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html). If the returned message is encoded, you can decode it using the DecodeAuthorizationMessage action. For more information, see [DecodeAuthorizationMessage](https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html) in the AWS Security Token Service API Reference. | 
| UnknownParameter | An unknown or unrecognized parameter was supplied. Requests that could cause this error include supplying a misspelled parameter or a parameter that is not supported for the specified API version. | 
| UnsupportedInstanceAttribute | The specified attribute cannot be modified. | 
| <a name="UnsupportedOperation"></a> UnsupportedOperation  | The specified request includes an unsupported operation. For example, you can't stop an instance that's instance store-backed. Or you might be trying to launch an instance type that is not supported by the specified AMI. The returned message provides details of the unsupported operation. | 
| UnsupportedProtocol | SOAP has been deprecated and is no longer supported. | 
| ValidationError | The input fails to satisfy the constraints specified by an AWS service. | 

## Client error codes for specific actions
<a name="api-error-codes-table-client"></a>

This section lists client errors that are specific to certain Amazon EC2 API actions. 


| Error code | Description | 
| --- | --- | 
| <a name="AccountDisabled"></a>AccountDisabled  | The functionality you have requested has been administratively disabled for this account. | 
| <a name="ActiveVpcPeeringConnectionPerVpcLimitExceeded"></a>ActiveVpcPeeringConnectionPerVpcLimitExceeded | You've reached the limit on the number of active VPC peering connections you can have for the specified VPC. | 
| <a name="AddressLimitExceeded"></a>AddressLimitExceeded  | You've reached the limit on the number of Elastic IP addresses that you can allocate. For more information, see [Elastic IP address limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-limit). | 
| <a name="AsnConflict"></a>AsnConflict | The Autonomous System Numbers (ASNs) of the specified customer gateway and the specified virtual private gateway are the same. | 
| <a name="AttachmentLimitExceeded"></a>AttachmentLimitExceeded  | You've reached the limit on the number of Amazon EBS volumes or network interfaces that can be attached to a single instance.<br />The number of Amazon EBS volumes that you can attach to an instance depends on the instance type. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html) in the *Amazon EC2 User Guide*. | 
| BootForVolumeTypeUnsupported | The specified volume type cannot be used as a boot volume. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html). | 
| <a name="BundlingInProgress"></a>BundlingInProgress  | The specified instance already has a bundling task in progress.  | 
| <a name="CannotDelete"></a>CannotDelete | You cannot delete the 'default' security group in your VPC, but you can change its rules. For more information, see [Amazon EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html). | 
| <a name="CapacityBlockDescribeLimitExceeded"></a>CapacityBlockDescribeLimitExceeded | You've reached the limit for this account. The returned message provides details. | 
| <a name="ClientInvalidParameterValue"></a>ClientInvalidParameterValue | A parameter specified in a request is not valid, is unsupported, or cannot be used. The returned message provides an explanation of the error value. For example, if you are launching an instance, you can't specify a security group and subnet that are in different VPCs. | 
| <a name="RuleLimit"></a>ClientVpnAuthorizationRuleLimitExceeded | You've reached the limit on the number of authorization rules that can be added to a single Client VPN endpoint. | 
| <a name="CrlLimit"></a>ClientVpnCertificateRevocationListLimitExceeded | You've reached the limit on the number of client certificate revocation lists that can be added to a single Client VPN endpoint. | 
| <a name="AlreadyAssociated"></a>ClientVpnEndpointAssociationExists | The specified target network is already associated with the Client VPN endpoint. | 
| <a name="EndpointLimit"></a>ClientVpnEndpointLimitExceeded | You've reached the limit on the number of Client VPN endpoints that you can create. | 
| <a name="RouteLimit"></a>ClientVpnRouteLimitExceeded | You've reached the limit on the number of routes that can be added to a single Client VPN endpoint. | 
| <a name="TerminateLimit"></a>ClientVpnTerminateConnectionsLimitExceeded | The number of client connections you're attempting to terminate exceeds the limit. | 
| ConcurrentCreateImageNoRebootLimitExceeded  | The maximum number of concurrent CreateImage requests for the instance has been reached. Wait for the current CreateImage requests to complete, and then retry your request. | 
| <a name="ConcurrentSnapshotLimitExceeded"></a>ConcurrentSnapshotLimitExceeded | You've reached the limit on the number of concurrent snapshots you can create on the specified volume. Wait until the 'pending' requests have completed, and check that you do not have snapshots that are in an incomplete state, such as 'error', which count against your concurrent snapshot limit. | 
| <a name="ConcurrentTagAccess"></a>ConcurrentTagAccess | You can't run simultaneous commands to modify a tag for a specific resource. Allow sufficient wait time for the previous request to complete, then retry your request. | 
| CreditSpecificationUpdateInProgress | The default credit specification for the instance family is currently being updated. It takes about five minutes to complete. For more information, see [Set the default credit specification for the account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-how-to.html#burstable-performance-instance-set-default-credit-specification-for-account). | 
| <a name="CustomerGatewayLimitExceeded"></a>CustomerGatewayLimitExceeded  | You've reached the limit on the number of customer gateways you can create for the AWS Region. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| CustomerKeyHasBeenRevoked | The KMS key cannot be accessed. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html). | 
| DeclarativePoliciesAccessDeniedException | You do not have sufficient access to perform this action, or the specified TargetId does not exist, or the specified TargetId is not in your organization. To generate an account status report for declarative policies, the caller must be the management account or a delegated administrator for the organization and the specified TargetId must belong to your organization. | 
| DeclarativePoliciesNotEnabledException | Trusted access is not enabled. Trusted access must be enabled for the service for which the declarative policy will enforce a baseline configuration. The API uses the following service principal to identify the EC2 service: ec2.amazonaws.com. For more information on how to enable trusted access with the AWS CLI and AWS SDKs, see [Using Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html). | 
| DeleteConversionTaskError | The conversion task cannot be canceled.  | 
| DefaultSubnetAlreadyExistsInAvailabilityZone | A default subnet already exists in the specified Availability Zone. You can have only one default subnet per Availability Zone. | 
| <a name="DefaultVpcAlreadyExists"></a>DefaultVpcAlreadyExists | A default VPC already exists in the AWS Region. You can only have one default VPC per Region. | 
| DefaultVpcDoesNotExist | There is no default VPC in which to carry out the request. If you've deleted your default VPC, you can create a new one. For more information, see [Create a default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html#create-default-vpc). | 
| <a name="DependencyViolation"></a> DependencyViolation  | The specified object has dependent resources. A number of resources in a VPC may have dependent resources, which prevent you from deleting or detaching them. Remove the dependencies first, then retry your request. For example, this error occurs if you try to delete a security group in a VPC that is in use by another security group. | 
| <a name="DiskImageSizeTooLarge"></a> DiskImageSizeTooLarge  | The disk image exceeds the allowed limit (for instance or volume import). | 
| DuplicateSubnetsInSameZone | For an interface VPC endpoint, you can specify only one subnet per Availability Zone. | 
| <a name="EncryptedVolumesNotSupported"></a> EncryptedVolumesNotSupported  | Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html). | 
| ExistingVpcEndpointConnections | You cannot delete a VPC endpoint service configuration or change the load balancers for the endpoint service if there are endpoints attached to the service. | 
| FleetNotInModifiableState | The Spot Fleet request must be in the active state to modify it. For more information, see [Spot Fleet request types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-requests.html). | 
| <a name="FlowLogAlreadyExists"></a> FlowLogAlreadyExists  | A flow log with the specified configuration already exists. | 
| <a name="FlowLogsLimitExceeded"></a> FlowLogsLimitExceeded  | You've reached the limit on the number of flow logs you can create. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="FilterLimitExceeded"></a> FilterLimitExceeded  | The request uses too many filters or too many filter values. | 
| <a name="Gateway.NotAttached"></a> Gateway.NotAttached  | An internet gateway is not attached to a VPC. If you are trying to detach an internet gateway, ensure that you specify the correct VPC. If you are trying to associate an Elastic IP address with a network interface or an instance, ensure that an internet gateway is attached to the relevant VPC. | 
| HostAlreadyCoveredByReservation | The specified Dedicated Host is already covered by a reservation. | 
| HostLimitExceeded | You've reached the limit on the number of Dedicated Hosts that you can allocate. For more information, see [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html). | 
| IdempotentInstanceTerminated | The request to launch an instance uses the same client token as a previous request for which the instance has been terminated. | 
| InaccessibleStorageLocation | The specified Amazon S3 URL cannot be accessed. Check the access permissions for the URL. | 
| InaccessibleStorageLocationException | The specified Amazon S3 bucket can't be accessed. An S3 bucket must be available before generating an account status report for declarative policies (you can create a new one or use an existing one), you must own the bucket, it must be in the same Region in which the request was made, and it must have an appropriate bucket policy. For a sample S3 policy, see [ Sample Amazon S3 policy](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.html#API_StartDeclarativePoliciesReport_Examples). | 
| <a name="IncorrectInstanceState"></a> IncorrectInstanceState  | The instance is in an incorrect state for the requested action. For example, some instance attributes, such as user data, can only be modified if the instance is in a 'stopped' state. If you are associating an Elastic IP address with a network interface, ensure that the instance that the interface is attached to is not in the 'pending' state. | 
| IncorrectModificationState | A new modification action on an EBS Elastic Volume cannot occur because the volume is currently being modified. | 
| <a name="IncorrectSpotRequestState"></a> IncorrectSpotRequestState  | The Spot Instance request is in an incorrect state for the request. Spot request status information can help you track your Amazon EC2 Spot Instance requests. For more information, see [Spot request status](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html). | 
| <a name="IncorrectState"></a> IncorrectState  | The resource is in an incorrect state for the request. This error can occur if you are trying to attach a volume that is still being created or detach a volume that is not in the 'available' state. Verify that the volume is in the 'available' state. If you are creating a snapshot, ensure that the previous request to create a snapshot on the same volume has completed. If you are deleting a virtual private gateway, ensure that it's detached from the VPC. | 
| IncorrectStateException | The resource is in an incorrect state for the request. This error can occur if you're trying to cancel the generation of an account status report for declarative policies that already has the `complete`, `cancelled`, or `error` status. Cancelation is only possible for reports with a `running` status. This error can also occur when you're trying to get a summary for a report that has not yet reached the `completed` status. This error can also occur if you start report generation while another report is being generated. Only one report per organization can be generated at a time. For more information, see [Generating the account status report for declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_status-report.html). | 
| IncompatibleHostRequirements | There are no available or compatible Dedicated Hosts available on which to launch or start the instance. | 
| InstanceCreditSpecification.NotSupported | The specified instance does not use CPU credits for CPU usage; only T2 instances use CPU credits for CPU usage. | 
| <a name="InstanceEventStartTimeCannotChange"></a> InstanceEventStartTimeCannotChange  | The specified scheduled event start time does not meet the requirements for rescheduling a scheduled event. For more information, see [Limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html). | 
| <a name="InstanceLimitExceeded"></a>InstanceLimitExceeded  | You've reached the limit on the number of instances you can run concurrently. This error can occur if you are launching an instance or if you are creating a Capacity Reservation. Capacity Reservations count towards your On-Demand Instance limits. If your request fails due to limit constraints, increase your On-Demand Instance limit for the required instance type and try again. For more information, see [EC2 On-Demand instance limits](https://aws.amazon.com/ec2/faqs/#EC2_On-Demand_Instance_limits). | 
| InsufficientCapacityOnHost | There is not enough capacity on the Dedicated Host to launch or start the instance. | 
| <a name="InstanceTpmEkPubNotFound"></a> InstanceTpmEkPubNotFound  | The public Trusted Platform Module (TPM) Endorsement Key (EK) cannot be found. | 
| <a name="InsufficientFreeAddressesInSubnet"></a>InsufficientFreeAddressesInSubnet | The specified subnet does not contain enough free private IP addresses to fulfill your request. Use the [DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html) request to view how many IP addresses are available (unused) in your subnet. IP addresses associated with stopped instances are considered unavailable. | 
| <a name="InsufficientReservedInstancesCapacity"></a>InsufficientReservedInstancesCapacity | There is insufficient capacity for the requested Reserved Instances.  | 
| InterfaceInUseByTrafficMirrorSession | The Traffic Mirror source that you are trying to create uses an interface that is already associated with a session. An interface can only be associated with a session, or with a target, but not both. | 
| InterfaceInUseByTrafficMirrorTarget | The Traffic Mirror source that you are trying to create uses an interface that is already associated with a target. An interface can only be associated with a session, or with a target, but not both. If the interface is associated with a target, it cannot be associated with another target. | 
| <a name="InternetGatewayLimitExceeded"></a>InternetGatewayLimitExceeded  | You've reached the limit on the number of internet gateways that you can create. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="InvalidAddress.Locked"></a>InvalidAddress.Locked | The specified Elastic IP address cannot be released from your account. A reverse DNS record may be associated with the Elastic IP address. To unlock the address, contact [Support](https://aws.amazon.com/contact-us/). | 
| <a name="InvalidAddress.Malformed"></a>InvalidAddress.Malformed | The specified IP address is not valid. Ensure that you provide the address in the form xx.xx.xx.xx; for example, 55.123.45.67 | 
| <a name="InvalidAddress.NotFound"></a>InvalidAddress.NotFound | The specified Elastic IP address that you are describing cannot be found. Ensure that you specify the AWS Region in which the IP address is located, if it's not in the default Region. | 
| <a name="InvalidAddressID.NotFound"></a>InvalidAddressID.NotFound | The specified allocation ID for the Elastic IP address you are trying to release cannot be found. Ensure that you specify the AWS Region in which the IP address is located, if it's not in the default Region. | 
| InvalidAffinity | The specified affinity value is not valid. | 
| <a name="InvalidAllocationID.NotFound"></a>InvalidAllocationID.NotFound | The specified allocation ID you are trying to describe or associate does not exist. Ensure that you specify the AWS Region in which the IP address is located, if it's not in the default Region. | 
| <a name="InvalidAMIAttributeItemValue"></a>InvalidAMIAttributeItemValue  | The value of an item added to, or removed from, an image attribute is not valid. If you are specifying a userId, check that it is in the form of an AWS account ID, without hyphens. | 
| <a name="InvalidAMIID.Malformed"></a>InvalidAMIID.Malformed  | The specified AMI ID is malformed. Ensure that you provide the full AMI ID, in the form ami-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidAMIID.NotFound"></a>InvalidAMIID.NotFound  | The specified AMI doesn't exist. Check the AMI ID, and ensure that you specify the AWS Region in which the AMI is located, if it's not in the default Region. This error might also occur if you specified an incorrect kernel ID when launching an instance. This error might also occur if the AMI doesn't meet your Allowed AMIs criteria. To use this AMI, you must change the Allowed AMIs criteria. For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html). | 
| <a name="InvalidAMIID.Unavailable"></a>InvalidAMIID.Unavailable  | The specified AMI has been deregistered and is no longer available, or is not in a state from which you can launch an instance or modify attributes. | 
| <a name="InvalidAMIName.Duplicate"></a>InvalidAMIName.Duplicate | The specified AMI name is already in use by another AMI. If you have recently deregistered an AMI with the same name, allow enough time for the change to propagate through the system, and retry your request. | 
| <a name="InvalidAMIName.Malformed"></a>InvalidAMIName.Malformed | AMI names must be between 3 and 128 characters long, and may only contain letters, numbers, and the following special characters: '-', '\_', '.', '/', '(', and ')'. | 
| <a name="InvalidAssociationID.NotFound"></a>InvalidAssociationID.NotFound | The specified association ID (for an Elastic IP address, a route table, or network ACL) does not exist. Ensure that you specify the AWS Region in which the association ID is located, if it's not in the default Region. | 
| <a name="InvalidAttachment.NotFound"></a>InvalidAttachment.NotFound  | Indicates an attempt to detach a volume from an instance to which it is not attached. | 
| <a name="InvalidAttachmentID.NotFound"></a>InvalidAttachmentID.NotFound | The specified network interface attachment does not exist. | 
| InvalidAutoPlacement | The specified value for auto-placement is not valid. | 
| InvalidAvailabilityZone | The specified Availability Zone is not valid. | 
| <a name="InvalidBlockDeviceMapping"></a>InvalidBlockDeviceMapping | A block device mapping parameter is not valid. The returned message indicates the incorrect value. | 
| <a name="InvalidBundleID.NotFound"></a>InvalidBundleID.NotFound | The specified bundle task ID cannot be found. Ensure that you specify the AWS Region in which the bundle task is located, if it's not in the default Region. | 
| <a name="InvalidCapacityBlockOfferingIdExpired"></a>InvalidCapacityBlockOfferingIdExpired | The Capacity Block offering ID is no longer available. | 
| <a name="InvalidCapacityBlockOfferingIdMalformed"></a>InvalidCapacityBlockOfferingIdMalformed | The Capacity Block offering ID is malformed. | 
| <a name="InvalidCapacityBlockOfferingIdNotFound"></a>InvalidCapacityBlockOfferingIdNotFound | The Capacity Block offering ID cannot be found for this account. | 
| <a name="InvalidCapacityReservationState.PendingActivation"></a>InvalidCapacityReservationState.PendingActivation | Your Capacity Block is not active yet. | 
| <a name="InvalidCarrierGatewayID.NotFound"></a>InvalidCarrierGatewayID.NotFound | The specified carrier gateway ID cannot be found. Ensure that you specify the AWS Region in which the carrier gateway is located, if it's not in the default Region. | 
| <a name="InvalidCidr.InUse"></a>InvalidCidr.InUse | The specified inside tunnel CIDR is already in use by another VPN tunnel for the virtual private gateway. | 
| <a name="InvalidClientToken"></a>InvalidClientToken | The specified client token is not valid. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html). | 
| <a name="EndpointState"></a>InvalidClientVpnActiveAssociationNotFound | You cannot perform this action on the Client VPN endpoint while it is in the pending-association state. | 
| <a name="AssociationNotFound"></a>InvalidClientVpnAssociationIdNotFound | The specified target network association cannot be found. | 
| <a name="EndpointNotFound"></a>InvalidClientVpnConnection.IdNotFound | The specified Client VPN endpoint cannot be found. | 
| <a name="UserNotFound"></a>InvalidClientVpnConnection.UserNotFound | The specified user does not have an active connection to the specified Client VPN endpoint. | 
| <a name="TargetNetworkDuplicate"></a>InvalidClientVpnDuplicateAssociationException | The specified target network has already been associated with the Client VPN endpoint. | 
| <a name="AuthRuleDuplicate"></a>InvalidClientVpnDuplicateAuthorizationRule | The specified authorization has already been added to the Client VPN endpoint. | 
| <a name="RouteRuleDuplicate"></a>InvalidClientVpnDuplicateRoute | The specified route has already been added to the Client VPN endpoint. | 
| <a name="RuleNotFound"></a>InvalidClientVpnEndpointAuthorizationRuleNotFound | The specified authorization rule cannot be found. | 
| <a name="EndpointNotFound"></a>InvalidClientVpnEndpointId.NotFound | The specified Client VPN Endpoint cannot be found. | 
| <a name="RouteNotFound"></a>InvalidClientVpnRouteNotFound | The specified route cannot be found. | 
| <a name="SubnetAccount"></a>InvalidClientVpnSubnetId.DifferentAccount | The specified subnet belongs to a different account. | 
| <a name="SubnetAZ"></a>InvalidClientVpnSubnetId.DuplicateAz | You have already associated a subnet from this Availability Zone with the Client VPN endpoint. | 
| <a name="SubnetNotInVPC"></a>InvalidClientVpnSubnetId.NotFound | The specified subnet cannot be found in the VPN with which the Client VPN endpoint is associated. | 
| <a name="OverlappingCIDR"></a>InvalidClientVpnSubnetId.OverlappingCidr | The specified target network's CIDR range overlaps with the Client VPN endpoint's client CIDR range. | 
| <a name="InvalidConversionTaskId"></a>InvalidConversionTaskId  | The specified conversion task ID (for instance or volume import) is not valid. | 
| <a name="InvalidConversionTaskId.Malformed"></a>InvalidConversionTaskId.Malformed | The specified conversion task ID (for instance or volume import) is malformed. Ensure that you've specified the ID in the form import-i-xxxxxxxx. | 
| <a name="InvalidCpuCredits"></a>InvalidCpuCredits | The specified CpuCredit value is invalid. Valid values are standard and unlimited. | 
| <a name="InvalidCpuCredits.Malformed"></a>InvalidCpuCredits.Malformed | The specified CpuCredit value is invalid. Valid values are standard and unlimited. | 
| <a name="InvalidCustomerGateway.DuplicateIpAddress"></a>InvalidCustomerGateway.DuplicateIpAddress  | There is a conflict among the specified gateway IP addresses. Each VPN connection in an AWS Region must be created with a unique customer gateway IP address (across all AWS accounts). For more information, see [Your customer gateway device](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html#Summary) in the AWS Site-to-Site VPN User Guide. | 
| <a name="InvalidCustomerGatewayId.Malformed"></a>InvalidCustomerGatewayId.Malformed | The specified customer gateway ID is malformed, or cannot be found. Specify the ID in the form cgw-xxxxxxxx, and ensure that you specify the AWS Region in which the customer gateway is located, if it's not in the default Region. | 
| <a name="InvalidCustomerGatewayID.NotFound"></a> InvalidCustomerGatewayID.NotFound  | The specified customer gateway ID cannot be found. Ensure that you specify the AWS Region in which the customer gateway is located, if it's not in the default Region. | 
| InvalidCustomerGatewayState | The customer gateway is not in the available state, and therefore cannot be used. | 
| <a name="InvalidParameterValue"></a> InvalidParameterValue  | The device to which you are trying to attach (for example, /dev/sdh) is already in use on the instance.  | 
| InvalidDeclarativePoliciesReportId.Malformed | The specified account status report ID for declarative policies is malformed. Ensure that you specify the ID in the form p-xxxxxxxxxx. For more information, see [Generating the account status report for declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_status-report.html). | 
| <a name="InvalidDhcpOptionID.NotFound"></a> InvalidDhcpOptionID.NotFound  | The specified DHCP options set does not exist. Ensure that you specify the AWS Region in which the DHCP options set is located, if it's not in the default Region. | 
| <a name="InvalidDhcpOptionsID.NotFound"></a> InvalidDhcpOptionsID.NotFound  | The specified DHCP options set does not exist. Ensure that you specify the AWS Region in which the DHCP options set is located, if it's not in the default Region. | 
| <a name="InvalidDhcpOptionsId.Malformed"></a> InvalidDhcpOptionsId.Malformed | The specified DHCP options set ID is malformed. Ensure that you provide the full DHCP options set ID in the request, in the form dopt-xxxxxxxx. | 
| InvalidEgressOnlyInternetGatewayId.Malformed | The specified egress-only internet gateway ID is malformed. Ensure that you specify the ID in the form eigw-xxxxxxxxxxxxxxxxx. | 
| InvalidEgressOnlyInternetGatewayId.NotFound | The specified egress-only internet gateway does not exist. | 
| InvalidElasticGpuID.Malformed | The specified Elastic GPU ID is malformed. Ensure that you specify the ID in the form egpu-xxxxxxxxxxxxxxxxx. | 
| InvalidElasticGpuID.NotFound | The specified Elastic GPU does not exist. | 
| <a name="InvalidExportTaskID.Malformed"></a>InvalidExportTaskID.Malformed | The specified export task ID cannot be found. | 
| <a name="InvalidExportTaskID.NotFound"></a>InvalidExportTaskID.NotFound | The specified export task ID is malformed. Ensure that you specify the ID in the form export-ami-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidFilter"></a> InvalidFilter  | The specified filter is not valid. | 
| <a name="InvalidFlowLogId.NotFound"></a> InvalidFlowLogId.NotFound  | The specified flow log does not exist. | 
| <a name="InvalidFormat"></a> InvalidFormat | The specified disk format (for the instance or volume import) is not valid. | 
| InvalidFpgaImageID.Malformed | The specified Amazon FPGA image (AFI) ID is malformed. Ensure that you provide the full AFI ID in the request, in the form afi-xxxxxxxxxxxxxxxxx. | 
| InvalidFpgaImageID.NotFound | The specified Amazon FPGA image (AFI) ID does not exist. Ensure that you specify the AWS Region in which the AFI is located, if it's not in the default Region. | 
| <a name="InvalidGatewayID.NotFound"></a> InvalidGatewayID.NotFound   | The specified gateway does not exist. | 
| <a name="InvalidGroup.Duplicate"></a> InvalidGroup.Duplicate  | You cannot create a security group with the same name as an existing security group in the same VPC. | 
| <a name="InvalidGroupId.Malformed"></a> InvalidGroupId.Malformed  | The specified security group ID is malformed. Ensure that you provide the full security group ID in the request, in the form sg-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidGroup.InUse"></a> InvalidGroup.InUse  | The specified security group can't be deleted because it's in use by another security group. You can remove dependencies by modifying or deleting rules in the affected security groups. | 
| <a name="InvalidGroup.NotFound"></a> InvalidGroup.NotFound  | The specified security group does not exist.<br />This error can occur because the ID of a recently created security group has not propagated through the system. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).<br />You can't specify a security group that is in a different AWS Region or VPC than the request. | 
| <a name="InvalidGroup.Reserved"></a> InvalidGroup.Reserved  | The name 'default' is reserved, and cannot be used to create a new security group. | 
| InvalidHostConfiguration | The specified Dedicated Host configuration is not supported. | 
| InvalidHostId | The specified Dedicated Host ID is not valid. | 
| InvalidHostID.Malformed | The specified Dedicated Host ID is not formed correctly. Ensure that you provide the full ID in the form h-xxxxxxxxxxxxxxxxx. | 
| InvalidHostId.Malformed | The specified Dedicated Host ID is not formed correctly. Ensure that you provide the full ID in the form h-xxxxxxxxxxxxxxxxx. | 
| InvalidHostID.NotFound | The specified Dedicated Host ID does not exist. Ensure that you specify the AWS Region in which the Dedicated Host is located, if it's not in the default Region. | 
| InvalidHostId.NotFound | The specified Dedicated Host ID does not exist. Ensure that you specify the region in which the Dedicated Host is located, if it's not in the default region. | 
| InvalidHostReservationId.Malformed | The specified Dedicated Host Reservation ID is not formed correctly. Ensure that you provide the full ID in the form hr-xxxxxxxxxxxxxxxxx. | 
| InvalidHostReservationOfferingId.Malformed | The specified Dedicated Host Reservation offering is not formed correctly. Ensure that you provide the full ID in the form hro-xxxxxxxxxxxxxxxxx. | 
| InvalidHostState | The Dedicated Host must be in the available state to complete the operation. | 
| InvalidIamInstanceProfileArn.Malformed | The specified IAM instance profile ARN is not valid. For more information about valid ARN formats, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). | 
| <a name="InvalidID"></a>InvalidID | The specified ID for the resource you are trying to tag is not valid. Ensure that you provide the full resource ID; for example, ami-2bb65342 for an AMI.If you're using the command line tools on a Windows system, you might need to use quotation marks for the key-value pair; for example, `"Name=TestTag"`. | 
| <a name="InvalidInput"></a>InvalidInput | An input parameter in the request is not valid. For example, you may have specified an incorrect Reserved Instance listing ID in the request or the Reserved Instance you tried to list cannot be sold in the Reserved Instances Marketplace (for example, if it has a scope of Region, or is a Convertible Reserved Instance). | 
| <a name="InvalidInstanceAttributeValue"></a>InvalidInstanceAttributeValue | The specified instance attribute value is not valid. This error is most commonly encountered when trying to set the InstanceType/--instance-type attribute to an unrecognized value. | 
| InvalidInstanceConnectEndpointId.Malformed | The specified EC2 Instance Connect Endpoint ID is malformed. Ensure that you specify the ID in the form eice-xxxxxxxxxxxxxxxxx. | 
| InvalidInstanceConnectEndpointId.NotFound | The specified EC2 Instance Connect Endpoint does not exist. | 
| <a name="InvalidInstanceCreditSpecification"></a>InvalidInstanceCreditSpecification | If you are modifying the credit option for CPU usage for T2 instances, the request may not contain duplicate instance IDs. | 
| <a name="InvalidInstanceCreditSpecification.DuplicateInstanceId"></a>InvalidInstanceCreditSpecification.DuplicateInstanceId | If you are modifying the credit option for CPU usage for T2 instances, the request may not contain duplicate instance IDs. | 
| <a name="InvalidInstanceEventIDNotFound"></a>InvalidInstanceEventIDNotFound | The specified ID of the event whose date and time you are modifying cannot be found. Verify the ID of the event and try your request again.  | 
| <a name="InvalidInstanceEventStartTime"></a>InvalidInstanceEventStartTime | The specified scheduled event start time does not meet the requirements for rescheduling a scheduled event. For more information, see [Limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html). | 
| InvalidInstanceFamily | The instance family is not supported for this request. For example, the instance family for the Dedicated Host Reservation offering is different from the instance family of the Dedicated Hosts. Or, you can only modify the default credit specification for burstable performance instance families (T2, T3, and T3a). For more information, see [Set the default credit specification for the account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-how-to.html#burstable-performance-instance-set-default-credit-specification-for-account). | 
| <a name="InvalidInstanceID"></a>InvalidInstanceID | This error can occur when trying to perform an operation on an instance that has multiple network interfaces.<br />A network interface can have individual attributes; therefore, you may need to specify the network interface ID as part of the request, or use a different request. For example, each network interface in an instance can have a source/destination check flag. To modify this attribute, modify the network interface attribute, and not the instance attribute.<br />To create a route in a route table, provide a specific network interface ID as part of the request. | 
| <a name="InvalidInstanceID.Malformed"></a> InvalidInstanceID.Malformed  | The specified instance ID is malformed. Ensure that you provide the full instance ID in the request, in the form i-xxxxxxxx or i-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidInstanceID.NotFound"></a> InvalidInstanceID.NotFound  | The specified instance does not exist. This error might occur because the ID of a recently created instance has not propagated through the system. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html). | 
| <a name="InvalidInstanceID.NotLinkable"></a>InvalidInstanceID.NotLinkable | The specified instance cannot be linked to the specified VPC. This error may also occur if the instance was recently launched, and its ID has not yet propagated through the system. Wait a few minutes, or wait until the instance is in the running state, and then try again. | 
| InvalidInstanceState | The instance is not in an appropriate state to complete the request. If you're modifying the instance placement, the instance must be in the stopped state. | 
| <a name="InvalidInstanceType"></a>InvalidInstanceType | The instance type is not supported for this request. For example, you can only bundle instance store-backed Windows instances. | 
| <a name="InvalidInterface.IpAddressLimitExceeded"></a>InvalidInterface.IpAddressLimitExceeded | The number of private IP addresses for a specified network interface exceeds the limit for the type of instance you are trying to launch. For more information, see [IP addresses per network interface per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI). | 
| <a name="InvalidInternetGatewayId.Malformed"></a> InvalidInternetGatewayId.Malformed  | The specified internet gateway ID is malformed. Ensure that you provide the full ID in the request, in the form igw-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidInternetGatewayID.NotFound"></a> InvalidInternetGatewayID.NotFound  | The specified internet gateway does not exist. Ensure that you specify the AWS Region in which the internet gateway is located, if it's not in the default Region. | 
| <a name="InvalidIPAddress.InUse"></a> InvalidIPAddress.InUse  | The specified IP address is already in use. If you are trying to release an address, you must first disassociate it from the instance. | 
| InvalidKernelId.Malformed | The specified kernel ID is not valid. Ensure that you specify the kernel ID in the form aki-xxxxxxxx. | 
| <a name="InvalidKey.Format"></a>InvalidKey.Format | The key pair is not specified in a valid OpenSSH public key format. | 
| <a name="InvalidKeyPair.Duplicate"></a> InvalidKeyPair.Duplicate  | The key pair name already exists in that AWS Region. If you are creating or importing a key pair, ensure that you use a unique name. | 
| <a name="InvalidKeyPair.Format"></a> InvalidKeyPair.Format  | The format of the public key you are attempting to import is not valid. | 
| <a name="InvalidKeyPair.NotFound"></a> InvalidKeyPair.NotFound  | The specified key pair name does not exist. Ensure that you specify the AWS Region in which the key pair is located, if it's not in the default Region. | 
| InvalidCapacityReservationId.Malformed | The ID for the Capacity Reservation is malformed. Ensure that you specify the Capacity Reservation ID in the form cr-xxxxxxxxxxxxxxxxx. | 
| InvalidCapacityReservationId.NotFound | The specified Capacity Reservation ID does not exist. | 
| <a name="InvalidLaunchTargets"></a>InvalidLaunchTargets | One or more specified targets are invalid. Verify the capacity for the Capacity Reservation selected or verify the ID. | 
| InvalidLaunchTemplateId.Malformed | The ID for the launch template is malformed. Ensure that you specify the launch template ID in the form lt-xxxxxxxxxxxxxxxxx. | 
| InvalidLaunchTemplateId.NotFound | The specified launch template ID does not exist. Ensure that you specify the AWS Region in which the launch template is located. | 
| InvalidLaunchTemplateId.VersionNotFound | The specified launch template version does not exist. | 
| InvalidLaunchTemplateName.AlreadyExistsException | The specified launch template name is already in use. | 
| InvalidLaunchTemplateName.MalformedException | The specified launch template name is invalid. A launch template name must be between 3 and 128 characters, and may contain letters, numbers, and the following characters: '-', '\_', '.', '/', '(', and ')'. | 
| InvalidLaunchTemplateName.NotFoundException | The specified launch template name does not exist. Check the spelling of the name and ensure that you specify the AWS Region in which the launch template is located. Launch template names are case-sensitive. | 
| <a name="InvalidManifest"></a> InvalidManifest  | The specified AMI has an unparsable manifest, or you may not have access to the location of the manifest file in Amazon S3. | 
| InvalidMaxResults | The specified value for MaxResults is not valid. | 
| InvalidNatGatewayID.NotFound | The specified NAT gateway ID does not exist. Ensure that you specify the AWS Region in which the NAT gateway is located, if it's not in the default Region. | 
| <a name="InvalidNetworkAclEntry.NotFound"></a> InvalidNetworkAclEntry.NotFound   | The specified network ACL entry does not exist. | 
| InvalidNetworkAclId.Malformed | The specified network ACL ID is malformed. Ensure that you provide the ID in the form acl-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidNetworkAclID.NotFound"></a> InvalidNetworkAclID.NotFound  | The specified network ACL does not exist. Ensure that you specify the AWS Region in which the network ACL is located, if it's not in the default Region. | 
| InvalidNetworkLoadBalancerArn.Malformed | The specified Network Load Balancer ARN is malformed. Ensure that you specify the ARN in the form arn:aws:elasticloadbalancing:region:account-id:loadbalancer/net/load-balancer-name/load-balancer-id. | 
| InvalidNetworkLoadBalancerArn.NotFound | The specified Network Load Balancer ARN does not exist. | 
| <a name="InvalidNetworkInterfaceAttachmentID.Malformed"></a>InvalidNetworkInterfaceAttachmentId.Malformed | The ID for the network interface attachment is malformed. Ensure that you use the attachment ID rather than the network interface ID, in the form eni-attach-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidNetworkInterface.InUse"></a>InvalidNetworkInterface.InUse | The specified interface is currently in use and cannot be deleted or attached to another instance. Ensure that you have detached the network interface first. If a network interface is in use, you may also receive the InvalidParameterValue error. | 
| <a name="InvalidNetworkInterfaceId.Malformed"></a>InvalidNetworkInterfaceId.Malformed | The specified network interface ID is malformed. Ensure that you specify the network interface ID in the form eni-xxxxxxxxxxxxxxxxx. | 
| InvalidNetworkInterface.NotFound | The specified network interface does not exist. | 
| <a name="InvalidNetworkInterfaceID.NotFound"></a>InvalidNetworkInterfaceID.NotFound | The specified network interface does not exist. Ensure that you specify the AWS Region in which the network interface is located, if it's not in the default Region. | 
| InvalidNextToken | The specified NextToken is not valid. | 
| <a name="InvalidOption.Conflict"></a>InvalidOption.Conflict | A VPN connection between the virtual private gateway and the customer gateway already exists. | 
| <a name="InvalidPermission.Duplicate"></a> InvalidPermission.Duplicate  | The specified inbound or outbound rule already exists for that security group. | 
| <a name="InvalidPermission.Malformed"></a> InvalidPermission.Malformed  | The specified security group rule is malformed. If you are specifying an IP address range, ensure that you use CIDR notation; for example, 203.0.113.0/24. | 
| <a name="InvalidPermission.NotFound"></a>InvalidPermission.NotFound | The specified rule does not exist in this security group. | 
| <a name="InvalidPlacementGroup.Duplicate"></a>InvalidPlacementGroup.Duplicate | The specified placement group already exists in that AWS Region. | 
| <a name="InvalidPlacementGroup.InUse"></a>InvalidPlacementGroup.InUse | The specified placement group is in use. If you are trying to delete a placement group, ensure that its instances have been terminated.  | 
| <a name="InvalidPlacementGroup.Unknown"></a>InvalidPlacementGroup.Unknown | The specified placement group cannot be found. Ensure that you specify the AWS Region in which the placement group is located, if it's not in the default Region. | 
| InvalidPlacementGroupId.Malformed | The specified placement group ID is malformed. Ensure that you specify the ID in the form pg-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidPolicyDocument"></a>InvalidPolicyDocument | The specified policy document is not a valid JSON policy document.  | 
| <a name="InvalidPrefixListId.Malformed"></a>InvalidPrefixListId.Malformed | The specified prefix list ID is malformed. Ensure that you provide the ID in the form pl-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidPrefixListId.NotFound"></a>InvalidPrefixListID.NotFound | The specified prefix list ID does not exist. | 
| InvalidProductInfo | (AWS Marketplace) The product code is not valid. | 
| <a name="InvalidPurchaseToken.Expired"></a>InvalidPurchaseToken.Expired | The specified purchase token has expired. | 
| <a name="InvalidPurchaseToken.Malformed"></a>InvalidPurchaseToken.Malformed | The specified purchase token is not valid. | 
| InvalidQuantity | The specified quantity of Dedicated Hosts is not valid. | 
| InvalidRamDiskId.Malformed | The specified RAM disk ID is not valid. Ensure that you specify the RAM disk ID in the form ari-xxxxxxxx. | 
| InvalidRegion | The specified AWS Region is not valid. For copying a snapshot or image, specify the source Region using its Region code, for example, us-west-2. | 
| <a name="InvalidRequest"></a>InvalidRequest | The request is not valid. The returned message provides details about the nature of the error. | 
| <a name="InvalidReservationID.Malformed"></a>InvalidReservationID.Malformed  | The specified reservation ID is not valid. | 
| <a name="InvalidReservationID.NotFound"></a>InvalidReservationID.NotFound  | The specified reservation does not exist. | 
| <a name="InvalidReservedInstancesId"></a>InvalidReservedInstancesId  | The specified Reserved Instance does not exist. | 
| <a name="InvalidReservedInstancesOfferingId"></a>InvalidReservedInstancesOfferingId | The specified Reserved Instances offering does not exist. | 
| <a name="InvalidResourceConfigurationArn.Malformed"></a>InvalidResourceConfigurationArn.Malformed | The specified resource configuration ARN is malformed. | 
| <a name="InvalidResourceConfigurationArn.NotFound"></a>InvalidResourceConfigurationArn.NotFound | The specified resource configuration ARN does not exist. | 
| InvalidResourceType.Unknown | The specified resource type is not supported or is not valid. To view resource types that support longer IDs, use [DescribeIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdFormat.html). | 
| InvalidRoute.InvalidState | The specified route is not valid. | 
| <a name="InvalidRoute.Malformed"></a>InvalidRoute.Malformed  | The specified route is not valid. If you are deleting a route in a VPN connection, ensure that you've entered the value for the CIDR block correctly. | 
| <a name="InvalidRoute.NotFound"></a>InvalidRoute.NotFound  | The specified route does not exist in the specified route table. Ensure that you indicate the exact CIDR range for the route in the request. This error can also occur if you've specified a route table ID in the request that does not exist. | 
| <a name="InvalidRouteTableId.Malformed"></a>InvalidRouteTableId.Malformed | The specified route table ID is malformed. Ensure that you specify the route table ID in the form rtb-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidRouteTableID.NotFound"></a>InvalidRouteTableID.NotFound  | The specified route table does not exist. Ensure that you specify the AWS Region in which the route table is located, if it's not in the default Region. | 
| <a name="InvalidScheduledInstance"></a>InvalidScheduledInstance | The specified Scheduled Instance does not exist. | 
| InvalidSecurityGroupId.Malformed | The specified security group ID is not valid. Ensure that you specify the security group ID in the form sg-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidSecurityGroupID.NotFound"></a>InvalidSecurityGroupID.NotFound | The specified security group does not exist. | 
| InvalidSecurityGroupRuleId.Malformed | The specified security group rule ID is not valid. Ensure that you specify the security group rule ID in the form sgr-xxxxxxxxxxxxxxxxx. | 
| InvalidSecurityGroupRuleId.NotFound | The specified security group rule does not exist. | 
| <a name="InvalidSecurity.RequestHasExpired"></a> InvalidSecurity.RequestHasExpired  | The difference between the request timestamp and the AWS server time is greater than 5 minutes. Ensure that your system clock is accurate and configured to use the correct time zone. | 
| <a name="InvalidServiceName"></a> InvalidServiceName  | The name of the service is not valid. To get a list of available service names, use [DescribeVpcEndpointServices](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html). | 
| <a name="InvalidSnapshotIDNotFound"></a> InvalidSnapshot.NotFound | The specified snapshot does not exist. Ensure that you specify the AWS Region in which the snapshot is located, if it's not in the default Region. | 
| <a name="InvalidSnapshotID.Malformed"></a> InvalidSnapshotID.Malformed | The snapshot ID is not valid. | 
| <a name="InvalidSnapshot.InUse"></a> InvalidSnapshot.InUse  | The snapshot that you are trying to delete is in use by one or more AMIs. | 
| <a name="InvalidSnapshot.NotFound"></a> InvalidSnapshot.NotFound  | The specified snapshot does not exist. Ensure that you specify the AWS Region in which the snapshot is located, if it's not in the default Region. | 
| <a name="InvalidSpotDatafeed.NotFound"></a>InvalidSpotDatafeed.NotFound | You have no data feed for Spot Instances. | 
| <a name="InvalidSpotFleetRequestConfig"></a>InvalidSpotFleetRequestConfig | The Spot Fleet request configuration is not valid. Ensure that you provide valid values for all of the configuration parameters; for example, a valid AMI ID. Limits apply on the target capacity and the number of launch specifications per Spot Fleet request. For more information, see [Fleet quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-quotas). | 
| <a name="InvalidSpotFleetRequestId.Malformed"></a>InvalidSpotFleetRequestId.Malformed | The specified Spot Fleet request ID is malformed. Ensure that you specify the Spot Fleet request ID in the form sfr- followed by 36 characters, including hyphens; for example, sfr-123f8fc2-11aa-22bb-33cc-example12710. | 
| <a name="InvalidSpotFleetRequestId.NotFound"></a>InvalidSpotFleetRequestId.NotFound | The specified Spot Fleet request ID does not exist. Ensure that you specify the AWS Region in which the Spot Fleet request is located, if it's not in the default Region. | 
| <a name="InvalidSpotInstanceRequestID.Malformed"></a>InvalidSpotInstanceRequestID.Malformed | The specified Spot Instance request ID is not valid. Ensure that you specify the Spot Instance request ID in the form sir-xxxxxxxx. | 
| <a name="InvalidSpotInstanceRequestID.NotFound"></a>InvalidSpotInstanceRequestID.NotFound | The specified Spot Instance request ID does not exist. Ensure that you specify the AWS Region in which the Spot Instance request is located, if it's not in the default Region. | 
| <a name="InvalidState"></a>InvalidState | The specified resource is not in the correct state for the request; for example, if you are trying to enable monitoring on a recently terminated instance, or if you are trying to create a snapshot when a previous identical request has not yet completed. | 
| <a name="InvalidStateTransition"></a>InvalidStateTransition | The specified VPC peering connection is not in the correct state for the request. For example, you may be trying to accept a VPC peering request that has failed, or that was rejected. | 
| InvalidSubnet | The specified subnet ID is not valid or does not exist. | 
| <a name="InvalidSubnet.Conflict"></a>InvalidSubnet.Conflict | The specified CIDR block conflicts with that of another subnet in your VPC. | 
| InvalidSubnetID.Malformed | The specified subnet ID is malformed. Ensure that you specify the ID in the form subnet-xxxxxxxxxxxxxxxxx | 
| <a name="InvalidSubnetID.NotFound"></a> InvalidSubnetID.NotFound or InvalidSubnetId.NotFound  | The specified subnet does not exist. | 
| <a name="InvalidSubnet.Range"></a>InvalidSubnet.Range | The CIDR block you've specified for the subnet is not valid. The allowed block size is between a /28 netmask and /16 netmask. | 
|  InvalidTagKey.Malformed  | The specified tag key is not valid. Tag keys cannot be empty or null, and cannot start with aws:. | 
| InvalidTargetArn.Unknown | The specified ARN for the specified user or role is not valid or does not exist. | 
| InvalidTargetException | The specified TargetId is not valid, does not exist, or is in another organization. You can only generate an account status report for declarative policies in your own organization. Ensure that you specify the TargetId in one of the following forms: r-xxxx, ou-xxxx-xxxxxxxx, or a 12-digit account ID in the form xxxxxxxxxxxx. | 
| InvalidTenancy | The tenancy of the instance or VPC is not supported for the requested action. For example, you cannot modify the tenancy of an instance or VPC that has a tenancy attribute of default. | 
| InvalidTime | The specified timestamp is not valid. | 
| InvalidTrafficMirrorFilterNotFound | The specified Traffic Mirror filter does not exist. | 
| InvalidTrafficMirrorFilterRuleNotFound | The specified Traffic Mirror filter rule does not exist. | 
| InvalidTrafficMirrorSessionNotFound  | The specified Traffic Mirror session does not exist. | 
| InvalidTrafficMirrorTargetNoFound | The specified Traffic Mirror target does not exist. | 
| <a name="InvalidUserID.Malformed"></a> InvalidUserID.Malformed  | The specified user or owner is not valid. If you are performing a [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) request, you must specify a valid value for the owner or executableBy parameters, such as an AWS account ID. If you are performing a [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) request, you must specify a valid value for the owner or restorableBy parameters. | 
| <a name="InvalidVolumeID.Duplicate"></a> InvalidVolumeID.Duplicate  | The Amazon EBS volume already exists. | 
| <a name="InvalidVolumeID.Malformed"></a> InvalidVolumeID.Malformed | The specified volume ID is not valid. Check the letter-number combination carefully. | 
| <a name="InvalidVolumeID.ZoneMismatch"></a> InvalidVolumeID.ZoneMismatch  | The specified volume and instance are in different Availability Zones. | 
| <a name="InvalidVolume.NotFound"></a> InvalidVolume.NotFound  | The specified volume does not exist. | 
| <a name="InvalidVolume.ZoneMismatch"></a>InvalidVolume.ZoneMismatch | The specified volume is not in the same Availability Zone as the specified instance. You can only attach an Amazon EBS volume to an instance if they are in the same Availability Zone. | 
| <a name="InvalidVpcEndpoint.NotFound"></a>InvalidVpcEndpoint.NotFound | The specified VPC endpoint does not exist. If you are performing a bulk request that is partially successful or unsuccessful, the response includes a list of the unsuccessful items. If the request succeeds, the list is empty. | 
| <a name="InvalidVpcEndpointId.Malformed"></a>InvalidVpcEndpointId.Malformed | The specified VPC endpoint ID is malformed. Use the full VPC endpoint ID in the request, in the form vpce-xxxxxxxxxxxxxxxxx.  | 
| <a name="InvalidVpcEndpointId.NotFound"></a>InvalidVpcEndpointId.NotFound | The specified VPC endpoint does not exist. If you are performing a bulk request that is partially successful or unsuccessful, the response includes a list of the unsuccessful items. If the request succeeds, the list is empty. | 
| <a name="InvalidVpcEndpointService.NotFound"></a>InvalidVpcEndpointService.NotFound | The specified VPC endpoint service does not exist. If you are performing a bulk request that is partially successful or unsuccessful, the response includes a list of the unsuccessful items. If the request succeeds, the list is empty. | 
| InvalidVpcEndpointServiceIdId.Malformed | The specified VPC endpoint service ID is malformed. Ensure that you specify the ID in the form vpc-svc-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidVpcEndpointServiceId.NotFound"></a>InvalidVpcEndpointServiceId.NotFound | The specified VPC endpoint service does not exist. If you are performing a bulk request that is partially successful or unsuccessful, the response includes a list of the unsuccessful items. If the request succeeds, the list is empty. | 
| InvalidVpcEndpointType | The specified VPC endpoint type is not valid. | 
| <a name="InvalidVpcID.Malformed"></a>InvalidVpcID.Malformed | The specified VPC ID is malformed. Ensure that you've specified the ID in the form vpc-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidVpcID.NotFound"></a> InvalidVpcID.NotFound  | The specified VPC does not exist.  | 
| <a name="InvalidVpcPeeringConnectionId.Malformed"></a>InvalidVpcPeeringConnectionId.Malformed | The specified VPC peering connection ID is malformed. Ensure that you provide the ID in the form pcx-xxxxxxxxxxxxxxxxx. | 
| <a name="InvalidVpcPeeringConnectionId.NotFound"></a>InvalidVpcPeeringConnectionID.NotFound | The specified VPC peering connection ID does not exist. | 
| InvalidVpcPeeringConnectionState.DnsHostnamesDisabled | To enable DNS hostname resolution for the VPC peering connection, DNS hostname support must be enabled for the VPCs. | 
| <a name="InvalidVpcRange"></a>InvalidVpcRange | The specified CIDR block range is not valid. The block range must be between a /28 netmask and /16 netmask. For more information, see [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html#vpc-cidr-blocks).  | 
| <a name="InvalidVpcState"></a>InvalidVpcState | The specified VPC already has a virtual private gateway attached to it. | 
| <a name="InvalidVpnConnectionID"></a>InvalidVpnConnectionID | The specified VPN connection ID cannot be found. | 
| <a name="InvalidVpnConnectionID.NotFound"></a> InvalidVpnConnectionID.NotFound  | The specified VPN connection ID does not exist. | 
| InvalidVpnConnection.InvalidState | The VPN connection must be in the available state to complete the request. | 
| InvalidVpnConnection.InvalidType | The specified VPN connection does not support static routes. | 
| <a name="InvalidVpnGatewayAttachment.NotFound"></a>InvalidVpnGatewayAttachment.NotFound | An attachment between the specified virtual private gateway and specified VPC does not exist. This error can also occur if you've specified an incorrect VPC ID in the request. | 
| <a name="InvalidVpnGatewayID.NotFound"></a> InvalidVpnGatewayID.NotFound  | The specified virtual private gateway does not exist. | 
| InvalidVpnGatewayState | The virtual private gateway is not in an available state. | 
| <a name="InvalidZone.NotFound"></a> InvalidZone.NotFound  | The specified Availability Zone does not exist, or is not available for you to use. Use the [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) request to list the Availability Zones that are currently available to you. Specify the full name of the Availability Zone: for example, us-east-1a. | 
| KeyPairLimitExceeded | You've reached the limit on the number of key pairs that you can have in this AWS Region. For more information, see [Amazon EC2 key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html). | 
| <a name="LegacySecurityGroup"></a> LegacySecurityGroup  | Any VPC created using an API version older than 2011-01-01 may have the 2009-07-15-default security group. You must delete this security group before you can attach an internet gateway to the VPC. | 
| LimitPriceExceeded | The cost of the total order is greater than the specified limit price (instance count \* price). | 
| LogDestinationNotFound | The specified Amazon S3 bucket does not exist. Ensure that you have specified the ARN for an existing Amazon S3 bucket, and that the ARN is in the correct format. | 
| LogDestinationPermissionIssue | You do not have sufficient permissions to publish flow logs to the specific Amazon S3 bucket. | 
| MaxConfigLimitExceededException | You’ve exceeded your maximum allowed Spot placement configurations. You can retry configurations that you used within the last 24 hours, or wait for 24 hours before specifying a new configuration. For more information, see [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score). | 
| <a name="MaxIOPSLimitExceeded"></a>MaxIOPSLimitExceeded | You've reached the limit on your IOPS usage for the AWS Region. For more information, see [Quotas for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html). | 
| <a name="MaxScheduledInstanceCapacityExceeded"></a>MaxScheduledInstanceCapacityExceeded | You've attempted to launch more instances than you purchased. | 
| <a name="MaxSpotFleetRequestCountExceeded"></a>MaxSpotFleetRequestCountExceeded | You've reached one or both of these limits: the total number of Spot Fleet requests that you can make, or the total number of instances in all Spot Fleets for the AWS Region (the target capacity). For more information, see [Fleet quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-quotas.html). | 
| <a name="MaxSpotInstanceCountExceeded"></a>MaxSpotInstanceCountExceeded | You've reached the limit on the number of Spot Instances that you can launch. The limit depends on the instance type. For more information, see [Spot Instance limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html). | 
| MaxTemplateLimitExceeded | You've reached the limit on the number of launch templates you can create. For more information, see [Launch template restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-template-restrictions.html). | 
| MaxTemplateVersionLimitExceeded | You've reached the limit on the number of launch template versions that you can create. For more information, see [Launch template restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-template-restrictions.html). | 
| MissingInput | An input parameter is missing. | 
| NatGatewayLimitExceeded | You've reached the limit on the number of NAT gateways that you can create. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| NatGatewayMalformed | The specified NAT gateway ID is not formed correctly. Ensure that you specify the NAT gateway ID in the form nat-xxxxxxxxxxxxxxxxx. | 
| NatGatewayNotFound | The specified NAT gateway does not exist. | 
| <a name="NetworkAclEntryAlreadyExists"></a> NetworkAclEntryAlreadyExists  | The specified rule number already exists in this network ACL. | 
| <a name="NetworkAclEntryLimitExceeded"></a> NetworkAclEntryLimitExceeded  | You've reached the limit on the number of rules that you can add to the network ACL. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="NetworkAclLimitExceeded"></a> NetworkAclLimitExceeded  | You've reached the limit on the number of network ACLs that you can create for the specified VPC. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| NetworkInterfaceLimitExceeded | You've reached the limit on the number of network interfaces that you can create. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| NetworkInterfaceNotSupported | The network interface is not supported for Traffic Mirroring. | 
| NetworkLoadBalancerNotFoundException | The specified Network Load Balancer does not exist. | 
| NlbInUseByTrafficMirrorTargetException | The Network Load Balancer is already configured as a Traffic Mirror target. | 
| <a name="NonEBSInstance"></a> NonEBSInstance  | The specified instance does not support Amazon EBS. Restart the instance and try again, to ensure that the code is run on an instance with updated code. | 
| NoSuchVersion | The specified API version does not exist. | 
| <a name="NotExportable"></a>NotExportable | The specified instance cannot be exported. You can only export certain instances. For more information, see [Considerations for instance export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html#vmexport-limits). | 
| <a name="OperationNotPermitted"></a>OperationNotPermitted | The specified operation is not allowed. This error can occur for a number of reasons; for example, you might be trying to terminate an instance that has termination protection enabled, or trying to detach the primary network interface (eth0) from an instance. | 
| <a name="OutstandingVpcPeeringConnectionLimitExceeded"></a>OutstandingVpcPeeringConnectionLimitExceeded | You've reached the limit on the number of VPC peering connection requests that you can create for the specified VPC. | 
| <a name="PendingSnapshotLimitExceeded"></a> PendingSnapshotLimitExceeded  | You've reached the limit on the number of Amazon EBS snapshots that you can have in the pending state. | 
| PendingVpcPeeringConnectionLimitExceeded | You've reached the limit on the number of pending VPC peering connections that you can have. | 
| PlacementGroupLimitExceeded | You've reached the limit on the number of placement groups that you can have. | 
| <a name="PrivateIpAddressLimitExceeded"></a>PrivateIpAddressLimitExceeded | You've reached the limit on the number of private IP addresses that you can assign to the specified network interface for that type of instance. For more information, see [IP addresses per network interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI). | 
| <a name="RequestResourceCountExceeded"></a>RequestResourceCountExceeded | Details in your Spot request exceed the numbers allowed by the Spot service in one of the following ways, depending on the action that generated the error:<br />—If you get this error when you submitted a request for Spot Instances, check the number of Spot Instances specified in your request. The number shouldn't exceed the 3,000 maximum allowed per request. Resend your Spot Instance request and specify a number less than 3,000. If your account's regional Spot request limit is greater than 3,000 instances, you can access these instances by submitting multiple smaller requests.<br />—If you get this error when you sent Describe Spot Instance requests, check the number of requests for Spot Instance data, the amount of data you requested, and how often you sent the request. The frequency with which you requested the data combined with the amount of data exceeds the levels allowed by the Spot service. Try again and submit fewer large Describe requests over longer intervals. | 
| ReservationCapacityExceeded | The targeted Capacity Reservation does not enough available instance capacity to fulfill your request. Either increase the instance capacity for the targeted Capacity Reservation, or target a different Capacity Reservation. | 
| ReservedInstancesCountExceeded | You've reached the limit for the number of Reserved Instances. | 
| <a name="ReservedInstancesLimitExceeded"></a> ReservedInstancesLimitExceeded | Your current quota does not allow you to purchase the required number of Reserved Instances. | 
| ReservedInstancesUnavailable | The requested Reserved Instances are not available. | 
| Resource.AlreadyAssigned | The specified private IP address is already assigned to a resource. Unassign the private IP first, or use a different private IP address. | 
| <a name="Resource.AlreadyAssociated"></a> Resource.AlreadyAssociated   | The specified resource is already in use. For example, in EC2-VPC, you cannot associate an Elastic IP address with an instance if it's already associated with another instance. You also cannot attach an internet gateway to more than one VPC at a time. | 
| <a name="ResourceCountExceeded"></a> ResourceCountExceeded  | You have exceeded the number of resources allowed for this request; for example, if you try to launch more instances than AWS allows in a single request. This limit is separate from your individual resource limit. If you get this error, break up your request into smaller requests; for example, if you are launching 15 instances, try launching 5 instances in 3 separate requests. | 
| ResourceCountLimitExceeded | You have exceeded a resource limit for creating routes.  | 
| <a name="ResourceLimitExceeded"></a> ResourceLimitExceeded  | You have exceeded an Amazon EC2 resource limit. For example, you might have too many snapshot copies in progress. | 
| <a name="RetryableError"></a> RetryableError  | A request submitted by an AWS service on your behalf could not be completed. The requesting service might automatically retry the request. | 
| <a name="RouteAlreadyExists"></a> RouteAlreadyExists  | A route for the specified CIDR block already exists in this route table. | 
| <a name="RouteLimitExceeded"></a> RouteLimitExceeded  | You've reached the limit on the number of routes that you can add to a route table. | 
| <a name="RouteTableLimitExceeded"></a> RouteTableLimitExceeded   | You've reached the limit on the number of route tables that you can create for the specified VPC. For more information about route table limits, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="RulesPerSecurityGroupLimitExceeded"></a> RulesPerSecurityGroupLimitExceeded  | You've reached the limit on the number of rules that you can add to a security group. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| ScheduledInstanceLimitExceeded | You've reached the limit on the number of Scheduled Instances that you can purchase.  | 
| <a name="ScheduledInstanceParameterMismatch"></a>ScheduledInstanceParameterMismatch | The launch specification does not match the details for the Scheduled Instance. | 
| <a name="ScheduledInstanceSlotNotOpen"></a>ScheduledInstanceSlotNotOpen | You can launch a Scheduled Instance only during its scheduled time periods. | 
| <a name="ScheduledInstanceSlotUnavailable"></a>ScheduledInstanceSlotUnavailable | The requested Scheduled Instance is no longer available during this scheduled time period. | 
| <a name="SecurityGroupLimitExceeded"></a> SecurityGroupLimitExceeded  | You've reached the limit on the number of security groups that you can create, or that you can assign to an instance. | 
| <a name="SecurityGroupsPerInstanceLimitExceeded"></a> SecurityGroupsPerInstanceLimitExceeded  | You've reached the limit on the number of security groups that you can assign to an instance. For more information, see [Amazon EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html). | 
| <a name="SecurityGroupsPerInterfaceLimitExceeded"></a>SecurityGroupsPerInterfaceLimitExceeded | You've reached the limit on the number of security groups you can associate with the specified network interface. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="SignatureDoesNotMatch"></a>SignatureDoesNotMatch | The request signature that Amazon has does not match the signature that you provided. Check your AWS credentials and signing method.  | 
| SnapshotCopyUnsupported.InterRegion | Inter-region snapshot copy is not supported for this AWS Region. | 
| <a name="SnapshotCreationPerVolumeRateExceeded"></a>SnapshotCreationPerVolumeRateExceeded | The rate limit for creating concurrent snapshots of an EBS volume has been exceeded. Wait at least 15 seconds between concurrent volume snapshots. | 
| <a name="SnapshotLimitExceeded"></a>SnapshotLimitExceeded  | You've reached the limit on the number of Amazon EBS snapshots that you can create. | 
| <a name="SpotMaxPriceTooLow"></a>SpotMaxPriceTooLow  | The request can't be fulfilled yet because your maximum price is below the Spot price. In this case, no instance is launched and your request remains open. | 
| <a name="SubnetLimitExceeded"></a>SubnetLimitExceeded  | You've reached the limit on the number of subnets that you can create for the specified VPC. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="TagLimitExceeded"></a>TagLimitExceeded | You've reached the limit on the number of tags that you can assign to the specified resource. For more information, see [Tag restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions). | 
| TargetCapacityLimitExceededException | The value for targetCapacity exceeds your limit on the amount of Spot placement target capacity you can explore. Reduce the targetCapacity value, and try again. For more information, see [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score). | 
| TrafficMirrorFilterInUse | The Traffic Mirror filter cannot be deleted because a Traffic Mirror session is currently using it. | 
| TrafficMirrorSessionsPerInterfaceLimitExceeded | The allowed number of Traffic Mirror sessions for the specified network interface has been exceeded. | 
| TrafficMirrorSessionsPerTargetLimitExceeded | The maximum number of Traffic Mirror sessions for the specified Traffic Mirror target has been exceeded. | 
| TrafficMirrorSourcesPerTargetLimitExceeded | The maximum number of Traffic Mirror sources for the specified Traffic Mirror target has been exceeded. | 
| TrafficMirrorTargetInUseException | The Traffic Mirror target cannot be deleted because a Traffic Mirror session is currently using it. | 
| TrafficMirrorFilterLimitExceeded | The maximum number of Traffic Mirror filters has been exceeded. | 
| TrafficMirrorFilterRuleLimitExceeded | The maximum number of Traffic Mirror filter rules has been exceeded. | 
| TrafficMirrorSessionLimitExceeded | The maximum number of Traffic Mirror sessions has been exceeded. | 
| TrafficMirrorTargetLimitExceeded | The maximum number of Traffic Mirror targets has been exceeded. | 
| TrafficMirrorFilterRuleAlreadyExists | The Traffic Mirror filter rule already exists. | 
| UnavailableHostRequirements | There are no valid Dedicated Hosts available on which you can launch an instance. | 
| <a name="UnfulfillableCapacity"></a>UnfulfillableCapacity | At this time there isn't enough spare capacity to fulfill your request for Spot Instances. You can wait a few minutes to see whether capacity becomes available for your request. Alternatively, create a more flexible request. For example, include additional instance types, include additional Availability Zones, or use the capacity-optimized allocation strategy. | 
| UnknownPrincipalType.Unsupported | The principal type is not supported. | 
| <a name="UnknownVolumeType"></a>UnknownVolumeType | The specified volume type is unsupported. The supported volume types are gp2, io1, st1, sc1, and standard. | 
| <a name="Unsupported"></a>Unsupported | The specified request is unsupported. For example, you might be trying to launch an instance in an Availability Zone that currently has constraints on that instance type. The returned message provides details of the unsupported request. | 
| UnsupportedException | Capacity Reservations are not supported for this Region. | 
| UnsupportedHibernationConfiguration | The instance could not be launched because one or more parameter values do not meet the prerequisites for enabling hibernation. For more information, see [Hibernation Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html#hibernating-prerequisites). Alternatively, the instance could not be hibernated because it is not enabled for hibernation. | 
| UnsupportedHostConfiguration | The specified Dedicated Host configuration is unsupported. For more information about supported configurations, see [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html). | 
| UnsupportedInstanceTypeOnHost | The instance type is not supported on the Dedicated Host. For more information about supported instance types, see [Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/). | 
| UnsupportedTenancy | The specified tenancy is unsupported. You can change the tenancy of a VPC to default only. | 
| UpdateLimitExceeded | The default credit specification for an instance family can be modified only once in a rolling 5-minute period, and up to four times in a rolling 24-hour period. For more information, see [Set the default credit specification for the account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-how-to.html#burstable-performance-instance-set-default-credit-specification-for-account). | 
| <a name="VcpuLimitExceeded"></a>VcpuLimitExceeded  | You've reached the limit on the number of vCPUs (virtual processing units) assigned to the running instances in your account. You are limited to running one or more On-Demand instances in an AWS account, and Amazon EC2 measures usage towards each limit based on the total number of vCPUs that are assigned to the running On-Demand instances in your AWS account. If your request fails due to limit constraints, increase your On-Demand instance limits and try again. For more information, see [EC2 On-Demand instance limits](https://aws.amazon.com/ec2/faqs/#EC2_On-Demand_Instance_limits). | 
| <a name="VolumeInUse"></a>VolumeInUse  | The specified Amazon EBS volume is attached to an instance. Ensure that the specified volume is in an ‘available’ state. | 
| VolumeIOPSLimit | The maximum IOPS limit for the volume has been reached. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html). | 
| <a name="VolumeLimitExceeded"></a>VolumeLimitExceeded | You've reached the limit on your Amazon EBS volume storage. For more information, see [Quotas for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html). | 
| VolumeModificationSizeLimitExceeded  | You've reached the limit on your Amazon EBS volume modification storage in this Region. For more information, see [Quotas for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html). | 
| <a name="VolumeTypeNotAvailableInZone"></a>VolumeTypeNotAvailableInZone | The specified Availability Zone does not support Provisioned IOPS SSD volumes. Try launching your instance in a different Availability Zone, or don't specify a zone in the request. If you're creating a volume, try specifying a different Availability Zone in the request. | 
| <a name="VPCIdNotSpecified"></a>VPCIdNotSpecified | You have no default VPC in which to carry out the request. Specify a VPC or subnet ID or, in the case of security groups, specify the ID and not the security group name. If you deleted your default VPC, you can create a new one. For more information, see [Create a default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html#create-default-vpc). | 
| <a name="VpcEndpointLimitExceeded"></a> VpcEndpointLimitExceeded  | You've reached the limit on the number of VPC endpoints that you can create in the AWS Region. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="VpcLimitExceeded"></a> VpcLimitExceeded  | You've reached the limit on the number of VPCs that you can create in the AWS Region. For more information about VPC limits, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="VpcPeeringConnectionAlreadyExists"></a>VpcPeeringConnectionAlreadyExists | A VPC peering connection between the VPCs already exists. | 
| VpcPeeringConnectionsPerVpcLimitExceeded | You've reached the limit on the number of VPC peering connections that you can have per VPC. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="VPCResourceNotSpecified"></a>VPCResourceNotSpecified | The specified resource can be used only in a VPC; for example, T2 instances. Ensure that you have a VPC in your account, and then specify a subnet ID or network interface ID in the request. | 
| <a name="VpnConnectionLimitExceeded"></a>VpnConnectionLimitExceeded  | You've reached the limit on the number of VPN connections that you can create. For more information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| <a name="VpnGatewayAttachmentLimitExceeded"></a> VpnGatewayAttachmentLimitExceeded  | You've reached the limit on the number of VPCs that can be attached to the specified virtual private gateway. | 
| <a name="VpnGatewayLimitExceeded"></a> VpnGatewayLimitExceeded  | You've reached the limit on the number of virtual private gateways that you can create. For more information about limits, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). | 
| ZonesMismatched | The Availability Zone for the instance does not match that of the Dedicated Host. | 

### Common causes of client errors
<a name="api-error-common-causes"></a>

There are a number of reasons that you might encounter an error while performing a request. Some errors can be prevented or easily solved by following these guidelines:
+ **Specify the Region**: Some resources can't be shared between AWS Regions. If you are specifying a resource that's located in a Region other than the current Region, specify its Region in the request. If the resource cannot be found, you get the following error: `Client.Invalid`*Resource*`.NotFound`; for example, `Client.InvalidInstanceID.NotFound`.
+ **Allow for eventual consistency**: Some errors are caused because a previous request has not yet propagated thorough the system. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
+ **Use a sleep interval between request rates**: Amazon EC2 API requests are throttled to help maintain the performance of the service. If your requests have been throttled, you get the following error: `Client.RequestLimitExceeded`. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
+ **Use the full ID of the resource**: When specifying a resource, ensure that you use its full ID, and not its user-supplied name or description. For example, when specifying a security group in a request, use its ID in the form sg-*xxxxxxxxxxxxxxxxx*.
+ **Check your services**: Ensure that you have signed up for all the services you are attempting to use. You can check which services you're signed up for by going to the **My Account** section of the [AWS home page](https://aws.amazon.com/).
+ **Check your permissions**: Ensure that you have the required permissions to carry out the request. If you are not authorized, you get the following error: `Client.UnauthorizedOperation`. For more information, see [Identity and access management for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html).
+ **Check your VPC**: Some resources cannot be shared between VPCs; for example, security groups. 
+ **Check your credentials**: Ensure that you entered the credentials correctly. If you have more than one account, verify that you are using the correct credentials for the specific account. If the provided credentials are incorrect, you might get the following error: `Client.AuthFailure`.

## Server error codes
<a name="api-error-codes-table-server"></a>

This section lists server error codes that can be returned.


| Error code | Description | 
| --- | --- | 
|  BandwidthLimitExceeded  | You've reached the limit on the network bandwidth that is available to an Amazon EC2 instance. For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html). | 
|  InsufficientAddressCapacity  | Not enough available addresses to satisfy your minimum request. Reduce the number of addresses you are requesting or wait for additional capacity to become available. | 
| InsufficientCapacity | There is not enough capacity to fulfill your import instance request. You can wait for additional capacity to become available.  | 
|  InsufficientInstanceCapacity  | There is not enough capacity to fulfill your request. This error can occur if you launch a new instance, restart a stopped instance, create a new Capacity Reservation, or modify an existing Capacity Reservation. Reduce the number of instances in your request, or wait for additional capacity to become available. You can also try launching an instance by selecting different instance types (which you can resize at a later stage). The returned message might also give specific guidance about how to solve the problem. | 
| InsufficientHostCapacity | There is not enough capacity to fulfill your Dedicated Host request. Reduce the number of Dedicated Hosts in your request, or wait for additional capacity to become available.  | 
|  InsufficientReservedInstanceCapacity  | Not enough available Reserved Instances to satisfy your minimum request. Reduce the number of Reserved Instances in your request or wait for additional capacity to become available. | 
| InsufficientVolumeCapacity | There is not enough capacity to fulfill your EBS volume provision request. You can try to provision a different volume type, EBS volume in a different availability zone, or you can wait for additional capacity to become available.  | 
| ServerInternal | An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a message on [AWS re:Post](https://repost.aws/). | 
| InternalFailure | The request processing has failed because of an unknown error, exception, or failure. | 
| RequestLimitExceeded | The maximum request rate permitted by the Amazon EC2 APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests. For more information, see [Query API request rate](query-api-troubleshooting.md#api-request-rate). | 
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 
| InternalError | An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a message on [AWS re:Post](https://repost.aws/). | 
| Unavailable | The server is overloaded and can't handle the request. | 

## Example error response
<a name="api-error-response"></a>

The following shows the structure of a request error response.

```
1. <Response>
2.     <Errors>
3.          <Error>
4.            <Code>Error code text</Code>
5.            <Message>Error message</Message>
6.          </Error>
7.     </Errors>
8.     <RequestID>request ID</RequestID>
9. </Response>
```

The following shows an example of an error response.

```
1. <Response>
2.     <Errors>
3.          <Error>
4.            <Code>InvalidInstanceID.NotFound</Code>
5.            <Message>The instance ID 'i-1a2b3c4d' does not exist</Message>
6.          </Error>
7.     </Errors>
8.     <RequestID>ea966190-f9aa-478e-9ede-example</RequestID>
9. </Response>
```

## Eventual consistency
<a name="api-eventual-consistency"></a>

The Amazon EC2 API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that when you run an API command, the result may not be immediately visible to subsequent API commands, which can result in an error. 

For more information about eventual consistency and how to manage it, see [Eventual consistency](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html).