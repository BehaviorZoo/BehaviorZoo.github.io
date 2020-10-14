#!/bin/bash
# chmod +x mkdocs.sh
# ./mkdocs.sh

function logging() { 
  echo -e "\033[0;32m$1\033[0m"
}
function whereIam() {	
  echo -e "@ \033[07m`pwd`\033[0m"
}
function deleteDir(){
  if [ -d $1 ]; then
    echo -e "Deleted old \033[31m$1\033[0m directory."
    rm -rf $1	
  fi
}

HERE=$(cd $(dirname $0);pwd)	
PYTHON="python3"
# Source Directory
SRC_DIRNAME="src"
PAGE_GENERATION_PROGRAM="${SRC_DIRNAME}/generate_pages.py"
SRC_DATA_PATH="${SRC_DIRNAME}/BehaviorZoo.xlsx"
# Pelican Directory
PELICAN_DIRNAME="pelican"
PELICAN_CONF_PATH="${PELICAN_DIRNAME}/pelicanconf.py"
PELICAN_SRC_DIRNAME="${PELICAN_DIRNAME}/content"
# Docs.
DOC_DIRNAME="docs"

logging "cd $HERE"	
cd $HERE	
whereIam

# Delete old Docs.
deleteDir $DOC_DIRNAME	
deleteDir $PELICAN_SRC_DIRNAME

# Generate markdown pages from file at ${SRC_DATA_PATH} and save them to ${PELICAN_SRC_DIRNAME} directory.
logging "${PYTHON} ${PAGE_GENERATION_PROGRAM} -D ${SRC_DATA_PATH} -O ${PELICAN_SRC_DIRNAME}"	
$PYTHON $PAGE_GENERATION_PROGRAM -D $SRC_DATA_PATH -O $PELICAN_SRC_DIRNAME

# Copy static directory for pelican.
logging "cp -r ${PELICAN_DIRNAME}/static!important/* ${PELICAN_SRC_DIRNAME}/"
cp -r $PELICAN_DIRNAME/static!important/* $PELICAN_SRC_DIRNAME/

# Generate docs using pelican.
logging "pelican ${PELICAN_SRC_DIRNAME} -o ${DOC_DIRNAME} -s ${PELICAN_CONF_PATH}"	
pelican $PELICAN_SRC_DIRNAME -o $DOC_DIRNAME -s $PELICAN_CONF_PATH