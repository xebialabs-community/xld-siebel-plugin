#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.siebel.data import SiebelDataBean
from com.siebel.data import SiebelBusComp

siebelDataBeanConnectionUrl = "siebel://" + deployed.container.server.host.address + ":" + str(deployed.container.scbPort) + "/" + deployed.container.server.enterprise.siebelEnterpriseName + "/" + deployed.container.siebelObjectManagerName

print "Create record [" + deployed.name + "] using objectmanager [" + deployed.container.siebelObjectManagerName + "] running on host [" + deployed.container.server.host.address + "] in enterprise [" + deployed.container.server.enterprise.siebelEnterpriseName + "]"
print "Connection URL: " + siebelDataBeanConnectionUrl

siebelDataBeanConnectionUsername = deployed.container.server.username
siebelDataBeanConnectionPassword = deployed.container.server.password
recordBusObjName = deployed.busObjName
recordBusCompName = deployed.busCompName
recordFieldValues = deployed.fieldValues

recordBusComp = SiebelBusComp()
childRecordBusComp = SiebelBusComp()
xlSiebelDataBean = SiebelDataBean()

xlSiebelDataBean.login(siebelDataBeanConnectionUrl, siebelDataBeanConnectionUsername, siebelDataBeanConnectionPassword)

recordBusComp = xlSiebelDataBean.getBusObject(recordBusObjName).getBusComp(recordBusCompName)
recordBusComp.newRecord(bool("true"))

print "Processing [" + deployed.name + "] for [" + recordBusCompName + "]"

for key in recordFieldValues.keys():
    recordBusComp.setFieldValue(key, recordFieldValues[key])

print "Writing [" + deployed.name + "]"
recordBusComp.writeRecord()

for childRecord in deployed.childRecords:
    print "Processing [" + childRecord.name + "] for [" + childRecord.busCompName + "]"
    childRecordBusComp = recordBusComp.busObject().getBusComp(childRecord.busCompName)
    childRecordBusComp.newRecord(bool("true"))
    for childKey in childRecord.fieldValues.keys():
        childRecordBusComp.setFieldValue(childKey, childRecord.fieldValues[childKey])
    print "Writing [" + childRecord.name + "]"
    childRecordBusComp.writeRecord()

xlSiebelDataBean.logoff()

print "Done."
