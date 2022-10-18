#!/usr/bin/env python3
import aws_cdk as cdk

from aws_lambda_layers.lambda_stack import LambdaStack
from aws_lambda_layers.lambda_container_stack import LambdaContainerStack

app = cdk.App()

LambdaStack(app, 'LambdaStack')
LambdaContainerStack(app, 'LambdaContainerStack')

app.synth()
