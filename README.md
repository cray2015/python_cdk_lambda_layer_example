
## install nodejs via nvm

        # Download and install nvm:
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
        # in lieu of restarting the shell
        \. "$HOME/.nvm/nvm.sh"
        # Download and install Node.js:
        nvm install 22
        # Verify the Node.js version:
        node -v # Should print "v22.17.1".


## install cdk via npm

        npm install -g aws-cdk

## create .venv for running CDK stack

        python3 -m env .venv
        source .venv/bin/activate
        pip install --upgrade pip
        pip install -r requirement.txt

## Bootstrap CDK

        cdk bootstrap

## deploy

        cdk deploy
