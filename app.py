#!/usr/bin/env python3
import aws_cdk as cdk
from my_lambda_stack import MyLambdaStack

app = cdk.App()
MyLambdaStack(app, "MyLambdaWithLayerStack")
app.synth()
