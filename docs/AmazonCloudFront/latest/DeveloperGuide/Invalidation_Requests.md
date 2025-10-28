# Invalidate files

You can use the CloudFront console to create and run an invalidation, display a list of
the invalidations that you submitted previously, and display detailed information
about an individual invalidation. You can also copy an existing invalidation, edit
the list of file paths, and run the edited invalidation. You can't remove
invalidations from the list.

###### Contents

- [Invalidate files](Invalidation_Requests.md#invalidating-objects-console "Invalidation_Requests.md#invalidating-objects-console")
- [Copy, edit, and rerun an
  existing invalidation](Invalidation_Requests.md#invalidating-objects-copy-console "Invalidation_Requests.md#invalidating-objects-copy-console")
- [Cancel invalidations](Invalidation_Requests.md#canceling-invalidations "Invalidation_Requests.md#canceling-invalidations")
- [List invalidations](Invalidation_Requests.md#listing-invalidations-console "Invalidation_Requests.md#listing-invalidations-console")
- [Display information about an
  invalidation](Invalidation_Requests.md#invalidation-details-console "Invalidation_Requests.md#invalidation-details-console")

## Invalidate files

To invalidate files using the CloudFront console, do the following.

Console

###### To invalidate files

(console)

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the distribution for which you want to invalidate files.
3. Choose the **Invalidations** tab.
4. Choose **Create invalidation**.
5. For the files that you want to invalidate, enter one invalidation path
   per line. For information about specifying invalidation paths, see [What you need to know when invalidating files](invalidation-specifying-objects.md "invalidation-specifying-objects.md").

###### Important

Specify file paths carefully. You can’t cancel an invalidation
request after you start it. 6. Choose **Create invalidation**.

CloudFront API
To learn about invalidating objects and displaying information about
invalidations, see the following topics in the
_Amazon CloudFront API Reference_:

- [CreateInvalidation](../../../cloudfront/latest/APIReference/API_CreateInvalidation.md "../../../cloudfront/latest/APIReference/API_CreateInvalidation.md")
- [ListInvalidations](../../../cloudfront/latest/APIReference/API_ListInvalidations.md "../../../cloudfront/latest/APIReference/API_ListInvalidations.md")
- [GetInvalidation](../../../cloudfront/latest/APIReference/API_GetInvalidation.md "../../../cloudfront/latest/APIReference/API_GetInvalidation.md")

###### Note

If you use the AWS Command Line Interface (AWS CLI) to invalidate files and you specify a path
that includes the `*` wildcard, you must use quotes (`"`)
around the path, such as the following example:

```
aws cloudfront create-invalidation --distribution-id `distribution_ID` --paths "/*"
```

## Copy, edit, and rerun an

existing invalidation

You can copy an invalidation that you created previously, update the list of
invalidation paths, and run the updated invalidation. You can't copy an existing
invalidation, update the invalidation paths, and then save the updated
invalidation without running it.

###### Important

If you copy an invalidation that is still in progress, update the list of
invalidation paths, and then run the updated invalidation, CloudFront won't stop
or delete the invalidation that you copied. If any invalidation paths appear
in the original and in the copy, CloudFront will try to invalidate the files
twice, and both invalidations will count against your maximum number of free
invalidations for the month. If you already reached the maximum number of
free invalidations, you will be charged for both invalidations of each file.
For more information, see [Concurrent invalidation request maximum](InvalidationLimits.md "InvalidationLimits.md").

###### To copy, edit, and

rerun an existing invalidation

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Select the distribution that contains the invalidation that you want
   to copy.
3. Choose the **Invalidations** tab.
4. Choose the invalidation that you want to copy.

If you aren’t sure which invalidation you want to copy, you can choose
an invalidation and choose **View details** to display
detailed information about that invalidation. 5. Choose **Copy to new**. 6. Update the list of invalidation paths if applicable. 7. Choose **Create invalidation**.

## Cancel invalidations

When you submit an invalidation request to CloudFront, CloudFront forwards the request to
all edge locations within a few seconds, and each edge location starts
processing the invalidation immediately. As a result, you can’t cancel an
invalidation after you submit it.

## List invalidations

You can display a list of the last 100 invalidations that you’ve created and
run for a distribution by using the CloudFront console. If you want to get a list of
more than 100 invalidations, use the `ListInvalidations` API
operation. For more information, see [ListInvalidations](../../../cloudfront/latest/APIReference/API_ListInvalidations.md "../../../cloudfront/latest/APIReference/API_ListInvalidations.md") in the
_Amazon CloudFront API Reference_.

###### To list

invalidations

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Select the distribution for which you want to display a list of
   invalidations.
3. Choose the **Invalidations** tab.

###### Note

You can’t remove invalidations from the list.

## Display information about an

invalidation

You can display detailed information about an invalidation, including
distribution ID, invalidation ID, the status of the invalidation, the date and
time that the invalidation was created, and a complete list of the invalidation
paths.

###### To display information

about an invalidation

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Select the distribution that contains the invalidation that you want
   to display detailed information for.
3. Choose the **Invalidations** tab.
4. Choose the applicable invalidation ID or select the invalidation ID
   and then choose **View details**.
