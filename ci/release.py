import subprocess
import re

p = subprocess.check_output("poetry version", shell=True)
ver = re.match(".* to (.*)\\\\.*$", str(p)).group(1)
open("attrs_serde/__version__.py", "w").write('__version__ = "{}"'.format(ver))
print("git tag v{}".format(ver))
print(subprocess.check_call("git tag v{}".format(ver), shell=True))
print("now run poetry publish --build, git push --tags")

