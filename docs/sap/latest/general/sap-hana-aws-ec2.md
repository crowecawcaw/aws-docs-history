# SAP HANA certified and non-certified instances

AWS has worked closely with SAP to test and certify Amazon EC2 instance types for SAP on AWS solutions.

Previous generation Amazon EC2 instances for SAP HANA are fully supported and these instance types retain the same features and functionality. We recommend using the current generation Amazon EC2 instance for new SAP HANA implementations or migrations.

All current and previous generation Amazon EC2 instance types for SAP HANA can be used for running non-production workloads. For more information, see [SAP Note 2271345](https://me.sap.com/notes/2271345 "https://me.sap.com/notes/2271345").

###### Contents

- [Current generation certified instances](sap-hana-aws-ec2.md#current-gen-hana-ec2 "sap-hana-aws-ec2.md#current-gen-hana-ec2")
  - [SAP HANA OLTP and OLAP Scale-up](sap-hana-aws-ec2.md#scale-up-current "sap-hana-aws-ec2.md#scale-up-current")
  - [SAP HANA OLTP and OLAP Scale-out](sap-hana-aws-ec2.md#scale-out-current "sap-hana-aws-ec2.md#scale-out-current")

- [Previous generation certified instances](sap-hana-aws-ec2.md#previous-gen-hana-ec2 "sap-hana-aws-ec2.md#previous-gen-hana-ec2")
  - [SAP HANA OLTP and OLAP Scale-up](sap-hana-aws-ec2.md#scale-up-previous "sap-hana-aws-ec2.md#scale-up-previous")
  - [SAP HANA OLTP and OLAP Scale-out](sap-hana-aws-ec2.md#scale-out-previous "sap-hana-aws-ec2.md#scale-out-previous")

- [Non-certified instances](sap-hana-aws-ec2.md#non-certified-hana "sap-hana-aws-ec2.md#non-certified-hana")

## Current generation certified instances

### SAP HANA OLTP and OLAP Scale-up

| Instance type        | vCPU  | Memory (GiB) | SAPS      | aSAPS   | Network (Gbps) | Storage (Mbps) | SAP HANA OLTP prod | SAP HANA OLTP sizing | SAP HANA OLAP prod | SAP HANA OLAP sizing | FSx for ONTAP |
| -------------------- | ----- | ------------ | --------- | ------- | -------------- | -------------- | ------------------ | -------------------- | ------------------ | -------------------- | ------------- |
| r5.8xlarge           | 32    | 256          | 46,257    | N/A     | 10             | 6,800          | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5.12xlarge          | 48    | 384          | 69,385    | N/A     | 10             | 9,500          | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5.16xlarge          | 64    | 512          | 92,513    | N/A     | 20             | 13,600         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5.24xlarge          | 96    | 768          | 138,770   | N/A     | 25             | 19,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5.metal             | 96    | 768          | 143,230   | N/A     | 25             | 19,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5b.8xlarge          | 32    | 256          | 46,257    | N/A     | 25             | 20,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5b.12xlarge         | 48    | 384          | 69,385    | N/A     | 50             | 30,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5b.16xlarge         | 64    | 512          | 92,513    | N/A     | 75             | 40,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5b.24xlarge         | 96    | 768          | 138,770   | N/A     | 100            | 60,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r5b.metal            | 96    | 768          | 143,230   | N/A     | 100            | 60,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| r6i.8xlarge          | 32    | 256          | 49,013    | N/A     | 12.5           | 10,000         | ✓                  | Standard             | ✗                  | N/A                  | ✗             |
| r6i.12xlarge         | 48    | 384          | 73,519    | N/A     | 18.75          | 15,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r6i.16xlarge         | 64    | 512          | 98,025    | N/A     | 25             | 20,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r6i.24xlarge         | 96    | 768          | 147,038   | N/A     | 37.5           | 30,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r6i.32xlarge         | 128   | 1,024        | 196,050   | N/A     | 50             | 40,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r7i.8xlarge          | 32    | 256          | 66,480    | N/A     | 12.5           | 10,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r7i.12xlarge         | 48    | 384          | 99,720    | N/A     | 18.75          | 15,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r7i.16xlarge         | 64    | 512          | 105,500   | N/A     | 25             | 20,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r7i.24xlarge         | 96    | 768          | 158,250   | N/A     | 37.5           | 30,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r7i.48xlarge         | 192   | 1536         | 296,200   | N/A     | 50             | 40,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r8i.12xlarge         | 48    | 384          | 115,270   | 17,763  | 22.5           | 15,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r8i.16xlarge         | 64    | 512          | 138,840   | 23,683  | 30             | 20,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r8i.24xlarge         | 96    | 768          | 208,260   | 35,525  | 40             | 30,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r8i.32xlarge         | 128   | 1024         | 277,680   | 47,367  | 50             | 40,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r8i.48xlarge         | 192   | 1536         | 416,520   | 71,050  | 75             | 60,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| r8i.96xlarge         | 384   | 3072         | 740,050   | 142,100 | 100            | 80,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| u-3tb1.56xlarge      | 224   | 3,072        | 237,750   | N/A     | 50             | 19,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| u-6tb1.56xlarge      | 224   | 6,144        | 380,770   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| u-6tb1.112xlarge     | 448   | 6,144        | 475,500   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| u-6tb1.metal         | 448   | 6,144        | 480,600   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| u-9tb1.112xlarge     | 448   | 9,216        | 475,500   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| u-9tb1.metal         | 448   | 9,216        | 480,600   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Workload             | ✗             |
| u-12tb1.112xlarge    | 448   | 12,288       | 475,500   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| u-12tb1.metal        | 448   | 12,288       | 480,600   | N/A     | 100            | 38,000         | ✓                  | Standard             | ✓                  | Workload             | ✗             |
| u-18tb1.112xlarge    | 448   | 18,432       | 520,330   | N/A     | 100            | 38,000         | ✓                  | Workload             | ✓                  | Workload             | ✓             |
| u-18tb1.metal        | 448   | 18,432       | 534,130   | N/A     | 100            | 38,000         | ✓                  | Workload             | ✓                  | Workload             | ✗             |
| u-24tb1.112xlarge    | 448   | 24,576       | 508,720   | N/A     | 100            | 38,000         | ✓                  | Workload             | ✗                  | N/A                  | ✓             |
| u-24tb1.metal        | 448   | 24,576       | 517,480   | N/A     | 100            | 38,000         | ✓                  | Workload             | ✗                  | N/A                  | ✗             |
| u7i-6tb.112xlarge    | 448   | 6,144        | 670,265   | N/A     | 100            | 60,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| u7i-8tb.112xlarge    | 448   | 8,192        | 674,950   | N/A     | 100            | 60,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| u7i-12tb.224xlarge   | 896   | 12,288       | 1,254,030 | N/A     | 100            | 60,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| u7in-16tb.224xlarge  | 896   | 16,384       | 1,281,620 | N/A     | 200            | 100,000        | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| u7in-24tb.224xlarge  | 896   | 24,576       | 1,225,150 | N/A     | 200            | 100,000        | ✓                  | Workload             | ✓                  | Workload             | ✓             |
| u7inh-32tb.480xlarge | 1,920 | 32,768       | N/A       | N/A     | 200            | 160,000        | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| x1.16xlarge          | 64    | 976          | 65,750    | N/A     | 10             | 7,000          | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| x1.32xlarge          | 128   | 1,952        | 131,500   | N/A     | 25             | 14,000         | ✓                  | Standard             | ✓                  | Standard             | ✗             |
| x1e.32xlarge         | 128   | 3,904        | 131,500   | N/A     | 25             | 14,000         | ✓                  | Standard             | ✓                  | Workload             | ✗             |
| x2idn.16xlarge       | 64    | 1,024        | 98,025    | N/A     | 50             | 40,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| x2idn.24xlarge       | 96    | 1,536        | 147,038   | N/A     | 75             | 60,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| x2idn.32xlarge       | 128   | 2,048        | 196,050   | N/A     | 100            | 80,000         | ✓                  | Standard             | ✓                  | Standard             | ✓             |
| x2iedn.24xlarge      | 96    | 3,072        | 141,750   | N/A     | 75             | 60,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |
| x2iedn.32xlarge      | 128   | 4,096        | 189,000   | N/A     | 100            | 80,000         | ✓                  | Standard             | ✓                  | Workload             | ✓             |

### SAP HANA OLTP and OLAP Scale-out

| Instance type        | vCPU  | Memory (GiB) | SAPS      | aSAPS | Network (Gbps) | Storage (Mbps) | SAP HANA OLTP prod | SAP HANA OLTP sizing | OLTP Max nodes | SAP HANA OLAP prod | SAP HANA OLAP sizing | OLAP Max nodes | FSx for ONTAP |
| -------------------- | ----- | ------------ | --------- | ----- | -------------- | -------------- | ------------------ | -------------------- | -------------- | ------------------ | -------------------- | -------------- | ------------- |
| r5.24xlarge          | 96    | 768          | 138,770   | N/A   | 25             | 19,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 16             | ✗             |
| r6i.24xlarge         | 96    | 768          | 147,038   | N/A   | 37.5           | 30,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 16             | ✓             |
| r6i.32xlarge         | 128   | 1,024        | 196,050   | N/A   | 50             | 40,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 16             | ✓             |
| u-6tb1.56xlarge      | 224   | 6,144        | 380,770   | N/A   | 100            | 38,000         | ✓                  | Standard             | 4              | ✓                  | Workload             | 16             | ✓             |
| u-6tb1.112xlarge     | 448   | 6,144        | 475,500   | N/A   | 100            | 38,000         | ✓                  | Standard             | 4              | ✓                  | Standard             | 16             | ✓             |
| u-6tb1.metal         | 448   | 6,144        | 480,600   | N/A   | 100            | 38,000         | ✓                  | Standard             | 4              | ✓                  | Standard             | 16             | ✗             |
| u-9tb1.112xlarge     | 448   | 9,216        | 475,500   | N/A   | 100            | 38,000         | ✓                  | Standard             | 4              | ✓                  | Workload             | 16             | ✓             |
| u-12tb1.112xlarge    | 448   | 12,288       | 475,500   | N/A   | 100            | 38,000         | ✓                  | Standard             | 4              | ✓                  | Workload             | 16             | ✓             |
| u-12tb1.metal        | 448   | 12,288       | 480,600   | N/A   | 100            | 38,000         | ✓                  | Standard             | 4              | ✗                  | N/A                  | N/A            | ✗             |
| u7i-6tb.112xlarge    | 448   | 6,144        | 670,265   | N/A   | 100            | 60,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 16             | ✗             |
| u7i-8tb.112xlarge    | 448   | 8,192        | 674,950   | N/A   | 100            | 60,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 16             | ✗             |
| u7in-12tb.224xlarge  | 896   | 12,288       | 1,254,030 | N/A   | 100            | 60,000         | ✓                  | Standard             | 4              | ✓                  | Standard             | 8              | ✓             |
| u7in-16tb.224xlarge  | 896   | 16,384       | 1,281,620 | N/A   | 200            | 100,000        | ✓                  | Standard             | 4              | ✓                  | Standard             | 8              | ✓             |
| u7in-24tb.224xlarge  | 896   | 24,576       | 1,225,150 | N/A   | 200            | 100,000        | ✓                  | Workload             | 4              | ✓                  | Workload             | 8              | ✓             |
| u7inh-32tb.480xlarge | 1,920 | 32,768       | N/A       | N/A   | 200            | 160,000        | ✓                  | Standard             | 4              | ✓                  | Workload             | 8              | ✗             |
| x1.16xlarge          | 64    | 976          | 65,750    | N/A   | 10             | 7,000          | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 7              | ✗             |
| x1.32xlarge          | 128   | 1,952        | 131,500   | N/A   | 25             | 14,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 25             | ✗             |
| x1e.32xlarge         | 128   | 3,904        | 131,500   | N/A   | 25             | 14,000         | ✗                  | N/A                  | N/A            | ✓                  | Workload             | 25             | ✗             |
| x2idn.16xlarge       | 64    | 1,024        | 98,025    | N/A   | 50             | 40,000         | ✗                  | N/A                  | N/A            | ✓                  | Standard             | 16             | ✓             |
| x2idn.24xlarge       | 96    | 1,536        | 147,038   | N/A   | 75             | 60,000         | ✗                  | N/A                  | N/A            | ✓                  | Workload             | 16             | ✓             |
| x2idn.32xlarge       | 128   | 2,048        | 196,050   | N/A   | 100            | 80,000         | ✗                  | N/A                  | N/A            | ✓                  | Workload             | 16             | ✓             |
| x2iedn.24xlarge      | 96    | 3,072        | 141,750   | N/A   | 75             | 60,000         | ✗                  | N/A                  | N/A            | ✓                  | Workload             | 16             | ✓             |
| x2iedn.32xlarge      | 128   | 4,096        | 189,000   | N/A   | 100            | 80,000         | ✗                  | N/A                  | N/A            | ✓                  | Workload             | 16             | ✓             |

## Previous generation certified instances

### SAP HANA OLTP and OLAP Scale-up

| Instance type | vCPU | Memory (GiB) | SAPS   | SAP HANA OLTP prod | SAP HANA OLTP sizing | SAP HANA OLAP prod | SAP HANA OLAP sizing |
| ------------- | ---- | ------------ | ------ | ------------------ | -------------------- | ------------------ | -------------------- |
| r3.2xlarge    | 8    | 61           | 7,980  | ✗                  | Standard             | ✗                  | Standard             |
| r3.4xlarge    | 16   | 122          | 15,960 | ✗                  | Standard             | ✗                  | Standard             |
| r3.8xlarge    | 32   | 244          | 31,920 | ✓                  | Standard             | ✓                  | Standard             |
| r4.8xlarge    | 32   | 244          | 38,200 | 10                 | 7,000                | ✓                  | Standard             |
| r4.16xlarge   | 64   | 488          | 76,400 | 25                 | 14,000               | ✓                  | Standard             |

### SAP HANA OLTP and OLAP Scale-out

| Instance type | vCPU | Memory (GiB) | SAPS   | SAP HANA OLTP prod | SAP HANA OLTP sizing | SAP HANA OLAP prod | SAP HANA OLAP sizing |
| ------------- | ---- | ------------ | ------ | ------------------ | -------------------- | ------------------ | -------------------- |
| r3.8xlarge    | 32   | 244          | 31,920 | ✗                  | N/A                  | ✓                  | Standard             |

## Non-certified instances

The Amazon EC2 instances in the following table are not certified for production usage. You can use them for running non-production workloads. For more information, see [SAP Note 2271345 – Cost-Optimized SAP HANA Hardware for Non-Production Usage](https://me.sap.com/notes/2271345 "https://me.sap.com/notes/2271345") (SAP portal access required).

| Instance type   | vCPU | Memory (GiB) | SAPS   | Network (Gbps) | Storage (Mbps) | FSx for ONTAP |
| --------------- | ---- | ------------ | ------ | -------------- | -------------- | ------------- |
| r4.2xlarge      | 8    | 61           | 9,550  | Up to 10       | 1,700          | ✗             |
| r4.4xlarge      | 16   | 122          | 19,100 | Up to 10       | 3,500          | ✗             |
| r5.2xlarge      | 8    | 64           | 11,564 | Up to 10       | Up to 4,750    | ✗             |
| r5.4xlarge      | 16   | 128          | 23,128 | Up to 10       | 4,750          | ✗             |
| r5b.2xlarge     | 8    | 64           | 11,564 | Up to 10       | Up to 10,000   | ✗             |
| r5b.4xlarge     | 16   | 128          | 23,128 | Up to 10       | 10,000         | ✗             |
| r6i.2xlarge     | 8    | 64           | 12,253 | Up to 12.5     | Up to 10,000   | ✗             |
| r6i.4xlarge     | 16   | 128          | 24,506 | Up to 12.5     | Up to 10,000   | ✗             |
| x1e.xlarge      | 4    | 122          | 4,109  | Up to 10       | 500            | ✗             |
| x1e.2xlarge     | 8    | 244          | 8,219  | Up to 10       | 1,000          | ✗             |
| x1e.4xlarge     | 16   | 488          | 16,437 | Up to 10       | 1,750          | ✗             |
| x2iedn.xlarge   | 4    | 128          | 5,906  | Up to 25       | Up to 20,000   | ✗             |
| x2iedn.2xlarge  | 8    | 256          | 11,813 | Up to 25       | Up tp 20,000   | ✗             |
| x2iedn.4xlarge  | 16   | 512          | 23,625 | Up to 25       | Up to 20,000   | ✗             |
| x2iedn.8xlarge  | 32   | 1,024        | 47,250 | 25             | 20,000         | ✗             |
| x2iedn.16xlarge | 64   | 2,048        | 94,500 | 50             | 40,000         | ✗             |
