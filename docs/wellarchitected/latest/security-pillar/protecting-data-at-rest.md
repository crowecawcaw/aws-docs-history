# Protecting data at rest

_Data at rest_ represents any data that you persist in non-volatile
storage for any duration in your workload. This includes block storage, object storage,
databases, archives, IoT devices, and any other storage medium on which data is persisted.
Protecting your data at rest reduces the risk of unauthorized access, when encryption and
appropriate access controls are implemented.

Encryption and tokenization are two important but distinct data protection schemes.

_Tokenization_ is a process that allows you to define a token to
represent an otherwise sensitive piece of information (for example, a token to represent a
customer’s credit card number). A token must be meaningless on its own, and must not be
derived from the data it is tokenizing–therefore, a cryptographic digest is not usable as a
token. By carefully planning your tokenization approach, you can provide additional protection
for your content, and you can ensure that you meet your compliance requirements. For example,
you can reduce the compliance scope of a credit card processing system if you leverage a token
instead of a credit card number.

_Encryption_ is a way of transforming content in a manner that makes it
unreadable without a secret key necessary to decrypt the content back into plaintext. Both
tokenization and encryption can be used to secure and protect information as appropriate.
Further, masking is a technique that allows part of a piece of data to be redacted to a point
where the remaining data is not considered sensitive. For example, PCI-DSS allows the last
four digits of a card number to be retained outside the compliance scope boundary for
indexing.

**Audit the use of encryption keys:** Ensure that you
understand and audit the use of encryption keys to validate that the access control mechanisms
on the keys are appropriately implemented. For example, any AWS service using an AWS KMS key
logs each use in AWS CloudTrail. You can then query AWS CloudTrail, by using a tool such as Amazon CloudWatch Logs
Insights, to ensure that all uses of your keys are valid.

###### Best practices

- [SEC08-BP01 Implement secure key management](sec_protect_data_rest_key_mgmt.md "sec_protect_data_rest_key_mgmt.md")
- [SEC08-BP02 Enforce encryption at rest](sec_protect_data_rest_encrypt.md "sec_protect_data_rest_encrypt.md")
- [SEC08-BP03 Automate data at rest protection](sec_protect_data_rest_automate_protection.md "sec_protect_data_rest_automate_protection.md")
- [SEC08-BP04 Enforce access control](sec_protect_data_rest_access_control.md "sec_protect_data_rest_access_control.md")
