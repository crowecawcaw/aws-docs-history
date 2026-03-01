# Example implementation of dynamic application management with React

The following example demonstrates how to dynamically manage AWS-managed applications
in a React application. This implementation uses `onAppHostAdded` and `onAppHostRemoved` events to automatically update the user interface when
applications are launched or destroyed. This example demonstrates how to position
applications one after the other vertically on a web page.

## Iframe container component

```

const IFrameAppContainer: React.FC<{ appHost: AppHost }> = ({ appHost }) => {
  const iframeRef = useRef<HTMLIFrameElement>(null);

  useEffect(() => {
    const iframe = iframeRef.current;
    if (iframe) {
      (appHost as IFrameAppHost).setIFrame(iframe);
    }
  }, [appHost]);

  const handleClose = (): void => {
    void appHost.destroy();
  };

  return (
    <div className="app-container">
      <div className="app-header">
        <h2>{appHost.config.name}</h2>
        <button onClick={handleClose}> Close </button>
      </div>
      <iframe ref={iframeRef} className="app-iframe" title={appHost.config.name} />
    </div>
  );
};
```

## Application container component

```

const ApplicationContainer: React.FC<{provider: AmazonConnectProvider}>
  = ({provider}) => {

  const [activeApps, setActiveApps] = useState<Set<AppHost>>(new Set());

  useEffect(() => {
    const appManager = provider.appManager;

    // Handle new applications being added
    const handleAppHostAdded = ({appHost}: AppHostAdded): Promise<void> => {
      setActiveApps((prevApps) => new Set(prevApps).add(appHost));
      return Promise.resolve();
    };

    // Handle applications being removed
    const handleAppHostRemoved = ({appHost}: AppHostRemoved): Promise<void> => {
      setActiveApps((prevApps) => {
        const newApps = new Set(prevApps);
        newApps.delete(appHost);
        return newApps;
      });

      return Promise.resolve();
    };

    // Register event handlers
    appManager.onAppHostAdded(handleAppHostAdded);
    appManager.onAppHostRemoved(handleAppHostRemoved);

    return () => {
        // Un-register event handlers
        appManager.offAppHostAdded(handleAppHostAdded);
        appManager.offAppHostRemoved(handleAppHostRemoved);
    }

  }, [provider.appManager]);

  return (
    <div className="application-container">
      {Array.from(activeApps).map((appHost) => (
        <IFrameAppContainer key={appHost.instanceId} appHost={appHost} />
      ))}
    </div>
  );
};
```
