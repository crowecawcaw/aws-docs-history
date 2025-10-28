# Enable Application Signals on Amazon ECS using AWS CDK

To enable Application Signals on Amazon ECS using AWS CDK, do the following.

1. Enable Application Signals for your applications – If you haven't enabled Application Signals in this account yet, you must grant Application
   Signals the permissions it needs to discover your services.

```
import { aws_applicationsignals as applicationsignals } from 'aws-cdk-lib';

const cfnDiscovery = new applicationsignals.CfnDiscovery(this,
  'ApplicationSignalsServiceRole', { }
);
```

The Discovery CloudFormation resource grants Application Signals the following permissions:

    * `xray:GetServiceGraph`
    * `logs:StartQuery`
    * `logs:GetQueryResults`
    * `cloudwatch:GetMetricData`
    * `cloudwatch:ListMetrics`
    * `tag:GetResources`

For more information about this role, see
[Service-linked role permissions for
CloudWatch Application Signals](using-service-linked-roles.md#service-linked-role-signals "using-service-linked-roles.md#service-linked-role-signals"). 2. Instrument your application with the [AWS::ApplicationSignals Construct Library](https://www.npmjs.com/package/@aws-cdk/aws-applicationsignals-alpha "https://www.npmjs.com/package/@aws-cdk/aws-applicationsignals-alpha") in the AWS CDK. The code snippets in this document are provided in _TypeScript_.
For other language-specific alternatives, see [Supported programming languages for the AWS CDK](../../../cdk/v2/guide/languages.md "../../../cdk/v2/guide/languages.md").

    * **Enable Application Signals on Amazon ECS with sidecar mode**


    	1. Configure `instrumentation` to instrument the application with the AWS Distro for OpenTelemetry (ADOT) SDK Agent. The following is an example of instrumenting a Java application.
    	 See [InstrumentationVersion](../../../cdk/api/v2/docs/@aws-cdk_aws-applicationsignals-alpha.md "../../../cdk/api/v2/docs/@aws-cdk_aws-applicationsignals-alpha.md") for all supported language versions.
    	2. Specify `cloudWatchAgentSidecar` to configure the CloudWatch Agent as a sidecar container.



    	```
    	import { Construct } from 'constructs';
    	import * as appsignals from '@aws-cdk/aws-applicationsignals-alpha';
    	import * as cdk from 'aws-cdk-lib';
    	import * as ec2 from 'aws-cdk-lib/aws-ec2';
    	import * as ecs from 'aws-cdk-lib/aws-ecs';

    	class MyStack extends cdk.Stack {
    	  public constructor(scope?: Construct, id?: string, props: cdk.StackProps = {}) {
    	    super();
    	    const vpc = new ec2.Vpc(this, 'TestVpc', {});
    	    const cluster = new ecs.Cluster(this, 'TestCluster', { vpc });

    	    const fargateTaskDefinition = new ecs.FargateTaskDefinition(this, 'SampleAppTaskDefinition', {
    	      cpu: 2048,
    	      memoryLimitMiB: 4096,
    	    });

    	    fargateTaskDefinition.addContainer('app', {
    	      image: ecs.ContainerImage.fromRegistry('test/sample-app'),
    	    });

    	    new appsignals.ApplicationSignalsIntegration(this, 'ApplicationSignalsIntegration', {
    	      taskDefinition: fargateTaskDefinition,
    	      instrumentation: {
    	        sdkVersion: appsignals.JavaInstrumentationVersion.V2_10_0,
    	      },
    	      serviceName: 'sample-app',
    	      cloudWatchAgentSidecar: {
    	        containerName: 'ecs-cwagent',
    	        enableLogging: true,
    	        cpu: 256,
    	        memoryLimitMiB: 512,
    	      }
    	    });

    	    new ecs.FargateService(this, 'MySampleApp', {
    	      cluster: cluster,
    	      taskDefinition: fargateTaskDefinition,
    	      desiredCount: 1,
    	    });
    	  }
    	}
    	```
    * **Enable Application Signals on Amazon ECS with daemon mode**


    ###### Note

    The daemon deployment strategy is not supported on Amazon ECS Fargate and is only supported on Amazon ECS on Amazon EC2.


    	1. Run CloudWatch Agent as a daemon service with `HOST` network mode.
    	2. Configure `instrumentation` to instrument the application with the ADOT Python Agent.



    	```
    	import { Construct } from 'constructs';
    	import * as appsignals from '@aws-cdk/aws-applicationsignals-alpha';
    	import * as cdk from 'aws-cdk-lib';
    	import * as ec2 from 'aws-cdk-lib/aws-ec2';
    	import * as ecs from 'aws-cdk-lib/aws-ecs';

    	class MyStack extends cdk.Stack {
    	  public constructor(scope?: Construct, id?: string, props: cdk.StackProps = {}) {
    	    super(scope, id, props);

    	    const vpc = new ec2.Vpc(this, 'TestVpc', {});
    	    const cluster = new ecs.Cluster(this, 'TestCluster', { vpc });

    	    // Define Task Definition for CloudWatch agent (Daemon)
    	    const cwAgentTaskDefinition = new ecs.Ec2TaskDefinition(this, 'CloudWatchAgentTaskDefinition', {
    	      networkMode: ecs.NetworkMode.HOST,
    	    });

    	    new appsignals.CloudWatchAgentIntegration(this, 'CloudWatchAgentIntegration', {
    	      taskDefinition: cwAgentTaskDefinition,
    	      containerName: 'ecs-cwagent',
    	      enableLogging: false,
    	      cpu: 128,
    	      memoryLimitMiB: 64,
    	      portMappings: [
    	        {
    	          containerPort: 4316,
    	          hostPort: 4316,
    	        },
    	        {
    	          containerPort: 2000,
    	          hostPort: 2000,
    	        },
    	      ],
    	    });

    	    // Create the CloudWatch Agent daemon service
    	    new ecs.Ec2Service(this, 'CloudWatchAgentDaemon', {
    	      cluster,
    	      taskDefinition: cwAgentTaskDefinition,
    	      daemon: true,  // Runs one container per EC2 instance
    	    });

    	    // Define Task Definition for user application
    	    const sampleAppTaskDefinition = new ecs.Ec2TaskDefinition(this, 'SampleAppTaskDefinition', {
    	      networkMode: ecs.NetworkMode.HOST,
    	    });

    	    sampleAppTaskDefinition.addContainer('app', {
    	      image: ecs.ContainerImage.fromRegistry('test/sample-app'),
    	      cpu: 0,
    	      memoryLimitMiB: 512,
    	    });

    	    // No CloudWatch Agent sidecar is needed as application container communicates to CloudWatch Agent daemon through host network
    	    new appsignals.ApplicationSignalsIntegration(this, 'ApplicationSignalsIntegration', {
    	      taskDefinition: sampleAppTaskDefinition,
    	      instrumentation: {
    	        sdkVersion: appsignals.PythonInstrumentationVersion.V0_8_0
    	      },
    	      serviceName: 'sample-app'
    	    });

    	    new ecs.Ec2Service(this, 'MySampleApp', {
    	      cluster,
    	      taskDefinition: sampleAppTaskDefinition,
    	      desiredCount: 1,
    	    });
    	  }
    	}
    	```
    * **Enable Application Signals on Amazon ECS with replica mode**


    ###### Note

    Running CloudWatch Agent service using replica mode requires specific security group configurations to enable communication with other services.
     For Application Signals functionality, configure the security group with the minimum inbound rules: Port 2000 (HTTP) and Port 4316 (HTTP). This configuration
     ensures proper connectivity between the CloudWatch Agent and dependent services.


    	1. Run CloudWatch Agent as a replica service with service connect.
    	2. Configure `instrumentation` to instrument the application with the ADOT Python Agent.
    	3. Override environment variables by configuring `overrideEnvironments` to use service connect endpoints to communicate to the CloudWatch agent server.



    	```
    	import { Construct } from 'constructs';
    	import * as appsignals from '@aws-cdk/aws-applicationsignals-alpha';
    	import * as cdk from 'aws-cdk-lib';
    	import * as ec2 from 'aws-cdk-lib/aws-ec2';
    	import * as ecs from 'aws-cdk-lib/aws-ecs';
    	import { PrivateDnsNamespace } from 'aws-cdk-lib/aws-servicediscovery';

    	class MyStack extends cdk.Stack {
    	  public constructor(scope?: Construct, id?: string, props: cdk.StackProps = {}) {
    	    super(scope, id, props);

    	    const vpc = new ec2.Vpc(this, 'TestVpc', {});
    	    const cluster = new ecs.Cluster(this, 'TestCluster', { vpc });
    	    const dnsNamespace = new PrivateDnsNamespace(this, 'Namespace', {
    	      vpc,
    	      name: 'local',
    	    });
    	    const securityGroup = new ec2.SecurityGroup(this, 'ECSSG', { vpc });
    	    securityGroup.addIngressRule(securityGroup, ec2.Port.tcpRange(0, 65535));

    	    // Define Task Definition for CloudWatch agent (Replica)
    	    const cwAgentTaskDefinition = new ecs.FargateTaskDefinition(this, 'CloudWatchAgentTaskDefinition', {});

    	    new appsignals.CloudWatchAgentIntegration(this, 'CloudWatchAgentIntegration', {
    	      taskDefinition: cwAgentTaskDefinition,
    	      containerName: 'ecs-cwagent',
    	      enableLogging: false,
    	      cpu: 128,
    	      memoryLimitMiB: 64,
    	      portMappings: [
    	        {
    	          name: 'cwagent-4316',
    	          containerPort: 4316,
    	          hostPort: 4316,
    	        },
    	        {
    	          name: 'cwagent-2000',
    	          containerPort: 2000,
    	          hostPort: 2000,
    	        },
    	      ],
    	    });

    	    // Create the CloudWatch Agent replica service with service connect
    	    new ecs.FargateService(this, 'CloudWatchAgentService', {
    	      cluster: cluster,
    	      taskDefinition: cwAgentTaskDefinition,
    	      securityGroups: [securityGroup],
    	      serviceConnectConfiguration: {
    	        namespace: dnsNamespace.namespaceArn,
    	        services: [
    	          {
    	            portMappingName: 'cwagent-4316',
    	            dnsName: 'cwagent-4316-http',
    	            port: 4316,
    	          },
    	          {
    	            portMappingName: 'cwagent-2000',
    	            dnsName: 'cwagent-2000-http',
    	            port: 2000,
    	          },
    	        ],
    	      },
    	      desiredCount: 1,
    	    });

    	    // Define Task Definition for user application
    	    const sampleAppTaskDefinition = new ecs.FargateTaskDefinition(this, 'SampleAppTaskDefinition', {});

    	    sampleAppTaskDefinition.addContainer('app', {
    	      image: ecs.ContainerImage.fromRegistry('test/sample-app'),
    	      cpu: 0,
    	      memoryLimitMiB: 512,
    	    });

    	    // Overwrite environment variables to connect to the CloudWatch Agent service just created
    	    new appsignals.ApplicationSignalsIntegration(this, 'ApplicationSignalsIntegration', {
    	      taskDefinition: sampleAppTaskDefinition,
    	      instrumentation: {
    	        sdkVersion: appsignals.PythonInstrumentationVersion.V0_8_0,
    	      },
    	      serviceName: 'sample-app',
    	      overrideEnvironments: [
    	        {
    	          name: appsignals.CommonExporting.OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT,
    	          value: 'http://cwagent-4316-http:4316/v1/metrics',
    	        },
    	        {
    	          name: appsignals.TraceExporting.OTEL_EXPORTER_OTLP_TRACES_ENDPOINT,
    	          value: 'http://cwagent-4316-http:4316/v1/traces',
    	        },
    	        {
    	          name: appsignals.TraceExporting.OTEL_TRACES_SAMPLER_ARG,
    	          value: 'endpoint=http://cwagent-2000-http:2000',
    	        },
    	      ],
    	    });

    	    // Create ECS Service with service connect configuration
    	    new ecs.FargateService(this, 'MySampleApp', {
    	      cluster: cluster,
    	      taskDefinition: sampleAppTaskDefinition,
    	      serviceConnectConfiguration: {
    	        namespace: dnsNamespace.namespaceArn,
    	      },
    	      desiredCount: 1,
    	    });
    	  }
    	}
    	```

3. Setting up a Node.js application with the ESM module format. There is limited support for Node.js applications with the ESM module format. For more information, see [Known limitations about Node.js with ESM](CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations "CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations").

For the ESM module format, enabling Application Signals by using the `init` container to inject the Node.js instrumentation SDK doesn't apply. Skip Step 2 in this procedure, and do the following instead.

    * Install the relevant dependencies to your Node.js application for autoinstrumentation.



    ```
    npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation
    npm install @opentelemetry/instrumentation@0.54.
    ```
    * Update TaskDefinition.


    	1. Add additional configuration to your application container.
    	2. Configure `NODE_OPTIONS`.
    	3. (Optional) Add CloudWatch Agent if you choose sidecar mode.



    	```
    	import { Construct } from 'constructs';
    	import * as appsignals from '@aws-cdk/aws-applicationsignals-alpha';
    	import * as ecs from 'aws-cdk-lib/aws-ecs';

    	class MyStack extends cdk.Stack {
    	  public constructor(scope?: Construct, id?: string, props: cdk.StackProps = {}) {
    	    super(scope, id, props);
    	    const fargateTaskDefinition = new ecs.FargateTaskDefinition(stack, 'TestTaskDefinition', {
    	      cpu: 256,
    	      memoryLimitMiB: 512,
    	    });
    	    const appContainer = fargateTaskDefinition.addContainer('app', {
    	      image: ecs.ContainerImage.fromRegistry('docker/cdk-test'),
    	    });

    	    const volumeName = 'opentelemetry-auto-instrumentation'
    	    fargateTaskDefinition.addVolume({name: volumeName});

    	    // Inject additional configurations
    	    const injector = new appsignals.NodeInjector(volumeName, appsignals.NodeInstrumentationVersion.V0_5_0);
    	    injector.renderDefaultContainer(fargateTaskDefinition);
    	    // Configure NODE_OPTIONS
    	    appContainer.addEnvironment('NODE_OPTIONS', '--import @aws/aws-distro-opentelemetry-node-autoinstrumentation/register --experimental-loader=@opentelemetry/instrumentation/hook.mjs')

    	    // Optional: add CloudWatch agent
    	    const cwAgent = new appsignals.CloudWatchAgentIntegration(stack, 'AddCloudWatchAgent', {
    	      containerName: 'ecs-cwagent',
    	      taskDefinition: fargateTaskDefinition,
    	      memoryReservationMiB: 50,
    	    });
    	    appContainer.addContainerDependencies({
    	      container: cwAgent.agentContainer,
    	      condition: ecs.ContainerDependencyCondition.START,
    	    });
    	}
    	```

4. Deploy the updated stack – Run the `cdk synth` command in your application's main directory.
   To deploy the service in your AWS account, run the `cdk deploy` command in your application's main directory.

If you used the sidecar strategy, you'll see one service created:

    * `APPLICATION_SERVICE` is the service of your application. It includes the three following containers:




    	+ `init`– A required container for initializing Application Signals.
    	+ `ecs-cwagent`– A container running the CloudWatch agent
    	+ ``my-app``– This is the example application container in our
    	 documentation. In your actual workloads, this specific container might not exist or might be replaced with your own service containers.

If you used the daemon strategy, you'll see two services created:

    * `CloudWatchAgentDaemon`  is the CloudWatch agent daemon service.
    * `APPLICATION_SERVICE` is the service of your application. It includes the two following containers:




    	+ `init`– A required container for initializing Application Signals.
    	+ ``my-app``– This is the example application container in our
    	 documentation. In your actual workloads, this specific container might not exist or might be replaced with your own service containers.

If you used the replica strategy, you'll see two services created:

    * `CloudWatchAgentService` is the CloudWatch agent replica service.
    * `APPLICATION_SERVICE` is the service of your application. It includes the two following containers:




    	+ `init`– A required container for initializing Application Signals.
    	+ ``my-app``– This is the example application container in our
    	 documentation. In your actual workloads, this specific container might not exist or might be replaced with your own service containers.
