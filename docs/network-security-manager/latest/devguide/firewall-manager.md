

# AWS Network Security Manager and AWS Firewall Manager
<a name="firewall-manager"></a>

AWS Network Security Manager is the service that is replacing AWS Firewall Manager. The two are wholly separate services, each with unique capabilities and a different pricing model. If you currently use AWS Firewall Manager, you don't need to take any action—your existing firewalls and policies continue to work. This chapter describes how the two services coexist, how precedence works when you use both, and how migration will work when it becomes available.

AWS Network Security Manager and AWS Firewall Manager operate side by side and independently of each other. At some point, AWS Firewall Manager will stop being sold and then stop operating.

## Coexistence with AWS Firewall Manager
<a name="firewall-manager-coexistence"></a>

AWS Network Security Manager doesn't affect firewalls that you created with AWS Firewall Manager unless you initiate an action to change them. Firewalls and policies that you created with AWS Firewall Manager continue to operate unless you terminate them. This is true even after AWS Firewall Manager is retired.

## Precedence during remediation
<a name="firewall-manager-precedence"></a>

While both services operate, you can take actions that affect firewalls that you created with AWS Firewall Manager. When you create AWS Network Security Manager policies, you apply them to a scope, which is a set of target resources. If that scope includes resources that an AWS Firewall Manager policy already addresses, AWS Network Security Manager takes precedence during remediation. In that case, the AWS Network Security Manager policy and scope override the existing AWS Firewall Manager firewall and policy. The specific behavior depends on the resolution options that you select.

## Planned migration from AWS Firewall Manager
<a name="firewall-manager-migration"></a>

Migrating from AWS Firewall Manager to AWS Network Security Manager consolidates your firewall management into a single service and lets you use its capabilities. Migrating is planned but is not yet available. When migration becomes available, you will be able to move your AWS Firewall Manager policies to AWS Network Security Manager. Migrating will require new actions in both services that are not yet in place.

The planned process will copy a selected policy from AWS Firewall Manager, transfer it to AWS Network Security Manager, and translate it into the new policy structure. This process doesn't affect your original policy or its associated firewalls in AWS Firewall Manager.