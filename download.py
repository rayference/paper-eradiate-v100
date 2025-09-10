from dataclasses import dataclass
import argparse
import os
import shutil
import sys

import pooch

root_dir = os.path.dirname(__file__)


@dataclass
class Resource:
    id: str
    url: str
    md5: str


RESOURCES = {
    "algeria": Resource(
        "algeria",
        "https://eradiate.eu/data/paper-eradiate-v100-data-algeria.tar.gz",
        "0d46a30ad4a1ca2b3e06f3d61562d511",
    ),
    "dakar": Resource(
        "dakar",
        "https://eradiate.eu/data/paper-eradiate-v100-data-dakar.tar.gz",
        "51ae4de1d62e903d54abb44078cc3921",
    ),
}

CACHE_PATH = "data_cache"


def download_core():
    print("** Installing Eradiate core resource files **")
    import eradiate.cli.data

    eradiate.cli.data.install(["core"])
    print("Done")


def download_resource(resource: Resource):
    """Download a specific resource."""

    print(f"** Downloading '{resource.id}' resource file **")
    pooch.retrieve(
        url=resource.url,
        known_hash=f"md5:{resource.md5}",
        processor=pooch.Untar(extract_dir=root_dir),
        progressbar=True,
        path=CACHE_PATH,
    )
    print("Done")


def clear_cache():
    """Clear the download cache directory."""
    if os.path.exists(CACHE_PATH):
        print(f"** Clearing download cache at '{CACHE_PATH}' **")
        shutil.rmtree(CACHE_PATH)
        print("Cache cleared")
    else:
        print("No cache directory to clear")


def main():
    parser = argparse.ArgumentParser(
        description="Download data resources for the paper-eradiate-v100 companion repository.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
available resources:
  core     - Eradiate core resource files only
  algeria  - Algeria scene data
  dakar    - Dakar scene data
  all      - All scene data
        """,
    )
    parser.add_argument(
        "resources",
        help="resources to download",
        nargs="*",
    )
    parser.add_argument(
        "-c",
        "--clear-cache",
        action="store_true",
        help="clear the download cache after successful downloads",
    )

    args = parser.parse_args()

    requested_resources = {"core"} if not args.resources else set(args.resources)

    allowed = {"core", "all"} | set(RESOURCES.keys())
    unsupported = requested_resources - allowed
    if unsupported:
        print(f"Unsupported resources {unsupported}")
        sys.exit(1)

    get_core = bool({"core", "all"} & requested_resources)
    if get_core:
        download_core()

    for resource_id, resource in RESOURCES.items():
        get_resource = bool({"all", resource_id} & requested_resources)
        if get_resource:
            download_resource(resource)

    if args.clear_cache:
        clear_cache()


if __name__ == "__main__":
    main()
