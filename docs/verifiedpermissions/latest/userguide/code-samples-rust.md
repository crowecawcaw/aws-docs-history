# Implementing Amazon Verified Permissions in Rust with the AWS

SDK

This topic provides a practical example of implementing Amazon Verified Permissions in Rust with the AWS
SDK. This example shows how to develop an authorization model that can test whether a user
is able to view a photo. The sample code uses the [aws-sdk-verifiedpermissions](https://docs.rs/aws-sdk-verifiedpermissions/latest/aws_sdk_verifiedpermissions/ "https://docs.rs/aws-sdk-verifiedpermissions/latest/aws_sdk_verifiedpermissions/") crate from the [AWS SDK for Rust](https://github.com/awslabs/aws-sdk-rust "https://github.com/awslabs/aws-sdk-rust"), which offers a
robust set of tools for interacting with AWS services.

## Prerequisites

Before starting, ensure that you have the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") configured on your system and that you're familiar with
Rust.

- For instructions on installing the AWS CLI, see [AWS CLI
  installation guide](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- For instructions on configuring the AWS CLI, see [Configuring
  settings for the AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") and [Configuration and
  credential file settings in the AWS CLI](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md").
- For more information on Rust, see [rust-lang.org](https://www.rust-lang.org/ "https://www.rust-lang.org/") and the [AWS SDK for Rust Developer
  Guide](../../../sdk-for-rust/latest/dg/welcome.md "../../../sdk-for-rust/latest/dg/welcome.md").

With your environment prepared, let's explore how to implement Verified Permissions in Rust.

## Test the sample code

The sample code does the following:

- Sets up the SDK client to communicate with AWS
- Creates a [policy store](policy-stores.md "policy-stores.md")
- Defines the structure of the policy store by adding a [schema](schema.md "schema.md")
- Adds a [policy](policies.md "policies.md") to check authorization
  requests
- Sends a test [authorization request](authorization.md "authorization.md") to
  verify everything is set up correctly

###### To test the sample code

1. Create a Rust project.
2. Replace any existing code in
   `main.rs` with the following code:

```
use std::time::Duration;
use std::thread::sleep;
use aws_config::BehaviorVersion;
use aws_sdk_verifiedpermissions::Client;
use aws_sdk_verifiedpermissions::{
    operation::{
        create_policy::CreatePolicyOutput,
        create_policy_store::CreatePolicyStoreOutput,
        is_authorized::IsAuthorizedOutput,
        put_schema::PutSchemaOutput,
    },
    types::{
        ActionIdentifier, EntityIdentifier, PolicyDefinition, SchemaDefinition, StaticPolicyDefinition, ValidationSettings
    },
};

//Function that creates a policy store in the client that's passed
async fn create_policy_store(client: &Client, valid_settings: &ValidationSettings)-> CreatePolicyStoreOutput {
    let policy_store = client.create_policy_store().validation_settings(valid_settings.clone()).send().await;
    return policy_store.unwrap();
}

//Function that adds a schema to the policy store in the client
async fn put_schema(client: &Client, ps_id: &str, schema: &str) -> PutSchemaOutput {
    let schema = client.put_schema().definition(SchemaDefinition::CedarJson(schema.to_string())).policy_store_id(ps_id.to_string()).send().await;
    return schema.unwrap();
}

//Function that creates a policy in the policy store in the client
async fn create_policy(client: &Client, ps_id: &str, policy_definition:&PolicyDefinition) -> CreatePolicyOutput {
    let create_policy = client.create_policy().definition(policy_definition.clone()).policy_store_id(ps_id).send().await;
    return create_policy.unwrap();
}

//Function that tests the authorization request to the policy store in the client
async fn authorize(client: &Client, ps_id: &str, principal: &EntityIdentifier, action: &ActionIdentifier, resource: &EntityIdentifier) -> IsAuthorizedOutput {
    let is_auth = client.is_authorized().principal(principal.to_owned()).action(action.to_owned()).resource(resource.to_owned()).policy_store_id(ps_id).send().await;
    return is_auth.unwrap();
}

#[::tokio::main]
async fn main() -> Result<(), aws_sdk_verifiedpermissions::Error> {

//Set up SDK client
    let config = aws_config::load_defaults(BehaviorVersion::latest()).await;
    let client = aws_sdk_verifiedpermissions::Client::new(&config);

//Create a policy store
    let valid_settings = ValidationSettings::builder()
    .mode({aws_sdk_verifiedpermissions::types::ValidationMode::Strict
    })
    .build()
    .unwrap();
    let policy_store = create_policy_store(&client, &valid_settings).await;
    println!(
    "Created Policy store with ID: {:?}",
    policy_store.policy_store_id
    );

//Add schema to policy store
    let schema= r#"{
        "PhotoFlash": {
            "actions": {
                "ViewPhoto": {
                    "appliesTo": {
                        "context": {
                            "type": "Record",
                            "attributes": {}
                        },
                        "principalTypes": [
                            "User"
                        ],
                        "resourceTypes": [
                            "Photo"
                        ]
                    },
                    "memberOf": []
                }
            },
            "entityTypes": {
                "Photo": {
                    "memberOfTypes": [],
                    "shape": {
                        "type": "Record",
                        "attributes": {
                            "IsPrivate": {
                                "type": "Boolean"
                            }
                        }
                    }
                },
                "User": {
                    "memberOfTypes": [],
                    "shape": {
                        "attributes": {},
                        "type": "Record"
                    }
                }
            }
        }
    }"#;
    let put_schema = put_schema(&client, &policy_store.policy_store_id, schema).await;
    println!(
        "Created Schema with Namespace: {:?}",
        put_schema.namespaces
    );

//Create policy
    let policy_text = r#"
        permit (
            principal in PhotoFlash::User::"alice",
            action == PhotoFlash::Action::"ViewPhoto",
            resource == PhotoFlash::Photo::"VacationPhoto94.jpg"
        );
        "#;
    let policy_definition = PolicyDefinition::Static(StaticPolicyDefinition::builder().statement(policy_text).build().unwrap());
    let policy = create_policy(&client, &policy_store.policy_store_id, &policy_definition).await;
    println!(
        "Created Policy with ID: {:?}",
        policy.policy_id
    );

//Break to make sure the resources are created before testing authorization
    sleep(Duration::new(2, 0));

//Test authorization
    let principal= EntityIdentifier::builder().entity_id("alice").entity_type("PhotoFlash::User").build().unwrap();
    let action = ActionIdentifier::builder().action_type("PhotoFlash::Action").action_id("ViewPhoto").build().unwrap();
    let resource = EntityIdentifier::builder().entity_id("VacationPhoto94.jpg").entity_type("PhotoFlash::Photo").build().unwrap();
    let auth = authorize(&client, &policy_store.policy_store_id, &principal, &action, &resource).await;
    println!(
        "Decision: {:?}",
        auth.decision
        );
        println!(
        "Policy ID: {:?}",
        auth.determining_policies
        );
     Ok(())
}
```

3. Run the code by entering
   `cargo run` in the terminal.

If the code runs correctly, the terminal will show `Decision: Allow`
followed by the policy ID of the determining policy. This means you've successfully
created a policy store and tested it using the AWS SDK for Rust.

## Clean up resources

After you have finished exploring your policy store, delete it.

###### To delete a policy store

You can delete a policy store by using the `delete-policy-store`
operation, replacing `PSEXAMPLEabcdefg111111` with the policy store ID you want to delete.

```
`$` `aws verifiedpermissions delete-policy-store \
 --policy-store-id `PSEXAMPLEabcdefg111111``
```

If successful, this command produces no output.
