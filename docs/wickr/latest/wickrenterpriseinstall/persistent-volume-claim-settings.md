This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Persistent volume claim settings

Wickr Enterprise requires Persistent Volume Claims to store stateful data. This setting
allows you to specify the name of the name of the Storage Class you would like to use. If left
blank Wickr will attempt to use the default Storage Class. Changing the Storage Class after
Wickr has been deployed is not supported.

A default StorageClass for Persistent Volume Claims is often provided by cloud providers,
however in fully onprem installations it may require explicit configuration using a third party
service such as [Longhorn](https://longhorn.io/ "https://longhorn.io/").
