import os

import eradiate.cli.data
import pooch

root_dir = os.path.dirname(__file__)

print("** Installing Eradiate resource files **\n")
eradiate.cli.data.install(["core"])
print("Done")

print("\n** Downloading extra resource files **\n")
pooch.retrieve(
    url="https://eradiate.eu/data/paper-eradiate-v100-data.zip",
    known_hash="md5:614e02d4e189800b6cbc1c5ea30e76e1",
    processor=pooch.Unzip(extract_dir=root_dir),
)
print("Done")
