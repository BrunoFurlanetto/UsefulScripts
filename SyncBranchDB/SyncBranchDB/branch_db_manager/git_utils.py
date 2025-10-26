import subprocess


def get_current_branch():
    """Return the current Git branch name"""
    branch_name = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"]
    ).strip().decode("utf-8")
    return branch_name
