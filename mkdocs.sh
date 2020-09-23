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

PYTHON="python3"
DATA_PATH="BehaviorZoo.xlsx"
SRC_DIRNAME="src"	
DOC_DIRNAME="docs"
PELICAN_DIRNAME="pelican"	
HERE=$(cd $(dirname $0);pwd)	

logging "cd $HERE"	
cd $HERE	
whereIam	

if [ -d $DOC_DIRNAME ]; then	
  warnings "Delete old $DOC_DIRNAME directory."	
  rm -rf $DOC_DIRNAME	
fi

logging "cd $SRC_DIRNAME"	
cd $SRC_DIRNAME	
whereIam	

logging "$PYTHON generate_page.py -D $DATA_PATH"	
$PYTHON generate_page.py -D $DATA_PATH

logging "cd ../$PELICAN_DIRNAME"	
cd ../$PELICAN_DIRNAME	
whereIam	

logging "cp -r _static/ content/_static"	
cp -r _static/ content/_static

logging "make html"	
make html
