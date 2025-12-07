# Getting started with AgentCore Policy

In this tutorial, you'll learn how to set up a Amazon Bedrock AgentCore Policy and integrate it with a
Amazon Bedrock AgentCore Gateway using the AgentCore starter toolkit. You'll create a refund processing tool
with Cedar policies that enforce business rules for refund amounts.

###### Topics

- [Prerequisites](#policy-getting-started-prerequisites "#policy-getting-started-prerequisites")
- [Step 1: Setup and install](#policy-getting-started-setup "#policy-getting-started-setup")
- [Step 2: Create policy setup
  script](#policy-getting-started-create-script "#policy-getting-started-create-script")
- [Step 3: Run the setup](#policy-getting-started-run-setup "#policy-getting-started-run-setup")
- [Step 4: Test the policy](#policy-getting-started-test "#policy-getting-started-test")
- [What you've built](#policy-getting-started-results "#policy-getting-started-results")
- [Troubleshooting](#policy-getting-started-troubleshooting "#policy-getting-started-troubleshooting")
- [Clean up](#policy-getting-started-cleanup "#policy-getting-started-cleanup")

## Prerequisites

Before starting, make sure you have the following:

- **AWS Account** with credentials
  configured
- **Python 3.10+** installed
- **IAM permissions** for creating roles, Lambda
  functions, policy engines, and using Amazon Bedrock AgentCore

## Step 1: Setup and install

Run the following in a terminal to set up the virtual environment:

```

mkdir agentcore-policy-quickstart
cd agentcore-policy-quickstart
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

Then install the dependencies:

```

pip install boto3
pip install bedrock-agentcore-starter-toolkit
pip install requests

```

## Step 2: Create policy setup

script

Create a new file called `setup_policy.py` and insert the following
code:

```

"""
Setup script to create Gateway with Policy Engine
Run this first: python setup_policy.py
"""

from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
from bedrock_agentcore_starter_toolkit.operations.policy.client import PolicyClient
from bedrock_agentcore_starter_toolkit.utils.lambda_utils import create_lambda_function
import boto3
import json
import logging
import time


def setup_policy():
    # Configuration
    region = "us-west-2"
    refund_limit = 1000

    print("🚀 Setting up AgentCore Gateway with Policy Engine...")
    print(f"Region: {region}\n")

    # Initialize clients
    gateway_client = GatewayClient(region_name=region)
    gateway_client.logger.setLevel(logging.INFO)

    policy_client = PolicyClient(region_name=region)
    policy_client.logger.setLevel(logging.INFO)

    # Step 1: Create OAuth authorizer
    print("Step 1: Creating OAuth authorization server...")
    cognito_response = gateway_client.create_oauth_authorizer_with_cognito("PolicyGateway")
    print("✓ Authorization server created\n")

    # Step 2: Create Gateway
    print("Step 2: Creating Gateway...")
    gateway = gateway_client.create_mcp_gateway(
        name=None,
        role_arn=None,
        authorizer_config=cognito_response["authorizer_config"],
        enable_semantic_search=False,
    )
    print(f"✓ Gateway created: {gateway['gatewayUrl']}\n")

    # Fix IAM permissions
    gateway_client.fix_iam_permissions(gateway)
    print("⏳ Waiting 30s for IAM propagation...")
    time.sleep(30)
    print("✓ IAM permissions configured\n")

    # Step 3: Create Lambda function with refund tool
    print("Step 3: Creating Lambda function with refund tool...")

    refund_lambda_code = """
def lambda_handler(event, context):
    amount = event.get('amount', 0)
    return {
        "status": "success",
        "message": f"Refund of ${amount} processed successfully",
        "amount": amount
    }
"""

    session = boto3.Session(region_name=region)
    lambda_arn = create_lambda_function(
        session=session,
        logger=gateway_client.logger,
        function_name=f"RefundTool-{int(time.time())}",
        lambda_code=refund_lambda_code,
        runtime="python3.13",
        handler="lambda_function.lambda_handler",
        gateway_role_arn=gateway["roleArn"],
        description="Refund tool for policy demo",
    )
    print("✓ Lambda function created\n")

    # Step 4: Add Lambda target with refund tool schema
    print("Step 4: Adding Lambda target with refund tool schema...")
    lambda_target = gateway_client.create_mcp_gateway_target(
        gateway=gateway,
        name="RefundTarget",
        target_type="lambda",
        target_payload={
            "lambdaArn": lambda_arn,
            "toolSchema": {
                "inlinePayload": [
                    {
                        "name": "process_refund",
                        "description": "Process a customer refund",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "amount": {
                                    "type": "integer",
                                    "description": "Refund amount in dollars"
                                }
                            },
                            "required": ["amount"],
                        },
                    }
                ]
            },
        },
        credentials=None,
    )
    print("✓ Lambda target added\n")

    # Step 5: Create Policy Engine
    print("Step 5: Creating Policy Engine...")
    engine = policy_client.create_or_get_policy_engine(
        name="RefundPolicyEngine",
        description="Policy engine for refund governance"
    )
    print(f"✓ Policy Engine: {engine['policyEngineId']}\n")

    # Step 6: Create Cedar policy
    print(f"Step 6: Creating Cedar policy (refund limit: ${refund_limit})...")
    cedar_statement = (
        f"permit(principal, "
        f'action == AgentCore::Action::"RefundTarget___process_refund", '
        f'resource == AgentCore::Gateway::"{gateway["gatewayArn"]}") '
        f"when {{ context.input.amount < {refund_limit} }};"
    )

    policy = policy_client.create_or_get_policy(
        policy_engine_id=engine["policyEngineId"],
        name="refund_limit_policy",
        description=f"Allow refunds under ${refund_limit}",
        definition={"cedar": {"statement": cedar_statement}},
    )
    print(f"✓ Policy: {policy['policyId']}\n")

    # Step 7: Attach Policy Engine to Gateway
    print("Step 7: Attaching Policy Engine to Gateway (ENFORCE mode)...")
    gateway_client.update_gateway_policy_engine(
        gateway_identifier=gateway["gatewayId"],
        policy_engine_arn=engine["policyEngineArn"],
        mode="ENFORCE"
    )
    print("✓ Policy Engine attached to Gateway\n")

    # Step 8: Save configuration
    config = {
        "gateway_url": gateway["gatewayUrl"],
        "gateway_id": gateway["gatewayId"],
        "gateway_arn": gateway["gatewayArn"],
        "policy_engine_id": engine["policyEngineId"],
        "policy_engine_arn": engine["policyEngineArn"],
        "policy_id": policy["policyId"],
        "region": region,
        "client_info": cognito_response["client_info"],
        "refund_limit": refund_limit
    }

    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

    print("=" * 60)
    print("✅ Setup complete!")
    print(f"Gateway URL: {gateway['gatewayUrl']}")
    print(f"Policy Engine ID: {engine['policyEngineId']}")
    print(f"Refund limit: ${refund_limit}")
    print("\nConfiguration saved to: config.json")
    print("\nNext step: Run 'python test_policy.py' to test your Policy")
    print("=" * 60)

    return config


if __name__ == "__main__":
    setup_policy()

```

### Understanding the setup

script

The setup script performs several key operations to create a complete
policy-enabled gateway. Here's a detailed explanation of each component.

###### Topics

- [Import required libraries](#policy-import-libraries "#policy-import-libraries")
- [Initialize clients](#policy-initialize-clients "#policy-initialize-clients")
- [Create an OAuth Authorization
  Server](#policy-oauth-server "#policy-oauth-server")
- [Create a Gateway](#policy-create-gateway "#policy-create-gateway")
- [Add Lambda Target](#policy-add-lambda-target "#policy-add-lambda-target")
- [Create a Policy Engine](#policy-create-policy-engine "#policy-create-policy-engine")
- [Create Cedar Policy](#policy-create-cedar-policy "#policy-create-cedar-policy")
- [Attach Policy to Gateway](#policy-attach-to-gateway "#policy-attach-to-gateway")

#### Import required libraries

```

from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
from bedrock_agentcore_starter_toolkit.operations.policy.client import PolicyClient
from bedrock_agentcore_starter_toolkit.utils.lambda_utils import create_lambda_function
import boto3
import json
import logging
import time

```

#### Initialize clients

```

gateway_client = GatewayClient(region_name=region)
policy_client = PolicyClient(region_name=region)

```

#### Create an OAuth Authorization

Server

Gateways are secured by OAuth authorization servers. This creates an Amazon Cognito
user pool with OAuth 2.0 configured.

#### Create a Gateway

The gateway acts as your MCP server endpoint that agents connect to. It
manages OAuth authorization and enables semantic search for tool
discovery.

#### Add Lambda Target

Creates a Lambda function with a refund tool that processes refund
requests.

#### Create a Policy Engine

A policy engine is a collection of Cedar policies that evaluates and
authorizes agent tool calls. The policy engine intercepts all requests at the
gateway boundary and determines whether to allow or deny each action based on
the defined policies. This provides deterministic authorization outside of the
agent's code, ensuring consistent security enforcement regardless of how the
agent is implemented.

#### Create Cedar Policy

Cedar is an open-source policy language developed by AWS for writing
authorization policies. This creates a Cedar policy that allows refunds under
$1000:

```

permit(principal,
  action == AgentCore::Action::"RefundToolTarget___refund",
  resource == AgentCore::Gateway::"<gateway-arn>")
when {
  context.input.amount < 1000
};

```

The policy uses:

- `permit` - Allows the action (Cedar also supports
  `forbid` to deny actions)
- `principal` - The user making the request
  (OAuth-authenticated)
- `action` - The specific tool being called
  (RefundToolTarget\_\_\_refund)
- `resource` - The gateway instance where the policy
  applies
- `when` condition - Additional requirements (amount must be
  < $1000)

#### Attach Policy to Gateway

Attaches the policy engine to the gateway in ENFORCE mode. In this
mode:

- Every tool call is intercepted and evaluated against all
  policies
- By default, all actions are denied unless explicitly permitted
- If any `forbid` policy matches, access is denied
  (forbid-wins semantics)
- Policy decisions are logged to CloudWatch for monitoring and
  compliance

This ensures all agent operations through the gateway are governed by your
security policies.

## Step 3: Run the setup

Execute the setup script:

```

python setup_policy.py

```

###### Note

The script will take about 2-3 minutes to complete.

## Step 4: Test the policy

Create a file called `test_policy.py`:

```

"""
Test Policy Engine with direct HTTP calls to Gateway
Run after setup: python test_policy.py
"""

import json
import sys
import requests
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient


def test_refund(gateway_url, bearer_token, amount):
    """Test a refund request - print raw response"""
    response = requests.post(
        gateway_url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer_token}",
        },
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "RefundTarget___process_refund",
                "arguments": {"amount": amount}
            },
        },
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {json.dumps(response.json(), indent=2)}")
    return response


def main():
    print("=" * 60)
    print("🧪 Testing Policy Engine")
    print("=" * 60 + "\n")

    # Load configuration
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ Error: config.json not found!")
        print("Please run 'python setup_policy.py' first.")
        sys.exit(1)

    gateway_url = config["gateway_url"]
    refund_limit = config["refund_limit"]

    print(f"Gateway: {gateway_url}")
    print(f"Refund limit: ${refund_limit}\n")

    # Get access token
    print("🔑 Getting access token...")
    gateway_client = GatewayClient(region_name=config["region"])
    token = gateway_client.get_access_token_for_cognito(config["client_info"])
    print("✅ Token obtained\n")

    # Test 1: Refund $500 (should be allowed)
    print(f"📝 Test 1: Refund $500 (Expected: ALLOW)")
    print("-" * 40)
    test_refund(gateway_url, token, 500)
    print()

    # Test 2: Refund $2000 (should be denied)
    print(f"📝 Test 2: Refund $2000 (Expected: DENY)")
    print("-" * 40)
    test_refund(gateway_url, token, 2000)
    print()

    print("=" * 60)
    print("✅ Testing complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

```

Run the test:

```

python test_policy.py

```

## What you've built

Through this tutorial, you've created:

- **MCP Server (Gateway)** - A managed endpoint for
  tools
- **Lambda function** - Mock refund processing
  tool
- **Policy engine** - Cedar-based policy evaluation
  system
- **Cedar policy** - Governance rule allowing
  refunds under $1000
- **OAuth authentication** - Secure access using
  Amazon Cognito tokens

## Troubleshooting

If you encounter issues during setup or testing, refer to the following common
problems and solutions:

| Issue                   | Solution                                                      |
| ----------------------- | ------------------------------------------------------------- |
| "AccessDeniedException" | Check IAM permissions for `bedrock-agentcore:*`               |
| Gateway not responding  | Wait 30-60 seconds after creation for DNS propagation         |
| OAuth token expired     | Tokens expire after 1 hour, script gets new one automatically |

## Clean up

Create a file called `cleanup_policy.py`:

```

"""
Cleanup script to remove Gateway and Policy Engine resources
Run this to clean up: python cleanup_policy.py
"""

from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
from bedrock_agentcore_starter_toolkit.operations.policy.client import PolicyClient
import json


def cleanup():
    with open("config.json", "r") as f:
        config = json.load(f)

    # Clean up Policy Engine first
    print("🧹 Cleaning up Policy Engine...")
    policy_client = PolicyClient(region_name=config["region"])
    policy_client.cleanup_policy_engine(config["policy_engine_id"])
    print("✓ Policy Engine cleaned up\n")

    # Then clean up Gateway
    print("🧹 Cleaning up Gateway...")
    gateway_client = GatewayClient(region_name=config["region"])
    gateway_client.cleanup_gateway(config["gateway_id"], config["client_info"])
    print("✅ Cleanup complete!")


if __name__ == "__main__":
    cleanup()

```

Run the cleanup:

```

python cleanup_policy.py

```
