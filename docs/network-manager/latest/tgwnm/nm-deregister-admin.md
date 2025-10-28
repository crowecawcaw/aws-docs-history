# Deregister an administrator from multi-account in an AWS

global network

Deregistering delegated administrators removes that account's permission to manage global
networks for your organization. All registered transit gateways from other member accounts are
deregistered from the specific delegated administrator's global networks. For more information
about how deregistering delegated administrators works, see [Deregister delegated
administrators](nm-multi-account.md#nm-how-it-works-deregister "nm-multi-account.md#nm-how-it-works-deregister").

###### To deregister a delegated administrator

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home") with the management account.
2. Under **Connectivity**, choose **Global Networks**.
3. In the navigation pane, choose **Settings**.
4. In the **Delegated Administrators** section, choose one or more
   accounts that you want to deregister.

Depending on your organization size and the number of delegated administrators you're
deregistering, this could take several minutes. During this time you won't be able to
register any new delegated administrators.
