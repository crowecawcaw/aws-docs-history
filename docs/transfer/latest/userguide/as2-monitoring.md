

# Monitoring AS2 usage
<a name="as2-monitoring"></a>

You can monitor AS2 activity using Amazon CloudWatch and AWS CloudTrail. To view other Transfer Family server metrics, see [Amazon CloudWatch logging for AWS Transfer Family servers](structured-logging.md)


**AS2 metrics**  

| Metric | Description | 
| --- | --- | 
| InboundMessage | The total number of AS2 messages successfully received from a trading partner.<br />Units: Count<br />Period: 5 minutes | 
| InboundFailedMessage | The total number of AS2 messages that were unsuccessfully received from a trading partner. That is, a trading partner sent a message, but the Transfer Family server was not able to successfully process it.<br />Units: Count<br />Period: 5 minutes | 
| OutboundMessage | The total number of AS2 messages successfully sent from the Transfer Family server to a trading partner.<br />Units: Count<br />Period: 5 minute | 
| OutboundFailedMessage | The total number of AS2 messages that were unsuccessfully sent to a trading partner. That is, they were sent from the Transfer Family server, but were not successfully received by the trading partner.<br />Units: Count<br />Period: 5 minutes | 
| DaysUntilExpiry | The number of days until a Certificate expires determined by the `InactiveDate` set on the Certificate when importing.<br />Units: Count<br />Dimensions: `CertificateId`, `Description` (if provided)<br />Period: 1 day<br />For more information, see [AS2 certificate rotation](managing-as2-partners.md#as2-certificate-rotation). | 

## AS2 Status codes
<a name="as2-monitor-status-codes"></a>

The following table lists all of the status codes that can be logged to CloudWatch logs when you or your partner send an AS2 message. Different message processing steps apply to different message types and are intended for monitoring only. The COMPLETED and FAILED states represent the final step in processing, and are visible in JSON files.



| Code | Description | Processing completed? | 
| --- | --- | --- | 
| PROCESSING | The message is in the process of being converted to its final format. For example, decompression and decryption steps both have this status. | No | 
| MDN\_TRANSMIT | Message processing is sending an MDN response. | No | 
| MDN\_RECEIVE | Message processing is receiving an MDN response. | No | 
| COMPLETED | Message processing has completed successfully. This state includes when an MDN is sent for an inbound message or for MDN verification of outbound messages. | Yes | 
| FAILED | The message processing has failed. For a list of error codes, see [AS2 error codes](#as2-error-codes). | Yes | 

## AS2 error codes
<a name="as2-error-codes"></a>

The following table lists and describes error codes that you might receive from AS2 file transfers.


**AS2 error codes**  

| Code | Error | Description and resolution | 
| --- | --- | --- | 
| ACCESS\_DENIED |  +  Access denied. Check if your access role has necessary permissions. <br />+   Invalid file path {{send-file-path}} <br />+  Failed to get credentials with ErrorCode: {{error-code}}   | Occurs when handling a `StartFileTransfer` request where any of the `SendFilePaths` are not valid or malformed. That is, the path is missing the Amazon S3 bucket name, or the path includes characters that aren't valid. Also occurs if Transfer Family fails to assume the access role or logging role.<br />Ensure that the path contains a valid Amazon S3 bucket name and key name. | 
| AGREEMENT\_NOT\_FOUND | Agreement was not found. | Either the agreement was not found, or the agreement is associated with an inactive profile.<br />Update the agreement within the Transfer Family server to include active profiles. | 
| CONNECTOR\_NOT\_FOUND | Connector or related configuration was not found. | Either the connector was not found, or the connector is associated with an inactive profile.<br />Update the connector to include active profiles. | 
| CREDENTIALS\_RETRIEVAL\_FAILED |  1.  Secret not found in Secrets Manager. <br />2.  Cannot access Secrets Manager. <br />3.  Failed to decrypt secret in Secrets Manager. <br />4.  Cannot get secret value due to throttling.   | For AS2 Basic authentication, the secret must be formatted correctly. The following resolutions correspond to the errors listed in the previous column.1.  Ensure that the secret ID is correct. <br />2.  Ensure that the access role has the appropriate permissions to read the secret. The access role must provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, make sure that the role provides read and write access to the parent directory of the files that you intend to send with `StartFileTransfer`. <br />3.  If a customer managed key is being used for the secret, ensure that the access role has permissions for the AWS Key Management Service (AWS KMS) key. <br />4.  For the applicable quotas, see [Quotas for handling secrets](create-b2b-server.md#as2-quotas-secrets).  | 
| DECOMPRESSION\_FAILED | Failed to decompress message. | Either the file sent is corrupt, or the compression algorithm is not valid. <br />Resend the message and verify that ZLIB compression is used, or resend the message without compression enabled. | 
| DECRYPT\_FAILED | Failed to decrypt message {{message-ID}}. Ensure that the partner has the correct public encryption key. | Decryption failed.<br />Confirm that the partner sent a payload by using a valid certificate and that encryption was performed by using a valid encryption algorithm. | 
| DECRYPT\_FAILED\_INVALID\_SMIME\_FORMAT | Unable to parse enveloped mimePart. | MIME payload is either corrupt or in an unsupported SMIME format.<br />The sender should make sure that the format they're using is supported, and then resend the payload. | 
| DECRYPT\_FAILED\_NO\_DECRYPTION\_KEY\_FOUND | No matching decryption key found. | The partner profile did not have a certificate assigned that matched the message, or the certificates that matched the message are now expired or no longer valid.<br />You must update the partner profile and ensure that it contains a valid certificate. | 
| DECRYPT\_FAILED\_UNSUPPORTED\_ENCRYPTION\_ALG | SMIME Payload Decryption requested using unsupported algorithm with ID: {{encryption-ID}}. | The remote sender has sent an AS2 payload with an unsupported encryption algorithm.<br />The sender must choose an encryption algorithm that's supported by AWS Transfer Family. | 
| DUPLICATE\_MESSAGE | Duplicate or double processed step. | The payload has a duplicate processing step. For example, there are two encryption steps.<br />Resend the message with a single step for signing, compression, and encryption. | 
| ENCRYPT\_FAILED\_NO\_ENCRYPTION\_KEY\_FOUND | No valid public encryption certificates found in profile: {{local-profile-ID}} | Transfer Family is attempting to encrypt an outbound message, but no encryption certificates are found for the local profile.Resolution options:+  Ensure that the local profile has a certificate and private key for encryption attached. <br />+  Ensure that the encryption certificate is currently active.  | 
| ENCRYPTION\_FAILED | Failed to encrypt file {{file-name}}. | The file to be sent is not available for encryption.<br />Verify that the file is in its expected AS2 location and that AWS Transfer Family has permission to read the file. | 
| FILE\_SIZE\_TOO\_LARGE | File size is too large. | This occurs when sending or receiving a file that exceeds the file size limit. | 
| HTTP\_ERROR\_RESPONSE\_FROM\_PARTNER | {{partner-URL}} returned status 400 for message with ID={{message-ID}}. | Communicating with the partner's AS2 server returned an unexpected HTTP response code.<br />The partner might be able to provide more diagnostics from their AS2 server logs. | 
| INSUFFICENT\_MESSAGE\_SECURITY\_UNENCRYPTED | Encryption is required. | The partner sent an unencrypted message to Transfer Family, which is not supported. The sender must use an encrypted payload. | 
| INVALID\_ENDPOINT\_PROTOCOL | Only HTTP and HTTPS are supported. | You must specify HTTP or HTTPS as the protocol in your AS2 connector configuration. | 
| INVALID\_REQUEST |  1.  There is a problem with a message header. <br />2.  Could not parse secret JSON. <br />Secret JSON did not match expected format. <br />3.  Secret must be a JSON string. <br />4.  Username must not contain a colon. <br />Username must not contain control characters. <br />Username must contain only ASCII characters. <br />Password must not contain control characters. <br />Password must contain only ASCII characters.   | This error has several causes. The following resolutions correspond to the errors listed in the previous column.1.  Check the `as2-from` and `as2-to` fields. Make sure that the original message ID is accurate for the MDN format. Also make sure that the message ID format is not missing any AS2 headers. <br />2.  Ensure that the secret value matches the documented format, as described in [Enable Basic authentication for AS2 connectors](configure-as2-connector.md#as2-secret-create). <br />3.  Ensure that the secret is provided as a string, and not as a binary. <br />4.  Make the necessary correction to the username or password.  | 
| INVALID\_URL\_FORMAT | Invalid URL format: {{URL}} | This occurs when you are sending an outbound message using a connector configured with a malformed URL.<br />Ensure that the connector is configured with a valid HTTP or HTTPS URL. | 
| MDN\_RESPONSE\_INDICATES\_AUTHENTICATION\_FAILED | Not applicable | The receiver cannot authenticate the sender. The trading partner returns an MDN to Transfer Family with the [disposition modifier ](https://datatracker.ietf.org/doc/html/rfc4130#section-7.5.4) Error: authentication-failed. | 
| MDN\_RESPONSE\_INDICATES\_DECOMPRESSION\_FAILED | Not applicable | This occurs when the receiver cannot decompress the message contents. The trading partner returns an MDN to Transfer Family with the [disposition modifier ](https://datatracker.ietf.org/doc/html/rfc4130#section-7.5.4) Error: decompression-failed. | 
| MDN\_RESPONSE\_INDICATES\_DECRYPTION\_FAILED | Not applicable | The receiver cannot decrypt the message contents. The trading partner returns an MDN to Transfer Family with the [disposition modifier ](https://datatracker.ietf.org/doc/html/rfc4130#section-7.5.4) Error: authentication-failed. | 
| MDN\_RESPONSE\_INDICATES\_INSUFFICIENT\_MESSAGE\_SECURITY | Not applicable | The receiver expects the message to be signed or encrypted, but it isn’t. The trading partner returns an MDN to Transfer Family with the [disposition modifier ](https://datatracker.ietf.org/doc/html/rfc4130#section-7.5.4)Error: insufficient-message-security.Enable signing and/or encryption on the connector to match the trading partner's expectations. | 
| MDN\_RESPONSE\_INDICATES\_INTEGRITY\_CHECK\_FAILED | Not applicable | The receiver cannot verify content integrity. The trading partner returns an MDN to Transfer Family with the [disposition modifier ](https://datatracker.ietf.org/doc/html/rfc4130#section-7.5.4) Error: integrity-check-failed. | 
| PATH\_NOT\_FOUND | Unable to create directory {{file-path}}. The parent path could not be found. | Transfer Family is attempting to create a directory in the customer's Amazon S3 bucket, but the bucket is not found.Ensure that each path mentioned in the `StartFileTransfer` command contains the name of an existing bucket. | 
| SEND\_FILE\_NOT\_FOUND | File path {{file-path}} not found. | Transfer Family can't locate the file in the send file operation.<br />Check that the configured home directory and path are valid and that Transfer Family has read permissions for the file. | 
| SERVER\_NOT\_FOUND | Server associated with the message cannot be found. | Transfer Family could not find the server when receiving a message. This can happen if the server is deleted during the processing of an incoming message. | 
| SERVER\_NOT\_ONLINE | Server {{server-ID}} is not online. | The Transfer Family server is offline.Start the server so that it can receive and process messages. | 
| SIGNING\_FAILED | Failed to sign file. | The file to be sent is not available for signing, or signing could not be performed.<br />Verify that the file is in its expected AS2 location and that AWS Transfer Family has permission to read the file. | 
| SIGNING\_FAILED\_NO\_SIGNING\_KEY\_FOUND | No certificate found for profile: {{local-profile-ID}}. | Attempting to sign an outbound message, but no signing certificates are found for the local profile.Resolution options:+  Ensure that the local profile has a certificate and private key for signing attached. <br />+  Ensure that the signing certificate is currently active.  | 
| UNABLE\_RESOLVE\_HOST\_TO\_IP\_ADDRESS | Unable to resolve hostname to IP addresses. | Transfer Family is unable to perform DNS to IP address resolution on the public DNS server that is configured in the AS2 connector.<br />Update the connector to point to a valid partner URL. | 
| UNABLE\_TO\_CONNECT\_TO\_REMOTE\_HOST\_OR\_IP | Connection to endpoint timed out. | Transfer Family cannot establish a socket connection to the configured partner's AS2 server.<br />Check that the partner's AS2 server is available at the configured IP address. | 
| UNABLE\_TO\_RESOLVE\_HOSTNAME | Unable to resolve hostname {{hostname}}.  | The Transfer Family server could not resolve the partner's hostname by using a public DNS server.<br />Check that the configured host is registered and that the DNS record has had time to publish. | 
| VERIFICATION\_FAILED | Signature verification failed for AS2 message {{message-ID}} or a MIC code did not match. | Check that the sender's signing certificate matches the signing certificates for the remote profile. Also check that the MIC algorithms are compatible with AWS Transfer Family. | 
| VERIFICATION\_FAILED\_NO\_MATCHING\_KEY\_FOUND |  +  No public certificate matching message signature could be found in profile: {{partner-profile-ID}}. <br />+  Cannot get certificates for non-existent profile: {{partner-profile-ID}}. <br />+  No valid certificate was found in profile: {{partner-profile-ID}}.   | AWS Transfer Family is attempting to verify the signature for a received message, but no matching signing certificate is found for the partner profile. Resolution options:+  Ensure that the partner profile has a signing certificate attached. <br />+  Ensure that the certificate is currently active. <br />+  Ensure that the certificate is the correct signing certificate for the partner.  | 