

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Persistent volume claim settings
<a name="persistent-volume-claim-settings"></a>

Wickr Enterprise requires Persistent Volume Claims to store stateful data. This setting allows you to specify the name of the name of the Storage Class you would like to use. If left blank Wickr will attempt to use the default Storage Class. Changing the Storage Class after Wickr has been deployed is not supported.

A default StorageClass for Persistent Volume Claims is often provided by cloud providers, however in fully onprem installations it may require explicit configuration using a third party service such as [Longhorn](https://longhorn.io/).