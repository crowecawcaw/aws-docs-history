# Data encryption

Data encryption refers to protecting data when at
 rest while stored
 in AWS CloudShell and when in transit it travels between AWS CloudShell and service endpoints. 


## Encryption at rest using AWS KMS

Encryption at rest refers to protecting your data from unauthorized access by encrypting data
 while stored. When using AWS CloudShell, you have persistent storage of 1 GB per AWS Region at
 no cost. Persistent storage is located in your home directory (`$HOME`)
 and is private to you. Unlike ephemeral environment resources that are recycled after each
 shell session ends, data in your home directory persists. 

The encryption of data stored in AWS CloudShell is implemented using cryptographic keys provided by
 AWS Key Management Service (AWS KMS). This is a managed AWS service for creating and controlling AWS KMS keys—the encryption keys used to encrypt customer data that’s stored in
 the AWS CloudShell environment. AWS CloudShell generates and manages cryptographic keys for encrypting
 data on behalf of customers.


## Encryption in transit


Encryption in transit refers to protecting your data from being intercepted while it

 moves between communication endpoints.

By default, all data communication between the client's web browser computer and the cloud-based AWS CloudShell is encrypted by sending everything through an HTTPS/TLS connection.


 You don't need to do anything to enable the use of HTTPS/TLS for communication.
