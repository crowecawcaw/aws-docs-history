# Guidelines for porting phone numbers to your

Amazon Connect project in South Korea

Rules for South Korea differ from those in other countries. To help with
requirements in South Korea, here are some helpful hints.

- When planning your Amazon Connect project in South Korea one of the most important
  things you will need to do is plan and request information up front. To port
  numbers in South Korea, you may need to complete and submit more than 5
  forms and you may need to engage with the local regulatory authority before
  approvals are granted to port numbers.
- All geographic numbers (that is, other than toll-free, national,
  representative, or 070 VOIP) must be in place on a physical termination for
  a minimum of 6 months before they can be ported into Amazon Connect. However, if a
  number has been in place for a minimum of 3 months, you can port it by
  filing a special request with the Korean Ministry of Telecommunications;
  upon approval, the porting process can begin. Amazon Connect can provide you with the
  forms, but you must complete and submit them to the regulator
  directly.
- All geographic, representative, or toll-free numbers (GRTFN) are assigned
  a 070 VOIP number to which the GRTFN terminates and which are associated
  with the GRTFN at the carrier. Do not remove this 070 number from your Amazon Connect
  instance until the related GFTN number is removed. If you do, all inbound
  and outbound calls will fail.
- Representative numbers (RN) have minimum session billing requirements
  based on the "attractiveness" of the RN, as determined by the carrier.
  Representative numbers have different costs depending on the scale of the
  number. Based on the size of the representative number you order, the
  service will have from 2 channels to 500 channels minimum to be charged for.
  This is managed by adding a minimum number of numbers to the account, equal
  to the number of channels needed. These are shown on the [Amazon Connect pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/")
  page as the shared cost service at $0.5433 per day of usage for the system.
  These additional shared cost number DIDs do not have the ability to be
  assigned call flows, and outbound calls from them will fail. If you
  disconnect RNs, be sure to also remove their associated Special Numbers to
  avoid future billing. Removal or reduction of Special Number DIDs without
  removal of the underlying RN is a violation of Amazon Connect Terms of Service.
