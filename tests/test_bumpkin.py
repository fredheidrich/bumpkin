
import os

import pytest

from bumpkin import bumpkin


WINDOWS_LINE_ENDING = R'\r\n'
UNIX_LINE_ENDING = R'\n'


def test_changelog_generation():

 datestr = "2021-09-18"
 prev_version = "2021.9"
 new_version = "2021.9.1"
 repo_name = "foo/bar"
 changes_pivoted = {}
 is_first_release = True

 result = bumpkin.generate_changelog_content(datestr, prev_version, new_version, repo_name, changes_pivoted, is_first_release)

 assert result


@pytest.fixture
def old_non_changelog_file():

 # arrange
 string = "foo bar baz"
 filepath = "SOME_RANDOM_FILE.md"
 with open(filepath, "w") as testfile:
  testfile.write(string)

 yield filepath, string, ""

 # cleanup
 os.remove(filepath)


def test_add_to_existing_invalid_changelog(old_non_changelog_file):
 release_version = "2021.9"
 
 with open(old_non_changelog_file[0], "r") as testfile:
  changelog_str = testfile.read()

 result = bumpkin.split_changelog_header_and_content(changelog_str, release_version)
 assert result[0] == "foo bar baz"
 assert result[1] == ""


@pytest.fixture
def old_fake_changelog_file():

 header = (
 """# Changelog

[Unreleased]
* foo
* bar
* baz

"""
 )
 body = (
 """<a name='2021.9'></a>## [2021.9]

### Additions
* foobar

<a name='2021.8'></a>## [2021.8]

### Changes
* foo
* var

"""
 )
 filepath = "TESTFILE_THAT_DOES_EXIST.md"
 string = header + body

 # arrange
 with open(filepath, "w") as testfile:
  testfile.write(string)

 yield filepath, header, body

 # cleanup
 os.remove(filepath)
 

def test_add_to_existing_changelog(old_fake_changelog_file):
 release_version = "2021.9"
 
 with open(old_fake_changelog_file[0], "r") as testfile:
  changelog_str = testfile.read()

 result = bumpkin.split_changelog_header_and_content(changelog_str, release_version)
 assert result[0] == old_fake_changelog_file[1]
 assert result[1] == old_fake_changelog_file[2]


######################
# todo/fred: more tests to add


def test_cli():
 pass

def test_parsing_git_commits():
 pass

def test_no_previous_tags_exists():
 pass

def test_bump_existing_version_number():
 pass

def test_wrong_version_spec_found():
 pass
