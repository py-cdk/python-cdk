import json
import yaml

from aws_cdk import(
    core,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_iam as iam,
)


class Ec2PolicyStage(core.Stage):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Ec2PolicyStack(self, 'EC2Policy')

class Ec2PolicyStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open('config/ec2policy.yaml') as f:
            policies = yaml.load(f, Loader=yaml.FullLoader)

            for name,statements in policies['Policies'].items():
                
                policy_statements = []
                for statement in statements:
                    if statement['Effect'] == 'Allow':
                        effect = iam.Effect.ALLOW
                    else:
                        effect = iam.Effect.DENY

                    policy_statements.append(
                            iam.PolicyStatement(
                                actions = statement['Action'],
                                #conditions = 
                                effect = effect,
                                resources= statement['Resources'],
                                #sid = statement['sid'],
                            )
                    )

                this_policy = iam.ManagedPolicy(self, name,
                        #description = 
                        managed_policy_name= name,
                ) 
                for statement in policy_statements:
                    this_policy.add_statements(statement)
        


            
            


        