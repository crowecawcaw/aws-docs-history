

# Using I-ODCRs with AWS PCS
<a name="capacity-reservations-iodcr"></a>

 Interruptible On-Demand Capacity Reservations (I-ODCRs) let ODCR owners temporarily share unused reserved capacity with other accounts in their AWS organization. Consumer instances receive a **2-minute termination warning** when the owner reclaims capacity, making I-ODCRs suitable for fault-tolerant workloads such as batch processing, ML training, and data analysis. 

 For more information about I-ODCRs, see [ Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html) in the *Amazon Elastic Compute Cloud User Guide*. 

## How I-ODCRs work with AWS PCS
<a name="capacity-reservations-iodcr-how-it-works"></a>

 An I-ODCR is created from an existing source ODCR. The owner specifies how many instances to allocate to the interruptible reservation. Those instances are transferred from the source ODCR to the new I-ODCR. The owner can reclaim capacity at any time, which terminates consumer instances with a 2-minute notice. 

Key characteristics:
+ I-ODCRs are **targeted** by default — consumers must reference the reservation ID in their launch configuration.
+ I-ODCRs **cannot** be added to Capacity Reservation groups.
+ Only **one** interruptible allocation can be created per source ODCR.
+ When the owner reclaims capacity, there is **no fallback** to On-Demand or Spot — consumer instances are terminated.

## Configuring an AWS PCS compute node group to use an I-ODCR
<a name="capacity-reservations-iodcr-configure"></a>

 You can configure an AWS PCS compute node group to use a shared I-ODCR by adding it to a launch template. Here are the steps: 
+  **Ensure you have access to the I-ODCR.** The ODCR owner must share the interruptible reservation with your account using [AWS Resource Access Manager (RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html). Once shared, the I-ODCR appears in your account under **Capacity Reservations** on the Amazon EC2 console. 
+  **Create a launch template that targets the I-ODCR.** Reference the I-ODCR ID directly and set the market type to `interruptible-capacity-reservation`. Here is an example launch template: 

  ```
  {
    "CapacityReservationSpecification": {
      "CapacityReservationTarget": {
        "CapacityReservationId": "cr-1234567890abcdef1"
      }
    },
    "InstanceMarketOptions": {
      "MarketType": "interruptible-capacity-reservation"
    }
  }
  ```
+  **Create or update an AWS PCS compute node group** to use the launch template. For more information, see [AWS PCS compute node groups](working-with_cng.md). 
  + Set the `purchaseOption` of the compute node group to `INTERRUPTIBLE_CAPACITY_RESERVATION`.

## Handling interruptions
<a name="capacity-reservations-iodcr-interruptions"></a>

 When the I-ODCR owner reclaims capacity, consumer instances receive a 2-minute termination warning through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). To handle interruptions gracefully in your AWS PCS workloads: 
+ Configure your applications to listen for EventBridge interruption events.
+ Implement checkpointing so jobs can save intermediate results and resume after interruption.
+ For compute node groups with a dynamic scaling configuration, set the minimum instance count to `0` so the group can scale down gracefully when capacity is reclaimed.

 For more information about monitoring interruption events, see [Monitor interruptible Capacity Reservations with EventBridge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-interruptible-cr.html) in the *Amazon Elastic Compute Cloud User Guide*. 

## Example: Share and use hpc7a.96xlarge instances with an I-ODCR
<a name="capacity-reservations-iodcr-example"></a>

 This example walks through creating an I-ODCR from an existing ODCR and using it with an AWS PCS compute node group. 

 **Step 1: Create the interruptible reservation from a source ODCR.** 

 The ODCR owner creates an interruptible allocation of 16 instances from their existing 32-instance reservation: 

```
aws ec2 create-interruptible-capacity-reservation-allocation \
    --capacity-reservation-id cr-source1234567890a \
    --instance-count 16
```

 The source ODCR now shows 16 instances, and a new I-ODCR is created with 16 instances. 

 **Step 2: Share the I-ODCR using AWS RAM.** 

 The owner shares the I-ODCR with the consumer account: 

```
aws ram create-resource-share \
    --name "HPC-Interruptible-Share" \
    --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity-reservation/cr-interruptible456 \
    --principals 987654321098
```

 **Step 3: Create a launch template targeting the I-ODCR.** 

 The consumer creates a launch template: 

```
{
  "CapacityReservationSpecification": {
    "CapacityReservationTarget": {
      "CapacityReservationId": "cr-interruptible456"
    }
  },
  "InstanceMarketOptions": {
    "MarketType": "interruptible-capacity-reservation"
  }
}
```

 **Step 4: Create an AWS PCS compute node group using the launch template.** 

 Create a dynamic compute node group with `purchaseOption` set to `INTERRUPTIBLE_CAPACITY_RESERVATION` and the launch template referencing the I-ODCR. Set the minimum instance count to 0 and the maximum to 16 (matching the I-ODCR capacity). 

## Billing considerations
<a name="capacity-reservations-iodcr-billing"></a>
+ The **ODCR owner** pays On-Demand rates for unused capacity in the I-ODCR (instances not launched by the consumer).
+ The **consumer** pays On-Demand rates only for instances they actually launch and use.

 For more information, see [Capacity Reservation pricing and billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html) in the *Amazon Elastic Compute Cloud User Guide*. 