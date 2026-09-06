

# How Amazon Data Firehose uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_AKF"></a>

You can use Amazon Data Firehose to deliver real-time streaming data to various streaming destinations. When the destination requires a credentials or key, Firehose retrieves a secret from Secrets Manager at runtime to connect to the destination. For more information, see [Authenticate with AWS Secrets Manager in Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/using-secrets-manager.html) in the *Amazon Data Firehose Developer Guide*.