# Plugin for Unreal: Integrate your game code

Before you can deploy your game server to a fleet, you need to make a series of
updates to game code and package game components for use with the Amazon GameLift Servers service.

This topic walks through the steps for doing a minimal integration. For server
integration, use the provided code sample to update your project's game mode.

- [Set up build targets and module rules](#unreal-plugin-anywhere-integrate-setup "#unreal-plugin-anywhere-integrate-setup")
- [Update your game server
  code](#unreal-plugin-anywhere-integrate-simple-server "#unreal-plugin-anywhere-integrate-simple-server")
- [Integrate your client game map](#unreal-plugin-anywhere-integrate-simple-client "#unreal-plugin-anywhere-integrate-simple-client")
- [Package your game components](#unreal-plugin-anywhere-integrate-build "#unreal-plugin-anywhere-integrate-build")

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

## Update your game server

code

Update your game server code to enable communication between a game server
process and the Amazon GameLift Servers service. Your game server must be able to respond to requests
from Amazon GameLift Servers, such as to start and stop new game sessions.

###### To add server code for Amazon GameLift Servers

1. In your code editor, open the solution (`.sln`) file for your game project, usually
   found in the project root folder. For example:
   `GameLiftUnrealApp.sln`.
2. With the solution open, locate the project game mode header file:
   `[project-name]GameMode.h` file. For example:
   `GameLiftUnrealAppGameMode.h`.
3. Change the header file to align with the following code. Be sure to replace
   "GameLiftServer" with your own project name. These updates are
   specific to the game server; we recommend that you make a backup
   copy of the original game mode files for use with your
   client.

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

- Open the related source file `[project-name]GameMode.cpp` file (for example
  `GameLiftUnrealAppGameMode.cpp`). Change the code to
  align with the following example code. Be sure to replace
  "GameLiftUnrealApp" with your own project name. These updates are
  specific to the game server; we recommend that you make a backup
  copy of the original file for use with your client.

The following example code shows how to add the minimum required elements for server integration with Amazon GameLift Servers:

    + Initialize an Amazon GameLift Servers API client. The `InitSDK()` call with server
     parameters is required for an Amazon GameLift Servers Anywhere
     fleet. When you connect to an Anywhere fleet, the plugin
     stores the server parameters as console arguments The sample
     code can access the values at runtime.
    + Implement required callback functions to respond to requests from the Amazon GameLift Servers service,
     including `OnStartGameSession`,
     `OnProcessTerminate`, and
     `onHealthCheck`.
    + Call `ProcessReady()` with a designated port to notify the Amazon GameLift Servers service
     when ready to host game sessions.

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

## Integrate your client game map

The startup game map contains blueprint logic and UI elements that already
include basic code to request game sessions and use connection information
to connect to a game session. You can use the map as is or modify these as
needed. Use the startup game map with other game assets, such as the Third Person
template project provided by Unreal Engine. These assets are available in
Content Browser. You can use them to test the plugin's deployment workflows,
or as a guide to create a custom backend service for your game.

The startup map has the following characteristics:

- It includes logic for both an Anywhere fleet and a managed EC2 fleet. When you run your
  client, you can choose to connect to either fleet.
- Client functionality includes find a game session (`SearchGameSessions()`), create
  a new game session (`CreateGameSession()`), and join a game
  session directly.
- It gets a unique player ID from your project's Amazon Cognito user pool (this is part of a
  deployed Anywhere solution).

###### To use the startup game map

1. In the UE editor, open the **Project Settings, Maps & Modes** page, and
   expand the **Default Maps** section.
2. For **Editor Startup Map**, select "StartupMap" from the dropdown list. You
   might need to search for the file, which is located in `... >
Unreal Projects/[project-name]/Plugins/Amazon GameLift Servers Plugin
Content/Maps`.
3. For **Game Default Map**, select the same "StartupMap" from the dropdown
   list.
4. For **Server Default Map**, select "ThirdPersonMap". This is a default map
   included in your game project. This map is designed for two players
   in the game.
5. Open the details panel for the server default map. Set **GameMode Override**
   to "None".
6. Expand the **Default Modes** section, and set **Global Default Server
   Game Mode** to the game mode you updated for your
   server integration.

After you've made these changes to your project, you're ready to build your game components.

## Package your game components

###### To package your game server and game client builds

1. Open your game project in a source-built version of the Unreal Engine editor.
2. Use the editor to package your game client and server builds.
   1. Choose a target. Go to **Platforms, Windows** and select one of the
      following:
      - Server: `[your-application-name]Server`
      - Client: `[your-application-name]Client`

   2. Start the build. Go to **Platform, Windows, Package Project**.

Each packaging process generates an executable:
`[your-application-name]Client.exe` or
`[your-application-name]Server.exe`.

In the plugin, set the paths to the client and server build executables on your local workstation.
