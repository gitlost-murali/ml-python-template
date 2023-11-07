#!/bin/bash

if [ -d .git ]; then
    echo "Git environment already exists."
    exit 0
fi

git config --global init.defaultBranch main
git init
git add .
git commit -m "initial commit"

pre-commit install -c git-hooks/.pre-commit-config.yaml  -t pre-commit
pre-commit install -c git-hooks/.pre-commit-config.yaml  --hook-type commit-msg

# Copy prepare-commit-msg
cp git-hooks/prepare-commit-msg .git/hooks/
chmod +x .git/hooks/prepare-commit-msg
echo 'prepare-commit-msg installed'