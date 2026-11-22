

# Install an SDK

Anthropic’s [client SDKs](https://platform.claude.com/docs/en/api/client-sdks) support Claude Platform on AWS. All seven SDKs provide a platform-specific client class; alternatively, you can configure the base client with the Claude Platform on AWS base URL.

 **Python** 

```bash
pip install -U "anthropic[aws]"
```

**Tip**  
On macOS with Homebrew Python or other externally managed Python environments, `pip install` may fail with a PEP 668 `externally-managed-environment` error. Create and activate a virtual environment first: `python3 -m venv .venv && source .venv/bin/activate`.

 **TypeScript** 

```bash
npm install @anthropic-ai/aws-sdk
```

 **C\#** 

```bash
dotnet add package Anthropic.Aws
```

 **Go** 

```bash
go get github.com/anthropics/anthropic-sdk-go
```

 **Java** 

```kotlin
implementation("com.anthropic:anthropic-java-aws:2.27.0")
```

```xml
<dependency>
  <groupId>com.anthropic</groupId>
  <artifactId>anthropic-java-aws</artifactId>
  <version>2.27.0</version>
</dependency>
```

 **PHP** 

```bash
composer require anthropic-ai/sdk aws/aws-sdk-php
```

 **Ruby** 

```bash
gem install anthropic aws-sdk-core
```

**Note**  
SDK clients for Claude Platform on AWS are in beta.