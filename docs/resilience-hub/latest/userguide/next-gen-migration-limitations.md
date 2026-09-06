

# Known limitations during migration
<a name="next-gen-migration-limitations"></a>

The following limitations apply during the migration period from AWS Resilience Hub v1 to the next generation of Resilience Hub.


| Limitation | Description | Workaround | 
| --- | --- | --- | 
| Assessment history | v1 assessment results are not automatically migrated to the next generation of Resilience Hub format | v1 results remain accessible through v1 APIs during the transition period | 
| Custom resilience checks | v1 custom checks are not migrated | Review failure mode findings – GenAI assessments typically cover the same concerns | 
| AppRegistry input source | AppRegistry is not supported as an input source in the next generation of Resilience Hub | Use alternative input sources such as CloudFormation stacks or resource tags | 