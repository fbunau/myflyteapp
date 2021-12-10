# %%
# The following import is required to configure a Spark Server in Flyte:
from flytekitplugins.spark.generic_task import GenericSparkTask, GenericSparkConf, JobType

from flytekit import kwtypes
from flytekit import workflow

scala_spark = GenericSparkTask(
    name="scala_spark_test",
    inputs=kwtypes(),
    job_type = JobType.Scala,
    task_config=GenericSparkConf(
        main_class="com.sparktest.HelloWorld",
        main_application_file="local:///opt/spark/examples/jars/sparktest.jar",
        job_type = JobType.Scala,
        spark_conf={
                'spark.driver.memory': "1000M",
                'spark.driver.cores': '1',
                'spark.executor.memory': "1000M",
                'spark.executor.cores': '1',
                'spark.executor.instances': '2',
        }
    )
    
)

@workflow
def scala_spark_wf(partitions: int) -> None:
    print("Starting Spark with Partitions: {}".format(partitions))
    scala_spark()