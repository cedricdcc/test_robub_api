import rohub
import os
import pathlib

# Load environment variables username and password
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

rohub.login(username=username, password=password)

# Create a new project

ro_title = "My first project"
ro_research_areas = ["Atom"]

# valid_areas = rohub.list_valid_research_areas()
# print(valid_areas)

# rohub.ros_create(title=ro_title, research_areas=ro_research_areas)

# get the first project from the list of projects in the user's account
project = rohub.list_my_ros()
print(project)
project_id = project.iloc[0]["identifier"]
print(project_id)
# download the project metadata reference file
loaded_ro = rohub.ros_load(identifier=project_id)
# completeness = rohub.ros_completeness(loaded_ro, verbose=True)

# parent dir of the project
pd = pathlib.Path(__file__).parent

requirements_file = pd / "requirements.txt"

# add file to the project
rohub.ros_add_internal_resource(
    project_id,
    "file",
    requirements_file,
    "requirements.txt",
    description="A file with requirements",
)


# download the project
rohub.ros_export_to_rocrate(project_id, "rocrate-metadata", pd, use_format="jsonld")
