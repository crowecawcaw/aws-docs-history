# Installing and setting up the Amazon Neptune utility for GraphQL

If you're going to use the utility with an existing Neptune database, you need
it to be able to connect to the database endpoint. By default, a Neptune database is
accessible only from within the VPC where it is located.

Because the utility is a Node.js command-line tool, you must have Node.js (version 18
or above) installed for the utility to run. To install Node.js on an EC2 instance in the
same VPC as your Neptune database, follow the [instructions
here](../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md "../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md"). The minimum size instance to run the utility is t2.micro. During the creation
of the instance select the Neptune database VPC from the **Common Security
Groups** pulldown menu.

To install the utility itself on an EC2 instance or your local machine, use NPM:

```
npm i @aws/neptune-for-graphql -g
```

You can then run the utility's help command to check whether it installed properly:

```
neptune-for-graphql --help
```

You may also want to [install the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") to
manage AWS resources.
