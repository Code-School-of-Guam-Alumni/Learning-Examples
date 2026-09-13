#!/usr/bin/env python3
"""Build the complete alumni and Lance reference-code catalogs."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = Path("/tmp/csg-reference-code.w8L58P/sources/csg2")
CORE_COMMIT = "afbe99cc129a2f6604be678c39968ba1632edbe4"
LEARNING_BASE = "https://github.com/Code-School-of-Guam-Alumni/Learning-Examples"
CSG2_BASE = "https://github.com/CSG-Live-July-2025"
ORGANIZER_BASE = "https://github.com/Code-School-of-Guam-Cohort-3/organizer_api"
RESOURCES_BASE = "https://github.com/Code-School-of-Guam-Alumni/Resources/tree/main"


def full_rev(repo: str, rev: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(SOURCES / repo), "rev-parse", rev], text=True
    ).strip()


def source_tree(repo: str, rev: str, label: str) -> dict[str, str]:
    commit = full_rev(repo, rev)
    return {
        "label": label,
        "url": f"{CSG2_BASE}/{repo}/tree/{commit}",
        "kind": "original classroom code",
    }


def source_compare(repo: str, start: str, complete: str, label: str) -> dict[str, str]:
    start_commit = full_rev(repo, start)
    complete_commit = full_rev(repo, complete)
    return {
        "label": label,
        "url": f"{CSG2_BASE}/{repo}/compare/{start_commit}...{complete_commit}",
        "kind": "original classroom change",
    }


def reconstructed(path: str, label: str) -> dict[str, str]:
    return {
        "label": label,
        "url": f"{LEARNING_BASE}/tree/{CORE_COMMIT}/{path}",
        "kind": "reconstructed current reference",
    }


def organizer_compare(start: str, complete: str, label: str) -> dict[str, str]:
    return {
        "label": label,
        "url": f"{ORGANIZER_BASE}/compare/{start}...{complete}",
        "kind": "Lance classroom change",
    }


def guide(path: str, label: str) -> dict[str, str]:
    return {
        "label": label,
        "url": f"{RESOURCES_BASE}/{path}",
        "kind": "current guide",
    }


RUBY_FUNDAMENTALS = reconstructed("ruby/fundamentals", "Ruby fundamentals reference")
RUBY_OOP = reconstructed("ruby/oop", "Ruby OOP and persistence reference")
JS_FUNDAMENTALS = reconstructed("javascript/fundamentals", "JavaScript fundamentals reference")
PYTHON_FUNDAMENTALS = reconstructed("python-fastapi/fundamentals", "Python fundamentals reference")
PUNDIT_REFERENCE = reconstructed("rails/authorization/pundit", "Pundit authorization reference")
BACKGROUND_JOBS = reconstructed("rails/background-jobs", "Namespacing and background-jobs reference")
REACT_AUTH = reconstructed("react/authentication", "React authentication reference")
ONE_TO_MANY = reconstructed("rails/associations/one-to-many", "One-to-many associations reference")


def result(status: str, reason: str, *references: dict[str, str]) -> dict[str, object]:
    return {"status": status, "reason": reason, "references": list(references)}


def alumni_reference(item: dict[str, object]) -> dict[str, object]:
    title = str(item["title"])
    lower = title.lower()
    module = str(item["module"])

    if module == "Start Here and What's New":
        if "github" in lower or "repo" in lower:
            return result(
                "classroom",
                "The repository itself is the completed artifact for the Git/GitHub workflow.",
                source_tree("github-practice", "751ff6b", "Git and GitHub classroom repository"),
                guide("web-development/02-git-github", "Current Git and GitHub guides"),
            )
        if "development environment" in lower or "vs code" in lower or "computer setup" in lower:
            return result(
                "guide",
                "This setup lesson produces a configured computer rather than application code.",
                guide("web-development/01-setup", "Current development setup guides"),
            )
        return result(
            "not-applicable",
            "This orientation or internship-onboarding recording does not produce a reusable code state.",
        )

    if module == "Ruby and Programming Fundamentals":
        if any(word in lower for word in ("object-oriented", "oop", "inheritance", "module", "mixin", "file i/o", "persistent", "abstraction", "encapsulation", "error handling", "rspec")):
            refs = [RUBY_OOP]
            if "error" in lower:
                refs.append(source_tree("week-3", "5e0d750", "Error-handling classroom checkpoint"))
            elif "module" in lower or "mixin" in lower:
                refs.append(source_compare("week-3", "8f4e532", "10d7b65", "Modules-to-mixins classroom change"))
            elif "rspec" in lower:
                refs.append(source_tree("week-3", "9306751", "OOP and RSpec classroom checkpoint"))
            else:
                refs.append(source_tree("week-3", "e6d0430", "OOP classroom checkpoint"))
            return result("classroom+reconstructed", "The exact classroom checkpoint is paired with a small current runnable example.", *refs)
        source = source_tree("week-1", "295f858", "Week 1 Ruby classroom code")
        if any(word in lower for word in ("hash", "nested", "catalog", "shopping", "cli")):
            source = source_tree("week-2", "582998d", "Week 2 Ruby classroom code")
        if "deliberate practice" in lower or "functions" in lower:
            source = source_tree("weeks", "c14946d", "Combined Ruby practice checkpoint")
        if "git and github" in lower:
            source = source_tree("github-practice", "751ff6b", "Git and GitHub classroom repository")
        return result("classroom+reconstructed", "The preserved class files are paired with a concise runnable current reference.", source, RUBY_FUNDAMENTALS)

    if module == "Rails APIs and Databases":
        if title == "Ruby File I/O, API Requests, and Rails Introduction":
            return result("classroom+reconstructed", "The recording bridges Ruby persistence into a newly generated Rails API.", RUBY_OOP, source_tree("shoes_api", "ec237d0", "Rails API starting checkpoint"))
        if title == "Rails Controllers, Routes, and Models":
            return result("classroom", "This comparison contains the model, controller, routes, and five CRUD actions.", source_compare("shoes_api", "ec237d0", "c03cb1c", "Shoes API CRUD progression"))
        if title == "Models, Migrations, and Rails Console CRUD":
            return result("classroom", "This comparison adds the model and schema before controller work.", source_compare("cookbook_api", "26f4290", "6b9083f", "Recipe model and migration"))
        if title == "Complete CRUD Implementation in Rails APIs":
            return result("classroom", "This is the complete recipe CRUD change from a generated API.", source_compare("cookbook_api", "26f4290", "e8bf8db", "Cookbook API complete CRUD"))
        if title == "Building a Rails API: CRUD Operations":
            return result("classroom", "This compact repository preserves the model and all five controller actions.", source_compare("animals_api", "44fdb1c", "0500612", "Animals API CRUD progression"))
        if title == "Building Rails APIs from Scratch and CRUD Implementation":
            return result("classroom", "This second complete CRUD example supports independent comparison.", source_compare("computer_api", "b750823", "dd2104d", "Computers API CRUD progression"))
        if title == "Building a CRUD API and Validations":
            return result("classroom", "The comparison adds CRUD, migrations, validation, and intentional error handling.", source_compare("store_api", "248402b", "d7d8a77", "Store API through validations"))
        if title == "Validations and Migrations":
            return result("classroom", "This classroom range isolates the table changes and model validation work.", source_compare("store_api", "e0a249f", "d7d8a77", "Store API migrations and validations"))
        if title == "Migrations and Associations":
            return result("classroom", "This range adds related tables, a foreign key, and Rails model relationships.", source_compare("store_api", "d7d8a77", "802e08a", "Store API one-to-many change"), ONE_TO_MANY)
        if title == "Model One-to-Many Relationships in Rails":
            return result("classroom+reconstructed", "The focused reference uses Lance's exact before/after class commits and a current migration note.", ONE_TO_MANY, organizer_compare("824b9035b34ac901adf1cec952aaa60c54c06e92", "fe0826187beb467865d28e4b3bc8c5d4fc96fb6e", "Organizer API association change"))
        if title == "Database Seeding and Faker":
            return result("classroom", "This comparison adds repeatable Faker-backed seeds to the evolving Store API.", source_compare("store_api", "802e08a", "ba40cb3", "Faker and seed-data change"))
        if title == "Active Model Serializers and Group Integration":
            return result("classroom", "This comparison adds the serializer to the existing API.", source_compare("store_api", "ba40cb3", "ca84cc9", "Product serializer change"))
        if title == "Rails Validations, Serializers, and Callbacks":
            return result("classroom", "This completed state preserves validations, serialization, and callback examples together.", source_compare("store_api", "ca84cc9", "6629164", "Serializer-to-callback change"))
        if title == "Many-to-Many Associations and Join Tables":
            return result("classroom", "This repository preserves the posts/authors join-table collaboration.", source_compare("many_to_many_blog_api", "2eadc38", "eaa4328", "Many-to-many classroom progression"))
        if "jwt authentication" in lower or "password hashing" in lower:
            return result("classroom", "This progression adds bcrypt, users, signup, login, and JWT issuance.", source_compare("auth-practice-api", "844c6a1", "2dfb177", "Authentication and JWT progression"))
        if title == "Active Record Queries and Scopes":
            return result("classroom", "This classroom repository contains the query and scope practice state.", source_tree("active_record_practice_api", "3baae52", "Active Record query and scope checkpoint"))
        if "pundit" in lower or "authorization" in lower:
            return result("reconstructed", "No safe exact Pundit snapshot survived, so the lesson points to a focused current policy implementation.", PUNDIT_REFERENCE)
        if "namespacing" in lower or "background jobs" in lower:
            return result("classroom+reconstructed", "The exact namespace change is paired with a current background-job boundary.", source_compare("namespace-background-job-api", "002fcef", "9cba85c", "API namespace classroom change"), BACKGROUND_JOBS)
        if "full-stack rails" in lower or "tailwind" in lower:
            return result("classroom", "This comparison adds the full-stack product flow and Tailwind styling.", source_compare("full-stack-app", "aea7024", "be1131f", "Full-stack Rails and Tailwind progression"))
        if "presentation" in lower:
            return result("showcase", "The recording reviews completed student work; these clean class applications are the inspectable reference states.", source_tree("cookbook-backend", "aeaa6d1", "Cookbook backend completed state"), source_tree("cookbook-frontend", "2e07a02", "Cookbook frontend completed state"))
        if "planning" in lower or "mvp" in lower:
            return result("not-applicable", "This lesson produces a scoped plan, schema, user stories, and backlog rather than a shared completed code solution.")

    if module == "JavaScript":
        return result("classroom+reconstructed", "A clean executable fundamentals example is paired with the immutable classroom tooling repository.", JS_FUNDAMENTALS, source_tree("modern-js", "b13bb02", "Modern JavaScript classroom checkpoint"))

    if module == "React and Full-Stack Integration":
        if "vite setup" in lower:
            return result("classroom", "The initial React commit preserves the generated Vite application and first page structure.", source_tree("cookbook-frontend", "8068ee1", "React/Vite starting checkpoint"))
        if "components" in lower or "dynamic rendering" in lower:
            return result("classroom", "This range adds reusable components, props, and state practice.", source_compare("cookbook-frontend", "8068ee1", "8ea3d59", "React components, props, and state progression"))
        if "load api data" in lower:
            return result("classroom", "This comparison adds Axios, useState, useEffect, and collection rendering.", source_compare("cookbook-frontend", "8068ee1", "8bce207", "React API loading change"))
        if "show modal" in lower or "component organization" in lower:
            return result("classroom", "This range adds the show action, modal, and focused show component.", source_compare("cookbook-frontend", "8ea3d59", "48d95ed", "React show-modal progression"))
        if "show and create" in lower or "create action" in lower:
            return result("classroom", "This comparison adds the controlled create form and API mutation.", source_compare("cookbook-frontend", "48d95ed", "d5e5bdd", "React create action"))
        if "create, update, and destroy" in lower or "crud" in lower:
            return result("classroom", "This range preserves the completed React CRUD progression.", source_compare("cookbook-frontend", "48d95ed", "2e07a02", "React CRUD progression"))
        if "cors" in lower:
            return result("classroom", "The backend CORS checkpoint and completed frontend show the two sides of the browser boundary.", source_tree("cookbook-backend", "0f79129", "Rails CORS checkpoint"), source_tree("cookbook-frontend", "2e07a02", "Completed React client"))
        return result("classroom", "The completed frontend and backend provide a full application for tracing setup and data flow.", source_tree("cookbook-frontend", "2e07a02", "Completed React client"), source_tree("cookbook-backend", "aeaa6d1", "Completed Rails API"))

    if module == "Python and FastAPI":
        return result("reconstructed", "No exact standalone fundamentals repository survived, so this lesson uses a verified standard-library reference.", PYTHON_FUNDAMENTALS, guide("AI-Engineering", "Current Python and FastAPI guides"))

    if module == "AI Engineering":
        if "introduction" in lower or "basic chatbot" in lower:
            return result("classroom", "The first chatbot commit preserves the initial model call and application structure.", source_tree("spam-bots-chatbot", "5c89b62", "Initial AI/chatbot classroom checkpoint"))
        return result("classroom", "This complete commit range preserves multi-turn memory, system prompts, FastAPI, and longer-context work.", source_compare("spam-bots-chatbot", "5c89b62", "32f6041", "Chatbot and FastAPI progression"))

    if module == "Testing and Deployment":
        if "factory bot" in lower:
            return result("classroom", "This comparison adds RSpec, Factory Bot, factories, and model tests.", source_compare("rspec_demo", "abda922", "cab46ea", "RSpec and Factory Bot setup"))
        if "request specs" in lower:
            return result("classroom", "This comparison adds controller behavior and request specs.", source_compare("rspec_demo", "cab46ea", "e64d125", "RSpec request-spec progression"))
        if "rspec" in lower or "automated testing" in lower:
            return result("classroom", "This range preserves the initial automated-test setup and first passing examples.", source_compare("rspec_demo", "2020a7e", "cab46ea", "RSpec introduction progression"))
        if "git workflow" in lower or "collaboration" in lower:
            return result("classroom", "The pull-request history is the artifact for this collaboration lesson.", source_compare("collab_api", "3477130", "670dc12", "Collaborative Git and pull-request history"))
        if "deploy" in lower:
            return result("classroom", "The completed frontend and backend preserve the production-oriented configuration discussed in class.", source_tree("cookbook-backend", "aeaa6d1", "Deployment-ready Rails API"), source_tree("cookbook-frontend", "2e07a02", "Deployment-ready React client"), guide("web-development/05-deployment", "Current deployment guides"))
        if "mini capstone" in lower:
            return result("showcase", "The lesson is planning-oriented; the completed application pair is available for architecture comparison.", source_tree("cookbook-backend", "aeaa6d1", "Completed Rails API"), source_tree("cookbook-frontend", "2e07a02", "Completed React client"))

    if module == "Professional Development":
        if "capstone presentations" in lower:
            return result("showcase", "The presentation is the primary artifact; the final chatbot repository is available for technical inspection.", source_tree("spam-bots-chatbot", "32f6041", "Spam Bots completed chatbot code"))
        if "technical interview" in lower or "data structures" in lower or "leetcode" in lower:
            return result("practice-reference", "Interview exercises can have many valid solutions; these executable fundamentals references provide code to trace and discuss rather than a single answer to memorize.", RUBY_FUNDAMENTALS, JS_FUNDAMENTALS, guide("web-development/supplemental", "Current supplemental practice resources"))
        return result("not-applicable", "This career, interview, reflection, planning, or presentation-preparation lesson does not have one canonical completed code solution.")

    return result("not-applicable", "No reusable code artifact applies to this lesson.")


def lance_reference(item: dict[str, object]) -> dict[str, object]:
    title = str(item["title"])
    lower = title.lower()

    if any(word in lower for word in ("zoom live class recording", "catch up day", "starting our mini capstones", "working on your mini capstone", "submit your mini capstone", "reflection", "reconfirm the organizer mvp", "lock the final scope", "production qa matrix", "portfolio entry", "final demo and handoff")):
        return result("not-applicable", "This is a session container, learner-owned project milestone, review, or delivery checklist rather than a shared answer key.")
    if "terminal" in lower or "course setup" in lower:
        return result("guide", "The output is a working development environment rather than application code.", guide("web-development/01-setup", "Current development setup guides"))
    if "javascript" in lower or "html" in lower or "loop through" in lower or "make decisions" in lower or "decomposition with task data" in lower or "asynchronous javascript" in lower:
        return result("reconstructed", "Use the executable fundamentals and async example after attempting the exercise.", JS_FUNDAMENTALS)
    if "ruby" in lower or "task tracker cli" in lower or "data structures" in lower:
        return result("reconstructed", "Use the concise runnable reference after attempting the exercise.", RUBY_FUNDAMENTALS, RUBY_OOP)
    if "database intro" in lower or "mvc" in lower:
        return result("classroom", "A completed Rails API provides an inspectable model/controller/database boundary.", source_compare("cookbook_api", "26f4290", "e8bf8db", "Cookbook API MVC and CRUD progression"))
    if "intro to rails" in lower or "breakdown of the week 2" in lower:
        return result("classroom", "This progression shows the generated API, model, controller, routes, and CRUD endpoints.", source_compare("shoes_api", "ec237d0", "c03cb1c", "Rails API introduction progression"))
    if "creating a new rails api" in lower:
        return result("classroom", "This progression starts from the generated application and ends with a working model and CRUD boundary.", source_compare("shoes_api", "ec237d0", "c03cb1c", "Rails API start-to-finish reference"))
    if "rails console" in lower or title == "Creating a Model" or "models" in lower or "model methods" in lower:
        return result("classroom", "This checkpoint exposes the model and database state for console practice.", source_compare("cookbook_api", "26f4290", "6b9083f", "Rails model and migration change"))
    if "controller" in lower or "routes" in lower or "crud actions in rails api" in lower or "crud functionality" in lower or "crud -" in lower or "happy and sad" in lower or "happy/sad" in lower or "create data in your rails api" in lower:
        return result("classroom", "This completed CRUD range supports tracing each request and response path.", source_compare("animals_api", "44fdb1c", "0500612", "Rails CRUD reference"))
    if "seeding" in lower or "seed database" in lower:
        return result("classroom", "This exact classroom change adds repeatable seed data.", source_compare("store_api", "802e08a", "ba40cb3", "Faker and seed-data change"))
    if "migration" in lower:
        return result("classroom", "This range demonstrates changing an existing table through migrations.", source_compare("store_api", "e0a249f", "a18b7df", "Store API migration changes"))
    if "validation" in lower:
        return result("classroom", "This range adds model validations and intentional 422 error handling.", source_compare("store_api", "a18b7df", "d7d8a77", "Store API validation change"))
    if "many-to-many" in lower:
        return result("classroom", "This exact repository history preserves the join-table and association work.", source_compare("many_to_many_blog_api", "2eadc38", "eaa4328", "Many-to-many reference"))
    if "association" in lower or "foreign key" in lower or "associating pre-existing" in lower:
        return result("classroom+reconstructed", "Compare Lance's exact class change with the focused associations reference.", ONE_TO_MANY, organizer_compare("824b9035b34ac901adf1cec952aaa60c54c06e92", "fe0826187beb467865d28e4b3bc8c5d4fc96fb6e", "Lance's association change"))
    if "serializer" in lower or "serialize relationships" in lower:
        return result("classroom", "This classroom comparison adds a serializer to an established API.", source_compare("store_api", "ba40cb3", "ca84cc9", "Product serializer change"))
    if "integrated rails api" in lower or "backend acceptance" in lower or "demo and document the backend" in lower:
        return result("classroom", "The completed classroom API is a comparison target; Lance's own Organizer API remains the assignment.", source_tree("cookbook-backend", "aeaa6d1", "Completed Rails API reference"))
    if (
        "secure user passwords" in lower
        or ("signup" in lower and "frontend" not in lower)
        or ("login" in lower and "frontend" not in lower)
        or "protect task endpoints" in lower
        or "scope data" in lower
    ):
        return result("classroom", "This range adds bcrypt, signup, login, JWT issuance, request authorization, and user-owned records.", source_compare("auth-practice-api", "844c6a1", "8e647ac", "Rails authentication and ownership progression"))
    if "pundit" in lower or "policy-based authorization" in lower:
        return result("reconstructed", "Use the focused policy, controller, and policy-spec files after attempting the task.", PUNDIT_REFERENCE)
    if "api/v1" in lower or "background jobs" in lower:
        return result("classroom+reconstructed", "The namespace history is paired with the current job/controller boundary.", source_compare("namespace-background-job-api", "002fcef", "9cba85c", "API namespace change"), BACKGROUND_JOBS)
    if "create the organizer react client" in lower or "split the interface" in lower or "props" in lower:
        return result("classroom", "This range preserves Vite setup, components, props, and state practice.", source_compare("cookbook-frontend", "8068ee1", "8ea3d59", "React foundation progression"))
    if "load tasks" in lower:
        return result("classroom", "This exact comparison adds Axios, state, effects, and collection rendering.", source_compare("cookbook-frontend", "8068ee1", "8bce207", "React API-loading change"))
    if "detail modal" in lower:
        return result("classroom", "This range adds a show action, modal, and focused detail component.", source_compare("cookbook-frontend", "8ea3d59", "48d95ed", "React show-modal progression"))
    if "create tasks from react" in lower:
        return result("classroom", "This comparison adds the create form and API mutation.", source_compare("cookbook-frontend", "48d95ed", "d5e5bdd", "React create action"))
    if "update tasks" in lower:
        return result("classroom", "This comparison isolates the update flow.", source_compare("cookbook-frontend", "d5e5bdd", "32c14f0", "React update action"))
    if "delete tasks" in lower or "crud acceptance" in lower or "crud flow" in lower:
        return result("classroom", "This completed range contains create, update, and delete behavior.", source_compare("cookbook-frontend", "48d95ed", "2e07a02", "Completed React CRUD progression"))
    if "frontend signup" in lower or "restore sessions" in lower or "protect the interface" in lower:
        return result("reconstructed", "Use the focused session-context and protected-route files after attempting the integration.", REACT_AUTH, source_tree("cookbook-backend", "549b707", "Authenticated Rails API checkpoint"))
    if "deploy the rails" in lower:
        return result("classroom", "The completed API preserves the configuration used for deployment practice.", source_tree("cookbook-backend", "aeaa6d1", "Deployment-ready Rails API"), guide("web-development/05-deployment", "Current deployment guides"))
    if "deploy the react" in lower:
        return result("classroom", "The completed client and API preserve the production integration boundary.", source_tree("cookbook-frontend", "2e07a02", "Deployment-ready React client"), source_tree("cookbook-backend", "aeaa6d1", "Deployment-ready Rails API"), guide("web-development/05-deployment", "Current deployment guides"))
    if "cors" in lower:
        return result("classroom", "Compare the backend CORS checkpoint with the completed client.", source_tree("cookbook-backend", "0f79129", "Rails CORS checkpoint"), source_tree("cookbook-frontend", "2e07a02", "Completed React client"))
    if "presentation and accessibility" in lower:
        return result("showcase", "There is no single visual answer key; use the completed client as an inspectable baseline, then improve it without copying its design.", source_tree("cookbook-frontend", "2e07a02", "Completed React client baseline"))
    if "creating basic rails api" in lower or "contacts_api answer key" in lower:
        return result("classroom", "The original answer-key repository is preserved at the exact reviewed commit.", {"label": "Contacts API answer key", "url": "https://github.com/CruzAlanna/contacts_api/tree/b13d2653756e7d1ac1d53b5142f47dd613f42deb", "kind": "original answer key"})

    return result("not-applicable", "This lesson is learner-owned planning, review, or delivery work and does not have one canonical shared answer key.")


def refs_markdown(references: list[dict[str, str]]) -> str:
    if not references:
        return "—"
    return "<br>".join(f'[{ref["label"]}]({ref["url"]})' for ref in references)


def build_alumni(items: list[dict[str, object]]) -> tuple[str, list[dict[str, object]]]:
    enriched = []
    lines = [
        "# Complete Alumni Recording and Reference-Code Catalog",
        "",
        "Every one of the 79 Cohort 2 archive lessons is accounted for below. Code-producing lessons point to exact immutable classroom commits, a reconstructed current example, or both. Non-code lessons are marked explicitly instead of receiving a misleading generic repository link.",
        "",
        "Alumni may inspect completed code immediately. Current students should attempt the exercise before opening the completed state.",
        "",
    ]
    for module in dict.fromkeys(str(item["module"]) for item in items):
        lines.extend([f"## {module}", ""])
        for item in [row for row in items if row["module"] == module]:
            mapped = alumni_reference(item)
            record = {**item, **mapped}
            enriched.append(record)
            lines.extend([
                f'<a id="alumni-lesson-{item["lesson_id"]}"></a>',
                f'### {item["title"]}',
                "",
                f'- Production: [lesson {item["lesson_id"]}](https://learn.codeschoolofguam.com/lessons/{item["lesson_id"]})',
                f'- Recording: [{item["video_title"]}]({item["video_url"]})',
                f'- Reference status: `{mapped["status"]}`',
                f'- Why: {mapped["reason"]}',
                f'- Reference: {refs_markdown(mapped["references"])}',
                "",
            ])
    return "\n".join(lines), enriched


def build_lance(items: list[dict[str, object]]) -> tuple[str, list[dict[str, object]]]:
    enriched = []
    lines = [
        "# Lance Live-Class Reference Map",
        "",
        "This map accounts for all 106 Live Class lessons in Lance's curriculum. A code-producing lesson points to an exact classroom change or a focused reconstructed reference. Session containers, catch-up days, learner-owned capstone milestones, and delivery checklists are marked `not-applicable` rather than pretending that a shared answer key exists.",
        "",
        "Lance should attempt each exercise in his own Organizer project before opening a completed reference.",
        "",
    ]
    for item in items:
        mapped = lance_reference(item)
        record = {**item, **mapped}
        enriched.append(record)
        lines.extend([
            f'<a id="lance-lesson-{item["id"]}"></a>',
            f'## {item["id"]}: {item["title"]}',
            "",
            f'- Production: [lesson {item["id"]}](https://learn.codeschoolofguam.com/lessons/{item["id"]})',
            f'- Required for Lance: `{str(item["required"]).lower()}`',
            f'- Reference status: `{mapped["status"]}`',
            f'- Why: {mapped["reason"]}',
            f'- Reference: {refs_markdown(mapped["references"])}',
            "",
        ])
    return "\n".join(lines), enriched


def validate(records: list[dict[str, object]], expected: int, id_key: str) -> None:
    assert len(records) == expected
    assert len({record[id_key] for record in records}) == expected
    assert all(record["status"] for record in records)
    assert all(record["reason"] for record in records)
    assert all(record["references"] or record["status"] == "not-applicable" for record in records)
    for record in records:
        for reference in record["references"]:
            assert reference["url"].startswith("https://")
            assert reference["label"]


def main() -> None:
    alumni = json.loads((ROOT / "data/alumni-archive-lessons.json").read_text())
    lance = json.loads((ROOT / "data/lance-live-lessons.json").read_text())
    alumni_markdown, alumni_records = build_alumni(alumni)
    lance_markdown, lance_records = build_lance(lance)
    validate(alumni_records, 79, "lesson_id")
    validate(lance_records, 106, "id")

    (ROOT / "CATALOG.md").write_text(alumni_markdown.rstrip() + "\n")
    (ROOT / "LANCE.md").write_text(lance_markdown.rstrip() + "\n")
    (ROOT / "data/reference-map.json").write_text(json.dumps({
        "alumni": alumni_records,
        "lance": lance_records,
    }, indent=2) + "\n")

    print(json.dumps({
        "alumni": {
            "total": len(alumni_records),
            "with_references": sum(bool(item["references"]) for item in alumni_records),
            "not_applicable": sum(item["status"] == "not-applicable" for item in alumni_records),
        },
        "lance": {
            "total": len(lance_records),
            "with_references": sum(bool(item["references"]) for item in lance_records),
            "not_applicable": sum(item["status"] == "not-applicable" for item in lance_records),
        },
    }, indent=2))


if __name__ == "__main__":
    main()
