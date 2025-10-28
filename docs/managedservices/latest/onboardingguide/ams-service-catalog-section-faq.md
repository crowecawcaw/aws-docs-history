# Service Catalog in AMS before you begin

**Does Service Catalog replace the existing AMS request for change (RFC) process?**
In accounts where Service Catalog is enabled, it will act as the change management system
in which you provision and update IT services in your AMS account through your predefined product
catalog; AMS will provide a default portfolio/product catalog, and your IT admins
can create and configure your own. Service Catalog will only acknowledge stacks provisioned through Service Catalog.
Likewise, services provisioned through Service Catalog will not be modifiable through the AMS
RFC process as modification outside of Service Catalog will drift the stack from the approved
product configuration.

**Can I see stacks provisioned through service catalog in the AMS Console?**
Yes. You can view all stacks provisioned through service catalog in the AMS console.
Stacks provisioned through service catalog are easily identifiable by the stack ID of "SC-". Although
stacks are viewable in the AMS console you will not be able to update through the AMS RFC process.
Access to the AMS change management system (RFCs) is limited to access request, patch orchestration
and back-up RFCs only.

**If I provision and/or update a stack through Service Catalog will there be a corresponding RFC
in the AMS Console?**
The only RFC that will show in the AMS console is an RFC to register the stack with AMS
when a stack is initially provisioned. This RFC is filed automatically by the AMS validation process that is
triggered when a stack is launched through Service Catalog. All other provisioning and changes are
tracked directly in Service Catalog and are viewable in the Service Catalog console. Furthermore, you
can use the **Provisioned Product Plan** feature in Service Catalog to view the list of changes that will be
made to the resources in advance of provisioning or updating the product.

**Do I have to do anything specific for provisioning products in my AMS managed account?**
Yes. All Service Catalog products provisioned in AMS accounts must contain this line of JSON in
the CFN template that defines that product:

```
"Transform":{"Name":"AmsStackTransform","Parameters":{"StackId":{"Ref":"AWS::StackId"}}}
```

This snippet of CloudFormation code triggers the AMS validations required before the resource
can be provisioned in your
AMS managed account. It is your responsibility to include this line of code as part of the product definition.
If it is not included, provisioning will fail and the following error message will be displayed:
"Failed to create product. This account is managed by AMS. All products in AMS accounts must have the
AMS `Transform` code in the template."

**Is there any Service Catalog functionality not available and/or limited for AMS customers at launch?**
Yes, the following SC features are not available for AMS customers at initial launch:

- Account Creation through Service Catalog
- Ability to launch all AWS Services through Service Catalog into an AMS-managed account.
  AWS Service availability
  is limited to AMS supported services (managed and self-provisioned). For more information on
  AMS-supported services, see the AMS service description.
- Service Catalog IT service manager (ITSM) connectors will not communicate with AMS incident reports,
  and service requests.
- Ability to leverage Service Catalog quick starts and reference architectures without
  modification. Remember that Service Catalog products for AMS accounts must contain this line of JSON code:

```
"Transform":{"Name":"AmsStackTransform","Parameters":{"StackId":{"Ref":"AWS::StackId"}}}
```

in the CNF template. Note that this line is _not_ part of a typical
AWS CloudFormation template and must be explicitly added.

- Terraform is not currently supported by AMS for provisioning Service Catalog products.
- AWS CFN stacksets are not supported in AMS.
- You cannot create custom IAM roles.
- Service Actions are limited to:

      + [AWS-RebootRdsInstance](https://console.aws.amazon.com/systems-manager/documents/AWS-RebootRdsInstance/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-RebootRdsInstance/description?region=us-east-1")
      + [AWS-RestartEC2Instance](https://console.aws.amazon.com/systems-manager/documents/AWS-RestartEC2Instance/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-RestartEC2Instance/description?region=us-east-1")
      + [AWS-StartEC2Instance](https://console.aws.amazon.com/systems-manager/documents/AWS-StartEC2Instance/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-StartEC2Instance/description?region=us-east-1")
      + [AWS-StartRdsInstance](https://console.aws.amazon.com/systems-manager/documents/AWS-StartRdsInstance/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-StartRdsInstance/description?region=us-east-1")
      + [AWS-StopEC2Instance](https://console.aws.amazon.com/systems-manager/documents/AWS-StopEC2Instance/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-StopEC2Instance/description?region=us-east-1")
      + [AWS-StopRdsInstance](https://console.aws.amazon.com/systems-manager/documents/AWS-StopRdsInstance/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-StopRdsInstance/description?region=us-east-1")
      + [AWS-CreateImage](https://console.aws.amazon.com/systems-manager/documents/AWS-CreateImage/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-CreateImage/description?region=us-east-1")
      + [AWS-CreateRdsSnapshot](https://console.aws.amazon.com/systems-manager/documents/AWS-CreateRdsSnapshot/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-CreateRdsSnapshot/description?region=us-east-1")
      + [AWS-CreateSnapshot](https://console.aws.amazon.com/systems-manager/documents/AWS-CreateSnapshot/description?region=us-east-1 "https://console.aws.amazon.com/systems-manager/documents/AWS-CreateSnapshot/description?region=us-east-1")


      ###### Note

      When creating service actions, you can configure the execution role to be the end user's permissions,
       the launch role, or a custom IAM role of your choosing. The selected execution role must have sufficient
       permissions to perform the service action, and have a TrustPolicy that allows it to be assumed
       by Service Catalog, otherwise that service action will fail at execution time.
       We recommend using the AWSManagedServicesServiceCatalogLaunchRole, which has the correct permissions
       and trust policy to be used as a service action.

  **What will I still need to use the AMS RFC system for?**
  At general availability (GA) you will still need to use RFCS to run the following actions:

- Configuring Patch Orchestrator
- Configuring Back up policies
- Requesting instance access
- Creating and assigning security groups that fall outside AMS guidelines.
- Performing workload ingest (WIGS)
- Creating IAM roles
  **Can I use the Service Catalog CLI to access Service Catalog in my AMS managed account?**
  Yes, Service Catalog APIs are available and enabled through the CLI. Actions from the management of Service Catalog
  artifacts through the provisioning and terminating of those artifacts, are available. For more information,
  see [AWS Service Catalog Resources](https://aws.amazon.com/servicecatalog/resources/ "https://aws.amazon.com/servicecatalog/resources/"),
  or download the latest AWS SDK or CLI.

**Who creates, manages, and distributes customers' catalogs of approved products?**
The customer's catalog administrator and/or IT administrator, or assigned resource, is
responsible for the management of your Service Catalog catalogs and approved products.

**Can I use AMS AMIs?**
AMS AMIs vended after March 2020 can be deployed through
AWS Service Catalog.

**How do I migrate to AMS using Service Catalog?**
To migrate your workload to AMS using Service Catalog you begin by following the
[Workload Ingest](../appguide/ams-workload-ingest.md "../appguide/ams-workload-ingest.md") (WIGs) process to
create an AMI in AMS. You use the AMI produced by WIGS to create a product in Service Catalog.
How to do this is detailed in
[AWS Service Catalog - Getting Started](../../../servicecatalog/latest/adminguide/getstarted.md "../../../servicecatalog/latest/adminguide/getstarted.md").
