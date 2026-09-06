

# Encryption at Rest
<a name="encryption-at-rest"></a>

Output of your Amazon Polly voice synthesis can be saved on your own system. You can also call Amazon Polly, and then encrypt the file with any encryption key of your choice and store it in Amazon Simple Storage Service (Amazon S3) or another secure storage. The Amazon Polly [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/APIReference/API_SynthesizeSpeech.html) operation is stateless and is not associated with a customer identity. You can't retrieve it from Amazon Polly later.