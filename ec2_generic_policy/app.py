from aws_cdk import core
from pipeline.pipeline_stack import PipelineStack

pipeline_env = core.Environment(account="160165474064", region="ap-southeast-2")


app = core.App()
PipelineStack(app, 'PipelineStack', env= pipeline_env)            
app.synth()

# Note: do not call the Application Stacks from app.  These will be called by the pipeline stack
