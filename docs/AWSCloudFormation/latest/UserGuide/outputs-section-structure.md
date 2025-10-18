# CloudFormation template Outputs syntax

The optional `Outputs` section declares output values for the stack. These
 output values can be used in various ways:


* Capture important details about your resources
 – An output is a convenient way to capture important information about your
 resources. For example, you can output the S3 bucket name for a stack to make the
 bucket easier to find. You can view output values in the
 **Outputs** tab of the CloudFormation console or by using the [describe-stacks](service_code_examples.md#describe-stacks-sdk "service_code_examples.md#describe-stacks-sdk") CLI command.
* Cross-stack references – You can import
 output values into other stacks to [create
 references between stacks](using-cfn-stack-exports.md "using-cfn-stack-exports.md"). This is helpful when you need to share
 resources or configurations across multiple stacks.
###### Important

CloudFormation doesn't redact or obfuscate any information you include in the
 `Outputs` section. We strongly recommend you don't use this section to
 output sensitive information, such as passwords or secrets.

Output values are available after the stack operation is complete. Stack output values
 aren't available when a stack status is in any of the `IN_PROGRESS`
[statuses](view-stack-events.md#cfn-console-view-stack-data-resources-status-codes "view-stack-events.md#cfn-console-view-stack-data-resources-status-codes"). We
 don't recommend establishing dependencies between a service runtime and the stack output
 value because output values might not be available at all times.


## Syntax


The `Outputs` section consists of the key name `Outputs`. You
 can declare a maximum of 200 outputs in a template.


The following example demonstrates the structure of the `Outputs`
 section.



### JSON


Use braces to enclose all output declarations. Delimit multiple outputs with
 commas.



```
"Outputs" : {
  "`OutputLogicalID`" : {
    "Description" : "`Information about the value`",
    "Value" : "`Value to return`",
    "Export" : {
      "Name" : "`Name of resource to export`"
    }
  }
}
```



### YAML



```
Outputs:
  `OutputLogicalID`:
    Description: `Information about the value`
    Value: `Value to return`
    Export:
      Name: `Name of resource to export`
```


### Output fields


The `Outputs` section can include the following fields.




**Logical ID (also called *logical name*)**

An identifier for the current output. The logical ID must be
 alphanumeric (`a–z`, `A–Z`,
 `0–9`) and unique within the template.



**`Description` (optional)**

A `String` type that describes the output value. The value
 for the description declaration must be a literal string that's between
 0 and 1024 bytes in length. You can't use a parameter or function to
 specify the description.
 



**`Value` (required)**

The value of the property returned by the [describe-stacks](service_code_examples.md#describe-stacks-sdk "service_code_examples.md#describe-stacks-sdk")
 command. The value of an output can include literals, parameter
 references, pseudo parameters, a mapping value, or intrinsic
 functions.



**`Export` (optional)**

The name of the resource output to be exported for a cross-stack
 reference.


You can use intrinsic functions to customize the `Name`
 value of an export.


For more information, see [Get exported outputs from a deployed CloudFormation
 stack](using-cfn-stack-exports.md "using-cfn-stack-exports.md").




To associate a condition with an output, define the condition in the [Conditions](conditions-section-structure.md "conditions-section-structure.md") section of the template.


## Examples


The following examples illustrate how stack output works.


###### Topics

* [Stack
 output](#outputs-section-structure-examples-stack-output "#outputs-section-structure-examples-stack-output")
* [Customize export
 name using Fn::Sub](#outputs-section-structure-examples-cross-stack "#outputs-section-structure-examples-cross-stack")
* [Customize
 export name using Fn::Join](#outputs-section-structure-examples-join-export-name "#outputs-section-structure-examples-join-export-name")
* [Return a URL
 constructed using Fn::Join](#outputs-section-structure-examples-join-export-url "#outputs-section-structure-examples-join-export-url")

### Stack
 output


In the following example, the output named `BackupLoadBalancerDNSName`
 returns the DNS name for the resource with the logical ID
 `BackupLoadBalancer` only when the `CreateProdResources`
 condition is true. The output named `InstanceID` returns the ID of the
 EC2 instance with the logical ID `EC2Instance`.



#### JSON



```
"Outputs" : {
  "BackupLoadBalancerDNSName" : {
    "Description": "The DNSName of the backup load balancer",  
    "Value" : { "Fn::GetAtt" : [ "BackupLoadBalancer", "DNSName" ]},
    "Condition" : "CreateProdResources"
  },
  "InstanceID" : {
    "Description": "The Instance ID",  
    "Value" : { "Ref" : "EC2Instance" }
  }
}
```



#### YAML



```
Outputs:
  BackupLoadBalancerDNSName:
    Description: The DNSName of the backup load balancer
    Value: !GetAtt BackupLoadBalancer.DNSName
    Condition: CreateProdResources
  InstanceID:
    Description: The Instance ID
    Value: !Ref EC2Instance
```


### Customize export
 name using `Fn::Sub`


In the following examples, the output named `StackVPC` returns the ID
 of a VPC, and then exports the value for cross-stack referencing with the name
 `VPCID` appended to the stack's name.



#### JSON



```
"Outputs" : {
  "StackVPC" : {
    "Description" : "The ID of the VPC",
    "Value" : { "Ref" : "MyVPC" },
    "Export" : {
      "Name" : {"Fn::Sub": "${AWS::StackName}-VPCID" }
    }
  }
}
```



#### YAML



```
Outputs:
  StackVPC:
    Description: The ID of the VPC
    Value: !Ref MyVPC
    Export:
      Name: !Sub "${AWS::StackName}-VPCID"
```


For more information about the `Fn::Sub` function, see [Fn::Sub](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html").


### Customize
 export name using `Fn::Join`


You can also use the `Fn::Join` function to construct values based on
 parameters, resource attributes, and other strings.


The following examples use the `Fn::Join` function to customize the
 export name instead of the `Fn::Sub` function. The example
 `Fn::Join` function concatenates the stack name with the name
 `VPCID` using a colon as a separator.



#### JSON



```
"Outputs" : {
  "StackVPC" : {
    "Description" : "The ID of the VPC",
    "Value" : { "Ref" : "MyVPC" },
    "Export" : {
      "Name" : { "Fn::Join" : [ ":", [ { "Ref" : "AWS::StackName" }, "VPCID" ] ] }
    }
  }
}
```



#### YAML



```
Outputs:
  StackVPC:
    Description: The ID of the VPC
    Value: !Ref MyVPC
    Export:
      Name: !Join [ ":", [ !Ref "AWS::StackName", VPCID ] ]
```


For more information about the `Fn::Join` function, see [Fn::Join](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-join.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-join.html").


### Return a URL
 constructed using `Fn::Join`


In the following example for a template that creates a WordPress site,
 `InstallURL` is the string returned by a `Fn::Join`
 function call that concatenates `http://`, the DNS name of the resource
 `ElasticLoadBalancer`, and `/wp-admin/install.php`. The
 output value would be similar to the following:



```
http://mywptests-elasticl-1gb51l6sl8y5v-206169572.aws-region.elb.amazonaws.com/wp-admin/install.php
```


#### JSON



```
{
    "Outputs": {
        "InstallURL": {
            "Value": {
                "Fn::Join": [
                    "",
                    [
                        "http://",
                        {
                            "Fn::GetAtt": [
                                "ElasticLoadBalancer",
                                "DNSName"
                            ]
                        },
                        "/wp-admin/install.php"
                    ]
                ]
            },
            "Description": "Installation URL of the WordPress website"
        }
    }
}
```



#### YAML



```
Outputs:
  InstallURL:
    Value: !Join 
      - ''
      - - 'http://'
        - !GetAtt 
          - ElasticLoadBalancer
          - DNSName
        - /wp-admin/install.php
    Description: Installation URL of the WordPress website
```


For more information about the `Fn::Join` function, see [Fn::Join](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-join.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-join.html").
