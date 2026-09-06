

# Troubleshooting customer segments in Connect Customer
<a name="customer-segments-troubleshooting"></a>

## The Customer segments option doesn't appear in the left navigation panel
<a name="customer-segments-does-not-exist-in-the-left-navigation-panel"></a>

 If a **Customer segments** option does not exist in Connect Customer admin website left navigation panel, check if the user's security profiles has the **Customer segment - View** permission. For more information, see [Assign security profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md). After the permission is updated, refresh the Connect Customer admin website page to reflect the change.

## Export CSV button not available, or export job timed out
<a name="export-csv-button-not-available-or-export-job-timed-out"></a>

 Exporting a segment that contains more than 350,000 profiles is not supported in the Connect Customer admin website. Alternatively, we recommend exporting this type of segment to an Amazon S3 bucket using the `CreateSegmentSnapshot` API through the command line reference (CLI) or SDK. 

## Error: You reached the limit of 60 unique attributes
<a name="error-you-reached-the-limit-of-20-unique-attributes"></a>

 This error occurs when the number of unique attributes in the segment definition exceeds the quota. The number of unique attributes are counted including the starting audiences recursively. 

**Solutions**
+  Reduce the number of unique attributes by removing audience filters in the segment definition, or removing starting audiences that contains audience filters. 
+  [Request a quota increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) for the service quotas - Maximum number of unique attributes in segment  

 For more about default service quota, see [Connect Customer Customer Profiles service quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html#limits_customer_profiles). 

## Error: You reached the limit of 10 unique calculated attributes
<a name="error-you-reached-the-limit-of-1-unique-calculated-attribute"></a>

 This error occurs when the number of unique calculated attributes in the segment definition exceeds the quota. The number of unique calculated attributes are counted including the starting audiences recursively. 

**Solutions**
+  Reduce the number of unique calculated attributes by removing audience filters on calculated attributes in the segment definition, or removing starting audiences that contains audience filters on calculated attributes. 
+  [Request a quota increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) for the service quotas - Maximum number of unique calculated attributes in segment. 

 For more about default service quota, see [Connect Customer Customer Profiles service quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html#limits_customer_profiles). 

## Error: You reached the limit of 5 depth of starting audiences
<a name="error-you-reached-the-limit-of-5-depth-of-starting-audiences"></a>

This error occurs when the depth of starting audiences exceeds the quota. The depth is counted recursively for all of the starting audiences in your audience group. For example, if you select a segment "Eligible rental upgrade" as a starting audience, and the segment "Eligible rental upgrade" has another segment as a starting audience, the depth will be 2.

**Solution**
+ Remove one or more starting audiences in your audience group that contains deeply nested starting audiences.

For more about default service quotas, see [Connect Customer Customer Profiles service quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html#limits_customer_profiles).