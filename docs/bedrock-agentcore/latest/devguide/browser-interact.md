# Interacting with a browser session

Once you have started a Browser session, you can interact with it using the WebSocket
API.

Console

###### To interact with a Browser session using the console

1. Navigate to your active Browser session.
2. Use the browser interface to navigate to websites, interact with web
   elements, and perform other browser actions.
3. You can view the browser activity in real-time through the live view
   feature.

SDK
To interact with a Browser session programmatically, use the WebSocket-based
streaming API with the following URL format:

```

https://bedrock-agentcore.<Region>.amazonaws.com/browser-streams/{browser_id}/sessions/{session_id}/automation
```

You can use libraries like Playwright to establish a connection with the
WebSocket and control the browser. Here's an example:

```

from playwright.sync_api import sync_playwright, Playwright, BrowserType
import os
import base64
from bedrock_agentcore.tools.browser_client import browser_session

def main(playwright: Playwright):
    # Keep browser session alive during usage
    with browser_session('us-west-2') as client:

        # Generate CDP endpoint and headers
        ws_url, headers = client.generate_ws_headers()

        # Connect to browser using headers
        chromium: BrowserType = playwright.chromium
        browser = chromium.connect_over_cdp(ws_url, headers=headers)

        # Use the first available context or create one
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()

        page.goto("https://amazon.com/")
        print("Navigated to Amazon")

        # Create CDP session for screenshot
        cdp_client = context.new_cdp_session(page)
        screenshot_data = cdp_client.send("Page.captureScreenshot", {
            "format": "jpeg",
            "quality": 80,
            "captureBeyondViewport": True
        })

        # Decode and save screenshot
        image_data = base64.b64decode(screenshot_data['data'])
        with open("screenshot.jpeg", "wb") as f:
            f.write(image_data)

        print("✅ Screenshot saved as screenshot.jpeg")
        page.close()
        browser.close()

with sync_playwright() as p:
    main(p)

```

The following example code shows how you can perform live view using the
WebSocket-based streaming API.

```

https://bedrock-agentcore.<Region>.amazonaws.com/browser-streams/{browser_id}/sessions/{session_id}/live-view
```

Below is the code.

```

import time
from rich.console import Console
from bedrock_agentcore.tools.browser_client import browser_session
from browser_viewer import BrowserViewerServer

console = Console()

def main():
    try:
         # Step 1: Create browser session
        with browser_session('us-west-2') as client:
            print("\r   ✅ Browser ready!                    ")
            ws_url, headers = client.generate_ws_headers()

            # Step 2: Start viewer server
            console.print("\n[cyan]Step 3: Starting viewer server...[/cyan]")
            viewer = BrowserViewerServer(client, port=8005)
            viewer_url = viewer.start(open_browser=True)

            # Keep running
            while True:
                time.sleep(1)

    except KeyboardInterrupt:
        console.print("\n\n[yellow]Shutting down...[/yellow]")
        if 'client' in locals():
            client.stop()
            console.print("✅ Browser session terminated")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

```
