

# Invalidate files
<a name="Invalidation_Requests"></a>

You can use the CloudFront console to create and run an invalidation, display a list of the invalidations that you submitted previously, and display detailed information about an individual invalidation. You can also copy an existing invalidation, edit the list of file paths, and run the edited invalidation. You can't remove invalidations from the list.

**Contents**
+ [Invalidate files](#invalidating-objects-console)
+ [Copy, edit, and rerun an existing invalidation](#invalidating-objects-copy-console)
+ [Cancel invalidations](#canceling-invalidations)
+ [List invalidations](#listing-invalidations-console)
+ [Display information about an invalidation](#invalidation-details-console)

## Invalidate files
<a name="invalidating-objects-console"></a>

To invalidate files using the CloudFront console, do the following.

------
#### [ Console ]<a name="invalidating-objects-console-procedure"></a>

**To invalidate files (console)**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Choose the distribution for which you want to invalidate files.

1. Choose the **Invalidations** tab.

1. Choose **Create invalidation**.

1. For the files that you want to invalidate, enter one invalidation path per line. For information about specifying invalidation paths, see [What you need to know when invalidating paths](invalidation-specifying-objects.md). 
**Important**  
Specify file paths carefully. You can’t cancel an invalidation request after you start it.

1. Choose **Create invalidation**.

------
#### [ CloudFront API ]

To learn about invalidating objects and displaying information about invalidations, see the following topics in the * Amazon CloudFront API Reference*:
+  [CreateInvalidation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateInvalidation.html) 
+  [ListInvalidations](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListInvalidations.html) 
+  [GetInvalidation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetInvalidation.html) 

**Note**  
If you use the AWS Command Line Interface (AWS CLI) to invalidate files and you specify a path that includes the `*` wildcard, you must use quotes (`"`) around the path, such as the following example:   

```
aws cloudfront create-invalidation --distribution-id {{distribution_ID}} --paths "/*"
```

------

## Copy, edit, and rerun an existing invalidation
<a name="invalidating-objects-copy-console"></a>

You can copy an invalidation that you created previously, update the list of invalidation paths, and run the updated invalidation. You can't copy an existing invalidation, update the invalidation paths, and then save the updated invalidation without running it.

**Important**  
If you copy an invalidation that is still in progress, update the list of invalidation paths, and then run the updated invalidation, CloudFront won't stop or delete the invalidation that you copied. If any invalidation paths appear in the original and in the copy, CloudFront will try to invalidate the files twice, and both invalidations will count against your maximum number of free invalidations for the month. If you already reached the maximum number of free invalidations, you will be charged for both invalidations of each file. For more information, see [Quotas on invalidations](cloudfront-limits.md#limits-invalidations).<a name="invalidating-objects-copy-console-procedure"></a>

**To copy, edit, and rerun an existing invalidation**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Select the distribution that contains the invalidation that you want to copy.

1. Choose the **Invalidations** tab.

1. Choose the invalidation that you want to copy.

   If you aren’t sure which invalidation you want to copy, you can choose an invalidation and choose **View details** to display detailed information about that invalidation.

1. Choose **Copy to new**.

1. Update the list of invalidation paths if applicable.

1. Choose **Create invalidation**.

## Cancel invalidations
<a name="canceling-invalidations"></a>

When you submit an invalidation request to CloudFront, CloudFront forwards the request to all edge locations within a few seconds, and each edge location starts processing the invalidation immediately. As a result, you can’t cancel an invalidation after you submit it.

## List invalidations
<a name="listing-invalidations-console"></a>

You can display a list of the last 100 invalidations that you’ve created and run for a distribution by using the CloudFront console. If you want to get a list of more than 100 invalidations, use the `ListInvalidations` API operation. For more information, see [ListInvalidations](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListInvalidations.html) in the * Amazon CloudFront API Reference*.<a name="listing-invalidations-console-procedure"></a>

**To list invalidations**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Select the distribution for which you want to display a list of invalidations.

1. Choose the **Invalidations** tab.

**Note**  
You can’t remove invalidations from the list.

## Display information about an invalidation
<a name="invalidation-details-console"></a>

You can display detailed information about an invalidation, including distribution ID, invalidation ID, the status of the invalidation, the date and time that the invalidation was created, and a complete list of the invalidation paths. <a name="invalidation-details-console-procedure"></a>

**To display information about an invalidation**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Select the distribution that contains the invalidation that you want to display detailed information for.

1. Choose the **Invalidations** tab.

1. Choose the applicable invalidation ID or select the invalidation ID and then choose **View details**.