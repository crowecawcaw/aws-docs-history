# Creating an allow list

In Amazon Macie, an allow list defines specific text or a text pattern that you want Macie to
ignore when it inspects Amazon Simple Storage Service (Amazon S3) objects for sensitive data. If text matches an entry or
pattern in an allow list, Macie doesn’t report the text in sensitive data findings, statistics,
or other types of results. This is the case even if the text matches the criteria of a [managed data identifier](managed-data-identifiers.md "managed-data-identifiers.md") or a [custom data identifier](custom-data-identifiers.md "custom-data-identifiers.md").

You can create the following types of allow lists in Macie.

**Predefined text**

Use this type of list to specify words, phrases, and other kinds of character
sequences that aren’t sensitive, aren’t likely to change, and don’t necessarily adhere to
a common pattern. Examples are: the names of public representatives for your organization,
specific phone numbers, and specific sample data that your organization uses for testing.
If you use this type of list, Macie ignores text that exactly matches an entry in the
list.

For this type of list, you create a line-delimited plaintext file that lists specific
text to ignore. You then store the file in an S3 bucket and configure settings for Macie
to access the list in the bucket. You can then create and configure sensitive data
discovery jobs to use the list, or add the list to your settings for automated sensitive data discovery. When each
job starts to run or the next automated discovery analysis cycle starts, Macie retrieves the latest
version of the list from Amazon S3. Macie then uses that version of the list when it inspects
S3 objects for sensitive data. If Macie finds text that exactly matches an entry in the
list, Macie doesn't report that occurrence of text as sensitive data.

**Regular expression**

Use this type of list to specify a regular expression (_regex_) that defines a text pattern to ignore. Examples are: public phone
numbers for your organization, email addresses for your organization’s domain, and
patterned sample data that your organization uses for testing. If you use this type of
list, Macie ignores text that completely matches the regex pattern defined by the
list.

For this type of list, you create a regex that defines a common pattern for text that
isn't sensitive but varies or is likely to change. Unlike a list of predefined text, you
create and store the regex and all other list settings in Macie. You can then create and
configure sensitive data discovery jobs to use the list, or add the list to your settings
for automated sensitive data discovery. When those jobs run or Macie performs automated discovery, Macie uses the latest
version of the list's regex to analyze data. If Macie finds text that completely matches
the pattern defined by the list, Macie doesn't report that occurrence of text as sensitive
data.

For detailed requirements, recommendations, and examples of each type, see [Configuration options and requirements for allow
lists](allow-lists-options.md "allow-lists-options.md").

You can create as many as 10 allow lists in each supported AWS Region: up to five allow
lists that specify predefined text, and up to five allow lists that specify regular expressions.
You can create and use allow lists in all the AWS Regions where Macie is currently available
except the Asia Pacific (Osaka) Region.

###### To create an allow list

How you create an allow list depends on the type of list that you want to create: a file
that lists predefined text to ignore, or a regular expression that defines a text pattern to
ignore. The following sections provide instructions for each type. Choose the section for the
type of list that you want to create.

Before you create this type of allow list in Macie, do the following:

1. By using a text editor, create a line-delimited plaintext file that lists specific
   text to ignore—for example, a .txt, .text, or .plain file. For more information,
   see [Syntax requirements](allow-lists-options.md#allow-lists-options-s3list-syntax "allow-lists-options.md#allow-lists-options-s3list-syntax").
2. Upload the file to an S3 general purpose bucket and note the name of the bucket and
   the object. You'll need to enter these names when you configure the settings in
   Macie.
3. Ensure that the settings for the S3 bucket and object allow you and Macie to
   retrieve the list from the bucket. For more information, see [Storage requirements](allow-lists-options.md#allow-lists-options-s3list-storage "allow-lists-options.md#allow-lists-options-s3list-storage").
4. If you encrypted the S3 object, ensure that it's encrypted with a key that you and
   Macie are allowed to use. For more information, see [Encryption/Decryption
   requirements](allow-lists-options.md#allow-lists-options-s3list-encryption "allow-lists-options.md#allow-lists-options-s3list-encryption").
   After you complete these tasks, you're ready to configure the list's settings in Macie.
   You can configure the settings by using the Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to configure the settings for an allow list by using the
Amazon Macie console.

###### To configure allow list settings in Macie

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose
   **Allow lists**.
3. On the **Allow lists** page, choose
   **Create**.
4. Under **Select a list type**, choose **Predefined
   text**.
5. Under **List settings**, use the following options to enter
   additional settings for the allow list:
   - For **Name**, enter a name for the list. The name can
     contain as many as 128 characters.
   - For **Description**, optionally enter a brief description
     of the list. The description can contain as many as 512 characters.
   - For **S3 bucket name**, enter the name of the bucket that
     stores the list.

   In Amazon S3, you can find this value in the **Name** field of
   the bucket's properties. This value is case sensitive. In addition, don't use
   wildcard characters or partial values when you enter the name.
   - For **S3 object name**, enter the name of the S3 object
     that stores the list.

   In Amazon S3, you can find this value in the **Key** field of
   the object's properties. If the name includes a path, be sure to include the
   complete path when you enter the name, for example
   `allowlists/macie/mylist.txt`. This value is case
   sensitive. In addition, don't use wildcard characters or partial values when
   you enter the name.

6. (Optional) Under **Tags**, choose **Add
   tag**, and then enter as many as 50 tags to assign to the allow
   list.

A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md"). 7. When you finish, choose **Create**.

Macie tests the list's settings. Macie also verifies that it can retrieve the list
from Amazon S3 and parse the list's content. If an error occurs, Macie displays a message
that describes the error. For detailed information that can help you troubleshoot the
error, see [Options and requirements for lists of
predefined text](allow-lists-options.md#allow-lists-options-s3list "allow-lists-options.md#allow-lists-options-s3list"). After you address any errors,
you can save the list's settings.

API
To configure allow list settings programmatically, use the [CreateAllowList](../APIReference/allow-lists.md "../APIReference/allow-lists.md") operation of the Amazon Macie API and specify the appropriate
values for the required parameters.

For the `criteria` parameter, use an `s3WordsList` object to
specify the name of the S3 bucket (`bucketName`) and the name of the S3
object (`objectKey`) that stores the list. To determine the bucket name,
refer to the `Name` field in Amazon S3. To determine the object name, refer to
the `Key` field in Amazon S3. Note that these values are case sensitive. In
addition, don't use wildcard characters or partial values when you specify these
names.

To configure the settings by using the AWS CLI, run the [create-allow-list](../../../cli/latest/reference/macie2/create-allow-list.md "../../../cli/latest/reference/macie2/create-allow-list.md")
command and specify the appropriate values for the required parameters. The following
examples show how to configure the settings for an allow list that's stored in an S3
bucket named `amzn-s3-demo-bucket`. The name of the S3 object
that stores the list is `allowlists/macie/mylist.txt`.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 create-allow-list \
--criteria '{"s3WordsList":{"bucketName":"`amzn-s3-demo-bucket`","objectKey":"`allowlists/macie/mylist.txt`"}}' \
--name `my_allow_list` \
--description "`Lists public phone numbers and names for Example Corp.``"
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 create-allow-list ^
--criteria={\"s3WordsList\":{\"bucketName\":\"`amzn-s3-demo-bucket`\",\"objectKey\":\"`allowlists/macie/mylist.txt`\"}} ^
--name `my_allow_list` ^
--description "`Lists public phone numbers and names for Example Corp.`"`
```

When you submit your request, Macie tests the list's settings. Macie also verifies
that it can retrieve the list from Amazon S3 and parse the list's content. If an error
occurs, your request fails and Macie returns a message that describes the error. For
detailed information that can help you troubleshoot the error, see [Options and requirements for lists of
predefined text](allow-lists-options.md#allow-lists-options-s3list "allow-lists-options.md#allow-lists-options-s3list").

If Macie can retrieve and parse the list, your request succeeds and you receive
output similar to the following.

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:allow-list/nkr81bmtu2542yyexample",
 "id": "nkr81bmtu2542yyexample"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the allow list that
was created, and `id` is the unique identifier for the list.

After you save the list's settings, you can [create
and configure sensitive data discovery jobs](discovery-jobs-create.md "discovery-jobs-create.md") to use the list, or [add the list to your settings for
automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"). Each time those jobs start to run or an automated discovery analysis cycle starts,
Macie retrieves the latest version of the list from Amazon S3. Macie then uses that version of
the list when it analyzes data.

When you create an allow list that specifies a regular expression (_regex_), you define the regex and all other list settings directly
in Macie. For the regex, Macie supports a subset of the pattern syntax provided by the
[Perl Compatible Regular Expressions (PCRE)
library](https://www.pcre.org/ "https://www.pcre.org/"). For more information, see [Syntax support and recommendations](allow-lists-options.md#allow-lists-options-regex-syntax "allow-lists-options.md#allow-lists-options-regex-syntax").

You can create this type of list by using the Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to create an allow list by using the Amazon Macie console.

###### To create an allow list by using the console

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose
   **Allow lists**.
3. On the **Allow lists** page, choose
   **Create**.
4. Under **Select a list type**, choose **Regular
   expression**.
5. Under **List settings**, use the following options to enter
   additional settings for the allow list:
   - For **Name**, enter a name for the list. The name can
     contain as many as 128 characters.
   - For **Description**, optionally enter a brief description
     of the list. The description can contain as many as 512 characters.
   - For **Regular expression**, enter the regex that defines
     the text pattern to ignore. The regex can contain as many as 512
     characters.

6. (Optional) For **Evaluate**, enter up to 1,000 characters in
   the **Sample data** box, and then choose
   **Test** to test the regex. Macie evaluates the sample data and
   reports the number of occurrences of text that match the regex. You can repeat
   this step as many times as you like to refine and optimize the regex.

###### Note

We recommend that you test and refine the regex with multiple sets of sample
data. If you create a regex that’s too general, Macie might ignore occurrences
of text that you consider sensitive. If a regex is too specific, Macie might not
ignore occurrences of text that you don’t consider sensitive. 7. (Optional) Under **Tags**, choose **Add
tag**, and then enter as many as 50 tags to assign to the allow
list.

A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md"). 8. When you finish, choose **Create**.

Macie tests the list's settings. Macie also tests the regex to verify that it can
compile the expression. If an error occurs, Macie displays a message that describes
the error. For detailed information that can help you troubleshoot the error, see
[Options and requirements for regular
expressions](allow-lists-options.md#allow-lists-options-regex "allow-lists-options.md#allow-lists-options-regex"). After you address any errors, you can save the allow list.

API
Before you create this type of allow list in Macie, we recommend that you test and
refine the regex with multiple sets of sample data. If you create a regex that’s too
general, Macie might ignore occurrences of text that you consider sensitive. If a
regex is too specific, Macie might not ignore occurrences of text that you don’t
consider sensitive.

To test an expression with Macie, you can use the [TestCustomDataIdentifier](../APIReference/custom-data-identifiers-test.md "../APIReference/custom-data-identifiers-test.md") operation of the Amazon Macie API or, for the AWS CLI,
run the [test-custom-data-identifier](../../../cli/latest/reference/macie2/test-custom-data-identifier.md "../../../cli/latest/reference/macie2/test-custom-data-identifier.md") command. Macie uses the same underlying code to
compile expressions for allow lists and custom data identifiers. If you test an
expression in this way, be sure to specify values only for the `regex` and
`sampleText` parameters. Otherwise, you'll receive inaccurate
results.

When you're ready to create this type of allow list, use the [CreateAllowList](../APIReference/allow-lists.md "../APIReference/allow-lists.md") operation of the Amazon Macie API and specify the appropriate
values for the required parameters. For the `criteria` parameter, use the
`regex` field to specify the regular expression that defines the text
pattern to ignore. The expression can contain as many as 512 characters.

To create this type of list by using the AWS CLI, run the [create-allow-list](../../../cli/latest/reference/macie2/create-allow-list.md "../../../cli/latest/reference/macie2/create-allow-list.md") command and specify the appropriate values for the
required parameters. The following examples create an allow list named
`my_allow_list`. The regex is designed to ignore all email
addresses that a custom data identifier might otherwise detect for the
`example.com` domain.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 create-allow-list \
--criteria '{"regex":"`[a-z]@example.com`"}' \
--name `my_allow_list` \
--description "`Ignores all email addresses for Example Corp.``"
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 create-allow-list ^
--criteria={\"regex\":\"`[a-z]@example.com`\"} ^
--name `my_allow_list` ^
--description "`Ignores all email addresses for Example Corp.`"`
```

When you submit your request, Macie tests the list's settings. Macie also tests
the regex to verify that it can compile the expression. If an error occurs, the
request fails and Macie returns a message that describes the error. For detailed
information that can help you troubleshoot the error, see [Options and requirements for regular
expressions](allow-lists-options.md#allow-lists-options-regex "allow-lists-options.md#allow-lists-options-regex").

If Macie can compile the expression, the request succeeds and you receive output
similar to the following:

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:allow-list/km2d4y22hp6rv05example",
 "id": "km2d4y22hp6rv05example"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the allow list that
was created, and `id` is the unique identifier for the list.

After you save the list, you can [create and
configure sensitive data discovery jobs](discovery-jobs-create.md "discovery-jobs-create.md") to use it, or [add it to your settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md").
When those jobs run or Macie performs automated discovery, Macie uses the latest version of the list's
regex to analyze data.
