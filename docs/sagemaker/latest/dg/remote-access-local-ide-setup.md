

# Set up Remote IDE
<a name="remote-access-local-ide-setup"></a>

After administrators complete the instructions in [Connect your Remote IDE to SageMaker spaces with remote access](remote-access.md), you can connect your Remote IDE to your remote SageMaker spaces.

**Topics**
+ [Set up your local environment](#remote-access-local-ide-setup-local-environment)
+ [Connect to your Remote IDE](#remote-access-local-ide-setup-local-vs-code)
+ [Connect to VPC with subnets without internet access](remote-access-local-ide-setup-vpc-no-internet.md)
+ [Filter your Studio spaces](remote-access-local-ide-setup-filter.md)

## Set up your local environment
<a name="remote-access-local-ide-setup-local-environment"></a>

Install your preferred Remote IDE on your local machine:
+ [Visual Studio Code](https://code.visualstudio.com/)
+ [Kiro](https://kiro.dev/)
+ [Cursor](https://cursor.com/home)

For information on the version requirements, see [IDE version requirements](remote-access.md#remote-access-ide-version-requirements).

## Connect to your Remote IDE
<a name="remote-access-local-ide-setup-local-vs-code"></a>

Before you can establish a connection from your Remote IDE to your remote SageMaker spaces, your administrator must [Set up remote access](remote-access-remote-setup.md). Your administrator sets up a specific method for you to establish a connection. Choose the method that was set up for you.

**Topics**
+ [Method 1: Deep link from Studio UI](#remote-access-local-ide-setup-local-vs-code-method-1-deep-link-from-studio-ui)
+ [Method 2: AWS Toolkit in the Remote IDE](#remote-access-local-ide-setup-local-vs-code-method-2-aws-toolkit-in-vs-code)
+ [Method 3: Connect from the terminal via SSH CLI](#remote-access-local-ide-setup-local-vs-code-method-3-connect-from-the-terminal-via-ssh-cli)

### Method 1: Deep link from Studio UI
<a name="remote-access-local-ide-setup-local-vs-code-method-1-deep-link-from-studio-ui"></a>

Use the following procedure to establish a connection using deep link.

1. [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html#studio-updated-launch-console).

1. In the Studio UI, navigate to your space.

1. Choose **Open in VS Code**, **Open in Kiro**, or **Open in Cursor** button for your preferred IDE. Ensure that your preferred IDE is already installed on your local computer.

1. When prompted, confirm to open your IDE. Your IDE opens with another pop-up to confirm. Once completed, the remote connection is established.

### Method 2: AWS Toolkit in the Remote IDE
<a name="remote-access-local-ide-setup-local-vs-code-method-2-aws-toolkit-in-vs-code"></a>

Use the following procedure to establish a connection using the AWS Toolkit for Visual Studio Code. This method is available for VS Code, Kiro, and Cursor.

1. Open your Remote IDE (VS Code, Kiro, or Cursor).

1. Open the AWS Toolkit extension.

1. [Connect to AWS](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html).

1. In the AWS Explorer, expand **SageMaker AI**, then expand **Studio**.

1. Find your Studio space.

1. Choose the **Connect** icon next to your space to start it.
**Note**  
Stop and restart the space in the Toolkit for Visual Studio to enable remote access, if not already connected.
If the space is not using a supported [instance size](https://docs.aws.amazon.com/sagemaker/latest/dg/remote-access.html#remote-access-instance-requirements), you will be asked to change the instance.

### Method 3: Connect from the terminal via SSH CLI
<a name="remote-access-local-ide-setup-local-vs-code-method-3-connect-from-the-terminal-via-ssh-cli"></a>

Choose one of the following platform options to view the procedure to establish a connection using the SSH CLI.

**Note**  
Ensure that you have the latest versions of the [Local machine prerequisites](remote-access.md#remote-access-local-prerequisites) installed before following the instructions below.
If you [Bring your own image (BYOI)](studio-updated-byoi.md), ensure you have installed the required dependencies listed in [Image requirements](remote-access.md#remote-access-image-requirements) before proceeding

------
#### [ Linux/macOS ]

Create a shell script (for example, `/home/user/sagemaker_connect.sh`):

```
#!/bin/bash
# Disable the -x option if printing each command is not needed.
set -exuo pipefail

SPACE_ARN="$1"
AWS_PROFILE="${2:-}"

# Validate ARN and extract region
if [[ "$SPACE_ARN" =~ ^arn:aws[-a-z]*:sagemaker:([a-z0-9-]+):[0-9]{12}:space\/[^\/]+\/[^\/]+$ ]]; then
    AWS_REGION="${BASH_REMATCH[1]}"
else
    echo "Error: Invalid SageMaker Studio Space ARN format."
    exit 1
fi

# Optional profile flag
PROFILE_ARG=()
if [[ -n "$AWS_PROFILE" ]]; then
    PROFILE_ARG=(--profile "$AWS_PROFILE")
fi

# Start session
START_SESSION_JSON=$(aws sagemaker start-session \
    --resource-identifier "$SPACE_ARN" \
    --region "${AWS_REGION}" \
    "${PROFILE_ARG[@]}")

# Extract fields using grep and sed
SESSION_ID=$(echo "$START_SESSION_JSON" | grep -o '"SessionId": "[^"]*"' | sed 's/.*: "//;s/"$//')
STREAM_URL=$(echo "$START_SESSION_JSON" | grep -o '"StreamUrl": "[^"]*"' | sed 's/.*: "//;s/"$//')
TOKEN=$(echo "$START_SESSION_JSON" | grep -o '"TokenValue": "[^"]*"' | sed 's/.*: "//;s/"$//')

# Validate extracted values
if [[ -z "$SESSION_ID" || -z "$STREAM_URL" || -z "$TOKEN" ]]; then
    echo "Error: Failed to extract session information from sagemaker start session response."
    exit 1
fi

# Call session-manager-plugin
session-manager-plugin \
    "{\"streamUrl\":\"$STREAM_URL\",\"tokenValue\":\"$TOKEN\",\"sessionId\":\"$SESSION_ID\"}" \
    "$AWS_REGION" "StartSession"
```

1. Make the script executable:

   ```
   chmod +x /home/user/sagemaker_connect.sh
   ```

1. Configure `$HOME/.ssh/config` to add the following entry:

```
Host {{space-name}}
  HostName 'arn:{{PARTITION}}:sagemaker:{{us-east-1}}:{{111122223333}}:space/{{domain-id}}/{{space-name}}'
  ProxyCommand '/home/user/sagemaker_connect.sh' '%h'
  ForwardAgent yes
  AddKeysToAgent yes
  StrictHostKeyChecking accept-new
```

For example, the `{{PARTITION}}` can be `aws`.

If you need to use a [named AWS credential profile](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-configure-files-using-profiles), change the proxy command as follows:

```
  ProxyCommand '/home/user/sagemaker_connect.sh' '%h' {{YOUR_CREDENTIAL_PROFILE_NAME}}
```
+ Connect via SSH or run SCP command:

```
ssh {{space-name}}
scp file_abc {{space-name}}:/tmp/
```

------
#### [ Windows ]

**Prerequisites for Windows:**
+ PowerShell 5.1 or later
+ SSH client (OpenSSH recommended)

Create a PowerShell script (for example, `C:\Users\{{user-name}}\sagemaker_connect.ps1`):

```
# sagemaker_connect.ps1
param(
    [Parameter(Mandatory=$true)]
    [string]$SpaceArn,

    [Parameter(Mandatory=$false)]
    [string]$AwsProfile = ""
)

# Enable error handling
$ErrorActionPreference = "Stop"

# Validate ARN and extract region
if ($SpaceArn -match "^arn:aws[-a-z]*:sagemaker:([a-z0-9-]+):[0-9]{12}:space\/[^\/]+\/[^\/]+$") {
    $AwsRegion = $Matches[1]
} else {
    Write-Error "Error: Invalid SageMaker Studio Space ARN format."
    exit 1
}

# Build AWS CLI command
$awsCommand = @("sagemaker", "start-session", "--resource-identifier", $SpaceArn, "--region", $AwsRegion)

if ($AwsProfile) {
    $awsCommand += @("--profile", $AwsProfile)
}

try {
    # Start session and capture output
    Write-Host "Starting SageMaker session..." -ForegroundColor Green
    $startSessionOutput = & aws @awsCommand

    # Try to parse JSON response
    try {
        $sessionData = $startSessionOutput | ConvertFrom-Json
    } catch {
        Write-Error "Failed to parse JSON response: $_"
        Write-Host "Raw response was:" -ForegroundColor Yellow
        Write-Host $startSessionOutput
        exit 1
    }

    $sessionId = $sessionData.SessionId
    $streamUrl = $sessionData.StreamUrl
    $token = $sessionData.TokenValue

    # Validate extracted values
    if (-not $sessionId -or -not $streamUrl -or -not $token) {
        Write-Error "Error: Failed to extract session information from sagemaker start session response."
        Write-Host "Parsed response was:" -ForegroundColor Yellow
        Write-Host ($sessionData | ConvertTo-Json)
        exit 1
    }

    Write-Host "Session started successfully. Connecting..." -ForegroundColor Green

    # Create session manager plugin command
    $sessionJson = @{
        streamUrl = $streamUrl
        tokenValue = $token
        sessionId = $sessionId
    } | ConvertTo-Json -Compress

    # Escape the JSON string
    $escapedJson = $sessionJson -replace '"', '\"'

    # Call session-manager-plugin
    & session-manager-plugin "$escapedJson" $AwsRegion "StartSession"

} catch {
    Write-Error "Failed to start session: $_"
    exit 1
}
```
+ Configure `C:\Users\{{user-name}}\.ssh\config` to add the following entry:

```
Host {{space-name}}                            
  HostName "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:space/{{domain-id}}/{{space-name}}"
  ProxyCommand "C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy RemoteSigned -File "C:\\Users\\{{user-name}}\\sagemaker_connect.ps1" "%h"
  ForwardAgent yes
  AddKeysToAgent yes
  User sagemaker-user
  StrictHostKeyChecking accept-new
```

------