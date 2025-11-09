# Amazon EC2 instance type quotas

Your AWS account has quotas that affect the number of instances that you can run
in each Region. These quotas are grouped by purchasing option.

###### Quotas

- [On-Demand Instance quotas](#on-demand-instance-quotas "#on-demand-instance-quotas")
- [Spot Instance quotas](#spot-instance-quotas "#spot-instance-quotas")
- [Dedicated Host quotas](#dedicated-host-quotas "#dedicated-host-quotas")
- [Capacity Blocks quotas](#capacity-blocks-quotas "#capacity-blocks-quotas")

## On-Demand Instance quotas

The following table shows the maximum number of vCPUs that you can provision for
On-Demand Instances. Amazon EC2 automatically increases your On-Demand Instance quotas
based on your usage. You can also request a quota increase. For more information, see
[On-Demand Instance quotas](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md#ec2-on-demand-instances-limits "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md#ec2-on-demand-instances-limits") in the _Amazon EC2 User
Guide_.

| Name                                                             | Default | Adjustable                                                                                                                                                                 |
| ---------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Running On-Demand DL instances                                   | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6E869C2A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6E869C2A") |
| Running On-Demand F instances                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-74FC7D96 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-74FC7D96") |
| Running On-Demand G and VT instances                             | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA") |
| Running On-Demand HPC instances                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F7808C92 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F7808C92") |
| Running On-Demand High Memory instances                          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-43DA4232 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-43DA4232") |
| Running On-Demand Inf instances                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1945791B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1945791B") |
| Running On-Demand P instances                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-417A185B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-417A185B") |
| Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1216C47A") |
| Running On-Demand Trn instances                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2C3B7624 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2C3B7624") |
| Running On-Demand X instances                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7295265B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7295265B") |

## Spot Instance quotas

The following table shows the maximum number of vCPUs that you can provision for Spot
Instances. Amazon EC2 automatically increases your Spot Instance quotas based on your usage.
You can also request a quota increase. For more information, see [Spot Instance quotas](../../../AWSEC2/latest/UserGuide/using-spot-limits.md "../../../AWSEC2/latest/UserGuide/using-spot-limits.md") in the _Amazon EC2 User Guide_.

| Name                                                            | Default | Adjustable                                                                                                                                                                 |
| --------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All DL Spot Instance Requests                                   | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-85EED4F7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-85EED4F7") |
| All F Spot Instance Requests                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-88CF9481 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-88CF9481") |
| All G and VT Spot Instance Requests                             | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3819A6DF "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3819A6DF") |
| All Inf Spot Instance Requests                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B5D1601B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B5D1601B") |
| All P4, P3 and P2 Spot Instance Requests                        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7212CCBC "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7212CCBC") |
| All P5 Spot Instance Requests                                   | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4BD4855 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4BD4855") |
| All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-34B43A08 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-34B43A08") |
| All Trn Spot Instance Requests                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6B0D517C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6B0D517C") |
| All X Spot Instance Requests                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E3A00192 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E3A00192") |

## Dedicated Host quotas

The following table shows the maximum number of running Dedicated Hosts that you can
allocate.

| Name                                 | Default | Adjustable                                                                                                                                                                 |
| ------------------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Running Dedicated a1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-949445B0 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-949445B0") |
| Running Dedicated c1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8365AB81 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8365AB81") |
| Running Dedicated c3 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8D142A2E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8D142A2E") |
| Running Dedicated c4 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E4BF28E0 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E4BF28E0") |
| Running Dedicated c5 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-81657574 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-81657574") |
| Running Dedicated c5a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-03F01FD8 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-03F01FD8") |
| Running Dedicated c5d Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C93F66A2 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C93F66A2") |
| Running Dedicated c5n Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-20F13EBD "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-20F13EBD") |
| Running Dedicated c6a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D75D2E84 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D75D2E84") |
| Running Dedicated c6g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A749B537 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A749B537") |
| Running Dedicated c6gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-545AED39 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-545AED39") |
| Running Dedicated c6gn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5E3A299D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5E3A299D") |
| Running Dedicated c6i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5FA3355A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5FA3355A") |
| Running Dedicated c6id Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1BBC5241 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1BBC5241") |
| Running Dedicated c6in Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6C2C40CC "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6C2C40CC") |
| Running Dedicated c7a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-698B67E5 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-698B67E5") |
| Running Dedicated c7g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-13B8FCE8 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-13B8FCE8") |
| Running Dedicated c7gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EF58B059 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EF58B059") |
| Running Dedicated c7gn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-97677CE3 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-97677CE3") |
| Running Dedicated c7i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-587AA6E3 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-587AA6E3") |
| Running Dedicated c7i-flex Hosts     | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-13DB310D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-13DB310D") |
| Running Dedicated c8g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6CB3332C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6CB3332C") |
| Running Dedicated c8gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BB2FAD1F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BB2FAD1F") |
| Running Dedicated c8gn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D2699F97 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D2699F97") |
| Running Dedicated c8i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0C0FF421 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0C0FF421") |
| Running Dedicated c8i-flex Hosts     | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C1B49A34 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C1B49A34") |
| Running Dedicated d2 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8B27377A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8B27377A") |
| Running Dedicated dl1 Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AD667A3D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AD667A3D") |
| Running Dedicated f1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5C4CD236 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5C4CD236") |
| Running Dedicated f2 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EB3A60B9 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EB3A60B9") |
| Running Dedicated g4ad Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-FD8E9B9A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-FD8E9B9A") |
| Running Dedicated g4dn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CAE24619 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CAE24619") |
| Running Dedicated g5 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A6E7FE5E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A6E7FE5E") |
| Running Dedicated g5g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4714FFEA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4714FFEA") |
| Running Dedicated g6 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B88B9D6B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B88B9D6B") |
| Running Dedicated g6e Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7069ADEB "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7069ADEB") |
| Running Dedicated g6f Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2C198A4A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2C198A4A") |
| Running Dedicated gr6 Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E68C3AFF "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E68C3AFF") |
| Running Dedicated gr6f Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-168EDD9C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-168EDD9C") |
| Running Dedicated h1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-84391ECC "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-84391ECC") |
| Running Dedicated i2 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6222C1B6 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6222C1B6") |
| Running Dedicated i3 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8E60B0B1 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8E60B0B1") |
| Running Dedicated i3en Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-77EE2B11 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-77EE2B11") |
| Running Dedicated i4g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F62CBADB "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F62CBADB") |
| Running Dedicated i4i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0300530D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0300530D") |
| Running Dedicated i7i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-ED9650A1 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-ED9650A1") |
| Running Dedicated i7ie Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A595803A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A595803A") |
| Running Dedicated i8g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1766526E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1766526E") |
| Running Dedicated i8ge Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-19A980DA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-19A980DA") |
| Running Dedicated im4gn Hosts        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-93155D6F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-93155D6F") |
| Running Dedicated inf Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5480EFD2 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5480EFD2") |
| Running Dedicated inf2 Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E5BCF7B5 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E5BCF7B5") |
| Running Dedicated is4gen Hosts       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CB4F5825 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CB4F5825") |
| Running Dedicated m1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CAF5302E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CAF5302E") |
| Running Dedicated m2 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5CBC0C23 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5CBC0C23") |
| Running Dedicated m3 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3C82F907 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3C82F907") |
| Running Dedicated m4 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EF30B25E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EF30B25E") |
| Running Dedicated m5 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8B7BF662 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8B7BF662") |
| Running Dedicated m5a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B10F70D6 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B10F70D6") |
| Running Dedicated m5ad Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-74F41837 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-74F41837") |
| Running Dedicated m5d Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8CCBD91B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8CCBD91B") |
| Running Dedicated m5dn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DA07429F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DA07429F") |
| Running Dedicated m5n Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-24D7D4AD "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-24D7D4AD") |
| Running Dedicated m5zn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BD9BD803 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BD9BD803") |
| Running Dedicated m6a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-80F2B67F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-80F2B67F") |
| Running Dedicated m6g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D50A37FA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D50A37FA") |
| Running Dedicated m6gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-84FB37AA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-84FB37AA") |
| Running Dedicated m6i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D269BEFD "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D269BEFD") |
| Running Dedicated m6id Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-FDB0A352 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-FDB0A352") |
| Running Dedicated m6idn Hosts        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9721EDD9 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9721EDD9") |
| Running Dedicated m6in Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D037CF10 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D037CF10") |
| Running Dedicated m7a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4740F819 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4740F819") |
| Running Dedicated m7g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9126620E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9126620E") |
| Running Dedicated m7gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F8516154 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F8516154") |
| Running Dedicated m7i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-30E31217 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-30E31217") |
| Running Dedicated m8g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7FD343E7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7FD343E7") |
| Running Dedicated m8gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2A9065B7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2A9065B7") |
| Running Dedicated m8i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-227FD167 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-227FD167") |
| Running Dedicated mac-m4 Hosts       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2CBA8B92 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2CBA8B92") |
| Running Dedicated mac-m4pro Hosts    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6919FC30 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6919FC30") |
| Running Dedicated mac1 Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A8448DC5 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A8448DC5") |
| Running Dedicated mac2 Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5D8DADF5 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5D8DADF5") |
| Running Dedicated mac2-m1ultra Hosts | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AE4D744C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AE4D744C") |
| Running Dedicated mac2-m2 Hosts      | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B90B5B66 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B90B5B66") |
| Running Dedicated mac2-m2pro Hosts   | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-14F120D1 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-14F120D1") |
| Running Dedicated p3 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A0A19F79 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A0A19F79") |
| Running Dedicated p3dn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B601B3B6 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B601B3B6") |
| Running Dedicated p4d Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-86A789C3 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-86A789C3") |
| Running Dedicated p4de Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-25176A65 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-25176A65") |
| Running Dedicated p5 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5136197D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5136197D") |
| Running Dedicated p5en Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-19A4C74C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-19A4C74C") |
| Running Dedicated r3 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B7208018 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B7208018") |
| Running Dedicated r4 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-313524BA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-313524BA") |
| Running Dedicated r5 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EA4FD6CF "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EA4FD6CF") |
| Running Dedicated r5a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8FE30D52 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8FE30D52") |
| Running Dedicated r5ad Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EC7178B6 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EC7178B6") |
| Running Dedicated r5b Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A2D59C67 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A2D59C67") |
| Running Dedicated r5d Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8814B54F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8814B54F") |
| Running Dedicated r5dn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4AB14223 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4AB14223") |
| Running Dedicated r5n Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-52EF324A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-52EF324A") |
| Running Dedicated r6a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BC1589C5 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BC1589C5") |
| Running Dedicated r6g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B6D6065D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B6D6065D") |
| Running Dedicated r6gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EF284EFB "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EF284EFB") |
| Running Dedicated r6i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F13A970A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F13A970A") |
| Running Dedicated r6id Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B89271A9 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B89271A9") |
| Running Dedicated r6idn Hosts        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4EABC2C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4EABC2C") |
| Running Dedicated r6in Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EA99608B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EA99608B") |
| Running Dedicated r7a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4D15192B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4D15192B") |
| Running Dedicated r7g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-67B8B4C7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-67B8B4C7") |
| Running Dedicated r7gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-01137DCE "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-01137DCE") |
| Running Dedicated r7i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-55E05032 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-55E05032") |
| Running Dedicated r7iz Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BC9FCC71 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BC9FCC71") |
| Running Dedicated r8a Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-935F9988 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-935F9988") |
| Running Dedicated r8g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5937C5FF "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5937C5FF") |
| Running Dedicated r8gb Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F5B6696D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F5B6696D") |
| Running Dedicated r8gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-89D39B5A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-89D39B5A") |
| Running Dedicated r8gn Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BCC01EAB "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BCC01EAB") |
| Running Dedicated r8i Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EEC0A186 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-EEC0A186") |
| Running Dedicated r8i-flex Hosts     | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0FBCED95 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0FBCED95") |
| Running Dedicated t1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BD62EDF4 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-BD62EDF4") |
| Running Dedicated t2 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DBCD5944 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DBCD5944") |
| Running Dedicated t3 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1586174D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-1586174D") |
| Running Dedicated trn1 Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5E4FB836 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5E4FB836") |
| Running Dedicated trn1n Hosts        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-39926A58 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-39926A58") |
| Running Dedicated u-3tb1 Hosts       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7F5506AB "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7F5506AB") |
| Running Dedicated u-6tb1 Hosts       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-89870E8E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-89870E8E") |
| Running Dedicated u7i-12tb Hosts     | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F4621520 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F4621520") |
| Running Dedicated u7i-6tb Hosts      | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4D9412E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4D9412E") |
| Running Dedicated u7i-8tb Hosts      | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9E2503C2 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9E2503C2") |
| Running Dedicated u7in-16tb Hosts    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-75B9BECB "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-75B9BECB") |
| Running Dedicated u7in-24tb Hosts    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CA51381E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-CA51381E") |
| Running Dedicated u7in-32tb Hosts    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9D28191F "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-9D28191F") |
| Running Dedicated vt1 Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A68CFBF7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A68CFBF7") |
| Running Dedicated x1 Hosts           | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DE3D9563 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DE3D9563") |
| Running Dedicated x1e Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DEF8E115 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DEF8E115") |
| Running Dedicated x2gd Hosts         | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5CC9EA82 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5CC9EA82") |
| Running Dedicated x2idn Hosts        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A84ABF80 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-A84ABF80") |
| Running Dedicated x2iedn Hosts       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D0AA08B1 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D0AA08B1") |
| Running Dedicated x2iezn Hosts       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-888B4496 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-888B4496") |
| Running Dedicated x8g Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2CC6888D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2CC6888D") |
| Running Dedicated z1d Hosts          | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F035E935 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-F035E935") |

## Capacity Blocks quotas

The following table shows the maximum number of vCPUs for concurrently active
Capacity Blocks.

| Name                                             | Default | Adjustable                                                                                                                                                                 |
| ------------------------------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Concurrent P4d Capacity Blocks per account       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2C8F52B3 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2C8F52B3") |
| Concurrent P4d Capacity Blocks per organization  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B67430DE "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B67430DE") |
| Concurrent P5 Capacity Blocks per account        | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DA6814F2 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DA6814F2") |
| Concurrent P5 Capacity Blocks per organization   | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8131B2C6 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8131B2C6") |
| Concurrent P5e Capacity Blocks per account       | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C45F30BC "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C45F30BC") |
| Concurrent P5e Capacity Blocks per organization  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AD1D1866 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AD1D1866") |
| Concurrent P5en Capacity Blocks per account      | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4F9BB70B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-4F9BB70B") |
| Concurrent P5en Capacity Blocks per organization | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7EA86503 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7EA86503") |
| Concurrent Trn1 Capacity Blocks per account      | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2E30FD7D "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-2E30FD7D") |
| Concurrent Trn1 Capacity Blocks per organization | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4947F9A "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-C4947F9A") |
| Concurrent Trn2 Capacity Blocks per account      | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-64569A79 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-64569A79") |
| Concurrent Trn2 Capacity Blocks per organization | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-24E8B4C0 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-24E8B4C0") |
