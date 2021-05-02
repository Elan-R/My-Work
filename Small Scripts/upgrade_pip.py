import pkg_resources;import os;os.system("pip install --upgrade "+" ".join(dist.project_name for dist in pkg_resources.working_set))
