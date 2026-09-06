

# Using IAM authentication and authorization for Amazon MQ for RabbitMQ
<a name="rabbitmq-iam-tutorial"></a>

The following procedure demonstrates how to enable AWS IAM authentication and authorization for an Amazon MQ for RabbitMQ broker. After enabling IAM, users can authenticate using AWS IAM credentials to access the RabbitMQ Management API and connect via AMQP. For details on how IAM authentication works with Amazon MQ for RabbitMQ, see [IAM authentication and authorization for Amazon MQ for RabbitMQ](iam-for-amq-for-rabbitmq.md).

## Prerequisites
<a name="iam-tutorial-prerequisites"></a>
+ AWS administrator credentials for the AWS account that owns the Amazon MQ for RabbitMQ broker
+ A shell environment configured with these administrator credentials (using AWS CLI profiles or environment variables)
+ AWS CLI installed and configured
+ `jq` command-line JSON processor installed
+ `curl` command-line tool installed

## Configuring IAM authentication and authorization using AWS CLI
<a name="iam-tutorial-procedure"></a>

1. **Set environment variables**

   Set the required environment variables for your broker:

   ```
   export AWS_DEFAULT_REGION={{<region>}}
   export BROKER_ID={{<broker-id>}}
   ```

1. **Enable outbound JWT tokens**

   Enable outbound web identity federation for your AWS account:

   ```
   ISSUER_IDENTIFIER=$(aws iam enable-outbound-web-identity-federation --query 'IssuerIdentifier' --output text)
   echo $ISSUER_IDENTIFIER
   ```

   The output displays a unique issuer identifier URL for your account in the format `https://<id>.tokens.sts.global.api.aws`.

1. **Create the IAM policy document**

   Create a policy document that grants permissions to obtain web identity tokens:

   ```
   cat > policy.json << 'EOF'
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "VisualEditor0",
               "Effect": "Allow",
               "Action": [
                   "sts:GetWebIdentityToken",
                   "sts:TagGetWebIdentityToken"
               ],
               "Resource": "*"
           }
       ]
   }
   EOF
   ```

1. **Create the trust policy**

   Retrieve your caller identity and create a trust policy document:

   ```
   CALLER_ARN=$(aws sts get-caller-identity --query Arn --output text)
   cat > trust-policy.json << EOF
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": "$CALLER_ARN"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   EOF
   ```

1. **Create the IAM role**

   Create the IAM role and attach the policy:

   ```
   aws iam create-role --role-name RabbitMqAdminRole --assume-role-policy-document file://trust-policy.json
   aws iam put-role-policy --role-name RabbitMqAdminRole --policy-name RabbitMqAdminRolePolicy --policy-document file://policy.json
   ```

1. **Configure RabbitMQ OAuth2 settings**

   Create a RabbitMQ configuration file with OAuth2 authentication and authorization settings:

   ```
   cat > rabbitmq.conf << EOF
   auth_backends.1 = oauth2
   auth_backends.2 = internal
   
   auth_oauth2.jwks_uri = ${ISSUER_IDENTIFIER}/.well-known/jwks.json
   auth_oauth2.resource_server_id = rabbitmq
   auth_oauth2.scope_prefix = rabbitmq/
   
   auth_oauth2.additional_scopes_key = sub
   auth_oauth2.scope_aliases.1.alias = arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/RabbitMqAdminRole
   auth_oauth2.scope_aliases.1.scope = rabbitmq/tag:administrator rabbitmq/read:*/* rabbitmq/write:*/* rabbitmq/configure:*/*
   auth_oauth2.https.hostname_verification = wildcard
   
   management.oauth_enabled = true
   EOF
   ```

1. **Update the broker configuration**

   Apply the new configuration to your broker:

   ```
   # Retrieve the configuration ID
   CONFIG_ID=$(aws mq describe-broker --broker-id $BROKER_ID --query 'Configurations[0].Id' --output text)
   
   # Create a new configuration revision
   REVISION=$(aws mq update-configuration --configuration-id $CONFIG_ID --data "$(cat rabbitmq.conf | base64 --wrap=0)" --query 'LatestRevision.Revision' --output text)
   
   # Apply the configuration to the broker
   aws mq update-broker --broker-id $BROKER_ID --configuration Id=$CONFIG_ID,Revision=$REVISION
   
   # Reboot the broker to apply changes
   aws mq reboot-broker --broker-id $BROKER_ID
   ```

   Wait for the broker status to return to `RUNNING` before proceeding to the next step.

1. **Obtain a JWT token**

   Assume the IAM role and obtain a web identity token:

   ```
   # Assume the RabbitMqAdminRole
   ROLE_CREDS=$(aws sts assume-role --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/RabbitMqAdminRole --role-session-name rabbitmq-session)
   
   # Configure the session with temporary credentials
   export AWS_ACCESS_KEY_ID=$(echo "$ROLE_CREDS" | jq -r '.Credentials.AccessKeyId')
   export AWS_SECRET_ACCESS_KEY=$(echo "$ROLE_CREDS" | jq -r '.Credentials.SecretAccessKey')
   export AWS_SESSION_TOKEN=$(echo "$ROLE_CREDS" | jq -r '.Credentials.SessionToken')
   
   # Obtain the web identity token
   TOKEN_RESPONSE=$(aws sts get-web-identity-token \
       --audience "rabbitmq" \
       --signing-algorithm ES384 \
       --duration-seconds 300 \
       --tags Key=scope,Value="rabbitmq/tag:administrator")
   
   # Extract the token
   TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.WebIdentityToken')
   ```

1. **Access the RabbitMQ Management API**

   Use the JWT token to access the RabbitMQ Management API:

   ```
   BROKER_URL={{<broker-id>}}.mq.{{<region>}}.on.aws
   
   curl -u ":$TOKEN" \
       -X GET https://${BROKER_URL}/api/overview \
       -H "Content-Type: application/json"
   ```

   A successful response confirms that IAM authentication is working correctly. The response contains broker overview information in JSON format.

1. **Connect via AMQP using the JWT token**

   Test AMQP connectivity using the JWT token with the perf-test tool:

   ```
   BROKER_DNS={{<broker-endpoint>}}
   CONNECTION_STRING=amqps://:${TOKEN}@${BROKER_DNS}:5671
   
   docker run -it --rm --ulimit nofile=40960:40960 pivotalrabbitmq/perf-test:latest \
       --queue-pattern 'test-queue-%d' --queue-pattern-from 1 --queue-pattern-to 1 \
       --producers 1 --consumers 1 \
       --uri ${CONNECTION_STRING} \
       --flag persistent --rate 1
   ```

   If you receive an `ACCESS_REFUSED` error, you can troubleshoot your configuration settings by using the CloudWatch logs for your broker. You can find the link for the CloudWatch Logs log group for your broker in the Amazon MQ console.