

# Encryption in transit
<a name="next-gen-encryption-in-transit"></a>

All data in transit is encrypted using TLS 1.2 or later, including:
+ API calls to Next generation Resilience Hub endpoints
+ Cross-service communication (Next generation Resilience Hub to topology service, Next generation Resilience Hub to Amazon Bedrock)
+ Cross-account credential passing (encrypted with AWS KMS before transmission)