

# Service implementation patterns
<a name="building-3P-services-implementation-patterns"></a>

third-party services can implement various patterns to extend the agent workspace functionality. The following examples demonstrate some of our key Connect Customer SDK capabilities:

## Launching an application on startup
<a name="building-3P-services-launching-app-on-startup"></a>

```
import {
  AmazonConnectService,
  ServiceContext,
  ServiceCreatedEvent,
} from "@amazon-connect/app";
import { AppControllerClient } from "@amazon-connect/app-controller";
import { AppConfig } from "@amazon-connect/workspace-types";

const SDK_LOG_PREFIX = "[TestService]";

const onCreateHandler = async (event: ServiceCreatedEvent) => {
  const context: ServiceContext = event.context;
  console.log(`${SDK_LOG_PREFIX} Service created: `, context.instanceId);

  const appName = "TargetAppName";
  console.log(`${SDK_LOG_PREFIX} Launching app on startup`, { appName });
  const appControllerClient = new AppControllerClient(context.getProvider());

  // Get list of all applications available to the agent.
  const apps: AppConfig[] = await appControllerClient.getAppCatalog();

  // Find your application by name.
  const appArn = apps.find(
    (app) => app.name === appName
  )?.arn;

  if (!appArn) {
    throw new Error(`${appName} not found.`);
  }

  await appControllerClient.launchApp(appArn);
};

const { provider } = AmazonConnectService.init({
  onCreate: onCreateHandler,
});
```

## Contact event listening with application launching functionality
<a name="building-3P-services-contact-event-listening"></a>

```
import {
  AmazonConnectService,
  ServiceContext,
  ServiceCreatedEvent,
} from "@amazon-connect/app";
import { AppControllerClient } from "@amazon-connect/app-controller";
import {
  ContactClearedHandler,
  ContactClient,
  ContactConnectedHandler,
  ContactStartingAcwHandler,
} from "@amazon-connect/contact";
import { AppConfig } from "@amazon-connect/workspace-types";

const SDK_LOG_PREFIX = "[TestService]";

// Log connected contacts.
const handleConnected: ContactConnectedHandler = async (contactEvent) => {
  console.log(`${SDK_LOG_PREFIX} Contact connected!`, { event: contactEvent });
};

// Launch an application when a contact enters After Contact Work (ACW).
const handleStartingAcw: ContactStartingAcwHandler = async (contactEvent) => {
  const appName = "TargetAppName";
  console.log(`${SDK_LOG_PREFIX} Launching app in ACW`, {
    event: contactEvent,
    appName,
  });
  const appControllerClient = new AppControllerClient(provider);

  // Get list of all applications available to the agent.
  const apps: AppConfig[] = await appControllerClient.getAppCatalog();

  // Find your application by name.
  const appArn = apps.find(
    (app) => app.name === appName
  )?.arn;

  if (!appArn) {
    throw new Error(`${appName} not found.`);
  }

  await appControllerClient.launchApp(appArn);
};

// Log contacts that are cleared.
const handleCleared: ContactClearedHandler = async (contactEvent) => {
  console.log(`${SDK_LOG_PREFIX} Contact cleared:`, {
    event: contactEvent,
    type: contactEvent.type,
  });
};

function registerEventHandlers(contactClient: ContactClient) {
  contactClient.onConnected(handleConnected);
  contactClient.onStartingAcw(handleStartingAcw);
  contactClient.onCleared(handleCleared);
}

// To stop receiving cleared events, pass the same handler that you subscribed.
function unregisterClearedHandler(contactClient: ContactClient) {
  contactClient.offCleared(handleCleared);
}

const onCreateHandler = async (event: ServiceCreatedEvent) => {
  const context: ServiceContext = event.context;
  console.log(`${SDK_LOG_PREFIX} Service created: `, context.instanceId);

  const contactClient = new ContactClient(context.getProvider());
  registerEventHandlers(contactClient);
};

const { provider } = AmazonConnectService.init({
  onCreate: onCreateHandler,
});
```

## Authentication popup functionality
<a name="building-3P-services-authentication-popup"></a>

```
import { AmazonConnectService } from "@amazon-connect/app";
import { AppControllerClient } from "@amazon-connect/app-controller";
import { AmazonConnectProvider } from "@amazon-connect/core";
import { AppConfig } from "@amazon-connect/workspace-types";

interface IdpMessage {
  type: 'IDP_MESSAGE';
  payload: {
    message: string;
    timestamp: string;
  };
}

const SDK_LOG_PREFIX = '[TestService]';
const APP_NAME = 'TestApp'

const IDP_POPUP_CONFIG = {
  width: 600,
  height: 400,
  title: 'IDP Simulation'
};

let provider: AmazonConnectProvider;

const onCreateHandler = async () => {
  console.log(`${SDK_LOG_PREFIX} Service running...`);

  // Start the authentication flow without waiting for it, so that service
  // creation completes. A failure in the auth flow is reported but allows
  // the service to continue running.
  runIdpFlow().catch((error: unknown) => {
    console.error(`${SDK_LOG_PREFIX} IDP flow failed:`, error);
  });

  console.log(`${SDK_LOG_PREFIX} Service creation complete`);
};

// Start the authentication service.
export function initIDPService() {
  ({ provider } = AmazonConnectService.init({
    onCreate: onCreateHandler
  }));
}

/**
  * Creates the IDP authentication popup
  * Returns a promise that resolves when authentication is complete
  * or rejects if authentication fails/times out 
  */
export const initIdpSimulator = (): Promise<void> => {
  return new Promise((resolve, reject) => {

    // Clean up event listeners and timers
    const cleanup = () => {
      window.removeEventListener('message', handleIdpMessage);
    };

    // Handle messages received from the IDP popup
    const handleIdpMessage = async (event: MessageEvent<IdpMessage>) => {
      if (event.data.type === 'IDP_MESSAGE') {
        // Implementation for a successful authentication
        console.log(`${SDK_LOG_PREFIX} Message received from IDP:`, event.data.payload);
        
        try {
          // Launch the application after successful authentication
          await launchApp(APP_NAME);
          console.log(`${SDK_LOG_PREFIX} Successfully launched app`);
          resolve();
        } catch (error) {
          console.error(`${SDK_LOG_PREFIX} Failed to launch app:`, error);
          reject(error);
        } finally {
          cleanup();
        }
      }
    };

    // Open the authentication popup window
    const openIdpPopup = () => {
      // https://developer.mozilla.org/en-US/docs/Web/API/Window/open
      const popup = window.open('/popup.html', // URL to your authentication page
        IDP_POPUP_CONFIG.title, 
        `width=${IDP_POPUP_CONFIG.width},height=${IDP_POPUP_CONFIG.height}`
      );
      
      if (!popup) {
        cleanup();
        reject(new Error('Failed to open IDP popup'));
        return;
      }
    };

    // Listen for messages from the popup
    window.addEventListener('message', handleIdpMessage);

    // Open the popup
    openIdpPopup();    
  });
};

/**
  * Manages the complete authentication flow
  * Handles errors and logging 
  */
export const runIdpFlow = async () => {
  try {
    console.log(`${SDK_LOG_PREFIX} Starting IDP flow...`);
    await initIdpSimulator();
    console.log(`${SDK_LOG_PREFIX} IDP flow completed successfully`);
  } catch (error) {
    console.error(`${SDK_LOG_PREFIX} IDP flow failed!`, error);
    throw error;
  }
};

/**
  * Launches the specified application using the AppController
  * Verifies the app exists in the catalog before attempting to launch 
  */
export async function launchApp(targetAppName: string) {
  const appControllerClient = new AppControllerClient(provider);
  
  // Get list of all applications available to the agent
  const apps: AppConfig[] = await appControllerClient.getAppCatalog();
  console.log(`${SDK_LOG_PREFIX} App Catalog: `, apps);
  
  // Find your application by name
  const testAppArn = apps.find(
    (app) => app.name === targetAppName
  )?.arn;
  
  if (!testAppArn) {
    throw new Error(targetAppName + " not found!");
  }
  
  await appControllerClient.launchApp(testAppArn);
}
```

This is the HTML template for the authentication popup:

```
<!DOCTYPE html>
<html>
  <head>
      <title>IDP Simulation</title>
      <style>
          body {
              font-family: Arial, sans-serif;
              padding: 20px;
              background: #f5f5f5;
          }
          .container {
              background: white;
              padding: 20px;
              border-radius: 8px;
              box-shadow: 0 2px 10px rgba(0,0,0,0.1);
          }
          button {
              padding: 10px 20px;
              margin: 5px;
              border: none;
              border-radius: 4px;
              cursor: pointer;
              background: #007bff;
              color: white;
          }
          button:hover {
              background: #0056b3;
          }
      </style>
  </head>
  <body>
      <div class="container">
          <h2>IDP Simulation</h2>
          <p>Click the button below to simulate IDP authentication</p>
          <button id="authButton">Authenticate</button>
      </div>
      <script>
          // When authentication button is clicked, send success message 
          // back to parent window
          document.getElementById('authButton').onclick = function() {
              window.opener.postMessage({
                  type: 'IDP_MESSAGE',
                  payload: {
                      message: 'User authenticated via IDP',
                      timestamp: new Date().toISOString()
                  }
              }, '*');
              window.close();
          };
      </script>
  </body>
</html>
```