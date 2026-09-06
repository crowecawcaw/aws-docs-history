

# review-walkthroughs
<a name="review-walkthroughs"></a>

**Topics**
+ [Create a managed prefix list](#ex-vpc-prefix-list-create-col)
+ [Delete a managed prefix list](#ex-vpc-prefix-list-delete-col)
+ [Modify a managed prefix list](#ex-vpc-prefix-list-modify-col)
+ [Create Resource Share](#ex-ram-resource-share-create-col)
+ [Delete ELB Listener Rule](#ex-load-balancer-delete-elb-listener-rule-col)
+ [Associate DHCP option set](#ex-vpc-associate-dhcp-option-set-col)
+ [Manage network firewall rules (managed automation)](#ex-man-fw-network-fw-manage-fw-rules-col)
+ [Remediate DNS scavenging issue](#ex-dirserv-dns-scavenging-remediate-col)
+ [Delete VPC route](#ex-vpc-route-delete-col)
+ [Update parameter group of DB instance or cluster](#ex-rds-db-parameter-group-update-col)
+ [Replace Site-to-Site VPN tunnel](#ex-vpn-s2s-tunnel-replace-col)
+ [Create a DHCP option set](#ex-vpc-create-dhcp-option-set-col)
+ [Create ELB Listener Rule](#ex-load-balancer-create-elb-listener-rule-col)
+ [Update VPC Endpoint Policy](#ex-vpc-endpoint-update-policy-col)
+ [Delete NAT gateway (Managed Automation)](#ex-nat-gateway-delete-rr-col)
+ [Update EC2 Instance Metadata Service (IMDS) Region Setting](#ex-ec2-imds-region-update-col)
+ [Create a computer object's SPN](#ex-dirserv-comp-object-spn-create-col)
+ [Delete target groups (Managed Automation)](#ex-tar-group-delete-rr-col)
+ [Create application load balancer (ALB)](#ex-alb-create-col)
+ [Update application load balancer (ALB)](#ex-alb-update-col)
+ [Create listener](#ex-listener-create-col)
+ [High availability one-tier stacks: Creating](#ex-HA-1-tier-create-col)
+ [Create IAM entity or policy (Managed Automation)](#ex-iam-resource-create-rr-col)
+ [Continue rollback on custom CloudFormation stack](#ex-custom-stack-cfn-template-continue-rollback-col)
+ [Manage the VPC Subnet IPv4 Address Auto Assigment](#ex-vpc-subnet-ipv4-assignment-manage-col)
+ [Schedule add](#ex-res-sched-schedule-add-col)
+ [Delete EBS snapshot (Managed Automation)](#ex-ebs-snpsht-delete-rr-col)
+ [Update SNS topic](#ex-sns-update-col)
+ [Create an S3 access point](#ex-s3-access-point-create-col)
+ [Create Custom RDS Parameter Group](#ex-rds-parameter-group-create-col)
+ [Add event notification to an Amazon S3 bucket](#ex-s3-add-event-notification-col)
+ [Update custom deny list for AMS Automated IAM Provisioning](#ex-man-acc-aip-update-custom-deny-list-col)
+ [Migrate AWS Managed Account DNS resolver to Route 53 for SALZ accounts (Managed Automation)](#ex-man-acct-dns-mig-r53-rr-col)
+ [Disassociate resolver rules from VPC](#ex-vpc-disassociate-resolver-rules-col)
+ [Update Enhanced Monitoring](#ex-rds-db-update-enhanced-monitoring-col)
+ [Associate VPC with Resolver Rule](#ex-vpc-associate-resolver-rule-col)
+ [Deploy AMS pattern (Managed Automation)](#ex-ams-pattern-deploy-rr-col)
+ [Share AWS KMS Key](#ex-man-kms-key-share-rr-col)
+ [Create Active Directory Trust](#ex-dirserv-create-ad-trust-col)
+ [Override Stack Access Duration (Managed automation)](#ex-stack-access-override-col)
+ [Enable automated IAM provisioning with read-write permissions](#ex-man-iam-auto-provision.col)
+ [Add VPC static route (Managed Automation)](#ex-vpc-static-route-add-rr-col)
+ [Create IAM entity or policy](#ex-iam-entity-create-col)
+ [Update IAM entity or policy](#ex-iam-entity-update-col)
+ [Delete IAM entity or policy](#ex-iam-entity-delete-col)
+ [Update detailed monitoring](#ex-ec2-update-detailed-mon-col)
+ [Share directory](#ex-dirserv-dir-share-col)
+ [Unshare directory](#ex-dirserv-dir-unshare-col)
+ [Create VPC endpoint](#ex-vpc-interface-create-col)
+ [Update RDS storage](#ex-rds-update-storage-col)
+ [Update an RDS multi-AZ deployment](#ex-rds-update-multi-az-col)
+ [Update an RDS instance type](#ex-rds-update-instance-type-col)
+ [Update S3 bucket versioning](#ex-s3-update-versioning-col)
+ [Update S3 bucket encryption](#ex-s3-update-encryption-col)
+ [Updating an application account (Managed Automation)](#ex-man-lz-app-acct-update-rr-col)
+ [Associate private IP addresses (Managed Automation) ct-1pvlhug439gl2](#ex-ec2-associate-ip-rr-col)
+ [Create Amazon RDS option group (Managed Automation)](#ex-rds-create-option-group-rr-col)
+ [Remove TGW static route](#ex-man-lz-net-acct-tgw-route-remove-col)
+ [Create for WIGS (Managed Automation)](#ex-ec2-create-preingest-col)
+ [Modify EBS volume](#ex-ebs-modify-col)
+ [Update AWS Backup plan (Managed Automation)](#ex-backup-backup-plan-update-col)
+ [Confirm offboarding](#ex-man-lz-app-acct-confirm-offb-col)
+ [Management account: Offboard Application account](#ex-man-lz-man-acct-offb-app-acct-col)
+ [Deploy AMS Resource Scheduler Solution](#ex-res-sched-deploy-col)
+ [Update AMS Resource Scheduler Solution](#ex-res-sched-update-col)
+ [Delete or deactivate access key](#ex-iam-key-deactivate-col)
+ [Create access key](#ex-iam-key-create-col)
+ [Enable Detailed Monitoring](#ex-ec2-enable-detail-mon-rr-col)
+ [Update the DeleteOnTermination option (Managed Automation)](#ex-ec2-update-termination-col)
+ [Update RDS maintainance window (Managed Automation)](#ex-rds-update-window-col)
+ [Update RDS performance insights (Managed Automation)](#ex-rds-update-insights-col)
+ [Create security group (Managed Automation)](#ex-sec-group-create-rr-col)

## Create a managed prefix list
<a name="ex-vpc-prefix-list-create-col"></a>

### Creating a managed prefix list with the console
<a name="vpc-prefix-list-create-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Create managed prefix list change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcPrefixListCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a managed prefix list with the CLI
<a name="vpc-prefix-list-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1bw3q0obl5y75" --change-type-version "1.0" --title "AWSManagedServices-CreatePrefixList" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-CreatePrefixList\",\"Region\":\"{{ap-southeast-1}}\",\"Parameters\":{\"PrefixListName\":[\"{{newprefix_list_2}}\"],\"MaxEntries\":[{{4}}],\"AddressFamily\":[\"{{IPv4}}\"],\"CIDRBlockIPv4\":[{\"Cidr\":\"{{10.0.0.0/16}}\",\"Description\":\"{{Value_1}}\"},{\"Cidr\":\"{{192.168.1.0/24}}\",\"Description\":\"{{networking item}}\"}]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it CreatePrefixListParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1bw3q0obl5y75" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreatePrefixListParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-CreatePrefixList",
     "Region": "{{ap-southeast-1}}",
     "Parameters": {
       "PrefixListName": ["{{newprefix_list_2}}"],
       "MaxEntries": [{{4}}],
       "AddressFamily": ["{{IPv4}}"],
       "CIDRBlockIPv4": [
         {"Cidr": "{{10.0.0.0/16}}", "Description": "{{Value_1}}"},
         {"Cidr": "{{192.168.1.0/24}}", "Description": "{{networking item}}"}
       ]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it CreatePrefixListRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreatePrefixListRfc.json
   ```

1. Modify and save the CreatePrefixListRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-1bw3q0obl5y75",
     "Title" : "{{Create managed prefix list}}"
   }
   ```

1. Create the RFC, specifying the CreatePrefixListRfc file and the CreatePrefixListParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreatePrefixListRfc.json  --execution-parameters file://CreatePrefixListParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Delete a managed prefix list
<a name="ex-vpc-prefix-list-delete-col"></a>

### Deleting a managed prefix list with the console
<a name="vpc-prefix-list-delete-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Delete managed prefix list change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcPrefixListDeleteCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting a managed prefix list with the CLI
<a name="vpc-prefix-list-delete-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3fh88p7t5k5gi" --change-type-version "1.0" --title "AWSManagedServices-DeletePrefixList" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-DeletePrefixList\",\"Region\":\"{{ap-southeast-1}}\",\"Parameters\":{\"PrefixListId\":[\"{{pl-0b6430edc53fc274c}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it DeletePrefixListParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3fh88p7t5k5gi" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeletePrefixListParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-DeletePrefixList",
     "Region": "{{ap-southeast-1}}",
     "Parameters": {
       "PrefixListId": ["{{pl-0b6430edc53fc274c}}"]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it DeletePrefixListRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeletePrefixListRfc.json
   ```

1. Modify and save the DeletePrefixListRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-3fh88p7t5k5gi",
     "Title" : "{{Delete managed prefix list}}"
   }
   ```

1. Create the RFC, specifying the DeletePrefixListRfc file and the DeletePrefixListParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeletePrefixListRfc.json  --execution-parameters file://DeletePrefixListParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Modify a managed prefix list
<a name="ex-vpc-prefix-list-modify-col"></a>

### Modifying a managed prefix list with the console
<a name="vpc-prefix-list-modify-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Modify managed prefix list change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcPrefixListModifyCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Modifying a managed prefix list with the CLI
<a name="vpc-prefix-list-modify-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2s1q5tjl0416n" --change-type-version "1.0" --title "AWSManagedServices-ModifyPrefixList" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-ModifyPrefixList\",\"Region\":\"{{ap-southeast-1}}\",\"Parameters\":{\"PrefixListId\":[\"{{pl-03d7a44509b1be33f}}\"],\"AddCIDRBlock\":[{\"Cidr\":\"{{10.0.1.0/24}}\",\"Description\":\"{{Value}}\"},{\"Cidr\":\"{{10.0.2.0/24}}\",\"Description\":\"{{new networking team}}\"}],\"RemoveCIDRBlock\":[\"{{10.0.0.0/24}}\"],\"AddTags\":[{\"Key\":\"{{name_2}}\",\"Value\":\"{{value_2}}\"}],\"RemoveTags\":[\"{{Name}}\",\"{{env}}\"],\"ResizeMaxEntries\":[{{0}}]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it ModifyPrefixListParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2s1q5tjl0416n" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ModifyPrefixListParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-ModifyPrefixList",
     "Region": "{{ap-southeast-1}}",
     "Parameters": {
       "PrefixListId": ["{{pl-03d7a44509b1be33f}}"],
       "AddCIDRBlock": [
         {"Cidr": "{{10.0.1.0/24}}", "Description": "{{Value}}"},
         {"Cidr": "{{10.0.2.0/24}}", "Description": "{{new networking team}}"}
       ],
       "RemoveCIDRBlock": ["{{10.0.0.0/24}}"],
       "AddTags": [{"Key": "{{name_2}}", "Value": "{{value_2}}"}],
       "RemoveTags": ["{{Name}}", "{{env}}"],
       "ResizeMaxEntries": [{{0}}]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it ModifyPrefixListRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ModifyPrefixListRfc.json
   ```

1. Modify and save the ModifyPrefixListRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-2s1q5tjl0416n",
     "Title" : "{{Modify managed prefix list}}"
   }
   ```

1. Create the RFC, specifying the ModifyPrefixListRfc file and the ModifyPrefixListParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ModifyPrefixListRfc.json  --execution-parameters file://ModifyPrefixListParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Create Resource Share
<a name="ex-ram-resource-share-create-col"></a>

### Creating a Resource Share with the console
<a name="ram-resource-share-create-con"></a>

The following shows this change type in the AMS console.

![Create Resource Share page showing ID, execution mode as Manual, version 1.0, and classification path.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiCreateResourceShareCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating an AWS RAM AMS Resource Share with the CLI
<a name="ram-resource-share-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc \
  --change-type-id "ct-054ysptoo4gyk" \
  --change-type-version "1.0" \
  --title "{{Create resource share (managed automation)}}" \
  --execution-parameters "{
    "Region": "{{us-east-1}}",
    "ResourceShareName": "{{MyResourceShare}}",
    "Resources": [
      "{{arn:aws:ec2:us-east-1:123456789012:vpc/vpc-12345}}"
    ],
    "Principals": [
      "{{111122223333}}"
    ],
    "AllowExternalPrincipals": true,
    "Priority": "{{Medium}}"
  }"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it CreateResourceShareParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-054ysptoo4gyk" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateResourceShareParams.json
   ```

1. Modify and save the CreateResourceShareParams file.

   ```
   {
     "Region": "{{us-east-1}}",
     "ResourceShareName": "{{MyResourceShare}}",
     "Resources": [
       "{{arn:aws:ec2:us-east-1:123456789012:vpc/vpc-12345}}"
     ],
     "Principals": [
       "{{111122223333}}"
     ],
     "AllowExternalPrincipals": true,
     "PermissionArns": [
       "{{arn:aws:ram::aws:permission/AWSRAMDefaultPermissionVpc}}"
     ],
     "Tags": [
       {
         "Key": "{{Environment}}",
         "Value": "{{Production}}"
       },
       {
         "Key": "{{{{Owner}}}}",
         "Value": "{{TeamName}}"
       }
     ],
     "Priority": "{{Medium}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateResourceShareRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateRsourceShareRfc.json
   ```

1. Modify and save the CreateResourceShareRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-054ysptoo4gyk",
     "Title": "{{Create resource share}}"
   }
   ```

1. Create the RFC, specifying the CreateResourceShareRfc file and the CreateResourceShareParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateResourceShareRfc.json --execution-parameters file://CreateResourceShareParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ram-resource-share-create-tip"></a>

## Delete ELB Listener Rule
<a name="ex-load-balancer-delete-elb-listener-rule-col"></a>

### Deleting an ELB listener rule with the console
<a name="load-balancer-delete-elb-listener-rule-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Delete ELB listener rule change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiLoadBalancerDeleteElbListenerRuleCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting an ELB listener rule with the CLI
<a name="load-balancer-delete-elb-listener-rule-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2qsgbfmrw92zw" --change-type-version "1.0" --title "Delete ALB Listener Rule" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-DeleteListenerRule\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"ListenerRuleArn\":[\"{{arn:aws:elasticloadbalancing:us-east-1:123456789012:listener-rule/app/my_alb/abc01234abc01234/abc01234abc01234/abc01234abc01234}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it DeleteListenerRuleParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2qsgbfmrw92zw" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteListenerRuleParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-DeleteListenerRule",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "ListenerRuleArn": ["{{arn:aws:elasticloadbalancing:us-east-1:123456789012:listener-rule/app/my_alb/abc01234abc01234/abc01234abc01234/abc01234abc01234}}"]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it DeleteListenerRuleRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteListenerRuleRfc.json
   ```

1. Modify and save the DeleteListenerRuleRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-2qsgbfmrw92zw",
     "Title" : "{{Delete ALB Listener Rule}}"
   }
   ```

1. Create the RFC, specifying the DeleteListenerRuleRfc file and the DeleteListenerRuleParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteListenerRuleRfc.json  --execution-parameters file://DeleteListenerRuleParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Associate DHCP option set
<a name="ex-vpc-associate-dhcp-option-set-col"></a>

### Associating a DHCP option set with the console
<a name="vpc-associate-dhcp-option-set-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Associate DHCP option set change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcAssociateDhcpOptionSetCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Associating a DHCP option set with the CLI
<a name="vpc-associate-dhcp-option-set-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0c2g2npbyyrny" --change-type-version "1.0" --title "Associate DHCP Option Set" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-AssociateDhcpOptionSetWithVpc\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"VPCId\":\"{{vpc-1234abcd}}\",\"DHCPOptionsId\":\"{{dopt-1234abcd}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it AssociateDhcpOptionSetParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0c2g2npbyyrny" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AssociateDhcpOptionSetParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-AssociateDhcpOptionSetWithVpc",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "VPCId": "{{vpc-1234abcd}}",
       "DHCPOptionsId": "{{dopt-1234abcd}}"
     }
   }
   ```

1. Output the RFC template JSON file; this example names it AssociateDhcpOptionSetRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > AssociateDhcpOptionSetRfc.json
   ```

1. Modify and save the AssociateDhcpOptionSetRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-0c2g2npbyyrny",
     "Title" : "{{Associate DHCP Option Set}}"
   }
   ```

1. Create the RFC, specifying the AssociateDhcpOptionSetRfc file and the AssociateDhcpOptionSetParams file:

   ```
   aws amscm create-rfc --cli-input-json file://AssociateDhcpOptionSetRfc.json  --execution-parameters file://AssociateDhcpOptionSetParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Manage network firewall rules (managed automation)
<a name="ex-man-fw-network-fw-manage-fw-rules-col"></a>

### Managing network firewall rules (managed automation) with the Console
<a name="man-fw-network-fw-manage-fw-rules-con"></a>

Screenshot of this change type in the AMS console:

![Manage Network Firewall Rules change type showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiManageNetworkFirewallRulesCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Managing network firewall rules (managed automation) with the CLI
<a name="man-fw-network-fw-manage-fw-rules-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2lo1hs6ks7chl" --change-type-version "{{1.0}}" --title "{{Manage Network Firewall Rules}}" --execution-parameters "{\"SourceIP\": \"{{192.168.1.0/24}}\", \"Destination\": \"{{example.com}}\", \"Protocol\": \"{{TCP}}\", \"Port\": {{443}}, \"Action\": \"{{Allow}}\", \"RuleName\": \"{{allow-https-traffic}}\", \"Operation\": \"{{Create}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ManageFirewallRulesParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-2lo1hs6ks7chl" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ManageFirewallRulesParams.json
   ```

1. Modify and save the ManageFirewallRulesParams file. For example, you can replace the contents with something like this:

   ```
   {
   "SourceIP": "{{192.168.1.0/24}}",
   "Destination": "{{example.com}}",
   "Protocol": "{{TCP}}",
   "Port": {{443}},
   "Action": "{{Allow}}",
   "RuleName": "{{allow-https-traffic}}",
   "Operation": "{{Create}}",
   "DryRun": {{false}}
   }
   ```

1. Output the RFC template JSON file to a file named ManageFirewallRulesRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ManageFirewallRulesRfc.json
   ```

1. Modify and save the ManageFirewallRulesRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-2lo1hs6ks7chl",
   "Title":                "{{Manage-Network-Firewall-Rules-RFC}}"
   }
   ```

1. Create the RFC, specifying the ManageFirewallRulesRfc file and the ManageFirewallRulesParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ManageFirewallRulesRfc.json  --execution-parameters file://ManageFirewallRulesParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-man-fw-network-fw-manage-fw-rules-tip"></a>
+ Use the `DryRun` parameter set to `true` to validate your request without making changes.
+ The `Operation` parameter supports Create, Read, Update, and Delete actions on Network Firewall rules.

## Remediate DNS scavenging issue
<a name="ex-dirserv-dns-scavenging-remediate-col"></a>

### Remediating DNS scavenging issue with the console
<a name="dirserv-dns-scavenging-remediate-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Remediate DNS scavenging issue change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiDirservDnsScavengingRemediateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Remediating DNS scavenging issue with the CLI
<a name="dirserv-dns-scavenging-remediate-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3k67klld7cimj" --change-type-version "1.0" --title "Remediate DNS scavenging issue" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateClusterNodeRecordPermissions-Admin\",\"Parameters\":{\"ClusterCNOName\":[\"{{CLUSTER_CNO_NAME}}\"],\"ClusterNodeComputerNames\":[\"{{NODE_NAME_1}}\",\"{{NODE_NAME_2}}\"],\"ClusterVCONames\":[\"{{VCO_NAME_1}}\",\"{{VCO_NAME_2}}\"]},\"Region\":\"{{us-east-1}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it RemediateDnsScavengingParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3k67klld7cimj" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > RemediateDnsScavengingParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateClusterNodeRecordPermissions-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "ClusterCNOName": ["{{CLUSTER_CNO_NAME}}"],
       "ClusterNodeComputerNames": ["{{NODE_NAME_1}}", "{{NODE_NAME_2}}"],
       "ClusterVCONames": ["{{VCO_NAME_1}}", "{{VCO_NAME_2}}"]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it RemediateDnsScavengingRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > RemediateDnsScavengingRfc.json
   ```

1. Modify and save the RemediateDnsScavengingRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-3k67klld7cimj",
     "Title" : "{{Remediate DNS scavenging issue}}"
   }
   ```

1. Create the RFC, specifying the RemediateDnsScavengingRfc file and the RemediateDnsScavengingParams file:

   ```
   aws amscm create-rfc --cli-input-json file://RemediateDnsScavengingRfc.json  --execution-parameters file://RemediateDnsScavengingParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Delete VPC route
<a name="ex-vpc-route-delete-col"></a>

### Deleting a VPC route with the console
<a name="vpc-route-delete-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Delete VPC route change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcRouteDeleteCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting a VPC route with the CLI
<a name="vpc-route-delete-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1nusoameibz5p" --change-type-version "1.0" --title "Delete VPC route" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-DeleteRoute\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"RouteTableId\":\"{{rtb-1234abcd12345abcd}}\",\"DestinationCidrBlock\":\"{{10.0.0.0/8}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it DeleteVPCRouteParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1nusoameibz5p" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteVPCRouteParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-DeleteRoute",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "RouteTableId": "{{rtb-1234abcd12345abcd}}",
       "DestinationCidrBlock": "{{10.0.0.0/8}}",
       "DestinationPrefixListId": "{{pl-abcd1234}}"
     }
   }
   ```

1. Output the RFC template JSON file; this example names it DeleteVPCRouteRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteVPCRouteRfc.json
   ```

1. Modify and save the DeleteVPCRouteRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-1nusoameibz5p",
     "Title" : "{{Delete VPC route}}"
   }
   ```

1. Create the RFC, specifying the DeleteVPCRouteRfc file and the DeleteVPCRouteParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteVPCRouteRfc.json  --execution-parameters file://DeleteVPCRouteParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Update parameter group of DB instance or cluster
<a name="ex-rds-db-parameter-group-update-col"></a>

### Updating a parameter group of DB instance or cluster with the console
<a name="rds-db-parameter-group-update-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Update Parameter Group of DB instance or cluster change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsDbParameterGroupUpdateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating a parameter group of DB instance or cluster with the CLI
<a name="rds-db-parameter-group-update-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0p1oqt4xcp1cv" --change-type-version "1.0" --title "Change Parameter Group" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateDBParameterGroup\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"DBArn\":\"{{arn:aws:rds:us-east-1:945533541580:db:database-1}}\",\"ParameterGroupName\":\"{{minlz-parameter-group-mysql}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it UpdateDBParameterGroupParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0p1oqt4xcp1cv" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateDBParameterGroupParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateDBParameterGroup",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "DBArn": "{{arn:aws:rds:us-east-1:945533541580:db:database-1}}",
       "ParameterGroupName": "{{minlz-parameter-group-mysql}}"
     }
   }
   ```

1. Output the RFC template JSON file; this example names it UpdateDBParameterGroupRFC.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateDBParameterGroupRFC.json
   ```

1. Modify and save the UpdateDBParameterGroupRFC.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-0p1oqt4xcp1cv",
     "Title" : "{{Change Parameter Group}}"
   }
   ```

1. Create the RFC, specifying the UpdateDBParameterGroupRFC file and the UpdateDBParameterGroupParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateDBParameterGroupRFC.json  --execution-parameters file://UpdateDBParameterGroupParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Replace Site-to-Site VPN tunnel
<a name="ex-vpn-s2s-tunnel-replace-col"></a>

### Replacing a Site-to-Site VPN tunnel with the console
<a name="vpn-s2s-tunnel-replace-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Replace Site-to-Site VPN tunnel change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpnS2sTunnelReplaceCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Replacing a Site-to-Site VPN tunnel with the CLI
<a name="vpn-s2s-tunnel-replace-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2sav5hzk5twk4" --change-type-version "1.0" --title "Replace S2S VPN Tunnel" --execution-parameters "{\"Region\":\"{{us-east-1}}\",\"VpnId\":\"{{vpn-01234567890abcdef}}\",\"VpnTunnelOutsideIpAddress\":\"{{203.0.113.1}}\",\"ApplyPendingMaintenance\": {{true}},\"Priority\":\"{{High}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it ReplaceS2SVpnTunnelParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2sav5hzk5twk4" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ReplaceS2SVpnTunnelParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "Region": "{{us-east-1}}",
     "VpnId": "{{vpn-01234567890abcdef}}",
     "VpnTunnelOutsideIpAddress": "{{203.0.113.1}}",
     "ApplyPendingMaintenance": {{true}},
     "Priority": "{{High}}"
   }
   ```

1. Output the RFC template JSON file; this example names it ReplaceS2SVpnTunnelRFC.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ReplaceS2SVpnTunnelRFC.json
   ```

1. Modify and save the ReplaceS2SVpnTunnelRFC.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-2sav5hzk5twk4",
     "Title": "{{Replace S2S VPN Tunnel}}"
   }
   ```

1. Create the RFC, specifying the ReplaceS2SVpnTunnelRFC file and the ReplaceS2SVpnTunnelParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ReplaceS2SVpnTunnelRFC.json --execution-parameters file://ReplaceS2SVpnTunnelParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Create a DHCP option set
<a name="ex-vpc-create-dhcp-option-set-col"></a>

### Create a DHCP option set with the console
<a name="vpc-create-dhcp-option-set-con"></a>

The following shows this change type in the AMS console.

![Create DHCP option set interface showing ID, execution mode as Automated, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiCreateDHCPOptionSetCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a DHCP option set with the CLI
<a name="vpc-create-dhcp-option-set-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-18rsjua1zosvo" --change-type-version "1.0" --title "{{AWSManagedServices-CreateDhcpOptionSet}}" --execution-parameters "{\"DocumentName\": \"{{AWSManagedServices-CreateDhcpOptionSet}}\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"DomainName\": \"{{example.com}}\",\"DomainNameServers\": [\"{{1.2.3.4\}}"],\"NtpServers\": [\"{{4.5.6.7\}}"],\"NetBiosNameServers\": [\"{{3.4.5.6\}}"],\"NetBiosNodeType\": \"{{1}}\",\"{{Ipv6AddressPreferredLeaseTime}}\": \"{{140}}\",\"DhcpOptionSetName\": \"{{optionsetname}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it CreateDhcpOptionSetParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-18rsjua1zosvo" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDhcpOptionSetParams.json
   ```

1. Modify and save the execution CreateDhcpOptionSetParams.json file. For example, you can replace the contents with something like this:

   ```
   {
   "DomainName": "{{example.com}}",
   "DomainNameServers": [
   "{{1.2.3.4}}"
   ],
   "NtpServers": [
   "{{4.5.6.7}}"
   ],
   "NetBiosNameServers": [
   "{{3.4.5.6}}"
   ],
   "NetBiosNodeType": "{{1}}",
   "Ipv6AddressPreferredLeaseTime": "{{140}}",
   "DhcpOptionSetName": "{{optionsetname}}"
   "Priority": "{{Medium}}"
   }
   ```

1. Output the RFC template JSON file; this example names it CreateDhcpOptionSet.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateDhcpOptionSet.json
   ```

1. Modify and save the CreateDhcpOptionSet.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-18rsjua1zosvo",
   "Title": "{{Create Dhcp Option Set}}"
   }
   ```

1. Create the RFC, specifying the CreateDhcpOptionSet file and the CreateDhcpOptionSetParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateDhcpOptionSet.json --execution-parameters file://CreateDhcpOptionSetParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-vpc-create-dhcp-option-set-tip"></a>

For information about VPCs, see [Virtual private clouds (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html).

## Create ELB Listener Rule
<a name="ex-load-balancer-create-elb-listener-rule-col"></a>

### Creating ELB Listener Rule with the Console
<a name="load-balancer-create-elb-listener-rule-con"></a>

Screenshot of this change type in the AMS console:

![AMS Advanced console, create RFC section, change type details box for ct-18weo4vv83ynk: Create ELB Listener Rule.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiLoadBalancerCreateELBListenerRule.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating ELB Listener Rule with the CLI
<a name="load-balancer-create-elb-listener-rule-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-18weo4vv83ynk" --change-type-version "1.0" --title "Create ALB Listener Rule" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-CreateListenerRule\",\"Parameters\":{\"ListenerArn\":[\"{{LISTENER_ARN}}\"],\"Conditions\":[\"{\\\"{{Field}}\\\":\\\"{{path-pattern}}\\\",\\\"{{PathPatternConfig}}\\\":{\\\"{{Values}}\\\":[\\\"/{{img}}/*\\\"]}}\"],\"RuleType\":[\"{{redirect}}\"],\"Priority\":[\"{{200}}\"],\"TargetGroups\":[\"{{{}}}\"],\"TargetGroupStickinessConfig\":[\"{{\}}"],\"TargetGroupStickinessDuration\":[\"{{\}}"],\"RedirectProtocol\":[\"{{HTTP}}\"],\"RedirectPort\":[\"{{85}}\"],\"RedirectHost\":[\"{{www.example.com}}\"],\"RedirectPath\":[\"/{{new-path}}\"],\"RedirectQuery\":[\"{{page1}}\"],\"RedirectStatusCode\":[\"{{HTTP_301}}\"]},\"Region\":\"{{REGION}}\""}"
```

```
aws amscm create-rfc --change-type-id "ct-18weo4vv83ynk" --change-type-version "1.0" --title "Create ALB Listener Rule" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-CreateListenerRule\",\"Parameters\":{\"ListenerArn\":[\"{{LISTENER_ARN}}\"],\"Conditions\":[\"{\\\"{{Field}}\\\":\\\"{{path-pattern}}\\\",\\\"{{PathPatternConfig}}\\\":{\\\"{{Values}}\\\":[\\\"/{{img}}/*\\\"]}}\"],\"RuleType\":[\"{{forward}}\"],\"Priority\":[\"{{125}}\"],\"TargetGroups\":[\"{\\\"{{TargetGroupArn}}\\\":\\\"{{TARGET_GROUP_ARN}}\\\",\\\"{{Weight}}\\\":\\\"{{20}}\\\"}\"],\"TargetGroupStickinessConfig\":[\"{{Enabled}}\"],\"TargetGroupStickinessDuration\":[\"{{15}}\"],\"RedirectProtocol\":[\"{{\}}"],\"RedirectPort\":[\"{{\}}"],\"RedirectHost\":[\"{{\}}"],\"RedirectPath\":[\"{{\}}"],\"RedirectQuery\":[\"{{\}}"],\"RedirectStatusCode\":[\"{{\}}"]},\"Region\":\"{{REGION}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named validateCreateRule.Actions.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-18weo4vv83ynk" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > validateCreateRule.Actions.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   All parameters example:

   ```
   {
   "DocumentName": "AWSManagedServices-CreateListenerRule",
   "Region": "{{us-west-2}}",
   "Parameters": {
     "ListenerArn": ["{{LISTENER_ARN}}"],
     "Conditions": ["{\"{{Field}}\":\"{{host-header}}\",\"{{HostHeaderConfig}}\":{\"{{Values}}\":[\"{{example.com}}\"]}}"],
     "RuleType": ["{{forward}}"],
     "Priority": ["{{200}}"],
     "TargetGroups": ["{\"{{TargetGroupArn}}\":\"{{TARGET_GROUP_ARN}}\",\"{{Weight}}\":\"{{100}}\"}"],
     "TargetGroupStickinessConfig": ["{{Enabled}}"],
     "TargetGroupStickinessDuration": ["{{86400}}"],
     "RedirectProtocol": [""],
     "RedirectPort": [""],
     "RedirectHost": [""],
     "RedirectPath": [""],
     "RedirectQuery": [""],
     "RedirectStatusCode": [""],
     "Priority": "{{High}}"
   }
   }
   ```

   ```
   {
   "DocumentName": "AWSManagedServices-CreateListenerRule",
   "Parameters": {
     "ListenerArn": [
       "{{LISTENER_ARN}}"
     ],
     "Conditions": [
       "{\"{{Field}}\":\"{{path-pattern}}\",\"{{PathPatternConfig}}\":{\"{{Values}}\":[\"/{{img}}/*\"]}}"
     ],
     "RuleType": [
       "{{forward}}"
     ],
     "Priority": [
       "{{125}}"
     ],
     "TargetGroups": [
       "{\"{{TargetGroupArn}}\":\"{{TARGET_GROUP_ARN}}\",\"{{Weight}}\":\"{{20}}\"}"
     ],
     "TargetGroupStickinessConfig": [
       "{{Enabled}}"
     ],
     "TargetGroupStickinessDuration": [
       "{{15}}"
     ],
     "RedirectProtocol": [
       ""
     ],
     "RedirectPort": [
       ""
     ],
     "RedirectHost": [
       ""
     ],
     "RedirectPath": [
       ""
     ],
     "RedirectQuery": [
       ""
     ],
     "RedirectStatusCode": [
       ""
     ]
   },
   "Region": "{{REGION}}",
   "Priority": "{{High}}"
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it CreateListenerRuleRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateListenerRuleRfc.json
   ```

1. Modify and save the CreateListenerRuleRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "{{1.0}}",
   "ChangeTypeId": "ct-18weo4vv83ynk",
   "Title": "{{Create ALB Listener Rule}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the validateCreateRule file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateListenerRuleRfc.json  --execution-parameters file://validateCreateRule.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-load-balancer-create-elb-listener-rule-tip"></a>

To learn more about AWS Application Load Balancers, see [What Is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

## Update VPC Endpoint Policy
<a name="ex-vpc-endpoint-update-policy-col"></a>

### Updating a VPC Endpoint Policy
<a name="vpc-endpoint-update-policy"></a>

The following shows this change type in the AMS console.

![Update VPC Endpoint Policy change type details showing ID, execution mode, and version fields.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcEndpointUpdatePolicyCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating a VPC Endpoint Policy with the CLI
<a name="vpc-endpoint-update-policy-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-128mp7mbxobd0" --change-type-version "1.0" --title "Update VPC Endpoint Policy" --execution-parameters "{\"Region\":\"{{us-east-1}}\",\"VpcEndpointId\":\"{{vpce-1a2b3c4d5e6f7g8h9}}\",\"PolicyDocument\":\"{{Example endpoint policy}}\",\"PolicyAction\":\"{{Append}}\",\"Priority\":\"{{High}}\"}
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it UpdateVPCEndpointPolicyParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-128mp7mbxobd0" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateVPCEndpointPolicyParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
   "Region": "{{us-east-1}}",
   "VpcEndpointId": "{{vpce-1a2b3c4d5e6f7g8h9}}",
   "PolicyDocument":"{{Example endpoint policy}}"
   "PolicyAction" : "{{Append}}",
   "Priority": "{{High}}"
   }
   ```

1. Output the RFC template JSON file; this example names it UpdateVPCEndpointPolicyRFC.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateVPCEndpointPolicyRFC.json
   ```

1. Modify and save the UpdateVPCEndpointPolicyRFC.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-128mp7mbxobd0",
   "Title": "{{Update VPC Endpoint Policy}}"
   }
   ```

1. Create the RFC, specifying the UpdateVPCEndpointPolicyRFC file and the UpdateVPCEndpointPolicyParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateVPCEndpointPolicyRFC.json --execution-parameters file://UpdateVPCEndpointPolicyParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-vpc-endpoint-update-policy-tip"></a>

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

## Delete NAT gateway (Managed Automation)
<a name="ex-nat-gateway-delete-rr-col"></a>

This operation requires manual review and approval before its completed successfully.

### Deleting NAT gateway (Managed Automation)
<a name="ex-nat-gateway-delete-rr-con"></a>

![Delete NAT gateway request details showing manual execution mode and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/ex-nat-gateway-delete-rr.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting NAT gateways with the CLI (Managed Automation)
<a name="ebs-snpsht-delete-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1rexstryxye1b" --change-type-version "1.0" --title "Delete NAT Gateway" --execution-parameters "{\"Region\":\"{{us-east-1}}\",\"NatGatewayId\":[\"nat-{{1234567890abcdef0}}\"],\"Priority\":\"{{High}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema to a file in your current folder. This example names it DeleteNATGatewayParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1rexstryxye1b" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteNATGatewayParams.json
   ```

1. Modify and save the DeleteNATGatewayParams.json file. For example, you can replace the contents with something like this:

   ```
   {
   "Region": "{{us-west-1}}",
   "NatGatewayId": "{{nat-1234567890abcdef0}}"
   "Priority": "{{High}}"
   }
   ```

1. Output the RFC template to a file in your current folder. This example names it DeleteNATGatewayRfc.json.

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteNATGatewayRfc.json
   ```

1. Modify and save the DeleteNATGatewayRfc.json file.

   The internal quotation marks in the `ExecutionParameters` JSON extension must be escaped with a backslash (\\). Example:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-1rexstryxye1b",
   "Title": "{{Delete-NAT-Gateway}}"
   }
   ```

1. Create the RFC:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteNATGatewayRfc.json  --execution-parameters file://DeleteNATGatewayParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-nat-gateway-delete-rr-tip"></a>

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

## Update EC2 Instance Metadata Service (IMDS) Region Setting
<a name="ex-ec2-imds-region-update-col"></a>

### Updating EC2 instance IMDS region setting with the console
<a name="ec2-update-imds-region-con"></a>

The following shows this change type in the AMS console.

![Update IMDS Region-Level Default Settings change type details in the AMS console.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEc2ImdsRegionUpdateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating EC2 instance IMDS region setting with the CLI
<a name="ec2-update-imds-region-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2o1knqxw39mkc" --change-type-version "1.0" --title "{{Update IMDS region-level default settings}}" --execution-parameters "{\"Region\":\"{{us-west-2}}\",\"HttpEndpoint\":\"{{Enabled}}\",\"HttpTokens\":\"{{Required}}\",\"InstanceMetadataTags\":\"{{Enabled}}\",\"HttpPutResponseHopLimit\":{{1}},\"Priority\":\"{{High}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it UPdateEC2ImdsRegionParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2o1knqxw39mkc" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateEC2ImdsRegionParams.json
   ```

1. Modify and save the UPdateEC2ImdsRegionParams file, retaining only the parameters that you want to change. For example, you can replace the contents with something like this: 

   ```
   {
   "Region": "{{us-west-2}}",
   "HttpEndpoint": "{{Enabled}}",
   "HttpTokens":"{{Required}}"
   "InstanceMetadataTags" : "{{Enabled}}",
   "HttpPutResponseHopLimit": {{1}},
   "Priority": "{{High}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it UPdateEC2ImdsRegionRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UPdateEC2ImdsRegionRfc.json
   ```

1. Modify and save the UPdateEC2ImdsRegionRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-2o1knqxw39mkc",
   "Title": "{{Update IMDS region-level default settings}}"
   }
   ```

1. Create the RFC, specifying the UPdateEC2ImdsRegionRfc file and the UPdateEC2ImdsRegionParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UPdateEC2ImdsRegionRfc.json  --execution-parameters file://UPdateEC2ImdsRegionParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ec2-update-imds-region-tip"></a>

You can set default values for the instance metadata options at the account level for each AWS Region. When an instance is launched, the instance metadata options are automatically set to the account-level values. You can change these values at launch. Account-level default values do not affect existing instances. For more information about Amazon EC2 IMDS settings, see [ Where to configure instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#where-to-configure-instance-metadata-options)

## Create a computer object's SPN
<a name="ex-dirserv-comp-object-spn-create-col"></a>

### Creating a computer object's SPN from an AMS-managed AD with the console
<a name="dirserv-comp-object-create-spn-con"></a>

The following shows this change type in the AMS console.

![Create service principal names change type showing ID, execution mode, version, and classification details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiDirservCompObjectSpnCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a computer object's SPN from an AMS-managed AD with the CLI
<a name="dirserv-comp-object-create-spn-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0ulaleq7ohuyq" --change-type-version "1.0" --title "{{Create service principal names}}" --execution-parameters "{ \"DocumentName\": \"AWSManagedServices-CreateADSPN-Admin\", \"Region\": \"{{us-east-1}}\", \"Parameters\": { \"ServiceType\": \"{{MSSQLSvc}}\", \"Hostnames\": \"{{server1,server2}}\", \"ServiceAccountName\": \"{{gmsa_sql}}\" } }"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ComputerObjectCreateSpnParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0ulaleq7ohuyq" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ComputerObjectCreateSpnParams.json
   ```

   Modify and save the ComputerObjectCreateSpnParams file. For example, you can replace the contents with something like this:

   ```
   {
       "DocumentName": "AWSManagedServices-CreateADSPN-Admin",
       "Region": "{{us-east-1}}",
       "Parameters": {
         "ServiceType": ["{{HOST}}"],
         "Hostnames": "{{server1}}",
         "ServiceAccountName": "{{gmsa_host}}",
         "Port": ["{{1433}}"],
         "ApplicationAccountId": "{{123456789012}}"
       }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it ComputerObjectCreateSpnRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ComputerObjectCreateSpnRfc.json
   ```

1. Modify and save the ComputerObjectCreateSpnRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-0ulaleq7ohuyq",
   "Title": "Create service principal names"
   }
   ```

1. Create the RFC, specifying the ComputerObjectCreateSpnRfc file and the ComputerObjectCreateSpnParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ComputerObjectCreateSpnRfc.json --execution-parameters file://ComputerObjectCreateSpnParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-dirserv-comp-object-create-spn-tip"></a>
+ For multi-account landing zone (MALZ), use this change type in the shared services account.
+ For information about Directory Service, see the [Directory Service Admin Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html).

## Delete target groups (Managed Automation)
<a name="ex-tar-group-delete-rr-col"></a>

### Delete a Target Group with the Console
<a name="tar-group-delete-con"></a>

Screenshot of this change type in the AMS console:

![Delete Target Group page showing execution mode, version, classification path, and description.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiTargetGroupDeleteCT.png)


**Note**  
When using manual CTs, AMS recommends that you use the ASAP **Scheduling** option (choose **ASAP** in the console, leave start and end time blank in the API/CLI) as these CTs require an AMS operator to examine the RFC, and possibly communicate with you before it can be approved and run. If you schedule these RFCs, be sure to allow at least 24 hours. If approval does not happen before the scheduled start time, the RFC is rejected automatically.

How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Delete a Target Group with the CLI
<a name="tar-group-delete-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0akjahmgqhu4u" --change-type-version "1.0" --title "{{Delete Target Group}}" --execution-parameters "{\"Region\":\"{{us-west-2}}\",\"TargetGroupArns\":[\"{{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067}}\"],\"Priority\":\"{{High}}\"}"
```

TEMPLATE CREATE:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it TgDeleteParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-0akjahmgqhu4u" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > TgDeleteParams.json
   ```

1. Modify and save the TgDeleteParams file. For example, you can replace the contents with something like this:

   ```
   {
   "Region": "{{us-west-2}}",
   "TargetGroupArns": "{{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067}}"
   "Priority": "{{High}}"
   }
   ```

1. Output the RFC template to a file in your current folder named TgDeleteRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > TgDeleteRfc.json
   ```

1. Modify and save the TgDeleteRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-0akjahmgqhu4u",
   "Title": "{{Delete Target Group}}"
   }
   ```

1. Create the RFC, specifying the TgDeleteRfc file and the TgDeleteParams file:

   ```
   aws amscm create-rfc --cli-input-json file://TgDeleteRfc.json --execution-parameters file://TgDeleteParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-tar-group-delete-tip"></a>

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.
+ Deleting a target group also deletes any associated health checks.
+ Deleting a target group does not affect its registered targets.
+ For information about target groups, see [ELB Target Groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html).

## Create application load balancer (ALB)
<a name="ex-alb-create-col"></a>

### Creating an ALB with the console
<a name="alb-create-con"></a>

The following shows this change type in the AMS console.

![Create Application Load Balancer interface showing ID ct-111r1yayblnw4 and version 3.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiAlbCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating an ALB with the CLI
<a name="alb-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm  --profile saml --region us-east-1 create-rfc --change-type-id "ct-111r1yayblnw4" --change-type-version "3.0" --title '{{Create ALB}}' --description "{{My Test ALB}}"  --execution-parameters ""{\"Description\":\"{{Test ALB}}\",\"VpcId\":\"{{VPC_ID}}\",\"Name\":\"{{TestStack}}\",\"StackTemplateId\":\"stm-sd7uv500000000000\",\"TimeoutInMinutes\":360,\"LoadBalancer\":{\"SecurityGroups\":[\"{{SG_ID}}\"],\"SubnetIds\":[\"{{SUBNET_ID}}\",\"{{SUBNET_ID}}\"]},\"Listener1\":{\"Port\":\"{{443}}\",\"Protocol\":\"{{HTTPS}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file. For example, you can replace the contents with something like this:

   ```
   aws amscm get-change-type-version --change-type-id "ct-111r1yayblnw4" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateAlbParams.json
   ```

1. Modify and save the CreateAlbParams file. For example:

   ```
   {
   "Description":      "{{ALB-Create}}", 
   "VpcId":            "{{VPC_ID}}",
   "Name":             "{{My-ALB}}",
   "StackTemplateId":  "stm-sd7uv500000000000",
   "TimeoutInMinutes" : 360,
   "LoadBalancer" : {
       "SecurityGroups" : ["{{SG_ID}}"],
       "SubnetIds" : ["{{SUBNET_ID}}", "{{SUBNET_ID}}"]
     },
     "Listener1" : {
       "Port" : "{{443}}",
       "Protocol" : "{{HTTPS}}"
     }
   }
   ```

1. Output the RFC template to a file in your current folder. For example, you can replace the contents with something like this:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateAlbRfc.json
   ```

1. Modify and save the CreateAlbRfc.json file. For example:

   ```
   {
   "ChangeTypeVersion":    "{{3.0}}",	
   "ChangeTypeId":         "ct-111r1yayblnw4",
   "Title":                "{{ALB-Create-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateAlbRfc file and the CreateAlbParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateAlbRfc.json --execution-parameters file://CreateAlbParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-alb-create-tip"></a>

**Note**  
As of version 3.0, you can also configure four CloudWatch alarms with customized alarm thresholds.

**Note**  
To open ports and associate all the load balancer resources, submit a Management \| Advanced stack components \| Security groups \| Update RFC.

To learn more about AWS Application Load Balancers, see [ What Is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

To create an Application Load Balancer target group, see [Target Group \| Create (For ALB)](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-target-group-create-for-alb.html).

## Update application load balancer (ALB)
<a name="ex-alb-update-col"></a>

### Updating an ALB with the console
<a name="alb-update-con"></a>

The following shows this change type in the AMS console.

![Update Application Load Balancer page showing description, ID ct-1a1zzgi2nb83d, and version 3.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiAlbUpdateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating an ALB with the CLI
<a name="alb-update-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title {{Test-Update-ALB}} --change-type-id ct-1a1zzgi2nb83d --change-type-version 3.0 --execution-parameters '{"Description":"{{Updating Test ALB}}","VpcId":"{{VPC_ID}}","StackTemplateId":"stm-sd7uv500000000000","Name":"{{Test-Application-LoadBalancer}}","TimeoutInMinutes":{{360}},"Parameters":{"TargetGroupHealthCheckPath": "{{/myAppHealth}}"}}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file. For example, you can replace the contents with something like this:

   ```
   aws amscm get-change-type-version --change-type-id "ct-111r1yayblnw4" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateAlbParams.json
   ```

1. Modify and save the UpdateAlbParams file. For example:

   ```
   {
   "Description":      "{{ALB-Update}}", 
   "VpcId":            "{{VPC_ID}}",
   "Name":             "{{My-ALB}}",
   "StackTemplateId":  "stm-sd7uv500000000000",
   "TimeoutInMinutes" : {{360}},
   "Parameters": {
       "LoadBalancerSecurityGroups": [
         "{{sg-1234567890abcdef0}}"
       ],
       "LoadBalancerSubnetIds": [
         "{{subnet-1234567890abcdef0}}",
         "{{subnet-1234567890abcdef1}}"
       ],
       "LoadBalancerDeletionProtection": "{{false}}",
       "LoadBalancerIdleTimeout": "{{60}}",
       "Listener1Port": "{{443}}",
       "Listener1Protocol": "{{HTTPS}}",
       "Listener1SSLCertificateArn": "{{arn:aws:acm:ap-southeast-2:012345678912:certificate/e23c3545-e92d-4542-83b8-63483505b5a5}}",
       "Listener1SSLPolicy": "{{ELBSecurityPolicy-TLS-1-2-Ext-2018-06}}",
       "Listener2Port": "{{8080}}",
       "Listener2Protocol": "{{HTTP}}",
       "TargetGroupHealthCheckInterval": "{{10}}",
       "TargetGroupHealthCheckPath": "{{/thing/index.html}}",
       "TargetGroupHealthCheckPort": "{{8080}}",
       "TargetGroupHealthCheckProtocol": "{{HTTP}}",
       "TargetGroupHealthCheckTimeout": "{{10}}",
       "TargetGroupHealthyThreshold": "{{2}}",
       "TargetGroupUnhealthyThreshold": "{{10}}",
       "TargetGroupValidHTTPCode": "{{200}}",
       "TargetGroupDeregistrationDelayTimeout": "{{300}}",
       "TargetGroupSlowStartDuration": "{{30}}",
       "TargetGroupCookieExpirationPeriod": "{{20}}"
     }
   }
   ```

1. Output the RFC template to a file in your current folder. For example, you can replace the contents with something like this:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateAlbRfc.json
   ```

1. Modify and save the UpdateAlbRfc.json file. For example:

   ```
   {
   "ChangeTypeVersion":    "{{3.0}}",	
   "ChangeTypeId":         "ct-111r1yayblnw4",
   "Title":                "{{ALB-Update-RFC}}"
   }
   ```

1. Create the RFC, specifying the UpdateAlbRfc file and the UpdateAlbParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateAlbRfc.json --execution-parameters file://UpdateAlbParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-alb-update-tip"></a>

**Note**  
This change type is version 3.0, and can be used with the version 3.0 of the Create ALB change type (ct-111r1yayblnw4).

To learn more about AWS Application Load Balancers, see [What Is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

## Create listener
<a name="ex-listener-create-col"></a>

### Creating a Listener for an ALB or NLB with the Console
<a name="listener-create-con"></a>

Screenshot of this change type in the AMS console:

![](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiListenerAlbNlbCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a Listener for an ALB or NLB with the CLI
<a name="listener-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-14yjom3kvpinu" --change-type-version "2.0" --title "{{TITLE}}" --execution-parameters "{\"Description\":\"{{DESCRIPTION}}\", \"VpcId\":\"{{VPC_ID}}\", \"StackTemplateId\": \"stm-u5n0r6aacdvdwthhm\", \"Name\":\"{{NAME}}\", \"TimeoutInMinutes\":60, \"Parameters\": {\"LoadBalancerArn\":\"{{LB-ARN}}",\"DefaultActionTargetGroupArn\":\"{{TARGET-GROUP-ARN}}",\"Port\":\"{{80}}\",\"Protocol\":\"{{HTTP}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it CreateListenerParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-14yjom3kvpinu" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateListenerParams.json
   ```

1. Modify and save the CreateListenerParams file. For example, you can replace the contents with something like this:

   ```
   {
   "Description":      "{{Listener-Create}}", 
   "VpcId":            "{{VPC_ID}}", 
   "StackTemplateId":  "stm-u5n0r6aacdvdwthhm", 
   "Name":             "{{My-Listener}}",
   
   "Parameters":   {
       "LoadBalancerArn":               {{ARN}},
       "DefaultActionTargetGroupArn":   {{ARN}},
       "Port":                          {{PORT}},
       "Protocol":                     {{Protocol}}"
       }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateListenerRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateListenerRfc.json
   ```

1. Modify and save the CreateListenerRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{2.0}}",	
   "ChangeTypeId":         "ct-14yjom3kvpinu",
   "Title":                "{{Listener-Create-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateListenerRfc file and the CreateListenerParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateListenerRfc.json --execution-parameters file://CreateListenerParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

   Next Steps: Submit a Management \| Other \| Other \| Update change type to open ports and associate security groups, see [Other \| Other requests](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-other-other.html). 

### Tips
<a name="ex-listener-alb-nlb-create-tip"></a>

**Note**  
You can specify up to four Target IDs, Ports, and Availability Zones.

## High availability one-tier stacks: Creating
<a name="ex-HA-1-tier-create-col"></a>

### Creating a high availability one-tier stack with the console
<a name="ha-1-tier-create-con"></a>

![Change type details showing ID, version 2.0, and automated execution mode for creating high availability stack.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiHa1tCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a high availability one-tier stack with the CLI
<a name="ha-1-tier-create-cli"></a>

How it works:

1. Use the Template Create method (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file in your current folder; this example names it CreateOnetierStackParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-09t6q7j9v5hrn" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateOnetierStackParams.json
   ```

1. Modify the schema, replacing the {{variables}} as appropriate.

   ```
   {
       "Description":          "{{HA-One-Tier-Stack}}",
       "Name":                 "{{One-Tier-Stack}}",
       "TimeoutInMinutes":     "{{360}}",
       "VpcId":                "{{VPC_ID}}",
       "ApplicationLoadBalancer": {
           "SubnetIds": [
                     "{{SUBNET_ID}}",
                     "{{SUBNET_ID}}"
           ]
       },
       "AutoScalingGroup": {
           "AmiId": "{{AMI-ID}}"
           "SubnetIds": [
                    "{{SUBNET_ID}}",
                    "{{SUBNET_ID}}"
           ]
       }
   }
   ```

1. Output the CreateRfc JSON template to a file in your current folder; example names it CreateOnetierStackRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateOnetierStackRfc.json
   ```

1. Modify the RFC template as appropriate and save it. Reset the start and end times for a scheduled RFC, or leave off for an ASAP RFC.

   ```
   {
   "ChangeTypeVersion":    {{2.0}}",
   "ChangeTypeId":         "ct-09t6q7j9v5hrn",
   "Title":                "{{HA-One-Tier-RFC}}",
   "RequestedStartTime":   "{{2019-04-28T22:45:00Z}}",
   "RequestedEndTime":     "{{2019-04-28T22:45:00Z}}"
   }
   ```

1. Create the RFC, specifying the CreateOnetierStackRfc.json file and the CreateOnetierStackParams.json execution parameters file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateOnetierStackRfc.json --execution-parameters file://CreateOnetierStackParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-HA-1-tier-create-tip"></a>

**Note**  
This is a large provisioning of resources, especially if you add UserData. The load balancer Amazon resource name (ARN) can be found through the Load Balancer page of the EC2 console by searching with the load balancer stack ID returned in the RFC execution output.

## Create IAM entity or policy (Managed Automation)
<a name="ex-iam-resource-create-rr-col"></a>

### Creating IAM resources (Managed Automation) with the console
<a name="iam-resource-create-rr-con"></a>

![Change type details showing Create IAM Resource with ID, version 1.0, and manual execution mode.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiIamResourceCreateRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating IAM resources (Managed Automation) with the CLI
<a name="iam-resource-create-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).
**Note**  
When pasting in a policy document, note that the RFC only accepts policy pastes up to 20,480 characters. If your file has more than 20,480 characters, create a service request to upload the policy and then refer to that service request in the RFC that you open for IAM.

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3dpd8mdd9jn1r" --change-type-version "1.0" --title "{{TestIamCreate}}" --execution-parameters "{\"UseCase\":\"{{IAM_RESOURCE_DETAILS}}\",\"IAM Role\":[{\"RoleName\":\"{{ROLE_NAME}}\",\"TrustPolicy\":\"{{TRUST_POLICY}}\",\"RolePermissions\":\"{{ROLE_PERMISSIONS}}\"}],\"Operation\":\"Create\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; example names it CreateIamResourceParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3dpd8mdd9jn1r" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateIamResourceParams.json
   ```

1. Modify and save the CreateIamResourceParams file; example creates an IAM Role with policy documents pasted inline.

   ```
   {
     "UseCase": "{{IAM_RESOURCE_DETAILS}}",
     "IAM Role": [
       {
         "RoleName": "{{codebuild_ec2_test_role}}",
         "TrustPolicy": {
           "Version": "{{2008-10-17}}",
           "Statement": [
             {
               "Effect": "{{Allow}}",
               "Principal": {
                 "Service": "{{codebuild.amazonaws.com}}"
               },
               "Action": "{{sts:AssumeRole}}"
             }
           ]
         },
         "RolePermissions": {
           "Version": "{{2012-10-17}}",
           "Statement": [
             {
               "Effect": "{{Allow}}",
               "Action": [
                 "{{ec2:DescribeInstanceStatus}}"
               ],
               "Resource": "{{*}}"
             }
           ]
         }
       }
     ],
     "Operation": "Create"
   }
   ```

1. Output the RFC template JSON file to a file named CreateIamResourceRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateIamResourceRfc.json
   ```

1. Modify and save the CreateIamResourceRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "1.0",
   "ChangeTypeId": "ct-3dpd8mdd9jn1r",
   "Title": "{{Create IAM Role}}"
   }
   ```

1. Create the RFC, specifying the CreateIamResourceRfc file and the CreateIamResourceParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateIamResourceRfc.json  --execution-parameters file://CreateIamResourceParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-iam-resource-create-rr-tip"></a>
+ After an IAM role is provisioned in your account, you must onboard the role in your federation solution.
+ When pasting in a policy document, note that the RFC only accepts policy pastes up to 20,480 characters. If your policy has more than 20,480 characters, create a service request to upload the policy, and then refer to that service request in the RFC that you open for IAM.
+ This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.
+ For information about AWS Identity and Access Management, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and for policy information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html). For information about AMS permissions, see [Deploying IAM resources](https://docs.aws.amazon.com/managedservices/latest/userguide/deploy-iam-resources.html).

## Continue rollback on custom CloudFormation stack
<a name="ex-custom-stack-cfn-template-continue-rollback-col"></a>

### Continue rollback a CloudFormation ingest stack failed update using the console
<a name="cfn-ingest-update-con"></a>

![AMS Advanced console, create RFC section, change type details box for ct-32r1igwrwag4i: Continue rollback on custom CloudFormation stack.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiCustomStackContinueRollback.png)


1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Continue rollback a CloudFormation ingest stack failed update using the CLI
<a name="custom-stack-cfn-continue-rollback-cli"></a>

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-32r1igwrwag4i" --change-type-version "1.0" --title "{{Continue Update Rollback}}" --execution-parameters "{\"StackId\":\"{{STACK_ID}}\",\"Region\":\"{{REGION}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file in your current folder; this example names it ContinueRollbackParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-32r1igwrwag4i" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ContinueRollbackParams.json
   ```

1. Modify and save the ContinueRollbackParams.json file. For example, you can replace the contents with something like this:

   ```
   {
       "StackId": "stack-a1b2c3d4e5f67890e",
       "Region": "{{us-east-1}}",
       "Priority": "{{High}}"
   }
   ```

1. Output the JSON template for CreateRfc to a file in your current folder; this example names it ContinueRollbackRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ContinueRollbackRfc.json
   ```

1. Modify and save the ContinueRollbackRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-32r1igwrwag4i",
     "Title": "{{Continue Update Rollback}}"
   }
   ```

1. Create the RFC, specifying the ContinueRollbackRfc file and the execution parameters file:

   ```
   aws amscm create-rfc --cli-input-json file://ContinueRollbackRfc.json --execution-parameters file://ContinueRollbackParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="custom-stack-cfn-continue-rollback-tip"></a>

For more information see [Continue rolling back an update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html).

## Manage the VPC Subnet IPv4 Address Auto Assigment
<a name="ex-vpc-subnet-ipv4-assignment-manage-col"></a>

### Manage VPC Subnet IPv4 Address Auto Assigment with the console
<a name="vpc-subnet-ipv4-assignment-manage-con"></a>

The following shows this change type in the AMS console.

![Manage subnet public IPv4 auto assignment change type details in the AMS console.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcManageSubnetAddressCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Manage VPC Subnet IPv4 Address Auto Assigment with the CLI
<a name="vpc-subnet-ipv4-assignment-manage-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1pqxczuw5uwu6" --change-type-version "1.0" --title "{{AWSManagedServices-ManageSubnetPublicIpv4AutoAssign}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-ManageSubnetPublicIpv4AutoAssign\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"SubnetId\": \"{{subnet-0a1b2c3d4e5f67890}}\", \"MapPublicIpOnLaunch\": {{true}}, \"AcknowledgeNetworkImpact\": [\"{{Yes}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it ManageSubnetAutoAddressParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1pqxczuw5uwu6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ManageSubnetAutoAddressParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
    "DocumentName": "AWSManagedServices-ManageSubnetPublicIpv4AutoAssign",
    "Region": "{{us-east-1}}",
    "Parameters": {
        "SubnetId": "{{subnet-0a1b2c3d4e5f67890}}",
        "MapPublicIpOnLaunch": {{true}},
        "AcknowledgeNetworkImpact": [
            "{{Yes}}"
        ]
    }
   }
   ```

1. Output the RFC template JSON file; this example names it ManageSubnetAutoAddressRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ManageSubnetAutoAddressRfc.json
   ```

1. Modify and save the ManageSubnetAutoAddressRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-1pqxczuw5uwu6",
     "Title" : "{{ManageSubnetAutoAddress}}"
   }
   ```

1. Create the RFC, specifying the ManageSubnetAutoAddressRfc file and the ManageSubnetAutoAddressParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ManageSubnetAutoAddressRfc.json  --execution-parameters file://ManageSubnetAutoAddressParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-vpc-endpoint-gateway-create-tip"></a>

For general information on VPCs and subnet addressing, see [IP addressing for your VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html).

## Schedule add
<a name="ex-res-sched-schedule-add-col"></a>

### Adding an AMS Resource Scheduler schedule with the console
<a name="res-sched-schedule-add-con"></a>

The following shows this change type in the AMS console.

![Add Resource Scheduler Schedule page showing ID ct-2bxelbn765ive and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiResSchedScheduleAddCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Adding an AMS Resource Scheduler schedule with the CLI
<a name="res-sched-schedule-add-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2bxelbn765ive" --change-type-version "1.0" --title "{{Add a schedule for AMS Resource Scheduler}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-AddOrUpdateSchedule\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"Action\":[\"add\"],\"Name\":[\"{{Schedule01}}\"],\"Description\":[\"{{Test schedule}}\"],\"Hibernate\":[\"{{true}}\"],\"Enforced\":[\"{{false}}\"],\"OverrideStatus\":[\"{{running}}\"],\"Periods\":[\"{{period01}}\",\"{{period02}}\"],\"RetainRunning\":[\"{{false}}\"],\"StopNewInstances\":[\"{{true}}\"],\"SSMMaintenanceWindow\":[\"{{window01}}\"],\"TimeZone\":[\"{{Australia/Sydney}}\"],\"UseMaintenanceWindow\":[\"{{true}}\"],\"UseMetrics\":[\"{{false}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it AddScheduleParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2bxelbn765ive" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AddScheduleParams.json
   ```

1. Modify and save the AddScheduleParams file.

   ```
   {
     "DocumentName" : "AWSManagedServices-AddOrUpdateSchedule",
     "Region" : "{{us-east-1}}",
     "Parameters" : {
       "Action" : ["add"],
       "Name" : ["{{Schedule01}}"],
       "Description" : ["{{Test schedule}}"],
       "Hibernate" : ["{{true}}"],
       "Enforced" : ["{{false}}"],
       "OverrideStatus" : ["{{running}}"],
       "Periods" : [
         "{{period01}}",
         "{{period02}}"
       ],
       "RetainRunning" : ["{{false}}"],
       "StopNewInstances" : ["{{true}}"],
       "SSMMaintenanceWindow" : ["{{window01}}"],
       "TimeZone" : ["{{Australia/Sydney}}"],
       "UseMaintenanceWindow" : ["{{true}}"],
       "UseMetrics" : ["{{false}}"]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it AddScheduleRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > AddScheduleRfc.json
   ```

1. Modify and save the AddScheduleRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-2bxelbn765ive",
   "Title":                "{{Add a schedule for AMS Resource Scheduler}}"
   }
   ```

1. Create the RFC, specifying the AddScheduleRfc file and the AddScheduleParams file:

   ```
   aws amscm create-rfc --cli-input-json file://AddScheduleRfc.json --execution-parameters file://AddScheduleParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-res-sched-schedule-add-tip"></a>
+ Do not begin the maintenance window name with 'mw-'.
+ For more information, see [How the AMS Resource Scheduler works](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-how-works.html).
+ AMS Resource Scheduler is based on the AWS Instance Scheduler; to learn more, see [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/welcome.html).

## Delete EBS snapshot (Managed Automation)
<a name="ex-ebs-snpsht-delete-rr-col"></a>

Use when you need extra help or communications about the snapshots to delete.

### Deleting EBS snapshots with the Console (Managed Automation)
<a name="ebs-snpsht-delete-rr-con"></a>

![Delete EBS Snapshot interface showing manual execution mode and version details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEbsSnpshtDeleteRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting EBS snapshots with the CLI (Review Requied)
<a name="ebs-snpsht-delete-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1vrnixswq1uwf" --change-type-version "1.0" --title "{{Delete EBS Snapshot (managed automation)}}" --execution-parameters "{\"SnapshotIds\": [\"{{snap-0a1b2c3d4e5f67890}}\",\"{{snap-1a2b3c4d5e6f78901}}\"], \"AMI\": \"{{No}}\", \"Region\": \"{{us-east-1}}\", \"Priority\": \"{{Medium}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DeleteEbsSnpshtRrParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1vrnixswq1uwf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteEbsSnpshtRrParams.json
   ```

1. Modify and save the DeleteEbsSnpshtRrParams file. For example, you can replace the contents with something like this:

   ```
   {
     "SnapshotIds": [
       "snap-0a1b2c3d4e5f67890",
       "snap-1a2b3c4d5e6f78901"
     ],
     "AMI": "No",
     "Region": "us-east-1",
     "Priority": "Medium"
   }
   ```

1. Output the RFC template JSON file to a file; this example names it DeleteEbsSnpshtRrRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteEbsSnpshtRrRfc.json
   ```

1. Modify and save the DeleteEbsSnpshtRrRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "1.0",
   "ChangeTypeId":         "ct-1vrnixswq1uwf",
   "Title":                "{{EBS-Snapshot-Delete-RR-RFC}}"
   }
   ```

1. Create the RFC, specifying the DeleteEbsSnpshtRrRfc file and the DeleteEbsSnpshtRrParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteEbsSnpshtRrRfc.json  --execution-parameters file://DeleteEbsSnpshtRrParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ebs-snpsht-delete-rr-tip"></a>

To learn more about Amazon EBS snapshots, see [Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html).

## Update SNS topic
<a name="ex-sns-update-col"></a>

### Update SNS topic with the Console
<a name="sns-update-con"></a>

Screenshot of this change type in the AMS console:

![Update SNS Topic change type details including ID, execution mode, and description.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiSnsUpdateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Update SNS topic with the CLI
<a name="sns-update-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE* (minimal parameters):

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0zzf0fjz76jmb" --change-type-version "1.0" --title "{{Update SNS Topic}}" --execution-parameters "{\"TopicArn\": \"{{arn:aws:sns:us-east-1:123456789101:My-SNS-Topic}}\", \"Priority\": \"{{Medium}}\", \"Parameters\": {\"DisplayName\": \"{{My-SNS-Topic}}\", \"KmsMasterKeyId\": \"{{arn:aws:kms:us-east-1:123456789101:key/cfe0542d-3be9-4166-9eac-d0cd6af61445}}\"}}"
```

*TEMPLATE CREATE* (all parameters):

1. Output the execution parameters JSON schema for this change type to a file; this example names it SnsUpdateParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-3rcl9u1k017wu" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > SnsUpdateParams.json
   ```

1. Modify and save the SnsUpdateParams file. For example, you can replace the contents with something like this:

   ```
   {
     "TopicArn": "{{arn:aws:sns:us-east-1:123456789101:Test-Stack}}",
     "Parameters": {
       "DisplayName": "{{My-Test-Stack}}",
       "DeliveryPolicy": "{\"http\":{\"defaultHealthyRetryPolicy\":{\"minDelayTarget\":{{20}},\"maxDelayTarget\":{{20}},\"numRetries\":{{3}},\"numMaxDelayRetries\":{{0}},\"numNoDelayRetries\":{{0}},\"numMinDelayRetries\":{{0}},\"backoffFunction\":\"{{linear}}\"},\"disableSubscriptionOverrides\":{{false}},\"defaultRequestPolicy\":{\"headerContentType\":\"{{text/plain; charset=UTF-8}}\"}}}",
       "DataProtectionPolicy": "{\"Name\":\"{{__example_data_protection_policy}}\",\"Description\":\"{{Exampledataprotectionpolicy}}\",\"Version\":\"2021-06-01\",\"Statement\":[{\"DataDirection\":\"{{Inbound}}\",\"Principal\":[\"{{arn:aws:iam::123456789101:user/ExampleUser}}\"],\"DataIdentifier\":[\"{{arn:aws:dataprotection::aws:data-identifier/CreditCardNumber}}\"],\"Operation\":{\"{{Deidentify}}\":{\"MaskConfig\":{\"{{MaskWithCharacter}}\":\"#\"}}}}]}",
       "KmsMasterKeyARN": "{{arn:aws:kms:ap-southeast-2:123456789101:key/bb43bd18-3a75-482e-822d-d0d3a5544dc8}}",
       "TracingConfig": "{{Active}}"
     },
     "Priority": "{{Medium}}"
   }
   ```

1. Output the RFC template JSON file to a file named SnsUpdateRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > SnsUpdateRfc.json
   ```

1. Modify and save the SnsUpdateRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-0zzf0fjz76jmb",
   "Title":                "{{Update-SNS-RFC}}"
   }
   ```

1. Create the RFC, specifying the SnsUpdate Rfc file and the SnsUpdateParams file:

   ```
   aws amscm create-rfc --cli-input-json file://SnsUpdateRfc.json  --execution-parameters file://SnsUpdateParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-sns-update-tip"></a>

To learn more about AWS Simple Notification Service (SNS), see [Amazon Simple Notification Service](https://aws.amazon.com/sns/). Also see [Getting Started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html).

## Create an S3 access point
<a name="ex-s3-access-point-create-col"></a>

### Creating an S3 access point with the Console
<a name="s3-access-point-create-con"></a>

Screenshot of this change type in the AMS console:

![Change type details for creating an S3 access point, including ID, execution mode, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiS3AccessPointCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating an S3 access point with the CLI
<a name="s3-access-point-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title="{{Add Static Route}}" --description="{{Create an access point and associate it with the specified S3 bucket}}." --ct-id="ct-1elb1vtam0ka5" --ct-version="1.0" --input-params="{\"Access Point Name\":\"{{accesspoint1}}\",\"Bucket Name\":\"{{s3bucket1}}\",\"Network Origin\":\"{{VPC}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateS3AccessPointParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1elb1vtam0ka5" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateS3AccessPointParams.json\"Access Point Policy\":\"Example access point policy\"
   ```

1. Modify and save the CreateS3AccessPointParams file.

   ```
   {
   "Access Point Name": "accesspoint1",
   "Bucket Name": "s3bucket1",
   "Network Origin": "VPC",
   "Vpc Id": "vpc-12345678"
   "Access Point Policy": "Example access point policy"
   }
   ```

1. Output the RFC template JSON file to a file named CreateS3AccessPointRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateS3AccessPointRfc.json
   ```

1. Modify and save the CreateS3AccessPointRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "1.0",
   "ChangeTypeId":         "ct-1elb1vtam0ka5",
   "Title":                "S3-Accesspoint-Create-RFC"
   }
   ```

1. Create the RFC, specifying the CreateS3AccessPointRfc file and the CreateS3AccessPointParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateS3AccesspointRfc.json  --execution-parameters file://CreateS3AccesspointParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-s3-access-point-create-tip"></a>

To learn more about Amazon S3, see [Amazon Simple Storage Service Documentation](https://aws.amazon.com/documentation/s3/).

## Create Custom RDS Parameter Group
<a name="ex-rds-parameter-group-create-col"></a>

### Requesting administrator access with the console
<a name="ds-parameter-group-create-con"></a>

The following shows this change type in the AMS console.

![Create Custom RDS Parameter Group change type showing manual execution mode and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRDSCreateParamCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Requesting administrator access with the CLI
<a name="ds-parameter-group-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3da2lxapopb86" --change-type-version "1.0" --title "Create Custom RDS Parameter Group" --execution-parameters "{\"ParameterGroupName\": \"{{my-db-parameter-group}}\", \"ParameterGroupFamily\": \"{{mysql5.6}}\", \"Description\": \"{{A meaningful description of the parameter group}}\", \"Priority\": \"{{Medium}}\", \"Parameters\": [{\"ParameterName\": \"{{max_connections}}\", \"ParameterValue\": \"{{100}}\"}], \"RDSInstanceName\": \"{{my-test-db}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it RDSCreateParameterGroupParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3da2lxapopb86" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > RDSCreateParameterGroupParams.json
   ```

   Modify and save the RDSCreateParameterGroupParams file. For example, you can replace the contents with something like this:

   ```
   {
     "ParameterGroupName": "{{my-db-parameter-group}}",
     "ParameterGroupFamily": "{{mysql5.6}}",
     "Description": "{{A meaningful description of the parameter group}}",
     "Priority": "{{Medium}}",
     "Parameters": [
       {
         "ParameterName": "{{max_connections}}",
         "ParameterValue": "{{100}}"
       }
     ],
     "RDSInstanceName": "{{my-test-db}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it RDSCreateParameterGroupRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > RDSCreateParameterGroupRfc.json
   ```

1. Modify and save the RDSCreateParameterGroupRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeId":         "ct-3da2lxapopb86",
   "ChangeTypeVersion":    "{{1.0}}",
   "Title":                "{{Create Custom RDS Parameter Group}}"
   }
   ```

1. Create the RFC, specifying the RDSCreateParameterGroupRfc file and the GRDSCreateParameterGroupParams file:

   ```
   aws amscm create-rfc --cli-input-json file://RDSCreateParameterGroupRfc.json --execution-parameters file://RDSCreateParameterGroupParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Add event notification to an Amazon S3 bucket
<a name="ex-s3-add-event-notification-col"></a>

### Add an event notification to an S3 bucket with the Amazon S3 Console
<a name="s3-s3-add-event-notification-con"></a>

The following is a screenshot of this change type in the AMS console:

![Example this change type in the console.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiS3AddNotificationCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Add an event notification to an S3 bucket with the CLI
<a name="s3-s3-add-event-notification-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0o4zi9bzg74lp" --change-type-version "{{1.0}}" --title "Add event notification" --execution-parameters "{ \"DocumentName\": \"AWSManagedServices-AddBucketEventNotification\", \"Region\": \"{{us-east-1}}\", \"Parameters\": { \"BucketName\": \"{{bucketname}}\", \"EventName\": \"{{eventname}}\", \"Prefix\": \"{{foo}}\", \"Suffix\": \"{{.bar}}\", \"EventTypes\": [ \"{{s3:ObjectCreated:Post}}\", \"{{s3:ObjectCreated:Put}}\" ], \"DestinationARN\": \"{{arn:aws:lambda:us-east-1:123456789012:function:functionname\}}" } }"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it AddEventNotificationS3Params.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-220bdb8blaixf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AddEventNotificationS3Params.json
   ```

1. Modify and save the AddEventNotificationS3Params file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-AddBucketEventNotification",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "BucketName": "{{bucketname}}",
       "EventName": "{{eventname}}",
       "Prefix": "{{foo}}",
       "Suffix": "{{.bar}}",
       "EventTypes": [
         "{{s3:ObjectCreated:Post}}",
         "{{s3:ObjectCreated:Put}}"
       ],
       "DestinationARN": "{{arn:aws:lambda:us-east-1:123456789012:function:functionname}}"
     }
   }
   ```

1. Output the RFC template JSON file to a file named AddEventNotificationS3Rfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > AddEventNotificationS3Rfc.json
   ```

1. Modify and save the AddS3LifecycleConfigRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion": "{{1.0}}",
   "ChangeTypeId": "ct-0o4zi9bzg74lp",
   "Title": "{{Add Event Notification}}"
   }
   ```

1. Create the RFC, specifying the AddEventNotificationS3Rfc file and the AddEventNotificationS3Params file:

   ```
   aws amscm create-rfc --cli-input-json file://AddEventNotificationS3Rfc.json --execution-parameters file://AddEventNotificationS3Params.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Update custom deny list for AMS Automated IAM Provisioning
<a name="ex-man-acc-aip-update-custom-deny-list-col"></a>

### Update custom deny list with the Console
<a name="update-custom-deny-list-con"></a>

Screenshot of this change type in the AMS console:

![Form for updating custom deny list in Automated IAM Provisioning, showing ID and classification details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiUpdateCustomDenyListCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Update custom deny list with the CLI
<a name="update-custom-deny-list-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2r9xvd3sdsic0" --change-type-version "1.0" --title "Update custom deny list for Automated IAM Provisioning" --execution-parameters "{\"CustomerCustomDenyActionsList1\":\"{{ec2:RunInstances,s3:PutBucket,sagemaker:*\}}",\"Priority\":\"{{High\}}"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named CustomerCustomDenyActionsList.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-2r9xvd3sdsic0" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CustomerCustomDenyActionsList.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
       "DocumentName": "AWSManagedServices-CustomerCustomDenyActionsList",
       "Region": "{{us-east-1}}",
       "Parameters": {
     "CustomerCustomDenyActionsList1": "ec2:RunInstances,s3:PutBucket,sagemaker:*",
     "Priority": "High"
   }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CustomerCustomDenyActionsListRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CustomerCustomDenyActionsListRfc.json
   ```

1. Modify and save the CustomerCustomDenyActionsListRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "{{1.0}}",
     "ChangeTypeId": "{{ct-2r9xvd3sdsic0}}",
     "Title": "Update custom deny list for Automated IAM Provisioning"
   }
   ```

1. Create the RFC, specifying the CreateAcmPublicRfc file and the CreateAcmPublicParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CustomerCustomDenyActionsListRfc.json  --execution-parameters file://CustomerCustomDenyActionsListParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Migrate AWS Managed Account DNS resolver to Route 53 for SALZ accounts (Managed Automation)
<a name="ex-man-acct-dns-mig-r53-rr-col"></a>

### Migrate AWS Managed Account DNS resolver to Route 53 (SALZ) with the console
<a name="man-acct-dns-mig-r53-rr-con"></a>

The following shows this change type in the AMS console.

![Change type details for migrating AWS Managed Microsoft AD to Route 53 DNS resolver.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/gui-man-acct-migrate-r53CT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Migrate AWS Managed Account DNS resolver to Route 53 (SALZ) with the CLI
<a name="man-acct-dns-mig-r53-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

Required parameters only:

```
aws amscm create-rfc --change-type-id "ct-2tqi3kjcusen4" --change-type-version "1.0" --title "Migrate AWS managed Microsoft AD to Route 53 DNS resolver for SALZ accounts" --execution-parameters "{}"
```

All required and optional parameters:

```
aws amscm create-rfc --change-type-id "ct-2tqi3kjcusen4" --change-type-version "1.0" --title "Migrate AWS managed Microsoft AD to Route 53 DNS resolver for SALZ accounts" --execution-parameters "{\"Priority\":\"{{Medium}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named CreateMigrateToRoute53RequiredParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-2tqi3kjcusen4" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateMigrateToRoute53RequiredParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "Priority": "Medium"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateMigrateToRoute53RequiredRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateMigrateToRoute53RequiredRfc.json
   ```

1. Modify and save the CreateMigrateToRoute53RequiredRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeId":         "ct-2tqi3kjcusen4",
   "ChangeTypeVersion":    "{{1.0}}",
   "Title":                "{{Migrate AWS managed Microsoft AD to Route 53 DNS resolver for SALZ accounts}}"
   }
   ```

1. Create the RFC, specifying the CreateMigrateToRoute53RequiredRfc file and the CreateMigrateToRoute53RequiredParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateMigrateToRoute53RequiredRfc.json  --execution-parameters file://CreateMigrateToRoute53RequiredParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="man-acct-dns-mig-r53-rr-tip"></a>

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

## Disassociate resolver rules from VPC
<a name="ex-vpc-disassociate-resolver-rules-col"></a>

### Disassociate resolver rules from a VPC with the console
<a name="vpc-disassociate-resolver-rules-con"></a>

The following shows this change type in the AMS console.

![Console page showing disassociate resolver rules from VPC change type with ID, execution mode, and version details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcDisassociateResolverRule.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Disassociate resolver rules from a VPC with the CLI
<a name="vpc-disassociate-resolver-rules-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-3e3prksxmdhw8" --change-type-version "2.0" --title "{{AMI-Create-IC}}" --execution-parameters "{\"AMIName\":\"{{MyAmi}}\",\"VpcId\":\"{{VPC_ID}}\",\"EC2InstanceId\":\"{{INSTANCE_ID}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateAmiFromAsgParams.json:

   ```
   aws amscm create-rfc --change-type-id "ct-3e3prksxmdhw8" --change-type-version "1.0" --title "{{Create AMI from an Auto Scaling group}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-CreateAmiInAutoScalingGroup\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"AutoScalingGroupName\": [\"{{stack-ab0123cdef-ASG-1ABC2345}}\"],\"Sysprep\": [\"{{False}}\"],\"StopInstance\": [\"{{False}}\"]}}"
   ```

1. Modify and save the execution parameters CreateAmiFromAsgParams.json file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-CreateAmiInAutoScalingGroup",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "AutoScalingGroupName": [
         "{{stack-ab0123cdef-ASG-1ABC2345}}"
       ],
       "Sysprep": [
         "{{False}}"
       ],
       "StopInstance": [
         "{{False}}"
       ]
     }
   }
   ```

1. Output the RFC template JSON file to a file in your current folder; this example names it CreateAmiFromAsgRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateAmiFromAsgRfc.json
   ```

1. Modify and save the CreateAmiFromAsgRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-3e3prksxmdhw8",
     "Title": "{{Create AMI from an Auto Scaling group}}"
   }
   ```

1. Create the RFC, specifying the CreateAmiFromAsgRfc file and the CreateAmiFromAsgParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateAmiFromAsgRfc.json  --execution-parameters file://CreateAmiFromAsgParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Update Enhanced Monitoring
<a name="ex-rds-db-update-enhanced-monitoring-col"></a>

### Updating enhanced monitoring with the console
<a name="rds-db-update-enhanced-monitoring-con"></a>

The following shows this change type in the AMS console.

![Update Enhanced Monitoring change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsDbUpdateEnhancedMonitoring.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating enhanced monitoring with the CLI
<a name="rds-db-update-enhanced-monitoring-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3jx80fquylzhf" --change-type-version "1.0" --title "Update Enhanced Monitoring" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateRDSEnhancedMonitoring\",\"Region\":\"{{us-east-1}}\",\"Parameters\": {\"DBIdentifierArn\":[\"{{arn:aws:rds:us-east-1:000000000000:db:testdbinstance}}\"], \"MonitoringInterval\": [\"{{60}}\"],,\"MonitoringRoleName\": \"{{ds-monitoring-role}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named RotateRdsCertParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-3jx80fquylzhf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateRDSEnhancedMonitoringParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
       "DocumentName": "AWSManagedServices-UpdateRDSEnhancedMonitoring",
       "Region": "{{us-east-1}}",
       "Parameters": {
           "DBIdentifierArn": "{{arn:aws:rds:us-east-1:000000000000:db:testdbinstance}}",
           "MonitoringInterval": "{{60}}",
           "MonitoringRoleName": [
               "{{rds-monitoring-role}}"
           ]
       }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateRDSEnhancedMonitoringRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateRDSEnhancedMonitoringRfc.json
   ```

1. Modify and save the UpdateRDSEnhancedMonitoringRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "1.0",
   "ChangeTypeId":         "ct-3jx80fquylzhf",
   "Title":                "Update Enhanced Monitoring"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateRDSEnhancedMonitoringRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateRDSEnhancedMonitoringRfc.json --execution-parameters file://UpdateRDSEnhancedMonitoringParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Associate VPC with Resolver Rule
<a name="ex-vpc-associate-resolver-rule-col"></a>

### Requesting administrator access with the console
<a name="vpc-associate-resolver-rule-con"></a>

The following shows this change type in the AMS console.

![Run RFC details page showing Associate VPC With Resolver Rule change type configuration.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/gui-vpc-associate-resolver-rule.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Requesting administrator access with the CLI
<a name="vpc-associate-resolver-rule-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title="Associate VPC with Resolver Rule" --ct-id="ct-2pbqoffhclpek" --ct-version="1.0" --execution-parameters "{\"Description\":\"Associate VPC with Resolver Rule\",\"ResolverRuleId\":\"{{rslvr-rr-974b1666869a4d27b}}\",\"VPCId\":\"{{vpc-02a18ed0cd3c17e71}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it VPCAssociateResolverRule.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2pbqoffhclpek" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > VPCAssociateResolverRule.json
   ```

1. Modify and save the execution parameters as VPCAssociateResolverRuleParams.json. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-AssociateVPCWithResolverRule",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "Name": "{{resolver-rule-associate-vpc-test}}",
       "ResolverRuleId": "{{rslvr-rr-1234567890abcdefg}}",
       "VPCId": "{{vpc-1a2b3c4d}}"
     }
   }
   ```

1. Output the RFC template JSON file; this example names it VPCAssociateResolverRuleRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > VPCAssociateResolverRuleRfc.json
   ```

1. Modify and save the VPCAssociateResolverRuleRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-2pbqoffhclpek",
     "Title" : "{{Associate VPC with Resolver Rule }}"
   }
   ```

1. Create the RFC, specifying the VPCAssociateResolverRuleRfc file and the VPCAssociateResolverRuleParams file:

   ```
   aws amscm create-rfc --cli-input-json file://VPCAssociateResolverRuleRfc.json  --execution-parameters file:/VPCAssociateResolverRuleParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Deploy AMS pattern (Managed Automation)
<a name="ex-ams-pattern-deploy-rr-col"></a>

### Deploying an AMS pattern (Managed Automation) with the Console
<a name="ams-pattern-deploy-rr-con"></a>

Screenshot of this change type in the AMS console:

![Deploy AMS Patterns section showing ID, execution mode as Manual, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiAmsPatternDeployRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deploying an AMS pattern (Managed Automation) with the CLI
<a name="ams-pattern-deploy-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2jndrh7uit8uf" --change-type-version "1.0" --title "Deploy AMS Patterns" --execution-parameters "{\"PatternName\": \"{{amsEbsVolumeSnapshotTagger}}\",\"PatternParameters\": "{\"ExcludedTags\":\"{{BackupProd,Backup}}\",\"ASMGuardRail\":\"{{enabled}}\"}", \"OrganizationalUnit\": \"{{ou-9dyd-s2vptest}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it DeployAMSPatternsParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2jndrh7uit8uf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeployAMSPatternsParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "PatternName": "{{amsEbsVolumeSnapshotTagger}}",
     "ExcludeAccounts": ["{{123456789012}}"],
     "OrganizationalUnitIds": ["{{ou-9dyd-jvsei4yg}}"],
     "Priority": "{{Medium}}",
     "PatternParameters": [
       {
         "Name": "{{Foo}}",
         "Value": "{{Bar}}"
       }
     ]
   }
   ```

1. Output the RFC template JSON file; this example names it DeployAMSPatternsRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeployAMSPatternsRfc.json
   ```

1. Modify and save the DeployAMSPatternsRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "1.0",
   "ChangeTypeId":         "ct-2jndrh7uit8uf",
   "Title":                "Deploy AMS Patterns"
   }
   ```

1. Create the RFC, specifying the DeployAMSPatternsRfc file and the DeployAMSPatternsParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeployAMSPatternsRfc.json --execution-parameters file://DeployAMSPatternsParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Share AWS KMS Key
<a name="ex-man-kms-key-share-rr-col"></a>

### Share an AWS KMS key with the console
<a name="ex-man-kms-key-share-rr-con"></a>

The following shows this change type in the AMS console.

![Share KMS Key change type details showing manual execution mode and classification path.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiShareKmsKeyCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Share an AWS KMS key with the CLI
<a name="ex-man-kms-key-share-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title="Add Static Route" --description="Share KMS Key" --ct-id="ct-05yb337abq3x5" --ct-version="1.0" --input-params="{\"KMSKeyArn\":\"{{arn:aws:kms:us-east-1:111122223333:key/06506094-64e2-47f3-94bd-f919eefa22f5}}\",\"TargetAccountId\":\"{{000000000000}}\",\"IncludeKeyGrantOperations\":\"{{false}}\",\"IAMUserOrRole\":\"{{arn:aws:iam::000000000000:role/role-name}}\", \"Priority\":\"High\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ShareKmsKeyParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-05yb337abq3x5" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ShareKmsKeyParams.json
   ```

   Modify and save the ShareKmsKeyParams file. For example, you can replace the contents with something like this:

   ```
   {
     "Description": "Share KMS Key",
     "Parameters": {
       "KMSKeyArn": "{{arn:aws:kms:us-east-1:111122223333:key/06506094-64e2-47f3-94bd-f919eefa22f5}}",
       "TargetAccountId": "{{000000000000}}",
       "IncludeKeyGrantOperations": "{{false}}"
       "IAMUserOrRole": "{{arn:aws:iam::000000000000:role/role-name}}"
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it ShareKmsKeyParamsRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ShareKmsKeyParamsRfc.json
   ```

1. Modify and save the ShareKmsKeyParams.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeId": {
     "ChangeTypeVersion":    "{{1.0}}",
     "ChangeTypeId":         "{{ct-05yb337abq3x5}}",
     "Title":                "{{Share KMS Key}}"
   }
   ```

1. Create the RFC, specifying the ShareKmsKeyParamsRfc file and the ShareKmsKeyParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ShareKmsKeyParamsRfc.json --execution-parameters file://ShareKmsKeyParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

   To log in to the instance through a bastion, follow the next procedure, [Instance access examples](https://docs.aws.amazon.com/managedservices/latest/userguide/access-examples.html).

## Create Active Directory Trust
<a name="ex-dirserv-create-ad-trust-col"></a>

### Adding an AD trust with the console
<a name="dirserv-create-ad-trust-con"></a>

The following shows this change type in the AMS console.

![Create Active Directory Trust change type showing ID, execution mode as Automated, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiDirservCreateTrustCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Adding an AD trust with the CLI
<a name="dirserv-create-ad-trust-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0x6dylrnfjgz5" --change-type-version "1.0" --title "Create AD Trust" --execution-parameters ' 
{"DocumentName":"AWSManagedServices-CreateADTrust","Region":"{{ap-southeast-2}}","Parameters":{"DirectoryId":["{{d-976774e42f}}"],"RemoteDomainName":["{{onprem.local}}"],"SecretArn":["{{arn:aws:secretsmanager:ap-southeast-2:996606605561:secret:customer-shared/CorrectTPW-BI79uu}}"],"TrustType":["External"],"ConditionalForwarderIpAddresses":["{{10.153.28.39}}"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateADTrustParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0x6dylrnfjgz5" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateADTrustParams.json
   ```

   Modify and save the CreateADTrustParams.json file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-CreateADTrust",
     "Region": "ap-southeast-2",
     "Parameters": {
       "DirectoryId": [
         "d-976774e42f"
       ],
       "RemoteDomainName": [
         "onprem.local"
       ],
       "SecretArn": [
         "arn:aws:secretsmanager:ap-southeast-2:996606605561:secret:customer-shared/CorrectTPW-BI79uu"
       ],
       "TrustType": [
         "External"
       ],
       "ConditionalForwarderIpAddresses": [
         "10.153.28.39"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateADTrustRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateADTrustRfc.json
   ```

1. Modify and save the CreateADTrustRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeId": "ct-0x6dylrnfjgz5",
     "ChangeTypeVersion": "1.0",
     "Title": "{{Active Directory Trust}}"
   }
   ```

1. Create the RFC, specifying the CreateADTrustRfc file and the CreateADTrustParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateADTrustRfc.json --execution-parameters file://CreateADTrustParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="dirserv-create-ad-trust-tip"></a>

 For information about Directory Service, see the [Directory Service Admin Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html). 

## Override Stack Access Duration (Managed automation)
<a name="ex-stack-access-override-col"></a>

### Override stack access duration with the Console
<a name="ex-stack-access-override-con"></a>

Screenshot of this change type in the AMS console:

![Override Stack Access Duration change type details showing manual execution mode and version.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiStackAccessOverrideCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Override stack access duration with the CLI
<a name="ex-stack-access-override-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title="Override Stack Access Duration" --description="Override Stack Access Duration" --ct-id="ct-0jb01cofkhwk1" --ct-version="1.0" --input-params="{\"TimeRequestedInHours\": {{15}},\"Priority\":\"{{High}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file. This example names it OverrideStackAccessDurationParameters.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0jb01cofkhwk1" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > OverrideStackAccessDurationParameters.json
   ```

1. Modify and save the OverrideStackAccessDurationParameters.json file. For example, you can replace the contents with something like this:

   ```
   {
     "TimeRequestedInHours": {{15}},
     "Priority": "{{High}}"
   }
   ```

1. Output the RFC template JSON file to a file named OverrideStackAccessDuration.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > OverrideStackAccessDuration.json
   ```

1. Modify and save the OverrideStackAccessDuration.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "{{1.0}}",
     "ChangeTypeId": "ct-0jb01cofkhwk1",
     "Title": "{{Override Stack Access Duration}}"
   }
   ```

1. Create the RFC:

   ```
   aws amscm create-rfc --cli-input-json file://OverrideStackAccessDuration.json --execution-parameters file://OverrideStackAccessDurationParameters.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Enable automated IAM provisioning with read-write permissions
<a name="ex-man-iam-auto-provision.col"></a>

### Enable automated AWS Identity and Access Management provisioning with read/write permissions with the Console
<a name="man-iam-auto-provision-con"></a>

Screenshot of this change type in the AMS console:

![Enable Automated IAM Provisioning checkbox selected with manual execution mode details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiAutomatedIAMProvisioningReadWriteCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Enable automated AWS Identity and Access Management provisioning with read/write permissions with the CLI
<a name="man-iam-auto-provision-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1706xvvk6j9hf" --change-type-version "1.0" --title "Enable (managed automation)" --execution-parameters "{\"SAMLIdentityProviderArns\": [\"arn:aws:iam::123456789012:saml-provider/customer-saml\"], \"IamEntityArns\": [\"arn:aws:iam::123456789012:role/test-role-one\", \"arn:aws:iam::123456789012:role/test-role-two\"], \"Priority\": \"High\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it EnableAutomatedIAMProvisioningParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1706xvvk6j9hf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > EnableAutomatedIAMProvisioningParams.json
   ```

1. Modify and save the EnableAutomatedIAMProvisioningParams file. For example, you can replace the contents with something like this:

   ```
   {
     "SAMLIdentityProviderArns": ["arn:aws:iam::{{123456789012:saml-provider/customer-saml}}"],
     "IamEntityArns": ["arn:aws:iam::{{123456789012:role/test-role-one}}", "{{arn:aws:iam::123456789012:role/test-role-two}}"],
     "Priority": "High"
   }
   ```

1. Output the RFC template JSON file to a file named EnableAutomatedIAMProvisioningRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > EnableAutomatedIAMProvisioningRfc.json
   ```

1. Modify and save the EnableAutomatedIAMProvisioningRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-1706xvvk6j9hf",
   "Title":                "{{Enable-Automated-IAM-Provisioning-RFC}}"
   }
   ```

1. Create the RFC, specifying the UpdateSecurityPolicy Rfc file and the UpdateSecurityPolicyParams file:

   ```
   aws amscm create-rfc --cli-input-json file://EnableAutomatedIAMProvisioningRfc.json  --execution-parameters file://EnableAutomatedIAMProvisioningParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Add VPC static route (Managed Automation)
<a name="ex-vpc-static-route-add-rr-col"></a>

### Add a static route with the console
<a name="vpc-static-route-add-rr-con"></a>

The following shows this change type in the AMS console.

![Add Static Route change type details showing ID, execution mode as Manual, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcStaticRouteAddRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Adding a static route with the CLI
<a name="vpc-static-route-add-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title="{{Add Static Route}}" --description="{{Add static route}}" --ct-id="ct-06bwg93ukgg8t" --ct-version="1.0" --input-params="{\"RouteTableId\":\"{{rtb-0123abcd}}\",\"DestinationCidrBlock\":\"{{172.31.0.0/16}}\",\"Target\":\"{{pcx-0123456789abcdefg}}\",\"Priority\":\"{{High}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it EncryptAmiParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-06bwg93ukgg8t" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AddStaticRouteParams.json
   ```

1. Modify and save the execution AddStaticRouteParams.json file. For example, you can replace the contents with something like this:

   ```
   {
       "RouteTableId": "{{rtb-0123abcd}}",
       "DestinationCidrBlock": "{{172.31.0.0/16}}",
       "Target": "{{pcx-0123456789abcdefg}}",
       "Priority": "{{High}}"
   }
   ```

1. Output the RFC template JSON file; this example names it AddStaticRouteRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > AddStaticRouteRfc.json
   ```

1. Modify and save the AddStaticRouteRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-06bwg93ukgg8t",
     "Title": "{{Add static route}}"
   }
   ```

1. Create the RFC, specifying the AddStaticRouteRfc file and the AddStaticRouteParams file:

   ```
   aws amscm create-rfc --cli-input-json file://AddStaticRouteRfc.json  --execution-parameters file://AddStaticRouteParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-vpc-static-route-add-rr-tip"></a>

For information about VPCs, see [Virtual private clouds (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html).

## Create IAM entity or policy
<a name="ex-iam-entity-create-col"></a>

### Creating IAM entity or policy with the console
<a name="iam-entity-create-con"></a>

![IAM role or policy creation interface with ID, execution mode, and description details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiIamEntityCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating IAM entity or policy with the CLI
<a name="iam-entity-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1n9gfnog5x7fl" --change-type-version "1.0" --title "{{Create role or policy}}" --execution-parameters '{"DocumentName":"AWSManagedServices-HandleAutomatedIAMProvisioningCreate-Admin","Region":"{{us-east-1}}","Parameters":{"ValidateOnly":"{{No}}"},"RoleDetails":{"Roles":[{"RoleName":"{{RoleTest01}}","Description":"{{This is a test role}}","AssumeRolePolicyDocument":"{"Version": "2012-10-17", 		 	 	 		 	 	 "Statement":{{[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":"sts:AssumeRole"}]}","ManagedPolicyArns":["arn:aws:iam::123456789012:policy/policy01","arn:aws:iam::123456789012:policy/policy02"],"Path":"/","MaxSessionDuration":"7200","PermissionsBoundary":"arn:aws:iam::123456789012:policy/permission_boundary01","InstanceProfile":"No"}]},"ManagedPolicyDetails":{"Policies":[{"ManagedPolicyName":"TestPolicy01","Description":"This is customer policy","Path":"/test/","PolicyDocument":"{"{{Version}}":"2012-10-17","Statement":[{"Sid":"AllQueueActions","Effect":"Allow","Action":"sqs:ListQueues","Resource":"*","Condition":{"ForAllValues:StringEquals":{"aws:tagKeys":["temporary"]}}}]}"}]}}}}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; example names it CreateIamResourceParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1n9gfnog5x7fl" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateIamResourceParams.json
   ```

1. Modify and save the CreateIamResourceParams file; example creates an IAM Role with policy documents pasted inline.

   ```
   {
     "DocumentName": "AWSManagedServices-HandleAutomatedIAMProvisioningCreate-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "ValidateOnly": "{{No}}"
     },
     "RoleDetails": {
       "Roles": [
         {
           "RoleName": "{{RoleTest01}}",
           "Description": "{{This is a test role}}",
           "AssumeRolePolicyDocument": {
             "Version": "2012-10-17", 		 	 	 		 	 	 
             "Statement": [
               {
                 "Effect": "{{Allow}}",
                 "Principal": {
                   "AWS": "{{arn:aws:iam::123456789012:root}}"
                 },
                 "Action": "{{sts:AssumeRole}}"
               }
             ]
           },
           "ManagedPolicyArns": [
             "{{arn:aws:iam::123456789012:policy/policy01}}",
             "{{arn:aws:iam::123456789012:policy/policy02}}"
           ],
           "Path": "/",
           "MaxSessionDuration": "{{7200}}",
           "PermissionsBoundary": "{{arn:aws:iam::123456789012:policy/permission_boundary01}}",
           "InstanceProfile": "{{No}}"
         }
       ]
     },
     "ManagedPolicyDetails": {
       "Policies": [
         {
           "ManagedPolicyName": "{{TestPolicy01}}",
           "Description": "{{This is customer policy}}",
           "Path": "{{/test/}}",
           "PolicyDocument": {
             "Version": "2012-10-17", 		 	 	 		 	 	 
             "Statement": [
               {
                 "Sid": "{{AllQueueActions}}",
                 "Effect": "{{Allow}}",
                 "Action": "{{sqs:ListQueues}}",
                 "Resource": "{{*}}",
                 "Condition": {
                   "{{ForAllValues:StringEquals}}": {
                     "{{aws:tagKeys}}": [
                       "{{temporary}}"
                     ]
                   }
                 }
               }
             ]
           }
         }
       ]
     }
   }
   ```

1. Output the RFC template JSON file to a file named CreateIamResourceRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateIamResourceRfc.json
   ```

1. Modify and save the CreateIamResourceRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-1n9gfnog5x7fl",
     "Title": "{{Create entity or policy (read-write permissions)}}"
   }
   ```

1. Create the RFC, specifying the CreateIamResourceRfc file and the CreateIamResourceParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateIamResourceRfc.json  --execution-parameters file://CreateIamResourceParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-iam-entity-create-tip"></a>
+ After an IAM role is provisioned in your account, depending on the role and the policy document you attach to the role, you may need to onboard the role in your federation solution. 
+ For information about AWS Identity and Access Management, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and for policy information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html). For information about AMS permissions, see [Deploying IAM resources](https://docs.aws.amazon.com/managedservices/latest/userguide/deploy-iam-resources.html).

## Update IAM entity or policy
<a name="ex-iam-entity-update-col"></a>

### Updating IAM entity or policy with the console
<a name="iam-entity-update-con"></a>

![Update Entity or Policy change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiIamEntityUpdateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating IAM entity or policy with the CLI
<a name="iam-entity-update-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1e0xmuy1diafq" --change-type-version "1.0" --title "{{Update role or policy}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-HandleAutomatedIAMProvisioningUpdate-Admin\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"ValidateOnly\":\"{{No}}\"},\"RoleDetails\":{{{\"Roles\":[{\"RoleName\":\"RoleTest01\",\"Description\":\"This is a test role\",\"AssumeRolePolicyDocument\":\"{\\\"Version\\\":\\\"2012-10-17\\\",\\\"Statement\\\":[{\\\"Effect\\\":\\\"Allow\\\",\\\"Principal\\\":{\\\"AWS\\\":\\\"arn:aws:iam::123456789012:root\\\"},\\\"Action\\\":\\\"sts:AssumeRole\\\"}]}\",\"ManagedPolicyArns\":[\"arn:aws:iam::123456789012:policy/policy01\",\"arn:aws:iam::123456789012:policy/policy02\"],\"MaxSessionDuration\":\"7200\",\"PermissionsBoundary\":\"arn:aws:iam::123456789012:policy/permission_boundary01\"}]}}},\"ManagedPolicyDetails\":{{{\"Policies\":[{\"ManagedPolicyName\":\"TestPolicy01\",\"PolicyDocument\":\"{\\\"Version\\\":\\\"2012-10-17\\\",\\\"Statement\\\":[{\\\"Sid\\\":\\\"AllQueueActions\\\",\\\"Effect\\\":\\\"Allow\\\",\\\"Action\\\":\\\"sqs:ListQueues\\\",\\\"Resource\\\":\\\"*\\\",\\\"Condition\\\":{\\\"ForAllValues:StringEquals\\\":{\\\"aws:tagKeys\\\":[\\\"temporary\\\"]}}}]}\"}]}}}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; example names it UpdateIamResourceParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1e0xmuy1diafq" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateIamResourceParams.json
   ```

1. Modify and save the UpdateIamResourceParams file; example creates an IAM Role with policy documents pasted inline.

   ```
   {
     "DocumentName": "AWSManagedServices-HandleAutomatedIAMProvisioningUpdate-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "ValidateOnly": "{{No}}"
     },
     "RoleDetails": {
       "Roles": [
         {
           "RoleName": "{{RoleTest01}}",
           "Description": "{{This is a test role}}",
           "AssumeRolePolicyDocument": {"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"{{Allow}}","Principal":{"AWS":"{{arn:aws:iam::123456789012:root}}"},"Action":"{{sts:AssumeRole}}"}]},
           "ManagedPolicyArns": [
             "{{arn:aws:iam::123456789012:policy/policy01}}",
             "{{arn:aws:iam::123456789012:policy/policy02}}"
           ],
           "MaxSessionDuration": "{{7200}}",
           "PermissionsBoundary": "{{arn:aws:iam::123456789012:policy/permission_boundary01}}"
         }
       ]
     },
     "ManagedPolicyDetails": {
       "Policies": [
         {
           "ManagedPolicyName": "{{TestPolicy01}}",
           "PolicyDocument": {"Version": "2012-10-17",		 	 	 "Statement":[{"Sid":"{{AllQueueActions}}","Effect":"{{Allow}}","Action":"{{sqs:ListQueues}}","Resource":"{{*}}","Condition":{"{{ForAllValues:StringEquals}}":{"{{aws:tagKeys}}":["{{temporary}}"]}}}]}
         }
       ]
     }
   }
   ```

1. Output the RFC template JSON file to a file named UpdateIamResourceRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateIamResourceRfc.json
   ```

1. Modify and save the UpdateIamResourceRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
       "ChangeTypeVersion": "1.0",
       "ChangeTypeId": "ct-1e0xmuy1diafq",
       "Title": "{{Update entity or policy (read-write permissions)}}"
   }
   ```

1. Create the RFC, specifying the UpdateIamResourceRfc file and the UpdateIamResourceParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateIamResourceRfc.json  --execution-parameters file://UpdateIamResourceParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-iam-entity-update-tip"></a>
+ For information about AWS Identity and Access Management, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and for policy information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html). For information about AMS permissions, see [Deploying IAM resources](https://docs.aws.amazon.com/managedservices/latest/userguide/deploy-iam-resources.html).

## Delete IAM entity or policy
<a name="ex-iam-entity-delete-col"></a>

### Deleting IAM entity or policy with the console
<a name="iam-entity-delete-con"></a>

![Delete Entity or Policy change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiIamEntityDeleteCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting IAM entity or policy with the CLI
<a name="iam-entity-delete-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-17cj84y7632o6" --change-type-version "1.0" --title "Delete role or policy" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-HandleAutomatedIAMProvisioningDelete-Admin\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"RoleName\":[\"{{TestRole01}}\",\"{{TestRole02}}\"],\"ManagedPolicyName\":[\"{{TestPolicy01}}\",\"{{TestPolicy02}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; example names it DeleteIamResourceParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-17cj84y7632o6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteIamResourceParams.json
   ```

1. Modify and save the DeleteIamResourceParams file; example creates an IAM Role with policy documents pasted inline.

   ```
   {
     "DocumentName" : "AWSManagedServices-HandleAutomatedIAMProvisioningDelete-Admin",
     "Region" : "{{us-east-1}}",
     "Parameters": {
       "RoleName": ["{{TestRole01}}", "{{TestRole02}}"],
       "ManagedPolicyName": ["{{TestPolicy01}}", "{{TestPolicy02}}"]
     }
   }
   ```

1. Output the RFC template JSON file to a file named DeleteIamResourceRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteIamResourceRfc.json
   ```

1. Modify and save the DeleteIamResourceRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
       "ChangeTypeVersion": "1.0",
       "ChangeTypeId": "ct-17cj84y7632o6",
       "Title": "{{Delete entity or policy (read-write permissions)}}"
   }
   ```

1. Create the RFC, specifying the DeleteIamResourceRfc file and the DeleteIamResourceParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteIamResourceRfc.json  --execution-parameters file://DeleteIamResourceParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-iam-entity-delete-tip"></a>
+ For information about AWS Identity and Access Management, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and for policy information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html). 

## Update detailed monitoring
<a name="ex-ec2-update-detailed-mon-col"></a>

### Updating EC2 instances with the Console
<a name="ec2-update-detailed-mon-con"></a>

Screenshot of this change type in the AMS console:

![Update Detailed Monitoring page showing ID, execution mode as Automated, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEc2UpdateDetailedMonCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating EC2 instances with the CLI
<a name="ec2-update-detailed-mon-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title "Update EC2 detailed monitoring" -update --change-type-id ct-0tmpmp1wpgkr9 --change-type-version 1.0 --execution-parameters '{"DocumentName":"AWSManagedServices-UpdateInstanceEnhancedMonitoring","Region":"{{us-east-1}}","Parameters":{"InstanceIds":["{{i-09d65b13db992e8d4}}","{{i-0cdbd78ad80d2378c}}"]}}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it UpdateEc2MonitoringParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0tmpmp1wpgkr9" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateEc2MonitoringParams.json
   ```

1. Modify and save the UpdateEc2MonitoringParams file, retaining only the parameters that you want to change. For example, you can replace the contents with something like this: 

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateInstanceEnhancedMonitoring",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "InstanceIds": [
         "{{i-09d65b13db992e8d4}}",
         "{{i-0cdbd78ad80d2378c}}"
       ],
       "MonitoringValue": "{{enabled}}"
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it UpdateEc2MonitoringRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateEc2MonitoringRfc.json
   ```

1. Modify and save the UpdateEc2MonitoringRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-0tmpmp1wpgkr9",
   "Title":                "{{EC2 Update Detailed Monitoring}}"
   }
   ```

1. Create the RFC, specifying the UpdateEc2MonitoringRfc file and the UpdateEc2MonitoringParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateEc2MonitoringRfc.json  --execution-parameters file://UpdateEc2MonitoringParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ec2-update-detailed-mon-tip"></a>

To learn more about Amazon EC2, see [Amazon Elastic Compute Cloud Documentation](https://aws.amazon.com/documentation/ec2/). 

## Share directory
<a name="ex-dirserv-dir-share-col"></a>

### Share a directory with the console
<a name="dirserv-dir-share-con"></a>

The following shows this change type in the AMS console.

![Share Directory details page showing ID, execution mode as Automated, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiDirservShareDirectoryCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Share a directory with the CLI
<a name="dirserv-dir-share-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm  create-rfc --change-type-id "ct-369odosk0pd9w" --change-type-version "1.0" --title "{{Share Directory}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-ShareDirectory\",\"Region\":\"{{ap-southeast-2}}\",\"Parameters\":{\"DirectoryId\":[\"{{d-123456ab7c}}\"],\"TargetAccountId\":[\"{{012345678912}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DirectorySharingParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-369odosk0pd9w" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DirectorySharingParams.json
   ```

   Modify and save the DirectorySharingParams.json file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-ShareDirectory",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "DirectoryId": [
         "{{d-123456ab7c}}"
       ],
       "TargetAccountId": [
         "{{012345678912}}"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it DirectorySharingRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DirectorySharingRfc.json
   ```

1. Modify and save the DirectorySharingRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeId": "ct-369odosk0pd9w",
     "ChangeTypeVersion": "1.0",
     "Title": "{{Share Directory}}"
   }
   ```

1. Create the RFC, specifying the DirectorySharingRfc file and the DirectorySharingParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DirectorySharingRfc.json --execution-parameters file://DirectorySharingParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-dirserv-dir-share-tip"></a>

For related CTs, see [Directory Service Subcategory](https://docs.aws.amazon.com/managedservices/latest/ctref/management-directory-service-section.html). 

## Unshare directory
<a name="ex-dirserv-dir-unshare-col"></a>

### Unshare a directory with the console
<a name="dirserv-dir-unshare-con"></a>

The following shows this change type in the AMS console.

![Unshare Directory change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiDirservUnshareDirectoryCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Unshare a directory with the CLI
<a name="dirserv-dir-unshare-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm  create-rfc --change-type-id "ct-2xd2anlb5hbzo" --change-type-version "1.0" --title "Unshare Directory" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-ShareDirectory\",\"Region\":\"{{ap-southeast-2}}\",\"Parameters\":{\"DirectoryId\":[\"{{d-123456ab7c}}\"],\"UnshareTarget\":[\"{{012345678912}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DirectoryUnsharingParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2xd2anlb5hbzo" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DirectoryUnsharingParams.json
   ```

   Modify and save the DirectoryUnsharingParams.json file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UnshareDirectory",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "DirectoryId": [
         "{{d-123456ab7c}}"
       ],
       "UnshareTarget": [
         "{{012345678912}}"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it DirectoryUnsharingRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DirectoryUnsharingRfc.json
   ```

1. Modify and save the DirectoryUnsharingRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeId": "ct-2xd2anlb5hbzo",
     "ChangeTypeVersion": "1.0", 
     "Title": "{{Unshare Directory}}"
   }
   ```

1. Create the RFC, specifying the DirectoryUnsharingRfc file and the DirectoryUnsharingParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DirectoryUnsharingRfc.json --execution-parameters file://DirectoryUnsharingParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-dirserv-dir-unshare-tip"></a>

For related CTs, see [Directory Service Subcategory](https://docs.aws.amazon.com/managedservices/latest/ctref/management-directory-service-section.html). 

## Create VPC endpoint
<a name="ex-vpc-interface-create-col"></a>

### Creating a VPC endpoint with the console
<a name="vpc-interface-create-con"></a>

The following shows this change type in the AMS console.

![Create VPC Endpoint Interface change type showing ID, execution mode as Automated, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiVpcEndpointCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a VPC endpoint with the CLI
<a name="vpc-interface-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3oafsdbzjtuqp" --change-type-version "1.0" --title "Create VPC Endpoint" --execution-parameters "{\"Description\":\"{{VPC endpoint interface}}\",\"VpcId\":\"{{vpc-1234567890abcdef0}}\",\"Name\":\"{{VPC endpoint interface}}\",\"StackTemplateId\":\"{{stm-f0cumpt1rfc1p1739}}\",\"TimeoutInMinutes\":{{60}},\"Parameters\":{\"VpcId\":\"{{vpc-1234567890abcdef0}}\",\"ServiceName\":\"{{com.amazonaws.us-east-1.codedeploy}}\",\"SecurityGroups\":[\"{{sg-1234567890abcdef0}}\",\"{{sg-1234567890abcdef1}}\"],\"SubnetIds\":[\"{{subnet-1234567890abcdef0}}\",\"{{subnet-1234567890abcdef1}}\"],\"EnablePrivateDns\":\"{{false}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it VPCEndpointCreateParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3oafsdbzjtuqp" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > VPCEndpointCreateParams.json
   ```

1. Modify and save the execution parameters as VPCEndpointCreateParams.json. For example, you can replace the contents with something like this:

   ```
   {
     "Description": "VPC endpoint interface",
     "VpcId": "{{vpc-1234567890abcdef0}}",
     "Name": "VPC endpoint interface",
     "StackTemplateId": "{{stm-f0cumpt1rfc1p1739}}",
     "TimeoutInMinutes": {{60}},
     "Parameters": {
       "VpcId": "{{vpc-1234567890abcdef0}}",
       "ServiceName": "{{com.amazonaws.us-east-1.codedeploy}}",
       "SecurityGroups": [
         "{{sg-1234567890abcdef0}}",
         "{{sg-1234567890abcdef1}}"
       ],
       "SubnetIds": [
         "{{subnet-1234567890abcdef0}}",
         "{{subnet-1234567890abcdef1}}"
       ],
       "EnablePrivateDns": "{{false}}"
     }
   }
   ```

1. Output the RFC template JSON file; this example names it VPCEndpointCreateRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > VPCEndpointCreateRfc.json
   ```

1. Modify and save the VPNGatewayCreateRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-3oafsdbzjtuqp",
     "Title" : "{{Create VPC Endpoint }}"
   }
   ```

1. Create the RFC, specifying the VPCEndpointCreateRfc file and the VPCEndpointCreateParams file:

   ```
   aws amscm create-rfc --cli-input-json file://VPCEndpointCreateRfc.json  --execution-parameters file://VPCEndpointCreateParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-vpc-endpoint-interface-create-tip"></a>

## Update RDS storage
<a name="ex-rds-update-storage-col"></a>

### Updating RDS storage with the Console
<a name="rds-update-storage-con"></a>

Screenshot of this change type in the AMS console:

![Update RDS Storage change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsUpdateStorageCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating RDS storage with the CLI
<a name="rds-update-storage-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0loed9dzig1ze" --change-type-version "1.0" --title "{{Update RDS storage}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateRDSStorage\",\"Region\":\"{{us-east-1}}\",\"Parameters\": {\"DBInstanceIdentifier\":[\"{{rt123456789}}\"], \"AllocatedStorage\": [\"{{100}}\"],,\"ApplyImmediately\": \"{{true}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdateStorageParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-0loed9dzig1ze" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateStorageParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateRDSStorage",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "DBInstanceIdentifier": [
         "{{rt123456789}}"
       ],
       "AllocatedStorage": [
         "{{100}}"
       ],
       "ApplyImmediately": "{{false}}"
     }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateStorageRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateStorageRfc.json
   ```

1. Modify and save the UpdateStorageRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-0loed9dzig1ze",
   "Title":                "{{Update RDS storage}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateStorageRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateStorageRfc.json --execution-parameters file://UpdateStorageParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-rds-update-storage-tip"></a>

**Note**  
AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance." 

To learn more about Amazon RDS, including size recommendations, see [Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/).

To update an RDS stack for Aurora, see [RDS Database Stack \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-rds-database-stack-update-for-aurora.html). 

## Update an RDS multi-AZ deployment
<a name="ex-rds-update-multi-az-col"></a>

### Updating an RDS multi-AZ deployment with the Console
<a name="rds-update-multi-az-con"></a>

Screenshot of this change type in the AMS console:

![Change RDS MultiAZ Setting page showing ID, execution mode, version, classification, and description.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsUpdateMultiAzCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating an RDS multi-AZ deployment with the CLI
<a name="rds-update-multi-az-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-36jq7gvwyty8h" --change-type-version "1.0" --title "{{Update RDS Multiple AZ}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateRDSMultiAZ\",\"Region\":\"{{us-east-1}}\",\"Parameters\": {\"DBInstanceIdentifier\":[\"{{rt123456789}}\"], \"MultiAZ\": \"{{true}}\",\"ApplyImmediately\": \"{{true}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdateMultipleAzParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-36jq7gvwyty8h" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateMultipleAzParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateRDSMultiAZ",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "DBInstanceIdentifier": [
         "{{rt123456789}}"
       ],
       "MultiAZ": "{{true}}",
       "ApplyImmediately": "{{false}}"
     }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateMultipleAzRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateMultipleAzRfc.json
   ```

1. Modify and save the UpdateMultipleAzRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-36jq7gvwyty8h",
   "Title":                "{{Update RDS Multiple AZ}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateMultipleAzRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateMultipleAzRfc.json --execution-parameters file://UpdateMultipleAzParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-rds-update-multi-az-tip"></a>

**Note**  
AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance." 

To learn more about Amazon RDS, including size recommendations, see [Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/).

To update an RDS stack for Aurora, see [RDS Database Stack \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-rds-database-stack-update-for-aurora.html). 

## Update an RDS instance type
<a name="ex-rds-update-instance-type-col"></a>

### Updating an RDS instance type with the Console
<a name="rds-update-instance-type-con"></a>

Screenshot of this change type in the AMS console:

![Update Instance Type page showing ID, execution mode, version, classification path, and description.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsUpdateInstanceTypeCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating an RDS instance type with the CLI
<a name="rds-update-instance-type-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-13swbwdxg106z" --change-type-version "1.0" --title "{{Update rds instance type}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateRDSInstanceType\",\"Region\":\"{{us-east-1}}\",\"Parameters\": {\"DBInstanceIdentifier\":[\"{{rt123456789}}\"], \"DBInstanceClass\": [\"{{db.m4.large}}\"],\"ApplyImmediately\": \"{{true}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdateInstanceTypeParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-13swbwdxg106z" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateInstanceTypeParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateRDSInstanceType",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "DBInstanceIdentifier": [
         "{{rt123456789}}"
       ],
       "DBInstanceClass": [
         "{{db.m4.large}}"
       ],
       "ApplyImmediately": "{{false}}"
     }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateInstanceTypeRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateInstanceTypeRfc.json
   ```

1. Modify and save the UpdateInstanceTypeRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-13swbwdxg106z",
   "Title":                "{{Update RDS instance type}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateInstanceTypeRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateInstanceTypeRfc.json --execution-parameters file://UpdateInstanceTypeParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-rds-update-instance-type-tip"></a>

**Note**  
AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance." 

To learn more about Amazon RDS, including size recommendations, see [Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/).

To update an RDS stack for Aurora, see [RDS Database Stack \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-rds-database-stack-update-for-aurora.html). 

## Update S3 bucket versioning
<a name="ex-s3-update-versioning-col"></a>

### Updating S3 bucket versioning with the Console
<a name="s3-update-versioning-con"></a>

Screenshot of this change type in the AMS console:

![Change S3 Bucket Versioning Setting page showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiS3UpdateVersioningCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating S3 bucket versioning with the CLI
<a name="s3-update-versioning-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2hh93eyzmwbkd" --change-type-version "1.0" --title "{{Update bucket versioning}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateBucketVersioning\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"BucketName\":[\"{{BucketName}}\"],\"Versioning\": \"{{Enabled}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdateBucketVersioningParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-2hh93eyzmwbkd" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateBucketVersioningParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateBucketVersioning",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "BucketName": [
         "{{BucketName}}"
       ],
       "Versioning": "{{Enabled}}"
     }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateBucketVersioningRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateBucketVersioningRfc.json
   ```

1. Modify and save the UpdateBucketVersioningRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-2hh93eyzmwbkd",
   "Title":                "{{Update bucket versioning}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateRdsRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateBucketVersioningRfc.json --execution-parameters file://UpdateBucketVersioningParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-s3-update-versioning-tip"></a>

To learn more about Amazon S3, see [Amazon Simple Storage Service Documentation](https://aws.amazon.com/documentation/s3/).

## Update S3 bucket encryption
<a name="ex-s3-update-encryption-col"></a>

### Updating S3 bucket encryption with the Console
<a name="s3-update-encryption-con"></a>

Screenshot of this change type in the AMS console:

![Change S3 Bucket Encryption Setting page showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiS3UpdateEncryptionCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating S3 bucket encryption with the CLI
<a name="s3-update-encryption-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-128svy9nn2yj8" --change-type-version "1.0" --title "{{Update bucket encryption}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateBucketEncryption\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"BucketName\":[\"{{BucketName}}\"],\"ServerSideEncryption\": \"{{KmsManagedKeys}}\",\"KMSKeyId\":[\"{{01234567-abcd-abcd-abcd-0123456789ab}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdateBucketEncryptionParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-128svy9nn2yj8" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateBucketEncryptionParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateBucketEncryption",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "BucketName": [
         "{{BucketName}}"
       ],
       "ServerSideEncryption": "KmsManagedKeys",
       "KMSKeyId": [
         "{{01234567-abcd-abcd-abcd-0123456789ab}}"
       ]
     }
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateBucketEncryptionRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateBucketEncryptionRfc.json
   ```

1. Modify and save the UpdateBucketEncryptionRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-128svy9nn2yj8",
   "Title":                "{{Update bucket encryption}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateBucketEncryptionRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateBucketEncryptionRfc.json --execution-parameters file://UpdateBucketEncryptionParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-s3-update-encryption-tip"></a>

To learn more about Amazon S3, see [Amazon Simple Storage Service Documentation](https://aws.amazon.com/documentation/s3/).

## Updating an application account (Managed Automation)
<a name="ex-man-lz-app-acct-update-rr-col"></a>

### Updating an application account with the Console
<a name="man-lz-app-acct-update-rr-con"></a>

Screenshot of this change type in the AMS console:

![Create Application Account VPC interface showing description, ID ct-1j3503fres5a5, and version 3.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiMalzAppAcctCreateVpcCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating an application account with the CLI
<a name="man-lz-app-acct-update-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:
**Note**  
Run this change type from your Application account.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0fuztxgwy37rf" --change-type-version "1.0" --title "{{Child Application Account RFC}}" --execution-parameters ""{\"RfcId\":\"{{7cc277c6-9b55-1f63-361b-5811fce9f830}}\",\"Comment\":\"{{test RFC}}\"}""
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateAppAcctVpcParams.json: 

   ```
   aws amscm get-change-type-version --change-type-id "ct-0fuztxgwy37rf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateAppAcctParams.json
   ```

1. Modify and save the UpdateAppAcctParams file. For example, you can replace the contents with something like this:

   ```
   {
     "RfcId": "{{7cc277c6-9b55-1f63-361b-5811fce9f830}}",
     "Comment": "{{test RFC}}"
   }
   ```

1. Output the RFC template JSON file to a file; this example names it UpdateAppAcctRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateAppAcctRfc.json
   ```

1. Modify and save the UpdateAppAcctRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-0fuztxgwy37rf",
   "Title":                "{{Child Application Account RFC}}"
   }
   ```

1. Create the RFC, specifying the UpdateAppAcctRfc file and the UpdateAppAcctParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateAppAcctRfc.json  --execution-parameters file://UpdateAppAcctParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-man-lz-app-acct-update-rr-tip"></a>
+ 
**Important**  
To create an additional public subnet in a new availability zone (AZ), a private subnet must already be present.
+ This change type is now at version 3.0 and it has been automated (it is no longer manually run by AMS). The 2.0 version of this change type was a "managed automation" (manual) change type.
+ To learn more about AMS multi-account landing zone, see [ VPC sharing: A new approach to multiple accounts and VPC management](https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/).

## Associate private IP addresses (Managed Automation) ct-1pvlhug439gl2
<a name="ex-ec2-associate-ip-rr-col"></a>

### Associate private IP addresses with the console
<a name="ec2-associate-ip-rr-con"></a>

The following shows this change type in the AMS console.

![Console interface showing details for associating private IP addresses to an EC2 instance.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEc2AssociateIpRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a pre-ingest instance with the CLI
<a name="ec2-associate-ip-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --title="Associate Private IP Addresses" --description="{{Associate Private IP Addresses}}" --ct-id="ct-1pvlhug439gl2" --ct-version="1.0" --input-params="{\"NetworkInterfaceId\":\"{{eni-0123456789abcdef0}}\",\"PrivateIpAddresses\":[\"{{10.0.0.82}}\",\"{{10.0.0.83}}\"]}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it AssociatePrivateIPAddressesParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1pvlhug439gl2" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AssociatePrivateIPAddressesParams.json
   ```

1. Modify and save the AssociatePrivateIPAddressesParams file. For example, you can replace the contents with something like this:

   ```
   {
       "NetworkInterfaceId": "{{eni-0123456789abcdef0}}",
       "PrivateIpAddresses": ["{{10.0.0.82}}", "{{10.0.0.83}}"]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it AssociatePrivateIPAddressesRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > AssociatePrivateIPAddressesRfc.json
   ```

1. Modify and save the AssociatePrivateIPAddressesRfc.json file. For example, you can replace the contents with something like this:.

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-1pvlhug439gl2",
     "Title": "{{Associate Private IP Addresses}}"
   }
   ```

1. Create the RFC, specifying the AssociatePrivateIPAddressesRfc file and the AssociatePrivateIPAddressesParams file:

   ```
   aws amscm create-rfc --cli-input-json file://AssociatePrivateIPAddressesRfc.json  --execution-parameters file://AssociatePrivateIPAddressesParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ec2-associate-ip-rr-tip"></a>

For more information about Amazon EC2 IP addresses, see [ Amazon EC2 instance IP addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html). 

If needed, see [EC2 instance stack create fail](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-troubleshoot.html#rfc-valid-execute-ec2-create).

## Create Amazon RDS option group (Managed Automation)
<a name="ex-rds-create-option-group-rr-col"></a>

### Creating an Amazon RDS Option Group with the Console
<a name="rds-create-option-group-rr-con"></a>

Screenshot of this change type in the AMS console:

![AMS Advanced console, create RFC section, change type details box for ct-10yi1sd9nst1c: Create Amazon RDS option group (managed automation).](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsCreateOptionGroupCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating an Amazon RDS Option Group with the CLI
<a name="rds-create-option-group-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-10yi1sd9nst1c" --change-type-version "1.0" --title "{{Create option group (managed automation)}}" --execution-parameters "{\"OptionGroupName\": \"{{CreatingTheOptionGroup}}\", \"Description\": \"{{RDS option group}}\", \"EngineName\": \"{{sqlserver-ee}}\", \"MajorEngineVersion\": \"{{10.01}}\", \"DBInstanceName\": \"{{database-1}}\", \"Priority\": \"{{Medium}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named CreateRdsOptionGroupParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-10yi1sd9nst1c" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateRdsOptionGroupParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "OptionGroupName": "{{OptionGroup}}",
     "EngineName": "{{sqlserver-ee}}",
     "MajorEngineVersion": "{{10.01}}"
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it CreateRdsOptionGroupRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateRdsOptionGroupRfc.json
   ```

1. Modify and save the CreateRdsOptionGroupRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-10yi1sd9nst1c",
   "Title":                "{{RDS-Create-RFC}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the CreateRdsOptionGroupRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateRdsOptionGroupRfc.json --execution-parameters file://CreateRdsOptionGroupParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-rds-create-option-group-rr-tip"></a>
+ To learn more about Amazon RDS DB option groups, see [Working with option groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html).
+ You can add up to 50 tags, but to do so you must enable the **Advanced** view.

## Remove TGW static route
<a name="ex-man-lz-net-acct-tgw-route-remove-col"></a>

### Networking account: Remove a TGW static route with the Console
<a name="ex-man-lz-net-acct-tgw-route-remove-con"></a>

Screenshot of this change type in the AMS console:

![Remove TGW Static Route change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiMalzNetAcctTgwRouteRemoveCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Networking account: Remove a TGW static route with the CLI
<a name="man-lz-net-acct-tgw-route-remove-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*: 

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0rmgrnr9w8mzh" --change-type-version "1.0" --title "{{Remove TGW Static Route}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-RemoveRouteFromTGWRouteTable\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"TransitGatewayRouteTableId\": \"{{tgw-rtb-06ddc751c0c0c881c}}\", \"DestinationCidrBlock\": \"{{10.16.1.0/24}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it RemoveTgwStaticRouteParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0rmgrnr9w8mzh" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > RemoveTgwStaticRouteParams.json
   ```

1. Modify and save the RemoveTgwStaticRouteParams file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-RemoveRouteFromTGWRouteTable",
     "Region": "us-east-1",
     "Parameters": {
       "TransitGatewayRouteTableId": "tgw-rtb-06ddc751c0c0c881c",
       "DestinationCidrBlock": "10.16.1.0/24"
     }
   }
   ```

1. Output the RFC template JSON file to a file; this example names it RemoveTgwStaticRouteRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > RemoveTgwStaticRouteRfc.json
   ```

1. Modify and save the RemoveTgwStaticRouteRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-0rmgrnr9w8mzh",
     "Title": "{{Remove TGW Static Route}}"
   }
   ```

1. Create the RFC, specifying the RemoveTgwStaticRouteRfc file and the RemoveTgwStaticRouteParams file:

   ```
   aws amscm create-rfc --cli-input-json file://RemoveTgwStaticRouteRfc.json  --execution-parameters file://RemoveTgwStaticRouteParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-man-lz-net-acct-tgw-route-remove-tip"></a>

**Note**  
This Change Type is only valid in Multi-account Landing Zone (MALZ) Networking accounts.

To learn more about AMS multi-account landing zones, see [AWS Managed Services (AMS) Now Offers Managed Landing Zones](https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/).

## Create for WIGS (Managed Automation)
<a name="ex-ec2-create-preingest-col"></a>

### Creating an instance for WIGS with the console
<a name="ec2-create-preingest-con"></a>

The following shows this change type in the AMS console.

![Create EC2 for WIGS change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEc2CreatePreIngestRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating an instance for WIGS with the CLI
<a name="ec2-create-preingest-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-36emj2uapfbu8" --change-type-version "2.0" --title "{{Create Pre-Ingestion Instance}}" --execution-parameters "{\"InstanceVpcId\": \"{{vpc-1234567890abcdef0}}\",\"InstanceAmiId\": \"{{ami-1234567890abcdef0}}\",\"InstanceEBSOptimized\": {{false}},\"InstanceRootVolumeSize\": {{60}},\"InstanceNameTagValue\": \"{{temp-wigs}}\",\"InstanceType\": \"{{t3.large}}\",\"InstanceSubnetId\": \"{{subnet-0bb1c79de3EXAMPLE}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it CreateEc2PreIngestParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-36emj2uapfbu8" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateEc2PreIngestParams.json
   ```

1. Modify and save the CreateEc2PreIngestParams file. For example, you can replace the contents with something like this:

   ```
   {
       "InstanceVpcId": "{{vpc-1234567890abcdef0}}",
       "InstanceAmiId": "{{ami-1234567890abcdef0}}",
       "InstanceEBSOptimized": {{false}},    
       "InstanceRootVolumeSize": {{60}},
       "InstanceSubnetId": "{{subnet-1234567890abcdef0}}",
       "InstanceType": "{{t3.large}}",
       "InstanceNameTagValue": "{{temp-wigs}}",   
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateEc2PreIngestRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateEc2PreIngestRfc.json
   ```

1. Modify and save the CreateEc2PreIngestRfc.json file. For example, you can replace the contents with something like this:.

   ```
   {
       "ChangeTypeVersion": "2.0",
       "ChangeTypeId": "ct-36emj2uapfbu8",
       "Title": "Create Pre-Ingestion Instance"
   }
   ```

1. Create the RFC, specifying the CreateEc2PreIngestRfc file and the CreateEc2PreIngestParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateEc2PreIngestRfc.json  --execution-parameters file://CreateEc2PreIngestParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ec2-create-preingest-tip"></a>
+ To use the AWS Marketplace AMI, you must subscribe to the AMI from your AWS Marketplace account and agree to the terms of the AMI. AMS can't perform these actions for you because, as a buyer, you perform these actions yourself. If you need additional IAM permissions for these actions, use the [ Identity and Access Management (IAM) \| Create EC2 Instance Profile](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-identity-and-access-management-iam-create-ec2-instance-profile.html) change type in a separate RFC to request them.

## Modify EBS volume
<a name="ex-ebs-modify-col"></a>

### Modifying an EBS Volume with the Console
<a name="ebs-modify-con"></a>

Screenshot of this change type, in the AMS console:

![Modify EBS Volume page showing description, ID ct-1wle0ai4en6km, and version 1.0 only version.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEbsModifyCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Modifying an EBS Volume with the CLI
<a name="ebs-modify-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1wle0ai4en6km" --change-type-version "2.0" --title "Modify EBS Volume" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-ModifyEBSVolumes\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"VolumeIds\":[\"{{vol-1234567890abcdef1}}\",\"{{vol-1234567890abcdef2}}\",\"{{vol-1234567890abcdef3}}\",\"{{vol-1234567890abcdef4}}\",\"{{vol-1234567890abcdef5}}\"],\"CreateSnapshot\":[\"{{False}}\"],\"VolumeType\":[\"{{gp3}}\"],\"VolumeSize\":[\"{{40}}\"],\"Iops\":[\"{{3000}}\"],\"Throughput\":[\"{{200}}\"],\"RemediateStackDrift\":[\"{{False}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it ModifyEBSVolumeParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1wle0ai4en6km" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ModifyEBSVolumeParams.json
   ```

1. Modify and save the ModifyEBSVolumeParams file.

   ```
       {
     "DocumentName" : "AWSManagedServices-ModifyEBSVolumes",
     "Region" : "{{us-east-1}}",
     "Parameters" : {
       "VolumeIds" : [
               "{{vol-1234567890abcdef1}}",
               "{{vol-1234567890abcdef2}}",
               "{{vol-1234567890abcdef3}}",
               "{{vol-1234567890abcdef4}}",
               "{{vol-1234567890abcdef5}}"
           ],
       "CreateSnapshot" : [
         "{{False}}"
       ],
       "VolumeType" : [
         "{{gp3}}"
       ],
       "VolumeSize" : [
         "{{40}}"
       ],
       "Iops" : [
         "{{3000}}"
       ],
       "Throughput" : [
         "{{200}}"
       ],
       "RemediateStackDrift" : [
         "{{False}}"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it ModifyEBSVolumeRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ModifyEBSVolumeRfc.json
   ```

1. Modify and save the ModifyEBSVolumeRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "2.0",
     "ChangeTypeId": "ct-1wle0ai4en6km",
     "Title": "{{Modify EBS Volume}}"
   }
   ```

1. Create the RFC, specifying the ModifyEBSVolumeRfc file and the ModifyEBSVolumeParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ModifyEBSVolumeRfc.json --execution-parameters file://ModifyEBSVolumeParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ebs-modify-tip"></a>

To learn more about Amazon EBS, see [Amazon Elastic Block Store (EBS)](https://aws.amazon.com/ebs/).

## Update AWS Backup plan (Managed Automation)
<a name="ex-backup-backup-plan-update-col"></a>

### Updating an AWS Backup plan with the console
<a name="backup-backup-plan-update-con"></a>

The following shows this change type in the AMS console.

![Update AWS Backup Plan change type showing manual execution mode and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiAwsBackupPlanUpdateRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating an AWS Backup plan with the CLI
<a name="backup-backup-plan-update-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1ay83wy4vxa3k" --change-type-version "1.0" --title "Update AWSBackup Plan" --execution-parameters ""{\"BackupPlanName\":\"{{PLAN_NAME}}\",\"ResourceTagKey\":\"{{TAG_KEY}}\",\"ResourceTagValue\":\"{{TAG_VALUE}}\",\"BackupRuleName\":\"{{RULE_NAME}}\",\"BackupRuleVault\":\"{{VAULT}}\",\"BackupRuleCompletionWindowMinutes\":{{120}},\"BackupRuleScheduleExpression\":\"{{cron(0 1 ? * * *)}}\",\"BackupRuleDeleteAfterDays\":{{90}},\"BackupRuleMoveToColdStorageAfterDays\":{{365}},\"BackupRuleStartWindowMinutes\":{{60}},\"BackupRuleRecoveryPointTagKey\":\"{{TAG_KEY}}\",\"BackupRuleRecoveryPointTagValue\":\"{{TAG_VALUE}}\,\"BackupRuleEnableContinuousBackup\":\"{{false}}\",\"BackupRuleCopyActionsDestVaultArn\":\"{{VAULT}}\",\"BackupRuleCAMoveToColdStorageAfterDays\":{{0}},\"BackupRuleCopyActionsDeleteAfterDays\":{{90}}}""
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it UpdateBackupPlanParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1ay83wy4vxa3k" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateBackupPlanParams.json
   ```

1. Modify and save the UpdateBackupPlanParams file.

   ```
   {
     "BackupPlanName": "{{MyCustomBackupPlan}}",
     "ResourceTagKey": "{{custom_backup_test}}",
     "ResourceTagValue": "{{true}}",
     "WindowsVSS": "{{disabled}}",
     "BackupRuleName": "{{BackupRule}}",
     "BackupRuleVault": "{{ams-custom-backups}}",
     "BackupRuleCompletionWindowMinutes": {{1440}},
     "BackupRuleScheduleExpression": "{{cron(0 2 ? * * *)}}",
     "BackupRuleDeleteAfterDays": {{0}},
     "BackupRuleMoveToColdStorageAfterDays": {{0}},
     "BackupRuleStartWindowMinutes": {{180}},
     "BackupRuleRecoveryPointTagKey": "{{test}}",
     "BackupRuleRecoveryPointTagValue": "{{test}}",
     "BackupRuleEnableContinuousBackup": "{{false}}",
     "BackupRuleCopyActionsDestVaultArn": "",
     "BackupRuleCAMoveToColdStorageAfterDays": {{0}},
     "BackupRuleCopyActionsDeleteAfterDays": {{0}}
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it UpdateBackupPlanRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateBackupPlanRfc.json
   ```

1. Modify and save the UpdateBackupPlanRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-1ay83wy4vxa3k",
     "Title": "{{Update AWS Backup Plan}}"
   }
   ```

1. Create the RFC, specifying the UpdateBackupPlanRfc file and the UpdateBackupPlanParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateBackupPlanRfc.json --execution-parameters file://UpdateBackupPlanParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-backup-backup-plan-update-tip"></a>

**Note**  
 Not all resource types supported by AWS Backup are enabled by default. Review the enabled resource types in your account using [Getting Started 1: Service Opt-In](https://docs.aws.amazon.com/aws-backup/latest/devguide/service-opt-in.html). 

To learn more about AWS Backup, see [AWS Backup: How It Works](https://docs.aws.amazon.com/aws-backup/latest/devguide/how-it-works.html).

Before creating backup plans, confirm supported resources at [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource).

## Confirm offboarding
<a name="ex-man-lz-app-acct-confirm-offb-col"></a>

**Important**  
After confirming your intent to offboard the application account, you have 48 hours to run the [Management account: Offboard Application account](#ex-man-lz-man-acct-offb-app-acct-col) change type (ct-0vdiy51oyrhhm). After 48 hours, the offboarding request fails and the process of confirming and then offboarding must be restarted.

### Application account: Confirming offboarding with the Console
<a name="man-lz-app-acct-confirm-offb-con"></a>

Screenshot of this change type in the AMS console:

![Confirm Account Offboarding change type details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiManLzAppAcctConfirmOffBCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Application account: Confirming offboarding with the CLI
<a name="man-lz-app-acct-confirm-offb-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:
**Note**  
Run this change type from your Application account.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2wlfo2jxj2rkj" --change-type-version "1.0" --title "{{Confirm Offboarding}}" --execution-parameters "{\"AccountID\": \"{{000000000000}}\",\"AccountEmail\": \"{{email@amazon.com}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ConfirmAppAcctOffBParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2wlfo2jxj2rkj" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ConfirmAppAcctOffBParams.json
   ```

1. Modify and save the ConfirmAppAcctOffBParams file. For example, you can replace the contents with something like this:

   ```
   {
     "AccountID": "{{000000000000}}",
     "AccountEmail": "{{email@amazon.com}}",
   }
   ```

1. Output the RFC template JSON file to a file; this example names it ConfirmAppAcctOffBRfc.json:

   ```
       aws amscm create-rfc --generate-cli-skeleton > ConfirmAppAcctOffBRfc.json
   ```

1. Modify and save the ConfirmAppAcctOffBRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-2wlfo2jxj2rkj",
     "Title": "Confirm Offboarding"
   }
   ```

1. Create the RFC, specifying the ConfirmAppAcctOffBRfc file and the ConfirmAppAcctOffBParams file:

   ```
       aws amscm create-rfc --cli-input-json file://ConfirmAppAcctOffBRfc.json  --execution-parameters file://ConfirmAppAcctOffBParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-man-lz-app-acct-confirm-offb-tip"></a>
+ The second step to offboarding the AMS multi-account landing zone Application account is to submit the [Management account: Offboard Application account](#ex-man-lz-man-acct-offb-app-acct-col) change type (ct-0vdiy51oyrhhm) from the application account *within 48 hours* of successfully running this change type confirming the intent to offboard.
+ For application accounts (other than Customer Managed), run this from the Application account that you want offboarded. After successful confirmation, run the [Offboard application account](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-management-account-offboard-application-account.html) CT (ct-0vdiy51oyrhhm) from the associated management account. Offboarding is intended for account closure and cannot be undone.
+ Do not use this CT for Customer Managed application accounts. Go directly to [Offboard application account](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-management-account-offboard-application-account.html) CT (ct-0vdiy51oyrhhm).

## Management account: Offboard Application account
<a name="ex-man-lz-man-acct-offb-app-acct-col"></a>

**Important**  
You have 48 hours to offboard the specified application account after successfully running the [Confirm offboarding](#ex-man-lz-app-acct-confirm-offb-col) change type (ct-2wlfo2jxj2rkj). After 48 hours, the offboarding request fails and the process of confirming and then offboarding must be restarted.

**Warning**  
Before submitting this change type to initiate application account offboarding, make sure that all RFCs associated with the application account have reached a terminal state. There must be no RFCs in any of the following statuses: Editing, Pending Approval, Scheduled, or In Progress. Cancel, complete, or resolve all active RFCs before proceeding.

### Management account: Offboarding an Application account with the Console
<a name="man-lz-man-acct-offb-app-acct-con"></a>

Screenshot of this change type in the AMS console:

![Offboard Application Account page showing ID, execution mode as Automated, and version 2.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiManLzAppAcctRunOffBCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Management account: Offboarding an Application account with the CLI
<a name="man-lz-man-acct-offb-app-acct-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:
**Note**  
Run this change type from the Management account associated with the application account being offboarded.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0vdiy51oyrhhm" --change-type-version "2.0" --title "{{Run Offboarding}}" --execution-parameters "{\"AccountID\": \"{{000000000000}}\",\"AccountEmail\": \"{{email@amazon.com}}\",\"Confirmation\": \"{{confirm}}\",\"DeleteTransitGatewayAttachment\":true}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it RunAppAcctOffBParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0vdiy51oyrhhm" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > RunAppAcctOffBParams.json
   ```

1. Modify and save the RunAppAcctOffBParams file. For example, you can replace the contents with something like this:

   ```
   {
     "AccountID": "{{000000000000}}",
     "AccountEmail": "{{email@amazon.com}}",
     "Confirmation": "{{confirm}}",
     "DeleteTransitGatewayAttachment" : true
   }
   ```

1. Output the RFC template JSON file to a file; this example names it RunAppAcctOffBRfc.json:

   ```
       aws amscm create-rfc --generate-cli-skeleton > RunAppAcctOffBRfc.json
   ```

1. Modify and save the RunAppAcctOffBRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "2.0",
     "ChangeTypeId": "ct-0vdiy51oyrhhm",
     "Title": "{{Execute Offboarding}}"
   }
   ```

1. Create the RFC, specifying the RunAppAcctOffBRfc file and the RunAppAcctOffBParams file:

   ```
       aws amscm create-rfc --cli-input-json file://RunAppAcctOffBRfc.json  --execution-parameters file://RunAppAcctOffBParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="man-lz-man-acct-offb-app-acct-tip"></a>
+ The first step to offboarding the AMS multi-account landing zone Application account is to submit the [Confirm offboarding](#ex-man-lz-app-acct-confirm-offb-col) CT (ct-2wlfo2jxj2rkj) from the application account.

  Run this change type within 48 hours of successfully running the confirmation change type.
+ There is no prerequisite or confirmation CT for Customer Managed application accounts.
+ Note that offboarding is irreversible.
+ If you intend to self-operate the account after offboarding from AMS, then make sure to specify `DeleteTransitGatewayAttachment` parameter as `false` to retain connectivity.

## Deploy AMS Resource Scheduler Solution
<a name="ex-res-sched-deploy-col"></a>

### Deploying AMS Resource Scheduler solution with the console
<a name="res-sched-deploy-con"></a>

The following shows this change type in the AMS console.

![Deploy AMS Resource Scheduler change type details showing ID, execution mode, and version.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiResSchedSolutionDeployCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deploying AMS Resource Scheduler solution with the CLI
<a name="res-sched-deploy-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id ct-0ywnhc8e5k9z5 --change-type-version "2.0" --title "{{Deploy Resource Scheduler}}" --execution-parameters '{"DocumentName":"AWSManagedServices-HandleAMSResourceSchedulerStack-Admin","Region":"{{us-east-1}}","Parameters":{"SchedulingActive":["{{Yes}}"],"ScheduledServices":["{{ec2,rds,autoscaling}}"],"TagName":["{{Schedule}}"],"DefaultTimezone":["{{America/New_York}}"],"Action":["Deploy"]}}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it DeployResSchedulerParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0ywnhc8e5k9z5" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeployResSchedulerParams.json
   ```

1. Modify and save the DeployResSchedulerParams file.

   ```
   {
     "DocumentName": "AWSManagedServices-HandleAMSResourceSchedulerStack-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "SchedulingActive": [
         "{{Yes}}"
       ],
       "ScheduledServices": [
         "{{ec2,rds,autoscaling}}"
       ],
       "TagName": [
         "{{Schedule}}"
       ],
       "DefaultTimezone": [
         "{{America/New_York}}"
       ],
       "Action": [
         "Deploy"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it DeployResSchedulerRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeployResSchedulerRfc.json
   ```

1. Modify and save the DeployResSchedulerRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{2.0}}",
   "ChangeTypeId":         "ct-0ywnhc8e5k9z5",
   "Title":                "{{Deploy AMS Resource Scheduler}}"
   }
   ```

1. Create the RFC, specifying the DeployResSchedulerRfc file and the DeployResSchedulerParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeployResSchedulerRfc.json --execution-parameters file://DeployResSchedulerParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-res-sched-deploy-tip"></a>

For background information, see [How the AMS Resource Scheduler works](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-how-works.html). For a quick-start tutorial, see [AMS Resource Scheduler quick start](https://docs.aws.amazon.com/managedservices/latest/appguide/qs-resource-scheduler.html). 

AMS Resource Scheduler is based on the AWS Instance Scheduler; to learn more, see [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/welcome.html). 

## Update AMS Resource Scheduler Solution
<a name="ex-res-sched-update-col"></a>

### Updating AMS Resource Scheduler solution with the console
<a name="res-sched-update-con"></a>

The following shows this change type in the AMS console.

![Update AMS Resource Scheduler page showing ID, execution mode as Automated, and version 2.0.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiResSchedSolutionUpdateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating AMS Resource Scheduler solution with the CLI
<a name="res-sched-update-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id ct-2c7ve50jost1v --change-type-version "2.0" --title "{{Update Resource Scheduler Configurations}}" --execution-parameters '{"DocumentName":"AWSManagedServices-HandleAMSResourceSchedulerStack-Admin","Region":"{{us-east-1}}","Parameters":{"SchedulingActive":["{{Yes}}"],"ScheduledServices":["{{ec2,rds,autoscaling}}"],"TagName":["{{Schedule}}"],"DefaultTimezone":["{{America/New_York}}"],"Action":["Update"]}}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it UpdateResSchedulerParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2c7ve50jost1v" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateResSchedulerParams.json
   ```

1. Modify and save the UpdateResSchedulerParams file.

   ```
   {
     "DocumentName": "AWSManagedServices-HandleAMSResourceSchedulerStack-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "SchedulingActive": [
         "{{Yes}}"
       ],
       "ScheduledServices": [
         "{{ec2,rds,autoscaling}}"
       ],
       "TagName": [
         "{{Schedule}}"
       ],
       "DefaultTimezone": [
         "{{America/New_York}}"
       ],
       "Action": [
         "Update"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it UpdateResSchedulerRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateResSchedulerRfc.json
   ```

1. Modify and save the UpdateResSchedulerRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "2.0",
   "ChangeTypeId":         "ct-2c7ve50jost1v",
   "Title":                "{{Update Resource Scheduler Configurations}}"
   }
   ```

1. Create the RFC, specifying the UpdateResSchedulerRfc file and the UpdateResSchedulerParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateResSchedulerRfc.json --execution-parameters file://UpdateResSchedulerParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-res-sched-update-tip"></a>

For background information, see [How the AMS Resource Scheduler works](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-how-works.html). For a quick-start tutorial, see [AMS Resource Scheduler quick start](https://docs.aws.amazon.com/managedservices/latest/appguide/qs-resource-scheduler.html). 

AMS Resource Scheduler is based on the AWS Instance Scheduler; to learn more, see [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/welcome.html). 

## Delete or deactivate access key
<a name="ex-iam-key-deactivate-col"></a>

### Deleting or deactivating access key with the console
<a name="iam-key-deactivate-con"></a>

![Delete or Deactivate Access Key interface showing ID, execution mode, version, and description.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiIamKeyDeactivateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Deleting or deactivating access key with the CLI
<a name="iam-key-deactivate-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).
**Note**  
When pasting in a policy document, note that the RFC only accepts policy pastes up to 5,000 characters. If your file has more than 5,000 characters, create a service request to upload the policy and then refer to that service request in the RFC that you open for IAM.

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-37qquo9wbpa8x" --change-type-version "2.0" --title "Delete or deactivate access key" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-DeactivateIAMAccessKeyV2\",\"Region\": \"\",\"Parameters\": {\"UserName\": \"{{test-user}}\", \"AccessKeyId\": \"{{AKIAIOSFODNN7EXAMPLE}}\", \"Delete\": {{false}}}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; example names it DeactivateIamAccessKeyParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-37qquo9wbpa8x" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeactivateIamAccessKeyParams.json
   ```

1. Modify and save the DeactivateIamAccessKey file; example creates an IAM Role with policy documents pasted inline.

   ```
   {
     "DocumentName": "AWSManagedServices-DeactivateIAMAccessKeyV2",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "UserName": "{{test-user}}",
       "AccessKeyId": "{{AKIAIOSFODNN7EXAMPLE}}",
       "Delete": {{false}}
     }
     }
   }
   ```

1. Output the RFC template JSON file to a file named DeactivateIamAccessKeyRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeactivateIamAccessKeyRfc.json
   ```

1. Modify and save the DeactivateIamAccessKeyRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
       "ChangeTypeVersion": "2.0",
       "ChangeTypeId": "ct-37qquo9wbpa8x",
       "Title": "{{Delete or Deactivate Access Key}}"
   }
   ```

1. Create the RFC, specifying the DeactivateIamAccessKeyRfc.json file and the CreateIamResourceNrrParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeactivateIamAccessKeyRfc.json --execution-parameters file://DeactivateIamAccessKeyParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-iam-key-deactivate-tip"></a>
+ For information about AWS Identity and Access Management, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and for policy information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html). For information about AMS permissions, see [Deploying IAM resources](https://docs.aws.amazon.com/managedservices/latest/userguide/deploy-iam-resources.html).

## Create access key
<a name="ex-iam-key-create-col"></a>

### Creating access key with the console
<a name="iam-key-create-con"></a>

![Create Access Key runbook details showing ID, execution mode, version, and classification.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiIamKeyCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating access key with the CLI
<a name="iam-key-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).
**Note**  
When pasting in a policy document, note that the RFC only accepts policy pastes up to 5,000 characters. If your file has more than 5,000 characters, create a service request to upload the policy and then refer to that service request in the RFC that you open for IAM.

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2hhqzgxvkcig8" --change-type-version "2.0" --title "Create access key" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-CreateIAMAccessKey\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"UserARN\": \"{{arn:aws:iam::012345678910:user/myusername}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; example names it CreateIamAccessKeyParameters.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2hhqzgxvkcig8" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateIamAccessKeyParameters.json
   ```

1. Modify and save the CreateIamAccessKeyParameters.json file; example creates an IAM Role with policy documents pasted inline.

   ```
   {
       "DocumentName": "AWSManagedServices-CreateIAMAccessKey",
       "Region": "{{ap-southeast-2}}",
       "Parameters": {
           "UserARN": "{{arn:aws:iam::012345678910:user/myusername}}"
       }
     }
   }
   ```

1. Output the RFC template JSON file to a file named CreateIamAccessKeyRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateIamAccessKeyRfc.json
   ```

1. Modify and save the CreateIamAccessKeyRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "2.0",
     "ChangeTypeId": "ct-2hhqzgxvkcig8",
     "Title": "{{Create IAM access key}}"
   }
   ```

1. Create the RFC, specifying the CreateIamAccessKeyRfc.json file and the CreateIamAccessKeyParameters.json file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateIamAccessKeyRFC.json --execution-parameters file://CreateIamAccessKeyParameters.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-iam-key-create-tip"></a>
+ For information about AWS Identity and Access Management, see [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and for policy information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html). For information about AMS permissions, see [Deploying IAM resources](https://docs.aws.amazon.com/managedservices/latest/userguide/deploy-iam-resources.html).

## Enable Detailed Monitoring
<a name="ex-ec2-enable-detail-mon-rr-col"></a>

### Enable detailed monitoring with the console
<a name="ec2-enable-detail-mon-rr-con"></a>

The following shows this change type in the AMS console.

![Interface showing Enable Detailed Monitoring option for EC2 instance with execution details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEc2EnableDetailMonitoringRr.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Enable detailed monitoring with the CLI
<a name="ec2-enable-detail-mon-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-211l2gxvsrrhy" --change-type-version "1.0" --title "Enable Detailed Monitoring" --execution-parameters "{\"InstanceIds\": [\"{{i-1234567890abcdef0}}\",\"{{i-1234567890abcdef1}}\"]}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it EnableDetailedMonitoringParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-211l2gxvsrrhy" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > EnableDetailedMonitoringParams.json
   ```

1. Modify and save the EnableDetailedMonitoringParams file, retaining only the parameters that you want to change. For example, you can replace the contents with something like this: 

   ```
   {
       "InstanceIds": ["{{i-0cc489fa851c31a21}}","{{i-0cc489fa851c31a22}}"]
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it EnableDetailedMonitoringRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > EnableDetailedMonitoringRfc.json
   ```

1. Modify and save the EnableDetailedMonitoringRfc file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-211l2gxvsrrhy",
     "Title": "{{Enable Detailed Monitoring}}"
   }
   ```

1. Create the RFC, specifying the EnableDetailedMonitoringRfc file and the EnableDetailedMonitoringParams file:

   ```
   aws amscm create-rfc --cli-input-json file://EnableDetailedMonitoringRfc.json  --execution-parameters file://EnableDetailedMonitoringParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ec2-enable-detail-mon-rr-tip"></a>

For more information about Amazon EC2, including size recommendations, see [Amazon Elastic Compute Cloud Documentation](https://aws.amazon.com/documentation/ec2/).

## Update the DeleteOnTermination option (Managed Automation)
<a name="ex-ec2-update-termination-col"></a>

### Updating the DeleteOnTermination option with the Console
<a name="ec2-update-termination-con"></a>

Screenshot of this change type in the AMS console:

![Update DeleteOnTermination change type details for EC2 instance EBS volumes in AMS console.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiEc2TerminationOptionUpdateRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating the DeleteOnTermination option with the CLI
<a name="ec2-update-termination-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2aaaqid7asjy6" --change-type-version "1.0" --title "Update DeleteOnTermination" --execution-parameters "{\"InstanceId\": \"{{i-1234567890abcdef0}}\", \"DeviceNames\": [\"{{/dev/sda1}}\", \"{{/dev/xvda}}\"], \"DeleteOnTermination\": \"{{False}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it UpdateDeleteOnTerminationParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2aaaqid7asjy6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateDeleteOnTerminationParames.json
   ```

1. Modify and save the UpdateDeleteOnTerminationParams.json file, retaining only the parameters that you want to change. For example, you can replace the contents with something like this: 

   ```
   {
     "InstanceId": "{{i-0cc489fa851c31a21}}",
     "DeviceNames": [
       "{{/dev/sda1}}",
       "{{/dev/xvda}}"
     ],
     "DeleteOnTermination": "{{False}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it UpdateDeleteOnTerminationRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateDeleteOnTerminationRfc.json
   ```

1. Modify and save the UpdateDeleteOnTerminationRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-2aaaqid7asjy6",
   "Title":                "{{Update DeleteOnTermination}}"
   }
   ```

1. Create the RFC, specifying the UpdateDeleteOnTerminationRfc.json file and the UpdateDeleteOnTerminationParams.json file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateDeleteOnTerminationRfc.json  --execution-parameters file://UpdateDeleteOnTerminationParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

1. You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-ec2-update-termination-tip"></a>

To learn more about Amazon EC2, including size recommendations, see [Amazon Elastic Compute Cloud Documentation](https://aws.amazon.com/documentation/ec2/).

## Update RDS maintainance window (Managed Automation)
<a name="ex-rds-update-window-col"></a>

### Updating an RDS maintainance window with the Console
<a name="rds-update-window-con"></a>

Screenshot of this change type in the AMS console:

![Update RDS Maintenance Window change type showing ID, execution mode as Manual, and version.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsWindowUpdateRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating an RDS maintainance window with the CLI
<a name="rds-update-window-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-27jjy5wnrfef2" --change-type-version "1.0" --title "Update RDS Maintenance Window" --execution-parameters "{\"DBIdentifierArn\": \"{{arn:aws:rds:us-east-1:123456789101:db:database-1}}\", \"PreferredMaintenanceWindow\": \"{{Sun:04:00-Sun:04:30}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdateRDSMaintenanceWindowParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-27jjy5wnrfef2" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateRDSMaintenanceWindowParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DBIdentifierArn": "{{arn:aws:rds:us-east-1:123456789101:db:database-1}}",
     "PreferredMaintenanceWindow": "{{Sun:04:00-Sun:04:30}}"
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdateRDSMaintenanceWindowRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateRDSMaintenanceWindowRfc.json
   ```

1. Modify and save the UpdateRDSMaintenanceWindowRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-27jjy5wnrfef2",
     "Title": "Update RDS Maintenance Window"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateRDSMaintenanceWindowRfc.json file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateRDSMaintenanceWindowRfc.json --execution-parameters file://UpdateRDSMaintenanceWindowParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

1. You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-rds-update-window-tip"></a>

**Note**  
AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance." 

To learn more about Amazon RDS, including size recommendations, see [Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/). 

## Update RDS performance insights (Managed Automation)
<a name="ex-rds-update-insights-col"></a>

### Updating an RDS performance insights with the Console
<a name="rds-update-insights-con"></a>

Screenshot of this change type in the AMS console:

![Update Performance Insights panel showing execution mode, version, and description for RDS database tuning.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiRdsInsightsUpdateRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Updating performance insights with the CLI
<a name="rds-update-insights-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-31eyj2hlvqjwu" --change-type-version "1.0" --title "Update Performance Insights." --execution-parameters "{\"DBIdentifierArn\": \"{{arn:aws:rds:us-east-1:123456789012:cluster:database-1}}\",\"PerformanceInsights\": \"{{true}}\", \"PerformanceInsightsKMSKeyId\": \"{{default}}\", \"PerformanceInsightsRetentionPeriod\": \"{{7 days}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named UpdatePerformanceInsightsParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-31eyj2hlvqjwu" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdatePerformanceInsightsParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DBIdentifierArn": "{{arn:aws:rds:us-east-1:123456789101:cluster:database-1}}",
     "PerformanceInsights": "{{true}}",
     "PerformanceInsightsKMSKeyId": "{{default}}",
     "PerformanceInsightsRetentionPeriod": "{{7 days}}"
   }
   ```

1. Output the JSON template to a file in your current folder; this example names it UpdatePerformanceInsightsRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdatePerformanceInsightsRfc.json
   ```

1. Modify and save the UpdatePerformanceInsightsRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-31eyj2hlvqjwu",
   "Title":                "{{Update Performance Insights}}"
   }
   ```

1. Create the RFC, specifying the execution parameters file and the UpdateRdsRfc file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdatePerformanceInsightsRfc.json --execution-parameters file://UpdatePerformanceInsightsParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

1. You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-rds-update-insights-tip"></a>

**Note**  
AMS employs drift detection on certain stacks, including RDS stacks, to determine if configuration changes. The AMS disallows updates to an RDS stack that has been determined to have configuration drift. The RFC will fail with the following error message: "Update cannot be performed on this stack, please contact AMS for further assistance." 

To learn more about Amazon RDS, including size recommendations, see [Amazon Relational Database Service Documentation](https://aws.amazon.com/documentation/rds/).

To update an RDS stack for Aurora, see [RDS Database Stack \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-rds-database-stack-update-for-aurora.html). 

## Create security group (Managed Automation)
<a name="ex-sec-group-create-rr-col"></a>

### Creating a Security Group (Managed Automation) with the Console
<a name="sec-group-create-rr-con"></a>

Screenshot of this change type in the AMS console:

![Create Security Group change type showing manual execution mode and version 2.0 details.](http://docs.aws.amazon.com/managedservices/latest/ctexguide/images/guiSecGroupCreateRrCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

### Creating a Security Group (Managed Automation) with the CLI
<a name="sec-group-create-rr-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws --profile saml amscm create-rfc --change-type-id "ct-1oxx2g2d7hc90" --change-type-version "2.0" --title "{{Test-SG-RR}}" --execution-parameters "{\"Description\":\"{{Test-SG-RR}}\", \"Name\":\"{{Test-SG-IC}}\", \"InboundRules\":{\"Protocol\":\"{{TCP}}\", \"PortRange\":\"{{49152-65535}}\, \"Source\":\"{{203.0.113.5/32}}\"}, \"OutboundRules\":{\"Protocol\":\"{{TCP}}\", \"PortRange\":\"{{49152-65535}}\, \"Destination\":\"{{203.0.113.5/32}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateSgRrParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1oxx2g2d7hc90" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateSgRrParams.json
   ```

1. Modify and save the CreateSgRrParams file. For example, you can replace the contents with something like this:

   ```
   {
   "Description":      "{{SG-Create-With-Review}}",
   "Name":             "{{My-SG}}",
   "VpcId":            "{{vpc-12345abc}}",    
   "InboundRules":   {
       "Protocol":     "{{TRAFFIC_PROTOCOL}}",
       "PortRange":    "{{PORT_RANGE}}",
       "Source":       "{{TRAFFIC_SOURCE}}"
       },
   "OutboundRules":   {
       "Protocol":     "{{TRAFFIC_PROTOCOL}}",
       "PortRange":    "{{PORT_RANGE}}",
       "Destination":  "{{TRAFFIC_DESTINATION}}"
       }
   }
   ```

1. Output the RFC template JSON file to a file named CreateSgRrRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateSgRrRfc.json
   ```

1. Modify and save the CreateSgRrRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{2.0}}",
   "ChangeTypeId":         "ct-1oxx2g2d7hc90",
   "Title":                "{{SG-Create-RR-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateSgRrRfc file and the CreateSgRrParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateSgRrRfc.json  --execution-parameters file://CreateSgRrParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-sec-group-create-rr-tip"></a>

**Note**  
There is an automated change type for creating a security group, Deployment \| Advanced stack components \| Security group \| Create (no managed automation) (ct-3pc215bnwb6p7) that provides options for TCP and ICMP ingress and egress rules. If those rules are adequate, the Create (auto) change type will execute more quickly than this change type. For details, see [ Security Group \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-security-group-create.html).

**Note**  
Once the security group is created, use [ Security Group \| Associate](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-security-group-associate.html) to associate the security group with your AMS resources. In order to delete a security group, it must have associated resources.

**Note**  
Outbound rules are not required; however, if they are not specified, then a "127.0.0.1/32 Blackhole Rule" is used, meaning that the resource will only be able to communicate to itself and not with other resources. You can see this default outbound rule when using the AMS console, but not when using the AMS API/CLI.

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

To learn more about AWS security groups and creating security groups, see [ Security Group Rules Reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html); this page can help you determine the rules you want and, importantly, how to name your security group so choosing it when creating other resources is intuitive. Also see [ Amazon EC2 Security Groups for Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) and/or [ Security Groups for Your VPC](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html).

To better understand general AWS security, see [ Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/).

Once the security group is created, use [Security Group \| Associate](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-security-group-associate.html) to associate the security group with your AMS resources. In order to delete a security group, it must have associated resources.