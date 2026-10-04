

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Delete a Hyperledger Fabric Network on Amazon Managed Blockchain (AMB)
<a name="delete-network"></a>

A Hyperledger Fabric network on Amazon Managed Blockchain (AMB) remains active as long as there are members. A network is deleted only when the last member deletes itself from the network. No member or AWS account, even the creator's AWS account, can delete the network until they are the last member and delete themselves. When you delete the last member, all resources for that member and the blockchain network are deleted. For more information, see [Delete a Member in Your AWS Account](managed-blockchain-members.md#managed-blockchain-delete-account-member).