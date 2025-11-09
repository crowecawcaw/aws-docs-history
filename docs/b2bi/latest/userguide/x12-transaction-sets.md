# Supported X12 transaction sets

ANSI X12 defines and maintains transaction sets that establish the data content exchanged
for specific business purposes. Transaction sets are identified by a numeric identifier and
a name. For more details about X12 transaction sets, see [X12 Transaction Sets](https://x12.org/products/transaction-sets "https://x12.org/products/transaction-sets"). The
following table lists the X12 transaction sets that AWS B2B Data Interchange currently supports.

###### Note

AWS B2B Data Interchange supports all transactions that are available for the 4010, 4030, 4050, 4060, and
5010 versions.

| Transaction set | Description                                                        | Category                    | 4010 | 4030 | 4050 | 4060 | 5010 |
| --------------- | ------------------------------------------------------------------ | --------------------------- | ---- | ---- | ---- | ---- | ---- |
| 100             | Insurance Plan Description                                         | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 101             | Name and Address Lists                                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 102             | Associated Data                                                    | Communications and Controls | N/A  | Yes  | Yes  | Yes  | Yes  |
| 103             | Abandoned Property Filings                                         | Finance                     | N/A  | Yes  | Yes  | Yes  | Yes  |
| 104             | Air Shipment Information                                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 105             | Business Entity Filings                                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 106             | Motor Carrier Rate Proposal                                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 107             | Request for Motor Carrier Rate Proposal                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 108             | Response to a Motor Carrier Rate Proposal                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 109             | Vessel Content Details                                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 110             | Air Freight Details and Invoice                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 111             | Individual Insurance Policy and Client Information                 | Insurance                   | N/A  | Yes  | Yes  | Yes  | Yes  |
| 112             | Property Damage Report                                             | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 113             | Election Campaign and Lobbyist Reporting                           | Finance                     | N/A  | Yes  | Yes  | Yes  | Yes  |
| 120             | Vehicle Shipping Order                                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 121             | Vehicle Service                                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 124             | Vehicle Damage                                                     | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 125             | Multilevel Railcar Load Details                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 126             | Vehicle Application Advice                                         | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 127             | Vehicle Baying Order                                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 128             | Dealer Information                                                 | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 129             | Vehicle Carrier Rate Update                                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 130             | Student Educational Record (Transcript)                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 131             | Student Educational Record (Transcript) Acknowledgment             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 132             | Human Resource Information                                         | Finance                     | N/A  | N/A  | Yes  | Yes  | Yes  |
| 133             | Educational Institution Record                                     | Finance                     | N/A  | N/A  | Yes  | Yes  | Yes  |
| 135             | Student Aid Origination Record                                     | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 138             | Educational Testing and Prospect Request and Report                | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 139             | Student Loan Guarantee Result                                      | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 140             | Product Registration                                               | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 141             | Product Service Claim Response                                     | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 142             | Product Service Claim                                              | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 143             | Product Service Notification                                       | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 144             | Student Loan Transfer and Status Verification                      | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 146             | Request for Student Educational Record (Transcript)                | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 147             | Response to Request for Student Educational Record (Transcript)    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 148             | Report of Injury, Illness or Incident                              | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 149             | Notice of Tax Adjustment or Assessment                             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 150             | Tax Rate Notification                                              | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 151             | Electronic Filing of Tax Return Data Acknowledgment                | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 152             | Statistical Government Information                                 | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 153             | Unemployment Insurance Tax Claim or Charge Information             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 154             | Secured Interest Filing                                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 155             | Business Credit Report                                             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 157             | Notice of Power of Attorney                                        | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 158             | Tax Jurisdiction Sourcing                                          | Finance                     | N/A  | N/A  | N/A  | Yes  | Yes  |
| 159             | Motion Picture Booking Confirmation                                | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 160             | Transportation Automatic Equipment Identification                  | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 161             | Train Sheet                                                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 163             | Transportation Appointment Schedule Information                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 170             | Revenue Receipts Statement                                         | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 175             | Court and Law Enforcement Notice                                   | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 176             | Court Submission                                                   | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 179             | Environmental Compliance Reporting                                 | Finance                     | N/A  | N/A  | Yes  | Yes  | Yes  |
| 180             | Return Merchandise Authorization and Notification                  | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 185             | Royalty Regulatory Report                                          | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 186             | Insurance Underwriting Requirements Reporting                      | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 187             | Premium Audit Request and Return                                   | Insurance                   | N/A  | Yes  | Yes  | Yes  | Yes  |
| 188             | Educational Course Inventory                                       | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 189             | Application for Admission to Educational Institutions              | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 190             | Student Enrollment Verification                                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 191             | Student Loan Pre-Claims and Claims                                 | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 194             | Grant or Assistance Application                                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 195             | Federal Communications Commission (FCC) License Application        | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 196             | Contractor Cost Data Reporting                                     | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 197             | Real Estate Title Evidence                                         | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 198             | Loan Verification Information                                      | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 199             | Real Estate Settlement Information                                 | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 200             | Mortgage Credit Report                                             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 201             | Residential Loan Application                                       | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 202             | Secondary Mortgage Market Loan Delivery                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 203             | Secondary Mortgage Market Investor Report                          | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 204             | Motor Carrier Load Tender                                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 205             | Mortgage Note                                                      | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 206             | Real Estate Inspection                                             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 210             | Motor Carrier Freight Details and Invoice                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 211             | Motor Carrier Bill of Lading                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 212             | Motor Carrier Delivery Trailer Manifest                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 213             | Motor Carrier Shipment Status Inquiry                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 214             | Transportation Carrier Shipment Status Message                     | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 215             | Motor Carrier Pickup Manifest                                      | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 216             | Motor Carrier Shipment Pickup Notification                         | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 217             | Motor Carrier Loading and Route Guide                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 218             | Motor Carrier Tariff Information                                   | Transportation              | Yes  | Yes  | N/A  | N/A  | N/A  |
| 219             | Logistics Service Request                                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 220             | Logistics Service Response                                         | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 222             | Cartage Work Assignment                                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 223             | Consolidators Freight Bill and Invoice                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 224             | Motor Carrier Summary Freight Bill Manifest                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 225             | Response to a Cartage Work Assignment                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 227             | Trailer Usage Report                                               | Transportation              | N/A  | Yes  | Yes  | Yes  | Yes  |
| 228             | Equipment Inspection Report                                        | Transportation              | N/A  | N/A  | N/A  | N/A  | Yes  |
| 240             | Motor Carrier Package Status                                       | Transportation              | N/A  | Yes  | Yes  | Yes  | Yes  |
| 242             | Data Status Tracking                                               | Communications and Controls | Yes  | Yes  | Yes  | Yes  | Yes  |
| 244             | Product Source Information                                         | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 245             | Real Estate Tax Service Response                                   | Finance                     | N/A  | Yes  | Yes  | Yes  | Yes  |
| 248             | Account Assignment/Inquiry and Service/Status                      | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 249             | Animal Toxicological Data                                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 250             | Purchase Order Shipment Management Document                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 251             | Pricing Support                                                    | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 252             | Insurance Producer Administration                                  | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 255             | Underwriting Information Services                                  | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 256             | Periodic Compensation                                              | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 259             | Residential Mortgage Insurance Explanation of Benefits             | Finance                     | N/A  | N/A  | N/A  | Yes  | Yes  |
| 260             | Application for Mortgage Insurance Benefits                        | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 261             | Real Estate Information Request                                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 262             | Real Estate Information Report                                     | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 263             | Residential Mortgage Insurance Application Response                | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 264             | Mortgage Loan Default Status                                       | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 265             | Real Estate Title Insurance Services Order                         | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 266             | Mortgage or Property Record Change Notification                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 267             | Individual Life, Annuity and Disability Application                | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 268             | Annuity Activity                                                   | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 269             | Health Care Benefit Coordination Verification                      | Insurance                   | N/A  | N/A  | Yes  | Yes  | Yes  |
| 270             | Eligibility, Coverage or Benefit Inquiry                           | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 271             | Eligibility, Coverage or Benefit Information                       | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 272             | Property and Casualty Loss Notification                            | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 273             | Insurance/Annuity Application Status                               | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 274             | Healthcare Provider Information                                    | Insurance                   | N/A  | Yes  | Yes  | Yes  | Yes  |
| 275             | Patient Information                                                | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 276             | Health Care Claim Status Request                                   | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 277             | Health Care Information Status Notification                        | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 278             | Health Care Services Review Information                            | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 280             | Voter Registration Information                                     | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 283             | Tax or Fee Exemption Certification                                 | Finance                     | N/A  | Yes  | Yes  | Yes  | Yes  |
| 284             | Commercial Vehicle Safety Reports                                  | Transportation              | N/A  | Yes  | Yes  | Yes  | Yes  |
| 285             | Commercial Vehicle Safety and Credentials Information Exchange     | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 286             | Commercial Vehicle Credentials                                     | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 288             | Wage Determination                                                 | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 290             | Cooperative Advertising Agreements                                 | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 300             | Reservation (Booking Request) (Ocean)                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 301             | Confirmation (Ocean)                                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 303             | Booking Cancellation (Ocean)                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 304             | Shipping Instructions                                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 309             | Customs Manifest                                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 310             | Freight Receipt and Invoice (Ocean)                                | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 311             | Canada Customs Information                                         | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 312             | Arrival Notice (Ocean)                                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 313             | Shipment Status Inquiry (Ocean)                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 315             | Status Details (Ocean)                                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 317             | Delivery/Pickup Order                                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 319             | Terminal Information                                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 322             | Terminal Operations and Intermodal Ramp Activity                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 323             | Vessel Schedule and Itinerary (Ocean)                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 324             | Vessel Stow Plan (Ocean)                                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 325             | Consolidation of Goods In Container                                | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 326             | Consignment Summary List                                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 350             | Customs Status Information                                         | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 352             | U.S. Customs Carrier General Order Status                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 353             | Customs Events Advisory Details                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 354             | U.S. Customs Automated Manifest Archive Status                     | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 355             | U.S. Customs Acceptance/Rejection                                  | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 356             | U.S. Customs Permit to Transfer Request                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 357             | U.S. Customs In-Bond Information                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 358             | Customs Consist Information                                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 361             | Carrier Interchange Agreement (Ocean)                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 362             | Cargo Insurance Advice of Shipment                                 | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 404             | Rail Carrier Shipment Information                                  | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 410             | Rail Carrier Freight Details and Invoice                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 412             | Trailer or Container Repair Billing                                | Transportation              | N/A  | Yes  | Yes  | Yes  | Yes  |
| 414             | Rail Carhire Settlements                                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 417             | Rail Carrier Waybill Interchange                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 418             | Rail Advance Interchange Consist                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 419             | Advance Car Disposition                                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 420             | Car Handling Information                                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 421             | Estimated Time of Arrival and Car Scheduling                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 422             | Equipment Order                                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 423             | Rail Industrial Switch List                                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 424             | Rail Carrier Services Settlement                                   | Transportation              | N/A  | N/A  | Yes  | Yes  | Yes  |
| 425             | Rail Waybill Request                                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 426             | Rail Revenue Waybill                                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 429             | Railroad Retirement Activity                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 431             | Railroad Station Master File                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 432             | Rail Deprescription                                                | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 433             | Railroad Reciprocal Switch File                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 434             | Railroad Mark Register Update Activity                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 435             | Standard Transportation Commodity Code Master                      | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 436             | Locomotive Information                                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 437             | Railroad Junctions and Interchanges Activity                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 440             | Shipment Weights                                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 451             | Railroad Event Report                                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 452             | Railroad Problem Log Inquiry or Advice                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 453             | Railroad Service Commitment Advice                                 | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 455             | Railroad Parameter Trace Registration                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 456             | Railroad Equipment Inquiry or Advice                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 460             | Railroad Price Distribution Request or Response                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 463             | Rail Rate Reply                                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 466             | Rate Request                                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 468             | Rate Docket Journal Log                                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 470             | Railroad Clearance                                                 | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 475             | Rail Route File Maintenance                                        | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 485             | Ratemaking Action                                                  | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 486             | Rate Docket Expiration                                             | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 490             | Rate Group Definition                                              | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 492             | Miscellaneous Rates                                                | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 494             | Rail Scale Rates                                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 500             | Medical Event Reporting                                            | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 501             | Vendor Performance Review                                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 503             | Pricing History                                                    | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 504             | Clauses and Provisions                                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 511             | Requisition                                                        | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 517             | Material Obligation Validation                                     | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 521             | Income or Asset Offset                                             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 527             | Material Due-In and Receipt                                        | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 536             | Logistics Reassignment                                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 540             | Notice of Employment Status                                        | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 561             | Contract Abstract                                                  | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 567             | Contract Completion Status                                         | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 568             | Contract Payment Management Report                                 | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 601             | U.S. Customs Export Shipment Information                           | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 602             | Transportation Services Tender                                     | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 620             | Excavation Communication                                           | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 625             | Well Information                                                   | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 650             | Maintenance Service Order                                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 715             | Intermodal Group Loading Plan                                      | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 753             | Request for Routing Instructions                                   | Supply Chain                | N/A  | Yes  | Yes  | Yes  | Yes  |
| 754             | Routing Instructions                                               | Supply Chain                | N/A  | Yes  | Yes  | Yes  | Yes  |
| 805             | Contract Pricing Proposal                                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 806             | Project Schedule Reporting                                         | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 810             | Invoice                                                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 811             | Consolidated Service Invoice/Statement                             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 812             | Credit/Debit Adjustment                                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 813             | Electronic Filing of Tax Return Data                               | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 814             | General Request, Response or Confirmation                          | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 815             | Cryptographic Service Message                                      | Communications and Controls | Yes  | Yes  | Yes  | Yes  | Yes  |
| 816             | Organizational Relationships                                       | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 818             | Commission Sales Report                                            | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 819             | Joint Interest Billing and Operating Expense Statement             | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 820             | Payment Order/Remittance Advice                                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 821             | Financial Information Reporting                                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 822             | Account Analysis                                                   | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 823             | Lockbox                                                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 824             | Application Advice                                                 | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 826             | Tax Information Exchange                                           | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 827             | Financial Return Notice                                            | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 828             | Debit Authorization                                                | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 829             | Payment Cancellation Request                                       | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 830             | Planning Schedule with Release Capability                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 831             | Application Control Totals                                         | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 832             | Price/Sales Catalog                                                | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 833             | Mortgage Credit Report Order                                       | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 834             | Benefit Enrollment and Maintenance                                 | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 835             | Health Care Claim Payment/Advice                                   | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 836             | Procurement Notices                                                | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 837             | Health Care Claim                                                  | Insurance                   | Yes  | Yes  | Yes  | Yes  | Yes  |
| 838             | Trading Partner Profile                                            | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 839             | Project Cost Reporting                                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 840             | Request for Quotation                                              | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 841             | Specifications/Technical Information                               | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 842             | Nonconformance Report                                              | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 843             | Response to Request for Quotation                                  | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 844             | Product Transfer Account Adjustment                                | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 845             | Price Authorization Acknowledgment/Status                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 846             | Inventory Inquiry/Advice                                           | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 847             | Material Claim                                                     | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 848             | Material Safety Data Sheet                                         | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 849             | Response to Product Transfer Account Adjustment                    | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 850             | Purchase Order                                                     | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 851             | Asset Schedule                                                     | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 852             | Product Activity Data                                              | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 853             | Routing and Carrier Instruction                                    | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 854             | Shipment Delivery Discrepancy Information                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 855             | Purchase Order Acknowledgment                                      | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 856             | Ship Notice/Manifest                                               | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 857             | Shipment and Billing Notice                                        | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 858             | Shipment Information                                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 859             | Freight Invoice                                                    | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 860             | Purchase Order Change Request<br>• Buyer Initiated                 | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 861             | Receiving Advice/Acceptance Certificate                            | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 862             | Shipping Schedule                                                  | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 863             | Report of Test Results                                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 864             | Text Message                                                       | Communications and Controls | Yes  | Yes  | Yes  | Yes  | Yes  |
| 865             | Purchase Order Change Acknowledgment/Request<br>• Seller Initiated | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 866             | Production Sequence                                                | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 867             | Product Transfer and Resale Report                                 | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 868             | Electronic Form Structure                                          | Communications and Controls | Yes  | Yes  | Yes  | Yes  | Yes  |
| 869             | Order Status Inquiry                                               | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 870             | Order Status Report                                                | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 871             | Component Parts Content                                            | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 872             | Residential Mortgage Insurance Application                         | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 873             | Commodity Movement Services                                        | Supply Chain                | N/A  | Yes  | Yes  | Yes  | Yes  |
| 874             | Commodity Movement Services Response                               | Supply Chain                | N/A  | N/A  | Yes  | Yes  | Yes  |
| 875             | Grocery Products Purchase Order                                    | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 876             | Grocery Products Purchase Order Change                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 877             | Manufacturer Coupon Family Code Structure                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 878             | Product Authorization/De-authorization                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 879             | Price Information                                                  | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 880             | Grocery Products Invoice                                           | Finance                     | Yes  | Yes  | Yes  | Yes  | Yes  |
| 881             | Manufacturer Coupon Redemption Detail                              | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 882             | Direct Store Delivery Summary Information                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 883             | Market Development Fund Allocation                                 | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 884             | Market Development Fund Settlement                                 | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 885             | Retail Account Characteristics                                     | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 886             | Customer Call Reporting                                            | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 887             | Coupon Notification                                                | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 888             | Item Maintenance                                                   | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 889             | Promotion Announcement                                             | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 891             | Deduction Research Report                                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 893             | Item Information Request                                           | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 894             | Delivery/Return Base Record                                        | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 895             | Delivery/Return Acknowledgment or Adjustment                       | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 896             | Product Dimension Maintenance                                      | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 920             | Loss or Damage Claim<br>• General Commodities                      | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 924             | Loss or Damage Claim<br>• Motor Vehicle                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 925             | Claim Tracer                                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 926             | Claim Status Report and Tracer Reply                               | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 928             | Automotive Inspection Detail                                       | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 940             | Warehouse Shipping Order                                           | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 943             | Warehouse Stock Transfer Shipment Advice                           | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 944             | Warehouse Stock Transfer Receipt Advice                            | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 945             | Warehouse Shipping Advice                                          | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 947             | Warehouse Inventory Adjustment Advice                              | Supply Chain                | Yes  | Yes  | Yes  | Yes  | Yes  |
| 980             | Functional Group Totals                                            | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 990             | Response to a Load Tender                                          | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 993             | Secured Receipt or Acknowledgment                                  | Communications and Controls | N/A  | Yes  | Yes  | Yes  | Yes  |
| 996             | File Transfer                                                      | Communications and Controls | Yes  | Yes  | Yes  | Yes  | Yes  |
| 997             | Functional Acknowledgment                                          | Communications and Controls | Yes  | Yes  | Yes  | Yes  | Yes  |
| 998             | Set Cancellation                                                   | Transportation              | Yes  | Yes  | Yes  | Yes  | Yes  |
| 999             | Implementation Acknowledgment                                      | Communications and Controls | N/A  | N/A  | N/A  | N/A  | Yes  |

## HIPAA Transaction sets

AWS B2B Data Interchange is a Health Insurance Portability and Accountability Act of 1996 (HIPAA)
eligible service and supports the following X12 version 5010 HIPAA transaction
sets.

###### Note

For these transaction sets, the X12 version is `VERSION_5010_HIPAA`.

| Transaction Set | Description                                                                         | Supported? |
| --------------- | ----------------------------------------------------------------------------------- | ---------- |
| 270 X279        | Eligibility Benefit Inquiry                                                         | Yes        |
| 271 X279        | Eligibility Benefit Response                                                        | Yes        |
| 275 X210        | Unsolicited Claim Attachments (from practice to payer)                              | `No`       |
| 275 X211        | Unsolicited Claim Attachments (from practice to clearinghouse to<br>payer)          | `No`       |
| 276 X212        | Claim Status Request                                                                | Yes        |
| 277 X212        | Claim Status Request Response                                                       | Yes        |
| 277 X214        | Claim Acknowledgement                                                               | Yes        |
| 277 X364        | Data Reporting Acknowledgement                                                      | `No`       |
| 278 X217        | Services Review Information Review/Response                                         | Yes        |
| 820 X218        | Payroll Deducted and Other Group Premium Payment For Insurance<br>Products Examples | Yes        |
| 820 X306        | Health Insurance Exchange Related Payments                                          | Yes        |
| 824 X186        | Application Advice                                                                  | `No`       |
| 834 X220        | Benefit Enrollment and Maintenance                                                  | Yes        |
| 834 X307        | Health Insurance Exchange: Enrollment                                               | `No`       |
| 834 X318        | Benefit Enrollment and Maintenance, Electronic Remittance Advice<br>(ERA)           | `No`       |
| 835 X221        | Claim Payment/Advice, Electronic Remittance Advice (ERA)                            | Yes        |
| 837 X222        | Claim, Professional and vision claims                                               | Yes        |
| 837 X223        | Claim, Institutional claims                                                         | Yes        |
| 837 X224        | Claim, Dental claims                                                                | Yes        |
| 837 X291        | Professional Pre-Determination                                                      | `No`       |
| 837 X292        | Institutional Pre-Determination                                                     | `No`       |
| 837 X298        | Post-adjudicated Claims Data Reporting, Professional                                | `No`       |
| 999 X231        | Implementation Acknowledgement                                                      | `No`       |
