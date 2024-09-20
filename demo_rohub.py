import rohub
import os
import pathlib
<<<<<<< HEAD
import zipfile
=======
>>>>>>> f0791fa7a8aba69a142304f24b2542521593402d

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
<<<<<<< HEAD
print(pd)
requirements_file = pd / "requirements.txt"


# download the project
# rohub.ros_export_to_rocrate(project_id, "rocrate-metadata", pd, use_format="jsonld")

# to exclude files
exclude_files = [
    "requirements.txt",
    ".gitignore",
    "demo_rohub.py",
    "venv",
    ".env",
    ".git",
    "demo_rohub.zip",
    "rocrate-metadata.jsonld",
]

# make a zip file of the current folder , do not include the files, folders in exclude_files
# do not include venv folder
zipf = zipfile.ZipFile("demo_rohub.zip", "w", zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(pd):
    # Exclude directories listed in exclude_files
    dirs[:] = [d for d in dirs if d not in exclude_files]
    for file in files:
        if file not in exclude_files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, pd)
            zipf.write(file_path, arcname)
zipf.close()

# add the zip file to the ro project
path_to_zip = pd / "demo_rohub.zip"
rohub.ros_upload_resources(project_id, path_to_zip)

# delete the zip file
os.remove(path_to_zip)

# download the project metadata
=======

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
>>>>>>> f0791fa7a8aba69a142304f24b2542521593402d
rohub.ros_export_to_rocrate(project_id, "rocrate-metadata", pd, use_format="jsonld")
