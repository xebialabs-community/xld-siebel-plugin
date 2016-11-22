#!/bin/bash

# ******************************************************************************
#
#  ---------------------------------------------------------------------------
#  THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
#  KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
#  PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#  ---------------------------------------------------------------------------
#
# ******************************************************************************

echo "Stopping OHS instance [${container.instanceName}] on host [${container.webTierInstance.host.address}]"

${container.home}/bin/opmnctl stopproc ias-component=${container.instanceName}

sleep 5

echo "Status of OPMN on host [${container.webTierInstance.host.address}]"

${container.home}/bin/opmnctl status

echo "Done."
