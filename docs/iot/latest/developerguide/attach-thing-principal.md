# Attach a principal to a thing

A physical device can use a principal to communicate with AWS IoT. A principal can
be an X.509 certificate or an Amazon Cognito ID. You can associate a certificate or an Amazon Cognito
ID with the thing in the registry that represents your device, by running the [attach-thing-principal](../../../cli/latest/reference/iot/attach-thing-principal.md "../../../cli/latest/reference/iot/attach-thing-principal.md") command.

To attach a certificate or an Amazon Cognito ID to your thing, use the [attach-thing-principal](../../../cli/latest/reference/iot/attach-thing-principal.md "../../../cli/latest/reference/iot/attach-thing-principal.md") command:

```
$ aws iot attach-thing-principal \
    --thing-name "MyLightBulb1" \
    --principal "arn:aws:iot:`us-east-1`:`123456789012`:cert/`a0c01f5835079de0a7514643d68ef8414ab739a1e94ee4162977b02b12842847`"
```

To attach a certificate to your thing with an attachment type (exclusive
attachment or non-exclusive attachment), use the [**attach-thing-principal**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html") command and
specify a type in the `--thing-principal-type` field. An exclusive
attachment means your IoT thing is the only thing attached to the certificate, and
this certificate cannot be associated with any other things. An non-exclusive
attachment means your IoT thing is attached to the certificate, and this certificate
can be associated with other things. For more information, see [Associating an AWS IoT thing to an MQTT client
connection](exclusive-thing.md "exclusive-thing.md").

###### Note

For the [Associating an AWS IoT thing to an MQTT client
connection](exclusive-thing.md "exclusive-thing.md") feature, you can only use X.509
certificate as a principal.

```
$ aws iot attach-thing-principal \
    --thing-name "MyLightBulb2" \
    --principal "arn:aws:iot:`us-east-1`:`123456789012`:cert/`a0c01f5835079de0a7514643d68ef8414ab739a1e94ee4162977b02b12842847`" \
    --thing-principal-type "EXCLUSIVE_THING"
```

If the attachment is successful, the **AttachThingPrincipal**
command does not produce any output. To describe the attachment, use
list-thing-principals-v2 CLI command.

For more information, see [AttachThingPrincipal](../apireference/API_AttachThingPrincipal.md "../apireference/API_AttachThingPrincipal.md") from the _AWS IoT Core API
Reference_.
