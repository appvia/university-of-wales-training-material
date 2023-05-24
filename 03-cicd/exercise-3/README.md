

# Automated Python Unit Testing Made Easy with Pytest and GitHub Actions

The source code for this example is a simple Python function that calculates the area of a square, given its length. which can be found in`area.py` and we also have a folder called test which includes the unit tests.

Please copy the below in your root directory within your repository.
- scr/
- tests/ 
- requirements.txt


After you've copied the below.

Create folder called `.github` 
Inside `.github` folder create another folder called `workflows` 
In the `workflows` folder create a new yaml file called `run_test.yml` 


In `run_test.yml`  add the below code.

    name: Run Unit Test via Pytest  
      
    on: [push]  
      
    jobs:  
      build:  
        runs-on: ubuntu-latest  
        strategy:  
          matrix:  
            python-version: ["3.10"]  
      
        steps:  
          - uses: actions/checkout@v3  
          - name: Set up Python ${{ matrix.python-version }}  
            uses: actions/setup-python@v4  
            with:  
              python-version: ${{ matrix.python-version }}  
          - name: Install dependencies  
            run: |  
              python -m pip install --upgrade pip  
              if [ -f requirements.txt ]; then pip install -r requirements.txt; fi  
          - name: Lint with Ruff  
            run: |  
              pip install ruff  
              ruff --format=github --target-version=py310 .  
            continue-on-error: true  
          - name: Test with pytest  
            run: |  
              coverage run -m pytest  -v -s  
          - name: Generate Coverage Report  
            run: |  
              coverage report -m

Let’s break down this file.

    name: Run Unit Test via Pytest  
      
    on: [push]  
      
    jobs:  
      build:  
        runs-on: ubuntu-latest  
        strategy:  
          matrix:  
            python-version: ["3.10"]

Here we define the name, the trigger for the workflow and some boilerplate including the type of GitHub Actions runner and what version of Python to run on.

Triggers can be events like a Pull Request, merge to  `x`  branch, release tag and so on.

The  [documentation](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)  covers this in detail.

    steps:  
          - uses: actions/checkout@v3  
          - name: Set up Python ${{ matrix.python-version }}  
            uses: actions/setup-python@v4  
            with:  
              python-version: ${{ matrix.python-version }}  
          - name: Install dependencies  
            run: |  
              python -m pip install --upgrade pip  
              if [ -f requirements.txt ]; then pip install -r requirements.txt; fi  
          - name: Lint with Ruff  
            run: |  
              pip install ruff  
              ruff --format=github --target-version=py310 .  
            continue-on-error: true  
          - name: Test with pytest  
            run: |  
              coverage run -m pytest  -v -s  
          - name: Generate Coverage Report  
            run: |  
              coverage report -m

The Job contains a sequence of steps.

1.  Check out the current repository
2.  Set up Python on the runner
3.  Install dependencies
4.  Lint with  [Ruff](https://github.com/charliermarsh/ruff)
5.  Run the Unit test (using Pytest) and generate a coverage report
6.  Print the coverage report to Console

You can include any amount of steps and essentially do whatever you like — send an email, write to an S3 bucket, generate logs and push to Elasticsearch, and build a Pypi package.

With the ability to easily create your own actions (run your own code) there are endless possiblities.

### [](https://pytest-with-eric.com/integrations/pytest-github-actions/#Running-the-Workflow-and-Output "Running the Workflow and Output")Running the Workflow and Output

This is the best part.

Running the workflow is automatic and is handled based on the  [triggers set in the workflow file](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow).

A simple merge or push to the branch will trigger your workflow, no need to write any additional code or maintain triggers.

You can track the workflow execution state and check the output in the  `Actions`  tab of your GitHub Repo.

![pytest-github-actions-workflow-run](https://pytest-with-eric.com/uploads/pytest-github-actions-workflow-run.png)

Here we can see our tests ran successfully on GitHub Actions including our coverage report.

