import nox

@nox.session(python = ["3.10", "3.11", "3.12", "3.13"], venv_backend = "mamba")
# @nox.parametrize("django", ["1.9", "2.0"]) # parametrize diff versions
def test_install_package(session):
    session.install(".[all]", "--no-user") # pip install
    # session.install(f"django=={django}") # parametrize diff versions
    # session.run("pytest", "-v", "tests") # run python commands
    # session.conda_install("pytest", channels=["conda-forge"]) # conda install