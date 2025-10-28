# Checking the status of an allow list

If you create an allow list, it's important to check its status periodically. Otherwise,
errors might cause Amazon Macie to produce unexpected analysis results for your Amazon Simple Storage Service (Amazon S3)
data. For example, Macie might create sensitive data findings for text that you specified in an
allow list.

If you configure a sensitive data discovery job to use an allow list and Macie can't access
or use the list when the job starts to run, the job continues to run. However, Macie doesn't use
the list when it analyzes S3 objects. Similarly, if an analysis cycle starts for automated sensitive data discovery and
Macie can't access or use a specified allow list, the analysis continues but Macie doesn't use
the list.

Errors are unlikely to occur for an allow list that specifies a regular expression
(_regex_). This is partly because Macie automatically tests the
regex when you create or update the list's settings. In addition, you store the regex and all
other list settings in Macie.

However, errors can occur for an allow list that specifies predefined text, partly because
you store the list in Amazon S3 instead of Macie. Common causes of errors are:

- The S3 bucket or object is deleted.
- The S3 bucket or object is renamed and the list's settings in Macie don't specify the new
  name.
- The S3 bucket's permissions settings are changed and Macie loses access to the bucket and
  the object.
- The encryption settings for the S3 bucket are changed and Macie can't decrypt the object
  that stores the list.
- The policy for the encryption key is changed and Macie loses access to the key. Macie
  can't decrypt the S3 object that stores the list.

###### Important

Because these errors affect your analyses' results, we recommend that you check the status
of all of your allow lists periodically. We recommend that you also do this if you change the
permissions or encryption settings for an S3 bucket that stores an allow list, or you change the
policy for an AWS Key Management Service (AWS KMS) key that's used to encrypt a list.

For detailed information that can help you troubleshoot errors that occur, see [Options and requirements for lists of predefined
text](allow-lists-options.md#allow-lists-options-s3list "allow-lists-options.md#allow-lists-options-s3list").

###### To check the status of an allow list

You can check the status of an allow list by using the Amazon Macie console or the Amazon Macie
API. On the console, you can use a single page to check the status of all of your allow lists at
the same time. If you use the Amazon Macie API, you can check the status of individual allow lists,
one at a time.

Console
Follow these steps to check the status of your allow lists by using the Amazon Macie
console.

###### To check the status of your allow lists

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose **Allow
   lists**.
3. On the **Allow lists** page, choose refresh (
   ![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
   ). Macie
   tests the settings for all of your allow lists and updates the **Status**
   field to indicate the current status of each list.

If a list specifies a regular expression, its status is typically
**OK**. This means that Macie can compile the expression. If a list
specifies predefined text, its status can be any of the following values.

**OK**

Macie can retrieve and parse the contents of the list.

**Access denied**

Macie isn't allowed to access the S3 object that stores the list. Amazon S3 denied the
request to retrieve the object. A list can also have this status if the object is
encrypted with a customer managed AWS KMS key that Macie isn't allowed to use.

To address this error, review the bucket policy and other permissions settings for
the bucket and the object. Ensure that Macie is allowed to access and retrieve the
object. If the object is encrypted with a customer managed AWS KMS key, also review the key
policy and ensure that Macie is allowed to use the key.

**Error**

A transient or internal error occurred when Macie attempted to retrieve or parse the
contents of the list. An allow list can also have this status if it's encrypted with an
encryption key that Amazon S3 and Macie can't access or use.

To address this error, wait a few minutes and then choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
)
again. If the status continues to be **Error**, check the encryption
settings for the S3 object. Ensure that the object is encrypted with a key that Amazon S3 and
Macie can access and use.

**Object is empty**

Macie can retrieve the list from Amazon S3 but the list doesn't contain any
content.

To address this error, download the object from Amazon S3 and ensure that it contains the
correct entries. If the entries are correct, review the list's settings in Macie. Ensure
that the specified bucket and object names are correct.

**Object not found**

The list doesn't exist in Amazon S3.

To address this error, review the list's settings in Macie. Ensure that the
specified bucket and object names are correct.

**Quota exceeded**

Macie can access the list in Amazon S3. However, the number of entries in the list or the
storage size of the list exceeds the quota for an allow list.

To address this error, break the list into multiple files. Ensure that each file
contains fewer than 100,000 entries. Also ensure that the size of each file is less than
35 MB. Then, upload each file to Amazon S3. When you finish, configure allow list settings in
Macie for each file. You can have as many as five lists of predefined text in each
supported AWS Region.

**Throttled**

Amazon S3 throttled the request to retrieve the list.

To address this error, wait a few minutes and then choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
)
again.

**User access denied**

Amazon S3 denied the request to retrieve the object. If the specified object exists,
you're not allowed to access it or it's encrypted with an AWS KMS key that you're not
allowed to use.

To address this error, work with your AWS administrator to ensure that the list's
settings specify the correct bucket and object names, and you have read access to the
bucket and the object. If the object is encrypted, also ensure that it's encrypted with a
key that you're allowed to use. 4. To review the settings and status of a specific list, choose the list's name.

API
To check the status of an allow list programmatically, use the [GetAllowList](../APIReference/allow-lists-id.md "../APIReference/allow-lists-id.md")
operation of the Amazon Macie API. Or, if you're using the AWS CLI, run the [get-allow-list](../../../cli/latest/reference/macie2/get-allow-list.md "../../../cli/latest/reference/macie2/get-allow-list.md") command.

For the `id` parameter, specify the unique identifier for the allow list whose
status you want to check. To get this identifier, you can use the [ListAllowLists](../APIReference/allow-lists.md "../APIReference/allow-lists.md") operation. The
**ListAllowLists** operation retrieves information about all the allow lists
for your account. If you're using the AWS CLI, you can run the [list-allow-lists](../../../cli/latest/reference/macie2/list-allow-lists.md "../../../cli/latest/reference/macie2/list-allow-lists.md") command to
retrieve this information.

When you submit a **GetAllowList** request, Macie tests all the settings
for the allow list. If the settings specify a regular expression (`regex`), Macie
verifies that it can compile the expression. If the settings specify a list of predefined text
(`s3WordsList`), Macie verifies that it can retrieve and parse the list.

Macie then returns a `GetAllowListResponse` object that provides the details
of the allow list. In the `GetAllowListResponse` object, the `status`
object indicates the current status of the list: a status code (`code`) and,
depending on the status code, a brief description of the list's status
(`description`).

If the allow list specifies a regex, the status code is typically `OK` and
there isn't an associated description. This means that Macie compiled the expression
successfully.

If the allow list specifies predefined text, the status code varies depending on the test
results:

- If Macie retrieved and parsed the list successfully, the status code is `OK`
  and there isn't an associated description.
- If an error prevented Macie from retrieving or parsing the list, the status code and
  description indicate the nature of the error that occurred.

For a list of possible status codes and a description of each one, see [AllowListStatus](../APIReference/allow-lists-id.md#allow-lists-id-model-allowliststatus "../APIReference/allow-lists-id.md#allow-lists-id-model-allowliststatus") in the _Amazon Macie API
Reference_.
