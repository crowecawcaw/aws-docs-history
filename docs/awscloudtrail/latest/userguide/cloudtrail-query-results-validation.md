# Validate CloudTrail Lake saved query results

To determine whether the query results were modified, deleted, or unchanged after CloudTrail delivered
 the query results, you can use CloudTrail query results integrity validation. This feature is built using industry
 standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This
 makes it computationally infeasible to modify, delete or forge CloudTrail query result files without
 detection. You can use the command line to validate the query result files. 

## Why use it?


Validated query result files are invaluable in security and forensic investigations. For
 example, a validated query result file enables you to assert positively that the query result file itself
 has not changed. The CloudTrail query result file integrity validation process also lets you know if a query result file has been
 deleted or changed. 


###### Topics

* [Validate saved query results with the AWS CLI](#cloudtrail-query-results-validation-cli "#cloudtrail-query-results-validation-cli")
* [CloudTrail sign file structure](#cloudtrail-results-file-validation-sign-file-structure "#cloudtrail-results-file-validation-sign-file-structure")
* [Custom implementations of CloudTrail query result file integrity validation](#cloudtrail-results-file-custom-validation "#cloudtrail-results-file-custom-validation")

## Validate saved query results with the AWS CLI


You can validate the integrity of the query result files and sign file by using the [**aws cloudtrail verify-query-results**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/verify-query-results.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/verify-query-results.html") command.


### Prerequisites


To validate query results integrity with the command line, the following conditions must be
 met:



* You must have online connectivity to AWS.
* You must use AWS CLI version 2.
* To validate query result files and sign file locally, the following conditions
 apply:




	+ You must put the query result files and sign file in the specified file
	 path. Specify the file path as the value for the
	 **--local-export-path** parameter.
	+ You must not rename the query result files and sign file.
* To validate the query result files and sign file in the S3 bucket, the following
 conditions apply:




	+ You must not rename the query result files and sign file.
	+ You must have read access to the Amazon S3 bucket that contains the
	 query result files and sign file.
	+ The specified S3 prefix must contain the query result files and sign file. Specify the S3 prefix as the value for the
	 **--s3-prefix** parameter.

### verify-query-results


 The **verify-query-results** command verifies the hash value
 of each query result file by comparing the value with the `fileHashValue` in
 the sign file, and then validating the `hashSignature` in the sign file. 


When you verify query results, you can use either the **--s3-bucket**
 and **--s3-prefix** command line options to validate the query result files
 and sign file stored in an S3 bucket, or you can use the
 **--local-export-path** command line option to perform a local
 validation of the downloaded query result files and sign file.


###### Note

The **verify-query-results** command is Region specific. You must
 specify the **--region** global option to validate query results for
 a specific AWS Region.


The following are the options for the **verify-query-results**
 command.




**--s3-bucket**
`<string>`

Specifies the S3 bucket name that stores the query result files and sign file. You cannot use this parameter with **--local-export-path**.






**--s3-prefix**
`<string>`

Specifies the S3 path of the S3 folder that contains the query result files and sign file (for example, `s3/path/`). You cannot use this parameter with 
 **--local-export-path**. You do not need to provide this parameter if the files are located in the root directory of the S3 bucket.






**--local-export-path**
`<string>`

Specifies the local directory that contains the query result files and sign file (for example, `/local/path/to/export/file/`). You cannot use this parameter with 
 **--s3-bucket** or **--s3-prefix**.




#### Examples


The following example validates query results using the
 **--s3-bucket** and **--s3-prefix** command line
 options to specify the S3 bucket name and prefix containing the query result files and
 sign file.



```
aws cloudtrail verify-query-results --s3-bucket `amzn-s3-demo-bucket` --s3-prefix `prefix` --region `region`
```

The following example validates downloaded query results using the
 **--local-export-path** command line option to specify the local
 path for the query result files and sign file. For more information about downloading
 query result files, see [Download your CloudTrail Lake saved query results](view-download-cloudtrail-lake-query-results.md#cloudtrail-download-lake-query-results "view-download-cloudtrail-lake-query-results.md#cloudtrail-download-lake-query-results").



```
aws cloudtrail verify-query-results --local-export-path `local_file_path` --region `region`
```

#### Validation results


The following table describes the possible validation messages for query result files and sign file.




| File Type | Validation Message | Description |
| --- | --- | --- |
| `Sign file` | `Successfully validated sign and query result files` | The sign file signature is valid. The query result files it references can be checked. |
| `Query result file` | `ValidationError: "File `file_name` has inconsistent hash value with hash value recorded in sign file, hash value in sign file is `expected_hash`, but get `computed_hash`` | Validation failed because the hash value for the query result file did not match the `fileHashValue` in the sign file. |
| `Sign file` | `ValidationError: Invalid signature in sign file` | Validation for the sign file failed because the signature is not valid. | ## CloudTrail sign file structure The sign file contains the name of each query result file that was delivered to your Amazon S3 bucket when you saved the query results, the hash value for each query result file, and the digital signature of the file. The digital signature and hash values are used for validating the integrity of the query result files and of the sign file itself. ### Sign file location The sign file is delivered to an Amazon S3 bucket location that follows this syntax. ``` s3://`amzn-s3-demo-bucket`/`optional-prefix/`AWSLogs/`aws-account-ID`/CloudTrail-Lake/Query/`year`/`month`/`date`/`query-ID`/result_sign.json ``` ### Sample sign file contents The following example sign file contains information for CloudTrail Lake query results. ``` { "version": "1.0", "region": "us-east-1", "files": [ { "fileHashValue" : "de85a48b8a363033c891abd723181243620a3af3b6505f0a44db77e147e9c188", "fileName" : "result_1.csv.gz" } ], "hashAlgorithm" : "SHA-256", "signatureAlgorithm" : "SHA256withRSA", "queryCompleteTime": "2022-05-10T22:06:30Z", "hashSignature" : "7664652aaf1d5a17a12ba50abe6aca77c0ec76264bdf7dce71ac6d1c7781117c2a412e5820bccf473b1361306dff648feae20083ad3a27c6118172a81635829bdc7f7b795ebfabeb5259423b2fb2daa7d1d02f55791efa403dac553171e7ce5f9307d13e92eeec505da41685b4102c71ec5f1089168dacde702c8d39fed2f25e9216be5c49769b9db51037cb70a84b5712e1dffb005a74580c7fdcbb89a16b9b7674e327de4f5414701a772773a4c98eb008cca34228e294169901c735221e34cc643ead34628aabf1ba2c32e0cdf28ef403e8fe3772499ac61e21b70802dfddded9bea0ddfc3a021bf2a0b209f312ccee5a43f2b06aa35cac34638f7611e5d7", "publicKeyFingerprint" : "67b9fa73676d86966b449dd677850753" } ``` ### Sign file field descriptions The following are descriptions for each field in the sign file: `version` The version of the sign file. `region` The Region for the AWS account used for saving the query results. `files.fileHashValue` The hexadecimal encoded hash value of the compressed query result file content. `files.fileName` The name of the query result file. `hashAlgorithm` The hash algorithm used to hash the query result file. `signatureAlgorithm` The algorithm used to sign the file. `queryCompleteTime` Indicates when CloudTrail delivered the query results to the S3 bucket. You can use this value to find the public key. `hashSignature` The hash signature for the file. `publicKeyFingerprint` The hexadecimal encoded fingerprint of the public key used to sign the file. ## Custom implementations of CloudTrail query result file integrity validation Because CloudTrail uses industry standard, openly available cryptographic algorithms and hash functions, you can create your own tools to validate the integrity of the CloudTrail query result files. When you save query results to an Amazon S3 bucket, CloudTrail delivers a sign file to your S3 bucket. You can implement your own validation solution to validate the signature and query result files. For more information about the sign file, see [CloudTrail sign file structure](#cloudtrail-results-file-validation-sign-file-structure "#cloudtrail-results-file-validation-sign-file-structure"). This topic describes how the sign file is signed, and then details the steps that you will need to take to implement a solution that validates the sign file and the query result files that the sign file references. ### Understanding how CloudTrail sign files are signed CloudTrail sign files are signed with RSA digital signatures. For each sign file, CloudTrail does the following: 1. Creates a hash list containing the hash value for each query result file. 2. Gets a private key unique to the Region. 3. Passes the SHA-256 hash of the string and the private key to the RSA signing algorithm, which produces a digital signature. 4. Encodes the byte code of the signature into hexadecimal format. 5. Puts the digital signature into the sign file. #### Contents of the data signing string The data signing string consists of the hash value for each query result file separated by a space. The sign file lists the `fileHashValue` for each query result file. ### Custom validation implementation steps When implementing a custom validation solution, you will need to validate the sign file and the query result files that it references. #### Validate the sign file To validate a sign file, you need its signature, the public key whose private key was used to sign it, and a data signing string that you compute. 1. Get the sign file. 2. Verify that the sign file has been retrieved from its original location. 3. Get the hexadecimal-encoded signature of the sign file. 4. Get the hexadecimal-encoded fingerprint of the public key whose private key was used to sign the sign file. 5. Retrieve the public key for the time range corresponding to `queryCompleteTime` in the sign file. For the time range, choose a `StartTime` earlier than the `queryCompleteTime` and an `EndTime` later than the `queryCompleteTime`. 6. From among the public keys retrieved, choose the public key whose fingerprint matches the `publicKeyFingerprint` value in the sign file. 7. Using a hash list containing the hash value for each query result file separated by a space, recreate the data signing string used to verify the sign file signature. The sign file lists the `fileHashValue` for each query result file. For example, if your sign file's `files` array contains the following three query result files, your hash list is "aaa bbb ccc". ``` “files": [ { "fileHashValue" : “aaa”, "fileName" : "result_1.csv.gz" }, { "fileHashValue" : “bbb”, "fileName" : "result_2.csv.gz" }, { "fileHashValue" : “ccc”, "fileName" : "result_3.csv.gz" } ], ``` 8. Validate the signature by passing in the SHA-256 hash of the string, the public key, and the signature as parameters to the RSA signature verification algorithm. If the result is true, the sign file is valid. #### Validate the query result files If the sign file is valid, validate the query result files that the sign file references. To validate the integrity of a query result file, compute its SHA-256 hash value on its compressed content and compare the results with the `fileHashValue` for the query result file recorded in the sign file. If the hashes match, the query result file is valid. The following sections describe the validation process in detail. #### A. Get the sign file The first steps are to get the sign file and get the fingerprint of the public key. 1. Get the sign file from your Amazon S3 bucket for the query results that you want to validate. 2. Next, get the `hashSignature` value from the sign file. 3. In the sign file, get the fingerprint of the public key whose private key was used to sign the file from the `publicKeyFingerprint` field. #### B. Retrieve the public key for validating the sign file To get the public key to validate the sign file, you can use either the AWS CLI or the CloudTrail API. In both cases, you specify a time range (that is, a start time and end time) for the sign file that you want to validate. Use a time range corresponding to the `queryCompleteTime` in the sign file. One or more public keys may be returned for the time range that you specify. The returned keys may have validity time ranges that overlap. ###### Note Because CloudTrail uses different private/public key pairs per Region, each sign file is signed with a private key unique to its Region. Therefore, when you validate a sign file from a particular Region, you must retrieve its public key from the same Region. ##### Use the AWS CLI to retrieve public keys To retrieve a public key for a sign file by using the AWS CLI, use the `cloudtrail list-public-keys` command. The command has the following format: `aws cloudtrail list-public-keys [--start-time <start-time>] [--end-time <end-time>]` The start-time and end-time parameters are UTC timestamps and are optional. If not specified, the current time is used, and the currently active public key or keys are returned. **Sample Response** The response will be a list of JSON objects representing the key (or keys) returned: ##### Use the CloudTrail API to retrieve public keys To retrieve a public key for a sign file by using the CloudTrail API, pass in start time and end time values to the `ListPublicKeys` API. The `ListPublicKeys` API returns the public keys whose private keys were used to sign the file within the specified time range. For each public key, the API also returns the corresponding fingerprint. ##### `ListPublicKeys` This section describes the request parameters and response elements for the `ListPublicKeys` API. ###### Note The encoding for the binary fields for `ListPublicKeys` is subject to change. **Request Parameters**
| Name | Description | | --- | --- |
| `StartTime` | Optionally specifies, in UTC, the start of the time range to look up the public key for CloudTrail sign file. If StartTime is not specified, the current time is used, and the current public key is returned. Type: DateTime  | | `EndTime` | Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail sign files. If EndTime is not specified, the current time is used. Type: DateTime  | **Response Elements** `PublicKeyList`, an array of `PublicKey` objects that contains:
|  |  | | --- | --- |
| **Name** | **Description** | | `Value` | The DER encoded public key value in PKCS #1 format. Type: Blob  |
| `ValidityStartTime` | The starting time of validity of the public key. Type: DateTime  | | `ValidityEndTime` | The ending time of validity of the public key. Type: DateTime  |
| `Fingerprint` | The fingerprint of the public key. The fingerprint can be used to identify the public key that you must use to validate the sign file. Type: String  | #### C. Choose the public key to use for validation From among the public keys retrieved by `list-public-keys` or `ListPublicKeys`, choose the public key whose fingerprint matches the fingerprint recorded in the `publicKeyFingerprint` field of the sign file. This is the public key that you will use to validate the sign file. ####  D. Recreate the data signing string Now that you have the signature of the sign file and the associated public key, you need to calculate the data signing string. After you have calculated the data signing string, you will have the inputs needed to verify the signature. The data signing string consists of the hash value for each query result file separated by a space. After you recreate this string, you can validate the sign file. ####  E. Validate the sign file Pass the recreated data signing string, digital signature, and public key to the RSA signature verification algorithm. If the output is true, the signature of the sign file is verified and the sign file is valid. ####  F. Validate the query result files After you have validated the sign file, you can validate the query result files it references. The sign file contains the SHA-256 hashes of the query result files. If one of the query result files was modified after CloudTrail delivered it, the SHA-256 hashes will change, and the signature of the sign file will not match. Use the following procedure to validate the query result files listed in the sign file's `files` array. 1. Retrieve the original hash of the file from the `files.fileHashValue` field in the sign file. 2. Hash the compressed contents of the query result file with the hashing algorithm specified in `hashAlgorithm`. 3. Compare the hash value that you generated for each query result file with the `files.fileHashValue` in the sign file. If the hashes match, the query result files are valid. ### Validating signature and query result files offline When validating sign and query result files offline, you can generally follow the procedures described in the previous sections. However, you must take into account the following information about public keys. #### Public keys In order to validate offline, the public key that you need for validating query result files in a given time range must first be obtained online (by calling `ListPublicKeys`, for example) and then stored offline. This step must be repeated whenever you want to validate additional files outside the initial time range that you specified. ### Sample validation snippet The following sample snippet provides skeleton code for validating CloudTrail sign and query result files. The skeleton code is online/offline agnostic; that is, it is up to you to decide whether to implement it with or without online connectivity to AWS. The suggested implementation uses the [Java Cryptography Extension (JCE)](https://en.wikipedia.org/wiki/Java_Cryptography_Extension "https://en.wikipedia.org/wiki/Java_Cryptography_Extension") and [Bouncy Castle](https://www.bouncycastle.org/ "https://www.bouncycastle.org/") as a security provider. The sample snippet shows: <br>• How to create the data signing string used to validate the sign file signature. <br>• How to verify the sign file's signature. <br>• How to calculate the hash value for the query result file and compare it with the `fileHashValue` listed in the sign file to verify the authenticity of the query result file. ``` import org.apache.commons.codec.binary.Hex; import org.bouncycastle.asn1.pkcs.PKCSObjectIdentifiers; import org.bouncycastle.asn1.pkcs.RSAPublicKey; import org.bouncycastle.asn1.x509.AlgorithmIdentifier; import org.bouncycastle.asn1.x509.SubjectPublicKeyInfo; import org.bouncycastle.jce.provider.BouncyCastleProvider; import org.json.JSONArray; import org.json.JSONObject; import java.security.KeyFactory; import java.security.MessageDigest; import java.security.PublicKey; import java.security.Security; import java.security.Signature; import java.security.spec.X509EncodedKeySpec; import java.util.ArrayList; import java.util.Arrays; import java.util.List; import java.util.stream.Collectors; public class SignFileValidationSampleCode { public void validateSignFile(String s3Bucket, String s3PrefixPath) throws Exception { MessageDigest messageDigest = MessageDigest.getInstance("SHA-256"); // Load the sign file from S3 (using Amazon S3 Client) or from your local copy JSONObject signFile = loadSignFileToMemory(s3Bucket, String.format("%s/%s", s3PrefixPath, "result_sign.json")); // Using the Bouncy Castle provider as a JCE security provider - http://www.bouncycastle.org/ Security.addProvider(new BouncyCastleProvider()); List<String> hashList = new ArrayList<>(); JSONArray jsonArray = signFile.getJSONArray("files"); for (int i = 0; i < jsonArray.length(); i++) { JSONObject file = jsonArray.getJSONObject(i); String fileS3ObjectKey = String.format("%s/%s", s3PrefixPath, file.getString("fileName")); // Load the export file from S3 (using Amazon S3 Client) or from your local copy byte[] exportFileContent = loadCompressedExportFileInMemory(s3Bucket, fileS3ObjectKey); messageDigest.update(exportFileContent); byte[] exportFileHash = messageDigest.digest(); messageDigest.reset(); byte[] expectedHash = Hex.decodeHex(file.getString("fileHashValue")); boolean signaturesMatch = Arrays.equals(expectedHash, exportFileHash); if (!signaturesMatch) { System.err.println(String.format("Export file: %s/%s hash doesn't match.\tExpected: %s Actual: %s", s3Bucket, fileS3ObjectKey, Hex.encodeHexString(expectedHash), Hex.encodeHexString(exportFileHash))); } else { System.out.println(String.format("Export file: %s/%s hash match", s3Bucket, fileS3ObjectKey)); } hashList.add(file.getString("fileHashValue")); } String hashListString = hashList.stream().collect(Collectors.joining(" ")); /* NOTE: To find the right public key to verify the signature, call CloudTrail ListPublicKey API to get a list of public keys, then match by the publicKeyFingerprint in the sign file. Also, the public key bytes returned from ListPublicKey API are DER encoded in PKCS#1 format: PublicKeyInfo ::= SEQUENCE { algorithm       AlgorithmIdentifier, PublicKey       BIT STRING } AlgorithmIdentifier ::= SEQUENCE { algorithm       OBJECT IDENTIFIER, parameters      ANY DEFINED BY algorithm OPTIONAL } */ byte[] pkcs1PublicKeyBytes = getPublicKey(signFile.getString("queryCompleteTime"), signFile.getString("publicKeyFingerprint")); byte[] signatureContent = Hex.decodeHex(signFile.getString("hashSignature")); // Transform the PKCS#1 formatted public key to x.509 format. RSAPublicKey rsaPublicKey = RSAPublicKey.getInstance(pkcs1PublicKeyBytes); AlgorithmIdentifier rsaEncryption = new AlgorithmIdentifier(PKCSObjectIdentifiers.rsaEncryption, null); SubjectPublicKeyInfo publicKeyInfo = new SubjectPublicKeyInfo(rsaEncryption, rsaPublicKey); // Create the PublicKey object needed for the signature validation PublicKey publicKey = KeyFactory.getInstance("RSA", "BC") .generatePublic(new X509EncodedKeySpec(publicKeyInfo.getEncoded())); // Verify signature Signature signature = Signature.getInstance("SHA256withRSA", "BC"); signature.initVerify(publicKey); signature.update(hashListString.getBytes("UTF-8")); if (signature.verify(signatureContent)) { System.out.println("Sign file signature is valid."); } else { System.err.println("Sign file signature failed validation."); } System.out.println("Sign file validation completed."); } } ```
