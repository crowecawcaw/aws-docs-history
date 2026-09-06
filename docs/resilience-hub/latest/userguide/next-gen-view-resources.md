

# View discovered resources
<a name="next-gen-view-resources"></a>

**To view resources (console)**

1. Open the Next generation Resilience Hub console and navigate to your service.

1. Choose **Service topology**.

1. The resources graph and resources list show all discovered resources with their type, Region, and associated service function.

1. Use the filters to narrow by Region or service function.

**To list resources (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 list-resources \
    --service-arn "{{service-arn}}"
  ```

  To filter by Region:

  ```
  aws resiliencehubv2 list-resources \
    --service-arn "{{service-arn}}" \
    --aws-region "{{region}}"
  ```