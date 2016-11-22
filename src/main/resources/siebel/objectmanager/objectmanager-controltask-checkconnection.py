#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.siebel.data import SiebelDataBean

siebelDataBeanConnectionUrl = "siebel://" + thisCi.server.host.address + ":" + str(thisCi.scbPort) + "/" + thisCi.server.enterprise.siebelEnterpriseName + "/" + thisCi.siebelObjectManagerName

siebelDataBeanConnectionUsername = thisCi.server.username
siebelDataBeanConnectionPassword = thisCi.server.password
comSanityCheckQueryBusObjName = thisCi.comSanityCheckQueryBusObjName
comSanityCheckQueryBusCompName = thisCi.comSanityCheckQueryBusCompName
comSanityCheckQueryResultDisplayField = thisCi.comSanityCheckQueryResultDisplayField
comSanityComSanityCheckQueryField = thisCi.comSanityCheckQueryField
comSanityComSanityCheckQuerySearchString = thisCi.comSanityCheckQuerySearchString

print "Attempting to query objectmanager [" + thisCi.siebelObjectManagerName + "] running on host [" + thisCi.server.host.address + "] in enterprise [" + thisCi.server.enterprise.siebelEnterpriseName + "]"
print "Query parameters: [BusObj: [" + comSanityCheckQueryBusObjName + "]],[BusComp: [" + comSanityCheckQueryBusCompName + "]], [QueryString: [" + comSanityComSanityCheckQuerySearchString + "]], [QueryField: [" + comSanityComSanityCheckQueryField +"]], [QueryResultDisplayField: [" + comSanityCheckQueryResultDisplayField + "]]"
print "Connection URL: " + siebelDataBeanConnectionUrl

xlSiebelDataBean = SiebelDataBean()
xlSiebelDataBean.login(siebelDataBeanConnectionUrl, siebelDataBeanConnectionUsername, siebelDataBeanConnectionPassword)

siebelDataBeanBusComp = xlSiebelDataBean.getBusObject(comSanityCheckQueryBusObjName).getBusComp(comSanityCheckQueryBusCompName)

siebelDataBeanBusComp.setSearchSpec(comSanityComSanityCheckQueryField, comSanityComSanityCheckQuerySearchString)
siebelDataBeanBusComp.executeQuery(bool("true"))
siebelDataBeanBusComp.firstRecord()

resultCounter = 1

while (siebelDataBeanBusComp.nextRecord()):
    print str(resultCounter) + ": " + siebelDataBeanBusComp.getFieldValue(comSanityCheckQueryResultDisplayField)
    resultCounter+=1

xlSiebelDataBean.logoff()

print "Done."
