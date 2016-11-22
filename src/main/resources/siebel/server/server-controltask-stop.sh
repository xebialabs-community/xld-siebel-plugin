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

source ${container.home}/siebenv.sh
echo "<#if container.forceShutdown>Force </#if>Shutdown Siebel server [${container.siebelServerName}] in enterprise [${container.enterprise.siebelEnterpriseName}]"

${container.home}/bin/stop_server <#if container.forceShutdown>-f </#if>-e ${container.enterprise.siebelEnterpriseName} ${container.siebelServerName}

<#if container.cleanupAfterShutdown>
echo "Removing [${container.home}/admin/${container.enterprise.siebelEnterpriseName}.${container.siebelServerName}.shm]"
rm -f ${container.home}/admin/${container.enterprise.siebelEnterpriseName}.${container.siebelServerName}.shm
echo "Removing [${container.home}/sys/osdf.${container.enterprise.siebelEnterpriseName}.${container.siebelServerName}]"
rm -f ${container.home}/sys/osdf.${container.enterprise.siebelEnterpriseName}.${container.siebelServerName}
</#if>

echo "Done."
