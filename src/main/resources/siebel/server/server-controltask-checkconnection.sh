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

ORACLE_HOME=${container.oracleClientHome}
LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
PATH=$ORACLE_HOME/bin:$PATH:$HOME/bin

export PATH ORACLE_HOME LD_LIBRARY_PATH

echo "Attempting to execute command [${container.srvrmgrSanityCheckCommand}] on [${container.host.address}] using [${container.home}/bin/srvrmgr]"
echo "Gateway: ${container.enterprise.gateway.host.address}"
echo "Enterprise: ${container.enterprise.siebelEnterpriseName}"
echo "Username: ${container.username}"

source ${container.home}/siebenv.sh
${container.home}/bin/srvrmgr /g ${container.enterprise.gateway.host.address} /e ${container.enterprise.siebelEnterpriseName} /u ${container.username} /p ${container.password} -c "${container.srvrmgrSanityCheckCommand}"

if [ $? != 0 ]; then
    exit 1
else
    echo "Done."
fi
