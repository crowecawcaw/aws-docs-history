# Using the role manager (AWS CDK)

Use the AWS Cloud Development Kit (AWS CDK) with Amazon SageMaker Role Manager to programmatically create roles and set permissions. You can use the AWS CDK to accomplish any task that you could perform using the AWS Management Console. The programmatic access of the CDK makes it easier to provide permissions that give your users access to specific resources.
For more information about the AWS CDK, see [What is AWS CDK?](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")

###### Important

You must use the SageMaker AI Compute Role persona to create a SageMaker AI Compute Role. For more information about the compute persona, see [SageMaker AI compute persona](role-manager-personas.md#role-manager-personas-compute "role-manager-personas.md#role-manager-personas-compute").
For code that you can use to create the compute role within the AWS CDK, see [Grant permissions to a Compute persona](#role-manager-cdk-compute-persona "#role-manager-cdk-compute-persona").

The following are examples of tasks that you can perform in the AWS CDK:

- Create IAM roles with granular permissions for machine learning (ML) personas, such as Data Scientists and MLOps Engineers.
- Grant permissions to CDK constructs from ML personas or ML activities.
- Set ML activity condition parameters.
- Enable global Amazon VPC and AWS Key Management Service conditions and set values for them.
- Choose from all versions of the ML activities for your users without causing disruptions in their access.
  There are common AWS tasks related to machine learning (ML) with SageMaker AI that require specific IAM permissions. The permissions to perform the tasks are defined as ML activities in Amazon SageMaker Role Manager. ML activities specify a set of permissions that are linked to the IAM role. For example, the ML activity for Amazon SageMaker Studio Classic has all of the permissions that a user
  needs to access Studio Classic. For more information about ML activities, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md").

When you're creating roles, you first define the constructs for the ML persona or the ML activity. A construct is a resource within the AWS CDK stack. For example, a construct could be an Amazon S3 bucket, an Amazon VPC subnet, or an IAM role.

As you're creating the persona or activity, you can limit the permissions associated with that persona or activity to specific resources. For example, you can customize the activity to only provide permissions for a specific subnet within an Amazon VPC.

After you've defined permissions, you can create roles and then pass those roles to create other resources, such as SageMaker notebook instances.

The following are code examples in Typescript for tasks that you can accomplish using the CDK. When you create an activity, you specify an ID and the options for the activity's construct. The options are dictionaries that specify the required parameters for the activities, such as an Amazon S3. You pass an empty dictionary for activities that don't have required parameters.

The following code creates a Data Scientist ML persona with a set of ML activities specific to the persona.
The permissions from ML activities only apply to the Amazon VPC and AWS KMS configurations specified in the persona construct.
The following code creates a class for a Data Scientist persona. The ML activities are defined in the activities list.
The VPC permissions and the KMS permissions are defined as optional parameters outside of the activities list.

After you’ve defined the class, you can create a role as a construct within the AWS CDK stack. You can also create a notebook instance. The person who is using the IAM role that you’ve created in the following code can access the notebook instance when they log in to their AWS account.

```

export class myCDKStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const persona = new Persona(this, 'example-persona-id', {
        activities: [
            Activity.accessAwsServices(this, '`example-id1`', {})
        ]
    });

    const role = persona.createRole(this, '`example-IAM-role-id`', '`example-IAM-role-name`');

    }
}

```

The following code creates a Data Scientist ML persona with a set of ML activities specific to the persona.
The permissions from ML activities only apply to the VPC and KMS configurations specified in the persona construct.
The following code creates a class for a Data Scientist persona. The ML activities are defined in the activities list.
The Amazon VPC permissions and the AWS KMS permissions are defined as optional parameters outside of the activities list.

After you’ve defined the class, you can create a role as a construct within the AWS CDK stack. You can also create a notebook instance. The person who is using the IAM role that you’ve created in the following code can access the notebook instance when they log in to their AWS account.

```

export class myCDKStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const persona = new Persona(this, '`example-persona-id`', {
        activities: [
            Activity.runStudioAppsV2(this, '`example-id1`', {}),
            Activity.manageJobs(this, '`example-id2`', {rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.manageModels(this, '`example-id3`', {rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.manageExperiments(this, '`example-id4`', {}),
            Activity.visualizeExperiments(this, '`example-id5`', {}),
            Activity.accessS3Buckets(this, '`example-id6`', {s3buckets: [s3.S3Bucket.fromBucketName('`amzn-s3-demo-bucket`')]})
        ],
        // optional: to configure VPC permissions
        subnets: [ec2.Subnet.fromSubnetId('`example-VPC-subnet-id`')],
        securityGroups: [ec2.SecurityGroup.fromSecurityGroupId('`example-VPC-security-group-id`')],
        // optional: to configure KMS permissions
        dataKeys: [kms.Key.fromKeyArn('`example-KMS-key-ARN`')],
        volumeKeys: [kms.Key.fromKeyArn('`example-KMS-key-ARN`')],
    });

    const role = persona.createRole(this, '`example-IAM-role-id`', '`example-IAM-role-name`');

    const notebookInstance = new CfnNotebookInstance(this, '`example-notebook-instance-name`', { RoleArn: role.RoleArn, ...});
    }
}

```

The following code creates an ML Ops persona with a set of ML activities specific to the persona. The permissions from ML activities only apply to the Amazon VPC and AWS KMS configurations specified in the persona construct.
The following code creates a class for an ML Ops persona. The ML activities are defined in the activities list. The VPC permissions and the KMS permissions are defined as optional parameters outside of the activities list.

After you’ve defined the class, you can create a role as a construct within the AWS CDK stack. You can also create an Amazon SageMaker Studio Classic user profile.
The person who is using the IAM role that you’ve created in the following code can open SageMaker Studio Classic when they log in to their AWS account.

```

export class myCDKStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const persona = new Persona(this, '`example-persona-id`', {
        activities: [
            Activity.runStudioAppsV2(this, '`example-id1`', {}),
            Activity.manageModels(this, '`example-id2`', {rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.manageEndpoints(this, '`example-id3`',{rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.managePipelines(this, '`example-id4`', {rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.visualizeExperiments(this, '`example-id5`', {})
        ],
        subnets: [ec2.Subnet.fromSubnetId('`example-VPC-subnet-id`')],
        securityGroups: [ec2.SecurityGroup.fromSecurityGroupId('`example-VPC-security-group-id`')],
        dataKeys: [kms.Key.fromKeyArn('`example-KMS-key-ARN`')],
        volumeKeys: [kms.Key.fromKeyArn('`example-KMS-key-ARN`')],
    });

    const role = persona.createRole(this, '`example-IAM-role-id`', '`example-IAM-role-name`');

    let userProfile = new CfnNUserProfile(this, '`example-Studio Classic-profile-name`', { RoleName: role.RoleName, ... });
    }
}

```

The following code creates an ML Ops persona with a set of ML activities specific to the persona. The following code creates a class for a ML Ops persona. The ML activities are defined in the activities list.

After you’ve defined the class, you can create a role as a construct within the AWS CDK stack. You can also create a notebook instance. The code grants permissions from the ML activities to the IAM role of the Lambda function.

```

export class myCDKStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const persona = new Persona(this, '`example-persona-id`', {
        activities: [
            Activity.runStudioAppsV2(this, '`example-id1`', {}),
            Activity.manageModels(this, '`example-id2`', {rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.manageEndpoints(this, '`example-id3`',{rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.managePipelines(this, '`example-id4`', {rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')]}),
            Activity.visualizeExperiments(this, '`example-id5`', {})
        ],
    });

    const lambdaFn = lambda.Function.fromFunctionName('`example-lambda-function-name`');
    persona.grantPermissionsTo(lambdaFn);
    }
}


```

The following code creates an ML activity and creates a role from the activity. The permissions from the activity only apply to the VPC and KMS configuration that you specify for the user.

```

export class myCDKStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const activity = Activity.manageJobs(this, '`example-activity-id`', {
        rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')],
        subnets: [ec2.Subnet.fromSubnetId('`example-VPC-subnet-id`')],
        securityGroups: [ec2.SecurityGroup.fromSecurityGroupId('`example-VPC-security-group-id`')],
        dataKeys: [kms.Key.fromKeyArn('`example-KMS-key-ARN`')],
        volumeKeys: [kms.Key.fromKeyArn('`example-KMS-key-ARN`')],
    });

    const role = activity.createRole(this, '`example-IAM-role-id`', '`example-IAM-role-name`');
    }
}

```

The following code creates an IAM role for a single ML activity.

```

export class myCDKStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const activity = Activity.manageJobs(this, '`example-activity-id`', {
        rolesToPass: [iam.Role.fromRoleName('`example-IAM-role-name`')],
    });


    activity.create_role(this, '`example-IAM-role-id`', '`example-IAM-role-name`')
    }
}

```
