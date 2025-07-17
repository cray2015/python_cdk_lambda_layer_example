from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    Duration,
)
from constructs import Construct
import os

class MyLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create the Lambda Layer from built ZIP
        psycopg2_layer = _lambda.LayerVersion(
            self, "Psycopg2Layer",
            code=_lambda.Code.from_asset("psycopg2-layer/layer.zip"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            description="Lambda Layer with psycopg2-binary"
        )

        # Define the Lambda function that uses the layer
        fn = _lambda.Function(
            self, "PostgresLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda_app"),
            handler="handler.lambda_handler",
            layers=[psycopg2_layer],
            timeout=Duration.seconds(30),
            environment={
                "DB_HOST": "your-db-host",
                "DB_NAME": "your-db-name",
                "DB_USER": "your-db-user",
                "DB_PASSWORD": "your-db-password"
            }
        )
