# no-unrestricted-route-to-igw

Checks if there are public routes in the route table to an Internet gateway (IGW). The rule is NON_COMPLIANT if a route to an IGW has a destination CIDR block of '0.0.0.0/0' or '::/0' or if a destination CIDR block does not match the rule parameter.

**Identifier:** NO_UNRESTRICTED_ROUTE_TO_IGW

**Resource Types:** AWS::EC2::RouteTable

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

routeTableIds (Optional)
Type: CSV

Comma-separated list of route table IDs that can have routes to an Internet Gateway with a destination CIDR block of '0.0.0.0/0' or '::/0'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
