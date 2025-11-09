# Using AgentCore Browser with other Browser libraries and

tools

You can build browser agents using various frameworks and libraries to automate web
interactions. This section demonstrates how to build browser agents using different
frameworks.

Nova Act
You can build a browser agent using Nova Act to automate web interactions:

###### Step 1: Install dependencies

Create a project folder (if you have not already):

```
mkdir agentcore-browser-quickstart
cd agentcore-browser-quickstart
python3 -m venv .venv
source .venv/bin/activate
```

###### Note

On Windows, use: `.venv\Scripts\activate`

Install the required packages:

```
pip install bedrock-agentcore nova-act rich boto3
```

These packages provide:

- `bedrock-agentcore`: The SDK for Amazon Bedrock AgentCore tools including
  AgentCore Browser
- `nova-act`: The SDK for Nova Act which includes the model and
  orchestrator for browser automation
- `rich`: Library for rich text and beautiful formatting in the
  terminal
- `boto3`: AWS SDK for Python (Boto3) to create, configure, and
  manage AWS services

###### Step 2: Get Nova Act API Key

Navigate to [Nova Act](https://nova.amazon.com/act "https://nova.amazon.com/act") page and
generate an API key using your amazon.com credentials. (Note this currently works only
for US based amazon.com accounts)

Create a file named `nova_act_browser_agent.py` and add the following
code:

###### Write a browser agent using Nova Act

The following Python code shows how to write a browser agent using Nova Act. For
information about obtaining the API key for Nova Act, see [Amazon Nova Act documentation](https://nova.amazon.com/act "https://nova.amazon.com/act").

```

from bedrock_agentcore.tools.browser_client import browser_session
from nova_act import NovaAct
from rich.console import Console
import argparse
import json
import boto3

console = Console()

from boto3.session import Session

boto_session = Session()
region = boto_session.region_name
print("using region", region)

def browser_with_nova_act(prompt, starting_page, nova_act_key, region="us-west-2"):
    result = None
    with browser_session(region) as client:
        ws_url, headers = client.generate_ws_headers()
        try:
            with NovaAct(
                cdp_endpoint_url=ws_url,
                cdp_headers=headers,
                nova_act_api_key=nova_act_key,
                starting_page=starting_page,
            ) as nova_act:
                result = nova_act.act(prompt)
        except Exception as e:
            console.print(f"NovaAct error: {e}")
        finally:
            return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Browser Search instruction")
    parser.add_argument("--starting-page", required=True, help="Starting URL")
    parser.add_argument("--nova-act-key", required=True, help="Nova Act API key")
    parser.add_argument("--region", default="us-west-2", help="AWS region")
    args = parser.parse_args()

    result = browser_with_nova_act(
        args.prompt, args.starting_page, args.nova_act_key, args.region
    )
    console.print(f"\n[cyan] Response[/cyan] {result.response}")
    console.print(f"\n[bold green]Nova Act Result:[/bold green] {result}")

```

###### Step 3: Run the agent

Execute the script (Replace with your Nova Act API key in the command):

```
python nova_act_browser_agent.py --prompt "What are the common usecases of Bedrock AgentCore?" --starting-page "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html" --nova-act-key "your-nova-act-API-key"
```

###### Expected output

You should see the agent's response containing details of the common usecases of
Amazon Bedrock AgentCore. The agent navigates the website, performs the search, and extracts
the requested information.

If you encounter errors, verify:

- Your IAM role/user has the correct permissions
- Your Nova Act API key is correct
- Your AWS credentials are properly configured

###### Step 4: View the browser session live

While your browser script is running, you can view the session in real-time
through the AWS Console:

1. Open the [Amazon Bedrock AgentCore Browser Console](https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools "https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools")
2. Navigate to **Built-in tools** in the left
   navigation
3. Select the Browser tool (for example, `AgentCore Browser Tool`, or
   your custom browser)
4. In the **Browser sessions** section, find your
   active session with status **Ready**
5. In the **Live view / recording** column, click the
   provided "View live session" URL
6. The live view opens in a new browser window, displaying the real-time browser
   session

The live view interface provides:

- Real-time video stream of the browser session
- Interactive controls to take over or release control from automation
- Ability to terminate the session

Strands
You can build an agent that uses the Browser Tool as one of its tools using the
Strands framework:

###### Step 1: Install dependencies

Create a project folder (if you have not already):

```
mkdir agentcore-browser-quickstart
cd agentcore-browser-quickstart
python3 -m venv .venv
source .venv/bin/activate
```

###### Note

On Windows, use: `.venv\Scripts\activate`

Install the required packages:

```
pip install bedrock-agentcore strands-agents strands-agents-tools playwright nest-asyncio
```

These packages provide:

- `bedrock-agentcore`: The SDK for Amazon Bedrock AgentCore tools including
  AgentCore Browser
- `strands-agents`: The Strands agent framework
- `strands-agents-tools`: The tools that the Strands agent framework
  offers including Browser tool
- `playwright`: Python library for browser automation. Strands uses
  playwright for browser automation
- `nest-asyncio`: Allows running asyncio event loops within existing
  event loops

###### Step 2: Create your agent with AgentCore Browser

Create a file named `browser_agent.py` and add the following
code:

```

from strands import Agent
from strands_tools.browser import AgentCoreBrowser

# Initialize the Browser tool
browser_tool = AgentCoreBrowser(region="us-west-2")

# Create an agent with the Browser tool
agent = Agent(tools=[browser_tool.browser])

# Test the agent with a web search prompt
prompt = "what are the services offered by Bedrock AgentCore? Use the documentation link if needed: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html"
print(f"\\n\\nPrompt: {prompt}\\n\\n")

response = agent(prompt)
print("\\n\\nAgent Response:")
print(response.message["content"][0]["text"])

```

This code:

- Initializes the Browser tool for your region
- Creates an agent that can use the browser to interact with websites
- Sends a prompt asking the agent to search AgentCore documentation and answer
  question
- Prints the agent's response with the information found

###### Step 3: Run the agent

Execute the script:

```
python browser_agent.py
```

###### Expected output

You should see the agent's response containing details about AgentCore services
from the documentation. The agent navigates the website and extracts the requested
information.

If you encounter errors, verify:

- Your IAM role/user has the correct permissions
- You have model access enabled in the Amazon Bedrock console
- Your AWS credentials are properly configured

###### Step 4: View the browser session live

While your browser script is running, you can view the session in real-time
through the AWS Console:

1. Open the [Amazon Bedrock AgentCore Browser Console](https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools "https://us-west-2.console.aws.amazon.com/bedrock-agentcore/builtInTools")
2. Navigate to **Built-in tools** in the left
   navigation
3. Select the Browser tool (for example, `AgentCore Browser Tool`, or
   your custom browser)
4. In the **Browser sessions** section, find your
   active session with status **Ready**
5. In the **Live view / recording** column, click the
   provided "View live session" URL
6. The live view opens in a new browser window, displaying the real-time browser
   session

The live view interface provides:

- Real-time video stream of the browser session
- Interactive controls to take over or release control from automation
- Ability to terminate the session

Playwright
You can use the Playwright automation framework with the Browser Tool:

###### Step 1: Install dependencies

Create a project folder (if you didn't create one before) and install the required
packages:

```
mkdir agentcore-browser-quickstart
cd agentcore-browser-quickstart
python3 -m venv .venv
source .venv/bin/activate
```

###### Note

On Windows, use: `.venv\Scripts\activate`

Install the required packages:

```
pip install bedrock-agentcore playwright boto3 nest-asyncio
```

These packages provide:

- `bedrock-agentcore`: The SDK for Amazon Bedrock AgentCore tools including
  AgentCore Browser
- `playwright`: Python library for browser automation
- `boto3`: AWS SDK for Python (Boto3) to create, configure, and
  manage AWS services
- `nest-asyncio`: Allows running asyncio event loops within existing
  event loops

###### Step 2: Control browser with Playwright

You can use Browser directly without an agent framework or an LLM. This is useful
when you want programmatic control over browser automation. Amazon Bedrock AgentCore provides
integration with Playwright for browser automation.

###### Async Playwright example

Create a file named `direct_browser_playwright.py` and add the
following code:

```

from playwright.async_api import async_playwright, Playwright, BrowserType
from bedrock_agentcore.tools.browser_client import browser_session
import asyncio

async def run(playwright: Playwright):
    # Create and maintain a browser session
    with browser_session('us-west-2') as client:
        # Get WebSocket URL and authentication headers
        ws_url, headers = client.generate_ws_headers()

        # Connect to the remote browser
        chromium: BrowserType = playwright.chromium
        browser = await chromium.connect_over_cdp(
            ws_url,
            headers=headers
        )

        # Get the browser context and page
        context = browser.contexts[0]
        page = context.pages[0]

        try:
            # Navigate to a website
            await page.goto("https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html")

            # Print the page title
            title = await page.title()
            print(f"Page title: {title}")

            # Keep the session alive for 2 minutes to allow viewing
            print("\\n\\nBrowser session is active. Check the AWS Console for live view.")
            await asyncio.sleep(120)

        finally:
            # Clean up resources
            await page.close()
            await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())

```

###### Sync Playwright example with live view

Alternatively, you can use the sync API with integrated live view server:

```

from playwright.sync_api import sync_playwright, Playwright, BrowserType
from bedrock_agentcore.tools.browser_client import browser_session
from browser_viewer import BrowserViewerServer
import time

def run(playwright: Playwright):
    # Create the browser session and keep it alive
    with browser_session('us-west-2') as client:
        ws_url, headers = client.generate_ws_headers()

        # Start viewer server
        viewer = BrowserViewerServer(client, port=8005)
        viewer_url = viewer.start(open_browser=True)

        # Connect using headers
        chromium: BrowserType = playwright.chromium
        browser = chromium.connect_over_cdp(
            ws_url,
            headers=headers
        )

        context = browser.contexts[0]
        page = context.pages[0]

        try:
            page.goto("https://amazon.com/")
            print(page.title())
            time.sleep(120)
        finally:
            page.close()
            browser.close()

with sync_playwright() as playwright:
    run(playwright)

```

###### Run the script

Execute either script:

```
python direct_browser_playwright.py
```

###### Expected output

You should see the page title printed (for example, `Page title: What is
 Amazon Bedrock AgentCore? - Amazon Bedrock AgentCore`). The script keeps the
browser session active for 2 minutes before closing.

Both examples:

- Create a managed browser session using Amazon Bedrock AgentCore Browser
- Connect to the remote Chrome browser using Playwright's Chrome DevTools Protocol
  (CDP)
- Navigate to AgentCore documentation and print the page title
- Keep the session alive for 2 minutes, allowing you to view it in the AWS
  Console
- Properly close the browser and clean up resources
