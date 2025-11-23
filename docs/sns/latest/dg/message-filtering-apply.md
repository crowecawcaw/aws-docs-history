# Applying a subscription filter policy in

Amazon SNS

Message filtering in Amazon SNS allows you to selectively deliver messages to subscribers based
on filter policies. These policies define conditions that messages must meet to be delivered
to a subscription. While raw message delivery is an option that can affect message
processing, it is not required for subscription filters to work.

You can apply a filter policy to an Amazon SNS subscription using the Amazon SNS console. Or, to
apply policies programmatically, you can use the Amazon SNS API, the AWS Command Line Interface (AWS CLI), or any
AWS SDK that supports Amazon SNS. You can also use AWS CloudFormation.

**Enabling Raw Message Delivery**

Raw message delivery ensures that message payloads are delivered as-is to subscribers
without any additional encoding or transformation. This can be useful when subscribers
require the original message format for processing. However, raw message delivery is not
directly related to the functionality of subscription filters.

**Applying Subscription Filters**

To apply message filters to a subscription, you define a filter policy using JSON syntax.
This policy specifies the conditions that a message must meet to be delivered to the
subscription. Filters can be based on message attributes, such as message attributes,
message structure, or even message content.

**Relationship between Raw Message Delivery and Subscription
Filters**

While enabling raw message delivery can affect how messages are delivered and processed by
subscribers, it is not a prerequisite for using subscription filters. However, in scenarios
where subscribers require the original message format without any modifications, enabling
raw message delivery might be beneficial alongside subscription filters.

**Considerations for Effective Filtering**

When implementing message filtering, consider the specific requirements of your
application and subscribers. Define filter policies that accurately match the criteria for
message delivery to ensure efficient and targeted message distribution.

###### Important

AWS services such as IAM and Amazon SNS use a distributed computing model called eventual consistency.
Additions or changes to a subscription filter policy require up to 15 minutes to fully take effect.

## AWS Management Console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Subscriptions**.
3. Select a subscription and then choose **Edit**.
4. On the **Edit** page, expand the **Subscription
   filter policy** section.
5. Choose between **attribute-based filtering** or
   **payload-based filtering**.
6. In the **JSON editor** field, provide the **JSON body** of your filter policy.
7. Choose **Save changes**.

Amazon SNS applies your filter policy to the subscription.

## AWS CLI

To apply a filter policy with the AWS Command Line Interface (AWS CLI), use the [`set-subscription-attributes`](../../../cli/latest/reference/sns/set-subscription-attributes.md "../../../cli/latest/reference/sns/set-subscription-attributes.md") command, as shown in the
following example. For the `--attribute-name` option, specify
`FilterPolicy`. For `--attribute-value`, specify your
**JSON policy**.

```
`$` `aws sns set-subscription-attributes --subscription-arn `arn:aws:sns: ...` --attribute-name FilterPolicy --attribute-value `'{"store":["example_corp"],"event":["order_placed"]}'``
```

To provide valid JSON for your policy, enclose the attribute names and values in
double quotes. You must also enclose the entire policy argument in quotes. To avoid
escaping quotes, you can use single quotes to enclose the policy and double quotes to
enclose the JSON names and values, as shown in the above example.

If you want to switch from attribute-based (default) to payload-based message
filtering, you can use the [set-subscription-attributes](../../../cli/latest/reference/sns/set-subscription-attributes.md "../../../cli/latest/reference/sns/set-subscription-attributes.md") command as well. For the
`--attribute-name` option, specify `FilterPolicyScope`. For
`--attribute-value`, specify `MessageBody`.

```
`$` `aws sns set-subscription-attributes --subscription-arn arn:aws:sns: ... --attribute-name FilterPolicyScope --attribute-value MessageBody`
```

To verify that your filter policy was applied, use the
`get-subscription-attributes` command. The attributes in the terminal
output should show your filter policy for the `FilterPolicy` key, as shown in
the following example:

```
`$` `aws sns get-subscription-attributes --subscription-arn `arn:aws:sns: ...``
`{
 "Attributes": {
 "Endpoint": "*endpoint . . .*",
 "Protocol": "https",
 "RawMessageDelivery": "false",
 "EffectiveDeliveryPolicy": "*delivery policy . . .*",
 "ConfirmationWasAuthenticated": "true",
 **"FilterPolicy": "{\"store\": [\"example\_corp\"], \"event\": [\"order\_placed\"]}",**
 **"FilterPolicyScope": "MessageAttributes",**
 "Owner": "111122223333",
 "SubscriptionArn": "*arn:aws:sns: . . .*",
 "TopicArn": "*arn:aws:sns: . . .*"
 }
}`
```

## AWS SDKs

The following code examples show how to use `SetSubscriptionAttributes`.

###### Important

If you are using the SDK for Java 2.x example, the class
`SNSMessageFilterPolicy` is not available out of the box. For
instructions on how to install this class, see the [example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/sns/src/main/java/com/example/sns/SNSMessageFilterPolicy.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/sns/src/main/java/com/example/sns/SNSMessageFilterPolicy.java") from the GitHub website.

CLI

**AWS CLI**

**To set subscription attributes**

The following `set-subscription-attributes` example sets the `RawMessageDelivery` attribute to an SQS subscription.

```
`aws sns set-subscription-attributes \
 --subscription-arn `arn:aws:sns:us-east-1:123456789012:mytopic:f248de18-2cf6-578c-8592-b6f1eaa877dc` \
 --attribute-name `RawMessageDelivery` \
 --attribute-value `true``

```

This command produces no output.

The following `set-subscription-attributes` example sets a `FilterPolicy` attribute to an SQS subscription.

```
`aws sns set-subscription-attributes \
 --subscription-arn `arn:aws:sns:us-east-1:123456789012:mytopic:f248de18-2cf6-578c-8592-b6f1eaa877dc` \
 --attribute-name `FilterPolicy` \
 --attribute-value "{ \"anyMandatoryKey\": [\"any\", \"of\", \"these\"] }"`

```

This command produces no output.

The following `set-subscription-attributes` example removes the `FilterPolicy` attribute from an SQS subscription.

```
`aws sns set-subscription-attributes \
 --subscription-arn `arn:aws:sns:us-east-1:123456789012:mytopic:f248de18-2cf6-578c-8592-b6f1eaa877dc` \
 --attribute-name `FilterPolicy` \
 --attribute-value `"{}"``

```

This command produces no output.

- For API details, see
  [SetSubscriptionAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-subscription-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-subscription-attributes.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.SnsException;
import java.util.ArrayList;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class UseMessageFilterPolicy {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <subscriptionArn>

                Where:
                   subscriptionArn - The ARN of a subscription.

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String subscriptionArn = args[0];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        usePolicy(snsClient, subscriptionArn);
        snsClient.close();
    }

    public static void usePolicy(SnsClient snsClient, String subscriptionArn) {
        try {
            SNSMessageFilterPolicy fp = new SNSMessageFilterPolicy();
            // Add a filter policy attribute with a single value
            fp.addAttribute("store", "example_corp");
            fp.addAttribute("event", "order_placed");

            // Add a prefix attribute
            fp.addAttributePrefix("customer_interests", "bas");

            // Add an anything-but attribute
            fp.addAttributeAnythingBut("customer_interests", "baseball");

            // Add a filter policy attribute with a list of values
            ArrayList<String> attributeValues = new ArrayList<>();
            attributeValues.add("rugby");
            attributeValues.add("soccer");
            attributeValues.add("hockey");
            fp.addAttribute("customer_interests", attributeValues);

            // Add a numeric attribute
            fp.addAttribute("price_usd", "=", 0);

            // Add a numeric attribute with a range
            fp.addAttributeRange("price_usd", ">", 0, "<=", 100);

            // Apply the filter policy attributes to an Amazon SNS subscription
            fp.apply(snsClient, subscriptionArn);

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [SetSubscriptionAttributes](../../../goto/SdkForJavaV2/sns-2010-03-31/SetSubscriptionAttributes.md "../../../goto/SdkForJavaV2/sns-2010-03-31/SetSubscriptionAttributes.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples").

```
class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource


    @staticmethod
    def add_subscription_filter(subscription, attributes):
        """
        Adds a filter policy to a subscription. A filter policy is a key and a
        list of values that are allowed. When a message is published, it must have an
        attribute that passes the filter or it will not be sent to the subscription.

        :param subscription: The subscription the filter policy is attached to.
        :param attributes: A dictionary of key-value pairs that define the filter.
        """
        try:
            att_policy = {key: [value] for key, value in attributes.items()}
            subscription.set_attributes(
                AttributeName="FilterPolicy", AttributeValue=json.dumps(att_policy)
            )
            logger.info("Added filter to subscription %s.", subscription.arn)
        except ClientError:
            logger.exception(
                "Couldn't add filter to subscription %s.", subscription.arn
            )
            raise



```

- For API details, see
  [SetSubscriptionAttributes](../../../goto/boto3/sns-2010-03-31/SetSubscriptionAttributes.md "../../../goto/boto3/sns-2010-03-31/SetSubscriptionAttributes.md")
  in _AWS SDK for Python (Boto3) API Reference_.

## Amazon SNS API

To apply a filter policy with the Amazon SNS API, make a request to the [`SetSubscriptionAttributes`](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md") action. Set the
`AttributeName` parameter to `FilterPolicy`, and set the
`AttributeValue` parameter to your filter policy JSON.

If you want to switch from attribute-based (default) to payload-based message
filtering, you can use the [`SetSubscriptionAttributes`](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md") action as well. Set the
`AttributeName` parameter to `FilterPolicyScope`, and set the
`AttributeValue` parameter to `MessageBody`.

## AWS CloudFormation

To apply a filter policy using CloudFormation, use a JSON or YAML template to create a CloudFormation
stack. For more information, see the [`FilterPolicy` property](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md#cfn-sns-subscription-filterpolicy "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md#cfn-sns-subscription-filterpolicy") of the
`AWS::SNS::Subscription` resource in the
_AWS CloudFormation User Guide_ and the [example CloudFormation template](https://github.com/aws-samples/aws-sns-samples/blob/master/templates/SNS-Subscription-Attributes-Tutorial-CloudFormation.template "https://github.com/aws-samples/aws-sns-samples/blob/master/templates/SNS-Subscription-Attributes-Tutorial-CloudFormation.template").

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
2. Choose **Create Stack**.
3. On the **Select Template** page, choose **Upload a
   template to Amazon S3**, choose the file, and choose
   **Next**.
4. On the **Specify Details** page, do the following:
   1. For **Stack Name**, type
      `MyFilterPolicyStack`.
   2. For **myHttpEndpoint**, type the HTTP endpoint to be
      subscribed to your topic.

   ###### Tip

   If you don't have an HTTP endpoint, create one.

5. On the **Options** page, choose
   **Next**.
6. On the **Review** page, choose
   **Create.**
