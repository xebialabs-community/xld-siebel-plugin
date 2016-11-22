#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.siebel.data import SiebelDataBean
from com.siebel.data import SiebelBusComp

siebelDataBeanConnectionUrl = "siebel://" + previousDeployed.container.server.host.address + ":" + str(previousDeployed.container.scbPort) + "/" + previousDeployed.container.server.enterprise.siebelEnterpriseName + "/" + previousDeployed.container.siebelObjectManagerName

print "Delete record [" + previousDeployed.name + "] using objectmanager [" + previousDeployed.container.siebelObjectManagerName + "] running on host [" + previousDeployed.container.server.host.address + "] in enterprise [" + previousDeployed.container.server.enterprise.siebelEnterpriseName + "]"
print "Connection URL: " + siebelDataBeanConnectionUrl

siebelDataBeanConnectionUsername = previousDeployed.container.server.username
siebelDataBeanConnectionPassword = previousDeployed.container.server.password
siebelRecordBusObjName = previousDeployed.busObjName
siebelRecordBusCompName = previousDeployed.busCompName
siebelRecordFieldValues = previousDeployed.fieldValues

siebelDataBeanBusComp = SiebelBusComp()
siebelDataBeanChildBusComp = SiebelBusComp()
xlSiebelDataBean = SiebelDataBean()

xlSiebelDataBean.login(siebelDataBeanConnectionUrl, siebelDataBeanConnectionUsername, siebelDataBeanConnectionPassword)

siebelDataBeanBusComp = xlSiebelDataBean.getBusObject(siebelRecordBusObjName).getBusComp(siebelRecordBusCompName)
siebelDataBeanBusComp.clearToQuery()

print "Processing [" + previousDeployed.name + "] for [" + siebelRecordBusCompName + "]"

for key in siebelRecordFieldValues.keys():
    siebelDataBeanBusComp.setSearchSpec(key, siebelRecordFieldValues[key])

siebelDataBeanBusComp.executeQuery(bool("true"))

print "Deleting [" + previousDeployed.name + "]"
siebelDataBeanBusComp.firstRecord()
siebelDataBeanBusComp.deleteRecord()

xlSiebelDataBean.logoff()

print "Done."
