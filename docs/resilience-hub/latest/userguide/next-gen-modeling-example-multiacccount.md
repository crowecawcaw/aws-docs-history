

# Example: Modeling a multi-account application
<a name="next-gen-modeling-example-multiacccount"></a>

This example shows how to model a large e-commerce platform with 30 services across 10 accounts in Next generation Resilience Hub.

**To model a multi-account application**

1. **Create the system in a central account.**

   Start by creating a single system that represents the entire e-commerce platform. Create the system in your central governance account and enable cross-account sharing:

   ```
   aws resiliencehubv2 create-system \
     --name "acme-ecommerce" \
     --description "Acme Corp e-commerce platform" \
     --sharing-enabled
   ```

1. **Create services in their respective accounts.**

   Each team creates their service in their own account, referencing the central system ARN:

   ```
   # In account A (auth team)
   aws resiliencehubv2 create-service \
     --name "auth-service" \
     --regions '["us-east-1", "us-west-2"]' \
     --permission-model '{"invokerRoleName": "AWSResilienceHubAssessmentRole"}' \
     --associated-systems '[{"systemArn": "arn:aws:resiliencehub:us-east-1:111111111111:system/acme-ecommerce:abc123"}]'
   
   # In account B (checkout team)
   aws resiliencehubv2 create-service \
     --name "checkout-service" \
     --regions '["us-east-1", "us-west-2"]' \
     --permission-model '{"invokerRoleName": "AWSResilienceHubAssessmentRole"}' \
     --associated-systems '[{"systemArn": "arn:aws:resiliencehub:us-east-1:111111111111:system/acme-ecommerce:abc123"}]'
   ```

1. **Add input sources to each service.**

   Each team adds their resource discovery configuration:

   ```
   # Auth team adds their CloudFormation stack
   aws resiliencehubv2 create-input-source \
     --service-arn "arn:aws:resiliencehub:us-east-1:222222222222:service/auth-service:def456" \
     --resource-configuration '{"cfnStackArn": "arn:aws:cloudformation:us-east-1:222222222222:stack/auth-prod/..."}'
   
   # Checkout team adds their EKS cluster
   aws resiliencehubv2 create-input-source \
     --service-arn "arn:aws:resiliencehub:us-east-1:333333333333:service/checkout-service:ghi789" \
     --resource-configuration '{"eks": {"clusterArn": "arn:aws:eks:us-east-1:333333333333:cluster/checkout-cluster", "namespaces": ["checkout"]}}'
   ```

1. **Define user journeys.**

   Create user journeys in the central account that group services by business capability:

   ```
   aws resiliencehubv2 create-user-journey \
     --system-arn "arn:aws:resiliencehub:us-east-1:111111111111:system/acme-ecommerce:abc123" \
     --name "Path to purchase" \
     --description "Customer browses, adds to cart, and completes checkout"
   ```

1. **Apply a resilience policy.**

   Create a policy and associate it with services:

   ```
   # Create a policy
   aws resiliencehubv2 create-policy \
     --name "mission-critical" \
     --availability-slo '{"target": 99.99}' \
     --multi-az '{"rtoInMinutes": 5, "rpoInMinutes": 1, "disasterRecoveryApproach": "ACTIVE_ACTIVE"}' \
     --multi-region '{"rtoInMinutes": 30, "rpoInMinutes": 5, "disasterRecoveryApproach": "WARM_STANDBY"}'
   
   # Associate with a service
   aws resiliencehubv2 update-service \
     --service-arn "arn:aws:resiliencehub:us-east-1:333333333333:service/checkout-service:ghi789" \
     --policy-arn "arn:aws:resiliencehub:us-east-1:111111111111:policy/mission-critical:xyz"
   ```

1. **Run assessments.**

   Start a failure mode assessment on each service to identify resilience gaps:

   ```
   aws resiliencehubv2 start-failure-mode-assessment \
     --service-arn "arn:aws:resiliencehub:us-east-1:333333333333:service/checkout-service:ghi789"
   ```

Services can be added incrementally – start with the most critical services and onboard more over time. The system-level view in the console shows all services across accounts in a single canvas.