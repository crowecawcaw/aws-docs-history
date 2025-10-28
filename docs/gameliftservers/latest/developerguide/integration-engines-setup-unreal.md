# Integrate Amazon GameLift Servers into an Unreal Engine

project

Learn how to integrate the Amazon GameLift Servers SDK for Unreal Engine into your game projects to access
the full server SDK feature set.

###### Tip

For faster deployment, try the Amazon GameLift Servers standalone plugin for Unreal Engine. It provides
guided UI workflows to quickly deploy your game server with minimal setup, so you can
try out your game components in action. See [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md").

Additional resources:

- [C++ (Unreal) server SDK 5.x for
  Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")
- [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md")

## Install the server SDK for

Unreal

Get the open-source Amazon GameLift Servers SDK for Unreal Engine from [GitHub](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal"). The repository's readme files contain prerequisites and
installation instructions.

## Set up build targets and module rules

Modify your game project files to properly generate build components for use with
Amazon GameLift Servers.

###### To add client and server build targets:

1. Open your game project's code files and locate the file
   `.../Games/`[your application name]`Source/`[your application name]`Target.cs`
   file. Example: `.../Source/GameLiftUnrealAppTarget.cs`.
   (If you use Visual Studio, open the project's `.sln` file.)
2. Copy this file to create two new target files in the `Source/` directory.
   - Client target – Rename the new file to ``[your application name]`Client.Target.cs`.
     Edit the contents to update the class name and target type values, as illustrated in the following sample code:

   ```
   using UnrealBuildTool;
     using System.Collections.Generic;

     public class GameLiftUnrealAppClientTarget :  TargetRules
    {
        public GameLiftUnrealAppClientTarget ( TargetInfo Target ) :  base ( Target )
        {
            Type = TargetType.Client;
            DefaultBuildSettings = BuildSettingsVersion.V2;
            IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_1;
            ExtraModuleNames.Add( "GameLiftUnrealApp");
        }
    }
   ```

   - Server target – Rename the new file to ``[your application name]`Server.Target.cs`.
     Edit the contents to update the class name and target type values, as illustrated in the following sample code:

   ```
   using UnrealBuildTool;
     using System.Collections.Generic;

     public class GameLiftUnrealAppServerTarget :  TargetRules
    {
        public GameLiftUnrealAppServerTarget ( TargetInfo Target ) :  base ( Target )
        {
            Type = TargetType.Server;
            DefaultBuildSettings = BuildSettingsVersion.V2;
            IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_1;
            ExtraModuleNames.Add( "GameLiftUnrealApp");
        }
    }
   ```

3. Regenerate your project files. If you're using Visual Studio, you can right-click your game project's `.uproject`
   file and select **Generate Visual Studio Project Files**.

###### To update the game project module rules:

Update the game project's module rules to take a dependency on the plugin.

1. Open your game project's code files and locate the file
   `.../Games/`[your application name]`Source/`[your application name]`.Build.cs`
   file. Example: `.../Source/GameLiftUnrealApp.Build.cs`.
   (If you use Visual Studio, open the project's `.sln` file.)
2. Locate the `ModuleRules` class and update as illustrated in the following sample code:

```
using UnrealBuildTool;

  public class GameLiftUnrealApp :  ModuleRules
 {
     public GameLiftUnrealApp ( ReadOnlyTargetRules Target ) :  base ( Target )
     {
         PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
         PublicDependencyModuleNames.AddRange( new string[] {  "Core",  "CoreUObject",  "Engine",  "InputCore",  "HeadMountedDisplay",  "EnhancedInput" });
      // Add the following section
         if (Target.Type == TargetType.Server)
         {
             PublicDependencyModuleNames.Add("GameLiftServerSDK");
         }
         else
         {
             PublicDefinitions.Add("WITH_GAMELIFT=0");
         }
         bEnableExceptions =  true;
     }
 }
```

3. After creating the new target files and modifying the module rules, rebuild your game
   project.

## Add game hosting functionality

to your server code

After server SDK installation and setup, the next step is to integrate game hosting
functionality into your server code. The server SDK enables your game server to
communicate with the Amazon GameLift Servers service, receive instructions for game sessions, report
status and health, and perform other actions.

This topic provides sample code that adds the minimum functionality required to host
your game with Amazon GameLift Servers.

###### Step 1: Update the `GameMode` header file

1. Open your game project's code files and locate the file
   ``Your-application-name`GameMode.h`file. Example:`GameLiftUnrealAppGameMode.h`. 
If you use Visual Studio, open the `.sln` file for your
   game project.
2. Change the header file to include the following example code. Be sure to
   replace "GameLiftUnrealApp" with your own application name.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "GameLiftUnrealAppGameMode.generated.h"

struct FProcessParameters;

DECLARE_LOG_CATEGORY_EXTERN(GameServerLog, Log, All);

UCLASS(minimalapi)
class AGameLiftUnrealAppGameMode : public AGameModeBase
{
    GENERATED_BODY()

public:
    AGameLiftUnrealAppGameMode();

protected:
    virtual void BeginPlay() override;

private:
    void InitGameLift();

private:
    TSharedPtr<FProcessParameters> ProcessParameters;
};
```

###### Step 2: Add required server SDK calls to your game server code

Use the sample code in this section to integrate your game server code for use with
Amazon GameLift Servers. For details on what the code does, see [Initialize the server process](gamelift-sdk-server-api.md#gamelift-sdk-server-initialize "gamelift-sdk-server-api.md#gamelift-sdk-server-initialize") and [C++ (Unreal) server SDK 5.x for
Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md").

###### Note

The `WITH_GAMELIFT` preprocessor flag serves two purposes:

- Restricts Amazon GameLift Servers backend API calls to Unreal server builds only
- Ensures compatibility across different Unreal build targets

1. Open the related source file
   ``Your-application-name`GameMode.cpp`file. In our example:`GameLiftUnrealAppGameMode.cpp`.
2. Change the code to align with the following example code. Be sure to replace
   any instance of "GameLiftUnrealApp" with your own application name.

The code sample provided shows how to add the required elements for integration
with Amazon GameLift Servers. These include:

    * Initialize an Amazon GameLift Servers API client.
    * Implement callback functions to respond to requests from the Amazon GameLift Servers
     service, including `OnStartGameSession`,
     `OnProcessTerminate`, and
     `onHealthCheck`.
    * Call `ProcessReady()` to notify the Amazon GameLift Servers service when
     ready to host game sessions.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#include "GameLiftUnrealAppGameMode.h"

#include "UObject/ConstructorHelpers.h"
#include "Kismet/GameplayStatics.h"

#if WITH_GAMELIFT
#include "GameLiftServerSDK.h"
#include "GameLiftServerSDKModels.h"
#endif

#include "GenericPlatform/GenericPlatformOutputDevices.h"

DEFINE_LOG_CATEGORY(GameServerLog);

AGameLiftUnrealAppGameMode::AGameLiftUnrealAppGameMode() :
    ProcessParameters(nullptr)
{
    // Set default pawn class to our Blueprinted character
    static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter"));

    if (PlayerPawnBPClass.Class != NULL)
    {
        DefaultPawnClass = PlayerPawnBPClass.Class;
    }

    UE_LOG(GameServerLog, Log, TEXT("Initializing AGameLiftUnrealAppGameMode..."));
}

void AGameLiftUnrealAppGameMode::BeginPlay()
{
    Super::BeginPlay();

#if WITH_GAMELIFT
    InitGameLift();
#endif
}

void AGameLiftUnrealAppGameMode::InitGameLift()
{
#if WITH_GAMELIFT
    UE_LOG(GameServerLog, Log, TEXT("Calling InitGameLift..."));

    // Getting the module first.
    FGameLiftServerSDKModule* GameLiftSdkModule = &FModuleManager::LoadModuleChecked<FGameLiftServerSDKModule>(FName("GameLiftServerSDK"));

    //Define the server parameters for a GameLift Anywhere fleet. These are not needed for a GameLift managed EC2 fleet.
    FServerParameters ServerParametersForAnywhere;

    bool bIsAnywhereActive = false;
    if (FParse::Param(FCommandLine::Get(), TEXT("glAnywhere")))
    {
        bIsAnywhereActive = true;
    }

    if (bIsAnywhereActive)
    {
        UE_LOG(GameServerLog, Log, TEXT("Configuring server parameters for Anywhere..."));

        // If GameLift Anywhere is enabled, parse command line arguments and pass them in the ServerParameters object.
        FString glAnywhereWebSocketUrl = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereWebSocketUrl="), glAnywhereWebSocketUrl))
        {
            ServerParametersForAnywhere.m_webSocketUrl = TCHAR_TO_UTF8(*glAnywhereWebSocketUrl);
        }

        FString glAnywhereFleetId = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereFleetId="), glAnywhereFleetId))
        {
            ServerParametersForAnywhere.m_fleetId = TCHAR_TO_UTF8(*glAnywhereFleetId);
        }

        FString glAnywhereProcessId = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereProcessId="), glAnywhereProcessId))
        {
            ServerParametersForAnywhere.m_processId = TCHAR_TO_UTF8(*glAnywhereProcessId);
        }
        else
        {
            // If no ProcessId is passed as a command line argument, generate a randomized unique string.
            FString TimeString = FString::FromInt(std::time(nullptr));
            FString ProcessId = "ProcessId_" + TimeString;
            ServerParametersForAnywhere.m_processId = TCHAR_TO_UTF8(*ProcessId);
        }

        FString glAnywhereHostId = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereHostId="), glAnywhereHostId))
        {
            ServerParametersForAnywhere.m_hostId = TCHAR_TO_UTF8(*glAnywhereHostId);
        }

        FString glAnywhereAuthToken = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereAuthToken="), glAnywhereAuthToken))
        {
            ServerParametersForAnywhere.m_authToken = TCHAR_TO_UTF8(*glAnywhereAuthToken);
        }

        FString glAnywhereAwsRegion = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereAwsRegion="), glAnywhereAwsRegion))
        {
            ServerParametersForAnywhere.m_awsRegion = TCHAR_TO_UTF8(*glAnywhereAwsRegion);
        }

        FString glAnywhereAccessKey = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereAccessKey="), glAnywhereAccessKey))
        {
            ServerParametersForAnywhere.m_accessKey = TCHAR_TO_UTF8(*glAnywhereAccessKey);
        }

        FString glAnywhereSecretKey = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereSecretKey="), glAnywhereSecretKey))
        {
            ServerParametersForAnywhere.m_secretKey = TCHAR_TO_UTF8(*glAnywhereSecretKey);
        }

        FString glAnywhereSessionToken = "";
        if (FParse::Value(FCommandLine::Get(), TEXT("glAnywhereSessionToken="), glAnywhereSessionToken))
        {
            ServerParametersForAnywhere.m_sessionToken = TCHAR_TO_UTF8(*glAnywhereSessionToken);
        }

        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_YELLOW);
        UE_LOG(GameServerLog, Log, TEXT(">>>> WebSocket URL: %s"), *ServerParametersForAnywhere.m_webSocketUrl);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Fleet ID: %s"), *ServerParametersForAnywhere.m_fleetId);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Process ID: %s"), *ServerParametersForAnywhere.m_processId);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Host ID (Compute Name): %s"), *ServerParametersForAnywhere.m_hostId);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Auth Token: %s"), *ServerParametersForAnywhere.m_authToken);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Aws Region: %s"), *ServerParametersForAnywhere.m_awsRegion);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Access Key: %s"), *ServerParametersForAnywhere.m_accessKey);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Secret Key: %s"), *ServerParametersForAnywhere.m_secretKey);
        UE_LOG(GameServerLog, Log, TEXT(">>>> Session Token: %s"), *ServerParametersForAnywhere.m_sessionToken);
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_NONE);
    }

    UE_LOG(GameServerLog, Log, TEXT("Initializing the GameLift Server..."));

    //InitSDK will establish a local connection with GameLift's agent to enable further communication.
    FGameLiftGenericOutcome InitSdkOutcome = GameLiftSdkModule->InitSDK(ServerParametersForAnywhere);
    if (InitSdkOutcome.IsSuccess())
    {
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_GREEN);
        UE_LOG(GameServerLog, Log, TEXT("GameLift InitSDK succeeded!"));
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_NONE);
    }
    else
    {
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_RED);
        UE_LOG(GameServerLog, Log, TEXT("ERROR: InitSDK failed : ("));
        FGameLiftError GameLiftError = InitSdkOutcome.GetError();
        UE_LOG(GameServerLog, Log, TEXT("ERROR: %s"), *GameLiftError.m_errorMessage);
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_NONE);
        return;
    }

    ProcessParameters = MakeShared<FProcessParameters>();

    //When a game session is created, Amazon GameLift Servers sends an activation request to the game server and passes along the game session object containing game properties and other settings.
    //Here is where a game server should take action based on the game session object.
    //Once the game server is ready to receive incoming player connections, it should invoke GameLiftServerAPI.ActivateGameSession()
    ProcessParameters->OnStartGameSession.BindLambda([=](Aws::GameLift::Server::Model::GameSession InGameSession)
        {
            FString GameSessionId = FString(InGameSession.GetGameSessionId());
            UE_LOG(GameServerLog, Log, TEXT("GameSession Initializing: %s"), *GameSessionId);
            GameLiftSdkModule->ActivateGameSession();
        });

    //OnProcessTerminate callback. Amazon GameLift Servers will invoke this callback before shutting down an instance hosting this game server.
    //It gives this game server a chance to save its state, communicate with services, etc., before being shut down.
    //In this case, we simply tell Amazon GameLift Servers we are indeed going to shutdown.
    ProcessParameters->OnTerminate.BindLambda([=]()
        {
            UE_LOG(GameServerLog, Log, TEXT("Game Server Process is terminating"));
            // First call ProcessEnding()
            FGameLiftGenericOutcome processEndingOutcome = GameLiftSdkModule->ProcessEnding();
            // Then call Destroy() to free the SDK from memory
            FGameLiftGenericOutcome destroyOutcome = GameLiftSdkModule->Destroy();
            // Exit the process with success or failure
            if (processEndingOutcome.IsSuccess() && destroyOutcome.IsSuccess()) {
                UE_LOG(GameServerLog, Log, TEXT("Server process ending successfully"));
            }
            else {
                if (!processEndingOutcome.IsSuccess()) {
                    const FGameLiftError& error = processEndingOutcome.GetError();
                    UE_LOG(GameServerLog, Error, TEXT("ProcessEnding() failed. Error: %s"),
                    error.m_errorMessage.IsEmpty() ? TEXT("Unknown error") : *error.m_errorMessage);
                }
                if (!destroyOutcome.IsSuccess()) {
                    const FGameLiftError& error = destroyOutcome.GetError();
                    UE_LOG(GameServerLog, Error, TEXT("Destroy() failed. Error: %s"),
                    error.m_errorMessage.IsEmpty() ? TEXT("Unknown error") : *error.m_errorMessage);
                }
            }
        });

    //This is the HealthCheck callback.
    //Amazon GameLift Servers will invoke this callback every 60 seconds or so.
    //Here, a game server might want to check the health of dependencies and such.
    //Simply return true if healthy, false otherwise.
    //The game server has 60 seconds to respond with its health status. Amazon GameLift Servers will default to 'false' if the game server doesn't respond in time.
    //In this case, we're always healthy!
    ProcessParameters->OnHealthCheck.BindLambda([]()
        {
            UE_LOG(GameServerLog, Log, TEXT("Performing Health Check"));
            return true;
        });

    //GameServer.exe -port=7777 LOG=server.mylog
    ProcessParameters->port = FURL::UrlConfig.DefaultPort;
    TArray<FString> CommandLineTokens;
    TArray<FString> CommandLineSwitches;

    FCommandLine::Parse(FCommandLine::Get(), CommandLineTokens, CommandLineSwitches);

    for (FString SwitchStr : CommandLineSwitches)
    {
        FString Key;
        FString Value;

        if (SwitchStr.Split("=", &Key, &Value))
        {
            if (Key.Equals("port"))
            {
                ProcessParameters->port = FCString::Atoi(*Value);
            }
        }
    }

    //Here, the game server tells Amazon GameLift Servers where to find game session log files.
    //At the end of a game session, Amazon GameLift Servers uploads everything in the specified
    //location and stores it in the cloud for access later.
    TArray<FString> Logfiles;
    Logfiles.Add(TEXT("GameLiftUnrealApp/Saved/Logs/server.log"));
    ProcessParameters->logParameters = Logfiles;

    //The game server calls ProcessReady() to tell Amazon GameLift Servers it's ready to host game sessions.
    UE_LOG(GameServerLog, Log, TEXT("Calling Process Ready..."));
    FGameLiftGenericOutcome ProcessReadyOutcome = GameLiftSdkModule->ProcessReady(*ProcessParameters);

    if (ProcessReadyOutcome.IsSuccess())
    {
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_GREEN);
        UE_LOG(GameServerLog, Log, TEXT("Process Ready!"));
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_NONE);
    }
    else
    {
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_RED);
        UE_LOG(GameServerLog, Log, TEXT("ERROR: Process Ready Failed!"));
        FGameLiftError ProcessReadyError = ProcessReadyOutcome.GetError();
        UE_LOG(GameServerLog, Log, TEXT("ERROR: %s"), *ProcessReadyError.m_errorMessage);
        UE_LOG(GameServerLog, SetColor, TEXT("%s"), COLOR_NONE);
    }

    UE_LOG(GameServerLog, Log, TEXT("InitGameLift completed!"));
#endif
}
```

###### Step 3: Rebuild the game project

- Build game project for both of the following target types:
  _Development Editor_ and _Development
  Server_.

###### Note

You don't need to rebuild the solution. Instead, build the project under
the `/Games/` folder for your app. Otherwise, Visual
Studio will rebuild the entire UE5 project, which can take up to an
hour.

## Package your game server for

hosting

With your game server code now integrated with the minimum required server SDK
functionality, you're ready to package your game server build using the Unreal Editor.

###### To package the game server build

1.  Open the game project in the Unreal Editor.
2.  Follow the Unreal Editor steps to package your game server:

        * Choose your target platform (Windows or Linux).
        * Select your server build target (``[your
         application name]`Server`.

    The packaging process generates your game server executable:
    ``[your application
 name]`Server.exe`.

3.  Prepare your game server build for deployment to hosting resources. The build
    should include the following files:
    - Your game server executable
    - If you're using Unreal Engine version 5.5 or older, include the
      following files for Windows builds. You can find them in your
      source-built version of the Unreal Engine:
      - `VC_redist.x64.exe`
        (`UnrealEngine\Engine\Source\Programs\PrereqInstaller\Resources\VCRedist\`)
      - `UEPrereqSetup_x64.exe or
UE5PrereqSetup_x64.exe`
        (`UnrealEngine\Engine\Extras\Redist\en-us\`)

    - All other required dependencies for your game server.
    - OpenSSL libraries, if needed. You can skip this step if your game
      server is integrated with Amazon GameLift Servers server SDK version 5.3 or later. [The latest server SDK version is available here.](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal "https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal")

You must include the same version of OpenSSL libraries that were used when packaging the game server in Unreal. These libraries are
located in your game engine source. The location varies depending on your development environment:

On Windows:

- `[ENGINE_ROOT_DIR]\Engine\Extras\ThirdPartyNotUE\libimobiledevice\x64\libssl-1_1-x64.dll`
- `[ENGINE_ROOT_DIR]\Engine\Extras\ThirdPartyNotUE\libimobiledevice\x64\libcrypto-1_1-x64.dll`
  On Linux:

- `Engine/Source/Thirdparty/OpenSSL/1.1.1*n*/include/libssl.so.1.1`
- `Engine/Source/Thirdparty/OpenSSL/1.1.1*n*/include/libcrypto.so.1.1`
  Copy the OpenSSL libraries to your game build
  package in the same directory as the game server executable file.

## Next steps

Now that you've prepared a game server build with the minimum required functionality
for hosting with Amazon GameLift Servers, consider these potential next steps:

- Deploy your integrated game server for and testing and development. With an Anywhere fleet, you can set up your local machine
  as a hosting resource and use it to test your game server and game client connections. For cloud-based hosting,
  deploy your game server to a managed EC2 or managed container fleet. See these topics for guidance:
  - [Set up for iterative development with Amazon GameLift Servers Anywhere](integration-dev-iteration.md "integration-dev-iteration.md")
  - [Amazon GameLift Servers Anywhere fleets](fleets-intro-anywhere.md "fleets-intro-anywhere.md")
  - [Amazon GameLift Servers managed EC2 fleets](fleets-intro-managed.md "fleets-intro-managed.md")
  - [Amazon GameLift Servers managed container fleets](fleets-intro-containers.md "fleets-intro-containers.md")

- Customize your game server integration by adding optional features. For example, you might want to add player sessions with unique player IDs, set up
  matchmaking backfill, or manage game server access to your other AWS resources (such as a database or content storage service). See these topics for guidance:
  - [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md")
  - [C++ (Unreal) server SDK 5.x for
    Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")

- Customize your game client component to request game sessions, receive connection information, and connect directly to a game server to play a game.
  See these topics for guidance:
  - [Integrate your game client
    withAmazon GameLift Servers](gamelift-sdk-client.md "gamelift-sdk-client.md")
