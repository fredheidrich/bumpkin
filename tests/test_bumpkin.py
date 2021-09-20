
import os

import pytest

from bumpkin import bumpkin


def test_changelog_generation():

	datestr = "2021-09-18"
	prev_version = "2021.9"
	new_version = "2021.9.1"
	repo_name = "foo/bar"
	changes_pivoted = {}
	is_first_release = True

	result = bumpkin.generate_changelog_content(datestr, prev_version, new_version, repo_name, changes_pivoted, is_first_release)

	assert result


def test_changelog_extraction():

	is_first_release = False
	release_version = "2021.9"
	changelog_path = "FILE_THAT_DOES_NOT_EXIST.foo"

	result = bumpkin.extract_existing_changelog_content(changelog_path, release_version, is_first_release)
	assert result[0] == False


NON_CHANGELOG_FILE_PATH = "TESTFILE_THAT_DOES_EXIST.md"


@pytest.fixture
def old_non_changelog_file():

	# arrange
	string = "foo bar baz"
	with open(NON_CHANGELOG_FILE_PATH, "w") as testfile:
		testfile.write(string)

	yield	string

	# cleanup
	os.remove(NON_CHANGELOG_FILE_PATH)

FAKE_HEADER = (
"""# Changelog

[Unreleased]
* foo
* bar
* baz
"""
)
FAKE_BODY = (
"""<a name='2021.9'></a>## [2021.9]

### Additions
* foobar

"""
)

@pytest.fixture
def old_fake_changelog_file():

	string = FAKE_HEADER + FAKE_BODY

	# arrange
	with open(NON_CHANGELOG_FILE_PATH, "w") as testfile:
		testfile.write(string)

	yield	string

	# cleanup
	os.remove(NON_CHANGELOG_FILE_PATH)


def test_add_to_existing_invalid_changelog(old_non_changelog_file):
	is_first_release = True
	release_version = "2021.9"
	result = bumpkin.extract_existing_changelog_content(NON_CHANGELOG_FILE_PATH, release_version, is_first_release)
	assert result[0] == True
	assert result[1] == "foo bar baz"
	

def test_add_to_existing_changelog(old_fake_changelog_file):
	is_first_release = True
	release_version = "2021.9"
	result = bumpkin.extract_existing_changelog_content(NON_CHANGELOG_FILE_PATH, release_version, is_first_release)
	assert result[0] == True
	assert result[1] == FAKE_HEADER
	assert result[2] == FAKE_BODY


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