# Enabling AWS WAF for an Amplify application using the AWS CDK

You can use the AWS Cloud Development Kit (AWS CDK) to enable AWS WAF for an Amplify application. To learn more about using the CDK, see [What is the CDK?](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") in the _AWS Cloud Development Kit (AWS CDK) Developer Guide_.

The following
TypeScript code example demonstrates how to create an AWS CDK app with two CDK stacks:
one for Amplify and one for AWS WAF. Notice that the AWS WAF stack must be deployed to the
US East (N. Virginia) (us-east-1) Region. The Amplify application stack can be deployed to a
different Region. You must create the web ACL that you want to associate with the Amplify app in the Global
(CloudFront) Region. Regional web ACLs might already exist in your AWS account, but they are not
compatible with Amplify.

```
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as wafv2 from "aws-cdk-lib/aws-wafv2";
import * as amplify from "aws-cdk-lib/aws-amplify";

interface WafStackProps extends cdk.StackProps {
  appArn: string;
}

export class AmplifyStack extends cdk.Stack {
  public readonly appArn: string;
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    const amplifyApp = new amplify.CfnApp(this, "AmplifyApp", {
      name: "MyApp",
    });
    this.appArn = amplifyApp.attrArn;
  }
}

export class WAFStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: WafStackProps) {
    super(scope, id, props);
    const webAcl = new wafv2.CfnWebACL(this, "WebACL", {
      defaultAction: { allow: {} },
      scope: "CLOUDFRONT",
      rules: [
        // Add your own rules here.
      ],
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: "my-metric-name",
        sampledRequestsEnabled: true,
      },
    });

    new wafv2.CfnWebACLAssociation(this, "WebACLAssociation", {
      resourceArn: props.appArn,
      webAclArn: webAcl.attrArn,
    });
  }
}

const app = new cdk.App();

// Create AmplifyStack in your desired Region.
const amplifyStack = new AmplifyStack(app, 'AmplifyStack', {
  env: { region: 'us-west-2' },
});

// Create WAFStack in IAD region, passing appArn from AmplifyStack.
new WAFStack(app, 'WAFStack', {
  env: { region: 'us-east-1' },
  crossRegionReferences: true,

  appArn: amplifyStack.appArn,  // Pass appArn from AmplifyStack.
});
```
