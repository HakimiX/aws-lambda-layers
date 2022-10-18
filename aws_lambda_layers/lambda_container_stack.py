from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_
)
from constructs import Construct

class LambdaContainerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

        sample_container_lambda = lambda_.DockerImageFunction(
            self,
            'sampleContainerLambda',
            architecture=lambda_.Architecture.X86_64,
            timeout=Duration.minutes(15),
            code=lambda_.DockerImageCode.from_image_asset(
                directory='./lambda_container',
                file='Dockerfile'
            ),
            role=lambda_role,
            environment={
                "SOMETHING": "bob1234"
            }
        )