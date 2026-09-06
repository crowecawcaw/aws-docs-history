

# Create a service
<a name="next-gen-create-service"></a>

**To create a service (console)**

1. Open the Next generation Resilience Hub console.

1. In the navigation pane, choose **Services**.

1. Choose **Create service**.

1. Provide the following details:
   + **Service name** – Enter a descriptive name for your service (for example, `checkout-service` or `payment-service`).
   + **Description** – (Optional) Enter a description of the service.
   + **Resilience policy** – Select a resilience policy to associate with this service. The policy defines your availability SLO and RTO/RPO targets.
   + **Permission model** – Specify the IAM role that the next generation of Resilience Hub uses for resource discovery. Choose one of the following options:
     + **Create a new service role** (recommended) – The console automatically creates an IAM role with the correct trust policy and attaches the required managed policy.
     + **Use an existing service role** – Choose an existing IAM role from the list. Make sure that the role has the required trust policy and permissions. For more information, see [Required IAM permissions and roles](next-gen-iam-permissions.md).
     + **Cross-account roles** – (Optional) If your resources are in other accounts, add the cross-account role ARNs.
   + **Regions** – Select the AWS Regions where your service operates. You can select up to 5 Regions.
   + **Resource discovery** – Provide input sources to enable discovery of resources used by your service. See [Add input sources to a service](next-gen-add-input-source.md) for instructions on adding input sources.
   + **Dependency discovery** – (Optional) Enable the dependency discovery feature for this service. See [Dependency discovery](next-gen-dependency-discovery.md) for more information on dependency discovery.
   + **Data encryption** – (Optional) Choose a customer managed AWS KMS key to encrypt service data. For more information, see [Data encryption](next-gen-data-encryption.md).
   + **Tags** – (Optional) Add tags to your service.

1. Choose **Create service**.

**To create a service (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 create-service \
    --name "{{service-name}}" \
    --regions '["{{region}}"]' \
    --permission-model '{"invokerRoleName": "{{role-name}}"}' \
    --associated-systems '[{"systemArn": "{{system-arn}}"}]'
  ```

The following table describes the available input source types that you can add after creating the service:


| Input source | Use when | 
| --- | --- | 
| AWS CloudFormation stacks | Your infrastructure is defined in AWS CloudFormation. | 
| Terraform state files | Your infrastructure is managed by Terraform (state file in Amazon S3). | 
| Resource tags | The service discovers resources by matching tags. A single tag-based input source with multiple tags discovers only resources that match all specified tags. Multiple tag-based input sources discover resources that match any of them. | 
| Amazon Elastic Kubernetes Service clusters | Your service runs on Amazon EKS. | 