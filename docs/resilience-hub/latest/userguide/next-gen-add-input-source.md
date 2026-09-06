

# Add input sources to a service
<a name="next-gen-add-input-source"></a>

**To add an input source (console)**

1. Open the Next generation Resilience Hub console and navigate to your service.

1. Choose the **Configuration** tab.

1. Choose **Edit** in the **Service resource discovery** section.

1. Select the input source type and provide the required configuration:
   + **AWS CloudFormation stack** – Select one or more AWS CloudFormation stacks. The selector will show stacks relevant to the Regions you have selected for this service.
   + **Terraform state file** – Enter the Amazon S3 URL of the state file.
   + **Resource tags** – Enter the tag key and values to match.
   + **Amazon EKS cluster** – Enter the cluster ARN and select the namespaces to include.

1. Choose **Add**.

**To add an input source (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 create-input-source \
    --service-arn "{{service-arn}}" \
    --resource-configuration '{"cfnStackArn": "{{stack-arn}}"}'
  ```