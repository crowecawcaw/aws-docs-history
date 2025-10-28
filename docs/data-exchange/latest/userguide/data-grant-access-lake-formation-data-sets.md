# Access an AWS Data Exchange data set containing

AWS Lake Formation data sets (Preview)

**Overview for recipients**

An AWS Lake Formation data set is a data set that contains AWS Lake Formation data permission assets.

As a recipient, you can accept a data grant containing AWS Lake Formation data sets. Once you're
entitled to an AWS Data Exchange for AWS Lake Formation data set, you can query, transform, and share access to the
data within your AWS account using AWS Lake Formation, or across your AWS organization using
AWS License Manager.

After you accept a data grant containing an AWS Lake Formation data set, you can use Lake Formation compatible
query engines, like Amazon Athena, to query your data.

###### After acceptance of the data grant is complete, you must do the following:

1. Accept the AWS Resource Access Manager (AWS RAM) share within 12 hours after you accept the data grant. You
   can accept the AWS RAM share from your entitled data sets page for your AWS Lake Formation data permission
   data set on the AWS Data Exchange console. You only need to accept an AWS RAM share once per provider. For
   more information about accepting a resource share invitation from AWS RAM, see [Accepting
   a resource share invitation from AWS RAM](../../../lake-formation/latest/dg/accepting-ram-invite.md "../../../lake-formation/latest/dg/accepting-ram-invite.md").
2. Navigate to AWS Lake Formation and create resource links from the new shared resources.
3. Navigate to Amazon Athena or another AWS Lake Formation compatible query engine to query your
   data.
