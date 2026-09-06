

# Verify card data
<a name="verify-card-data"></a>

`Verify Card Data` is used to verify data that has been created using payment algorithms that rely on encryption principals such as `DISCOVER_DYNAMIC_CARD_VERIFICATION_CODE`. 

The input values are typically provided as part of an inbound transaction to an issuer or supporting platform partner. To verify an ARQC cryptogram (used for EMV chips cards), please see [Verify ARQC](data-operations.verifyauthrequestcryptogram.md). 

For more information, see [VerifyCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyCardValidationData.html) in the API guide.

If the value is verified, then the api will return http/200. If the value is not verified, it will return http/400.