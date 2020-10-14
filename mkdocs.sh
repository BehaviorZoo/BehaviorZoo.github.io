#!/bin/bash
# chmod +x mkdocs.sh
# ./mkdocs.sh

function logging() { 
  echo -e "\033[0;32m$1\033[0m"
}
function warnings() {	
  echo -e "\033[31m$1\033[0m"
}
function whereIam() {	
  echo -e "@ \033[07m`pwd`\033[0m"
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
PELICAN_STATIC_DIRNAME="${PELICAN_DIRNAME}/static!important"
# Docs.
DOC_DIRNAME="docs"

logging "cd $HERE"	
cd $HERE	
whereIam

# Delete old Docs.
if [ -d $DOC_DIRNAME ]; then	
  warnings "Delete old $DOC_DIRNAME directory."	
  rm -rf $DOC_DIRNAME	
fi

# Generate markdown pages from file at ${SRC_DATA_PATH} and save them to ${PELICAN_SRC_DIRNAME} directory.
logging "${PYTHON} ${PAGE_GENERATION_PROGRAM} -D ${SRC_DATA_PATH} -O ${PELICAN_SRC_DIRNAME}"	
$PYTHON $PAGE_GENERATION_PROGRAM -D $SRC_DATA_PATH -O $PELICAN_SRC_DIRNAME

# Copy static directory for pelican.
logging "cp -r ${PELICAN_STATIC_DIRNAME} ${PELICAN_SRC_DIRNAME}/static"
cp -r $PELICAN_STATIC_DIRNAME $PELICAN_SRC_DIRNAME/static

# Generate docs using pelican.
logging "pelican ${PELICAN_SRC_DIRNAME} -o ${DOC_DIRNAME} -s ${PELICAN_CONF_PATH}"	
pelican $PELICAN_SRC_DIRNAME -o $DOC_DIRNAME -s $PELICAN_CONF_PATH