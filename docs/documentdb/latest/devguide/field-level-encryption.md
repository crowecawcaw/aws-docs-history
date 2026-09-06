

# Client-side field level encryption
<a name="field-level-encryption"></a>

Amazon DocumentDB client-side field level encryption (FLE) allows you to encrypt sensitive data in your client applications before it is transferred to a Amazon DocumentDB cluster. Sensitive data remains encrypted when it is stored and processed in a cluster and is decrypted at the client application when retrieved.

**Topics**
+ [Getting started](#fle-getting-started)
+ [Querying in client-side FLE](#fle-querying)

## Getting started
<a name="fle-getting-started"></a>

The initial configuration of client-side FLE in Amazon DocumentDB is a four-step process that includes creating an encryption key, associating a role to the application, configuring the application, and defining CRUD operation with encryption options.

**Topics**
+ [Step 1: Create the encryption keys](#fle-step-create-key)
+ [Step 2: Associate a role with the application](#fle-step-associate-role)
+ [Step 3: Configure the application](#fle-step-config-app)
+ [Step 4: Define a CRUD operation](#fle-step-crud-ops)
+ [Example: client-side field level encryption configuration file](#fle-config-example)

### Step 1: Create the encryption keys
<a name="fle-step-create-key"></a>

Using AWS Key Management Service, create a symmetric customer managed key that encrypts and decrypts the sensitive data field, and grant it the necessary IAM usage permissions. AWS KMS stores the customer managed key, which is used to encrypt data keys. Storing the customer managed key in AWS KMS strengthens your security posture. The data key is the secondary key, which is stored in an Amazon DocumentDB collection and is required to encrypt sensitive fields before storing the document in Amazon DocumentDB. The customer managed key encrypts the data key, which in turn encrypts and decrypts your data. If you use a global cluster, you can create a multi-Region key that different service roles can use in different Regions.

For more information about the AWS Key Management Service, including how to create a key, see [AWS Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) in the *AWS Key Management Service Developer Guide*.

### Step 2: Associate a role with the application
<a name="fle-step-associate-role"></a>

Create an IAM policy with appropriate AWS KMS permissions. This policy allows the IAM identities to which it is attached to encrypt and decrypt the KMS key specified in the resource field. Your application assumes this IAM role to authenticate with AWS KMS.

The policy should look similar to this:

```
{ "Effect": "Allow",
"Action": ["kms:Decrypt", "kms:Encrypt"],
"Resource": "Customer Key ARN"
}
```

### Step 3: Configure the application
<a name="fle-step-config-app"></a>

You have defined a customer managed key in AWS KMS and created an IAM role with the necessary permissions to access it. Import the required packages.

```
import boto3
import json
import base64
from pymongo import MongoClient
from pymongo.encryption import (Algorithm,
                                ClientEncryption)
```

```
# create a session object: 
my_session = boto3.session.Session()

# get access_key and secret_key programmatically using get_frozen_credentials() method:
current_credentials = my_session.get_credentials().get_frozen_credentials()
```

1. Specify `aws` as the AWS KMS provider type and enter the account credentials that you retrieved in the previous step.

   ```
   provider = "aws"
   kms_providers = {
       provider: {
           "accessKeyId": current_credentials.access_key,
           "secretAccessKey": current_credentials.secret_key
       }
   }
   ```

1. Specify the customer managed key to encrypt the data key:

   ```
   customer_key = {
   “region”: “AWS region of the customer_key”,
       “key”: “customer_key ARN”
   }
   
   key_vault_namespace = "encryption.dataKeys"
   
   key_alt_name = 'TEST_DATA_KEY'
   ```

1. Configure the MongoClient object:

   ```
   client = MongoClient(connection_string)
   
   coll = client.test.coll
   coll.drop()
   
   client_encryption = ClientEncryption(
       kms_providers, # pass in the kms_providers variable from the previous step
       key_vault_namespace = key_vault_namespace,
       client,
       coll.codec_options
   )
   ```

1. Generate your data key:

   ```
   data_key_id = client_encryption.create_data_key(provider,
       customer_key,
       key_alt_name = [key_alt_name])
   ```

1. Retrieve your existing data key:

   ```
   data_key = DataKey("aws",
       master_key = customer_key)
   key_id = data_key["_id"]
   data_key_id = client[key_vault_namespace].find_one({"_id": key_id})
   ```

### Step 4: Define a CRUD operation
<a name="fle-step-crud-ops"></a>

Define the CRUD operation with encryption options.

1. Define the collection to write/read/delete a single document:

   ```
   coll = client.gameinfo.users
   ```

1. Explicit Encryption - encrypt fields and insert:
**Note**  
Exactly one of "key\_id" or "key\_alt\_name" must be provided.

   ```
   encrypted_first_name = client_encryption.encrypt(
       "Jane",
       Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
       key_id=data_key_id
   )
   encrypted_last_name = client_encryption.encrypt(
       "Doe",
       Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
       key_id=data_key_id
   )
   encrypted_dob = client_encryption.encrypt(
       "1990-01-01",
       Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Random,
       key_id=data_key_id
   )
   
   coll.insert_one(
       {"gamerTag": "jane_doe90",
       "firstName": encrypted_first_name,
       "lastName": encrypted_last_name,
       "dateOfBirth":encrypted_dob,
       "Favorite_games":["Halo","Age of Empires 2","Medal of Honor"]
   })
   ```

### Example: client-side field level encryption configuration file
<a name="fle-config-example"></a>

In the following example, replace each {{placeholder}} with your own information.

```
# import python packages:
import boto3
import json
import base64
from pymongo import MongoClient
from pymongo.encryption import (Algorithm,
                                ClientEncryption)

def main():
    
    # create a session object:
    my_session = boto3.session.Session()
    
    # get aws_region from session object:
    aws_region = my_session.region_name
    
    # get access_key and secret_key programmatically using get_frozen_credentials() method:
    current_credentials = my_session.get_credentials().get_frozen_credentials()
    provider = "aws"
    
    # define the kms_providers which is later used to create the Data Key:
    kms_providers = {
        provider: {
            "accessKeyId": current_credentials.access_key,
            "secretAccessKey": current_credentials.secret_key
        }
    }
    
    # enter the kms key ARN. Replace the example ARN value.
    kms_arn = "{{arn:aws:kms:us-east-1:123456789:key/abcd-efgh-ijkl-mnop}}"
    customer_key = {
        "region": aws_region,
        "key":kms_arn
    }

    # secrets manager is used to store and retrieve user credentials for connecting to an Amazon DocumentDB cluster. 
    # retrieve the secret using the secret name. Replace the example secret key.
    secret_name = "{{/dev/secretKey}}"
    docdb_credentials = json.loads(my_session.client(service_name = 'secretsmanager', region_name = "us-east-1").get_secret_value(SecretId = secret_name)['SecretString'])

    connection_params = '/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false'
    conn_str = 'mongodb://' + docdb_credentials["username"] + ':' + docdb_credentials["password"] + '@' + docdb_credentials["host"] + ':' + str(docdb_credentials["port"]) + connection_params
    client = MongoClient(conn_str) 

    coll = client.test.coll
    coll.drop()
    
    # store the encryption data keys in a key vault collection (having naming convention as db.collection):
    key_vault_namespace = "encryption.dataKeys"
    key_vault_db_name, key_vault_coll_name = key_vault_namespace.split(".", 1)

    # set up the key vault (key_vault_namespace) for this example:
    key_vault = client[key_vault_db_name][key_vault_coll_name]
    key_vault.drop()
    key_vault.create_index("keyAltNames", unique=True)

    client_encryption = ClientEncryption(
        kms_providers,
        key_vault_namespace,
        client,
        coll.codec_options)
    
    # create a new data key for the encrypted field:
    data_key_id = client_encryption.create_data_key(provider, master_key=customer_key, key_alt_names=["some_key_alt_name"], key_material = None)
    
    # explicitly encrypt a field:
    encrypted_first_name = client_encryption.encrypt(
    "Jane",
    Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
    key_id=data_key_id
    )
    coll.insert_one(
    {"gamerTag": "jane_doe90",
    "firstName": encrypted_first_name
    })
    doc = coll.find_one()
    print('Encrypted document: %s' % (doc,))
    
    # explicitly decrypt the field:
    doc["firstName"] = client_encryption.decrypt(doc["firstName"])
    print('Decrypted document: %s' % (doc,))
    
    # cleanup resources:
    client_encryption.close()
    client.close()
    
if __name__ == "__main__":
    main()
```

## Querying in client-side FLE
<a name="fle-querying"></a>

Amazon DocumentDB only supports equality queries with client-side FLE encrypted values.

For example, to query for documents where encrypted gamerscore equals 500 the client uses an explicit encryption method to encrypt the query value:

```
encrypted_gamerscore_filter = client_encryption.encrypt(
    500,
    Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
    key_id=data_key_id
)

coll.find( {
    "gamerscore" : { "$eq" : encrypted_gamerscore_filter }
} )
```