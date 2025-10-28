# Set up the Amazon SageMaker Partner AI Apps SDKs

The following topic outlines the process needed to install and use the application-specific
SDKs with Amazon SageMaker Partner AI Apps. To install and use SDKs for applications, you must specify environment
variables specific to Partner AI Apps, so the application’s SDK can pick up environment variables and
trigger authorization. The following sections give information about the steps needed to
complete this for each of the supported application types.

## Comet

Comet offers two products:

- Opik is an source LLM evaluation framework.
- Comet’s ML platform can be used to track, compare, explain, and optimize models across the
  complete ML lifecycle.

Comet supports the use of two different SDKs based on the product that you are interacting
with. Complete the following procedure to install and use the Comet or Opik SDKs. For more
information about the Comet SDK, see [Quickstart](https://www.comet.com/docs/v2/guides/quickstart/ "https://www.comet.com/docs/v2/guides/quickstart/"). For more information about the Opik SDK,
see [Open source LLM evaluation framework](https://github.com/comet-ml/opik "https://github.com/comet-ml/opik").

1. Launch the environment that you are using the Comet or Opik SDKs with Partner AI Apps in. For
   information about launching a JupyterLab application, see [Create a space](studio-updated-jl-user-guide-create-space.md "studio-updated-jl-user-guide-create-space.md"). For information about
   launching a Code Editor, based on Code-OSS, Visual Studio Code - Open Source application, see [Launch a Code Editor application in Studio](code-editor-use-studio.md "code-editor-use-studio.md").
2. Launch a Jupyter notebook or Code Editor space.
3. From the development environment, install the compatible Comet, Opik, and SageMaker Python SDK
   versions. To be compatible:
   - The SageMaker Python SDK version must be at least `2.237.0`.
   - The Comet SDK version must be the latest version.
   - The Opik SDK version must match the version used by your Opik application. Verify the
     Opik version used in the Opik web application UI. The exception to this is that the
     Opik SDK version must be at least `1.2.0` when the Opik application version
     is `1.1.5`.

###### Note

SageMaker JupyterLab comes with SageMaker Python SDK installed. However, you may need to upgrade
the SageMaker Python SDK if the version is lower than `2.237.0`.

```
%pip install sagemaker>=2.237.0 comet_ml

##or

%pip install sagemaker>=2.237.0 opik=`<compatible-version>`
```

4. Set the following environment variables for the application resource ARN. These
   environment variables are used to communicate with the Comet and Opik SDKs. To retrieve
   these values, navigate to the details page for the application in
   Amazon SageMaker Studio.

```
os.environ['AWS_PARTNER_APP_AUTH'] = 'true'
os.environ['AWS_PARTNER_APP_ARN'] = '`<partner-app-ARN>`'
```

5. For the Comet application, the SDK URL is automatically included as part of the API key
   set in the following step. You may instead set the `COMET_URL_OVERRIDE`
   environment variable to manually override the SDK URL.

```
os.environ['COMET_URL_OVERRIDE'] = '`<comet-url>`'
```

6. For the Opik application, the SDK URL is automatically included as part of the API key
   set in the following step. You may instead set the `OPIK_URL_OVERRIDE`
   environment variable to manually override the SDK URL. To get the Opik workspace name,
   see the Opik application and navigate to the user's workspace.

```
os.environ['OPIK_URL_OVERRIDE'] = '`<opik-url>`'
os.environ['OPIK_WORKSPACE'] = '`<workspace-name>`'
```

7. Set the environment variable that identifies the API key for Comet or Opik. This is used
   to verify the connection from SageMaker to the application when the Comet and Opik SDKs are
   used. This API key is application-specific and is not managed by SageMaker. To get this key,
   you must log into the application and retrieve the API key. The Opik API key is the same
   as the Comet API key.

```
os.environ['COMET_API_KEY'] = '`<API-key>`'
os.environ["OPIK_API_KEY"] = os.environ["COMET_API_KEY"]
```

## Fiddler

Complete the following procedure to install and use the Fiddler Python Client. For information
about the Fiddler Python Client, see [About Client 3.x](https://docs.fiddler.ai/python-client-3-x/about-client-3x "https://docs.fiddler.ai/python-client-3-x/about-client-3x").

1. Launch the notebook environment that you are using the Fiddler Python Client with Partner AI Apps
   in. For information about launching a JupyterLab application, see [Create a space](studio-updated-jl-user-guide-create-space.md "studio-updated-jl-user-guide-create-space.md"). For information about
   launching a Code Editor, based on Code-OSS, Visual Studio Code - Open Source application, see [Launch a Code Editor application in Studio](code-editor-use-studio.md "code-editor-use-studio.md").
2. Launch a Jupyter notebook or Code Editor space.
3. From the development environnment, install the Fiddler Python Client and SageMaker Python SDK
   versions. To be compatible:
   - The SageMaker Python SDK version must be at least `2.237.0`.
   - The Fiddler Python Client version must be compatible with the version of Fiddler used in
     the application. After verifying the Fiddler version from the UI, see the Fiddler
     [Compatibility Matrix](https://docs.fiddler.ai/history/compatibility-matrix "https://docs.fiddler.ai/history/compatibility-matrix")
     for the compatible Fiddler Python Client version.

###### Note

SageMaker JupyterLab comes with SageMaker Python SDK installed. However, you may need to upgrade
the SageMaker Python SDK if the version is lower than `2.237.0`.

```
%pip install sagemaker>=2.237.0 fiddler-client=`<compatible-version>`
```

4. Set the following environment variables for the application resource ARN and the SDK URL.
   These environment variables are used to communicate with the Fiddler Python Client. To
   retrieve these values, navigate to the details page for the Fiddler application in Amazon SageMaker Studio.  

```
os.environ['AWS_PARTNER_APP_AUTH'] = 'true'
os.environ['AWS_PARTNER_APP_ARN'] = '`<partner-app-ARN>`'
os.environ['AWS_PARTNER_APP_URL'] = '`<partner-app-URL>`'
```

5. Set the environment variable that identifies the API key for the Fiddler application.
   This is used to verify the connection from SageMaker to the Fiddler application when
   the Fiddler Python Client is used. This API key is application-specific and is not managed
   by SageMaker. To get this key, you must log into the Fiddler application and retrieve the API
   key.

```
os.environ['FIDDLER_KEY'] = '`<API-key>`'
```

## Deepchecks

Complete the following procedure to install and use Deepchecks Python SDK.

1. Launch the notebook environment that you are using the Deepchecks Python SDK with Partner AI Apps
   in. For information about launching a JupyterLab application, see [Create a space](studio-updated-jl-user-guide-create-space.md "studio-updated-jl-user-guide-create-space.md"). For information about
   launching a Code Editor, based on Code-OSS, Visual Studio Code - Open Source application, see [Launch a Code Editor application in Studio](code-editor-use-studio.md "code-editor-use-studio.md").
2. Launch a Jupyter notebook or Code Editor space.
3. From the development environment, install the compatible Deepchecks Python SDK and SageMaker
   Python SDK versions.  Partner AI Apps is running version `0.21.15` of Deepchecks. To be
   compatible:
   - The SageMaker Python SDK version must be at least `2.237.0`.
   - The Deepchecks Python SDK must use the minor version `0.21`.

###### Note

SageMaker JupyterLab comes with SageMaker Python SDK installed. However, you may need to upgrade
the SageMaker Python SDK if the version is lower than `2.237.0`.

```
%pip install sagemaker>=2.237.0 deepchecks-llm-client>=0.21,<0.22
```

4. Set the following environment variables for the application resource ARN and the SDK URL.
   These environment variables are used to communicate with the Deepchecks Python SDK. To
   retrieve these values, navigate to the details page for the application in
   Amazon SageMaker Studio.  

```
os.environ['AWS_PARTNER_APP_AUTH'] = 'true'
os.environ['AWS_PARTNER_APP_ARN'] = '`<partner-app-ARN>`'
os.environ['AWS_PARTNER_APP_URL'] = '`<partner-app-URL>`'
```

5. Set the environment variable that identifies the API key for the Deepchecks application.
   This is used to verify the connection from SageMaker to the Deepchecks application when the
   Deepchecks Python SDK is used. This API key is application-specific and is not managed by
   SageMaker. To get this key, see [Setup: Python SDK Installation & API Key Retrieval](https://llmdocs.deepchecks.com/docs/setup-sdk-installation-api-key#generate-an-api-key-via-the-ui "https://llmdocs.deepchecks.com/docs/setup-sdk-installation-api-key#generate-an-api-key-via-the-ui").

```
os.environ['DEEPCHECKS_API_KEY'] = '`<API-key>`'
```

## Lakera

Lakera does not offer an SDK. Instead, you can interact with the Lakera Guard API through HTTP
requests to the available endpoints in any programming language. For more information, see [Lakera
Guard API](https://platform.lakera.ai/docs/api "https://platform.lakera.ai/docs/api").

To use the SageMaker Python SDK with Lakera, complete the following steps:

1. Launch the environment that you are using Partner AI Apps in. For information about launching
   a JupyterLab application, see [Create a space](studio-updated-jl-user-guide-create-space.md "studio-updated-jl-user-guide-create-space.md"). For information about
   launching a Code Editor, based on Code-OSS, Visual Studio Code - Open Source application, see [Launch a Code Editor application in Studio](code-editor-use-studio.md "code-editor-use-studio.md").
2. Launch a Jupyter notebook or Code Editor space.
3. From the development environment, install the compatible SageMaker Python SDK version. The
   SageMaker Python SDK version must be at least `2.237.0`

###### Note

SageMaker JupyterLab comes with SageMaker Python SDK installed. However, you may need to upgrade
the SageMaker Python SDK if the version is lower than `2.237.0`.

```
%pip install sagemaker>=2.237.0
```

4. Set the following environment variables for the application resource ARN and the SDK URL.
   To retrieve these values, navigate to the details page for the application in
   Amazon SageMaker Studio.

```
os.environ['AWS_PARTNER_APP_ARN'] = '`<partner-app-ARN>`'
os.environ['AWS_PARTNER_APP_URL'] = '`<partner-app-URL>`'
```
