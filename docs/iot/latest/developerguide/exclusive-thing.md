# Associating an AWS IoT thing to an MQTT client

connection

An exclusive thing association is when you attach an X.509 certificate to a single
AWS IoT thing. In this case, the certificate cannot be used with other things. By ensuring
that a certificate is used only by a single IoT thing, it helps prevent security
vulnerabilities.

In AWS IoT, the client ID is a unique identifier for a thing or a device when it connects
to the AWS IoT Core MQTT broker. If you use a non-exclusive association, multiple things can
be attached to the same certificate. When non-exclusive thing association is in place, to
maintain a clear association and to avoid potential conflicts, you must match your client
ID with the thing name.

###### In this topic

- [Use cases](#exclusive-thing-benefits "#exclusive-thing-benefits")
- [How to associate a thing to a
  connection](#exclusive-thing-how-to "#exclusive-thing-how-to")

## Use cases

Associating a thing to a connection provides the following capabilities.

###### Note

Note that if your IoT thing and client connection has a non-exclusive association,
you can use all the following capabilities except the lifecycle events
capability. To include your thing name in the lifecycle event messages, you IoT
thing and client connection must have an exclusive association.

**Thing policy variables** - You can use thing policy
variables to authorize device access to AWS IoT API operations. These variables allow
you to write AWS IoT Core policies that grant or deny permissions based on thing
properties like names, types, and attribute values. By using thing policy variables,
you can apply the same policy to control multiple AWS IoT Core devices. This allows you
to simplify policy management and reduce resource duplication. For more information,
see [Thing policy
variables](thing-policy-variables.md "thing-policy-variables.md").

**Lifecycle events** - You can receive the thing name
in lifecycle events (for example, connect, disconnect and subscribe, and
unsubscribe). This allows processing of the thing name included in the messages,
such as in rules. For more information, see [Lifecycle
events](life-cycle-events.md "life-cycle-events.md").

**Resource-specific logging** - You can configure resource-specific logging for thing groups, and easily apply the desired logging configuration for all things within the thing group defined. For more
information, see [Configure Resource-specific overrides in AWS IoT (CLI)](configure-logging.md#fine-logging-cli "configure-logging.md#fine-logging-cli").

**Cost allocation** - You can create billing groups
with custom tags for cost allocation and add the things to these groups. For more
information, see [Billing
groups](tagging-iot-billing-groups.md "tagging-iot-billing-groups.md").

## How to associate a thing to a

connection

If your client ID matches your thing's name in the registry, after you attach an
X.509 certificate to that IoT thing, AWS IoT Core will associate the client connection
with the thing. If your client ID doesn't match the thing's name in the registry,
you can exclusively attach an X.509 certificate to the thing to establish this
association. The thing that has this exclusive attachment is called an exclusive
thing. Otherwise, it's called a non-exclusive thing. When a certificate is
associated with an exclusive thing, this certificate can only be associated with
other things if you detach it from the exclusive thing. In this section, choose
either AWS Management Console or AWS CLI to associate a thing to a connection.

###### To attach a certificate to a thing exclusively using the

AWS Management Console.

1. Open the [AWS IoT home
   page](https://console.aws.amazon.com//iot/home#/home "https://console.aws.amazon.com//iot/home#/home") in the AWS IoT console. On the left navigation, from
   **Security**, choose
   **Certificates**.
2. On the **Certificates** page, choose a certificate
   you want to attach a thing to. Then choose **Attach to
   things** from **Actions** on the upper
   right corner of the page.

Alternatively, choose a certificate and navigate to the certificate
details page. Choose the **Things** tab, then choose
**Attach to things**. 3. On the **Attach certificate to thing(s)** page,
check the **Associate thing to connection** check
box. Then choose a thing to attach this certificate to from the
**Things** dropdown list. 4. Choose **Attach thing(s)**. If the action
succeeds, you will see a banner that says "Successfully attached a
thing to your certificate", and the thing will be added to the
**Things** tab.

###### To detach a certificate from an exclusive thing using the

AWS Management Console

1. Open the [AWS IoT home
   page](https://console.aws.amazon.com//iot/home#/home "https://console.aws.amazon.com//iot/home#/home") in the AWS IoT console. On the left navigation, from
   **Security**, choose
   **Certificates**.
2. On the **Certificates** page, choose a
   certificate and navigate to the certificate details page.
3. On the certificate details page, choose the
   **Things** tab. Then choose a thing that you
   want to detach the certificate to. Choose **Detach
   things**.
4. On the **Detach things** window, confirm your
   action. Choose **Detach**. If the action succeeds,
   you will see a banner that says "Successfully detached a thing from
   your certificate", and the thing will no longer appear in the
   **Things** tab.

5. To attach a certificate to an thing using AWS CLI, run the [**attach-thing-principal**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html") command. To specify
   the exclusive certificate-to-thing attachment, you must specify
   `EXCLUSIVE_THING` in the
   `--thing-principal-type` field. An example command
   can be the following.

```
aws iot attach-thing-principal \
    --thing-name "thing_1" \
    --principal "arn:aws:iot:`us-east-1`:`123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`" \
    --thing-principal-type "EXCLUSIVE_THING"
```

This command doesn't produce any output. For more information, see [Attach a principal to a thing](attach-thing-principal.md "attach-thing-principal.md"). 2. To list the things associated with the specified certificate along with the
attachment type, run the `list-principal-things-v2` command. The
attachment type refers to how the certificate is attached to the thing. An
example command can be the following.

```
$ aws iot list-principal-things-v2 \
    --principal "arn:aws:iot:`us-east-1:123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`"
```

The output can look like the following.

```
{
    "PrincipalThingObjects": [
        {
            "thingPrincipalType": "EXCLUSIVE_THING",
            "thing": "arn:aws:iot:`us-east-1`:`123456789012`:thing/`thing_1`"
        }
    ]
}
```

For more information, see [List things associated with a principal
V2](list-principal-things-v2.md "list-principal-things-v2.md"). 3. To list the principals associated with the specified thing along with the
attachment type, run the `list-thing-principals-v2` command . The
attachment type refers to how the certificate is attached to the thing. An
example command can be the following.

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
            "principal": "arn:aws:iot:`us-east-1`:`123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`"
        }
    ]
}
```

For more information, see [List principals associated with a thing
V2](list-thing-principals-v2.md "list-thing-principals-v2.md"). 4. To detach a certificate from a thing, run the [detach-thing-principal](../../../cli/latest/reference/iot/detach-thing-principal.md "../../../cli/latest/reference/iot/detach-thing-principal.md") command.

```
aws iot detach-thing-principal \
    --principal "arn:aws:iot:`us-east-1`:`123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`" \
    --thing-name "thing_1"
```

This command doesn't produce any output. For more information, see [Detach a principal from a thing](detach-thing-principal.md "detach-thing-principal.md").
