

# Create a context store

Create a context store in a global network. Each global network can have one context store. When created, a context store starts in the `PENDING` state and then moves to `AVAILABLE`. You can optionally associate registered transit gateways while creating the context store or create the associations after the context store is `AVAILABLE`. For more information, see [Associate a transit gateway with a context store using AWS Network Manager](context-store-associations.md#associate-context-store).

**To create a context store**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Context Store**.

1. Choose **Create context store**.

1. (Optional) Enter a **Name tag**.

1. (Optional) Enter a **Description**.

1. (Optional) Under **Create associations**, choose one or more registered transit gateways to associate with the context store.

1. (Optional) Under **Additional settings**, enter a tag **Key** and **Value**. To add another tag, choose **Add tag**.

1. Choose **Create context store**.

1. Wait until the context store state is `AVAILABLE`. If you selected transit gateways during creation, wait until their association state is `ASSOCIATED`.

**To create a context store using the AWS CLI**  
Use the [create-context-store](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/create-context-store.html) command and specify the ID of the global network where you want to create the context store. You can also specify a description and tags.

## Grant firewall access to a context store
<a name="grant-context-store-access"></a>

After you create a context store, grant the firewall permission to read it. The required IAM role and permissions depend on the firewall integration.

### AWS Network Firewall
<a name="grant-context-store-access-nfw"></a>

AWS Network Firewall uses a service-specific IAM role and trust policy to access the context store. To configure access, see the [AWS Network Firewall documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/). The IAM role and trust policy in the following section apply to other firewall integrations, not to AWS Network Firewall.

### Other firewall integrations
<a name="grant-context-store-access-firewall"></a>

Create an IAM role in the account that owns the context store. Your firewall provider supplies the AWS principal ARN and external ID for the role trust policy. The firewall integration assumes the role to read context records.

The following trust policy allows the provider principal to assume the role. Replace the example values with the principal ARN and external ID supplied by your firewall provider.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "{{firewall-provider-principal-arn}}"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "{{external-id}}"
        }
      }
    }
  ]
}
```

Attach the following permissions policy to the role. Replace the example account ID and context store ID with the account ID and ID of your context store.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadContextStore",
      "Effect": "Allow",
      "Action": [
        "networkmanager:ListContexts",
        "networkmanager:GetContextVersion",
        "networkmanager:ListContextChanges"
      ],
      "Resource": "arn:aws:networkmanager::{{123456789012}}:context-store/{{context-store-id}}"
    }
  ]
}
```

After you create the role, follow your firewall provider's instructions to link the role and context store to the firewall integration.