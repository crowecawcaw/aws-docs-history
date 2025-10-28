# Data protection for Amazon Managed Blockchain (AMB) Access Ethereum

Data encryption helps prevent unauthorized users from reading data from a blockchain network
and the associated data storage systems. This includes data that might be intercepted as it
travels the network, known as _data in transit_.

## Encryption in transit

By default, AMB Access uses an HTTPS/TLS connection to encrypt all the data that's transmitted
from a client computer that runs the AWS CLI to AWS service endpoints.

You don't need to do anything to enable the use of HTTPS/TLS. It's always enabled unless
you explicitly disable it for an individual AWS CLI command by using the `--no-verify-ssl` command
line option.
