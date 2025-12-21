# Getting started with AWS Payment Cryptography

To get started with AWS Payment Cryptography, you'll first want to create keys and then use them in various cryptographic operations. The below tutorial provides a simple use case of generating a key to be used for
generating/verifying CVV2 values. To try out other examples and to explore deployment patterns within AWS, please try out the following [AWS Payment Cryptography Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/b85843d4-a5e4-40fc-9a96-de0a99312a4b/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/b85843d4-a5e4-40fc-9a96-de0a99312a4b/en-US")
or explore our sample project available on [GitHub](https://github.com/aws-samples/samples-for-payment-cryptography-service "https://github.com/aws-samples/samples-for-payment-cryptography-service")

This tutorial walks you through creating a single key and performing
cryptographic operations using the key. Afterward, you delete the key
if you no longer want it, which completes the key lifecycle.

###### Warning

Examples throughout this user guide may use sample values. We _strongly recommend_ not using sample values in a production environment such as key serial numbers.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Create a key](#getting-started-step1 "#getting-started-step1")
- [Step 2: Generate a CVV2 value using the key](#getting-started-step2 "#getting-started-step2")
- [Step 3: Verify the value generated in step 2](#getting-started-step3 "#getting-started-step3")
- [Step 4: Perform a negative test](#getting-started-step4 "#getting-started-step4")
- [Step 5: (Optional) Clean up](#getting-started-cleanup "#getting-started-cleanup")

## Prerequisites

Before you begin, make sure that:

- You have permission to access the service. For more information, see [IAM policies](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- You have the [AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") installed. You can also use [AWS SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") or [AWS APIs](../APIReference/Welcome.md "../APIReference/Welcome.md") to access AWS Payment Cryptography, but the instructions in this tutorial use the AWS CLI.

## Step 1: Create a key

The first step is to create a key. For this tutorial,
you create a [CVK](terminology.md#terms.cvk "terminology.md#terms.cvk") double-length 3DES (2KEY TDES) key for generating and verifying CVV/CVV2 values.

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY,KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,KeyModesOfUse='{Generate=true,Verify=true}'`
```

The response echoes back the request parameters, including an ARN for subsequent calls as well as a Key Check Value (KCV).

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyAttributes": {
 "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "TDES_2KEY",
 "KeyModesOfUse": {
 "Encrypt": false,
 "Decrypt": false,
 "Wrap": false,
 "Unwrap": false,
 "Generate": true,
 "Sign": false,
 "Verify": true,
 "DeriveKey": false,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "CADDA1",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2023-06-05T06:41:46.648000-07:00",
 "UsageStartTimestamp": "2023-06-05T06:41:46.626000-07:00"
 }
}`
```

Take note of the `KeyArn` that represents the key, for example _arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi_. You need that in the next step.

## Step 2: Generate a CVV2 value using the key

In this step, you generate a CVV2 for a given `PAN` and expiration date using the key from step 1.

```
`$`  `aws payment-cryptography-data generate-card-validation-data \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
 --primary-account-number=171234567890123 \
 --generation-attributes CardVerificationValue2={CardExpiryDate=0123}`
```

```
`{
 "CardDataGenerationKeyCheckValue": "CADDA1",
 "CardDataGenerationKeyIdentifier": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "CardDataType": "CARD_VERIFICATION_VALUE_2",
 "CardDataValue": "144"
}`
```

Take note of the `cardDataValue`, in this case the 3-digit number 144. You need that in the next step.

## Step 3: Verify the value generated in step 2

In this example, you validate the CVV2 from step 2 using the key you created in step 1.

Run the following command to validate the CVV2.

```
``$`  aws payment-cryptography-data verify-card-validation-data \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
 --primary-account-number=171234567890123 \
 --verification-attributes CardVerificationValue2={CardExpiryDate=0123} \
 --validation-data 144`
```

```
`{
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyCheckValue": "CADDA1"
}`
```

The service returns an HTTP response of 200 to indicate that it validated the CVV2.

## Step 4: Perform a negative test

In this step, you create a negative test where the CVV2 is not correct and does not validate. You attempt to validate an incorrect CVV2 using the key you created in step 1. This is an expected operation for example if a cardholder
entered the wrong CVV2 at checkout.

```
``$`  aws payment-cryptography-data verify-card-validation-data \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
 --primary-account-number=171234567890123 \
 --verification-attributes CardVerificationValue2={CardExpiryDate=0123} \
 --validation-data 999`
```

```
`Card validation data verification failed.`
```

The service returns an HTTP response of 400 with the message "Card validation data verification failed" and a reason of INVALID_VALIDATION_DATA.

## Step 5: (Optional) Clean up

Now you can delete the key you created in step 1. To minimize unrecoverable changes, the default key deletion period is seven days.

```
`$` `aws payment-cryptography delete-key \
 --key-identifier=arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi`
```

```
`{
 "Key": {
 "CreateTimestamp": "2022-10-27T08:27:51.795000-07:00",
 "DeletePendingTimestamp": "2022-11-03T13:37:12.114000-07:00",
 "Enabled": true,
 "Exportable": true,
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
 "KeyAttributes": {
 "KeyAlgorithm": "TDES_3KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyModesOfUse": {
 "Decrypt": true,
 "DeriveKey": false,
 "Encrypt": true,
 "Generate": false,
 "NoRestrictions": false,
 "Sign": false,
 "Unwrap": true,
 "Verify": false,
 "Wrap": true
 },
 "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY"
 },
 "KeyCheckValue": "CADDA1",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "KeyState": "DELETE_PENDING",
 "UsageStartTimestamp": "2022-10-27T08:27:51.753000-07:00"
 }
}`
```

Take note of two fields in the output. The `deletePendingTimestamp` is set to seven days in the future by default.
The keyState is set to `DELETE_PENDING`. You can cancel this deletion any time before the scheduled deletion time by calling [`restore-key`](../../../cli/latest/reference/payment-cryptography/restore-key.md "../../../cli/latest/reference/payment-cryptography/restore-key.md").
