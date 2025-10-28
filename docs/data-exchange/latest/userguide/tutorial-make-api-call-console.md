# Making an AWS Data Exchange API call

You can call a single endpoint in the AWS Data Exchange console.

###### To make an API call from the console

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **My
   subscriptions**, choose **Entitled data**.
3. Choose the product titled \***\*AWS Data Exchange** for APIs
   (Test Product)** and then choose the **AWS Data Exchange for
   APIs\*\* data set.
4. Under the **Revisions** tab, choose the revision.
5. Under **API assets**, choose the API.

You will see the sample **Code structure** and
**OpenApi 3.0 specification** to structure your API
request, which you can use in the AWS Command Line Interface to call the API. 6. Under **Integration notes**, choose
**Copy** to copy the **Code
structure** and then paste it into the AWS CLI. 7. Replace the sample values with the parameter key-value pairs you need
using the information in the specification documentation.

Following is a sample API request for **AWS Data Exchange for APIs (Test
Product)**.

```
aws dataexchange send-api-asset \
  --data-set-id 8d494cba5e4720e5f6072e280daf70a8 \
  --revision-id b655d5be3da04fcbdca21a5a2932d789 \
  --asset-id 8550cfab16b444a794402f2c3f11eae1 \
  --method `POST` \
  --path "`someresource`" \
  --query-string-parameters '`param1=value1,param2=value2`' \
  --request-headers '`header=header_value`' \
  --body "{\"`body_param`\":\"`body_param_value`\"}"

```
