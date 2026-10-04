

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Data protection for Amazon Managed Blockchain (AMB) Access Ethereum
<a name="ethereum-data-protection"></a>

Data encryption helps prevent unauthorized users from reading data from a blockchain network and the associated data storage systems. This includes data that might be intercepted as it travels the network, known as *data in transit*.

## Encryption in transit
<a name="managed-blockchain-encryption-in-transit"></a>

By default, AMB Access uses an HTTPS/TLS connection to encrypt all the data that's transmitted from a client computer that runs the AWS CLI to AWS service endpoints.

You don't need to do anything to enable the use of HTTPS/TLS. It's always enabled unless you explicitly disable it for an individual AWS CLI command by using the `--no-verify-ssl` command line option.