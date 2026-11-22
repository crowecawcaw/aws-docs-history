

# Code Interpreter API Reference Examples

This section provides reference examples for common Code Interpreter operations using different approaches. Each example shows how to perform the same operation using AWS CLI, Boto3 SDK, and direct API calls.

## Code Execution
<a name="code-interpreter-api-code-execution"></a>

These examples demonstrate how to execute code in a Code Interpreter session.

**Example**  

1. 

   ```python
   params = {
         "language": "python",
         "code": "print(\"Hello, world!\")"
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "executeCode",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "executeCode",
       "arguments": {
         "language": "python",
         "code": "print(\"Hello, world!\")"
       }
     }'
   ```

## Terminal Commands
<a name="code-interpreter-api-terminal-commands"></a>

These examples demonstrate how to execute terminal commands in a Code Interpreter session.

### Execute Command
<a name="code-interpreter-api-execute-command"></a>

**Example**  

1. 

   ```python
   params = {
         "command": "ls -l"
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "executeCommand",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "executeCommand",
       "arguments": {
         "command": "ls -l"
       }
     }'
   ```

### Start Command Execution
<a name="code-interpreter-api-start-command"></a>

**Example**  

1. 

   ```python
   params = {
         "command": "sleep 15 && echo Task completed successfully"
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "startCommandExecution",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "startCommandExecution",
       "arguments": {
         "command": "sleep 15 && echo Task completed successfully"
       }
     }'
   ```

### Get Task
<a name="code-interpreter-api-get-task"></a>

**Example**  

1. 

   ```python
   params = {
         "taskId": "<your-task-id>"
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "getTask",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "getTask",
       "arguments": {
         "taskId": "<your-task-id>"
       }
     }'
   ```

### Stop Command Execution Task
<a name="code-interpreter-api-stop-task"></a>

**Example**  

1. 

   ```python
   params = {
         "taskId": "<your-task-id>"
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "stopTask",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "stopTask",
       "arguments": {
         "taskId": "<your-task-id>"
       }
     }'
   ```

## File Management
<a name="code-interpreter-api-file-management"></a>

These examples demonstrate how to manage files in a Code Interpreter session.

### Write Files
<a name="code-interpreter-api-write-files"></a>

**Example**  

1. 

   ```python
   params = {
           "content": [{"path": "dir1/samename.txt", "text": "File in dir1"}]
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "writeFiles",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "writeFiles",
       "arguments": {
         "content": [{"path": "dir1/samename.txt", "text": "File in dir1"}]
       }
     }'
   ```

### Read Files
<a name="code-interpreter-api-read-files"></a>

**Example**  

1. 

   ```python
   params = {
         "paths": ["tmp.txt"]
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "readFiles",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "readFiles",
       "arguments": {
         "paths": ["tmp.txt"]
       }
     }'
   ```

### Remove Files
<a name="code-interpreter-api-remove-files"></a>

**Example**  

1. 

   ```python
   params = {
         "paths": ["tmp.txt"]
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "removeFiles",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "removeFiles",
       "arguments": {
         "paths": ["tmp.txt"]
       }
     }'
   ```

### List Files
<a name="code-interpreter-api-list-files"></a>

**Example**  

1. 

   ```python
   params = {
         "directoryPath": ""
       }
   
   client.invoke_code_interpreter(
       **{
           "codeInterpreterIdentifier": "aws.codeinterpreter.v1",
           "sessionId": "<your-session-id>",
           "name": "listFiles",
           "arguments": params
       })
   ```

1. 

   ```bash
   # Using awscurl
   awscurl -X POST \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/tools/invoke" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "x-amzn-code-interpreter-session-id: your-session-id" \
     --service bedrock-agentcore \
     --region <Region> \
     -d '{
       "name": "listFiles",
       "arguments": {
         "directoryPath": ""
       }
     }'
   ```