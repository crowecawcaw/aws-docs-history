# Strands Agents Integrations

[Strands Agents](https://strandsagents.com/ "https://strandsagents.com/") is an open source framework for building AI agents with a broad set of tool support. Strands makes it simple to equip an agent with tools it can use. For example, you can equip an agent with a tool that enables it to search the web. In the example below, we configure Nova Act for a Strands agent to use it as a tool.

###### Note

When Nova Act is run as a tool, the run time (Nova Act SDK) is run on the same compute as the Strands agent. For example, if the Strands agent is running on AgentCore Runtime, the Nova Act SDK will also run there. If you want the browser that Nova Act uses to run on AgentCore Browser Tool, you define that behavior within the Nova Act tool definition.

## Running a local Strands agent that uses a Nova Act tool

In this example, we run Strands Agents on our local machine. We assume that Strands has already been installed. The Nova Act SDK automatically installs Chromium the first time you run it, if Chrome is not already installed on your system. On some platforms where Chromium requires root installation, you may need to install it manually.

Start by installing `nova-act` and the Bedrock AgentCore libraries:

- `pip install nova-act, bedrock_agentcore`

Now let’s create Nova Act as a tool for our Strands agent. The tool will take in a website url, an instruction, and an option to download content. Save the below in a folder named `tools` in a file named `web-browser-tool.py`. Note the description of the tool at the start of the `get_current_ticker_price`. This informs the Strands agent what this tool should be used for, arguments to pass in, and the return type.

```
from strands import Agent, tool
from nova_act import NovaAct

@tool
def browser_automation_tool(starting_url:str, instr: str, download: bool) -> str:
    """
    Automates tasks in a browser on the starting_url website, using the instructions provided.
    Multiple sessions can be run in parallel. The tool can do some basic reasoning of its own.

    Args:
        starting_url (str): The website url to perform actions on
        instr (str): the instruction in natural language to be sent to the browser for the task to be performed
        download (bool): Whether to download generated content from the page or not

    Returns:
        str: The result of the action performed.
    """

    with NovaAct(
        starting_page=starting_url
    ) as browser:
        try:
            result = browser.act(instr, max_steps=10)
            if download:
                with browser.page.expect_download() as download_info:
                    browser.act("click on the download button")
                    # Temp path for the download is available.
                    print(f"Downloaded file {download_info.value.path()}")
                    download_info.value.save_as("my_downloaded_file.png")
                    print("Image downloaded successfully.")
                    success = True
            return success

        except Exception as e:
            error_msg = f"Error processing instruction: {instr}. Error: {str(e)}"
            print(error_msg)
            return error_msg
```

To make this tool available to a Strands agent, import the tool, and then add it to the list of tools available to the agent.

```
from tools import browser_automation_tool

def generate_and_retrieve_image():
    agent = Agent(tools=[browser_automation_tool])
    agent("On nova.amazon.com, generate an image of a wise robot contemplating life, and download the image.")

def main():
    generate_and_retrieve_image()
```

## Running a Strands agent on AgentCore that uses a Nova Act tool

Now let’s run the same agent as above but instead of running on our local machine, this time let’s run it on AgentCore Runtime with AgentCore BrowserTool. Refer to [this guide](https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/ "https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/") for instructions on deploying a Strands agent on AgentCore, and [this guide](https://builder.aws.com/content/32HpPjNanKLl7OZTpn48xhV0mSX/run-your-nova-act-workflow-on-amazon-bedrock-agentcore "https://builder.aws.com/content/32HpPjNanKLl7OZTpn48xhV0mSX/run-your-nova-act-workflow-on-amazon-bedrock-agentcore") for using Nova Act with AgentCore Browser Tool.
