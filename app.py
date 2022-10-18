#!/usr/bin/env python3
import aws_cdk as cdk

from aws_lambda_layers.lambda_stack import LambdaStack

app = cdk.App()

LambdaStack(app, 'LambdaStack')

app.synth()
