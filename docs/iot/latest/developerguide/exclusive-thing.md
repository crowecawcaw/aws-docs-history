

# Associating an AWS IoT thing to an MQTT client connection
<a name="exclusive-thing"></a>

An exclusive thing association is when you attach an X.509 certificate to a single AWS IoT thing. In this case, the certificate cannot be used with other things. By ensuring that a certificate is used only by a single IoT thing, it helps prevent security vulnerabilities.

In AWS IoT, the client ID is a unique identifier for a thing or a device when it connects to the AWS IoT Core MQTT broker. If you use a non-exclusive association, multiple things can be attached to the same certificate. When non-exclusive thing association is in place, to maintain a clear association and to avoid potential conflicts, you must match your client ID with the thing name.

**Topics**
+ [Use cases](#exclusive-thing-benefits)
+ [How to associate a thing to a connection](#exclusive-thing-how-to)

## Use cases
<a name="exclusive-thing-benefits"></a>

Associating a thing to a connection provides the following capabilities. 

**Note**  
Note that if your IoT thing and client connection has a non-exclusive association, you can use all the following capabilities except the lifecycle events capability. To include your thing name in the lifecycle event messages, you IoT thing and client connection must have an exclusive association.

**Thing policy variables** - You can use thing policy variables to authorize device access to AWS IoT API operations. These variables allow you to write AWS IoT Core policies that grant or deny permissions based on thing properties like names, types, and attribute values. By using thing policy variables, you can apply the same policy to control multiple AWS IoT Core devices. This allows you to simplify policy management and reduce resource duplication. For more information, see [Thing policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/thing-policy-variables.html).

**Lifecycle events** - You can receive the thing name in lifecycle events (for example, connect, disconnect and subscribe, and unsubscribe). This allows processing of the thing name included in the messages, such as in rules. For more information, see [Lifecycle events](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html).

**Resource-specific logging** - You can configure resource-specific logging for thing groups, and easily apply the desired logging configuration for all things within the thing group defined. For more information, see [Configure Resource-specific overrides in AWS IoT (CLI)](configure-logging.md#fine-logging-cli).

**Cost allocation** - You can create billing groups with custom tags for cost allocation and add the things to these groups. For more information, see [Billing groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html).

## How to associate a thing to a connection
<a name="exclusive-thing-how-to"></a>

If your client ID matches your thing's name in the registry, after you attach an X.509 certificate to that IoT thing, AWS IoT Core will associate the client connection with the thing. If your client ID doesn't match the thing's name in the registry, you can exclusively attach an X.509 certificate to the thing to establish this association. The thing that has this exclusive attachment is called an exclusive thing. Otherwise, it's called a non-exclusive thing. When a certificate is associated with an exclusive thing, this certificate can only be associated with other things if you detach it from the exclusive thing. In this section, choose either AWS Management Console or AWS CLI to associate a thing to a connection.

### AWS Management Console
<a name="attach-thing-principal-console"></a>

**To attach a certificate to a thing exclusively using the AWS Management Console.**

1. Open the [AWS IoT home page](https://console.aws.amazon.com/iot/home#/home) in the AWS IoT console. On the left navigation, from **Security**, choose **Certificates**.

1. On the **Certificates** page, choose a certificate you want to attach a thing to. Then choose **Attach to things** from **Actions** on the upper right corner of the page.

   Alternatively, choose a certificate and navigate to the certificate details page. Choose the **Things** tab, then choose **Attach to things**.

1. On the **Attach certificate to thing(s)** page, check the **Associate thing to connection** check box. Then choose a thing to attach this certificate to from the **Things** dropdown list.

1. Choose **Attach thing(s)**. If the action succeeds, you will see a banner that says "Successfully attached a thing to your certificate", and the thing will be added to the **Things** tab.

**To detach a certificate from an exclusive thing using the AWS Management Console**

1. Open the [AWS IoT home page](https://console.aws.amazon.com/iot/home#/home) in the AWS IoT console. On the left navigation, from **Security**, choose **Certificates**.

1. On the **Certificates** page, choose a certificate and navigate to the certificate details page.

1. On the certificate details page, choose the **Things** tab. Then choose a thing that you want to detach the certificate to. Choose **Detach things**.

1. On the **Detach things** window, confirm your action. Choose **Detach**. If the action succeeds, you will see a banner that says "Successfully detached a thing from your certificate", and the thing will no longer appear in the **Things** tab.

### AWS CLI
<a name="attach-thing-principal-cli"></a>

1. To attach a certificate to an thing using AWS CLI, run the [**attach-thing-principal**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html) command. To specify the exclusive certificate-to-thing attachment, you must specify `EXCLUSIVE_THING` in the `--thing-principal-type` field. An example command can be the following.

   ```
   aws iot attach-thing-principal \
       --thing-name "thing_1" \
       --principal "arn:aws:iot:{{us-east-1}}:{{123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}" \
       --thing-principal-type "EXCLUSIVE_THING"
   ```

   This command doesn't produce any output. For more information, see [Attach a principal to a thing](attach-thing-principal.md).

1. To list the things associated with the specified certificate along with the attachment type, run the `list-principal-things-v2` command. The attachment type refers to how the certificate is attached to the thing. An example command can be the following.

   ```
   $ aws iot list-principal-things-v2 \
       --principal "arn:aws:iot:{{us-east-1:123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}"
   ```

   The output can look like the following.

   ```
   {
       "PrincipalThingObjects": [
           {
               "thingPrincipalType": "EXCLUSIVE_THING",
               "thing": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:thing/{{thing_1}}"
           }
       ]
   }
   ```

   For more information, see [List things associated with a principal V2](list-principal-things-v2.md).

1. To list the principals associated with the specified thing along with the attachment type, run the `list-thing-principals-v2` command . The attachment type refers to how the certificate is attached to the thing. An example command can be the following.

   ```
   $ aws iot list-thing-principals-v2 \
       --thing-name "thing_1"
   ```

   The output can look like the following.

   ```
   {
       "ThingPrincipalObjects": [
           {
               "thingPrincipalType": "EXCLUSIVE_THING",
               "principal": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}"
           }
       ]
   }
   ```

   For more information, see [List principals associated with a thing V2](list-thing-principals-v2.md).

1. To detach a certificate from a thing, run the [detach-thing-principal](https://docs.aws.amazon.com/cli/latest/reference/iot/detach-thing-principal.html) command.

   ```
   aws iot detach-thing-principal \
       --principal "arn:aws:iot:{{us-east-1}}:{{123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}" \
       --thing-name "thing_1"
   ```

   This command doesn't produce any output. For more information, see [Detach a principal from a thing](detach-thing-principal.md).