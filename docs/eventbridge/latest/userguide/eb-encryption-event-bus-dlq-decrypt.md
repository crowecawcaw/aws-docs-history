# Decrypting events in EventBridge dead-letter queues

Once you've resolved the underlying issue that is causing a non-retriable error,
you can process the events sent to the event bus or target DLQs.
For encrypted events, you must first decrypt the event in order to process it.

The following example demonstrates how to decrypt an event that EventBridge has delivered to an event bus or target DLQ.

````
// You will receive an encrypted event in the following json format.
        // ```
        //   {
        //     "version": "0",
        //     "id": "`053afa53-cdd7-285b-e754-b0dfd0ac0bfb`",  // New event id not the same as the original one
        //     "account": "`123456789012`",
        //     "time": "`2020-02-10T10:22:00Z`",
        //     "resources": [ ],
        //     "region": "`us-east-1`",
        //     "source": "aws.events",
        //     "detail-type": "Encrypted Events",
        //     "detail": {
        //       "event-bus-arn": "arn:aws:events:`region`:`account`:event-bus/`bus-name`",
        //       "rule-arn": "arn:aws:events:`region`:`account`:event-bus/`bus-name`/`rule-name`",
        //       "kms-key-arn": "arn:aws:kms:`region`:`account`:key/`key-arn`",
        //       "encrypted-payload": "`AgR4qiru/XNwTUyCgRHqP7rbbHn/xpmVeVeRIAd12TDYYVwAawABABRhd3M6ZXZlbnRzOmV2ZW50LWJ1cwB
 // RYXJuOmF3czpldmVudHM6dXMtZWFzdC0xOjE0NjY4NjkwNDY3MzpldmVudC1idXMvY21rbXMtZ2EtY3Jvc3
 // MtYWNjb3VudC1zb3VyY2UtYnVzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMToxNDY2ODY5`"
        //     }
        //   }
        // ```

        // Construct an AwsCrypto object with the encryption algorithm `ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY` which
        // is used by EventBridge for encryption operation. This object is an entry point for decryption operation.
        // It can later use decryptData(MasterKeyProvider, byte[]) method to decrypt data.
        final AwsCrypto crypto = AwsCrypto.builder()
                .withEncryptionAlgorithm(CryptoAlgorithm.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
                .build();

        // Construct AWS KMS master key provider with AWS KMS Client Supplier and AWS KMS Key ARN. The KMS Client Supplier can
        // implement a RegionalClientSupplier interface. The AWS KMS Key ARN can be fetched from kms-key-arn property in
        // encrypted event json detail.
        final KmsMasterKeyProvider kmsMasterKeyProvider = KmsMasterKeyProvider.builder()
                .customRegionalClientSupplier(...)
                .buildStrict(KMS_KEY_ARN);

        // The string of encrypted-payload is base64 encoded. Decode it into byte array, so it can be furthur
        // decrypted. The encrypted payload can be fetched from encrypted-payload field in encrypted event json detail.
        byte[] encryptedByteArray = Base64.getDecoder().decode(ENCRYPTED_PAYLOAD);

        // The decryption operation. It retrieves the encryption context and encrypted data key from the cipher
        // text headers, which is parsed from byte array encrypted data. Then it decrypts the data key, and
        // uses it to finally decrypt event payload. This encryption/decryption strategy is called envelope
        // encryption, https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping
        final CryptoResult<byte[], KmsMasterKey> decryptResult = crypto.decryptData(kmsMasterKeyProvider, encryptedByteArray);

        final byte[] decryptedByteArray = decryptResult.getResult();

        // Decode the event json plaintext from byte array into string with UTF_8 standard.
        String eventJson = new String(decryptedByteArray, StandardCharsets.UTF_8);
````
