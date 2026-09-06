

# Feature compatibility tables
<a name="chap-oracle-aurora-mysql.features"></a>

With AWS DMS, you can ensure compatibility between the source and target databases during migration. Feature Compatibility defines the set of database engine features that AWS DMS supports for a specific source-target combination. The following tables provide legends for feature compatibility to help you plan for your specific migration scenario.

## Feature compatibility legend
<a name="chap-oracle-aurora-mysql.features.legend"></a>


| Automation level icon | Description | 
| --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-5.png)  |  **Very high compatibility**. None or minimal low-risk and low-effort rewrites needed. | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  **High compatibility**. Some low-risk rewrites needed, easy workarounds exist for incompatible features. | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  **Medium compatibility**. More involved low-medium risk rewrites needed, some redesign may be needed for incompatible features. | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  **Low compatibility**. Medium to high risk rewrites needed, some incompatible features require redesign and reasonable-effort workarounds exist. | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  |  **Very low compatibility**. High risk and/or high-effort rewrites needed, some features require redesign and workarounds are challenging. | 
|  ![No compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-0.png)  |  **Not compatible**. No practical workarounds yet, may require an application level architectural solution to work around incompatibilities. | 

## AWS SCT and AWS DMS automation level legend
<a name="chap-oracle-aurora-mysql.features.automation"></a>


| Automation level icon | Description | 
| --- | --- | 
|  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-5.png)  |  **Full automation**. AWS SCT performs fully automatic conversion, no manual conversion needed. | 
|  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  **High automation**. Minor, simple manual conversions may be needed. | 
|  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  |  **Medium automation**. Low-medium complexity manual conversions may be needed. | 
|  ![Two star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-2.png)  |  **Low automation**. Medium-high complexity manual conversions may be needed. | 
|  ![One star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-1.png)  |  **Very low automation**. High risk or complex manual conversions may be needed. | 
|  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  **No automation**. Not currently supported by AWS SCT, manual conversion is required for this feature. | 