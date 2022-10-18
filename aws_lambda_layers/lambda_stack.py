from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_layer = lambda_.LayerVersion(
            self,
            'sampleLambdaLayer',
            compatible_runtimes=[
                lambda_.Runtime.PYTHON_3_7,
                lambda_.Runtime.PYTHON_3_8,
                lambda_.Runtime.PYTHON_3_9
            ],
            code=lambda_.Code.from_asset('layers/python-layer.zip'),
            description='python dependencies'
        )

        lambda_role = iam.Role(
            scope=self,
            id="lambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
            ],
        )

        sample_lambda = lambda_.Function(
          self,
          'sampleLambda',
          description='Sample Lambda using Layers',
          handler='lambda.handler',
          runtime=lambda_.Runtime.PYTHON_3_9,
          code=lambda_.Code.from_asset('lambda'),
          layers=[lambda_layer]
        )

        