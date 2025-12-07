# Step 2: Develop locally

**Prerequisites:** Python development environment (Python 3.10 or later)

The Nova Act extension transforms how you build with Nova Act by bringing the entire agent development experience directly into IDEs such as [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-nova-act-extension "https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-nova-act-extension"), [Cursor](https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension "https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension"), and [Kiro](https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension "https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension"). Develop, test, and debug your agent in a single IDE environment.

## Choose your authentication method

Nova Act supports two authentication methods for local development:

### **API key authentication**

- **Prerequisites:** API key from [nova.amazon.com/act](http://nova.amazon.com/act "http://nova.amazon.com/act"). Your API key is tied to your Amazon.com account.
- **Billing:** Free of charge with daily limits
- **Best for:** Quick experimentation and prototyping

###### Note

By authenticating using your API key, your access and use of the Nova Act extension is subject to the nova.amazon.com [Terms of Use](https://www.amazon.com/gp/help/customer/display.html?&nodeId=Tsn7s47ytlgjRBHozK "https://www.amazon.com/gp/help/customer/display.html?&nodeId=Tsn7s47ytlgjRBHozK") and Amazon collects information from your interactions with Nova Act.

### **AWS IAM authentication** (Recommended for production)

- **Prerequisites:**
  AWS account with IAM permissions (see [AWS Managed Policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md"))
- **Billing:** Usage charges apply to your AWS account. Visit the [Nova Act pricing](https://aws.amazon.com/nova/pricing "https://aws.amazon.com/nova/pricing") page for details.
- **Best for:** Production development and deployment

###### Note

By authenticating using your AWS IAM, your access and use of the Nova Act extension is subject to your [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") and/or [Customer Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/") (or other agreement governing your use of the AWS service). Amazon temporarily collects information from your interactions with Nova Act to support runtime of the model.

When using the Nova Act SDK, you’ll see a console message indicating which authentication method is active.

## Which authentication method should I choose?

Use API key authentication when you want to quickly explore Nova Act capabilities without AWS setup. This is ideal for learning, prototyping, and validating automation ideas before committing to production deployment.

Use AWS IAM authentication when you’re ready to build production workflows. This method provides full access to AWS services, monitoring, and production-scale infrastructure.

### Develop with API key authentication

With API key authentication, you can develop Nova Act workflows using either the Nova Act SDK or the Nova Act extension. You can start from scratch, import scripts from the playground, or generate workflows using the IDE’s chat experience.

1. Get your API key from [nova.amazon.com/act](http://nova.amazon.com/act "http://nova.amazon.com/act")
2. Install the Nova Act extension (check the [nova-act-extension](https://github.com/aws/nova-act-extension "https://github.com/aws/nova-act-extension") GitHub repository for instructions and supported environments).
3. Open Builder Mode in the Nova Act extension to access the live browser preview
4. Generate your workflow using one of these approaches:
   - **Chat-to-code**: Use GitHub Copilot in VS Code to describe your automation needs in natural language
     - Example: `@novaAct: "I need an agent that logs into a customer portal, searches for unresolved tickets, and updates their status based on completion criteria."`

   - **Import from playground**: Download a script you created in the Nova Act playground and open it in the IDE
   - **Start from template**: Select a workflow template from the extension

5. Run and debug your workflow in Builder Mode with live browser preview

Example script with API key authentication:

```
from nova_act import NovaAct
import os

# Browser args enables browser debugging on port 9222.
os.environ["NOVA_ACT_BROWSER_ARGS"] = "--remote-debugging-port=9222"
# Get your API key from https://nova.amazon.com/act
# Set API Key using Set API Key command (CMD/Ctrl+Shift+P) or set it below.
# os.environ["NOVA_ACT_API_KEY"] = "<YOUR_API_KEY>"

# Initialize Nova Act with your starting page.
nova = NovaAct(
    starting_page="https://nova.amazon.com/act/gym",
    headless=True,
    tty=False
)

# Running nova.start will launch a new browser instance.
# Only one nova.start() call is needed per Nova Act session.
nova.start()

# Add your nova.act(<prompt>) statement here
nova.act("Click on NextDot, then explore possible destinations.")

# Leaving nova.stop() commented keeps NovaAct session running.
# To stop a NovaAct instance, press "Restart Notebook" (top-right) or uncomment nova.stop() - note this also shuts down the browser instantiated by NovaAct so subsequent nova.act() calls will fail.
# nova.stop()
```

### Develop with AWS IAM authentication

To develop workflows locally using AWS IAM authentication:

1. Configure AWS credentials with appropriate IAM roles and permissions (see [AWS Managed Policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md")) in your development environment.
2. Create a Nova Act workflow definition using the Nova Act AWS console or CLI:
   - In the Nova Act AWS console, select **Create workflow definition** and follow the instructions to create a workflow definition.
   - Or, using the Nova Act CLI, run `act workflow create —name <your-workflow-name>`

3. Use the AWS workflow template in the IDE extension or an example script, such as the one shown below, to start developing your script.

**Example script with AWS IAM authentication (using workflow context manager)**

```
import os
from nova_act import NovaAct, Workflow

def main(payload):
    with Workflow(
        workflow_definition_name="<your-workflow-name>",
        model_id="nova-act-latest"
    ) as workflow:
        with NovaAct(
            starting_page="https://nova.amazon.com/act/gym",
            workflow=workflow,
            headless=True,
            tty=False
        ) as nova:
            nova.act("Click on NextDot, then explore possible destinations.")

if __name__ == "__main__":
    main({})
```

**Example script with AWS IAM authentication (using @workflow Python decorator to wrap your function)**

```
from nova_act import NovaAct, workflow

@workflow(workflow_definition_name="<your-workflow-name>", model_id="nova-act-latest")
def search_space_destinations():
    with NovaAct(
        starting_page="https://nova.amazon.com/act/gym",
        headless=True,
        tty=False
    ) as nova:
        nova.act("Click on NextDot, then explore possible destinations.")

# main function MUST accept payload
def main(payload):
    search_space_destinations()

if __name__ == "__main__":
    main({})
```
