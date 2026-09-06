

# VM Import Manifest
<a name="manifest"></a>

The import manifest is an XML file created and consumed by the Amazon EC2 API operations [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) and [ImportVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportVolume.html). Note that these operations are not supported by the AWS CLI.

The manifest allows a virtual machine image to be broken into small parts for transfer and then reassembled at the destination, with support for retrying failed partial transfers. This file is generally created, consumed, and destroyed by the Amazon EC2 tools without user intervention.

In some exceptional situations, developers may wish to construct a manifest manually or programmatically, making it possible to bypass certain API operations while still providing a manifest for other operations that require the file as a parameter value. 

This topic documents the structure of the manifest and provides a sample file.

**Note**  
Direct manipulation of the manifest departs from the standard workflow of the Amazon EC2 API. We recommend that you follow the procedures in [VM Import/Export processes](https://docs.aws.amazon.com/vm-import/latest/userguide/import-export-processes.html) instead.

## Manifest Schema
<a name="manifest_file_elements"></a>

The schema below describes the format of the manifest. Documentation for the schema elements is presented inline. 

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="manifest">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="version" type="xs:string">
                    <xs:annotation>
                        <xs:documentation> Version designator for the manifest file,
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="file-format" type="xs:string">
                    <xs:annotation>
                        <xs:documentation> File format of volume to be imported, with value RAW,
                            VHD, or VMDK. </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="importer" type="Importer">
                    <xs:annotation>
                        <xs:documentation> Complex type describing the software that created the
                            manifest. </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="self-destruct-url" type="xs:anyURI">
                    <xs:annotation>
                        <xs:documentation> Signed URL used to delete the stored manifest file.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="import" type="Import">
                    <xs:annotation>
                        <xs:documentation> Complex type describing the size and chunking of the
                            volume file. </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:complexType name="Importer">
        <xs:sequence>
            <xs:element name="name" type="xs:string">
                <xs:annotation>
                    <xs:documentation> Name of the software that created the manifest.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="version" type="xs:string">
                <xs:annotation>
                    <xs:documentation> Version of the software that created the manifest.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="release" type="xs:string">
                <xs:annotation>
                    <xs:documentation> Release number of the software that created the manifest.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="Import">
        <xs:sequence>
            <xs:element name="size" type="xs:long">
                <xs:annotation>
                    <xs:documentation> Exact size of the file to be imported (bytes on disk).
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="volume-size" type="xs:long">
                <xs:annotation>
                    <xs:documentation> Rounded size in gigabytes of volume to be imported.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="parts" type="Parts">
                <xs:annotation>
                    <xs:documentation> Complex type describing and counting the parts into which the
                        file is split. </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="Parts">
        <xs:sequence>
            <xs:element minOccurs="1" maxOccurs="unbounded" name="part" type="Part">
                <xs:annotation>
                    <xs:documentation> Definition of a particular part. Any number of parts may be
                        defined. </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="count" type="xs:int">
            <xs:annotation>
                <xs:documentation> Total count of the parts. </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>

    <xs:complexType name="Part">
        <xs:sequence>
            <xs:element name="byte-range" type="ByteRange">
                <xs:annotation>
                    <xs:documentation> Complex type defining the starting and ending byte count of a
                        part. </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="key" type="xs:string">
                <xs:annotation>
                    <xs:documentation> The S3 object name of the part. </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="head-url" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation> Signed URLs for issuing a HEAD request on the S3 object
                        containing this part. </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="get-url" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation> Signed URLs for issuing a GET request on the S3 object
                        containing this part. </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="delete-url" minOccurs="0" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation> Signed URLs for issuing a DELETE request on the S3 object
                        containing this part. </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="index" type="xs:int">
            <xs:annotation>
                <xs:documentation> Index number of this part. </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>

    <xs:complexType name="ByteRange">
        <xs:attribute name="start" type="xs:long">
            <xs:annotation>
                <xs:documentation> Offset of a part's first byte in the disk image.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="end" type="xs:long">
            <xs:annotation>
                <xs:documentation> Offset of a part's last byte in the disk image.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:schema>
```

## Examples
<a name="sample_manifest_file"></a>

This first example of a manifest describes a volume image with two parts. The files containing the parts are on a local system and must be uploaded to Amazon S3. 

```
<manifest>
    <version>2010-11-15</version>
    <file-format>VMDK</file-format>
    <importer>
        <name>ec2-upload-disk-image</name>
        <version>1.0.0</version>
        <release>2010-11-15</release>
    </importer>
    <self-destruct-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdkmanifest.xml?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=m%2Bl%2FkuKuvfEeD%2Fya%2B0TrgeiH%2FLM%3D</self-destruct-url>
    <import>
        <size>12595200</size>
        <volume-size>1</volume-size>
        <parts count="2">
            <part index="0">
                <byte-range end="10485759" start="0"/>
                <key>d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part0</key>
                <head-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part0?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=2yqS2VGYXGmqcbu%2FrQEn8FGIKaI%3D</head-url>
                <get-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part0?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=nEvl8VhFoEuIjJFRkAYB2IWKRtY%3D</get-url>
                <delete-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part0?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=CX19zc4Eys8BN%2FXsoepk%2Bi3i4No%3D</delete-url>
            </part>
            <part index="1">
                <byte-range end="12595199" start="10485760"/>
                <key>d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part1</key>
                <head-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part1?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=3b%2F8ky92L8g%2BBf15Ou194VnR4Js%3D</head-url>
                <get-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part1?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=W%2FxagI5ChmfqqgY8WwyDJ3Rgviw%3D</get-url>
                <delete-url>https://example-disk-part-bucket.s3.amazonaws.com/d6e1ca17-72f6-4ab0-b2c8-d7ba8186cb23/cirros-0.3.2-x86_64-disk.vmdk.part1?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&amp;Expires=1416618486&amp;Signature=08FH3QPwkIcNURnNpT9DIvvhQ0I%3D</delete-url>
            </part>
        </parts>
    </import>
</manifest>
```

The second example describes a volume image with a single part that has already been uploaded to Amazon S3. 

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<manifest>
    <version>2010-11-15</version>
    <file-format>VMDK</file-format>
    <importer>
        <name>Linux_RHEL_59_64.vmdk</name>
        <version>1.0.0</version>
        <release>2010-11-15</release>
    </importer>
    <self-destruct-url>https://example-disk-part-bucket.s3.ap-northeast-2.amazonaws.com/Linux_RHEL_59_64.vmdk?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAJ26ZRPZDGYJT4KAQFEXAMPLE%2Fap-northeast-2%2Fs3%2Faws4_request&amp;X-Amz-Date=20151119T234529Z&amp;X-Amz-Expires=604800&amp;X-Amz-Signature=4dbf803f2e52fb6a876d3b63778033af42ec11155b37366ab4fca56691672807&amp;X-Amz-SignedHeaders=Host</self-destruct-url>
    <import>
        <size>994433536</size>
        <volume-size>1</volume-size>
        <parts count="1">
            <part index="0">
                <byte-range end="994433536" start="0"/>
                <key>Linux_RHEL_59_64.vmdk</key>
                <head-url>https://example-disk-part-bucket.s3.ap-northeast-2.amazonaws.com/Linux_RHEL_59_64.vmdk?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAJ26ZRPZDGYJT4KAQFEXAMPLE%2Fap-northeast-2%2Fs3%2Faws4_request&amp;X-Amz-Date=20151119T234529Z&amp;X-Amz-Expires=604800&amp;X-Amz-Signature=4c3a7bdf3ef8fa53a5585fc67747c81ea1f65bf09f3768998a575dabf5dfda2e&amp;X-Amz-SignedHeaders=Host</head-url>
                <get-url>https://example-disk-part-bucket.s3.ap-northeast-2.amazonaws.com/Linux_RHEL_59_64.vmdk?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAJ26ZRPZDGYJT4KAQFEXAMPLE%2Fap-northeast-2%2Fs3%2Faws4_request&amp;X-Amz-Date=20151119T234529Z&amp;X-Amz-Expires=604800&amp;X-Amz-Signature=329d6abb673e4ce11c0aa602f34f62fb8ced703e8ae6c04f24c16e79d7699e52&amp;X-Amz-SignedHeaders=Host</get-url>
                <delete-url>https://example-disk-part-bucket.s3.ap-northeast-2.amazonaws.com/Linux_RHEL_59_64.vmdk?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAJ26ZRPZDGYJT4KAQFEXAMPLE%2Fap-northeast-2%2Fs3%2Faws4_request&amp;X-Amz-Date=20151119T234529Z&amp;X-Amz-Expires=604800&amp;X-Amz-Signature=4dbf803f2e52fb6a876d3b63778033af42ec11155b37366ab4fca56691672807&amp;X-Amz-SignedHeaders=Host</delete-url>
            </part>
        </parts>
    </import>
</manifest>
```