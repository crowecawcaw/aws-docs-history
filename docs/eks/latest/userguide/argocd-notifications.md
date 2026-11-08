

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Send notifications for Argo CD Applications
<a name="argocd-notifications"></a>

The EKS Capability for Argo CD runs a managed notifications controller. Use it to send a message when an Application syncs, fails to sync, or changes health, so that your team learns about deployment outcomes without watching the Argo CD UI.

Notifications have three parts:

1. An `argocd-notifications-cm` ConfigMap in your Argo CD namespace that defines your services, triggers, and message templates.

1. An optional `argocd-notifications-secret` Secret in the same namespace that holds credentials, such as a Slack token.

1. An annotation on each Application that subscribes it to a trigger and a destination.

The capability does not create these resources for you, and it does not install a catalog of predefined triggers and templates. You author the triggers and templates that you need. For the trigger expression syntax, the template fields, and the options that each service accepts, see [Notifications](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/) in the Argo CD documentation.

## Prerequisites
<a name="_prerequisites"></a>
+ An EKS cluster with the Argo CD capability created. See [Create an Argo CD capability](create-argocd-capability.md).
+ The `kubectl` CLI configured to communicate with your cluster.
+ At least one Argo CD Application. See [Create Applications](argocd-create-application.md).

## Enable notifications
<a name="argocd-notifications-enable"></a>

The notifications controller ignores a ConfigMap that does not carry an opt-in label. To turn notifications on, add the following label to your `argocd-notifications-cm` ConfigMap:

```
labels:
  eks.amazonaws.com/managed-notifications: "enabled"
```

**Note**  
The label value must be exactly `enabled`. Without the label, the capability reads no configuration from the ConfigMap and sends no notifications. The label is required on every notifications ConfigMap, including the one in your primary Argo CD namespace.

The `argocd-notifications-secret` Secret does not need the label.

## Example: notify a Slack channel
<a name="_example_notify_a_slack_channel"></a>

The following example sends a message to Slack when an Application syncs successfully.

Create the ConfigMap and the Secret in your primary Argo CD namespace:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-notifications-cm
  namespace: argocd
  labels:
    eks.amazonaws.com/managed-notifications: "enabled"
data:
  service.slack: |
    token: $slack-token
  trigger.on-sync-succeeded: |
    - when: app.status.operationState.phase in ['Succeeded']
      send: [app-sync-succeeded]
  template.app-sync-succeeded: |
    message: "Application {{.app.metadata.name}} synced successfully."
---
apiVersion: v1
kind: Secret
metadata:
  name: argocd-notifications-secret
  namespace: argocd
type: Opaque
stringData:
  slack-token: <SLACK_BOT_TOKEN>
```

Replace `<SLACK_BOT_TOKEN>` with your Slack bot token. The `$slack-token` reference in the service definition resolves to the `slack-token` key in the Secret. To keep the token out of the Secret entirely, store an AWS Secrets Manager ARN as the value instead, as described in [Store credentials in AWS Secrets Manager](#argocd-notifications-secrets).

### Subscribe an Application
<a name="_subscribe_an_application"></a>

Add an annotation to each Application that you want notifications for. The annotation names a trigger and a service, and its value is the recipient.

```
metadata:
  annotations:
    notifications.argoproj.io/subscribe.on-sync-succeeded.slack: my-channel
```

Replace `my-channel` with the name of your Slack channel. Sync the Application and check the channel. If no message arrives, see [Monitor and troubleshoot notifications](#argocd-notifications-troubleshooting).

## Supported notification services
<a name="argocd-notifications-services"></a>

The capability supports 16 service types:

 **Chat and collaboration**   
 `slack`, `googlechat`, `mattermost`, `teams-workflows`, `telegram`, `webex` 

 **Incident management**   
 `pagerduty`, `pagerdutyv2`, `opsgenie` 

 ** AWS **   
 `awssqs`, `eventbridge` 

 **Other**   
 `github`, `grafana`, `newrelic`, `pushover`, `gcppubsub` 

A `service.` key for any other type is dropped, and the rest of your configuration still loads. Upstream Argo CD also supports the `email`, `teams`, `webhook`, `rocketchat`, `nats`, and `alertmanager` service types. These are not available in the managed capability. The `eventbridge` service is specific to this capability and has no upstream equivalent.

**Important**  
A supported service whose options are invalid behaves differently from an unsupported one. An unsupported service type is dropped on its own. An invalid service definition fails the whole namespace’s configuration, so that namespace sends no notifications at all until you correct it. The capability records a `NotificationConfigInvalid` event on the ConfigMap, as described in [Monitor and troubleshoot notifications](#argocd-notifications-troubleshooting).

**Important**  
The `gcppubsub` service requires inline credentials in this capability. Set `keyJSON` to a `$` reference for the service account key JSON in your Secret, as in `keyJSON: $gcp-key`.  
The capability rejects both the `keyFile` path and Application Default Credentials, which are the two approaches the upstream Argo CD documentation describes. Because a rejected service definition fails the whole namespace’s configuration, following the upstream instructions for this service stops notifications for every other service in the same ConfigMap.

**Note**  
Declare services as `service.` keys in `argocd-notifications-cm`. Upstream Argo CD also honors a deprecated `notifiers.yaml` key in the notification Secret that registers services directly. The capability ignores that key, because a service declared there would bypass the supported-service check.

## Send to Amazon SQS and Amazon EventBridge
<a name="argocd-notifications-aws"></a>

The `awssqs` and `eventbridge` services authenticate with your IAM Capability Role. They take no credentials in the service definition, so you grant access through the role’s IAM policy rather than storing keys in the Secret.

### Grant permissions to the Capability Role
<a name="_grant_permissions_to_the_capability_role"></a>

Attach a policy to your IAM Capability Role with only the statements that you need. In the following example, replace the AWS Region, the account ID, and the queue, key, and event bus names with your own values.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SendToQueue",
      "Effect": "Allow",
      "Action": [
        "sqs:GetQueueUrl",
        "sqs:SendMessage"
      ],
      "Resource": "arn:aws:sqs:us-west-2:111122223333:my-queue"
    },
    {
      "Sid": "DecryptQueueKmsKey",
      "Effect": "Allow",
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:us-west-2:111122223333:key/my-key-id"
    },
    {
      "Sid": "PutEvents",
      "Effect": "Allow",
      "Action": "events:PutEvents",
      "Resource": "arn:aws:events:us-west-2:111122223333:event-bus/my-event-bus"
    }
  ]
}
```

The queue statement needs both actions. The controller looks up the queue URL from the queue name before each send, so `sqs:SendMessage` alone is not enough. Include the AWS KMS statement only if your queue is encrypted with a customer managed key.

### Configure the services
<a name="_configure_the_services"></a>

Add the services to `argocd-notifications-cm`:

```
  service.awssqs: |
    queue: my-queue
    region: us-west-2
    account: "111122223333"
  service.eventbridge: |
    region: us-west-2
    eventBusName: my-event-bus
    source: argocd
    detailType: argocd-sync
```

The fields have the following effects:

 `queue`   
The name of the queue, not its URL. For a FIFO queue, the name ends in `.fifo`.

 `region`   
The AWS Region of the queue or event bus.

 `account`   
The AWS account that owns the queue. Set it when the queue is in another account.

 `eventBusName`   
The event bus to publish to. If you omit it, the default bus is used. For an event bus in another account, use the full event bus ARN.

 `source`   
The `source` field of the published event. The default is `argocd`.

 `detailType`   
The `detail-type` field of the published event. The default is `argocd-notification`.

Subscribe an Application with the queue name or the event bus name as the recipient:

```
metadata:
  annotations:
    notifications.argoproj.io/subscribe.on-sync-succeeded.awssqs: my-queue
    notifications.argoproj.io/subscribe.on-sync-succeeded.eventbridge: my-event-bus
```

The recipient in the annotation takes precedence over the queue or event bus in the service definition.

Both services can send to another AWS Region or another account, as long as the Capability Role has the required permissions:
+ For a queue or event bus in another Region, set `region` to that Region.
+ For a queue in another account, set `account` to the owning account ID, and add a resource policy on the queue that allows the Capability Role.
+ For an event bus in another account, set `eventBusName` to the full event bus ARN rather than the name, and add a resource policy on the bus that allows the Capability Role.

**Note**  
EventBridge requires the event detail to be a JSON object, and the capability sends your template’s `message` as the detail. Write the template to produce valid JSON, for example `message: '{"app": "{{.app.metadata.name}}"}'`.

**Note**  
A successful `PutEvents` call that matches no EventBridge rule succeeds silently. To confirm that events arrive, add a rule that matches your `source` value, such as `{"source":["argocd"]}`, with a target you can read, such as a CloudWatch log group.

## Store credentials in AWS Secrets Manager
<a name="argocd-notifications-secrets"></a>

Instead of storing a credential in `argocd-notifications-secret`, you can store a Secrets Manager ARN as the value. The capability resolves the ARN at send time using your IAM Capability Role.

1. Store the ARN as the value of the key:

   ```
   stringData:
     slack-token: arn:aws:secretsmanager:us-west-2:111122223333:secret:my-secret
   ```

1. Reference the key from your service definition with `$`, exactly as you would for a literal value:

   ```
     service.slack: |
       token: $slack-token
   ```

1. Grant the Capability Role read access to the secret:

   ```
   {
     "Effect": "Allow",
     "Action": "secretsmanager:GetSecretValue",
     "Resource": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-secret-*"
   }
   ```

If the secret is encrypted with a customer managed AWS KMS key, also allow `kms:Decrypt` on that key.

Resolution behaves as follows:
+ A value that is not a Secrets Manager ARN is used exactly as written.
+ The secret can be in any account, in any Region of the same partition as your capability. A cross-account secret needs a resource policy that allows the Capability Role, and must use a customer managed AWS KMS key whose key policy also allows the role.
+ References resolve one level only. If the value of a secret is itself a Secrets Manager ARN, the reference is rejected.
+ A resolved value is reused for about 5 minutes, so a rotated secret is picked up within about 5 minutes.
+ Resolution fails closed. A reference that cannot be resolved is dropped and is never sent. The service configuration keeps the literal `$` reference instead, so the send fails at any destination that authenticates it.

When a reference is dropped, the capability records a `NotificationSecretRejected` event on your `argocd-notifications-cm` that names the key and the reason. Common reasons are that the secret was not found, access was denied, the secret is empty, or the secret is in a different partition. When every key resolves again, the capability records a `NotificationSecretResolved` event.

## Configure notifications per namespace
<a name="argocd-notifications-selfservice"></a>

By default, the capability reads notification configuration only from your primary Argo CD namespace. If you run Applications in additional namespaces, you can let each namespace carry its own notification configuration.

1. In the `argocd-cmd-params-cm` ConfigMap in your primary Argo CD namespace, list the namespaces and turn on self-service configuration:

   ```
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: argocd-cmd-params-cm
     namespace: argocd
   data:
     application.namespaces: "team-a-gitops,team-b-gitops"
     notificationscontroller.selfservice.enabled: "true"
   ```

   The value of `notificationscontroller.selfservice.enabled` must be exactly `true`. Any other value, such as `True` or `yes`, turns the setting off. For more information about `application.namespaces`, see [Configure namespaces for Applications and ApplicationSets](argocd-configure-settings.md#argocd-configure-resource-namespaces).

1. In each namespace, create an `argocd-notifications-cm` ConfigMap with the opt-in label, and optionally its own `argocd-notifications-secret`.

1. Wait for the change to apply. A change to `argocd-cmd-params-cm` can take up to about 10 minutes to reach the notifications controller.

**Important**  
List each namespace by its exact name. A namespace that `application.namespaces` matches only with a wildcard, such as `team-*`, can still run Applications, but the capability does not read its notification configuration. The capability records a `NotificationConfigNotRead` event on that namespace’s ConfigMap.

**Self-service configuration withholds credentials from templates**  
Turning on self-service configuration withholds the `{{ .secrets }}` template variable from **every** notification configuration, including the one in your primary Argo CD namespace. This matches upstream Argo CD, where the setting is process-wide.  
A template that still references `{{ .secrets }}` then behaves in one of three ways, depending on how it is written:  
 `{{ .secrets.mykey }}` renders the literal text `<no value>`, and the notification is still sent without the credential.
 `{{ index .secrets "my-key" }}` fails to render, which blocks the send and records a `NotificationFailed` event on the Application.
 `{{ .secrets.my-key }}` fails to parse, which stops the whole namespace’s configuration from loading.
Reference credentials from the service definition with `$`, as in `token: $slack-token`, rather than from a template. A `$` reference is resolved before this setting applies, and works whether self-service configuration is on or off.

## Differences from upstream Argo CD
<a name="argocd-notifications-limits"></a>

### Supported configuration keys
<a name="_supported_configuration_keys"></a>

The capability reads the following keys from `argocd-notifications-cm`:
+  `service.` keys for the service types in [Supported notification services](#argocd-notifications-services) 
+  `trigger.` keys
+  `template.` keys
+  `subscriptions` 
+  `defaultTriggers` 
+  `context` 

Any other key is dropped, and the rest of your configuration still loads.

### Size limits
<a name="_size_limits"></a>
+ A `template.` or `trigger.` value over 64 KiB is dropped. The rest of the configuration still loads, and notifications that use the dropped key fail.
+ A ConfigMap whose keys and values total more than 256 KiB is ignored completely, and no notification configuration is read from it.
+ A template function that would produce more than 64 KiB of output fails.

### Template functions
<a name="_template_functions"></a>

Templates can use the Sprig function library, with the following exceptions. These functions are not available:
+ Environment and DNS functions: `env`, `expandenv`, and `getHostByName` 
+ Copy and merge functions: `deepCopy`, `mustDeepCopy`, `merge`, `mergeOverwrite`, `mustMerge`, and `mustMergeOverwrite` 
+ Cryptographic and key generation functions: `bcrypt`, `htpasswd`, `derivePassword`, `genPrivateKey`, `genCA`, `genSelfSignedCert`, `genSignedCert`, `genCAWithKey`, `genSelfSignedCertWithKey`, `genSignedCertWithKey`, and `buildCustomCert` 
+ Generator functions: `until`, `untilStep`, `seq`, `randAlpha`, `randAlphaNum`, `randAscii`, `randNumeric`, `randBytes`, and `wrapWith` 
+ List functions: `uniq` and `mustUniq` 

The `printf`, `repeat`, `indent`, `nindent`, `replace`, and `regexReplaceAll` functions are available, but fail if a single call would produce more than 64 KiB of output.

A template that names an unavailable function stops its namespace’s configuration from loading.

### Destination requirements
<a name="_destination_requirements"></a>

For services where you supply a URL, the destination must meet the following requirements:
+ The URL uses `https`. A plain `http` URL is refused.
+ The host is a host name, not an IP address, and it resolves to a public address. A private or link-local address is refused.
+ TLS certificate verification is always on. If you set `insecureSkipVerify` to `true`, the capability resets it to `false`.

## Monitor and troubleshoot notifications
<a name="argocd-notifications-troubleshooting"></a>

### Check events
<a name="_check_events"></a>

The capability records Kubernetes events that explain why a notification did not arrive. To see them, describe the object that the event is recorded on.

Events on `argocd-notifications-cm` in the namespace that owns the configuration:

```
kubectl describe configmap argocd-notifications-cm -n argocd
```

 `NotificationConfigInvalid`   
The namespace’s configuration failed to load. The message gives the reason, such as a template that does not parse.

 `NotificationConfigValid`   
The configuration loaded successfully.

 `NotificationConfigNotRead`   
The namespace’s configuration is never read. Add the namespace to `application.namespaces` by name, and add the opt-in label to its ConfigMap.

 `NotificationSecretRejected`   
One or more Secrets Manager references were dropped. The message names each key and its reason.

 `NotificationSecretResolved`   
Every Secrets Manager reference resolved again.

Events on an Application:

```
kubectl describe application {{my-app}} -n argocd
```

 `NotificationFailed`   
A send to a destination failed. The message carries the destination’s own error.

 `NotificationTimeout`   
A send to a destination timed out.

**Note**  
An event that reports recovery, such as `NotificationConfigValid`, is a separate event rather than a removal of the warning that preceded it. Both events remain, so compare their timestamps. A recovery event that is newer than the warning means the problem is resolved.

### Review controller logs
<a name="_review_controller_logs"></a>

To investigate a problem that the events do not explain, deliver the notifications controller’s logs to CloudWatch Logs, Amazon S3, or Amazon Data Firehose. Use the Amazon EKS capability log type `EKS_CAPABILITY_ARGOCD_NOTIFICATION_LOGS`. For instructions, see [Access EKS Capabilities controller logs](capabilities-controller-logs.md).

### Common causes
<a name="_common_causes"></a>

No notifications at all  
Confirm that your `argocd-notifications-cm` carries the `eks.amazonaws.com/managed-notifications: "enabled"` label, with that exact value.

Notifications work from the primary namespace but not from another namespace  
Confirm that you listed the namespace by name in `application.namespaces`, that you set `notificationscontroller.selfservice.enabled` to `true`, and that the namespace’s own ConfigMap carries the opt-in label.

A message arrives with `<no value>` in place of a credential  
One of your templates references `{{ .secrets }}` while self-service configuration is on. Reference the credential from the service definition with `$` instead. For more information, see [Configure notifications per namespace](#argocd-notifications-selfservice).

A destination rejects the credential  
Check for a `NotificationSecretRejected` event. If the capability dropped a Secrets Manager reference, it sends the literal `$` reference in place of the credential.

A service you configured is ignored  
Confirm that your service type is listed in [Supported notification services](#argocd-notifications-services).

## Next steps
<a name="_next_steps"></a>
+  [Create Applications](argocd-create-application.md) - Create Applications to subscribe to notifications
+  [Access EKS Capabilities controller logs](capabilities-controller-logs.md) - Deliver controller logs to CloudWatch Logs, Amazon S3, or Amazon Data Firehose
+  [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md) - Troubleshoot other Argo CD issues