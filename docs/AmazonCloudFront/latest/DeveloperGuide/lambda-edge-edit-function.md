# Edit a Lambda function

After you create a Lambda@Edge function, you can use the Lambda console to edit
it.

###### Notes

- The original version is labeled $LATEST.
- You can edit only the $LATEST version.
- Each time you edit the $LATEST version, you must publish a new
  numbered version.
- You can't create triggers for $LATEST.
- When you publish a new version of a function, Lambda doesn't
  automatically copy triggers from the previous version to the new
  version. You must reproduce the triggers for the new version.
- When you add a trigger for a CloudFront event to a function, if there's
  already a trigger for the same distribution, cache behavior, and event
  for an earlier version of the same function, Lambda deletes the trigger
  from the earlier version.
- After you make updates to a CloudFront distribution, like adding triggers,
  you must wait for the changes to propagate to edge locations before the
  functions you've specified in the triggers will work.

###### To edit a Lambda

function

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the Region list at the top of the page, choose
   **US East (N. Virginia)**.
3. In the list of functions, choose the name of the function.

By default, the console displays the $LATEST version. You can view earlier
versions (choose **Qualifiers**), but you can only edit
$LATEST. 4. On the **Code** tab, for **Code entry
type**, choose to edit the code in the browser, upload a .zip
file, or upload a file from Amazon S3. 5. Choose either **Save** or **Save and
test**. 6. Choose **Actions**, and choose **Publish new
version**. 7. In the **Publish new version from $LATEST** dialog box,
enter a description of the new version. This description appears in the list
of versions, along with an automatically generated version number. 8. Choose **Publish**.

The new version automatically becomes the latest version. The version
number appears on the **Version** in the upper-left corner
of the page.

###### Note

If you haven't added triggers for your function yet, see [Add triggers for a Lambda@Edge
function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md"). 9. Choose the **Triggers** tab. 10. Choose **Add trigger**. 11. In the **Add trigger** dialog box, choose the dotted box,
and then choose **CloudFront**.

###### Note

If you've already created one or more triggers for a function, CloudFront is
the default service. 12. Specify the following values to indicate when you want the Lambda function
to execute.

    1. **Distribution ID** – Choose the ID of the
     distribution that you want to add the trigger to.
    2. **Cache behavior** – Choose the cache
     behavior that specifies the objects that you want to execute the
     function on.
    3. **CloudFront event** – Choose the CloudFront event
     that causes the function to execute.
    4. **Enable trigger and replicate** – Select
     this check box so Lambda replicates the function to AWS Regions
     globally.

13. Choose **Submit**.
14. To add more triggers for this function, repeat steps 10 through 13.
    For more information about testing and debugging the function in the Lambda
    console, see [Invoke
    a Lambda function using the console](../../../lambda/latest/dg/getting-started.md#get-started-invoke-manually "../../../lambda/latest/dg/getting-started.md#get-started-invoke-manually") in the
    _AWS Lambda Developer Guide_.

When you're ready to have the function execute for CloudFront events, publish another
version and edit the function to add triggers. For more information, see [Add triggers for a Lambda@Edge
function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md").
