  
from aws_cdk import(
  core,
  aws_codepipeline as codepipeline,
  aws_codepipeline_actions as cpactions,
  aws_codecommit as codecommit,
  pipelines
)


from ec2policy.ec2policy import Ec2PolicyStage

class PipelineStack(core.Stack):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    source_repo = codecommit.Repository(self, "sourcerepo",
        repository_name = 'ec2_generic_policy',
        description = 'Generic EC2 policy for using on EC2 Instance Roles'
    )

    source_artifact = codepipeline.Artifact()
    cloud_assembly_artifact = codepipeline.Artifact()

    pipeline = pipelines.CdkPipeline(self, 'Pipeline',
        cloud_assembly_artifact = cloud_assembly_artifact,
        pipeline_name = 'EC2RolePolicy',
        source_action=cpactions.CodeCommitSourceAction(
          output = source_artifact,
          repository = source_repo,
          branch = 'master',
          trigger = cpactions.CodeCommitTrigger.EVENTS,
          action_name = 'OnRepoevent',
          run_order= 1
        ),
        synth_action=pipelines.SimpleSynthAction(
          source_artifact=source_artifact,
          cloud_assembly_artifact=cloud_assembly_artifact,
          install_command='npm install -g aws-cdk && pip install -r requirements.txt',
          #build_command='pytest unittests',
          synth_command='cdk synth')
    )

    # Add stages as required. 
    app_env = core.Environment(account="123456789098", region="ap-southeast-2")  
    prod_app = Ec2PolicyStage(self, 'Prod', env = app_env)
    prod_stage = pipeline.add_application_stage(prod_app)
