#!/bin/bash

KILL_LIST=(
  externals
  kaplademo
  physx/bin
  physx/buildtools
  physx/compiler
  physx/documentation
  physx/samples
  physx/snippets
  physx/source/compiler
  physx/tools
  physx/generate_projects.bat
  physx/generate_projects.sh
  physx/platform_readme.html
  physx/release_notes.html
)

for i in "${KILL_LIST[@]}"
do
  git filter-branch --force --index-filter "git rm -r --cached --ignore-unmatch $i" --prune-empty --tag-name-filter cat -- --all
done
