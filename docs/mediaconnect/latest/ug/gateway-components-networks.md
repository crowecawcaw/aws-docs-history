

# MediaConnect Gateway networks
<a name="gateway-components-networks"></a>



An AWS Elemental MediaConnect Gateway *network* is a collection of IP information that will be used by the instances and bridges to communicate on your local data center network. The gateway network information must match the local data center network that you are using to communicate with the gateway. Each gateway may contain a maximum of two networks. All gateways must contain at least one network. 

## Key points
<a name="gateway-components-networks-key-points"></a>
+ Networks are automatically created during the initial setup process of a new gateway.
+ You can't add or edit a network after the initial creation of the gateway. 
+ Networks are deleted as part of the gateway deletion process. 

## Next steps
<a name="gateway-components-networks-next-steps"></a>
+ To learn about creating a gateway and its networks, see [Setting up a MediaConnect Gateway](gateway-create.md).
+ To learn about deleting a gateway and its networks, see [Removing a MediaConnect Gateway](gateway-cleanup-console.md).