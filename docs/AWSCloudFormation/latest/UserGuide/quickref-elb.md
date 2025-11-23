# ELB template snippets

To create an Application Load Balancer, a Network Load Balancer, or a Gateway Load Balancer, use the V2 resource types, which start with `AWS::ElasticLoadBalancingV2`.
To create a Classic Load Balancer, use the resource types that start with `AWS::ElasticLoadBalancing`.

###### Contents

- [ELBv2 resources](#scenario-elbv2-load-balancer "#scenario-elbv2-load-balancer")
- [Classic Load Balancer resources](#scenario-elb-load-balancer "#scenario-elb-load-balancer")

## ELBv2 resources

This example defines an Application Load Balancer with an HTTP listener and a default action that
forwards traffic to the target group. The load balancer uses the default health check
settings. The target group has two registered EC2 instances.

YAML

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup

  myHTTPlistener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: HTTP
      Port: 80
      DefaultActions:
        - Type: "forward"
          TargetGroupArn: !Ref myTargetGroup

  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: "my-target-group"
      Protocol: HTTP
      Port: 80
      TargetType: instance
      VpcId: !Ref myVPC
      Targets:
        - Id: !GetAtt Instance1.InstanceId
          Port: 80
        - Id: !GetAtt Instance2.InstanceId
          Port: 80
```

JSON

```
{
    "Resources": {
        "myLoadBalancer": {
            "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "Properties": {
                "Name": "my-alb",
                "Type": "application",
                "Scheme": "internal",
                "Subnets": [
                    {
                        "Ref": "subnet-AZ1"
                    },
                    {
                        "Ref": "subnet-AZ2"
                    }
                ],
                "SecurityGroups": [
                    {
                        "Ref": "mySecurityGroup"
                    }
                ]
            }
        },
        "myHTTPlistener": {
            "Type": "AWS::ElasticLoadBalancingV2::Listener",
            "Properties": {
                "LoadBalancerArn": {
                    "Ref": "myLoadBalancer"
                },
                "Protocol": "HTTP",
                "Port": 80,
                "DefaultActions": [
                    {
                        "Type": "forward",
                        "TargetGroupArn": {
                            "Ref": "myTargetGroup"
                        }
                    }
                ]
            }
        },
        "myTargetGroup": {
            "Type": "AWS::ElasticLoadBalancingV2::TargetGroup",
            "Properties": {
                "Name": "my-target-group",
                "Protocol": "HTTP",
                "Port": 80,
                "TargetType": "instance",
                "VpcId": {
                    "Ref": "myVPC"
                },
                "Targets": [
                    {
                        "Id": {
                            "Fn::GetAtt": [
                                "Instance1",
                                "InstanceId"
                            ]
                        },
                        "Port": 80
                    },
                    {
                        "Id": {
                            "Fn::GetAtt": [
                                "Instance2",
                                "InstanceId"
                            ]
                        },
                        "Port": 80
                    }
                ]
            }
        }
    }
}
```

## Classic Load Balancer resources

This example defines a Classic Load Balancer with an HTTP listener and no registered EC2 instances.
The load balancer uses the default health check settings.

YAML

```
myLoadBalancer:
  Type: 'AWS::ElasticLoadBalancing::LoadBalancer'
  Properties:
    AvailabilityZones:
    - "us-east-1a"
    Listeners:
    - LoadBalancerPort: '80'
      InstancePort: '80'
      Protocol: HTTP
```

JSON

```
"myLoadBalancer" : {
    "Type" : "AWS::ElasticLoadBalancing::LoadBalancer",
    "Properties" : {
        "AvailabilityZones" : [ "us-east-1a" ],
        "Listeners" : [ {
            "LoadBalancerPort" : "80",
            "InstancePort" : "80",
            "Protocol" : "HTTP"
        } ]
    }
}
```

This example defines a Classic Load Balancer with an HTTP listener, two registered EC2 instances,
and custom health check settings.

YAML

```
myClassicLoadBalancer:
  Type: 'AWS::ElasticLoadBalancing::LoadBalancer'
  Properties:
    AvailabilityZones:
    - "us-east-1a"
    Instances:
    - Ref: Instance1
    - Ref: Instance2
    Listeners:
    - LoadBalancerPort: '80'
      InstancePort: '80'
      Protocol: HTTP
    HealthCheck:
      Target: HTTP:80/
      HealthyThreshold: '3'
      UnhealthyThreshold: '5'
      Interval: '30'
      Timeout: '5'
```

JSON

```
"myClassicLoadBalancer" : {
    "Type" : "AWS::ElasticLoadBalancing::LoadBalancer",
    "Properties" : {
        "AvailabilityZones" : [ "us-east-1a" ],
        "Instances" : [
            { "Ref" : "Instance1" },
            { "Ref" : "Instance2" }
        ],
        "Listeners" : [ {
            "LoadBalancerPort" : "80",
            "InstancePort" : "80",
            "Protocol" : "HTTP"
        } ],

        "HealthCheck" : {
            "Target" : "HTTP:80/",
            "HealthyThreshold" : "3",
            "UnhealthyThreshold" : "5",
            "Interval" : "30",
            "Timeout" : "5"
        }
    }
}
```
