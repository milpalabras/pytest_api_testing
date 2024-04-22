from invoke import task


@task(help={"module": "Module to test"})
def run_tests(ctx, module=None):
    """Run tests with pytest"""
    cmd = "poetry shell & python -m pytest"
    if module:
        cmd += f" tests/{module}"
    ctx.run(cmd)


@task
def install_poetry(ctx):
    ctx.run(
        "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"
    )


@task(install_poetry)
def install_dependencies(ctx):
    ctx.run("poetry install")


@task
def generate_report(ctx):
    ctx.run("allure serve allure-results --port 8081")


@task
def install_scoop(ctx):
    ctx.run('powershell -command "Set-ExecutionPolicy RemoteSigned -scope CurrentUser"')
    ctx.run('powershell -command "iwr -useb get.scoop.sh | iex"')


@task
def install_allure(ctx):
    ctx.run("scoop install allure")


@task
def setup(ctx):
    install_poetry(ctx)
    install_dependencies(ctx)
    install_scoop(ctx)
    install_allure(ctx)



@task
def run_tests_with_allure(ctx):
    run_tests(ctx)
    generate_report(ctx)


@task
def pre_commit(ctx):
    ctx.run("pre-commit run --all-files")


@task
def regresion_sin_bugs(ctx):
    ctx.run('python -m pytest -m "not bug"')

@task
def regresion_solo_bugs(ctx):
    ctx.run('python -m pytest -m bug')
