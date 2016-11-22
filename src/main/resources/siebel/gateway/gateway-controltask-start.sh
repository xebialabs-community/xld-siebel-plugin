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

echo "Starting Siebel gateway [${container.name}] on [${container.host.address}]"

${container.home}/bin/start_ns

echo "Done."