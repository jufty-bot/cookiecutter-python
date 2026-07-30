"""Verify that Copier renders the expected Python project."""

from pathlib import Path

import pytest
from copier import run_copy


@pytest.fixture
def rendered_project(tmp_path: Path) -> Path:
    """Render the template with the answers used by the example project."""
    template_root = Path(__file__).parent.parent
    project_root = tmp_path / "example-project"
    run_copy(
        src_path=str(template_root),
        dst_path=project_root,
        data={
            "build_docker_image": True,
            "publish_to_pypi": True,
            "publish_to_docker_hub": True,
        },
        defaults=True,
        overwrite=True,
        vcs_ref="HEAD",
    )
    return project_root


def test_copier_renders_expected_project(rendered_project: Path) -> None:
    """Keep the generated example project synchronized with the template."""
    expected_project = Path(__file__).parent / "example-project"
    generated_files = {
        path.relative_to(rendered_project)
        for path in rendered_project.rglob("*")
        if path.is_file() and path.name != ".copier-answers.yml"
    }
    expected_files = {
        path.relative_to(expected_project)
        for path in expected_project.rglob("*")
        if path.is_file() and path.name != ".copier-answers.yml"
    }

    assert generated_files == expected_files
    for relative_path in generated_files:
        assert (rendered_project / relative_path).read_text() == (
            expected_project / relative_path
        ).read_text()


def test_copier_records_answers(rendered_project: Path) -> None:
    """Ensure generated projects retain the metadata required for updates."""
    answers = (rendered_project / ".copier-answers.yml").read_text()

    assert "_commit:" in answers
    assert "_src_path:" in answers
    assert "project_slug: example_project" in answers


def test_copier_omits_disabled_optional_files(tmp_path: Path) -> None:
    """Preserve the optional-file behavior previously handled by hooks."""
    project_root = tmp_path / "minimal-project"
    run_copy(
        src_path=str(Path(__file__).parent.parent),
        dst_path=project_root,
        data={
            "build_docker_image": False,
            "publish_to_pypi": False,
            "publish_to_docker_hub": False,
            "license": "UNLICENSED",
        },
        defaults=True,
        overwrite=True,
        vcs_ref="HEAD",
    )

    assert not (project_root / "Dockerfile").exists()
    assert not (project_root / "LICENSE").exists()
    assert not (project_root / ".github/workflows/docker.yaml").exists()
    assert not (project_root / ".github/workflows/publish.yaml").exists()
