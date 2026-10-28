from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def test_model():
    import subprocess

    print("Running model tests...")

    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        raise Exception("Model testing failed!")

    print("MODEL TESTING PASSED")


def train_model():
    import subprocess

    print("Training model...")

    result = subprocess.run(
        ["python", "src/train.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        raise Exception("Model training failed!")

    print("MODEL TRAINING COMPLETED")


def validate_model():
    import subprocess

    print("Validating model...")

    result = subprocess.run(
        ["python", "src/validate.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        raise Exception("Model validation failed!")

    print("MODEL VALIDATION PASSED")


def deploy_model():
    import subprocess

    print("Deploying model...")

    result = subprocess.run(
        ["python", "src/deploy.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        raise Exception("Model deployment failed!")

    print("MODEL DEPLOYMENT COMPLETED")


with DAG(
    dag_id="ml_cicd_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["machine-learning", "cicd"],
) as dag:

    test_task = PythonOperator(
        task_id="test_model",
        python_callable=test_model,
    )

    train_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )

    validate_task = PythonOperator(
        task_id="validate_model",
        python_callable=validate_model,
    )

    deploy_task = PythonOperator(
        task_id="deploy_model",
        python_callable=deploy_model,
    )

    test_task >> train_task >> validate_task >> deploy_task