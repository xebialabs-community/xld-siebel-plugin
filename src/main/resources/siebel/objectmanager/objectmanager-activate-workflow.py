#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.siebel.data import SiebelDataBean
from com.siebel.data import SiebelBusComp
from com.siebel.data import SiebelPropertySet

siebelDataBeanConnectionUrl = "siebel://" + deployed.container.server.host.address + ":" + str(deployed.container.scbPort) + "/" + deployed.container.server.enterprise.siebelEnterpriseName + "/" + deployed.container.siebelObjectManagerName

siebelDataBeanConnectionUsername = deployed.container.server.username
siebelDataBeanConnectionPassword = deployed.container.server.password
workflowActivationBusObjName = deployed.busObjName
workflowActivationBusCompName = deployed.busCompName
workflowActivationWorkflowName = deployed.workflowName
workflowActivationWorkflowVersion = deployed.workflowVersion
workflowStatusCheckValue = deployed.workflowStatusCheckValue
workflowActivationWorkSearchSpec = workflowActivationWorkflowName + ": " + workflowActivationWorkflowVersion

workflowActivationBusComp = SiebelBusComp()
xlSiebelDataBean = SiebelDataBean()

xlSiebelDataBean.login(siebelDataBeanConnectionUrl, siebelDataBeanConnectionUsername, siebelDataBeanConnectionPassword)

workflowActivationBusComp = xlSiebelDataBean.getBusObject(workflowActivationBusObjName).getBusComp(workflowActivationBusCompName)

workflowActivationBusComp.clearToQuery()
workflowActivationBusComp.activateField("Name")
workflowActivationBusComp.setSearchSpec("Name", "\"" + workflowActivationWorkSearchSpec + "\"")
workflowActivationBusComp.executeQuery(bool("true"))

if workflowActivationBusComp.firstRecord():
    workflowActivationBusComp = xlSiebelDataBean.getBusObject(workflowActivationBusObjName).getBusComp("Workflow Process Deployment")
    workflowActivationBusComp.clearToQuery()
    workflowActivationBusComp.activateField("Name")
    workflowActivationBusComp.setSearchSpec("Name", "\"" + workflowActivationWorkflowName + "\"")
    workflowActivationBusComp.setSearchSpec("Deployment Status", workflowStatusCheckValue)
    workflowActivationBusComp.setSearchSpec("Repository Version", workflowActivationWorkflowVersion)
    workflowActivationBusComp.executeQuery(bool("true"))

    if workflowActivationBusComp.firstRecord():
        print "Version [" + workflowActivationWorkflowVersion + "] of workflow [" + workflowActivationWorkflowName + "] already has status [" + workflowStatusCheckValue + "] ... skipping activation"
    else:
        print "Activate version [" + workflowActivationWorkflowVersion + "] of workflow [" + workflowActivationWorkflowName + "] on objectmanager [" + deployed.container.siebelObjectManagerName + "] running on host [" + deployed.container.server.host.address + "] in enterprise [" + deployed.container.server.enterprise.siebelEnterpriseName + "]"

        workflowActivationInput = SiebelPropertySet()
        workflowActivationOutput = SiebelPropertySet()

        workflowActivationInput.setProperty("FlowSearchSpec", "Process Name like '" + workflowActivationWorkflowName + "'")
        xlSiebelDataBean.getService("Workflow Admin Service").invokeMethod("Activate", workflowActivationInput, workflowActivationOutput)
else:
    print "Version [" + workflowActivationWorkflowVersion + "] of workflow [" + workflowActivationWorkflowName + "] was not found"

xlSiebelDataBean.logoff()

print "Done."
