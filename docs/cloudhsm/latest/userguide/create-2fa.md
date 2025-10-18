# Create users with 2FA enabled for AWS CloudHSM Management Utility users

Use AWS CloudHSM Management Utility CMU (CMU) and the key pair to create a new crypto office (CO) user with two-factor authentication (2FA) enabled.

###### To create CO users with 2FA enabled

1. In one terminal, perform the following steps:


	1. Access your HSM and log in to the CloudHSM Management utility:
	
	
	
	```
	`/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`
	```
	2. Log in as a CO and use the following command to create a new user MFA with 2FA:
	
	
	
	```
	`aws-cloudhsm >` `createUser CO MFA `<CO USER NAME>` -2fa /home/ec2-user/authdata``*************************CAUTION********************************
	This is a CRITICAL operation, should be done on all nodes in the
	cluster. AWS does NOT synchronize these changes automatically with the 
	nodes on which this operation is not executed or failed, please 
	ensure this operation is executed on all nodes in the cluster. 
	****************************************************************
	
	Do you want to continue(y/n)? `y`
	
	Creating User exampleuser3(CO) on 1 nodesAuthentication data written to: "/home/ec2-user/authdata"Generate Base64-encoded signatures for SHA256 digests in the authentication datafile. 
	To generate the signatures, use the RSA private key, which is the second factor ofauthentication for this user. Paste the signatures and the corresponding public keyinto the authentication data file and provide 
	the file path below.Leave this field blank to use the path initially provided.Enter filename:`
	```
	3. Leave the above terminal in this state. Do not press enter or enter any filename.
2. In another terminal, perform the following steps:


	1. Access your HSM and log in to the CloudHSM Management utility:
	
	
	
	```
	`/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`
	```
	2. Generate a public-private key-pair using the following commands:
	
	
	
	```
	`openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048`
	```
	
	
	```
	`openssl rsa -pubout -in private_key.pem -out public_key.pem`
	```
	3. Run the following command to install a json querying feature for extracting the Digest from authdata file:
	
	
	
	```
	`sudo yum install jq`
	```
	4. To extract the digest value, first find the following data in the authdata file:
	
	
	
	```
	`{
	 "Version":"1.0",
	 "PublicKey":"",
	 "Data":[
	 {
	 "HsmId": `<"HSM ID">`,
	 "Digest": `<"DIGEST">`,
	 "Signature": ""
	 }
	 ]
	}`
	```
	
	###### Note
	
	The obtained Digest is base64 encoded, however to sign the digest, you need the file to be decoded first and then signed. The following command will decode the digest and store the decoded content in ‘digest1.bin’
	
	
	```
	cat authdata | jq '.Data[0].Digest' | cut -c2- | rev | cut -c2- | rev | base64 -d > digest1.bin
	```
	5. Convert the public key content, adding "\n" and removing spaces as shown here:
	
	
	
	```
	-----BEGIN PUBLIC KEY-----\n`<PUBLIC KEY>`\n-----END PUBLIC KEY----- 
	```
	
	###### Important
	
	The above command shows how "\n" is added immediately after **BEGIN PUBLIC KEY-----**, spaces between "\n" and the first character of the public key are removed,
	 "\n" is added before **-----END PUBLIC KEY**, and spaces are removed between "\n" and the end of the public key.
	
	
	This is the PEM format for public key which is accepted in the authdata file.
	6. Paste the public key pem format content in the public key section in the authdata file.
	
	
	
	```
	vi authdata
	```
	
	
	```
	{
	  "Version":"1.0",
	  "PublicKey":"-----BEGIN PUBLIC KEY-----\n`<"PUBLIC KEY">`\n-----END PUBLIC KEY-----",
	  "Data":[    
	    {      
	      "HsmId":`<"HSM ID">`,
	      "Digest":`<"DIGEST">`,      
	      "Signature": ""   
	    }  
	  ]
	}
	```
	7. Sign the token file using the following command:
	
	
	
	```
	`openssl pkeyutl -sign -in digest1.bin -inkey private_key.pem -pkeyopt digest:sha256 | base64``Output Expected:
	`<"THE SIGNATURE">``
	```
	
	###### Note
	
	As shown in the above command, use **openssl pkeyutl** instead of **openssl dgst** for signing.
	8. Add the signed digest in the Authdata File in "Signature" field.
	
	
	
	```
	vi authdata
	```
	
	
	```
	{
	    "Version": "1.0",
	    "PublicKey": "-----BEGIN PUBLIC KEY----- ... -----END PUBLIC KEY-----",
	    "Data": [
	        {
	            "HsmId": `<"HSM ID">`,
	            "Digest": `<"DIGEST">`,
	            "Signature": `<"Kkdl ... rkrvJ6Q==">`
	        },
	        {
	            "HsmId": `<"HSM ID">`,
	            "Digest": `<"DIGEST">`,
	            "Signature": `<"K1hxy ... Q261Q==">`
	        }
	    ]
	}
	```
3. Go back to the first terminal and press `Enter`:



```
`Generate Base64-encoded signatures for SHA256 digests in the authentication datafile. To generate the signatures, use the RSA private key, 
which is the second factor ofauthentication for this user. Paste the signatures and the corresponding public keyinto the authentication data file and provide the file path below. Leave this field blank to use the path initially provided. 
Enter filename: >>>>> Press Enter here

createUser success on server 0(10.0.1.11)`
```
